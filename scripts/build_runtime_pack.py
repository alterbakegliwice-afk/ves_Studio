#!/usr/bin/env python3
"""Compile the ChatGPT Runtime Pack from active sources.

Generates at most 8 files in `runtime/` from canonical sources. Rules:
- no placeholders (ARCHITECTURE_ONLY) and no SUPERSEDED content,
- no full changelog, no archive,
- every runtime file carries a `## SOURCE MAP` section pointing at the
  canonical source file(s) for each rule.

Build date comes from $BUILD_DATE (fallback: today) so CI stays reproducible;
source commit comes from $SOURCE_COMMIT or `git rev-parse HEAD`.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

from vlib import REPO_ROOT, RUNTIME_DIR, load_sources

RUNTIME_VERSION = "1.1.0"

# runtime doc -> ordered list of source rel paths
COMPOSITION = {
    "01_VES_STUDIO_CORE.md": [
        "sources/01_MASTER_CONTEXT/MASTER_CONTEXT.md",
        "sources/01_MASTER_CONTEXT/ROUTING.md",
        "sources/01_MASTER_CONTEXT/SOURCE_OF_TRUTH.md",
        "sources/01_MASTER_CONTEXT/QUALITY_GATE.md",
        "sources/01_MASTER_CONTEXT/DATA_AND_PRIVACY_POLICY.md",
    ],
    "02_BRAND_CONTEXTS.md": [
        "sources/02_BRAND_SYSTEM/ALTERBAKE_BRAND.md",
        "sources/02_BRAND_SYSTEM/DIETANKA_BRAND_HYPOTHESES.md",
        "sources/02_BRAND_SYSTEM/PERSONAL_OS_BRAND.md",
    ],
    "03_VISUAL_SYSTEM.md": [
        "sources/03_VISUAL_LANGUAGE/VISUAL_LANGUAGE.md",
        "sources/03_VISUAL_LANGUAGE/LAYOUT_SYSTEM.md",
        "sources/03_VISUAL_LANGUAGE/PHOTO_SYSTEM.md",
        "sources/03_VISUAL_LANGUAGE/STUDIO_WORKFLOW.md",
        "sources/06_PROMPT_LIBRARY/FRAME_12.md",
    ],
    "04_DOCUMENT_SYSTEM.md": [
        "sources/05_DOCUMENT_SYSTEM/BRIEF_SYSTEM.md",
        "sources/05_DOCUMENT_SYSTEM/PDF_SYSTEM.md",
        "sources/05_DOCUMENT_SYSTEM/PRESENTATION_SYSTEM.md",
        "sources/05_DOCUMENT_SYSTEM/REPORT_SYSTEM.md",
        "sources/05_DOCUMENT_SYSTEM/AI_BATON_SYSTEM.md",
        "sources/05_DOCUMENT_SYSTEM/ARTIFACT_NAMING.md",
    ],
    "05_PROJECT_SYSTEM.md": [
        "sources/08_PROJECT_TEMPLATE/PROJECT_TEMPLATE.md",
        "sources/08_PROJECT_TEMPLATE/STATUS.md",
        "sources/08_PROJECT_TEMPLATE/DECISION_RECORD.md",
    ],
    "06_REVIEW_SYSTEM.md": [
        "sources/09_REVIEW_SYSTEM/REVIEW_INDEX.md",
        "sources/09_REVIEW_SYSTEM/BRAND_REVIEW.md",
        "sources/09_REVIEW_SYSTEM/UI_REVIEW.md",
        "sources/09_REVIEW_SYSTEM/DASHBOARD_REVIEW.md",
        "sources/09_REVIEW_SYSTEM/PDF_REVIEW.md",
        "sources/09_REVIEW_SYSTEM/PHOTO_REVIEW.md",
        "sources/09_REVIEW_SYSTEM/PRESENTATION_REVIEW.md",
        "sources/09_REVIEW_SYSTEM/PROMPT_REVIEW.md",
        "sources/09_REVIEW_SYSTEM/FINAL_REVIEW.md",
    ],
}

TITLES = {
    "01_VES_STUDIO_CORE.md": "VES STUDIO — CORE (runtime)",
    "02_BRAND_CONTEXTS.md": "VES STUDIO — BRAND CONTEXTS (runtime)",
    "03_VISUAL_SYSTEM.md": "VES STUDIO — VISUAL SYSTEM (runtime)",
    "04_DOCUMENT_SYSTEM.md": "VES STUDIO — DOCUMENT SYSTEM (runtime)",
    "05_PROJECT_SYSTEM.md": "VES STUDIO — PROJECT SYSTEM (runtime)",
    "06_REVIEW_SYSTEM.md": "VES STUDIO — REVIEW SYSTEM (runtime)",
}


def build_date() -> str:
    d = os.environ.get("BUILD_DATE")
    if d:
        return d
    import datetime
    return datetime.date.today().isoformat()


def source_commit() -> str:
    c = os.environ.get("SOURCE_COMMIT")
    if c:
        return c
    try:
        return subprocess.check_output(
            ["git", "-C", REPO_ROOT, "rev-parse", "HEAD"],
            text=True).strip()
    except Exception:
        return "UNKNOWN"


def main() -> int:
    sources = {s.rel: s for s in load_sources()}
    os.makedirs(RUNTIME_DIR, exist_ok=True)

    # guard: never compile placeholder/superseded content
    for docs in COMPOSITION.values():
        for rel in docs:
            s = sources.get(rel)
            if s is None:
                print(f"ERROR: composition references missing source {rel}")
                return 1
            if s.status in ("ARCHITECTURE_ONLY", "SUPERSEDED", "ARCHIVED"):
                print(f"ERROR: cannot compile {rel} with status {s.status}")
                return 1

    written = []
    for doc, rels in COMPOSITION.items():
        parts = [f"# {TITLES[doc]}", ""]
        source_map = []
        for rel in rels:
            s = sources[rel]
            parts.append(s.body.strip())
            parts.append("\n---\n")
            source_map.append(f"- `{s.sid}` — `{rel}` (status: {s.status})")
        parts.append("## SOURCE MAP")
        parts.append("")
        parts.extend(source_map)
        content = "\n".join(parts).rstrip() + "\n"
        path = os.path.join(RUNTIME_DIR, doc)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        written.append(doc)
        print(f"built runtime/{doc} <- {len(rels)} sources")

    # 07 source registry (runtime copy)
    with open(os.path.join(REPO_ROOT, "registries", "SOURCE_REGISTRY.json"),
              encoding="utf-8") as f:
        registry = json.load(f)
    registry["generated"] = "runtime"
    with open(os.path.join(RUNTIME_DIR, "07_SOURCE_REGISTRY.json"), "w",
              encoding="utf-8") as f:
        json.dump(registry, f, ensure_ascii=False, indent=2)
        f.write("\n")
    written.append("07_SOURCE_REGISTRY.json")
    print("built runtime/07_SOURCE_REGISTRY.json")

    # 00 runtime index
    partial_or_draft = sorted(
        f"- `{s.sid}` ({s.status}) — `{s.rel}`"
        for s in sources.values()
        if s.status in ("PARTIAL", "DRAFT")
        and any(s.rel in rels for rels in COMPOSITION.values())
    )
    idx = [
        "# 00 RUNTIME INDEX",
        "",
        f"- **Runtime version:** {RUNTIME_VERSION}",
        f"- **Build date:** {build_date()}",
        f"- **Source commit:** {source_commit()}",
        "",
        "## Files",
        "",
        "- `00_RUNTIME_INDEX.md`",
    ]
    for doc in list(COMPOSITION.keys()) + ["07_SOURCE_REGISTRY.json"]:
        idx.append(f"- `{doc}`")
    idx += [
        "",
        "## Known limitations",
        "",
        "- Runtime zawiera źródła o statusie PARTIAL/DRAFT wymienione niżej.",
        "- Dietanka jest zestawem hipotez, nie zatwierdzonym brandbookiem.",
        "- Tokeny produkcyjne są w wersji DRAFT.",
        "- STATUS_ALTERBAKE (Drive) wymaga synchronizacji typografii.",
        "- Konkretne modele wykonawcze wskazuje AI Command Center, nie runtime.",
        "",
    ]
    idx.extend(partial_or_draft or ["- (brak PARTIAL/DRAFT w kompilacji)"])
    idx += [
        "",
        "## SOURCE MAP",
        "",
        "- Index generowany przez `scripts/build_runtime_pack.py` ze źródeł `sources/`.",
    ]
    with open(os.path.join(RUNTIME_DIR, "00_RUNTIME_INDEX.md"), "w",
              encoding="utf-8") as f:
        f.write("\n".join(idx).rstrip() + "\n")
    written.insert(0, "00_RUNTIME_INDEX.md")
    print("built runtime/00_RUNTIME_INDEX.md")

    print(f"\nRuntime pack: {len(written)} files")
    if len(written) > 8:
        print("ERROR: more than 8 runtime files")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
