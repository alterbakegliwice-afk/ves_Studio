---
id: VES-ROUTING-001
version: 1.1.0
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
dependencies:
  - sources/01_MASTER_CONTEXT/MASTER_CONTEXT.md
---

# VES STUDIO 2.0 — ROUTING

**Wersja:** 1.1
**Status:** obowiązujący

## 1. Cel

Wybrać najmniejszy zestaw źródeł, ról i narzędzi potrzebny do wykonania zadania.

Router nie tworzy treści projektu. Kieruje wykonaniem.

Router opisuje **cechy zadania i role**. Nie zapisuje na stałe nazw ani wersji
modeli. Bieżący, najlepszy model dla danej roli wskazuje AI Command Center
(w Runtime Packu: `07_RUNTIME_REGISTRY.json`, sekcja `model_routing_pointer`).

## 2. Algorytm

### Krok 1 — rozpoznaj rezultat

Czy końcowym wynikiem ma być: odpowiedź, decyzja, research, grafika, zdjęcie,
PDF, prezentacja, UI, dashboard, system marki, źródło/komponent czy AI Baton?

### Krok 2 — wybierz tryb główny

| Sygnał | Tryb |
|---|---|
| prosta ocena lub korekta | QUICK |
| wybór kierunku, koszt błędu | DECISION |
| dane aktualne lub niszowe | RESEARCH |
| praca wizualna | STUDIO |
| rzeczywisty plik | ARTIFACT |
| kontrola istniejącego wyniku | REVIEW |
| zmiana zasad lub repo | SYSTEM |

### Krok 3 — określ domenę

AlterBake · Dietanka · Personal OS · Visual Language · Document System ·
UI / Dashboard · Photo · Prompt / Automation.

### Krok 4 — załaduj źródła

Zawsze: `MASTER_CONTEXT.md`, `SOURCE_OF_TRUTH.md`.

Warunkowo: właściwy plik marki, `VISUAL_LANGUAGE.md`, odpowiedni Document
System, odpowiednie komponenty, status projektu, jedna checklista review.

Limit domyślny: **maksymalnie 7 plików źródłowych na jedno zadanie**.

> Runtime Pack (8 plików) to prekompilowany kontekst bazowy, ładowany zawsze.
> Limit 7 dotyczy **dodatkowych** źródeł projektowych ładowanych do konkretnego
> zadania ponad Runtime Pack, nie liczby plików samego Runtime Packa.

### Krok 5 — wybierz rolę wykonawczą

VES Studio przypisuje zadanie do **roli**, a nie do nazwy modelu. AI Command
Center mapuje rolę na aktualny model.

| Zadanie | Prowadzi (rola) | Wspiera (rola/narzędzie) |
|---|---|---|
| art direction, branding, review | VES CREATIVE DIRECTOR / Ves | generator obrazu, Figma, Canva |
| ilustracja, koncept, lokalne edycje | GENERATYWNY MODEL OBRAZU (koncept) | Photoshop |
| serie, wiele referencji, tekst w obrazie | GENERATYWNY MODEL OBRAZU (seria) | Figma / Canva / Photoshop |
| finalny layout, wektor, UI | NARZĘDZIE WEKTOROWE / UI (Figma) | VES CREATIVE DIRECTOR |
| skalowanie social i szablony | NARZĘDZIE SZABLONÓW (Canva) | VES CREATIVE DIRECTOR |
| retusz i maski | NARZĘDZIE RETUSZU (Photoshop) | VES CREATIVE DIRECTOR |
| automatyzacja, repo, walidatory | INŻYNIER AUTOMATYZACJI (Claude Code) | VES CREATIVE DIRECTOR |
| Docs, Sheets, Drive | OPERATOR WORKSPACE | VES CREATIVE DIRECTOR |
| produkcja piekarska | ŹRÓDŁO OPERACYJNE (Claude) | Ves jako forma / handoff |

Cechy zadania, które opisuje VES Studio (0–5): fotorealizm, dokładność tekstu,
zgodność z referencjami, spójność serii, wiedza o świecie, precyzyjna edycja,
art direction, edytowalność wektorowa, skala wariantów, presja czasu. Na tej
podstawie AI Command Center wybiera bieżący model.

## 3. Routing artefaktów

### Branding
Ładuj: Master Context, plik marki, Visual Language, References, Brand Review,
Project Status. Finalizacja: Figma lub plik wektorowy.

### PDF / raport
Ładuj: Master Context, plik marki, Visual Language, PDF System lub Report
System, komponenty PDF, PDF Review, Project Status.

### UI / dashboard
Ładuj: Master Context, plik marki, Tokens, Layout System, Component Library,
UI lub Dashboard Review, Project Status. Finalizacja: Figma lub kod.

### Foto produktowe
Ładuj: Master Context, plik marki, Photo System, Asset Policy, Photo Review,
Project Status. Finalizacja: generator obrazu + Photoshop.

### Prezentacja
Ładuj: Master Context, plik marki, Visual Language, Presentation System,
Presentation Review, Project Status.

## 4. Konflikt routingu

1. wybierz rolę, która kontroluje finalny typ pliku,
2. generatywny model traktuj jako dostawcę assetów,
3. jeżeli różnica jakości jest nieznana — wykonaj A/B,
4. nie powielaj całego procesu w dwóch narzędziach bez kryterium porównania.

## 5. Routing do źródła operacyjnego (Claude)

Powiedz „to robi Claude”, gdy decyzja dotyczy: receptury, procesu
technologicznego, bezpieczeństwa żywności, foodcostu, harmonogramu produkcji
lub parametrów fermentacji. VES może przygotować formularz, diagram, panel,
dokument lub AI Baton, ale nie zastępuje decyzji operacyjnej.

## 6. Warunek uproszczenia

Jeżeli rezultat można osiągnąć jednym plikiem zamiast systemem, jednym
komponentem zamiast biblioteki, edycją źródła zamiast nowym dokumentem, jedną
rolą zamiast orkiestracji — wybierz prostszy wariant.
