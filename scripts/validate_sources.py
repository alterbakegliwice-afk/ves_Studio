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
REQUIRED = ["id", "version", "status", "owner", "approved_by", "updated",
            "source_type", "scope", "canonical", "dependencies"]
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

        if not str(m.get("owner", "")).strip():
            errors.append(f"{s.rel}: owner is empty")
        if not str(m.get("approved_by", "")).strip():
            errors.append(f"{s.rel}: approved_by is empty")

        if not isinstance(m.get("canonical"), bool):
            errors.append(f"{s.rel}: canonical must be a boolean")

        if not isinstance(m.get("dependencies"), list):
            errors.append(f"{s.rel}: dependencies must be a list")

        # placeholders must never be ACTIVE
        if status == "ARCHITECTURE_ONLY" and m.get("canonical") is True:
            errors.append(f"{s.rel}: ARCHITECTURE_ONLY placeholder must not be canonical:true")

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
