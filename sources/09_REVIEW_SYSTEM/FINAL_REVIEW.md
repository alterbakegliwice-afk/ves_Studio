---
id: VES-REVIEW-FINAL-001
version: 1.0.0
status: ACTIVE
owner: Ves
approved_by: Piotrek
updated: "2026-07-11"
source_type: normative
scope: review-system
canonical: true
dependencies:
  - sources/01_MASTER_CONTEXT/QUALITY_GATE.md
  - sources/09_REVIEW_SYSTEM/REVIEW_INDEX.md
---

# FINAL REVIEW — RAPORT KOŃCOWY

Migrowane z `VES_VISUAL_STUDIO.md` (v1, SUPERSEDED). Kanoniczny format raportu
końcowego dołączanego do każdego większego rezultatu wizualnego.

## Zawartość raportu

Do gotowego rezultatu dołącz krótko:

- wybraną rolę/model wykonawczy i powód wyboru,
- użyte soczewki projektowe,
- elementy niezmienne (BRAND LOCK / INVARIANTS),
- wynik Quality Gate (punkty + brak/hard fail),
- metryki jakości wizualnej (patrz niżej),
- co zostało domknięte w narzędziu produkcyjnym,
- ryzyka przed publikacją lub drukiem.

## Metryki jakości wizualnej

Raportuj wartości metryk zdefiniowanych w `QUALITY_GATE.md`:

- `grid_adherence` — udział kluczowych krawędzi zgodnych z siatką ±2%,
- `brand_fidelity` — zgodność obowiązkowych atrybutów marki,
- `text_accuracy` — liczba poprawnych znaków / liczba znaków,
- `series_consistency` — zgodność stałych cech w całej serii,
- `editability` — procent elementów wymagających ponownego zbudowania.

## Zasada

Raport końcowy nie broni koncepcji. Ocenia rezultat tak, jak zrobiłby to
niezależny recenzent bez znajomości promptu.
