"""Semantic policy tests (P0-01, P0-02, P0-05, P0-07, P1-04)."""
import copy

import validate_policies as vp
import vlib


def test_validate_policies_passes():
    assert vp.main() == 0


def test_new_active_canonical_without_composition_fails():
    """P0-07: adding an unaccounted ACTIVE canonical source fails."""
    comp = vlib.composition()
    by_id = vlib.sources_by_id()
    # fabricate a new ACTIVE canonical source not in composition/exclusions
    fake = copy.copy(next(iter(by_id.values())))

    class S:  # minimal stand-in matching attributes used by the checker
        sid = "VES-FAKE-UNACCOUNTED-001"
        status = "ACTIVE"
        meta = {"canonical": True}
    by_id2 = dict(by_id)
    by_id2[S.sid] = S()
    assert vp.source_accounting_errors(by_id2, comp)


def test_draft_in_composition_is_rejected():
    """P0-01: a DRAFT/PARTIAL id placed in composition fails eligibility."""
    comp = copy.deepcopy(vlib.composition())
    by_id = vlib.sources_by_id()
    # inject a real DRAFT source id into the first target
    comp["targets"][0]["sources"].append("VES-BRAND-DIETANKA-001")
    assert vp.runtime_eligibility_errors(by_id, comp)
    # unmodified composition is clean
    assert vp.runtime_eligibility_errors(by_id, vlib.composition()) == []


def test_all_current_active_canonical_accounted():
    comp = vlib.composition()
    by_id = vlib.sources_by_id()
    assert vp.source_accounting_errors(by_id, comp) == []


def test_pending_decision_not_compiled():
    """P0-02: a decision with external_sync_status != SYNCED is excluded."""
    comp = vlib.composition()
    compiled = {sid for t in comp["targets"] for sid in t["sources"]}
    by_id = vlib.sources_by_id()
    for s in by_id.values():
        if s.meta.get("source_type") == "decision":
            if s.meta.get("external_sync_status") != "SYNCED":
                assert s.sid not in compiled, s.sid


def test_typography_decision_has_structured_sync_state():
    by_id = vlib.sources_by_id()
    dec = by_id["DEC-ALTERBAKE-TYPOGRAPHY-001"]
    assert dec.meta.get("decision_status") == "ACCEPTED"
    assert dec.meta.get("external_sync_status") == "PENDING"


def test_manifest_has_split_status():
    """P0-05: repository/release/runtime statuses are separate."""
    m = vlib.manifest()
    for field in ("repository_status", "release_status", "runtime_status"):
        assert field in m
    assert m["release_status"] == "CORE_BETA"


def test_no_hardcoded_runtime_version_constant():
    """P0-06: builder has no RUNTIME_VERSION constant."""
    import os
    import re
    src = open(os.path.join(vlib.REPO_ROOT, "scripts", "build_runtime_pack.py"),
               encoding="utf-8").read()
    assert not re.search(r"^\s*RUNTIME_VERSION\s*=", src, re.M)
