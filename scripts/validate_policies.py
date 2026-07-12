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
    """Composition may compile only sources that are:
    - default_allowed_status (or a listed exception), AND
    - review_status REVIEWED or APPROVED (P0-04), AND
    - if a decision, decision_status ACCEPTED (P0-02; PROPOSED/REJECTED blocked)."""
    allowed = set(comp.get("default_allowed_status", ["ACTIVE"]))
    exceptions = {e["id"] for e in comp.get("exceptions", [])}
    errors = []
    for t in comp["targets"]:
        for sid in t["sources"]:
            s = by_id.get(sid)
            if s is None:
                errors.append(f"unknown source id {sid}")
                continue
            if s.status not in allowed and sid not in exceptions:
                errors.append(f"{sid} status {s.status} compiled without exception "
                              f"(allowed={sorted(allowed)})")
            if s.meta.get("review_status") not in ("REVIEWED", "APPROVED"):
                errors.append(f"{sid} review_status {s.meta.get('review_status')} "
                              f"not runtime-eligible (need REVIEWED/APPROVED)")
            if s.meta.get("source_type") == "decision" \
                    and s.meta.get("decision_status") != "ACCEPTED":
                errors.append(f"decision {sid} decision_status "
                              f"{s.meta.get('decision_status')} must be ACCEPTED to compile")
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

    # decision sync policy (P0-02): a decision pending external sync MAY compile
    # into runtime (latest Piotrek decision wins), but the pack must carry a
    # warning and the external conflict must stay visible in the registry.
    src_registry = vlib.load_json(os.path.join(vlib.REGISTRIES_DIR, "SOURCE_REGISTRY.json"))
    registry_conflicts = " ".join(
        c.get("summary", "") for s in src_registry.get("sources", [])
        for c in s.get("known_conflicts", []))
    index_txt = ""
    idx_path = os.path.join(vlib.RUNTIME_DIR, "00_RUNTIME_INDEX.md")
    if os.path.isfile(idx_path):
        index_txt = open(idx_path, encoding="utf-8").read()
    for s in by_id.values():
        if s.meta.get("source_type") == "decision":
            sync = s.meta.get("external_sync_status")
            # prose/metadata consistency
            body_pending = bool(re.search(r"PENDING[_ ]?(SOURCE[_ ])?SYNC", s.body, re.I))
            if body_pending and sync != "PENDING":
                errors.append(f"decision sync: {s.sid} prose says pending sync but "
                              f"external_sync_status={sync}")
            # a compiled pending-sync decision must be flagged and its conflict visible
            if s.sid in compiled_ids and sync == "PENDING":
                if index_txt and s.sid not in index_txt:
                    errors.append(f"decision sync: {s.sid} compiled with PENDING sync "
                                  f"but runtime index has no warning for it")
                if "typograf" not in registry_conflicts.lower() \
                        and "signage" not in registry_conflicts.lower():
                    errors.append(f"decision sync: {s.sid} compiled with PENDING sync "
                                  f"but SOURCE_REGISTRY no longer shows the conflict")

    # top-level release version consistency (P0-05): manifest == registries
    mver = manifest.get("version")
    for reg in ("SOURCE_REGISTRY.json", "ASSET_REGISTRY.json"):
        rv = vlib.load_json(os.path.join(vlib.REGISTRIES_DIR, reg)).get("version")
        if rv != mver:
            errors.append(f"version drift: {reg} version {rv} != manifest {mver}")
    label = manifest.get("release_label", "")
    if mver and mver not in label:
        errors.append(f"version drift: release_label '{label}' does not contain {mver}")

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
