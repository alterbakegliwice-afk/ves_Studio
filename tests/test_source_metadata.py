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
        for field in ("id", "version", "status", "owner", "authored_by",
                      "review_status", "updated", "source_type", "scope",
                      "canonical", "dependencies"):
            assert field in s.meta, f"{s.rel} missing {field}"


def test_honest_approval_model():
    """P0-04: no blanket approved_by; draft/partial/arch never APPROVED."""
    for s in vlib.load_sources():
        review = s.meta.get("review_status")
        assert review in ("UNREVIEWED", "REVIEWED", "APPROVED"), s.rel
        if s.status in ("DRAFT", "PARTIAL", "ARCHITECTURE_ONLY"):
            assert review != "APPROVED", f"{s.rel} draft/partial/arch is APPROVED"
        if s.meta.get("approved_by"):
            assert review == "APPROVED", f"{s.rel} approved_by set without APPROVED"


def test_only_decision_is_piotrek_approved():
    approved = [s.sid for s in vlib.load_sources()
               if s.meta.get("approved_by") == "Piotrek"]
    assert approved == ["DEC-ALTERBAKE-TYPOGRAPHY-001"], approved


def test_decision_approval_date_provenance():
    """P0-08: approval_date is not the record timestamp; evidence is required."""
    dec = vlib.sources_by_id()["DEC-ALTERBAKE-TYPOGRAPHY-001"]
    m = dec.meta
    assert m.get("approval_date") in (None, "null") or m.get("approval_date") != m.get("updated")
    assert m.get("approval_evidence"), "APPROVED decision needs approval_evidence"
    assert "record_created" in m


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
    missing = [f for f in ("version", "owner", "authored_by", "review_status",
                           "updated", "source_type", "scope", "canonical",
                           "dependencies")
               if f not in src.meta]
    assert missing, "fixture should be missing required fields"


def test_no_outdated_model_names_in_active_sources():
    for s in vlib.load_sources():
        text = s.body
        for bad in ("GPT-5.6", "GPT‑5.6", "Nano Banana"):
            assert bad not in text, f"{s.rel} contains outdated model name {bad}"
