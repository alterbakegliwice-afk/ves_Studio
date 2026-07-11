---
id: VES-ARTIFACT-NAMING-001
version: 1.0.0
status: ACTIVE
owner: Ves
approved_by: Piotrek
updated: "2026-07-11"
source_type: normative
scope: document-system
canonical: true
dependencies:
  - sources/01_MASTER_CONTEXT/MASTER_CONTEXT.md
---

# ARTIFACT NAMING v1

## 1. Wzorzec nazwy

```
YYYY-MM-DD__PROJECT__TYPE__NAME__vX.Y.Z.ext
```

Przykład:

```
2026-07-11__ALTERBAKE__STORY__urlop-jagodzianki__v1.0.0.png
```

## 2. Pola

- `YYYY-MM-DD` — data wersji,
- `PROJECT` — kod projektu / marki (ALTERBAKE, DIETANKA, PERSONAL-OS),
- `TYPE` — typ artefaktu (STORY, MENU, PDF, DECK, PHOTO, UI, LOGO),
- `NAME` — krótki slug bez spacji,
- `vX.Y.Z` — wersja semantyczna artefaktu,
- `ext` — rozszerzenie pliku.

## 3. Zasady

- brak spacji i polskich znaków w slugu,
- separator pól: podwójny podkreślnik `__`,
- separator słów w slugu: pojedynczy myślnik `-`,
- wersja artefaktu rośnie niezależnie od wersji systemu,
- finalny plik produkcyjny nie może mieć sufiksu `draft` bez wersji.

## 4. Relacja do changelogu

Wersja artefaktu należy do **project delta**, nie do systemowego changelogu
(patrz `sources/10_CHANGELOG/CHANGELOG.md` i `REVIEW_CHANGELOG_SYSTEM.md`).
