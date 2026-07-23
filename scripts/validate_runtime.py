#!/usr/bin/env python3
"""Validate the compiled Runtime Pack in `runtime/`.

Structural + provenance checks:
- at most manifest.runtime_pack.max_files files,
- no placeholder markers and no SUPERSEDED document content,
- no outdated concrete model names, no secrets/tokens, size limit,
- every .md carries a `## SOURCE MAP`; every .json parses,
- every compiled section carries a `<!-- SOURCE ... -->` marker and the marker
  ids match the SOURCE MAP ids (rule-level traceability),
- runtime version equals the manifest version (no drift),
- runtime index checksum equals a fresh checksum of the compiled sources.

Exit code 0 on success, 1 on any error.
"""
from __future__ import annotations

import json
import os
import re
import sys

import vlib
from vlib import RUNTIME_DIR

MAX_BYTES = 60_000

PLACEHOLDER_MARKERS = ["ARCHITECTURE ONLY", "ARCHITECTURE_ONLY", "TODO", "TBD",
                       "PLACEHOLDER", "LOREM IPSUM"]
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
MARKER_RE = re.compile(r"<!--\s*SOURCE\s+id=(\S+)\s+path=(\S+)\s+status=(\S+)\s+version=(\S+)\s*-->")
PATH_REF_RE = re.compile(r"(?:registries|sources|schemas|scripts|tests)/[\w./-]+\.(?:md|json|py)")
SOURCEMAP_ID_RE = re.compile(r"^-\s+`([A-Z0-9-]+)`\s+—", re.M)
CHECKSUM_RE = re.compile(r"Source checksum:\*\*\s*(sha256:[0-9a-f]+)")
VERSION_RE = re.compile(r"Runtime version:\*\*\s*([0-9]+\.[0-9]+\.[0-9]+)")


def main() -> int:
    if not os.path.isdir(RUNTIME_DIR):
        print("validate_runtime: runtime/ directory missing")
        return 1

    manifest = vlib.manifest()
    max_files = manifest["runtime_pack"]["max_files"]
    comp = vlib.composition()
    target_files = {t["file"] for t in comp["targets"]}
    by_id = vlib.sources_by_id()
    # a runtime reference is in-pack if it resolves to a compiled source (its
    # content is present) or to a runtime file itself.
    compiled_basenames = {os.path.basename(by_id[sid].rel)
                          for t in comp["targets"] for sid in t["sources"]
                          if sid in by_id}
    runtime_filenames = set(target_files) | {"00_RUNTIME_INDEX.md",
                                             "07_RUNTIME_REGISTRY.json"}

    files = sorted(f for f in os.listdir(RUNTIME_DIR)
                   if os.path.isfile(os.path.join(RUNTIME_DIR, f)))
    errors: list[str] = []

    if len(files) > max_files:
        errors.append(f"runtime has {len(files)} files (max {max_files})")

    for name in files:
        path = os.path.join(RUNTIME_DIR, name)
        raw = open(path, "rb").read()
        if len(raw) > MAX_BYTES:
            errors.append(f"{name}: {len(raw)} bytes exceeds limit {MAX_BYTES}")
        text = raw.decode("utf-8", errors="replace")

        for m in PLACEHOLDER_MARKERS:
            if m in text:
                errors.append(f"{name}: contains placeholder marker '{m}'")
        for pat in SUPERSEDED_DOC:
            if pat.search(text):
                errors.append(f"{name}: contains SUPERSEDED document content")
        for pat in OUTDATED_MODELS:
            mm = pat.search(text)
            if mm:
                errors.append(f"{name}: outdated model name '{mm.group(0)}'")
        for pat in SECRET_PATTERNS:
            if pat.search(text):
                errors.append(f"{name}: possible secret/token detected")

        if name.endswith(".md"):
            if "## SOURCE MAP" not in text:
                errors.append(f"{name}: missing '## SOURCE MAP' section")
            # rule-level markers on compiled target files
            if name in target_files:
                marker_ids = [m.group(1) for m in MARKER_RE.finditer(text)]
                map_ids = SOURCEMAP_ID_RE.findall(text.split("## SOURCE MAP", 1)[-1])
                if not marker_ids:
                    errors.append(f"{name}: no <!-- SOURCE --> section markers")
                if set(marker_ids) != set(map_ids):
                    errors.append(f"{name}: marker ids {set(marker_ids)} do not "
                                  f"match SOURCE MAP ids {set(map_ids)}")
                # P0-03: no operational reference to a file outside the pack
                for line in text.splitlines():
                    if line.lstrip().startswith("<!-- SOURCE") or line.lstrip().startswith("- `"):
                        continue  # provenance markers / SOURCE MAP entries
                    for ref in PATH_REF_RE.findall(line):
                        base = os.path.basename(ref)
                        if base not in compiled_basenames and base not in runtime_filenames:
                            errors.append(f"{name}: dangling runtime reference '{ref}' "
                                          f"(file not shipped in the pack)")
        if name.endswith(".json"):
            try:
                json.loads(text)
            except json.JSONDecodeError as exc:
                errors.append(f"{name}: invalid JSON ({exc})")

    # provenance: version + checksum in index
    index_path = os.path.join(RUNTIME_DIR, "00_RUNTIME_INDEX.md")
    if os.path.isfile(index_path):
        idx = open(index_path, encoding="utf-8").read()
        vm = VERSION_RE.search(idx)
        if not vm:
            errors.append("00_RUNTIME_INDEX.md: missing Runtime version")
        elif vm.group(1) != manifest["version"]:
            errors.append(f"00_RUNTIME_INDEX.md: version {vm.group(1)} != "
                          f"manifest {manifest['version']} (drift)")
        cm = CHECKSUM_RE.search(idx)
        if not cm:
            errors.append("00_RUNTIME_INDEX.md: missing Source checksum")
        else:
            fresh = vlib.runtime_checksum(vlib.compiled_items())
            if cm.group(1) != fresh:
                errors.append("00_RUNTIME_INDEX.md: checksum stale — rebuild runtime "
                              f"(index={cm.group(1)} current={fresh})")
    else:
        errors.append("00_RUNTIME_INDEX.md missing")

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
