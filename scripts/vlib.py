"""Shared helpers for VES Studio validators.

Standard library + PyYAML only. No third-party imports required at module load
so the individual validators stay runnable even without jsonschema installed.
"""
from __future__ import annotations

import os
import re
from dataclasses import dataclass, field

import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SOURCES_DIR = os.path.join(REPO_ROOT, "sources")
RUNTIME_DIR = os.path.join(REPO_ROOT, "runtime")
REGISTRIES_DIR = os.path.join(REPO_ROOT, "registries")
SCHEMAS_DIR = os.path.join(REPO_ROOT, "schemas")
MANIFEST_PATH = os.path.join(REPO_ROOT, "ves-studio.manifest.json")
COMPOSITION_PATH = os.path.join(REGISTRIES_DIR, "RUNTIME_COMPOSITION.json")

PLACEHOLDER_STATUS = "ARCHITECTURE_ONLY"
ACTIVE_LIKE = {"ACTIVE", "PARTIAL"}

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


@dataclass
class Source:
    path: str          # absolute path
    rel: str           # repo-relative path (posix)
    meta: dict = field(default_factory=dict)
    body: str = ""
    errors: list = field(default_factory=list)

    @property
    def status(self) -> str:
        return str(self.meta.get("status", ""))

    @property
    def sid(self) -> str:
        return str(self.meta.get("id", ""))


def rel_posix(abs_path: str) -> str:
    return os.path.relpath(abs_path, REPO_ROOT).replace(os.sep, "/")


def parse_source(abs_path: str) -> Source:
    with open(abs_path, encoding="utf-8") as f:
        text = f.read()
    src = Source(path=abs_path, rel=rel_posix(abs_path))
    m = FM_RE.match(text)
    if not m:
        src.errors.append("missing YAML frontmatter block")
        src.body = text
        return src
    try:
        meta = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as exc:  # pragma: no cover - defensive
        src.errors.append(f"invalid YAML frontmatter: {exc}")
        meta = {}
    if not isinstance(meta, dict):
        src.errors.append("frontmatter is not a mapping")
        meta = {}
    src.meta = meta
    src.body = text[m.end():]
    return src


def iter_source_paths():
    for root, _dirs, files in os.walk(SOURCES_DIR):
        for name in sorted(files):
            if name.endswith(".md"):
                yield os.path.join(root, name)


def load_sources():
    return [parse_source(p) for p in iter_source_paths()]


def load_json(path):
    import json
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def schema_errors(instance, schema_filename):
    """Return a list of human-readable schema violation messages.

    Returns [] if jsonschema is not installed (structural fallback), so the
    validators still run in minimal environments; CI installs jsonschema.
    """
    try:
        import jsonschema  # noqa: F401
    except ImportError:
        return []
    from jsonschema import Draft202012Validator
    schema = load_json(os.path.join(SCHEMAS_DIR, schema_filename))
    validator = Draft202012Validator(schema)
    return [f"{'/'.join(str(p) for p in e.path)}: {e.message}"
            for e in sorted(validator.iter_errors(instance), key=lambda e: list(e.path))]


def manifest():
    return load_json(MANIFEST_PATH)


def composition():
    return load_json(COMPOSITION_PATH)


def sources_by_id():
    return {s.sid: s for s in load_sources()}


def runtime_checksum(items):
    """Deterministic checksum over an ordered list of (id, version, status, body).

    Independent of filesystem ordering: the caller supplies the canonical order
    (composition order). Body whitespace is stripped so trivial trailing-newline
    changes do not spuriously invalidate the checksum.
    """
    import hashlib
    h = hashlib.sha256()
    for sid, version, status, body in items:
        h.update(f"{sid}\x1f{version}\x1f{status}\x1f".encode("utf-8"))
        h.update(body.strip().encode("utf-8"))
        h.update(b"\x1e")
    return "sha256:" + h.hexdigest()


def compiled_items():
    """Return the ordered (id, version, status, body) tuples that the runtime
    composition compiles, in canonical composition order. Raises KeyError if a
    composition source id is unknown."""
    comp = composition()
    by_id = sources_by_id()
    items = []
    for target in comp["targets"]:
        for sid in target["sources"]:
            s = by_id[sid]
            items.append((sid, str(s.meta.get("version", "")), s.status, s.body))
    return items

