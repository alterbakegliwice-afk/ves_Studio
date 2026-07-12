---
id: VES-SOURCE-OF-TRUTH-001
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
scope: governance
canonical: true
dependencies: []
---

# VES STUDIO 2.0 — SOURCE OF TRUTH

**Wersja:** 1.0  
**Status:** obowiązujący  
**Data:** 2026-07-11

## 1. Hierarchia

W razie sprzeczności obowiązuje kolejność:

1. **Najnowsza jednoznaczna decyzja Piotrka.**
2. **Aktualne kanoniczne źródło projektu.**
3. **Aktualny Brand System / Document System / Visual Language.**
4. **Decision Record zatwierdzony przez Piotrka.**
5. **Status projektu.**
6. **Changelog.**
7. **Wcześniejsze rozmowy i pamięć.**
8. **Domysł modelu.**

Domysł nie może nadpisać źródła.

## 2. Typy źródeł

### Źródło normatywne

Definiuje, jak system ma działać:

- Master Context,
- Brand System,
- Visual Language,
- Document System,
- Component Library,
- Review System.

### Źródło stanu

Definiuje, jak jest teraz:

- `STATUS.md`,
- aktywny brief,
- lista blockerów,
- deadline,
- aktywna wersja artefaktu.

### Źródło decyzji

Definiuje, co zostało zatwierdzone i dlaczego:

- `DECISION_RECORD.md`,
- Decision Log.

### Źródło dowodowe

Materiał wejściowy:

- asset,
- zdjęcie,
- dokument,
- dane,
- referencja.

### Artefakt

Wynik projektu. Artefakt nie staje się automatycznie źródłem reguł.

## 3. Aktualność

Każde źródło powinno mieć:

- wersję,
- datę aktualizacji,
- właściciela,
- status: `DRAFT`, `ACTIVE`, `SUPERSEDED`, `ARCHIVED`,
- wskazanie zastępującego pliku, gdy jest przestarzałe.

Dane zmienne wymagają aktualnego sprawdzenia:

- ceny,
- prawo,
- dostępność,
- specyfikacje,
- modele AI,
- funkcje aplikacji,
- harmonogramy i deadline’y.

## 4. Protokół konfliktu

Gdy dwa źródła są sprzeczne:

1. nazwij konflikt,
2. wskaż oba źródła,
3. sprawdź datę, właściciela i status,
4. zastosuj hierarchię,
5. jeżeli nadal brak rozstrzygnięcia — oznacz `BLOCKED`,
6. nie aktualizuj artefaktów zależnych od konfliktu,
7. po decyzji utwórz Decision Record i zsynchronizuj źródła.

## 5. AlterBake

Kanoniczne źródło bieżącego stanu między projektami:

- `STATUS_ALTERBAKE` w Google Drive,
- ID: `13MxzoNH4VDyb7eDgN8bFtZuXmP_kxyaQUvbvfPXffRQ`.

Pliki VES Studio opisują trwały system marki. Nie zastępują bieżącego statusu firmy.

### Znany konflikt do synchronizacji

W Drive występują konkurencyjne zapisy dotyczące typografii:

- status oznacza konflikt Signage Grotesk vs Google Sans jako nierozstrzygnięty,
- najnowsza decyzja Piotrka przyjęta przez VES Studio:  
  **Signage Grotesk — szyld i ekspresja marki; Google Sans — font pomocniczy/systemowy.**

Do czasu aktualizacji dokumentu Drive VES Studio stosuje najnowszą decyzję Piotrka, ale oznacza konieczność synchronizacji źródła.

## 6. Dietanka

Nie istnieje jeszcze kompletny, zatwierdzony dokument źródłowy marki Dietanka.

`DIETANKA_BRAND.md` w wersji v1 jest:

- baseline’em roboczym,
- zbiorem bezpiecznych ograniczeń,
- rejestrem pól wymagających potwierdzenia.

Nie wolno traktować roboczych hipotez jako zatwierdzonego brandbooka.

## 7. Zasada bez duplikacji

Pełna treść reguły znajduje się w jednym miejscu.

Przykład:

- kolor marki → `TOKENS.md`,
- użycie koloru w fotografii → `PHOTO_SYSTEM.md` odwołuje się do tokenu,
- PDF → `PDF_SYSTEM.md` używa tokenu,
- nie kopiuje wartości HEX do trzech dokumentów.

## 8. Aktualizacja źródła

Zmiana trwała wymaga:

- Decision Record,
- aktualizacji pliku kanonicznego,
- wpisu w changelogu,
- sprawdzenia zależności,
- wskazania rollbacku.
