# VES STUDIO — DOCUMENT SYSTEM (runtime)

<!-- SOURCE id=VES-BRIEF-001 path=sources/05_DOCUMENT_SYSTEM/BRIEF_SYSTEM.md status=ACTIVE version=1.0.0 -->
# BRIEF SYSTEM v1

## Minimalny brief

1. Problem
2. Cel
3. Odbiorca
4. Medium i format
5. Istniejące aktywa
6. Elementy niezmienne
7. Ograniczenia
8. Treść obowiązkowa
9. Czego unikać
10. Definicja sukcesu
11. Termin
12. Osoba zatwierdzająca

## Założenia

Brakujące dane oznacz jako:

- `[ZAŁOŻENIE ROBOCZE]` — można rozpocząć,
- `[BLOCKER]` — nie można bezpiecznie kontynuować,
- `[DO POTWIERDZENIA]` — wynik możliwy, ale nie finalny.

## Kryterium dobrego briefu

Inna osoba lub model może rozpocząć pracę bez odtwarzania rozmowy.

---

<!-- SOURCE id=VES-PRESENTATION-001 path=sources/05_DOCUMENT_SYSTEM/PRESENTATION_SYSTEM.md status=ACTIVE version=1.0.0 -->
# PRESENTATION SYSTEM v1

## Zasada

Jedna główna idea na slajd.

## Sekwencja

- kontekst,
- problem,
- napięcie,
- dowód,
- decyzja,
- plan,
- zamknięcie.

## Wymogi

- różnorodność layoutów bez utraty systemu,
- obraz ma mieć funkcję,
- nie kopiuj raportu do slajdów,
- slajd powinien działać z wypowiedzią prowadzącego,
- dane muszą być czytelne z dystansu.

---

<!-- SOURCE id=VES-BATON-001 path=sources/05_DOCUMENT_SYSTEM/AI_BATON_SYSTEM.md status=ACTIVE version=1.0.0 -->
# AI BATON SYSTEM v1

## Cel

Przekazać zadanie między modelami bez utraty decyzji, źródeł i ograniczeń.

## Struktura

1. Nazwa zadania
2. Cel biznesowy
3. Aktualny stan
4. Źródła prawdy
5. Zatwierdzone decyzje
6. Otwarte konflikty
7. Zakres odbiorcy batonu
8. Czego nie zmieniać
9. Oczekiwany rezultat
10. Quality Gate
11. Pliki wejściowe
12. Miejsce zapisu wyniku
13. Następny właściciel

## Zasada

Baton nie może zawierać ukrytej decyzji. Założenia, fakty i polecenia muszą być rozdzielone.

---

<!-- SOURCE id=VES-ARTIFACT-NAMING-001 path=sources/05_DOCUMENT_SYSTEM/ARTIFACT_NAMING.md status=ACTIVE version=1.0.0 -->
# ARTIFACT NAMING v1

## 1. Wzorzec nazwy

```
YYYY-MM-DD__PROJECT__TYPE__NAME__vX.Y.Z.ext
```

Przykład:

```
2026-07-11__ALTERBAKE__STORY__urlop-jagodzianki__v1.0.0.png
```

## 2. Pola

- `YYYY-MM-DD` — data wersji,
- `PROJECT` — kod projektu / marki (ALTERBAKE, DIETANKA, PERSONAL-OS),
- `TYPE` — typ artefaktu (STORY, MENU, PDF, DECK, PHOTO, UI, LOGO),
- `NAME` — krótki slug bez spacji,
- `vX.Y.Z` — wersja semantyczna artefaktu,
- `ext` — rozszerzenie pliku.

## 3. Zasady

- brak spacji i polskich znaków w slugu,
- separator pól: podwójny podkreślnik `__`,
- separator słów w slugu: pojedynczy myślnik `-`,
- wersja artefaktu rośnie niezależnie od wersji systemu,
- finalny plik produkcyjny nie może mieć sufiksu `draft` bez wersji.

## 4. Relacja do changelogu

Wersja artefaktu należy do **project delta**, nie do systemowego changelogu
(project delta, nie systemowy changelog; zasada rozdziału w `REVIEW_CHANGELOG_SYSTEM.md`).

---

<!-- SOURCE id=VES-REVIEW-CHANGELOG-001 path=sources/05_DOCUMENT_SYSTEM/REVIEW_CHANGELOG_SYSTEM.md status=ACTIVE version=1.0.0 -->
# REVIEW & CHANGELOG SYSTEM v1

## Review

Każdy review zapisuje:

- wersję,
- kryteria,
- wynik,
- hard fails,
- trzy największe problemy,
- jedną instrukcję następnej rundy,
- decyzję PASS / REVISE / REJECT.

## Changelog

Każda zmiana systemowa zapisuje:

- co,
- dlaczego,
- wpływ,
- pliki zależne,
- rollback,
- status.

---

## SOURCE MAP

- `VES-BRIEF-001` — `sources/05_DOCUMENT_SYSTEM/BRIEF_SYSTEM.md` (status: ACTIVE)
- `VES-PRESENTATION-001` — `sources/05_DOCUMENT_SYSTEM/PRESENTATION_SYSTEM.md` (status: ACTIVE)
- `VES-BATON-001` — `sources/05_DOCUMENT_SYSTEM/AI_BATON_SYSTEM.md` (status: ACTIVE)
- `VES-ARTIFACT-NAMING-001` — `sources/05_DOCUMENT_SYSTEM/ARTIFACT_NAMING.md` (status: ACTIVE)
- `VES-REVIEW-CHANGELOG-001` — `sources/05_DOCUMENT_SYSTEM/REVIEW_CHANGELOG_SYSTEM.md` (status: ACTIVE)
