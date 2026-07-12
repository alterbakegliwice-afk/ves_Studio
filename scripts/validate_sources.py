#!/usr/bin/env python3
"""Validate frontmatter of every source in `sources/`.

Checks: required fields, semantic version, allowed status, owner present,
canonical boolean, unique IDs, and that placeholders (ARCHITECTURE_ONLY) are
never ACTIVE. Validates each frontmatter against schemas/source.schema.json
when jsonschema is available.

Exit code 0 on success, 1 on any error.
"""
from __future__ import annotations

import os
import sys

from vlib import REPO_ROOT, load_sources, load_json

ALLOWED_STATUS = {
    "DRAFT", "ACTIVE", "PARTIAL", "SUPERSEDED", "ARCHIVED", "BLOCKED",
    "ARCHITECTURE_ONLY",
}
ALLOWED_TYPES = {
    "normative", "state", "decision", "evidence", "template", "registry",
    "generated-runtime",
}
REQUIRED = ["id", "version", "status", "owner", "authored_by", "review_status",
            "updated", "source_type", "scope", "canonical", "dependencies"]
SEMVER = __import__("re").compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")


def _schema_validator():
    try:
        import jsonschema  # noqa: F401
    except ImportError:
        return None
    schema = load_json(os.path.join(REPO_ROOT, "schemas", "source.schema.json"))
    from jsonschema import Draft202012Validator
    return Draft202012Validator(schema)


def main() -> int:
    sources = load_sources()
    errors: list[str] = []
    ids: dict[str, str] = {}
    validator = _schema_validator()

    for s in sources:
        for e in s.errors:
            errors.append(f"{s.rel}: {e}")
        if not s.meta:
            continue
        m = s.meta

        for field in REQUIRED:
            if field not in m:
                errors.append(f"{s.rel}: missing required field '{field}'")

        sid = m.get("id")
        if sid:
            if sid in ids:
                errors.append(f"{s.rel}: duplicate id '{sid}' (also in {ids[sid]})")
            else:
                ids[sid] = s.rel

        ver = m.get("version")
        if ver is not None and not SEMVER.match(str(ver)):
            errors.append(f"{s.rel}: version '{ver}' is not semantic (X.Y.Z)")

        status = m.get("status")
        if status not in ALLOWED_STATUS:
            errors.append(f"{s.rel}: status '{status}' not in {sorted(ALLOWED_STATUS)}")

        stype = m.get("source_type")
        if stype not in ALLOWED_TYPES:
            errors.append(f"{s.rel}: source_type '{stype}' not in {sorted(ALLOWED_TYPES)}")

        # decision sources must carry structured lifecycle + external sync state
        if stype == "decision":
            if m.get("decision_status") not in {"PROPOSED", "ACCEPTED", "SUPERSEDED", "REJECTED"}:
                errors.append(f"{s.rel}: decision source needs valid decision_status")
            if m.get("external_sync_status") not in {"NOT_REQUIRED", "PENDING", "SYNCED"}:
                errors.append(f"{s.rel}: decision source needs valid external_sync_status")

        if not str(m.get("owner", "")).strip():
            errors.append(f"{s.rel}: owner is empty")

        # honest approval model (P0-04)
        review = m.get("review_status")
        if review not in {"UNREVIEWED", "REVIEWED", "APPROVED"}:
            errors.append(f"{s.rel}: review_status '{review}' invalid")
        if status in {"DRAFT", "PARTIAL", "ARCHITECTURE_ONLY"} and review == "APPROVED":
            errors.append(f"{s.rel}: {status} source must not be review_status APPROVED")
        if review == "APPROVED" and not m.get("approved_by"):
            errors.append(f"{s.rel}: review_status APPROVED requires approved_by")
        if m.get("approved_by") and review != "APPROVED":
            errors.append(f"{s.rel}: approved_by set but review_status is {review}")
        if stype == "decision" and m.get("decision_status") == "ACCEPTED" \
                and m.get("approved_by") != "Piotrek":
            errors.append(f"{s.rel}: ACCEPTED decision requires approved_by: Piotrek")
        # decision approval provenance (P0-08): don't pass off the record date as
        # the business approval date; require evidence for an approved decision
        if stype == "decision":
            if m.get("approval_date") and m.get("approval_date") == m.get("updated"):
                errors.append(f"{s.rel}: approval_date equals 'updated' — use the real "
                              f"decision date or null, not the record timestamp")
            if review == "APPROVED" and not m.get("approval_evidence"):
                errors.append(f"{s.rel}: APPROVED decision requires approval_evidence")

        if not isinstance(m.get("canonical"), bool):
            errors.append(f"{s.rel}: canonical must be a boolean")

        if not isinstance(m.get("dependencies"), list):
            errors.append(f"{s.rel}: dependencies must be a list")

        # placeholders must never be ACTIVE
        if status == "ARCHITECTURE_ONLY" and m.get("canonical") is True:
            errors.append(f"{s.rel}: ARCHITECTURE_ONLY placeholder must not be canonical:true")

        # body vs frontmatter version consistency (P1-07)
        bm = __import__("re").search(r"\*\*Wersja:\*\*\s*([0-9]+\.[0-9]+)", s.body)
        if bm and ver:
            fm_mm = ".".join(str(ver).split(".")[:2])
            if bm.group(1) != fm_mm:
                errors.append(f"{s.rel}: body version {bm.group(1)} != frontmatter "
                              f"{ver} (major.minor must match)")

        if validator is not None:
            for err in sorted(validator.iter_errors(m), key=lambda e: e.path):
                errors.append(f"{s.rel}: schema: {err.message}")

    print(f"validate_sources: scanned {len(sources)} source files, "
          f"{len(ids)} unique ids")
    if errors:
        print(f"\nFAILED with {len(errors)} error(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("validate_sources: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
