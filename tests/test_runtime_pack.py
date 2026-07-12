"""Runtime pack build + validation tests (P0-01, P0-05, P0-06, P0-07, P1-01, P1-03)."""
import os
import shutil
import subprocess
import sys

import build_runtime_pack
import validate_runtime
import verify_runtime_freshness
import vlib


def _build():
    os.environ["BUILD_DATE"] = "2026-07-11"
    assert build_runtime_pack.main() == 0


def test_build_and_validate_runtime():
    _build()
    assert validate_runtime.main() == 0


def test_runtime_has_at_most_max_files():
    _build()
    files = [f for f in os.listdir(vlib.RUNTIME_DIR)
             if os.path.isfile(os.path.join(vlib.RUNTIME_DIR, f))]
    assert len(files) <= vlib.manifest()["runtime_pack"]["max_files"], files
    assert "00_RUNTIME_INDEX.md" in files
    assert "07_RUNTIME_REGISTRY.json" in files


def test_runtime_is_active_only():
    """P0-01: no DRAFT/PARTIAL source content reaches the runtime."""
    _build()
    by_id = vlib.sources_by_id()
    comp = vlib.composition()
    for t in comp["targets"]:
        for sid in t["sources"]:
            assert by_id[sid].status == "ACTIVE", f"{sid} is {by_id[sid].status}"
    # Dietanka hypotheses / Personal OS drafts must not be compiled
    for draft_id in ("VES-BRAND-DIETANKA-001", "VES-BRAND-PERSONAL-OS-001",
                     "VES-PDF-001", "VES-REPORT-001"):
        text = open(os.path.join(vlib.RUNTIME_DIR, "02_BRAND_CONTEXTS.md"),
                    encoding="utf-8").read()
        assert draft_id not in text


def test_runtime_md_have_source_map_and_markers():
    """P1-01: rule-level markers present on compiled targets."""
    _build()
    comp = vlib.composition()
    targets = {t["file"] for t in comp["targets"]}
    for f in os.listdir(vlib.RUNTIME_DIR):
        if not f.endswith(".md"):
            continue
        text = open(os.path.join(vlib.RUNTIME_DIR, f), encoding="utf-8").read()
        assert "## SOURCE MAP" in text, f
        if f in targets:
            assert "<!-- SOURCE id=" in text, f


def test_runtime_version_from_manifest():
    """P0-06: index version equals manifest version (no hard-coded constant)."""
    _build()
    idx = open(os.path.join(vlib.RUNTIME_DIR, "00_RUNTIME_INDEX.md"),
               encoding="utf-8").read()
    assert vlib.manifest()["version"] in idx
    assert vlib.manifest()["runtime_status"] in idx


def test_build_is_deterministic():
    """P0-06: same inputs -> same checksum."""
    a = vlib.runtime_checksum(vlib.compiled_items())
    b = vlib.runtime_checksum(vlib.compiled_items())
    assert a == b and a.startswith("sha256:")


def test_freshness_passes_after_build():
    _build()
    assert verify_runtime_freshness.main() == 0


def test_stale_committed_runtime_fails_freshness(tmp_path):
    """P0-01: modifying an ACTIVE runtime source WITHOUT rebuilding must make the
    freshness validator exit 1 — verified end-to-end in an isolated repo copy."""
    _build()
    repo = vlib.REPO_ROOT
    dst = tmp_path / "repo"

    def ignore(d, names):
        return [n for n in names if n in (".git", "__pycache__") or n.endswith(".zip")]
    shutil.copytree(repo, dst, ignore=ignore)

    # sanity: fresh copy passes
    r0 = subprocess.run([sys.executable, "scripts/verify_runtime_freshness.py"],
                        cwd=dst, capture_output=True, text=True)
    assert r0.returncode == 0, r0.stdout + r0.stderr

    # mutate a compiled ACTIVE source WITHOUT rebuilding runtime
    target = dst / "sources/01_MASTER_CONTEXT/MASTER_CONTEXT.md"
    target.write_text(target.read_text(encoding="utf-8") + "\n\nEDYCJA BEZ REBUILDU\n",
                      encoding="utf-8")
    r1 = subprocess.run([sys.executable, "scripts/verify_runtime_freshness.py"],
                        cwd=dst, capture_output=True, text=True)
    assert r1.returncode == 1, "stale committed runtime must fail freshness"
    assert "STALE" in r1.stdout
