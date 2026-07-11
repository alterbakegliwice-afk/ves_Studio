---
id: VES-VISUAL-LANGUAGE-001
version: 1.0.0
status: ACTIVE
owner: Ves
approved_by: Piotrek
updated: "2026-07-11"
source_type: normative
scope: visual-system
canonical: true
dependencies:
  - sources/01_MASTER_CONTEXT/MASTER_CONTEXT.md
  - sources/01_MASTER_CONTEXT/QUALITY_GATE.md
---

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
