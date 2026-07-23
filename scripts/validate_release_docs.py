#!/usr/bin/env python3
"""Guard active release documents against version / report / test-count drift.

This is the check that would have caught the round-2 docs drift (P0-09/P0-10):
- the manifest version must appear in each active release doc,
- active release docs must not declare a different release version,
- active docs must not hard-code a test count (pytest PASS is enough),
- every referenced report/registry file path must actually exist.

Note: per-source module versions in frontmatter (e.g. QUALITY_GATE 1.1.x) are NOT
checked here — those are module versions, not the release version.

Exit 0 on success, 1 on any drift.
"""
from __future__ import annotations

import os
import re
import sys

import vlib

# active docs that must track the release version
VERSION_DOCS = ["README.md", "STATUS.md", "VALIDATION_REPORT.md",
                os.path.join("runtime", "00_RUNTIME_INDEX.md")]
# docs where a stale version / test count is forbidden
DRIFT_DOCS = ["README.md", "STATUS.md", "VALIDATION_REPORT.md"]
# docs scanned for dead file references
REF_DOCS = ["README.md", "STATUS.md", "VALIDATION_REPORT.md", "CHANGELOG.md",
            "CLAUDE_CODE_IMPLEMENTATION_REPORT_v1.1.1.md"]

SEMVER = re.compile(r"\b\d+\.\d+\.\d+\b")
TESTCOUNT = re.compile(r"\b\d+\s*(?:tests?|testy|testów|testów)\b", re.I)
REF = re.compile(r"`(CLAUDE_CODE_[\w.]+\.md|[\w.\-]+/[\w./-]+\.(?:md|json))`")


def _read(rel):
    p = os.path.join(vlib.REPO_ROOT, rel)
    return open(p, encoding="utf-8").read() if os.path.isfile(p) else None


def main() -> int:
    errors: list[str] = []
    mver = vlib.manifest()["version"]

    for rel in VERSION_DOCS:
        txt = _read(rel)
        if txt is None:
            errors.append(f"{rel}: missing")
            continue
        if mver not in txt:
            errors.append(f"{rel}: does not contain release version {mver}")

    for rel in DRIFT_DOCS:
        txt = _read(rel) or ""
        for v in set(SEMVER.findall(txt)):
            if v != mver:
                errors.append(f"{rel}: stale release version '{v}' (manifest is {mver})")
        for tc in set(TESTCOUNT.findall(txt)):
            errors.append(f"{rel}: hard-coded test count '{tc}' — use 'pytest PASS'")

    for rel in REF_DOCS:
        txt = _read(rel)
        if txt is None:
            continue
        for m in REF.finditer(txt):
            ref = m.group(1)
            if not os.path.exists(os.path.join(vlib.REPO_ROOT, ref)):
                errors.append(f"{rel}: references missing file '{ref}'")

    print("validate_release_docs: version + report + test-count coherence")
    if errors:
        print(f"\nFAILED with {len(errors)} error(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("validate_release_docs: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
