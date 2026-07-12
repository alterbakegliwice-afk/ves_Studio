#!/usr/bin/env bash
# Full merge gate for VES Studio. Exit 0 only if every stage passes.
#
# Freshness is verified BEFORE building, and a rebuild must produce no diff, so
# a stale committed runtime fails the gate instead of being silently repaired
# by the build step (P0-01).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "==> validate sources";       python scripts/validate_sources.py
echo "==> validate dependencies";  python scripts/validate_dependencies.py
echo "==> validate registries";    python scripts/validate_registries.py
echo "==> validate policies";      python scripts/validate_policies.py
echo "==> detect duplicate rules"; python scripts/detect_duplicate_rules.py

echo "==> verify committed runtime is fresh"; python scripts/verify_runtime_freshness.py
echo "==> validate runtime";       python scripts/validate_runtime.py

echo "==> rebuild runtime and assert no diff"
python scripts/build_runtime_pack.py
if ! git diff --quiet -- runtime/ 2>/dev/null; then
  echo "ERROR: committed runtime/ differs from a fresh build — rebuild and commit."
  git --no-pager diff -- runtime/ || true
  exit 1
fi

echo "==> pytest";                 python -m pytest -q

echo "==> MERGE GATE PASSED"
