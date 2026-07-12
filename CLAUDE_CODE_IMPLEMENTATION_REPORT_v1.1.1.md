# IMPLEMENTATION REPORT — VES Studio Core Beta v1.1.1

**Data:** 2026-07-12
**Snapshot:** branch `claude/new-session-fokyyp` (PR #3)
**Zakres:** VES review PR #2 (P0-01…04, P1-01…08) + review v1.1.1 round 2
(P0-05…08, P1-01…04) + docs/truth fix (P0-09/10).
**Merge gate:** PASSED (`bash scripts/run_merge_gate.sh`).

## P0 — wymagane przed merge

### P0-01 — freshness gate naprawiał błąd przed wykryciem
- Merge gate i CI: kolejność zmieniona — `verify_runtime_freshness` uruchamia się
  **przed** buildem; po buildzie `git diff --exit-code -- runtime/` wymusza brak
  różnicy. Builder nie maskuje stale runtime.
- Runtime jest deterministyczny: `source_commit` nie stempluje już żywego HEAD
  (tylko przez `$SOURCE_COMMIT`), więc rebuild w CI daje zero-diff.
- Prawdziwy test regresyjny `test_stale_committed_runtime_fails_freshness`:
  kopiuje repo do `tmp_path`, zmienia aktywne źródło **bez** rebuildu, uruchamia
  walidator jako subprocess i oczekuje kodu `1`.

### P0-02 — pending-sync było pozornym wykluczeniem
- Zmieniono semantykę: decyzja `ACCEPTED` + `external_sync: PENDING` jest
  **runtime-eligible** (latest Piotrek decision wins). Decision Record jest teraz
  jawnie skompilowany do `02_BRAND_CONTEXTS.md` z ostrzeżeniem
  `⚠️ EXTERNAL SYNC PENDING` przed treścią i w indeksie.
- `SOURCE_REGISTRY` nadal pokazuje konflikt STATUS_ALTERBAKE.
- `PROPOSED`/`REJECTED` nie mogą trafić do runtime (builder + walidator + test).
- Ograniczenie licencyjne fontów jest niezależne od decyzji typograficznej.
- Usunięto `test_pending_decision_not_compiled`; dodano
  `test_accepted_pending_decision_is_runtime_eligible_with_warning` i
  `test_proposed_or_rejected_decision_is_not_runtime_eligible`.

### P0-03 — runtime odwoływał się do plików spoza packa
- `07_SOURCE_REGISTRY.json` zastąpiony przez **`07_RUNTIME_REGISTRY.json`** —
  skompilowane sekcje: `external_sources`, `asset_constraints`
  (z `approved_fallback` lub `NO_APPROVED_FALLBACK`), `model_routing_pointer`,
  `domain_capabilities`.
- Operacyjne odwołania w źródłach przekierowane na `07_RUNTIME_REGISTRY.json`
  (ASSET_POLICY, MASTER_CONTEXT, ROUTING, Decision Record) albo usunięte
  (ARTIFACT_NAMING → changelog).
- `validate_runtime.py` wykrywa **dangling references** — odwołanie do pliku
  spoza packa blokuje build.

### P0-04 — metadane fałszywie deklarowały akceptację Piotrka
- Rozdzielono pola: `authored_by`, `review_status`
  (`UNREVIEWED`/`REVIEWED`/`APPROVED`), `reviewed_by`, `approved_by` (nullable),
  `approval_date`, `approval_scope`. Zmigrowano wszystkie 67 źródeł.
- Reguły w schemacie i walidatorze:
  - `DRAFT`/`PARTIAL`/`ARCHITECTURE_ONLY` nie mogą być `APPROVED`,
  - `approved_by` tylko przy `APPROVED`,
  - decyzja `ACCEPTED` wymaga `approved_by: Piotrek`,
  - runtime kompiluje tylko `review_status ∈ {REVIEWED, APPROVED}`.
- Jedyny `approved_by: Piotrek` to Decision Record typografii (test to sprawdza).

## P1

- **P1-01** domenowy stan (`domain_capabilities`) w Runtime Registry i indeksie:
  alterbake ACTIVE, dietanka HYPOTHESES_ONLY, personal-os DRAFT.
- **P1-02** warunek zamknięcia projektu: status/project delta aktualne; systemowy
  changelog tylko przy zmianie źródła/reguły/komponentu (MASTER_CONTEXT, QUALITY_GATE).
- **P1-03** `source_commit` opcjonalny; kanoniczną identyfikacją jest checksum;
  brak self-referential SHA w commitowanym runtime.
- **P1-04** doprecyzowano: Runtime Pack (8) to kontekst bazowy; limit 7 dotyczy
  dodatkowych źródeł projektowych (ROUTING).
- **P1-05** rozdzielono `availability_state` / `freshness_state` / `integrity_state`
  w SOURCE_REGISTRY (świeżo zweryfikowane ≠ spójne).
- **P1-06** `runtime_status` ma jednego właściciela — manifest; usunięto z kompozycji.
- **P1-07** walidacja zgodności wersji frontmatter vs nagłówek treści.
- **P1-08** `permissions: contents: read` w GitHub Actions.

## Runda 2 — VES review v1.1.1 (P0-05…P0-08, P1-01…P1-04)

- **P0-05** wersja release ujednolicona do `1.1.1` (manifest = rejestry = runtime
  index = STATUS = README); walidator `validate_policies` blokuje dryf.
- **P0-06** `VALIDATION_REPORT.md` zaktualizowany; usunięto twierdzenie „pending-sync
  wykluczona z runtime”; stary raport implementacyjny → 
  `history/reports/2026-07-11__IMPLEMENTATION_REPORT_v1.1.0_SUPERSEDED.md` z bannerem. Top-level ma jeden
  aktualny raport (ten plik).
- **P0-07** fallbacki: `fallback_candidate` + `fallback_status`
  (`NONE`/`PROPOSED`/`APPROVED`) + `fallback_approved_by`. Runtime publikuje
  `approved_fallback` tylko przy `APPROVED`; inaczej `NO_APPROVED_FALLBACK`
  (fonty PROVISIONAL → brak approved fallbacku). Walidator wymusza semantykę.
- **P0-08** proweniencja: `record_created` (data pliku), `decision_date`/
  `approval_date` = `null` (niepotwierdzone), `approval_evidence` wskazuje AI Baton.
  Walidator zabrania `approval_date == updated` i wymaga evidence dla APPROVED.
- **P1-01** merge gate porównuje katalogi (bez `git diff`) — działa na snapshot
  bez `.git`; handoff jest realnie samodzielnie weryfikowalny.
- **P1-02** `personal-os` → `SOURCE_NOT_LOADED` z regułą „nie deklaruj zgodności”.
- **P1-03** `integrity_state`: dodano `UNKNOWN`/`NOT_APPLICABLE`; AI Command Center
  i Dietanka nie są już fałszywie `CONFLICTED` (brak źródła ≠ konflikt treści).
- **P1-04** docstring buildera zgodny z kodem (tylko `$SOURCE_COMMIT`).

## Pozostałe ryzyka (jawne)

- Licencje fontów, URI AI Command Center, synchronizacja Drive, tokeny i Dietanka
  pozostają otwarte (decyzje Piotrka) — bez zgadywania.
- Pinowanie GitHub Actions do commit SHA odłożone do przejścia z Core Beta do
  production (P1-08 opcjonalne).
