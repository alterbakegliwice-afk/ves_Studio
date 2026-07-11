#!/usr/bin/env python3
"""Semantic policy validation (beyond structural checks).

Covers:
- runtime eligibility: composition compiles only ACTIVE (or explicit exceptions),
- decision sync: a decision pending external sync is excluded from runtime and
  its structured metadata agrees with its prose,
- status coherence: manifest carries repository/release/runtime status and does
  not contradict STATUS.md or the runtime index,
- source accounting: every ACTIVE + canonical source is compiled or explicitly
  excluded,
- version single-source: the builder derives the runtime version from the
  manifest (no hard-coded RUNTIME_VERSION constant),
- composition data validates against its schema.

Exit 0 on success, 1 on any error.
"""
from __future__ import annotations

import os
import re
import sys

import vlib
from vlib import REPO_ROOT


def runtime_eligibility_errors(by_id, comp) -> list:
    """Composition may compile only default_allowed_status (or listed exceptions)."""
    allowed = set(comp.get("default_allowed_status", ["ACTIVE"]))
    exceptions = {e["id"] for e in comp.get("exceptions", [])}
    errors = []
    for t in comp["targets"]:
        for sid in t["sources"]:
            s = by_id.get(sid)
            if s is None:
                errors.append(f"unknown source id {sid}")
            elif s.status not in allowed and sid not in exceptions:
                errors.append(f"{sid} status {s.status} compiled without exception "
                              f"(allowed={sorted(allowed)})")
    return errors


def source_accounting_errors(by_id, comp) -> list:
    """Every ACTIVE + canonical source must be compiled or explicitly excluded."""
    compiled = {sid for t in comp["targets"] for sid in t["sources"]}
    excluded = {e["id"] for e in comp.get("exclusions", [])}
    errors = []
    for s in by_id.values():
        if s.status == "ACTIVE" and s.meta.get("canonical") is True:
            if s.sid not in compiled and s.sid not in excluded:
                errors.append(f"ACTIVE canonical {s.sid} is neither compiled nor "
                              f"explicitly excluded")
    return errors


def main() -> int:
    errors: list[str] = []
    manifest = vlib.manifest()
    comp = vlib.composition()
    by_id = vlib.sources_by_id()
    allowed = set(comp.get("default_allowed_status", ["ACTIVE"]))
    exceptions = {e["id"] for e in comp.get("exceptions", [])}

    for e in vlib.schema_errors(comp, "runtime_composition.schema.json"):
        errors.append(f"RUNTIME_COMPOSITION schema: {e}")

    compiled_ids = {sid for t in comp["targets"] for sid in t["sources"]}
    errors += [f"runtime eligibility: {e}" for e in runtime_eligibility_errors(by_id, comp)]

    # decision sync policy
    for s in by_id.values():
        if s.meta.get("source_type") == "decision":
            sync = s.meta.get("external_sync_status")
            if sync and sync != "SYNCED" and s.sid in compiled_ids:
                errors.append(f"decision sync: {s.sid} has external_sync_status "
                              f"{sync} but is compiled into runtime")
            # prose/metadata consistency
            body_pending = bool(re.search(r"PENDING[_ ]?(SOURCE[_ ])?SYNC", s.body, re.I))
            if body_pending and sync != "PENDING":
                errors.append(f"decision sync: {s.sid} prose says pending sync but "
                              f"external_sync_status={sync}")

    # status coherence
    for field in ("repository_status", "release_status", "runtime_status"):
        if field not in manifest:
            errors.append(f"status coherence: manifest missing {field}")
    status_md = os.path.join(REPO_ROOT, "STATUS.md")
    if os.path.isfile(status_md):
        txt = open(status_md, encoding="utf-8").read()
        label = manifest.get("release_status", "")
        if label and label not in txt and "Core Beta" not in txt:
            errors.append("status coherence: STATUS.md does not reflect release status "
                          f"'{label}'")
    idx = os.path.join(vlib.RUNTIME_DIR, "00_RUNTIME_INDEX.md")
    if os.path.isfile(idx):
        itxt = open(idx, encoding="utf-8").read()
        rs = manifest.get("runtime_status", "")
        if rs and rs not in itxt:
            errors.append(f"status coherence: runtime index missing runtime_status '{rs}'")

    # source accounting: every ACTIVE + canonical accounted for
    errors += [f"source accounting: {e}" for e in source_accounting_errors(by_id, comp)]

    # version single-source: no hard-coded RUNTIME_VERSION constant
    build_src = open(os.path.join(REPO_ROOT, "scripts", "build_runtime_pack.py"),
                     encoding="utf-8").read()
    if re.search(r"^\s*RUNTIME_VERSION\s*=", build_src, re.M):
        errors.append("version single-source: build_runtime_pack.py still defines a "
                      "hard-coded RUNTIME_VERSION constant")

    print("validate_policies: eligibility, decision sync, status, accounting, version")
    if errors:
        print(f"\nFAILED with {len(errors)} error(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("validate_policies: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
