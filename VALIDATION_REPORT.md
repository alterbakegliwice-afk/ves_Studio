# VALIDATION REPORT — VES Studio Core Beta v1.1

**Data:** 2026-07-11
**Werdykt:** PASS (merge gate zielony)

## Zakres

Walidacja strukturalna i **semantyczna** źródeł, rejestrów, polityk i Runtime
Pack. Uruchamiana lokalnie (`scripts/run_merge_gate.sh`) i w CI
(`.github/workflows/validate.yml`).

## Wyniki

| Kontrola | Skrypt | Wynik |
|---|---|---|
| Frontmatter, metadane, stany decyzji | `validate_sources.py` | PASS (67 źródeł, 67 ID) |
| Graf zależności i cykle | `validate_dependencies.py` | PASS (67 węzłów, 91 krawędzi, 0 cykli) |
| Licencje assetów, źródła zewnętrzne, wskaźnik modeli | `validate_registries.py` | PASS |
| Semantyka (eligibility, sync, statusy, rozliczenie, wersja) | `validate_policies.py` | PASS |
| Duplikaty reguł normatywnych | `detect_duplicate_rules.py` | PASS (0 niezwolnionych) |
| Runtime Pack (markery, wersja, checksum) | `validate_runtime.py` | PASS (8 plików) |
| Świeżość runtime | `verify_runtime_freshness.py` | PASS |
| Testy | `pytest` | PASS (34 testy) |

## Statusy release (rozdzielone)

- `repository_status: ACTIVE`
- `release_status: CORE_BETA`
- `runtime_status: BETA`

## Runtime Pack

- 8 plików, wersja z manifestu (1.1.0), deterministyczny checksum źródeł.
- Kompilowane wyłącznie źródła `ACTIVE` (27), 8 ACTIVE+canonical jawnie
  wykluczonych z powodem i właścicielem.
- Brak DRAFT/PARTIAL w runtime; brak wyjątków w tym wydaniu.

## Kontrole polityk (dawne P0)

- [x] Runtime kompiluje wyłącznie `ACTIVE` (P0-01).
- [x] Decyzja pending-sync jest strukturalna i wykluczona z runtime (P0-02).
- [x] `ACTIVE + UNKNOWN license` jest zablokowane; fonty PROVISIONAL (P0-03).
- [x] Źródła EXTERNAL bez URI są BLOCKED/MISSING; null pointer nie jest usable (P0-04).
- [x] Statusy repo/release/runtime rozdzielone i zgodne (P0-05).
- [x] Wersja runtime z manifestu + checksum; brak stałej w kodzie (P0-06).
- [x] Każde `ACTIVE + canonical` jest skompilowane lub jawnie wykluczone (P0-07).

## Decyzja

PASS jako **Core Beta**. System nie jest opisywany jako production-ready.
Otwarte ryzyka: patrz `CLAUDE_CODE_IMPLEMENTATION_REPORT.md` sekcja 5.
