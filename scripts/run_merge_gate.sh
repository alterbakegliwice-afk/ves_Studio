#!/usr/bin/env bash
# Full merge gate for VES Studio. Exit 0 only if every stage passes.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "==> validate sources";       python scripts/validate_sources.py
echo "==> validate dependencies";  python scripts/validate_dependencies.py
echo "==> validate registries";    python scripts/validate_registries.py
echo "==> validate policies";      python scripts/validate_policies.py
echo "==> detect duplicate rules"; python scripts/detect_duplicate_rules.py
echo "==> build runtime";          python scripts/build_runtime_pack.py
echo "==> validate runtime";       python scripts/validate_runtime.py
echo "==> verify freshness";       python scripts/verify_runtime_freshness.py
echo "==> pytest";                 python -m pytest -q

echo "==> MERGE GATE PASSED"
