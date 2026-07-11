# CONTRIBUTING — VES Studio Source Repository

## Zasady

1. **Source-first.** Trwała reguła istnieje w `sources/`, nie w promptcie.
2. **One owner per rule.** Nie utrzymuj równoległych kopii tej samej zasady.
3. **Repo ≠ runtime.** Nie edytuj `runtime/` ręcznie — jest generowane.
4. **No silent design decisions.** Zmiana marki, typografii, kolorów, logo lub
   podziału ról wymaga Decision Record i zgody Piotrka.

## Frontmatter źródła

Każdy plik w `sources/` musi mieć frontmatter:

```yaml
---
id: VES-UNIQUE-ID
version: 1.0.0
status: ACTIVE
owner: Ves
approved_by: Piotrek
updated: "2026-07-11"
source_type: normative
scope: visual-system
canonical: true
dependencies:
  - sources/01_MASTER_CONTEXT/QUALITY_GATE.md
---
```

Dozwolone statusy: `DRAFT`, `ACTIVE`, `PARTIAL`, `SUPERSEDED`, `ARCHIVED`,
`BLOCKED`, `ARCHITECTURE_ONLY`.
Dozwolone typy: `normative`, `state`, `decision`, `evidence`, `template`,
`registry`, `generated-runtime`.

## Reguły zależności

- każda zależność to pełna ścieżka `sources/.../PLIK.md`,
- brak cykli,
- plik `ACTIVE` nie może zależeć od `ARCHITECTURE_ONLY` (oznacz `PARTIAL`),
- nie zależ od `SUPERSEDED`,
- placeholder (`ARCHITECTURE_ONLY`) nie może być `canonical: true`.

## Przed commitem

```bash
python scripts/validate_sources.py
python scripts/validate_dependencies.py
python scripts/build_runtime_pack.py
python scripts/validate_runtime.py
pytest
```

CI uruchamia te same kroki przy `push` i `pull_request`. Nie merguj bez zgody
Piotrka.

## Bezpieczeństwo

Nie commituj sekretów, tokenów, danych osobowych/zdrowotnych ani plików fontów.
Assety z licencją rejestruj w `registries/ASSET_REGISTRY.json`, nie w repo.
