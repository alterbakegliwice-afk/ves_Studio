# VES STUDIO — SYSTEM CHANGELOG

Ten changelog dotyczy **zmian systemowych** (źródeł i reguł). Wersje artefaktów
i status projektów należą do *project delta*, nie tutaj
(patrz `sources/05_DOCUMENT_SYSTEM/REVIEW_CHANGELOG_SYSTEM.md`).

## [2026-07-11] — v1.1 SOURCE NORMALIZATION + RUNTIME PACK

### Co zmieniono

- utworzono kanoniczne repozytorium źródeł (`sources/`, source-first),
- znormalizowano frontmatter wszystkich 67 źródeł (id, wersja, status, owner,
  approved_by, updated, source_type, scope, canonical, dependencies),
- usunięto cykl zależności `PROJECT_TEMPLATE ↔ BRIEF_SYSTEM`,
- scalono unikalne elementy `VES_VISUAL_STUDIO.md` do kanonicznych źródeł
  (FRAME-12, Studio Workflow / Pass 0–6, metryki Quality Gate, Final Review)
  i oznaczono oryginał jako SUPERSEDED w `sources/99_ARCHIVE/`,
- zastąpiono konkretne nazwy modeli rolą `VES CREATIVE DIRECTOR`; capability
  wskazuje `registries/MODEL_CAPABILITY_POINTER.json` (AI Command Center),
- oznaczono systemy zależne od placeholderów jako PARTIAL
  (PDF_SYSTEM, REPORT_SYSTEM, DASHBOARD_REVIEW, PROMPT_REVIEW),
- dodano rejestry: SOURCE_REGISTRY, ASSET_REGISTRY, MODEL_CAPABILITY_POINTER,
- dodano Decision Record `DEC-ALTERBAKE-TYPOGRAPHY-001` (typografia AlterBake),
- zmieniono `DIETANKA_BRAND.md` na `DIETANKA_BRAND_HYPOTHESES.md` z tagami
  CONFIRMED / HYPOTHESIS / TO_VALIDATE,
- dodano `DATA_AND_PRIVACY_POLICY.md` i `ARTIFACT_NAMING.md`,
- dodano walidatory (sources, dependencies, duplicates, runtime), builder
  Runtime Pack, testy pytest i CI GitHub Actions.

### Dlaczego

Audyt v1 (`PASS WITH CONDITIONS`) wskazał: archiwum ≠ runtime, dwa konkurencyjne
źródła zasad wizualnych, zbyt optymistyczną walidację, aktywne systemy zależne
od placeholderów oraz twardo wpisane nazwy modeli.

### Wpływ

- projekt ChatGPT może korzystać z lekkiego Runtime Pack (max 8 plików),
- walidacja jest semantyczna, nie tylko sprawdza obecność plików,
- decyzje trwałe są rozdzielone od bieżącego stanu.

### Ryzyka

- Dietanka nadal bez pełnego brandbooka (hypotheses),
- tokeny produkcyjne w wersji DRAFT,
- STATUS_ALTERBAKE (Drive) wymaga synchronizacji typografii,
- biblioteka komponentów i prompt library pozostają ARCHITECTURE_ONLY.

### Rollback

Przywrócić poprzedni commit `main`; oznaczyć v1.1 jako SUPERSEDED.

### Status

ACTIVE
