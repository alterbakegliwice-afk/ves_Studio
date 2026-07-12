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
import sys

import vlib
from vlib import REPO_ROOT, RUNTIME_DIR


def build_date(manifest) -> str:
    return os.environ.get("BUILD_DATE") or manifest.get("date") or _today()


def _today() -> str:
    import datetime
    return datetime.date.today().isoformat()


def source_commit() -> str:
    # Only stamp an explicit commit (release/handoff via $SOURCE_COMMIT). The
    # committed runtime stays deterministic — its canonical identity is the
    # source checksum, not a self-referential git SHA (P1-03).
    return os.environ.get("SOURCE_COMMIT", "").strip() or "UNKNOWN"


def _commit_line() -> str:
    c = source_commit()
    return c if c != "UNKNOWN" else "n/a (nie stemplowany; użyj SOURCE_COMMIT w release/handoff)"


def marker(sid, rel, status, version) -> str:
    return f"<!-- SOURCE id={sid} path={rel} status={status} version={version} -->"


def build_runtime_registry(manifest, comp, version) -> dict:
    """Compile the minimal operational registry shipped as 07_RUNTIME_REGISTRY.json.

    The runtime pack is self-contained: the model gets asset constraints,
    fallbacks, external-source states and the model routing pointer here, so no
    runtime instruction has to reference a file outside the pack (P0-03)."""
    src = vlib.load_json(os.path.join(vlib.REGISTRIES_DIR, "SOURCE_REGISTRY.json"))
    assets = vlib.load_json(os.path.join(vlib.REGISTRIES_DIR, "ASSET_REGISTRY.json"))
    pointer = vlib.load_json(os.path.join(vlib.REGISTRIES_DIR,
                                          "MODEL_CAPABILITY_POINTER.json"))
    external_sources = [{
        "id": s["id"], "name": s["name"], "domain": s.get("domain"),
        "availability_state": s.get("availability_state"),
        "freshness_state": s.get("freshness_state"),
        "integrity_state": s.get("integrity_state"),
        "criticality": s.get("criticality"),
        "conflicts": [{"summary": c["summary"], "severity": c["severity"]}
                      for c in s.get("known_conflicts", [])],
    } for s in src.get("sources", [])]
    asset_constraints = [{
        "id": a["id"], "name": a["name"], "type": a["type"],
        "license_status": a["license_status"], "status": a["status"],
        "approved_fallback": (a.get("fallback") if a["status"] == "ACTIVE"
                              and a["license_status"] == "CONFIRMED"
                              else a.get("fallback") or "NO_APPROVED_FALLBACK"),
        "restriction": (a.get("restrictions") or [None])[0],
    } for a in assets.get("assets", [])]
    return {
        "runtime_version": version,
        "generated": "runtime",
        "external_sources": external_sources,
        "asset_constraints": asset_constraints,
        "model_routing_pointer": {
            "state": pointer.get("state"), "usable": pointer.get("usable"),
            "rule": pointer.get("rule"), "blocked_reason": pointer.get("blocked_reason"),
        },
        "domain_capabilities": comp.get("domain_capabilities", []),
    }


def main() -> int:
    manifest = vlib.manifest()
    comp = vlib.composition()
    by_id = vlib.sources_by_id()
    allowed = set(comp.get("default_allowed_status", ["ACTIVE"]))
    exceptions = {e["id"]: e for e in comp.get("exceptions", [])}
    version = manifest["version"]
    runtime_status = manifest.get("runtime_status", "")  # single owner: manifest (P1-06)

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
            if s.meta.get("review_status") not in ("REVIEWED", "APPROVED"):
                print(f"ERROR: {sid} review_status {s.meta.get('review_status')} "
                      f"is not runtime-eligible (need REVIEWED or APPROVED)")
                return 1
            if s.meta.get("source_type") == "decision" \
                    and s.meta.get("decision_status") != "ACCEPTED":
                print(f"ERROR: decision {sid} decision_status "
                      f"{s.meta.get('decision_status')} must be ACCEPTED to compile")
                return 1

    sync_warnings = []
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
            # decision obowiązuje w runtime, ale sygnalizuj brak synchronizacji
            if s.meta.get("external_sync_status") == "PENDING":
                w = (f"> ⚠️ EXTERNAL SYNC PENDING — `{sid}`: decyzja obowiązuje "
                     f"(latest Piotrek decision wins), ale źródło zewnętrzne nie "
                     f"jest zsynchronizowane. Traktuj jako obowiązującą regułę, "
                     f"oznaczając ryzyko rozjazdu z Drive.")
                parts.append(w)
                parts.append("")
                sync_warnings.append(f"- `{sid}`: external_sync PENDING (obowiązuje z ostrzeżeniem)")
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

    # 07 runtime registry — compiled minimal operational data the model needs
    reg = build_runtime_registry(manifest, comp, version)
    with open(os.path.join(RUNTIME_DIR, "07_RUNTIME_REGISTRY.json"), "w",
              encoding="utf-8") as f:
        json.dump(reg, f, ensure_ascii=False, indent=2)
        f.write("\n")
    written.append("07_RUNTIME_REGISTRY.json")
    print("built runtime/07_RUNTIME_REGISTRY.json")

    # 00 runtime index
    excluded = comp.get("exclusions", [])
    idx = [
        "# 00 RUNTIME INDEX",
        "",
        f"- **Runtime version:** {version}",
        f"- **Runtime status:** {runtime_status}",
        f"- **Release:** {manifest.get('release_label', '')}",
        f"- **Build date:** {build_date(manifest)}",
        f"- **Source commit:** {_commit_line()}",
        f"- **Source checksum:** {checksum}  (kanoniczna identyfikacja runtime)",
        "",
        "## Files",
        "",
        "- `00_RUNTIME_INDEX.md`",
    ]
    for t in comp["targets"]:
        idx.append(f"- `{t['file']}`")
    idx.append("- `07_RUNTIME_REGISTRY.json`")
    idx += ["", "## Runtime eligibility", "",
            f"- Kompilowane statusy: {sorted(allowed)} (ACTIVE-only default), "
            f"review_status ∈ {{REVIEWED, APPROVED}}."]
    if exception_warnings:
        idx += ["", "### Wyjątki (źródła nie-ACTIVE dopuszczone jawnie)", ""]
        idx.extend(exception_warnings)
    else:
        idx.append("- Brak wyjątków: żadne źródło DRAFT/PARTIAL nie trafia do runtime.")
    if sync_warnings:
        idx += ["", "### Decyzje obowiązujące z ostrzeżeniem (external sync PENDING)", ""]
        idx.extend(sync_warnings)
    dom = comp.get("domain_capabilities", [])
    if dom:
        idx += ["", "## Domain capabilities", ""]
        idx.extend(f"- `{d['domain']}` — {d['state']}: {d['rule']}" for d in dom)
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

    # prune stale runtime files no longer produced by the composition
    for existing in os.listdir(RUNTIME_DIR):
        p = os.path.join(RUNTIME_DIR, existing)
        if os.path.isfile(p) and existing not in written:
            os.remove(p)
            print(f"pruned stale runtime/{existing}")

    print(f"\nRuntime pack: {len(written)} files, version {version}, {checksum}")
    if len(written) > manifest["runtime_pack"]["max_files"]:
        print("ERROR: more than max runtime files")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
