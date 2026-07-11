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
