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


def test_accepted_pending_decision_is_runtime_eligible_with_warning():
    """P0-02: ACCEPTED + PENDING decision compiles (latest Piotrek decision wins)
    but the runtime index must warn and the registry must still show the conflict."""
    comp = vlib.composition()
    by_id = vlib.sources_by_id()
    compiled = {sid for t in comp["targets"] for sid in t["sources"]}
    dec = by_id["DEC-ALTERBAKE-TYPOGRAPHY-001"]
    assert dec.meta.get("decision_status") == "ACCEPTED"
    assert dec.meta.get("external_sync_status") == "PENDING"
    assert dec.sid in compiled, "ACCEPTED decision should be runtime-eligible"
    # runtime index warns about the pending sync
    import os
    idx = os.path.join(vlib.RUNTIME_DIR, "00_RUNTIME_INDEX.md")
    if os.path.isfile(idx):
        assert dec.sid in open(idx, encoding="utf-8").read()
    # SOURCE_REGISTRY still exposes the conflict
    reg = vlib.load_json(os.path.join(vlib.REGISTRIES_DIR, "SOURCE_REGISTRY.json"))
    summaries = " ".join(c["summary"] for s in reg["sources"]
                         for c in s.get("known_conflicts", [])).lower()
    assert "signage" in summaries or "typograf" in summaries


def test_proposed_or_rejected_decision_is_not_runtime_eligible():
    """P0-02: only ACCEPTED decisions may compile."""
    comp = vlib.composition()
    by_id = dict(vlib.sources_by_id())

    class D:
        sid = "DEC-FAKE-PROPOSED"
        status = "ACTIVE"
        meta = {"source_type": "decision", "decision_status": "PROPOSED",
                "review_status": "REVIEWED"}
    by_id[D.sid] = D()
    comp2 = copy.deepcopy(comp)
    comp2["targets"][0]["sources"].append("DEC-FAKE-PROPOSED")
    assert vp.runtime_eligibility_errors(by_id, comp2)


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
