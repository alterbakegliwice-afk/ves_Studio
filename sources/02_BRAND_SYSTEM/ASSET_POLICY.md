---
id: VES-ASSET-POLICY-001
version: 1.0.0
status: ACTIVE
owner: Ves
approved_by: Piotrek
updated: "2026-07-11"
source_type: normative
scope: brand-system
canonical: true
dependencies:
  - sources/02_BRAND_SYSTEM/BRAND_SYSTEM_INDEX.md
---

# ASSET POLICY v1

## 1. Klasy assetów

- logo i znaki,
- fonty,
- fotografie własne,
- fotografie licencjonowane,
- ilustracje,
- ikony,
- mockupy,
- materiały AI,
- materiały archiwalne.

## 2. Minimalne metadane

Każdy asset produkcyjny powinien mieć:

- nazwę,
- właściciela,
- źródło,
- status licencji,
- datę,
- wersję,
- dozwolone zastosowania,
- ograniczenia.

## 3. AI

Asset AI musi mieć zapisane:

- model,
- datę,
- prompt lub brief,
- obrazy referencyjne,
- zakres ręcznej obróbki,
- informację, czy przedstawia dane lub produkt wymagający wierności.

## 4. Fonty

- nie udostępniaj plików fontów przez repo,
- zapisuj nazwę, licencję i źródło zakupu/pobrania,
- finalny plik musi używać legalnej licencji dla danego medium.

### 4.1. Polityka licencji i fallback

- font o statusie `license_status: UNKNOWN` nie może być `ACTIVE` w
  `ASSET_REGISTRY.json`; pozostaje `PROVISIONAL` lub `BLOCKED`,
- font `PROVISIONAL`/`BLOCKED` wolno stosować wyłącznie do makiet i eksploracji,
  nigdy do finalnego druku ani publikacji,
- do czasu potwierdzenia licencji materiały produkcyjne używają **fallbacku**
  z jawnie otwartą licencją (np. krój OFL/Apache),
- awans do `ACTIVE` wymaga potwierdzonej licencji zgodnej z deklarowanym użyciem.

Bieżące fallbacki są zapisane w `registries/ASSET_REGISTRY.json` (pole
`fallback`). Walidator rejestrów blokuje `ACTIVE + UNKNOWN license`.

## 5. Logo

- kanoniczne logo istnieje jako plik wektorowy,
- bitmapa AI nie jest masterem znaku,
- warianty mają kontrolowane pole ochronne i minimalny rozmiar.
