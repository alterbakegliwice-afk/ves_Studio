# MIGRATION REPORT — VES Studio v1 → v1.1

**Data:** 2026-07-11

## Liczby

- pliki wejściowe (foundation): **68** (64 Markdown + 4 JSON),
- źródła w repo (`sources/`): **67**,
- aktywne źródła (ACTIVE): **35**,
- PARTIAL: **4**, DRAFT: **5**, SUPERSEDED: **1**,
- placeholdery (ARCHITECTURE_ONLY): **22**,
- pliki Runtime Pack: **8**,
- znormalizowane / naprawione zależności: **91 krawędzi** (wszystkie pełne
  ścieżki), w tym usunięty **1 cykl** i wyeliminowane nienormalizowane
  identyfikatory (`Pliki marek`, `BRAND_SYSTEM`, `schemas`, `wszystkie pliki`).

## Poprawki z audytu

| ID | Poprawka | Status |
|---|---|---|
| K-01 | Runtime Pack (max 8) zamiast archiwum jako runtime | DONE |
| K-02 | Scalenie `VES_VISUAL_STUDIO.md`, oznaczenie SUPERSEDED | DONE |
| K-03 | Walidacja semantyczna (nie tylko obecność plików) | DONE |
| K-04 | Systemy zależne od placeholderów → PARTIAL | DONE |
| K-05 | Routing opisuje cechy zadania; capability w AI Command Center | DONE |
| K-06 | `GPT-5.6 Sol` → rola `VES CREATIVE DIRECTOR` | DONE |
| W-01 | Spójny frontmatter na wszystkich źródłach | DONE |
| W-02 | Zależności jako pełne ścieżki | DONE |
| W-03 | SOURCE_REGISTRY + ASSET_REGISTRY | DONE |
| W-04 | Decision Record typografii AlterBake | DONE |
| W-05 | Dietanka → HYPOTHESES z tagami | DONE |
| W-06 | Rozdział system changelog / project delta | DONE |
| Śr. | DATA_AND_PRIVACY_POLICY, ARTIFACT_NAMING | DONE |

## Migracja VES_VISUAL_STUDIO.md

| Element | Kanoniczne miejsce |
|---|---|
| Wektor zadania / scoring | `sources/01_MASTER_CONTEXT/ROUTING.md` + AI Command Center |
| FRAME-12 | `sources/06_PROMPT_LIBRARY/FRAME_12.md` |
| Pass 0–6, soczewki, matematyka układu | `sources/03_VISUAL_LANGUAGE/STUDIO_WORKFLOW.md` |
| Metryki jakości | `sources/01_MASTER_CONTEXT/QUALITY_GATE.md` |
| Raport końcowy | `sources/09_REVIEW_SYSTEM/FINAL_REVIEW.md` |
| Oryginał | `sources/99_ARCHIVE/VES_VISUAL_STUDIO_v1_SUPERSEDED.md` (SUPERSEDED) |

## Nowe pliki

- `sources/01_MASTER_CONTEXT/DATA_AND_PRIVACY_POLICY.md`
- `sources/05_DOCUMENT_SYSTEM/ARTIFACT_NAMING.md`
- `sources/06_PROMPT_LIBRARY/FRAME_12.md`
- `sources/03_VISUAL_LANGUAGE/STUDIO_WORKFLOW.md`
- `sources/09_REVIEW_SYSTEM/FINAL_REVIEW.md`
- `sources/10_CHANGELOG/decisions/DEC-ALTERBAKE-TYPOGRAPHY-001.md`
- `registries/SOURCE_REGISTRY.json`, `ASSET_REGISTRY.json`,
  `MODEL_CAPABILITY_POINTER.json`
- `schemas/source.schema.json`, `decision_record.schema.json`,
  `source_registry.schema.json`

## Zmiany nazw

- `DIETANKA_BRAND.md` → `DIETANKA_BRAND_HYPOTHESES.md`
  (tagi CONFIRMED / HYPOTHESIS / TO_VALIDATE).

## Wykryte konflikty

1. **Typografia AlterBake** — repo przyjęło `DEC-ALTERBAKE-TYPOGRAPHY-001`
   (Signage Grotesk = szyld/ekspresja, Google Sans = UI/system). Dokument Drive
   `STATUS_ALTERBAKE` nadal pokazuje konflikt → wymaga synchronizacji
   (zapisane w `registries/SOURCE_REGISTRY.json`).
2. **Dietanka** — brak zatwierdzonego brandbooka; repo utrzymuje wyłącznie
   hipotezy.

## Decyzje wymagające Piotrka

- synchronizacja typografii w STATUS_ALTERBAKE (Drive),
- potwierdzenie tokenów produkcyjnych (dziś DRAFT),
- warsztat i awans marki Dietanka do ACTIVE,
- potwierdzenie URL repo AI Command Center (dziś `TO_BE_CONFIRMED`),
- licencje fontów Signage Grotesk / Google Sans.

## Nie zmieniono

Nie zmieniono strategii marki, typografii (poza zapisaniem istniejącej decyzji),
kolorów, logo, tone of voice ani podziału odpowiedzialności modeli bez Decision
Record. Historyczne cytaty w changelogu pozostały nietknięte.
