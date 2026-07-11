# VES STUDIO — REVIEW SYSTEM (runtime)

<!-- SOURCE id=VES-REVIEW-INDEX-001 path=sources/09_REVIEW_SYSTEM/REVIEW_INDEX.md status=ACTIVE version=1.0.0 -->
# REVIEW INDEX

| Review | Stosuj do |
|---|---|
| BRAND_REVIEW | logo, identyfikacja, system marki |
| UI_REVIEW | ekrany, aplikacje, kiosk, narzędzia |
| DASHBOARD_REVIEW | dashboardy i panele danych |
| PDF_REVIEW | dokumenty i raporty PDF |
| PHOTO_REVIEW | zdjęcia i wizualizacje produktu |
| PRESENTATION_REVIEW | prezentacje i decki |
| PROMPT_REVIEW | prompty wielokrotnego użycia |

Każdy review stosuje nadrzędny Quality Gate oraz kryteria domenowe.

---

<!-- SOURCE id=VES-REVIEW-BRAND-001 path=sources/09_REVIEW_SYSTEM/BRAND_REVIEW.md status=ACTIVE version=1.0.0 -->
# BRAND REVIEW

## Strategia

- [ ] Projekt wynika z pozycjonowania, nie trendu.
- [ ] Odbiorca jest jawny.
- [ ] Marka jest odróżnialna od kategorii.
- [ ] Idea daje się opisać jednym zdaniem.

## System

- [ ] Logo działa w wymaganych skalach.
- [ ] Istnieją warianty jednokolorowe.
- [ ] Typografia ma role, nie tylko listę fontów.
- [ ] Kolory są tokenami funkcjonalnymi.
- [ ] Fotografia i ilustracja mają reguły.
- [ ] Layout jest powtarzalny bez monotonii.

## Użycie

- [ ] System działa na szyldzie, social, dokumencie i małym formacie.
- [ ] Nie opiera się na mockupie.
- [ ] Nie wymaga generatora do każdego użycia.
- [ ] Finalne pliki są edytowalne.

## Anti-slop

- [ ] Brak generycznego premium.
- [ ] Brak przypadkowego monogramu.
- [ ] Brak efektu „pierwszy wynik AI”.
- [ ] Brak dekoracji bez funkcji.

---

<!-- SOURCE id=VES-REVIEW-UI-001 path=sources/09_REVIEW_SYSTEM/UI_REVIEW.md status=ACTIVE version=1.0.0 -->
# UI REVIEW

## Cel i przepływ

- [ ] Użytkownik rozumie główną akcję.
- [ ] Najważniejszy scenariusz ma najmniej kroków.
- [ ] Stan pusty, ładowania, błędu i sukcesu są zaprojektowane.
- [ ] Nawigacja jest przewidywalna.

## Hierarchia

- [ ] Jedna dominująca akcja na widok.
- [ ] Etykiety są jednoznaczne.
- [ ] Gęstość odpowiada odbiorcy.
- [ ] Dane i akcje nie konkurują.

## Dostępność

- [ ] Kontrast.
- [ ] Rozmiary dotykowe.
- [ ] Czytelne focus states.
- [ ] Znaczenie nie zależy wyłącznie od koloru.
- [ ] Obsługa reduced motion.

## Produkcja

- [ ] Komponenty i stany są kompletne.
- [ ] Layout działa w docelowych wymiarach.
- [ ] Dane testowe nie udają prawdziwych.
- [ ] Specyfikacja może zostać wdrożona.

---

<!-- SOURCE id=VES-REVIEW-PDF-001 path=sources/09_REVIEW_SYSTEM/PDF_REVIEW.md status=ACTIVE version=1.0.0 -->
# PDF REVIEW

## Treść

- [ ] Cel dokumentu jest jasny.
- [ ] Struktura odpowiada kolejności czytania.
- [ ] Fakty, wnioski i decyzje są rozdzielone.
- [ ] Brak powtórzeń i tekstu zastępczego.

## Layout

- [ ] Spójny grid i marginesy.
- [ ] Hierarchia tytułów jest jednoznaczna.
- [ ] Tabele mieszczą się i są czytelne.
- [ ] Obrazy mają podpisy, gdy potrzebne.
- [ ] Numeracja i nawigacja są poprawne.

## Produkcja

- [ ] Tekst jest tekstem.
- [ ] Linki działają.
- [ ] Fonty są prawidłowo użyte.
- [ ] Brak nachodzenia elementów.
- [ ] Render każdej strony został sprawdzony.
- [ ] Druk w skali szarości działa, jeśli wymagany.

---

<!-- SOURCE id=VES-REVIEW-PHOTO-001 path=sources/09_REVIEW_SYSTEM/PHOTO_REVIEW.md status=ACTIVE version=1.0.0 -->
# PHOTO REVIEW

## Produkt

- [ ] Geometria i proporcje są poprawne.
- [ ] Tekstura wygląda wiarygodnie.
- [ ] Kolor produktu jest zgodny.
- [ ] Nie dodano ani nie usunięto cech produktu.
- [ ] Etykieta i logo są poprawne.

## Światło i przestrzeń

- [ ] Kierunek światła jest spójny.
- [ ] Cień kontaktowy jest wiarygodny.
- [ ] Perspektywa i ogniskowa są logiczne.
- [ ] Tło wspiera produkt.
- [ ] Materiały reagują na światło zgodnie z fizyką.

## Marka

- [ ] Zdjęcie pasuje do systemu marki.
- [ ] Nie jest generycznym food porn.
- [ ] Retusz nie usuwa charakteru.
- [ ] Kadr ma miejsce na wymagane copy.

## AI artifacts

- [ ] Brak błędów etykiety.
- [ ] Brak powtórzonych lub zniekształconych detali.
- [ ] Brak nierealnych odbić.
- [ ] Brak niemożliwej anatomii lub fizyki.

---

<!-- SOURCE id=VES-REVIEW-PRESENTATION-001 path=sources/09_REVIEW_SYSTEM/PRESENTATION_REVIEW.md status=ACTIVE version=1.0.0 -->
# PRESENTATION REVIEW

- [ ] Jedna główna idea na slajd.
- [ ] Narracja prowadzi do decyzji.
- [ ] Tytuły są wnioskami, gdy to możliwe.
- [ ] Dane są czytelne z dystansu.
- [ ] Layouty są zróżnicowane, ale systemowe.
- [ ] Obrazy wspierają argument.
- [ ] Slajdy nie są kopią raportu.
- [ ] Ostatni slajd zamyka decyzję lub działanie.

---

<!-- SOURCE id=VES-REVIEW-FINAL-001 path=sources/09_REVIEW_SYSTEM/FINAL_REVIEW.md status=ACTIVE version=1.0.0 -->
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

Raportuj wartości metryk. Kanoniczna definicja metryk (`grid_adherence`,
`brand_fidelity`, `text_accuracy`, `series_consistency`, `editability`) znajduje
się wyłącznie w `sources/01_MASTER_CONTEXT/QUALITY_GATE.md`, sekcja „Metryki
jakości wizualnej”. Tu ich nie powielaj — odwołaj się do źródła
(`ONE OWNER PER RULE`).

## Zasada

Raport końcowy nie broni koncepcji. Ocenia rezultat tak, jak zrobiłby to
niezależny recenzent bez znajomości promptu.

---

## SOURCE MAP

- `VES-REVIEW-INDEX-001` — `sources/09_REVIEW_SYSTEM/REVIEW_INDEX.md` (status: ACTIVE)
- `VES-REVIEW-BRAND-001` — `sources/09_REVIEW_SYSTEM/BRAND_REVIEW.md` (status: ACTIVE)
- `VES-REVIEW-UI-001` — `sources/09_REVIEW_SYSTEM/UI_REVIEW.md` (status: ACTIVE)
- `VES-REVIEW-PDF-001` — `sources/09_REVIEW_SYSTEM/PDF_REVIEW.md` (status: ACTIVE)
- `VES-REVIEW-PHOTO-001` — `sources/09_REVIEW_SYSTEM/PHOTO_REVIEW.md` (status: ACTIVE)
- `VES-REVIEW-PRESENTATION-001` — `sources/09_REVIEW_SYSTEM/PRESENTATION_REVIEW.md` (status: ACTIVE)
- `VES-REVIEW-FINAL-001` — `sources/09_REVIEW_SYSTEM/FINAL_REVIEW.md` (status: ACTIVE)
