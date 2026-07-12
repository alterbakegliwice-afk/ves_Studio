"""Registry policy tests (P0-03, P0-04)."""
import os

import validate_registries as vr
import vlib

REG = vlib.REGISTRIES_DIR


def test_validate_registries_passes():
    assert vr.main() == 0


def test_active_asset_with_unknown_license_fails():
    """P0-03: ACTIVE + UNKNOWN license is rejected."""
    bad = {"assets": [{"id": "ASSET-X", "status": "ACTIVE",
                       "license_status": "UNKNOWN"}]}
    assert vr.asset_policy_errors(bad)
    ok = {"assets": [{"id": "ASSET-X", "status": "ACTIVE",
                      "license_status": "CONFIRMED"}]}
    assert not vr.asset_policy_errors(ok)


def test_current_fonts_are_not_active_with_unknown_license():
    data = vlib.load_json(os.path.join(REG, "ASSET_REGISTRY.json"))
    for a in data["assets"]:
        if a["license_status"] != "CONFIRMED":
            assert a["status"] != "ACTIVE", a["id"]


def test_external_source_missing_uri_must_be_blocked_or_missing():
    """P0-04: EXTERNAL + null URI + AVAILABLE fails."""
    bad = {"sources": [{"id": "SRC-X", "status": "EXTERNAL", "uri": None,
                        "availability_state": "AVAILABLE",
                        "freshness_state": "UNKNOWN", "integrity_state": "CONSISTENT"}]}
    assert vr.source_registry_errors(bad)
    ok = {"sources": [{"id": "SRC-X", "status": "EXTERNAL", "uri": None,
                       "availability_state": "BLOCKED",
                       "freshness_state": "UNKNOWN", "integrity_state": "CONSISTENT"}]}
    assert not vr.source_registry_errors(ok)


def test_available_source_with_blocking_conflict_fails():
    """P1-05: availability AVAILABLE cannot carry a BLOCKING conflict."""
    bad = {"sources": [{"id": "SRC-X", "status": "EXTERNAL",
                        "uri": "https://x", "availability_state": "AVAILABLE",
                        "freshness_state": "CURRENT", "integrity_state": "CONFLICTED",
                        "last_verified": "2026-07-11",
                        "known_conflicts": [{"summary": "c", "severity": "BLOCKING"}]}]}
    assert vr.source_registry_errors(bad)


def test_conflict_requires_conflicted_integrity():
    """P1-05: freshness and integrity are separate — fresh but conflicted is OK,
    but a conflict must be reflected in integrity_state."""
    bad = {"sources": [{"id": "SRC-X", "status": "EXTERNAL", "uri": "https://x",
                        "availability_state": "AVAILABLE", "freshness_state": "CURRENT",
                        "integrity_state": "CONSISTENT", "last_verified": "2026-07-11",
                        "known_conflicts": [{"summary": "c", "severity": "WARNING"}]}]}
    assert vr.source_registry_errors(bad)


def test_null_model_pointer_cannot_be_usable():
    """P0-04: null routing pointer presented as usable fails."""
    bad = {"repository": "TO_BE_CONFIRMED", "uri": None,
           "usable": True, "state": "AVAILABLE"}
    assert vr.model_pointer_errors(bad)
    ok = {"repository": "TO_BE_CONFIRMED", "uri": None,
          "usable": False, "state": "BLOCKED"}
    assert not vr.model_pointer_errors(ok)
