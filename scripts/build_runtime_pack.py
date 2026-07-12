#!/usr/bin/env python3
"""Compile the ChatGPT Runtime Pack from active sources (data-driven).

Composition, exclusions and non-ACTIVE exceptions live in
`registries/RUNTIME_COMPOSITION.json` (not Python constants). Rules:
- by default only sources whose frontmatter status is in
  `default_allowed_status` (ACTIVE) are compiled,
- any non-ACTIVE source must be an explicit `exceptions` entry; its warning is
  rendered immediately before its content and repeated in 00_RUNTIME_INDEX.md,
- each compiled section carries a machine-readable `<!-- SOURCE ... -->` marker,
- the runtime version is read from `ves-studio.manifest.json` (no hard-coded
  constant), and the index records a deterministic source checksum.

Build date comes from $BUILD_DATE (fallback: manifest date, then today) so CI
stays reproducible; source commit comes from $SOURCE_COMMIT or `git rev-parse`.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

import vlib
from vlib import REPO_ROOT, RUNTIME_DIR


def build_date(manifest) -> str:
    return os.environ.get("BUILD_DATE") or manifest.get("date") or _today()


def _today() -> str:
    import datetime
    return datetime.date.today().isoformat()


def source_commit() -> str:
    c = os.environ.get("SOURCE_COMMIT")
    if c:
        return c
    try:
        return subprocess.check_output(
            ["git", "-C", REPO_ROOT, "rev-parse", "HEAD"], text=True,
            stderr=subprocess.DEVNULL).strip()
    except Exception:
        return "UNKNOWN"


def marker(sid, rel, status, version) -> str:
    return f"<!-- SOURCE id={sid} path={rel} status={status} version={version} -->"


def main() -> int:
    manifest = vlib.manifest()
    comp = vlib.composition()
    by_id = vlib.sources_by_id()
    allowed = set(comp.get("default_allowed_status", ["ACTIVE"]))
    exceptions = {e["id"]: e for e in comp.get("exceptions", [])}
    version = manifest["version"]
    runtime_status = comp.get("runtime_status") or manifest.get("runtime_status", "")

    os.makedirs(RUNTIME_DIR, exist_ok=True)
    exception_warnings = []

    # validate eligibility up front (controlled failure, not silent compile)
    for target in comp["targets"]:
        for sid in target["sources"]:
            s = by_id.get(sid)
            if s is None:
                print(f"ERROR: composition references unknown source id {sid}")
                return 1
            if s.status not in allowed and sid not in exceptions:
                print(f"ERROR: {sid} status {s.status} is not runtime-eligible "
                      f"(allowed={sorted(allowed)}) and has no exception entry")
                return 1

    written = []
    for target in comp["targets"]:
        parts = [f"# {target['title']}", ""]
        source_map = []
        for sid in target["sources"]:
            s = by_id[sid]
            ver = str(s.meta.get("version", ""))
            if sid in exceptions:
                exc = exceptions[sid]
                warn = (f"> ⚠️ WYJĄTEK RUNTIME — źródło `{sid}` ma status "
                        f"`{s.status}`. {exc['warning']}")
                parts.append(warn)
                parts.append("")
                exception_warnings.append(f"- `{sid}` ({s.status}): {exc['warning']}")
            parts.append(marker(sid, s.rel, s.status, ver))
            parts.append(s.body.strip())
            parts.append("\n---\n")
            source_map.append(f"- `{sid}` — `{s.rel}` (status: {s.status})")
        parts.append("## SOURCE MAP")
        parts.append("")
        parts.extend(source_map)
        content = "\n".join(parts).rstrip() + "\n"
        with open(os.path.join(RUNTIME_DIR, target["file"]), "w",
                  encoding="utf-8") as f:
            f.write(content)
        written.append(target["file"])
        print(f"built runtime/{target['file']} <- {len(target['sources'])} sources")

    # deterministic checksum over compiled sources (composition order)
    checksum = vlib.runtime_checksum(vlib.compiled_items())

    # 07 source registry (runtime copy) — preserve blocking state
    registry = vlib.load_json(os.path.join(vlib.REGISTRIES_DIR, "SOURCE_REGISTRY.json"))
    registry["generated"] = "runtime"
    with open(os.path.join(RUNTIME_DIR, "07_SOURCE_REGISTRY.json"), "w",
              encoding="utf-8") as f:
        json.dump(registry, f, ensure_ascii=False, indent=2)
        f.write("\n")
    written.append("07_SOURCE_REGISTRY.json")
    print("built runtime/07_SOURCE_REGISTRY.json")

    # 00 runtime index
    excluded = comp.get("exclusions", [])
    idx = [
        "# 00 RUNTIME INDEX",
        "",
        f"- **Runtime version:** {version}",
        f"- **Runtime status:** {runtime_status}",
        f"- **Release:** {manifest.get('release_label', '')}",
        f"- **Build date:** {build_date(manifest)}",
        f"- **Source commit:** {source_commit()}",
        f"- **Source checksum:** {checksum}",
        "",
        "## Files",
        "",
        "- `00_RUNTIME_INDEX.md`",
    ]
    for t in comp["targets"]:
        idx.append(f"- `{t['file']}`")
    idx.append("- `07_SOURCE_REGISTRY.json`")
    idx += ["", "## Runtime eligibility", "",
            f"- Kompilowane statusy: {sorted(allowed)} (ACTIVE-only default)."]
    if exception_warnings:
        idx += ["", "### Wyjątki (źródła nie-ACTIVE dopuszczone jawnie)", ""]
        idx.extend(exception_warnings)
    else:
        idx.append("- Brak wyjątków: żadne źródło DRAFT/PARTIAL nie trafia do runtime.")
    idx += ["", "## Explicitly excluded ACTIVE canonical sources", ""]
    if excluded:
        idx.extend(f"- `{e['id']}` (owner: {e['owner']}) — {e['reason']}"
                   for e in excluded)
    else:
        idx.append("- (brak)")
    idx += [
        "",
        "## Known limitations",
        "",
        "- Release to Core Beta: część systemów (Component/Prompt/Reference/Automation) pozostaje poza runtime.",
        "- Konkretne modele wykonawcze wskazuje AI Command Center (obecnie BLOCKED — brak URI).",
        "- Typografia AlterBake: decyzja przyjęta, synchronizacja Drive PENDING.",
        "- Fonty Signage Grotesk / Google Sans: licencja NIEPOTWIERDZONA (PROVISIONAL).",
        "",
        "## SOURCE MAP",
        "",
        "- Index generowany przez `scripts/build_runtime_pack.py` z `registries/RUNTIME_COMPOSITION.json` i `sources/`.",
    ]
    with open(os.path.join(RUNTIME_DIR, "00_RUNTIME_INDEX.md"), "w",
              encoding="utf-8") as f:
        f.write("\n".join(idx).rstrip() + "\n")
    written.insert(0, "00_RUNTIME_INDEX.md")
    print("built runtime/00_RUNTIME_INDEX.md")

    print(f"\nRuntime pack: {len(written)} files, version {version}, {checksum}")
    if len(written) > manifest["runtime_pack"]["max_files"]:
        print("ERROR: more than max runtime files")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
