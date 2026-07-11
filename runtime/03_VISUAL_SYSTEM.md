# VES STUDIO — VISUAL SYSTEM (runtime)

# VES STUDIO — VISUAL LANGUAGE v1

## 1. Cel

Zdefiniować zasady niezależne od narzędzia i marki.

Visual Language opisuje relacje, nie dekoracje.

## 2. Hierarchia

Każdy layout ma:

1. dominantę,
2. informację wspierającą,
3. metadane lub akcję.

Nie twórz więcej niż dwóch równorzędnych dominant.

### Test 3 sekund

Po 3 sekundach odbiorca powinien wiedzieć:

- czego dotyczy materiał,
- co jest najważniejsze,
- co zrobić dalej, jeżeli istnieje CTA.

## 3. Kontrast

Kontrast może wynikać z:

- skali,
- masy,
- koloru,
- pozycji,
- rytmu,
- pustej przestrzeni,
- materiału,
- ruchu.

Nie próbuj zwiększać wszystkiego jednocześnie.

## 4. Rytm

Rytm tworzą:

- powtarzalne odstępy,
- kontrolowane zmiany skali,
- sekwencja gęstość → pauza → akcent,
- powtórzenie komponentu z celową zmianą.

Powtórzenie bez zmiany tworzy monotonię. Zmiana bez systemu tworzy chaos.

## 5. Skala

Domyślna skala typograficzna:

- funkcjonalna: 1,20,
- editorial: 1,25,
- ekspresyjna: 1,333.

Wybierz jedną skalę na system. Nie dobieraj każdego rozmiaru osobno.

## 6. Grid

Najczęstsze siatki:

- 4 kolumny — mobile i proste dokumenty,
- 6 kolumn — editorial i social,
- 12 kolumn — dashboardy i złożone layouty.

Dla szerokości `W`, marginesu `m`, guttera `g` i liczby kolumn `n`:

`col = (W - 2m - (n - 1)g) / n`

Punkt startowy:

- margines: 5–8% szerokości,
- gutter: 1,5–3% szerokości,
- bezpieczny obszar social: minimum 6% od krawędzi.

## 7. Spacing

Używaj ograniczonej skali odstępów.

Relacje:

- odstęp wewnątrz grupy < odstęp między grupami,
- odstęp między sekcjami > odstęp między akapitami,
- komponenty tej samej klasy mają ten sam rytm.

## 8. Gęstość informacji

Oceń gęstość 1–10:

- 1–3: hero, plakat, obraz narracyjny,
- 4–6: social, karta, PDF,
- 7–8: raport, dashboard,
- 9–10: wyłącznie narzędzie eksperckie i z silną hierarchią.

Nie mieszaj lekkiego stylu z przypadkowo zatłoczonym środkiem.

## 9. Typografia

- maksymalnie dwie rodziny w jednym systemie,
- długość wiersza: 45–75 znaków,
- tekst główny musi mieć komfortowy kontrast,
- label nie może konkurować z wartością,
- wielkie litery są akcentem, nie domyślnym formatem długiego tekstu,
- tracking i leading wynikają z funkcji i kroju.

## 10. Kolor

- kolor działa relacyjnie,
- jeden dominujący akcent,
- drugi akcent wyłącznie z funkcją semantyczną,
- neutralne powinny mieć spójną temperaturę,
- nie używaj koloru jako jedynego nośnika znaczenia,
- sprawdzaj kontrast i skalę szarości.

## 11. Kompozycja

Preferuj:

- jedno napięcie,
- kontrolowaną asymetrię,
- świadome kadrowanie,
- negatywną przestrzeń jako aktywny element,
- konsekwentną oś.

Unikaj:

- przypadkowego centrowania wszystkiego,
- automatycznego układu trzech kart,
- dekoracyjnej symetrii,
- elementów unoszących się bez zakotwiczenia.

## 12. Światło i głębia

W fotografii i mockupach określ:

- źródło światła,
- kierunek,
- twardość,
- wypełnienie,
- cień kontaktowy,
- perspektywę,
- ogniskową,
- głębię ostrości.

Cień nie służy do „upiększenia”. Ma wyjaśniać przestrzeń.

## 13. Ikonografia i ilustracja

- jedna rodzina geometrii,
- jedna grubość linii lub jawny system wariantów,
- ikona musi wspierać rozpoznanie,
- ilustracja ma wyjaśniać, budować świat lub nadawać charakter.

Nie dodawaj ilustracji jako wypełnienia pustego miejsca.

## 14. Anti-slop

Odrzucaj jako domyślne:

- gradient AI purple/blue,
- glassmorphism,
- dekoracyjny HUD,
- sparkles,
- przypadkowy grain,
- bezpodstawne „premium”,
- fałszywe metryki,
- karty o identycznej wadze,
- przypadkowy monogram,
- mockup maskujący słaby projekt.

## 15. Test miniatury

Projekt musi zachować:

- dominantę,
- podstawowy kontrast,
- charakterystyczną sylwetkę,
- markę,

po zmniejszeniu do typowego realnego rozmiaru.

---

# LAYOUT SYSTEM v1

## Metryki podstawowe

- grid adherence: minimum 85% kluczowych krawędzi na siatce,
- maksymalnie 2 dominujące osie,
- maksymalnie 3 poziomy hierarchii na pojedynczym ekranie lub małym formacie,
- bezpieczne marginesy wynikają z medium.

## Breakpointy logiczne

Nie kopiuj breakpointów automatycznie. Zmieniaj layout, gdy:

- długość wiersza przekracza zakres,
- CTA traci widoczność,
- dwie kolumny nie mieszczą treści,
- hierarchia zmienia kolejność czytania.

## Dokumenty

- A4: preferuj siatkę 6 lub 12 kolumn,
- prezentacja: 12 kolumn, ale 1 główna idea na slajd,
- Instagram 4:5: 6 kolumn,
- Story 9:16: 4 lub 6 kolumn,
- dashboard: 12 kolumn.

## Zasada odstępów

Najpierw ustaw layout w czerni, bieli i szarości. Kolor nie może naprawiać złej struktury.

---

# PHOTO SYSTEM v1

## Cel

Fotografia ma budować wiarygodność produktu i marki, nie demonstrować możliwości generatora.

## Brief zdjęcia

Zawsze określ:

- obiekt,
- cel,
- medium,
- kadr,
- punkt widzenia,
- ogniskową,
- światło główne,
- wypełnienie,
- tło i powierzchnię,
- stopień retuszu,
- elementy niezmienne.

## Produkt

Zachowaj:

- geometrię,
- proporcje,
- teksturę,
- oznaczenia,
- kolor produktu,
- cechy charakterystyczne.

## Retusz

Dozwolony:

- korekta ekspozycji,
- usunięcie przypadkowych zabrudzeń,
- korekta tła,
- kontrola koloru,
- poprawa separacji produktu.

Niedozwolony:

- zmiana produktu w inną wersję,
- wygładzenie usuwające rzemieślniczy charakter,
- fałszywa obfitość,
- błędne etykiety,
- nierealne odbicia i cienie.

## Seria

Stałe:

- temperatura światła,
- perspektywa,
- wysokość aparatu,
- charakter cienia,
- poziom kontrastu,
- proporcja pustej przestrzeni.

Zmienna powinna być jawna: produkt, kolor tła, gest albo kadr.

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

---

# FRAME-12 — SZKIELET PROMPTU PRODUKCYJNEGO

Migrowane z `VES_VISUAL_STUDIO.md` (v1, SUPERSEDED). Kanoniczny szkielet
promptu obrazowego dla VES Studio.

## Kolejność

1. **OBJECTIVE** — co ma osiągnąć obraz.
2. **AUDIENCE** — dla kogo.
3. **DELIVERABLE** — format i medium.
4. **BRAND LOCK** — elementy niezmienne.
5. **CORE IDEA** — jedna idea lub metafora.
6. **COMPOSITION** — siatka, kadrowanie, hierarchia.
7. **SUBJECT** — produkt, postać lub obiekt.
8. **LIGHT / MATERIAL / COLOR** — fizyczność i paleta.
9. **TYPOGRAPHY** — treść, pozycja, charakter; albo jawnie bez tekstu.
10. **REFERENCES** — rola każdej referencji, nie samo „inspiruj się”.
11. **MUST / AVOID** — warunki konieczne i zakazy.
12. **OUTPUT** — proporcje, rozdzielczość, liczba wariantów.

## Edycja istniejącego obrazu

Przy edycji dodaj sekcję **INVARIANTS**: lista elementów, których model nie
może zmienić (produkt, logo, tekst, proporcje, kolor produktu).

## Zasada

FRAME-12 jest strukturą promptu, nie zbiorem trwałych reguł marki. Reguły marki
pozostają w plikach `02_BRAND_SYSTEM/` i `03_VISUAL_LANGUAGE/`.

---

## SOURCE MAP

- `VES-VISUAL-LANGUAGE-001` — `sources/03_VISUAL_LANGUAGE/VISUAL_LANGUAGE.md` (status: ACTIVE)
- `VES-LAYOUT-001` — `sources/03_VISUAL_LANGUAGE/LAYOUT_SYSTEM.md` (status: ACTIVE)
- `VES-PHOTO-001` — `sources/03_VISUAL_LANGUAGE/PHOTO_SYSTEM.md` (status: ACTIVE)
- `VES-STUDIO-WORKFLOW-001` — `sources/03_VISUAL_LANGUAGE/STUDIO_WORKFLOW.md` (status: ACTIVE)
- `VES-PROMPT-FRAME12-001` — `sources/06_PROMPT_LIBRARY/FRAME_12.md` (status: ACTIVE)
