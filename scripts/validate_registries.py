#!/usr/bin/env python3
"""Validate registries: asset licenses, external source truth, model pointer.

Policies:
- ASSET_REGISTRY: an ACTIVE asset must have license_status CONFIRMED
  (UNKNOWN/RESTRICTED cannot be ACTIVE).
- SOURCE_REGISTRY: an EXTERNAL source with a null URI must be in state
  BLOCKED or MISSING; a source in state AVAILABLE must not carry a BLOCKING
  conflict and must have a non-null last_verified.
- MODEL_CAPABILITY_POINTER: a null/unconfirmed pointer cannot be presented as
  usable (usable must be false and state BLOCKED/MISSING).

No network calls. Exit 0 on success, 1 on any error.
"""
from __future__ import annotations

import os
import sys

import vlib
from vlib import REGISTRIES_DIR


def asset_policy_errors(data) -> list:
    """Pure policy check for ASSET_REGISTRY data. Returns error strings."""
    errors = []
    for a in data.get("assets", []):
        if a.get("status") == "ACTIVE" and a.get("license_status") != "CONFIRMED":
            errors.append(f"asset {a.get('id')} is ACTIVE with license_status "
                          f"{a.get('license_status')} (must be CONFIRMED)")
    return errors


def source_registry_errors(data) -> list:
    """Pure policy check for SOURCE_REGISTRY data. Returns error strings."""
    errors = []
    for s in data.get("sources", []):
        sid = s.get("id")
        state = s.get("state")
        if s.get("status") == "EXTERNAL" and s.get("uri") in (None, ""):
            if state not in ("BLOCKED", "MISSING"):
                errors.append(f"{sid} is EXTERNAL with null URI but state {state} "
                              f"(must be BLOCKED or MISSING)")
        if state == "AVAILABLE":
            if s.get("last_verified") in (None, ""):
                errors.append(f"{sid} is AVAILABLE without last_verified")
            for c in s.get("known_conflicts", []):
                if c.get("severity") == "BLOCKING":
                    errors.append(f"{sid} is AVAILABLE but has a BLOCKING conflict")
    return errors


def model_pointer_errors(data) -> list:
    """Pure policy check for MODEL_CAPABILITY_POINTER data. Returns error strings."""
    errors = []
    no_pointer = data.get("uri") in (None, "") and \
        data.get("repository") in (None, "", "TO_BE_CONFIRMED")
    if no_pointer:
        if data.get("usable") is not False:
            errors.append("no confirmed pointer but usable != false")
        if data.get("state") not in ("BLOCKED", "MISSING"):
            errors.append(f"no confirmed pointer but state {data.get('state')} "
                          "(must be BLOCKED or MISSING)")
    return errors


def main() -> int:
    errors: list[str] = []
    assets = vlib.load_json(os.path.join(REGISTRIES_DIR, "ASSET_REGISTRY.json"))
    for e in vlib.schema_errors(assets, "asset_registry.schema.json"):
        errors.append(f"ASSET_REGISTRY schema: {e}")
    errors += [f"ASSET_REGISTRY: {e}" for e in asset_policy_errors(assets)]

    sreg = vlib.load_json(os.path.join(REGISTRIES_DIR, "SOURCE_REGISTRY.json"))
    for e in vlib.schema_errors(sreg, "source_registry.schema.json"):
        errors.append(f"SOURCE_REGISTRY schema: {e}")
    errors += [f"SOURCE_REGISTRY: {e}" for e in source_registry_errors(sreg)]

    pointer = vlib.load_json(os.path.join(REGISTRIES_DIR, "MODEL_CAPABILITY_POINTER.json"))
    errors += [f"MODEL_CAPABILITY_POINTER: {e}" for e in model_pointer_errors(pointer)]
    print("validate_registries: asset + source + model pointer")
    if errors:
        print(f"\nFAILED with {len(errors)} error(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("validate_registries: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
