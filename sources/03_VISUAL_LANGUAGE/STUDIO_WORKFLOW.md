---
id: VES-STUDIO-WORKFLOW-001
version: 1.0.0
status: ACTIVE
owner: Ves
authored_by: Ves
review_status: REVIEWED
reviewed_by: Ves
approved_by: null
approval_date: null
approval_scope: content
updated: "2026-07-11"
source_type: normative
scope: visual-system
canonical: true
dependencies:
  - sources/03_VISUAL_LANGUAGE/VISUAL_LANGUAGE.md
  - sources/01_MASTER_CONTEXT/QUALITY_GATE.md
  - sources/06_PROMPT_LIBRARY/FRAME_12.md
---

# STUDIO WORKFLOW — PASS 0–6

Migrowane z `VES_VISUAL_STUDIO.md` (v1, SUPERSEDED). Kanoniczny proces
produkcji wizualnej VES Studio. Wektor zadania i scoring modeli są opisane jako
cechy zadania; wybór konkretnego modelu należy do AI Command Center
(patrz `sources/01_MASTER_CONTEXT/ROUTING.md`).

## Wektor zadania

Oceń każdą cechę 0–5: `P` fotorealizm, `T` dokładność tekstu, `R` referencje,
`C` spójność serii, `K` wiedza o świecie, `E` precyzyjna edycja, `A` art
direction, `V` edytowalność wektorowa, `B` skala wariantów, `L` presja czasu.

Wagi `w_i` wynikają z briefu. VES Studio przekazuje wektor do AI Command Center,
które wybiera bieżący model. Jeżeli różnica między dwoma najlepszymi modelami
jest mniejsza niż 8%, wykonaj rundę A/B na tym samym briefie i oceń oba wyniki
tym samym Quality Gate.

## Soczewki projektowe

Wybierz maksymalnie dwie soczewki główne i jedną kontrolną: CONCEPT REDUCTION,
GRID SYSTEM, COLOR RELATION, EDITORIAL RHYTHM, FUNCTIONAL RESTRAINT,
MATERIAL PHOTOGRAPHY.

## Pass 0 — brief
Zapisz brief w ustandaryzowanym formacie (patrz `BRIEF_SYSTEM.md`). Nie generuj
przed określeniem elementów niezmiennych.

## Pass 1 — rozbieżność
Wygeneruj 3 kierunki różniące się ideą, nie kolorem: bezpieczny, wyrazisty,
eksperymentalny.

## Pass 2 — selekcja
Odrzuć kierunek, jeżeli nie da się go opisać jednym zdaniem albo nie pozostaje
rozpoznawalny w miniaturze.

## Pass 3 — rozwinięcie
2–4 warianty wybranego kierunku, zmieniając jeden kontrolowany parametr na rundę.

## Pass 4 — krytyk
Oceń bez znajomości promptu: hierarchię, ideę, markę, błędy AI, prawdopodobieństwo
fizyczne i zgodność z medium.

## Pass 5 — produkcja
- Photoshop: retusz, maski, tło, kolor, materialność.
- Figma: siatka, typografia, wektor, komponenty, design system.
- Canva: brand templates, warianty kanałowe, proste materiały.

## Pass 6 — Quality Gate
Projekt przechodzi przy wyniku co najmniej 82/100 i braku hard fail
(patrz `sources/01_MASTER_CONTEXT/QUALITY_GATE.md`). Wynik 70–81 wymaga jednej
rundy korekty. Poniżej 70 wraca do kierunku, nie do kosmetyki.

## Matematyka układu

Dla szerokości `W`, marginesu `m`, guttera `g` i liczby kolumn `n`:

`col = (W - 2m - (n - 1)g) / n`

Punkty startowe: margines 5–8% szerokości, gutter 1,5–3%, baseline 4/6/8 px dla
UI, bezpieczny obszar social min. 6% od krawędzi, długość wiersza 45–75 znaków,
skala typograficzna 1,20–1,333 zależnie od medium.
