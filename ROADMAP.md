# ROADMAP

## v1.1 — źródła kanoniczne i Runtime Pack (obecne)

Cel: jedno spójne repo źródeł z walidacją i skompilowanym Runtime Packiem.

Zakres:
- znormalizowany frontmatter wszystkich źródeł,
- usunięty cykl PROJECT_TEMPLATE ↔ BRIEF_SYSTEM,
- `VES_VISUAL_STUDIO.md` scalony i oznaczony SUPERSEDED,
- rejestry: SOURCE, ASSET, MODEL_CAPABILITY_POINTER,
- walidatory źródeł, zależności, duplikatów i runtime,
- Runtime Pack (max 8 plików) z sekcją SOURCE MAP,
- CI (GitHub Actions) + testy pytest.

## v2 — komponenty i walidacja rozszerzona

Cel: powtarzalne artefakty i mniej ręcznej kontroli.

Zakres:
- pełna biblioteka komponentów (dziś ARCHITECTURE_ONLY),
- zatwierdzone tokeny produkcyjne,
- pełna Prompt Library,
- prompt tests i benchmark modeli graficznych,
- integracje Figma / Canva / Photoshop.

## v3 — orkiestracja

Cel: półautomatyczne studio wielomodelowe.

Zakres:
- router modeli sterowany AI Command Center,
- automatyczne ładowanie kontekstu,
- system oceny i regresji,
- publish pipeline do Figma / Canva / Drive,
- dashboard VES Studio.

Role (v2–v3): VES CREATIVE DIRECTOR prowadzi art direction i final review;
Źródło operacyjne (Claude) prowadzi backend, CI i automatyzację; Operator
Workspace (Gemini) prowadzi operacje Google Workspace.
