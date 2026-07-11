"""Runtime pack build + validation tests."""
import os

import build_runtime_pack
import validate_runtime
import vlib


def _build():
    os.environ["BUILD_DATE"] = "2026-07-11"
    assert build_runtime_pack.main() == 0


def test_build_and_validate_runtime():
    _build()
    assert validate_runtime.main() == 0


def test_runtime_has_at_most_8_files():
    _build()
    files = [f for f in os.listdir(vlib.RUNTIME_DIR)
             if os.path.isfile(os.path.join(vlib.RUNTIME_DIR, f))]
    assert len(files) <= 8, files
    assert "00_RUNTIME_INDEX.md" in files
    assert "07_SOURCE_REGISTRY.json" in files


def test_runtime_md_have_source_map():
    _build()
    for f in os.listdir(vlib.RUNTIME_DIR):
        if f.endswith(".md"):
            text = open(os.path.join(vlib.RUNTIME_DIR, f), encoding="utf-8").read()
            assert "## SOURCE MAP" in text, f


def test_runtime_has_no_placeholder_or_superseded():
    _build()
    for f in os.listdir(vlib.RUNTIME_DIR):
        text = open(os.path.join(vlib.RUNTIME_DIR, f), encoding="utf-8").read()
        assert "ARCHITECTURE ONLY" not in text
        assert "ARCHITECTURE_ONLY" not in text
