#!/usr/bin/env python3
"""Verify that runtime/ was rebuilt from the current sources.

Recomputes the deterministic checksum of the compiled sources and compares it
with the checksum recorded in `runtime/00_RUNTIME_INDEX.md`. If a source that
feeds runtime changed without a rebuild, the checksums diverge and this exits 1.

Human workflow when it fails:
    python scripts/build_runtime_pack.py   # rebuild
    # re-upload runtime/ to the ChatGPT project (replace the old pack)

Exit 0 on success, 1 on mismatch/missing.
"""
from __future__ import annotations

import os
import re
import sys

import vlib

CHECKSUM_RE = re.compile(r"Source checksum:\*\*\s*(sha256:[0-9a-f]+)")


def main() -> int:
    idx = os.path.join(vlib.RUNTIME_DIR, "00_RUNTIME_INDEX.md")
    if not os.path.isfile(idx):
        print("verify_runtime_freshness: runtime index missing — build runtime first")
        return 1
    m = CHECKSUM_RE.search(open(idx, encoding="utf-8").read())
    if not m:
        print("verify_runtime_freshness: no checksum recorded in runtime index")
        return 1
    recorded = m.group(1)
    current = vlib.runtime_checksum(vlib.compiled_items())
    if recorded != current:
        print("verify_runtime_freshness: STALE runtime pack")
        print(f"  recorded: {recorded}")
        print(f"  current : {current}")
        print("  -> run scripts/build_runtime_pack.py and re-upload runtime/")
        return 1
    print(f"verify_runtime_freshness: OK ({current})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
