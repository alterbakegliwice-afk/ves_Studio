# VES Studio 2.0 — Architektura

## Decyzja główna

VES Studio jest repozytorium źródeł, reguł, komponentów, decyzji i procedur.
Artefakty końcowe są eksportem systemu. Projekt ChatGPT dostaje skompilowany
Runtime Pack, nie pełne repo (`REPO ≠ RUNTIME`).

## Warstwy

1. Governance — `sources/01_MASTER_CONTEXT`
2. Design system — `sources/02_BRAND_SYSTEM`, `03_VISUAL_LANGUAGE`, `04_COMPONENT_LIBRARY`
3. Output systems — `sources/05_DOCUMENT_SYSTEM`, `06_PROMPT_LIBRARY`
4. Evidence — `sources/07_REFERENCE_LIBRARY`
5. Project execution — `sources/08_PROJECT_TEMPLATE`
6. Quality and history — `sources/09_REVIEW_SYSTEM`, `10_CHANGELOG`, `12_TESTS`
7. Automation and handoffs — `sources/11_AUTOMATION`, `13_SHARED_HANDOFFS`
8. Compilation — `scripts/`, `runtime/`, `schemas/`, `registries/`, `tests/`

## Reguła source-first

Prompt nie może wprowadzać trwałej zasady, której nie ma w źródłach. Nowa reguła
wielokrotnego użycia trafia najpierw do źródła, potem do artefaktu.

## Reguła ładowania

Do jednego zadania ładowane są: MASTER_CONTEXT, ROUTING, właściwy system marki,
właściwy system dokumentu lub komponentów, jeden szablon projektu, jedna
checklista review, aktualny status projektu. Nie ładuje się całego repozytorium.

## Reguła własności

- **Piotrek** zatwierdza trwałe decyzje marki i zmiany krytyczne.
- **Ves** prowadzi system wizualny, spójność, review i decyzje kreatywne.
- **VES CREATIVE DIRECTOR** (rola; bieżący model wskazuje AI Command Center)
  prowadzi art direction, projektowanie systemów i final review.
- **Źródło operacyjne (Claude)** prowadzi operacyjny trzon piekarni oraz kod
  i automatyzację.
- **Operator Workspace (Gemini)** prowadzi natywne przepływy Google Workspace
  i operacje masowe na dokumentach.

## Statusy (rozdzielone)

Dojrzałość opisują trzy niezależne pola w `ves-studio.manifest.json`:

- `repository_status` — czy repo działa i jest utrzymywane,
- `release_status` — dojrzałość wydania (obecnie `CORE_BETA`),
- `runtime_status` — dojrzałość Runtime Pack (obecnie `BETA`, ACTIVE-only).

Jedno pole nie opisuje trzech różnych rzeczy.

## Warstwa kompilacji

- `scripts/validate_sources.py` — frontmatter, metadane, stany decyzji,
- `scripts/validate_dependencies.py` — graf zależności i cykle,
- `scripts/validate_registries.py` — licencje assetów, prawda źródeł zewnętrznych,
  wskaźnik modeli,
- `scripts/validate_policies.py` — semantyka: eligibility runtime, sync decyzji,
  spójność statusów, rozliczenie źródeł, jedna wersja,
- `scripts/detect_duplicate_rules.py` — blokada zduplikowanych reguł normatywnych,
- `scripts/build_runtime_pack.py` — kompilacja Runtime Pack (ACTIVE-only, dane
  w `registries/RUNTIME_COMPOSITION.json`),
- `scripts/validate_runtime.py` — kontrola Runtime Pack (markery, wersja, checksum),
- `scripts/verify_runtime_freshness.py` — czy runtime = bieżące źródła.

Runtime kompiluje wyłącznie źródła `ACTIVE`. Każde `ACTIVE + canonical` źródło
jest albo skompilowane, albo jawnie wykluczone (z powodem i właścicielem) w
`registries/RUNTIME_COMPOSITION.json`.

## Cykl zmiany

1. Zmiana powstaje w wersji roboczej.
2. Przechodzi review domenowe.
3. Przechodzi kontrolę sprzeczności i duplikatów.
4. Otrzymuje wpis w changelogu.
5. Zmiana krytyczna wymaga zatwierdzenia Piotrka.
6. Dopiero wtedy staje się źródłem prawdy.
