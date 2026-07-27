---
id: VES-PROMPT-LOGO-ENGINE-001
version: 1.0.0
status: ACTIVE
owner: Ves
authored_by: Claude Code
review_status: UNREVIEWED
reviewed_by: null
approved_by: null
approval_date: null
approval_scope: content
updated: "2026-07-27"
source_type: normative
scope: prompt-library
canonical: true
dependencies:
  - sources/02_BRAND_SYSTEM/ALTERBAKE_BRAND.md
  - sources/06_PROMPT_LIBRARY/FRAME_12.md
  - sources/01_MASTER_CONTEXT/QUALITY_GATE.md
---

# ALTERBAKE — SILNIK LOGO v1.0

**Cel:** po wrzuceniu tematu silnik prowadzi proces od briefu do **jednego,
solidnego, zbudowalnego i zatwierdzalnego kierunku znaku**, iteruje w pętli aż
przejdzie bramkę jakości, a następnie **domyka temat logo AlterBake raz na
zawsze** przez zlecenie wektorowe + Decision Record dla Piotra.

Silnik jest zgodny z kanonem marki (`kanon_marki_v2026-06-01`) i systemem VES
Studio (Quality Gate, FRAME-12, anti-slop, honest approval).

---

## 0. JAK URUCHOMIĆ

Wklej do modelu (projekt ChatGPT z Runtime Pack + ten plik):

```
RUN ALTERBAKE_LOGO_ENGINE
TEMAT: <opcjonalnie zawęź, np. „monogram na haft + szyld", inaczej: pełny system>
```

Model wykonuje maszynę stanów S0→S12 bez zatrzymywania się na analizie. Pyta
tylko, gdy odpowiedź zmienia kierunek strategiczny albo dotyka bramki człowieka
(wektor / decyzja Piotra / weryfikacja archiwalna). Każda runda kończy się
kartą oceny; pętla trwa aż do `WARUNEK STOPU`.

### ⛔ REGUŁY NIENARUSZALNE (hard rules — złamanie = automatyczny REJECT)

1. **AI nie tworzy finalnego pliku znaku.** Obrazy z modelu = wyłącznie
   szkice koncepcyjne / studia geometryczne do **odrysowania w wektorze**.
   Każdy prompt kończy się: „TO NIE JEST FINALNY ZNAK — do odbudowy w SVG/EPS".
2. **Terakota (#B5532E) i jakiekolwiek złoto/pszenica NIGDY w logo.** Znak żyje
   w czerni `#141413` na papierze `#EDE7DA` (i wersji odwróconej). Terakota jest
   akcentem opakowań/grafik, nie znaku.
3. **Zero klisz rustykalnych:** worek juty, pole pszenicy, tablica kredowa,
   owalne godła, „vintage" pieczęcie, sepia. Kłos w monogramie jest
   geometrycznym elementem liter, **nie** dekoracyjnym kłosem z banku ikon.
4. **Data i nazwisko pod kontrolą.** Nie wbijaj „1908" ani „Willrig/Willrich" w
   znak. Do potwierdzenia dokumentem obowiązuje „od ponad 100 lat". Weryfikacja
   archiwalna = zadanie Piotra, **nie AI**.
5. **Maks. 2 kroje w całej marce.** Logo: geometryczna groteska wersalik
   (obecna, lekko ścieśniony rozstaw dla ciepła).
6. **Znak musi działać w 1 kolorze, w rewersie i w skali min.** (monogram
   ≥ ~10 mm, wordmark ≥ ~25 mm szer.). Jeśli nie działa — wraca do kierunku.

---

## 1. STRATEGIA ZNAKU (co znak ma powiedzieć)

- **Rdzeń — dwoistość:** STARA (miejsce-piekarnia z czasów Gleiwitz, ciągłość)
  × NA NOWO (minimalizm, metoda „na oko", wieczorny wypiek, młody zespół).
- **Mit MIEJSCA i zespołu**, nie kult właściciela.
- **Hasło przy logo:** „stara piekarnia na nowo" (tożsamościowe). „pieczemy
  inaczej" to hasło kampanijne — **nie** wchodzi do znaku.
- **Architektura znaku (z kanonu §4):**
  - **Monogram „AB"-kłos = BOHATER** — awatar, stempel, metka, haft, winyl.
    Zdolny do pracy samodzielnie.
  - **Jeden podstawowy wordmark** — koniec z wieloma lockupami (to jest luka do
    domknięcia).
  - Monogram nie jest obowiązkowo „przyklejony" do wordmarku — to system:
    monogram solo + wordmark solo + jeden kanoniczny lockup.
- **Różnicowanie (ownability):** konkurencja gra „zał. 1932/1987" + złoto +
  rustykalność. AlterBake robi **odwrotnie**: chłodna geometria mono, mit
  miejsca, rytuał wieczorny. Dystynktywność jest wbudowana strukturalnie.

---

## 2. STANDARDY 2025–2026 (egzekwowane przez kartę oceny)

- **Responsive identity system** (tiery redukcji): pełny lockup → sam wordmark
  → monogram → ikona/favicon 16–32 px → app tile. Każdy tier ma min. rozmiar i
  kontekst.
- **Reduction-first:** projektuj od najmniejszego/1-kolorowego użycia w górę,
  nie odwrotnie.
- **Motion-ready:** znak zbudowany na siatce, jednowagowy, gotowy do prostej
  animacji (bez zależności od efektów).
- **Dostępność:** kontrast pary znak/tło wg WCAG (czerń na papierze i rewers);
  czytelność przy 16 px i przy limicie ściegu haftu.
- **Korekta optyczna, nie tylko matematyka:** overshoot na łukach, spójna waga
  kreski, wyrównania optyczne.
- **Walidacja na realnych nośnikach (mockup-driven):** szyld, winyl na szybie,
  haft na fartuchu, stempel na torbie papierowej, awatar 1:1, favicon.
- **Anti-AI-slop:** brak gradientów AI, glassmorphismu, sparkli, przypadkowego
  monogramu, owalnego godła, fałszywej głębi.
- **Dystynktywność/pamięciowość:** test sylwetki, test zmrużonych oczu, test
  miniatury.
- **Handoff rzemieślniczy:** budowa wektorowa, keyline, ograniczenia
  digitalizacji haftu (min. ścieg ~1 mm → reguła ≥ 10 mm dla monogramu).

---

## 3. WEKTOR ZADANIA (kalibracja rundy — 0–5)

Oceń brief i ustaw wagi: `V` edytowalność wektorowa (zawsze 5), `A` art
direction/koncept (5), `R` zgodność z kanonem (5), `C` spójność systemu
wersji (5), `T` czytelność tekstu/wordmarku (5), `E` precyzja redukcji
(5), `B` liczba wariantów do przeglądu (3–4), `L` presja czasu (wg Piotra).
Fotorealizm `P` = 0 (znak jest wektorowy, nie zdjęciowy). Wynik steruje liczbą
rund dywergencji.

---

## 4. PĘTLA — MASZYNA STANÓW

Każdy stan ma **wejście → działanie → wyjście/bramkę**. Bramka niezaliczona =
powrót do wskazanego stanu. Nie pomijaj stanów.

- **S0 INTAKE.** Zbierz/załóż: zakres (system czy fragment), nośniki docelowe,
  elementy niezmienne, deadline. Braki niekrytyczne oznacz `[ZAŁOŻENIE]`.
  → wyjście: brief w JSON (patrz `BRIEF_SYSTEM`).
- **S1 STRATEGY LOCK.** Zablokuj inwarianty z sekcji 1 + reguły nienaruszalne.
  → wyjście: lista „musi / nie może".
- **S2 DIVERGE.** Wygeneruj **min. 3 terytoria koncepcyjne** różniące się IDEĄ
  (nie kolorem), każde opisane jednym zdaniem. Rekomendowane osie:
  1. **Ciągłość** — monogram jako pieczęć/ciągły ślad (stempel miejsca),
  2. **Metoda** — AB-kłos jako geometryczne cięcie/nacięcie chleba (grigne),
  3. **Rytuał wieczorny** — znak jako światło/okno po zmroku (kontrast masy).
  Odrzuć terytorium, którego nie da się opisać jednym zdaniem.
- **S3 SKETCH.** Dla wybranych terytoriów zrób **studia mono, czerń na
  papierze**, na siatce (patrz biblioteka promptów). Wyłącznie ideacja.
- **S4 SCORE.** Oceń każde studium `KARTĄ OCENY LOGO 100`. Zbierz hard-faile.
- **S5 SELECT.** Wybierz 1 kierunek z wynikiem ≥ 82 i bez hard-fail. Jeśli brak
  → wróć do S2 (nowe terytoria) lub S3 (nowe studia).
- **S6 REFINE.** 2–4 warianty wybranego kierunku, **zmieniając jeden
  kontrolowany parametr na rundę** (proporcja, ścieśnienie, grubość kreski,
  logika kłosa). Loop S6→S4 aż wariant ≥ 90 (READY) albo stabilne 82–89 (PASS).
- **S7 CONSTRUCT.** Zdefiniuj budowę: siatka i geometria, proporcje monogramu,
  rozstaw wordmarku, pole ochronne (= wys. litery wordmarku), min. rozmiary,
  keyline. Zbuduj **3 wersje obowiązkowe** (pełny kolor=mono-czerń / 1-kolor /
  biała odwrócona) + tiery responsywne (wordmark / monogram / favicon).
- **S8 STRESS-TEST.** Uruchom `TESTY WYTRZYMAŁOŚCIOWE` (sekcja 6). Każdy fail →
  powrót do S6 lub S7.
- **S9 GATE.** Quality Gate: wynik ≥ 82 i zero hard-fail we wszystkich wersjach
  i tierach. Zaliczony → S10. Niezaliczony → S2/S6.
- **S10 VECTOR BUILD ORDER.** Wygeneruj **zlecenie wektorowe** (sekcja 7):
  specyfikacja odbudowy w SVG/EPS, warstwy, siatka, warianty, eksporty. To robi
  człowiek/grafik — silnik dostarcza kompletną specyfikację, nie plik.
- **S11 APPROVAL PACKAGE.** Wypełnij **Decision Record** (sekcja 8) + aktualizację
  `ASSET_REGISTRY` + notę konfliktu paleta/font repo↔kanon. Dołącz mockupy i
  kartę oceny końcowej.
- **S12 LOCK.** Po (a) dostarczeniu wektora, (b) zatwierdzeniu Piotra, (c)
  weryfikacji daty/nazwiska — oznacz temat `LOGO LOCKED`, zaktualizuj źródła i
  zamknij zadania otwarte. **Dopiero to zamyka temat na zawsze.**

---

## 5. BIBLIOTEKA PROMPTÓW (FRAME-12, ideacja — NIE finał)

Wszystkie prompty: czerń `#141413` na papierze `#EDE7DA`, jednowagowa kreska,
na siatce, bez koloru, bez tekstur, bez efektów. Zakończenie obowiązkowe:
„TO NIE JEST FINALNY ZNAK — do odrysowania w wektorze."

### P1 — Studium monogramu „AB"-kłos
```
OBJECTIVE: geometryczne studium monogramu AB, w którym litery A i B tworzą
  zarazem stylizowany kłos/nacięcie chleba — jednym ciągłym systemem kreski.
AUDIENCE: piekarnia rzemieślnicza, odbiorca miejski, ceniący minimalizm.
DELIVERABLE: kwadrat 1:1, znak mono na siatce modularnej, wersja pełna i uproszczona.
BRAND LOCK: dwoistość STARA×NA NOWO; chłodna geometria; mit miejsca.
CORE IDEA: „AB jak kłos, kłos jak nacięcie" — dziedzictwo zapisane metodą.
COMPOSITION: siatka, oś pionowa, jeden punkt skupienia, pole ochronne.
SUBJECT: monogram AB + zintegrowany motyw kłosa/grigne (2–5 ziaren/nacięć).
LIGHT/MATERIAL/COLOR: tylko czerń na papierze; brak gradientu; brak złota.
TYPOGRAPHY: wersaliki geometryczne, lekko ścieśnione; bez szeryfów.
REFERENCES: rola = logika konstrukcyjna, nie styl; ZERO owalnych godeł i pieczęci.
MUST: czytelny przy 10 mm i w rewersie. AVOID: kłos „z banku ikon", juta, sepia.
OUTPUT: 1:1, 6–9 wariantów siatkowych.
TO NIE JEST FINALNY ZNAK — do odrysowania w wektorze.
```

### P2 — Studium wordmarku (jeden, ostateczny)
```
OBJECTIVE: jeden wordmark „ALTERBAKE" — wersaliki geometryczne, ścieśniony
  rozstaw dla ciepła, bez ozdobników; kandydat na jedyny kanoniczny.
DELIVERABLE: poziomy, mono, na siatce bazowej; pokaż rozstaw i światła.
CORE IDEA: chłodna forma, ciepły rytm liter.
TYPOGRAPHY: 1 krój, wersaliki; testuj 2–3 warianty trackingu i wagi.
MUST: czytelny przy 25 mm szer. AVOID: ciężki skondensowany „blok",
  charakter browaru/burgerowni/siłowni, chirurgia liter bez uzasadnienia.
OUTPUT: 3–4 warianty rozstawu/wagi. TO NIE JEST FINALNY ZNAK — do wektora.
```

### P3 — Lockup + tiery responsywne
```
OBJECTIVE: jeden kanoniczny lockup (monogram + wordmark) oraz tiery redukcji:
  lockup → sam wordmark → monogram → favicon 16–32 px.
COMPOSITION: relacja monogram/wordmark, wyrównanie optyczne, wspólna siatka.
MUST: każdy tier czytelny w swoim min. rozmiarze; monogram działa solo.
OUTPUT: tablica tierów mono. TO NIE JEST FINALNY ZNAK — do wektora.
```

### P4 — Wersje: mono / rewers
```
OBJECTIVE: znak w 3 obowiązkowych wersjach: pełna (czerń na papierze),
  1-kolor (pełna czerń), odwrócona (papier/biel na czerni #141413).
MUST: identyczna sylwetka i światła we wszystkich; brak cienkich detali
  ginących w rewersie. TO NIE JEST FINALNY ZNAK — do wektora.
```

### P5 — Mockupy walidacyjne (realne nośniki)
```
OBJECTIVE: makiety użycia (nie znak) do oceny: szyld nad witryną, winyl na
  szybie, haft na fartuchu (ciemny), stempel na papierowej torbie, awatar
  Instagram 1:1, favicon w karcie przeglądarki.
BRAND LOCK: fotografia ciemna, editorialowa, ciepłe światło, dużo przestrzeni.
MUST: „zostaw miejsce na logo — nałożę je z wektora". AVOID: wygenerowany znak
  jako finalny. OUTPUT: 6 scen. Logo tylko jako placeholder wektorowy.
```

---

## 6. KARTA OCENY LOGO 100 (+ hard-faile)

| Kryterium | Pkt |
|---|---:|
| Idea i zgodność z rdzeniem (STARA×NA NOWO, mit miejsca) | 20 |
| Dystynktywność / ownability (vs konkurencja, sylwetka, pamięć) | 15 |
| Redukcja i wszechstronność (mono, rewers, favicon 16 px, haft ≥10 mm, grawer) | 20 |
| Konstrukcja i rzemiosło (siatka, korekta optyczna, rozstaw, balans) | 15 |
| Typografia (wersaliki geometryczne, tracking-ciepło, ≤2 kroje) | 10 |
| Paleta i kontrast (czerń+papier, terakota/złoto = 0 w logo, WCAG) | 10 |
| Działanie na nośnikach (szyld, szyba, awatar, stempel, fartuch) | 10 |

**Decyzja:** ≥90 READY · 82–89 PASS · 70–81 REVISE · <70 REJECT DIRECTION.

**Hard-fail (automatyczny REJECT):**
- terakota/złoto/pszenica w znaku;
- klisza: pole pszenicy / juta / owalne godło / vintage-pieczęć / sepia;
- kłos dekoracyjny „z ikony" zamiast elementu konstrukcji liter;
- znak wygenerowany przez AI podany jako finalny (zamiast wektora);
- „1908" lub nazwisko wbite przed weryfikacją archiwalną;
- nieczytelny w min. rozmiarze / w rewersie / w 1 kolorze;
- > 2 kroje; sparkle/przypadkowy monogram; brak wersji wektorowej.

---

## 7. TESTY WYTRZYMAŁOŚCIOWE (S8)

- [ ] **Skala:** favicon 16 px, monogram 10 mm, wordmark 25 mm — czytelne.
- [ ] **1 kolor:** pełna czerń, bez zależności od koloru.
- [ ] **Rewers:** papier/biel na `#141413`, detale nie giną.
- [ ] **Haft:** brak elementów cieńszych niż ~1 mm ściegu; pole ochronne trzyma.
- [ ] **Grawer/stempel:** działa jako jednolity ślad (torba, pieczątka).
- [ ] **Sylwetka/miniatura/zmrużenie:** rozpoznawalny bez detalu.
- [ ] **Dystynktywność:** nie myli się z lokalną konkurencją ani z generic-bakery.
- [ ] **A11y:** kontrast pary znak/tło ≥ WCAG AA dla grafiki.
- [ ] **Bramka dziedzictwa:** brak „1908"/nazwiska w znaku (do weryfikacji).
- [ ] **Mockupy:** szyld / szyba / fartuch / torba / awatar / favicon — OK.

---

## 8. PAKIET DOMKNIĘCIA (S10–S12)

### 8.1. Zlecenie wektorowe (build order — dla grafika)
- odbudować wybrany kierunek w SVG/EPS (krzywe, nie AI-bitmapa);
- warstwy: monogram / wordmark / lockup; wspólna siatka i keyline;
- eksporty: **pełny kolor (czerń/papier), 1-kolor czerń, odwrócona biała**;
  formaty SVG + EPS + PDF; favicon (ICO/SVG) 16/32; PNG podglądowe;
- pole ochronne, min. rozmiary i warianty tierów w pliku specyfikacji;
- plik do haftu (digitalizacja) po zatwierdzeniu.

### 8.2. Decision Record (do zatwierdzenia przez Piotra)
```
ID: DEC-ALTERBAKE-LOGO-001
Projekt: AlterBake — Brand System / Logo
decision_status: PROPOSED   (→ ACCEPTED po zgodzie Piotra)
approved_by: null           (→ Piotrek po decyzji)
approval_evidence: {type: user_statement, verification_status: PENDING}
PROBLEM: wiele lockupów, brak jednego kanonicznego znaku i eksportu wektorowego.
DECYZJA: kanoniczny system = monogram AB-kłos (bohater) + jeden wordmark +
  jeden lockup; paleta znaku: czerń #141413 / papier #EDE7DA; bez terakoty.
UZASADNIENIE: dwoistość STARA×NA NOWO, dystynktywność vs konkurencja, redukcja.
KOSZT/RYZYKO: wektoryzacja + ewentualna korekta u grafika.
WPŁYW NA ŹRÓDŁA: ALTERBAKE_BRAND (typografia/wordmark), ASSET_REGISTRY,
  TOKENS (kolory znaku), zadania_otwarte (eksport SVG/EPS, szyld).
WARUNEK OTWARCIA: nowa decyzja Piotra lub zmiana strategii.
ROLLBACK: poprzedni znak/kartka A4 do czasu wdrożenia.
```

### 8.3. Aktualizacja ASSET_REGISTRY (po locku)
`ASSET-ALTERBAKE-LOGO`: MISSING → **PROVISIONAL/ACTIVE** (po wektorze),
`license_status` wg autorstwa grafika, `canonical_uri` = plik SVG,
`allowed_uses` = [szyld, haft, winyl, awatar, stempel, favicon].

### 8.4. Nota konfliktu (repo ↔ kanon)
Repo `ALTERBAKE_BRAND.md` mówi „Signage Grotesk = szyld"; kanon v2026-06-01
mówi „logo = geometryczna groteska wersalik (obecna)". Hierarchia źródeł: **kanon
Piotra jest nowszy i wygrywa**. Zapisz jako `known_conflict` w SOURCE_REGISTRY i
zsynchronizuj repo osobnym Decision Record (nie po cichu).

---

## 9. WARUNEK STOPU (co znaczy „zamknięte na zawsze")

Temat logo AlterBake jest `LOGO LOCKED`, gdy **wszystkie** prawdziwe:
1. jeden kierunek przeszedł Quality Gate ≥ 82, zero hard-fail, wszystkie wersje
   i tiery zaliczone;
2. istnieją pliki **wektorowe** (SVG/EPS: kolor, mono, rewers) — nie AI-bitmapa;
3. Piotr zatwierdził `DEC-ALTERBAKE-LOGO-001` (approval_evidence VERIFIED);
4. bramka dziedzictwa rozstrzygnięta (data/nazwisko: albo poza znakiem, albo
   po weryfikacji archiwalnej);
5. zaktualizowano ALTERBAKE_BRAND / TOKENS / ASSET_REGISTRY i zamknięto punkty
   „eksport logo" oraz „szyld" w zadaniach otwartych.

Do czasu spełnienia — silnik **nie ogłasza** logo jako finalnego; iteruje albo
czeka na bramkę człowieka, jawnie ją wskazując.

---

## 10. LUKI I ICH DOMKNIĘCIE (plan uzupełnień)

| Luka / niedopatrzenie | Jak silnik domyka |
|---|---|
| Wiele lockupów, brak jednego wordmarku | S6 wybiera 1 kanoniczny; DEC-LOGO-001 |
| Brak eksportu SVG/EPS mono/rewers | S10 build order → zadanie grafika |
| Font logo „do potwierdzenia z grafikiem" | S7 rekomenduje geometryczną grotesk-wersalik + kryteria; flaguje do potwierdzenia |
| Logika kłosa vs zakaz „pszenicy" | S2/S3: kłos = element konstrukcji liter, nie dekoracja; hard-fail pilnuje |
| Brak favicon / app-icon / tierów | S7 tier responsywny + test 16 px |
| Brak pola ochronnego i min. rozmiarów w pliku | S7 formalizuje (= wys. litery; 10/25 mm) |
| Data 1908 / nazwisko niepotwierdzone | bramka dziedzictwa: poza znakiem do weryfikacji Piotra |
| Brak kontroli dystynktywności | test uniqueness vs konkurencja (S8) |
| Brak śladu decyzji / zgody | DEC-ALTERBAKE-LOGO-001 + honest approval |
| Konflikt repo↔kanon (font/paleta) | nota konfliktu + Decision Record synchronizujący |
| Szyld = kartka A4 | po locku: wymiana na wektorowy szyld (zadanie otwarte) |
| Klirens prawny znaku (trademark) | flaga: screening dystynktywności ≠ zastępuje badania prawne; zadanie człowieka |

---

## 11. NOTA UCZCIWOŚCI

Silnik **nie generuje** finalnego znaku obrazem AI — to reguła marki, nie
ograniczenie techniczne. „Wygenerowanie solidnego logo" = doprowadzenie do
jednego, zbudowalnego, zatwierdzonego kierunku i domknięcie go w wektorze +
Decision Record. Trzy bramki pozostają przy człowieku i są jawne: **budowa
wektorowa, zgoda Piotra, weryfikacja archiwalna daty/nazwiska.** Silnik dowozi
wszystko, co potrzebne, by te bramki zamknąć jednym ruchem.
