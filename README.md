# VES Studio — Source Repository

Kanoniczne, prywatne repozytorium źródeł systemu **VES Studio 2.0**.

To repozytorium **nie jest aplikacją ani dashboardem**. Przechowuje zasady,
źródła, komponenty, decyzje, checklisty review, schematy, rejestry, walidatory,
testy regresji i changelog. Projekt ChatGPT otrzymuje wyłącznie skompilowany
**Runtime Pack** (`runtime/`), nie całe repo.

## Zasady nadrzędne

- **SOURCE FIRST** — trwała reguła istnieje w źródłach, nie w promptcie.
- **ONE OWNER PER RULE** — jedna reguła, jedno kanoniczne źródło.
- **REPO ≠ RUNTIME** — repo jest źródłem edycyjnym; runtime jest kompilacją.
- **LEAN** — bez katalogów i plików bez realnej funkcji.
- **NO SILENT DESIGN DECISIONS** — zmiana marki wymaga Decision Record i zgody.

## Struktura

```
sources/      kanoniczne źródła (znormalizowany frontmatter)
runtime/      skompilowany Runtime Pack (max 8 plików) — GENEROWANE
schemas/      schematy JSON (source, project manifest, decision, source registry)
registries/   SOURCE_REGISTRY, ASSET_REGISTRY, MODEL_CAPABILITY_POINTER
scripts/      walidatory + builder runtime
tests/        testy pytest
.github/       CI, szablony issue i PR
```

## Szybki start

```bash
pip install -r requirements-dev.txt
python scripts/validate_sources.py
python scripts/validate_dependencies.py
python scripts/build_runtime_pack.py
python scripts/validate_runtime.py
pytest
```

## Runtime Pack

`runtime/` jest **generowane** ze źródeł przez `scripts/build_runtime_pack.py`.
Nie edytuj plików w `runtime/` ręcznie. Każdy runtime file ma sekcję
`## SOURCE MAP` wskazującą kanoniczne źródło każdej reguły.

## Modele i routing

VES Studio opisuje **cechy zadania i role** (np. `VES CREATIVE DIRECTOR`).
Konkretne, zmienne nazwy modeli nie są trwałą częścią repo — wskazuje je
**AI Command Center** (`registries/MODEL_CAPABILITY_POINTER.json`).

## Bezpieczeństwo

Repo jest prywatne. Nie commituj sekretów, tokenów, danych zdrowotnych/osobowych
ani plików fontów/assetów bez potwierdzonej licencji
(`sources/01_MASTER_CONTEXT/DATA_AND_PRIVACY_POLICY.md`, `ASSET_POLICY.md`).
