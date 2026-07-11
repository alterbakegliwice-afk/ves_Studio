---
id: VES-TOKENS-001
version: 0.1.0
status: DRAFT
owner: Ves
approved_by: Piotrek
updated: "2026-07-11"
source_type: normative
scope: brand-system
canonical: true
dependencies:
  - sources/02_BRAND_SYSTEM/BRAND_SYSTEM_INDEX.md
---

# TOKENS v0.1

**Status:** DRAFT — struktura gotowa, wartości produkcyjne wymagają zatwierdzenia.

## Model tokenów

```yaml
brand:
  color:
    background:
    surface:
    text:
    text-muted:
    accent-primary:
    accent-secondary:
    signal-success:
    signal-warning:
    signal-danger:
  typography:
    display:
    heading:
    body:
    label:
    numeric:
  spacing:
    1:
    2:
    3:
    4:
    6:
    8:
    12:
  radius:
    none:
    small:
    medium:
  grid:
    columns:
    margin:
    gutter:
  motion:
    fast:
    standard:
    slow:
```

## Zasady

- token ma nazwę funkcjonalną, nie nazwę koloru,
- wartość powinna mieć jednego właściciela,
- pliki projektowe odwołują się do tokenów,
- nie kopiuj HEX do wielu dokumentów,
- każda marka ma własny namespace.
