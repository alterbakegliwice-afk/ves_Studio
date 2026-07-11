---
id: VES-QUALITY-GATE-001
version: 1.1.0
status: ACTIVE
owner: Ves
approved_by: Piotrek
updated: "2026-07-11"
source_type: normative
scope: governance
canonical: true
dependencies: []
---

# VES STUDIO 2.0 — QUALITY GATE

**Wersja:** 1.0  
**Status:** obowiązujący

## 1. Zasada

Pierwsza wersja jest materiałem do review, nie automatycznie rezultatem końcowym.

Każdy większy projekt przechodzi:

1. **Pass A — zgodność z briefem**
2. **Pass B — niezależny review**
3. **Pass C — uproszczenie**
4. **Pass D — kontrolę produkcyjną**

## 2. Skala 100 punktów

| Kryterium | Punkty |
|---|---:|
| Rozwiązanie problemu i idea | 20 |
| Zgodność z marką | 20 |
| Hierarchia i kompozycja | 15 |
| Typografia i tekst | 15 |
| Kolor, kontrast i dostępność | 10 |
| Rzemiosło, materialność i detal | 10 |
| Medium, produkcyjność i eksport | 10 |

## 3. Decyzja

- **90–100:** READY
- **82–89:** PASS
- **70–81:** REVISE
- **poniżej 70:** REJECT DIRECTION
- **hard fail:** automatyczne REJECT

## 4. Hard fail

- błędna nazwa, logo lub claim,
- literówka w finalnym copy,
- brak czytelności kluczowej informacji,
- niewłaściwy format lub wymiar,
- wygenerowane dane przedstawione jako prawdziwe,
- niezgodność z decyzją marki,
- ewidentny artefakt AI,
- brak praw do użycia assetu,
- finalny tekst istnieje wyłącznie jako bitmapa, gdy wymaga edycji,
- plik nie otwiera się lub nie nadaje się do przekazania,
- projekt ignoruje podstawowe ograniczenie briefu.

## 5. Pass A — zgodność

Sprawdź:

- problem,
- cel,
- odbiorcę,
- medium,
- elementy niezmienne,
- wymagane treści,
- definicję sukcesu.

## 6. Pass B — review bez obrony koncepcji

Recenzent ocenia rezultat tak, jakby nie znał promptu ani intencji autora.

Pytania:

- co widzę najpierw,
- co rozumiem po 3 sekundach,
- czy projekt jest charakterystyczny,
- gdzie gubi się informacja,
- co wygląda jak domyślność generatora,
- co nie przetrwa realnego użycia?

## 7. Pass C — uproszczenie

Usuń:

- elementy bez funkcji,
- równorzędne dominanty,
- powtarzające się komunikaty,
- zbędne ramki, karty i dekoracje,
- procesy i komponenty utworzone dla jednego przypadku.

Wymóg: wskaż przynajmniej jedną rzecz, którą można usunąć albo potwierdź, że usunięcie obniży jakość.

## 8. Pass D — produkcja

Sprawdź:

- wymiary,
- spady i margines bezpieczeństwa,
- rozdzielczość,
- profile i format eksportu,
- warstwy edytowalne,
- nazewnictwo plików,
- wersję źródłową,
- wariant mobilny / druk / miniaturę, jeśli wymagane.

## 9. Zamknięcie

Projekt można zamknąć wyłącznie, gdy:

- nie ma hard fail,
- wynik wynosi minimum 82,
- zapisano trwałe decyzje,
- status wskazuje finalny artefakt,
- changelog zawiera zmianę,
- ryzyka pozostałe są jawne.

## 10. Metryki jakości wizualnej

Dla rezultatów wizualnych raportuj (patrz `09_REVIEW_SYSTEM/FINAL_REVIEW.md`):

- `grid_adherence` — udział kluczowych krawędzi zgodnych z siatką ±2%,
- `brand_fidelity` — zgodność obowiązkowych atrybutów marki,
- `text_accuracy` — liczba poprawnych znaków / liczba znaków,
- `series_consistency` — zgodność stałych cech w całej serii,
- `editability` — procent elementów wymagających ponownego zbudowania.
