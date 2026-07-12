# 00 RUNTIME INDEX

- **Runtime version:** 1.1.0
- **Runtime status:** BETA
- **Release:** VES Studio Core Beta v1.1
- **Build date:** 2026-07-11
- **Source commit:** 27fedacf388596d9b61ce9bb94640d623491e740
- **Source checksum:** sha256:106444e2e21b6cc7b26a1350bdf531430f7076c86c063482c6cdab05a09ed7fb

## Files

- `00_RUNTIME_INDEX.md`
- `01_VES_STUDIO_CORE.md`
- `02_BRAND_CONTEXTS.md`
- `03_VISUAL_SYSTEM.md`
- `04_DOCUMENT_SYSTEM.md`
- `05_PROJECT_SYSTEM.md`
- `06_REVIEW_SYSTEM.md`
- `07_SOURCE_REGISTRY.json`

## Runtime eligibility

- Kompilowane statusy: ['ACTIVE'] (ACTIVE-only default).
- Brak wyjątków: żadne źródło DRAFT/PARTIAL nie trafia do runtime.

## Explicitly excluded ACTIVE canonical sources

- `VES-BRAND-INDEX-001` (owner: Ves) — Indeks nawigacyjny Brand System, nie reguła runtime.
- `VES-CHANGELOG-001` (owner: Piotrek) — Systemowy changelog (historia), nie instrukcja dla modelu.
- `VES-ROLLBACK-001` (owner: Piotrek) — Polityka rollbacku repo, poza runtime projektu ChatGPT.
- `DEC-ALTERBAKE-TYPOGRAPHY-001` (owner: Piotrek) — Decyzja z external_sync_status=PENDING; nie może być bezwarunkową regułą runtime do czasu synchronizacji Drive.
- `VES-GOLDEN-CASES-001` (owner: Ves) — Materiał testowy/regresyjny, nie reguła runtime.
- `VES-TEST-MATRIX-001` (owner: Ves) — Macierz testów, nie reguła runtime.
- `VES-HANDOFF-CLAUDE-001` (owner: Piotrek) — Handoff międzymodelowy, poza rdzeniem runtime STUDIO.
- `VES-HANDOFF-GEMINI-001` (owner: Piotrek) — Handoff międzymodelowy, poza rdzeniem runtime STUDIO.

## Known limitations

- Release to Core Beta: część systemów (Component/Prompt/Reference/Automation) pozostaje poza runtime.
- Konkretne modele wykonawcze wskazuje AI Command Center (obecnie BLOCKED — brak URI).
- Typografia AlterBake: decyzja przyjęta, synchronizacja Drive PENDING.
- Fonty Signage Grotesk / Google Sans: licencja NIEPOTWIERDZONA (PROVISIONAL).

## SOURCE MAP

- Index generowany przez `scripts/build_runtime_pack.py` z `registries/RUNTIME_COMPOSITION.json` i `sources/`.
