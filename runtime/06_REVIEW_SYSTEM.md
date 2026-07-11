# VES STUDIO — REVIEW SYSTEM (runtime)

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

# DASHBOARD REVIEW

## Decyzja

- [ ] Dashboard wspiera konkretną decyzję.
- [ ] Każda metryka ma właściciela i źródło.
- [ ] Widać stan wymagający działania.
- [ ] Nie ma metryk próżności.

## Dane

- [ ] Jednostki i zakres czasu są jawne.
- [ ] Aktualność danych jest widoczna.
- [ ] Brak danych jest odróżniony od zera.
- [ ] Alert ma próg i reakcję.

## Layout

- [ ] Najważniejsza informacja jest pierwsza.
- [ ] Karty nie są równorzędnym murem.
- [ ] Wykres ma właściwy typ.
- [ ] Kolor ma funkcję semantyczną.
- [ ] Widok działa na docelowym urządzeniu.

## Produkcja

- [ ] Źródła danych istnieją.
- [ ] Błędy i opóźnienia są obsłużone.
- [ ] Dashboard nie udaje automatyzacji, której nie ma.

---

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

# PROMPT REVIEW

## Zastosowanie

- [ ] Wiadomo, kiedy prompt uruchomić.
- [ ] Wiadomo, kiedy go nie używać.
- [ ] Prompt wskazuje wymagane źródła.
- [ ] Nie kopiuje całego Master Context.

## Konstrukcja

- [ ] Cel jest jednoznaczny.
- [ ] Dane wejściowe są rozdzielone od instrukcji.
- [ ] Elementy niezmienne są jawne.
- [ ] Expected output jest określony.
- [ ] Quality Gate jest wskazany.

## Utrzymanie

- [ ] Prompt ma wersję.
- [ ] Ma właściciela.
- [ ] Ma test pozytywny i negatywny.
- [ ] Nie zawiera trwałej reguły istniejącej tylko w promptcie.

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

---

## SOURCE MAP

- `VES-REVIEW-INDEX-001` — `sources/09_REVIEW_SYSTEM/REVIEW_INDEX.md` (status: ACTIVE)
- `VES-REVIEW-BRAND-001` — `sources/09_REVIEW_SYSTEM/BRAND_REVIEW.md` (status: ACTIVE)
- `VES-REVIEW-UI-001` — `sources/09_REVIEW_SYSTEM/UI_REVIEW.md` (status: ACTIVE)
- `VES-REVIEW-DASHBOARD-001` — `sources/09_REVIEW_SYSTEM/DASHBOARD_REVIEW.md` (status: PARTIAL)
- `VES-REVIEW-PDF-001` — `sources/09_REVIEW_SYSTEM/PDF_REVIEW.md` (status: ACTIVE)
- `VES-REVIEW-PHOTO-001` — `sources/09_REVIEW_SYSTEM/PHOTO_REVIEW.md` (status: ACTIVE)
- `VES-REVIEW-PRESENTATION-001` — `sources/09_REVIEW_SYSTEM/PRESENTATION_REVIEW.md` (status: ACTIVE)
- `VES-REVIEW-PROMPT-001` — `sources/09_REVIEW_SYSTEM/PROMPT_REVIEW.md` (status: PARTIAL)
- `VES-REVIEW-FINAL-001` — `sources/09_REVIEW_SYSTEM/FINAL_REVIEW.md` (status: ACTIVE)
