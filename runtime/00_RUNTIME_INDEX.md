# 00 RUNTIME INDEX

- **Runtime version:** 1.1.0
- **Runtime status:** BETA
- **Release:** VES Studio Core Beta v1.1
- **Build date:** 2026-07-11
- **Source commit:** n/a (nie stemplowany; użyj SOURCE_COMMIT w release/handoff)
- **Source checksum:** sha256:01915260635ca2f0b797b62236ef94868902c40617c75ed772c2aee365cc069b  (kanoniczna identyfikacja runtime)

## Files

- `00_RUNTIME_INDEX.md`
- `01_VES_STUDIO_CORE.md`
- `02_BRAND_CONTEXTS.md`
- `03_VISUAL_SYSTEM.md`
- `04_DOCUMENT_SYSTEM.md`
- `05_PROJECT_SYSTEM.md`
- `06_REVIEW_SYSTEM.md`
- `07_RUNTIME_REGISTRY.json`

## Runtime eligibility

- Kompilowane statusy: ['ACTIVE'] (ACTIVE-only default), review_status ∈ {REVIEWED, APPROVED}.
- Brak wyjątków: żadne źródło DRAFT/PARTIAL nie trafia do runtime.

### Decyzje obowiązujące z ostrzeżeniem (external sync PENDING)

- `DEC-ALTERBAKE-TYPOGRAPHY-001`: external_sync PENDING (obowiązuje z ostrzeżeniem)

## Domain capabilities

- `alterbake` — ACTIVE: Kanoniczny kontekst marki dostępny; stosuj bezpośrednio.
- `dietanka` — HYPOTHESES_ONLY: Brak zatwierdzonego brandbooka. Nie przedstawiaj wyniku jako zgodnego z finalnym brandbookiem; oznacz założenia.
- `personal-os` — DRAFT: Użyj zasad ogólnych Personal OS i oznacz założenia jako robocze.

## Explicitly excluded ACTIVE canonical sources

- `VES-BRAND-INDEX-001` (owner: Ves) — Indeks nawigacyjny Brand System, nie reguła runtime.
- `VES-CHANGELOG-001` (owner: Piotrek) — Systemowy changelog (historia), nie instrukcja dla modelu.
- `VES-ROLLBACK-001` (owner: Piotrek) — Polityka rollbacku repo, poza runtime projektu ChatGPT.
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
