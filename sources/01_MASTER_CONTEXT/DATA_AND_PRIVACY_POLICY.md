---
id: VES-PRIVACY-001
version: 1.0.0
status: ACTIVE
owner: Ves
authored_by: Claude Code
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

# DATA AND PRIVACY POLICY v1

## 1. Cel

Chronić dane osobiste, zdrowotne i biznesowe w całym systemie VES Studio oraz
w repozytorium źródeł.

## 2. Zasady

- Dane zdrowotne i osobiste nie trafiają do publicznego repozytorium.
- Repozytorium źródeł jest prywatne.
- Sekrety, tokeny i klucze wyłącznie w `secrets` / zmiennych środowiskowych,
  nigdy w plikach źródłowych ani w Runtime Pack.
- Assety z licencją nie są automatycznie commitowane (patrz `ASSET_POLICY.md`).
- Dane klientek Dietanki (psychodietetyka) traktuj jako wrażliwe — nie
  umieszczaj realnych przypadków w źródłach ani przykładach.
- Bieżący stan firmy (STATUS_ALTERBAKE) żyje w Google Drive, nie w repo.

## 3. Klasyfikacja

| Klasa | Przykład | Gdzie może być |
|---|---|---|
| Publiczna | zasady systemu, komponenty | repo (prywatne) i Runtime Pack |
| Wewnętrzna | status projektu, brief | repo, nie Runtime Pack |
| Wrażliwa | dane zdrowotne, dane klientek | poza repo |
| Sekret | tokeny, klucze API | secrets / env |

## 4. Kontrola

- walidator runtime sprawdza brak wzorców sekretów,
- review źródeł odrzuca realne dane osobowe,
- każdy asset ma status licencji w `ASSET_REGISTRY.json`.
