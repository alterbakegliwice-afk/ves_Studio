---
id: VES-TEST-MATRIX-001
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
source_type: evidence
scope: tests
canonical: true
dependencies:
  - sources/01_MASTER_CONTEXT/QUALITY_GATE.md
---

# TEST MATRIX v1

| ID | Test | Źródła | Review | Kryterium |
|---|---|---|---|---|
| G-01 | AlterBake: story urlop + jagodzianki | AlterBake Brand, Visual Language | Brand + PDF/visual | jasny komunikat, poprawna hierarchia |
| G-02 | AlterBake: menu board iPad | AlterBake Brand, Layout, UI | UI + Dashboard | czytelność z dystansu, prosty przepływ |
| G-03 | Dietanka: karta ćwiczeń B/W | Dietanka Brand, PDF System | PDF + Brand | efekt wow bez utraty drukowalności |
| G-04 | Foto produktu AlterBake | AlterBake Brand, Photo System | Photo | prawdziwa materialność, brak AI artifacts |
| G-05 | Nowy prompt wielokrotnego użycia | Prompt Review | Prompt | źródła, expected output, test negatywny |

## Regresja

Po zmianie pliku krytycznego uruchom wszystkie testy, których źródła od niego zależą.
