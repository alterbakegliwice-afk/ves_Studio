# VES Studio — Source Repository

Kanoniczne, prywatne repozytorium źródeł systemu **VES Studio 2.0**.

**Release:** VES Studio Core Beta v1.1.1 — rdzeń governance, brand AlterBake,
visual system, document/project/review systems i Runtime Pack są gotowe.
To **nie jest** system production-ready: część modułów (Component/Prompt/
Reference Library, Automation) pozostaje `ARCHITECTURE_ONLY` i poza runtime.
Statusy repo/release/runtime są rozdzielone w `ves-studio.manifest.json`.

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

Pełny merge gate (weryfikuje świeżość runtime **przed** buildem, więc nie maskuje
starego commitowanego runtime):

```bash
pip install -r requirements-dev.txt
bash scripts/run_merge_gate.sh
```

Świadoma aktualizacja runtime po zmianie źródeł (osobno):

```bash
python scripts/build_runtime_pack.py
bash scripts/run_merge_gate.sh
```

## Runtime Pack

`runtime/` jest **generowane** ze źródeł przez `scripts/build_runtime_pack.py`
na podstawie danych w `registries/RUNTIME_COMPOSITION.json`. Nie edytuj plików
w `runtime/` ręcznie.

- domyślnie kompilowane są **wyłącznie źródła `ACTIVE`**; DRAFT/PARTIAL są
  wykluczone (wyjątek wymaga jawnego wpisu z ostrzeżeniem),
- każda sekcja ma marker `<!-- SOURCE ... -->` (śledzenie reguły do źródła),
- `00_RUNTIME_INDEX.md` zawiera wersję (z manifestu) i **checksum źródeł**
  (kanoniczna identyfikacja runtime); `Source commit` jest stemplowany tylko w
  artefakcie release/handoff (`$SOURCE_COMMIT`), inaczej `n/a`,
- świeżość sprawdza `python scripts/verify_runtime_freshness.py` — po zmianie
  źródła przebuduj pack i wgraj go ponownie do projektu ChatGPT.

## Modele i routing

VES Studio opisuje **cechy zadania i role** (np. `VES CREATIVE DIRECTOR`).
Konkretne, zmienne nazwy modeli nie są trwałą częścią repo — wskazuje je
**AI Command Center** (`registries/MODEL_CAPABILITY_POINTER.json`).

## Bezpieczeństwo

Repo jest prywatne. Nie commituj sekretów, tokenów, danych zdrowotnych/osobowych
ani plików fontów/assetów bez potwierdzonej licencji
(`sources/01_MASTER_CONTEXT/DATA_AND_PRIVACY_POLICY.md`, `ASSET_POLICY.md`).
