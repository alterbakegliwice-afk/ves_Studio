#!/usr/bin/env python3
"""Validate the compiled Runtime Pack in `runtime/`.

Checks:
- at most 8 files,
- no placeholder markers and no SUPERSEDED content,
- no outdated concrete model names,
- every .md carries a `## SOURCE MAP` section,
- every .json parses,
- no secrets/tokens,
- each file under the size limit.

Exit code 0 on success, 1 on any error.
"""
from __future__ import annotations

import json
import os
import re
import sys

from vlib import RUNTIME_DIR

MAX_FILES = 8
MAX_BYTES = 60_000

PLACEHOLDER_MARKERS = [
    "ARCHITECTURE ONLY", "ARCHITECTURE_ONLY", "TODO", "TBD", "PLACEHOLDER",
    "LOREM IPSUM",
]
# Detect an actual superseded *document* (frontmatter status or title marker),
# not the word 'SUPERSEDED' used as a status option inside a template.
SUPERSEDED_DOC = [
    re.compile(r"(?im)^\s*status:\s*SUPERSEDED\s*$"),
    re.compile(r"(?im)^#.*—\s*SUPERSEDED\s*$"),
]
OUTDATED_MODELS = [
    re.compile(r"GPT[-‑– ]?5\.6", re.I),
    re.compile(r"Nano Banana", re.I),
    re.compile(r"GPT Image", re.I),
]
SECRET_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"][^'\"]{8,}"),
    re.compile(r"sk-[A-Za-z0-9]{16,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"AIza[0-9A-Za-z_\-]{30,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]


def main() -> int:
    if not os.path.isdir(RUNTIME_DIR):
        print("validate_runtime: runtime/ directory missing")
        return 1

    files = sorted(f for f in os.listdir(RUNTIME_DIR)
                   if os.path.isfile(os.path.join(RUNTIME_DIR, f)))
    errors: list[str] = []

    if len(files) > MAX_FILES:
        errors.append(f"runtime has {len(files)} files (max {MAX_FILES})")

    for name in files:
        path = os.path.join(RUNTIME_DIR, name)
        raw = open(path, "rb").read()
        if len(raw) > MAX_BYTES:
            errors.append(f"{name}: {len(raw)} bytes exceeds limit {MAX_BYTES}")
        text = raw.decode("utf-8", errors="replace")

        for marker in PLACEHOLDER_MARKERS:
            if marker in text:
                errors.append(f"{name}: contains placeholder marker '{marker}'")
        for pat in SUPERSEDED_DOC:
            if pat.search(text):
                errors.append(f"{name}: contains SUPERSEDED document content")
        for pat in OUTDATED_MODELS:
            m = pat.search(text)
            if m:
                errors.append(f"{name}: outdated model name '{m.group(0)}'")
        for pat in SECRET_PATTERNS:
            if pat.search(text):
                errors.append(f"{name}: possible secret/token detected")

        if name.endswith(".md"):
            if "## SOURCE MAP" not in text:
                errors.append(f"{name}: missing '## SOURCE MAP' section")
        if name.endswith(".json"):
            try:
                json.loads(text)
            except json.JSONDecodeError as exc:
                errors.append(f"{name}: invalid JSON ({exc})")

    print(f"validate_runtime: {len(files)} runtime files")
    if errors:
        print(f"\nFAILED with {len(errors)} error(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("validate_runtime: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
