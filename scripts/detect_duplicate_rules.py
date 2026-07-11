#!/usr/bin/env python3
"""Detect potentially duplicated rules across sources (report only).

Minimum viable duplication detector required by the audit:
- identical or near-identical headings that appear in more than one file,
- repeated non-trivial text blocks (paragraphs) shared across files.

This tool NEVER edits or deletes content. It prints a report for manual review
and always exits 0 (it is a signal, not a gate). Pass --out PATH to also write
the report to a file.
"""
from __future__ import annotations

import argparse
import re
from collections import defaultdict

from vlib import load_sources

HEADING_RE = re.compile(r"^#{1,6}\s+(.*)$")
GENERIC_HEADINGS = {
    "cel", "właściciel", "zależności", "aktualizacja", "ważność",
    "automatyzacja", "współdzielenie", "status", "zasada", "zasady",
    "produkcja", "layout", "struktura", "marka", "dane",
}


def normalize(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[`*_#>]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    args = ap.parse_args()

    sources = load_sources()
    heading_map: dict[str, set] = defaultdict(set)
    block_map: dict[str, set] = defaultdict(set)

    for s in sources:
        # skip archived/superseded from duplication signal
        if s.status in ("SUPERSEDED", "ARCHIVED"):
            continue
        for line in s.body.splitlines():
            hm = HEADING_RE.match(line.strip())
            if hm:
                h = normalize(hm.group(1))
                if h and h not in GENERIC_HEADINGS and len(h) > 3:
                    heading_map[h].add(s.rel)
        # paragraph blocks
        for block in re.split(r"\n\s*\n", s.body):
            nb = normalize(block)
            if len(nb) >= 60 and not nb.startswith("|"):
                block_map[nb].add(s.rel)

    dup_headings = {h: sorted(f) for h, f in heading_map.items() if len(f) > 1}
    dup_blocks = {b: sorted(f) for b, f in block_map.items() if len(f) > 1}

    lines = ["# DUPLICATE RULES REPORT", ""]
    lines.append(f"Scanned {len(sources)} sources.")
    lines.append(f"Repeated headings: {len(dup_headings)}")
    lines.append(f"Repeated text blocks: {len(dup_blocks)}")
    lines.append("")

    if dup_headings:
        lines.append("## Repeated headings (manual review)")
        for h, files in sorted(dup_headings.items()):
            lines.append(f"- \"{h}\" -> {', '.join(files)}")
        lines.append("")
    if dup_blocks:
        lines.append("## Repeated text blocks (manual review)")
        for b, files in sorted(dup_blocks.items()):
            preview = (b[:80] + "...") if len(b) > 80 else b
            lines.append(f"- \"{preview}\" -> {', '.join(files)}")
        lines.append("")

    report = "\n".join(lines)
    print(report)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(report + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
