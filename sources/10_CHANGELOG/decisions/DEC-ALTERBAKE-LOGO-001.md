---
id: DEC-ALTERBAKE-LOGO-001
version: 1.0.0
status: DRAFT
owner: Ves
authored_by: Claude Code
review_status: UNREVIEWED
reviewed_by: null
approved_by: null
record_created: "2026-07-27"
decision_date: null
approval_date: null
approval_evidence:
  type: pending
  date: null
  quote: null
  source_ref: "Silnik logo (VES-PROMPT-LOGO-ENGINE-001) — proces do uruchomienia; decyzja i akceptacja Piotrka jeszcze nie podjęte"
  verification_status: PENDING
approval_scope: decision
updated: "2026-07-27"
source_type: decision
scope: brand-alterbake
canonical: false
decision_status: PROPOSED
external_sync_status: PENDING
dependencies: []
---

# DEC-ALTERBAKE-LOGO-001

- **ID:** DEC-ALTERBAKE-LOGO-001
- **Projekt:** AlterBake — Brand System (Logo)
- **Data utworzenia rekordu:** 2026-07-27
- **Data decyzji / akceptacji:** niepodjęta (rekord PROPOSED — patrz `approval_evidence`)
- **Status:** PROPOSED (czeka na uruchomienie silnika i zgodę Piotrka)
- **Decydent:** Piotrek (po biegu silnika)
- **Autor rekomendacji:** Claude Code / VES Studio

## PROBLEM

Temat logo AlterBake pozostaje otwarty: kanon marki wskazuje monogram „AB"-kłos
jako bohatera i jeden wordmark, ale brakuje (1) zamkniętego, zbudowalnego
kierunku znaku, (2) formalnych wersji obowiązkowych (mono / odwrócona / min.
rozmiar), (3) pola ochronnego i tierów responsywnych w pliku, (4) śladu decyzji.
Zadania otwarte kanonu: eksport SVG/EPS, wymiana kartki A4 na szyld.

## KONTEKST I NARZĘDZIE

Rekord jest domknięciem procesu prowadzonego przez silnik
`sources/06_PROMPT_LIBRARY/LOGO_ENGINE.md` (VES-PROMPT-LOGO-ENGINE-001). Silnik
prowadzi stan S0→S12 (intake → strategia → dywergencja ≥3 terytoria → szkic →
scoring 100 pkt → wybór → refine → konstrukcja → stress-test → bramka →
zlecenie wektorowe → pakiet akceptacyjny → lock). Ten Decision Record to pole
S8/S11 silnika — wypełniane danymi z rzeczywistego biegu przed akceptacją.

## ROZWAŻONE WARIANTY (wynik biegu S2–S5, 2026-07-27)

Monogram „AB"-kłos w trzech konstrukcjach; scoring rubryką §6 (100 pkt):

- **T1 — Ciągłość (88/100):** A i B na wspólnej pionowej osi (jeden słupek);
  kłos jako 3–4 ukośne nacięcia (ości) ze wspólnego słupka. Najlepszy w mono i
  skali, „znikające" ości = darmowy tier responsywny.
- **T2 — Metoda (79/100):** monogram z jednego gestu o stałej grubości; grigne
  (nacięcie rzemieślnicze) na brzuchu B. Wnosi 1 gen do T1.
- **T3 — Rytuał wieczorny (dyskwalifikacja):** kłos w kontrformie A/B
  (figure-ground). Hard-fail: pada w hafcie i mono w min. skali. Idea przechodzi
  do systemu (motion/witryna/foto), nie do znaku.

## DECYZJA

**Rekomendacja (PROPOSED, czeka na Piotrka): kierunek T1 „Ciągłość" + gen grigne
z T2.** Domknięcie wg `INSTRUKCJA_WYKONCZENIA_LOGO` (kroki S6–S12): 2 warianty
finalne (z grigne / bez) → stress-test → bramka ≥85 → zlecenie wektorowe
(komplet SVG/EPS/PNG: pełny kolor / mono / odwrócony / tier uproszczony /
lockup) → pakiet dla Piotrka (1 pytanie: wariant A czy B) → lock. Konstrukcja:
pole ochronne = wys. litery wordmarku; monogram ≥ ~10 mm, wordmark ≥ ~25 mm;
jeden wordmark, geometryczna groteska wersalik; font wordmarku = osobna decyzja
(patrz nota konfliktu).

## UZASADNIENIE

T1 najlepiej niesie rdzeń marki (nieprzerwane trwanie miejsca = STARA), jest
najczystszy w mono/hafcie i najlepiej się skaluje; „znikające" ości dają
naturalny tier responsywny (pełny → uproszczony → samo „AB"). Wygrywa w
kryteriach strategii, redukcji i skalowalności; hard-fail wykluczył T3.

## KOSZT I RYZYKO

- **Bramka człowieka (jawna):** AI nie tworzy finalnego pliku znaku — budowa
  wektorowa (SVG/EPS) po stronie grafika. Ten rekord domyka kierunek, nie plik.
- **Data 1908 / nazwisko Willrig/Willrich:** poza znakiem, do weryfikacji
  archiwalnej Piotra; do tego czasu „od ponad 100 lat".
- **Konflikt repo ↔ kanon (font/paleta):** patrz sekcja poniżej.

## WPŁYW NA ŹRÓDŁA

- `sources/06_PROMPT_LIBRARY/LOGO_ENGINE.md` — narzędzie procesu (to źródło).
- `sources/02_BRAND_SYSTEM/ALTERBAKE_BRAND.md` — sekcja Logo (po locku
  zaktualizować o pole ochronne, min. rozmiary, tiery, wersje obowiązkowe).
- `registries/ASSET_REGISTRY.json` — po eksporcie: wpis assetów SVG/EPS logo
  (license_status i status wg rzeczywistego stanu; nie ustawiać ACTIVE bez
  potwierdzonej licencji/fontu).

## NOTA KONFLIKTU repo ↔ kanon

Kanon marki (`kanon_marki_v2026-06-01`) mówi „font logo: zachować obecny (do
potwierdzenia z grafikiem)"; repo przyjęło `DEC-ALTERBAKE-TYPOGRAPHY-001`
(Signage Grotesk = szyld/ekspresja, Google Sans = UI/system) z licencją
NIEPOTWIERDZONĄ (PROVISIONAL). Font logo NIE jest tym samym co font systemowy —
rozstrzygnięcie fontu wordmarku wymaga decyzji Piotrka + grafika i osobnej
synchronizacji. Silnik nie zgaduje kroju wordmarku.

## WARUNEK PONOWNEGO OTWARCIA

Zawsze otwarty do czasu locku (S12). Po locku: nowa decyzja Piotrka lub zmiana
strategii marki.

## ROLLBACK

Porzucenie biegu przywraca stan „logo otwarte" bez wpływu na runtime (silnik i
ten rekord są wykluczone z Runtime Packa / poza always-on).

## ZASTĘPUJE / ZASTĄPIONA PRZEZ

Pierwsza decyzja logo. Nie zastępuje wcześniejszego Decision Record.
