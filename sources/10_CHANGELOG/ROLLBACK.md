---
id: VES-ROLLBACK-001
version: 1.0.0
status: ACTIVE
owner: Ves
approved_by: Piotrek
updated: "2026-07-11"
source_type: normative
scope: changelog
canonical: true
dependencies:
  - sources/10_CHANGELOG/CHANGELOG.md
---

# ROLLBACK POLICY

## Poziomy zmian

### PATCH

Korekta języka, literówki, doprecyzowanie bez zmiany znaczenia.

Rollback: poprzednia wersja pliku.

### MINOR

Nowa reguła, komponent lub checklista zgodna z architekturą.

Rollback: wycofanie pliku i aktualizacja changelogu.

### MAJOR

Zmiana hierarchii źródeł, ról modeli, struktury repo lub zasad marki.

Rollback wymaga:

1. identyfikacji wszystkich plików zależnych,
2. przywrócenia ostatniej wersji stabilnej,
3. oznaczenia Decision Record jako `SUPERSEDED`,
4. aktualizacji statusów projektów,
5. testu regresji.

## Wersja stabilna

Pierwsza wersja stabilna: `v1.0 FOUNDATION`.

## Zakaz

Nie kasuj historii decyzji. Oznaczaj przestarzałe pliki jako `SUPERSEDED` i wskazuj następcę.
