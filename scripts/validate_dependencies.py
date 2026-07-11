#!/usr/bin/env python3
"""Validate the dependency graph across `sources/`.

Checks:
- every dependency is a repo-relative path under sources/ that exists,
- no non-resolvable identifiers (e.g. 'BRAND_SYSTEM', 'schemas', 'wszystkie pliki'),
- no dependency cycles,
- an ACTIVE file does not depend on an ARCHITECTURE_ONLY placeholder (PARTIAL may),
- an ACTIVE/PARTIAL file does not depend on a SUPERSEDED source.

Exit code 0 on success, 1 on any error.
"""
from __future__ import annotations

import os
import sys

from vlib import REPO_ROOT, ACTIVE_LIKE, load_sources


def main() -> int:
    sources = load_sources()
    by_rel = {s.rel: s for s in sources}
    errors: list[str] = []
    graph: dict[str, list[str]] = {}

    for s in sources:
        deps = s.meta.get("dependencies") or []
        graph[s.rel] = []
        for dep in deps:
            dep = str(dep)
            if not dep.startswith("sources/") or not dep.endswith(".md"):
                errors.append(
                    f"{s.rel}: dependency '{dep}' is not a resolvable sources/ path")
                continue
            abspath = os.path.join(REPO_ROOT, dep)
            if not os.path.isfile(abspath):
                errors.append(f"{s.rel}: dependency '{dep}' does not exist")
                continue
            graph[s.rel].append(dep)
            target = by_rel.get(dep)
            if target is None:
                continue
            tstatus = target.status
            if s.status == "ACTIVE" and tstatus == "ARCHITECTURE_ONLY":
                errors.append(
                    f"{s.rel} (ACTIVE) depends on placeholder {dep} "
                    f"(ARCHITECTURE_ONLY); mark it PARTIAL or fill the component")
            if s.status in ACTIVE_LIKE and tstatus == "SUPERSEDED":
                errors.append(
                    f"{s.rel} ({s.status}) depends on SUPERSEDED source {dep}")

    # cycle detection (DFS)
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {n: WHITE for n in graph}
    stack: list[str] = []
    cycles: list[str] = []

    def dfs(node: str):
        color[node] = GRAY
        stack.append(node)
        for nxt in graph.get(node, []):
            if nxt not in color:
                continue
            if color[nxt] == GRAY:
                i = stack.index(nxt)
                cycles.append(" -> ".join(stack[i:] + [nxt]))
            elif color[nxt] == WHITE:
                dfs(nxt)
        stack.pop()
        color[node] = BLACK

    for n in graph:
        if color[n] == WHITE:
            dfs(n)

    for c in cycles:
        errors.append(f"dependency cycle: {c}")

    edges = sum(len(v) for v in graph.values())
    print(f"validate_dependencies: {len(graph)} nodes, {edges} edges")
    if errors:
        print(f"\nFAILED with {len(errors)} error(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("validate_dependencies: OK (no cycles, all paths resolve)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
