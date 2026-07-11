#!/usr/bin/env python3
"""Detect duplicated rules across sources — policy-aware.

- Repeated GENERIC headings (Problem, Decyzja, ...) are reported, never fail.
- Exact repeated NORMATIVE text blocks above a length threshold, shared by more
  than one ACTIVE/PARTIAL/DRAFT normative source, FAIL the build unless listed
  in `registries/DUPLICATE_EXEMPTIONS.json` (with reason + owner).

This enforces ONE OWNER PER RULE at the block level. It still never edits
content. Pass --out PATH to also write the report to a file.

Exit 0 when no unexempted normative duplicate remains, 1 otherwise.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re
from collections import defaultdict

import vlib

HEADING_RE = re.compile(r"^#{1,6}\s+(.*)$")
GENERIC_HEADINGS = {
    "cel", "właściciel", "zależności", "aktualizacja", "ważność",
    "automatyzacja", "współdzielenie", "status", "zasada", "zasady",
    "produkcja", "layout", "struktura", "marka", "dane",
}
NORMATIVE_STATUS = {"ACTIVE", "PARTIAL", "DRAFT"}
BLOCK_THRESHOLD = 200  # chars of normalized text to count as a normative block


def normalize(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[`*_#>]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    args = ap.parse_args()

    sources = vlib.load_sources()
    heading_map: dict[str, set] = defaultdict(set)
    block_map: dict[str, set] = defaultdict(set)
    block_text: dict[str, str] = {}

    for s in sources:
        if s.status in ("SUPERSEDED", "ARCHIVED"):
            continue
        for line in s.body.splitlines():
            hm = HEADING_RE.match(line.strip())
            if hm:
                h = normalize(hm.group(1))
                if h and h not in GENERIC_HEADINGS and len(h) > 3:
                    heading_map[h].add(s.rel)
        if s.status in NORMATIVE_STATUS and s.meta.get("source_type") == "normative":
            for block in re.split(r"\n\s*\n", s.body):
                nb = normalize(block)
                if len(nb) >= BLOCK_THRESHOLD and not nb.startswith("|"):
                    key = hashlib.sha256(nb.encode()).hexdigest()
                    block_map[key].add(s.rel)
                    block_text[key] = nb

    exemptions = vlib.load_json(
        os.path.join(vlib.REGISTRIES_DIR, "DUPLICATE_EXEMPTIONS.json"))
    exempt_keys = {e.get("block_sha256") for e in exemptions.get("exemptions", [])}

    dup_headings = {h: sorted(f) for h, f in heading_map.items() if len(f) > 1}
    dup_blocks = {k: sorted(f) for k, f in block_map.items() if len(f) > 1}
    violations = {k: f for k, f in dup_blocks.items() if k not in exempt_keys}

    lines = ["# DUPLICATE RULES REPORT", "",
             f"Scanned {len(sources)} sources.",
             f"Repeated headings (informational): {len(dup_headings)}",
             f"Repeated normative blocks: {len(dup_blocks)} "
             f"({len(violations)} unexempted)", ""]
    if dup_headings:
        lines.append("## Repeated headings (informational)")
        for h, files in sorted(dup_headings.items()):
            lines.append(f"- \"{h}\" -> {', '.join(files)}")
        lines.append("")
    if violations:
        lines.append("## Normative duplicate BLOCKERS")
        for k, files in sorted(violations.items()):
            preview = block_text[k][:90] + "..."
            lines.append(f"- sha256={k[:16]} \"{preview}\" -> {', '.join(files)}")
        lines.append("")
        lines.append("Fix: dedupe by reference (ONE OWNER PER RULE), or add an "
                     "exemption with block_sha256 + reason + owner in "
                     "registries/DUPLICATE_EXEMPTIONS.json.")

    report = "\n".join(lines)
    print(report)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(report + "\n")

    if violations:
        print(f"\nFAILED: {len(violations)} unexempted normative duplicate block(s)")
        return 1
    print("\ndetect_duplicate_rules: OK (no unexempted normative duplicates)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
