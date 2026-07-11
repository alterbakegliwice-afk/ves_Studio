# VALIDATION REPORT — VES Studio v1.1

**Data:** 2026-07-11
**Werdykt:** PASS

## Zakres

Walidacja semantyczna źródeł, zależności i Runtime Pack (nie tylko obecność
plików). Uruchamiana lokalnie i w CI (`.github/workflows/validate.yml`).

## Wyniki

| Kontrola | Skrypt | Wynik |
|---|---|---|
| Frontmatter i metadane źródeł | `validate_sources.py` | PASS (67 źródeł, 67 unikalnych ID) |
| Graf zależności i cykle | `validate_dependencies.py` | PASS (67 węzłów, 91 krawędzi, 0 cykli) |
| Sygnał duplikacji reguł | `detect_duplicate_rules.py` | REPORT (bez blokad) |
| Runtime Pack | `validate_runtime.py` | PASS (8 plików) |
| Testy | `pytest` | PASS (17 testów) |

## Statystyka źródeł

| Status | Liczba |
|---|---:|
| ACTIVE | 35 |
| PARTIAL | 4 |
| DRAFT | 5 |
| ARCHITECTURE_ONLY (placeholder) | 22 |
| SUPERSEDED | 1 |
| **Razem** | **67** |

## Kontrole szczegółowe

- [x] Każde aktywne źródło ma kompletny frontmatter (id, wersja, status, owner,
      approved_by, updated, source_type, scope, canonical, dependencies).
- [x] Wszystkie ID unikalne, wersje semantyczne.
- [x] Wszystkie zależności to pełne, rozwiązywalne ścieżki `sources/…`.
- [x] Brak cykli zależności (cykl PROJECT_TEMPLATE ↔ BRIEF_SYSTEM usunięty).
- [x] Żaden plik ACTIVE nie zależy od ARCHITECTURE_ONLY.
- [x] Systemy zależne od placeholderów oznaczone jako PARTIAL.
- [x] Brak zależności ACTIVE/PARTIAL od SUPERSEDED.
- [x] Placeholdery nie są `canonical: true`.
- [x] Runtime Pack ≤ 8 plików, bez placeholderów i treści SUPERSEDED.
- [x] Każdy runtime `.md` ma sekcję `## SOURCE MAP`.
- [x] Brak nieaktualnych nazw modeli i wzorców sekretów w Runtime Pack.
- [x] `VES_VISUAL_STUDIO.md` scalony i oznaczony SUPERSEDED.

## Decyzja

PASS — źródła i Runtime Pack są gotowe do review przez Ves / VES CREATIVE
DIRECTOR.
