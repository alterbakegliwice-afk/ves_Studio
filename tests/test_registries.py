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
                        "state": "AVAILABLE"}]}
    assert vr.source_registry_errors(bad)
    ok = {"sources": [{"id": "SRC-X", "status": "EXTERNAL", "uri": None,
                       "state": "BLOCKED"}]}
    assert not vr.source_registry_errors(ok)


def test_available_source_with_blocking_conflict_fails():
    bad = {"sources": [{"id": "SRC-X", "status": "EXTERNAL",
                        "uri": "https://x", "state": "AVAILABLE",
                        "last_verified": "2026-07-11",
                        "known_conflicts": [{"summary": "c", "severity": "BLOCKING"}]}]}
    assert vr.source_registry_errors(bad)


def test_null_model_pointer_cannot_be_usable():
    """P0-04: null routing pointer presented as usable fails."""
    bad = {"repository": "TO_BE_CONFIRMED", "uri": None,
           "usable": True, "state": "AVAILABLE"}
    assert vr.model_pointer_errors(bad)
    ok = {"repository": "TO_BE_CONFIRMED", "uri": None,
          "usable": False, "state": "BLOCKED"}
    assert not vr.model_pointer_errors(ok)
