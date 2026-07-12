# VES STUDIO — SYSTEM CHANGELOG

Ten changelog dotyczy **zmian systemowych** (źródeł i reguł). Wersje artefaktów
i status projektów należą do *project delta*, nie tutaj
(patrz `sources/05_DOCUMENT_SYSTEM/REVIEW_CHANGELOG_SYSTEM.md`).

## [2026-07-12] — v1.1.1 CORE BETA (VES review response)

### Co zmieniono

- freshness gate: weryfikacja przed buildem + `git diff` po buildzie; builder
  nie maskuje stale runtime; deterministyczny commit (P0-01),
- decyzja `ACCEPTED`+`PENDING` jest runtime-eligible z ostrzeżeniem (nie pozorne
  wykluczenie); `PROPOSED`/`REJECTED` blokowane (P0-02),
- `07_RUNTIME_REGISTRY.json` zamiast `07_SOURCE_REGISTRY.json` + wykrywanie
  dangling references w runtime (P0-03),
- honest approval model: `authored_by`/`review_status`/`reviewed_by`/
  `approved_by`(nullable)/`approval_date`/`approval_scope`; koniec hurtowego
  `approved_by: Piotrek` (P0-04),
- domain capabilities, changelog policy, split registry state
  (availability/freshness/integrity), single-owner runtime_status, version
  consistency, CI permissions (P1-01…P1-08).

### Dlaczego

VES review PR #2: `REQUEST_CHANGES` — luki semantyczne i proceduralne w merge gate.

### Status

ACTIVE

## [2026-07-11] — v1.1 CORE BETA (red-team fix pack)

### Co zmieniono

- runtime kompiluje wyłącznie źródła `ACTIVE`; kompozycja i wykluczenia jako dane
  w `registries/RUNTIME_COMPOSITION.json` (schema), bez stałych w Pythonie (P0-01, P0-07),
- strukturalny stan decyzji: `decision_status` + `external_sync_status`; decyzja
  typografii AlterBake `ACCEPTED` + `PENDING`, wykluczona z runtime (P0-02),
- polityka licencji assetów: `ACTIVE` wymaga `CONFIRMED`; Signage Grotesk i Google
  Sans → `PROVISIONAL` z fallbackiem (P0-03),
- walidacja rejestru źródeł zewnętrznych: `criticality`, `state`, `severity`;
  AI Command Center `BLOCKED` (brak URI) (P0-04),
- rozdzielone statusy `repository_status` / `release_status` (CORE_BETA) /
  `runtime_status` (P0-05),
- wersja runtime z manifestu + deterministyczny checksum źródeł (P0-06),
- markery reguł `<!-- SOURCE ... -->` w runtime (P1-01), blokada duplikatów
  normatywnych (P1-02), weryfikacja świeżości runtime (P1-03), semantyczny etap
  CI (P1-04),
- nowe walidatory: `validate_registries.py`, `validate_policies.py`,
  `verify_runtime_freshness.py`; merge gate `scripts/run_merge_gate.sh`.

### Dlaczego

Architecture Review + Red Team: zielone CI potwierdzało spójność strukturalną,
ale nie prawdziwość decyzji, licencji, źródeł zewnętrznych ani zgodności statusów.

### Wpływ

- runtime nie zawiera hipotez ani systemów PARTIAL,
- niepotwierdzone licencje i źródła zewnętrzne są jawnie zablokowane,
- release opisany prawdziwie jako Core Beta, nie production-ready.

### Ryzyka

Patrz `CLAUDE_CODE_IMPLEMENTATION_REPORT.md` sekcja 5 (licencje fontów,
AI Command Center, synchronizacja Drive, Dietanka, prompt injection).

### Status

ACTIVE

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
