"""Source metadata / frontmatter tests."""
import os

import validate_sources
import vlib

FIXTURES = os.path.join(os.path.dirname(__file__), "fixtures")


def test_validate_sources_passes():
    assert validate_sources.main() == 0


def test_all_sources_have_unique_ids():
    sources = vlib.load_sources()
    ids = [s.sid for s in sources]
    assert len(ids) == len(set(ids)), "source ids are not unique"


def test_required_fields_present():
    for s in vlib.load_sources():
        for field in ("id", "version", "status", "owner", "approved_by",
                      "updated", "source_type", "scope", "canonical",
                      "dependencies"):
            assert field in s.meta, f"{s.rel} missing {field}"


def test_placeholders_never_active():
    for s in vlib.load_sources():
        if s.status == "ARCHITECTURE_ONLY":
            assert s.meta.get("canonical") is False, f"{s.rel} placeholder canonical"


def test_dietanka_renamed_to_hypotheses():
    rels = {s.rel for s in vlib.load_sources()}
    assert "sources/02_BRAND_SYSTEM/DIETANKA_BRAND_HYPOTHESES.md" in rels
    assert "sources/02_BRAND_SYSTEM/DIETANKA_BRAND.md" not in rels


def test_visual_studio_superseded():
    sources = {s.rel: s for s in vlib.load_sources()}
    vvs = sources["sources/99_ARCHIVE/VES_VISUAL_STUDIO_v1_SUPERSEDED.md"]
    assert vvs.status == "SUPERSEDED"
    assert vvs.meta.get("canonical") is False
    assert vvs.meta.get("superseded_by")


def test_parser_flags_incomplete_frontmatter():
    src = vlib.parse_source(os.path.join(FIXTURES, "invalid_missing_fields.md"))
    assert not src.errors, "frontmatter block itself is well-formed"
    missing = [f for f in ("version", "owner", "approved_by", "updated",
                           "source_type", "scope", "canonical", "dependencies")
               if f not in src.meta]
    assert missing, "fixture should be missing required fields"


def test_no_outdated_model_names_in_active_sources():
    for s in vlib.load_sources():
        text = s.body
        for bad in ("GPT-5.6", "GPT‑5.6", "Nano Banana"):
            assert bad not in text, f"{s.rel} contains outdated model name {bad}"
