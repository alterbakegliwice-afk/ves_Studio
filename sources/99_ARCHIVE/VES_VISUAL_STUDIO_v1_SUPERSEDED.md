---
id: VES-VISUAL-STUDIO-V1
version: 1.0.0
status: SUPERSEDED
owner: Ves
approved_by: Piotrek
updated: "2026-07-11"
source_type: normative
scope: visual-system
canonical: false
superseded_by:
  - sources/03_VISUAL_LANGUAGE/STUDIO_WORKFLOW.md
  - sources/06_PROMPT_LIBRARY/FRAME_12.md
  - sources/09_REVIEW_SYSTEM/FINAL_REVIEW.md
  - sources/01_MASTER_CONTEXT/QUALITY_GATE.md
  - sources/01_MASTER_CONTEXT/ROUTING.md
dependencies: []
---

# VES VISUAL STUDIO v1 — SUPERSEDED

> Ten plik został scalony z kanonicznymi źródłami repozytorium i nie jest już
> aktywnym źródłem. Nie ładuj go do projektu ChatGPT ani do Runtime Pack.

## Dokąd trafiła treść

| Element VES_VISUAL_STUDIO.md | Kanoniczne miejsce |
|---|---|
| Wektor zadania i scoring modeli | `sources/01_MASTER_CONTEXT/ROUTING.md` + AI Command Center |
| FRAME-12 | `sources/06_PROMPT_LIBRARY/FRAME_12.md` |
| Pass 0–6, soczewki, matematyka układu | `sources/03_VISUAL_LANGUAGE/STUDIO_WORKFLOW.md` |
| Metryki (grid_adherence, brand_fidelity, text_accuracy, series_consistency, editability) | `sources/01_MASTER_CONTEXT/QUALITY_GATE.md` |
| Raport końcowy | `sources/09_REVIEW_SYSTEM/FINAL_REVIEW.md` |
| Twarde reguły logo / tekstu / danych / druku | `sources/03_VISUAL_LANGUAGE/VISUAL_LANGUAGE.md` + `QUALITY_GATE.md` |

## Powód

Zasada `ONE OWNER PER RULE`: `VES_VISUAL_STUDIO.md` powielał Quality Gate,
layout, anti-slop, fotografię, routing i procedurę iteracji. Unikalne elementy
zostały przeniesione do właścicieli kanonicznych; reszta usunięta jako duplikat.
