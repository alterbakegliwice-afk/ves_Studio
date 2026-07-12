---
id: DEC-ALTERBAKE-TYPOGRAPHY-001
version: 1.0.0
status: ACTIVE
owner: Ves
authored_by: Ves
review_status: APPROVED
reviewed_by: Ves
approved_by: Piotrek
approval_date: "2026-07-11"
approval_scope: decision
updated: "2026-07-11"
source_type: decision
scope: brand-alterbake
canonical: true
decision_status: ACCEPTED
external_sync_status: PENDING
dependencies: []
---

# DEC-ALTERBAKE-TYPOGRAPHY-001

- **ID:** DEC-ALTERBAKE-TYPOGRAPHY-001
- **Projekt:** AlterBake — Brand System
- **Data:** 2026-07-11
- **Status:** ACCEPTED_PENDING_SOURCE_SYNC
- **Decydent:** Piotrek
- **Autor rekomendacji:** Ves

## PROBLEM

Źródła AlterBake w Google Drive (STATUS_ALTERBAKE) wskazują nierozstrzygnięty
konflikt typografii: Signage Grotesk vs Google Sans.

## ROZWAŻONE WARIANTY

### A — Signage Grotesk jako jedyny krój
Silna ekspresja, ale słaba czytelność w UI, cennikach i długich treściach.

### B — podział ról krojów
Signage Grotesk do ekspresji miejsca, Google Sans do warstwy systemowej.

## DECYZJA

Przyjęto wariant B:

- **Signage Grotesk:** szyld, ekspresja marki, display, elementy o wysokiej
  rozpoznawalności.
- **Google Sans:** UI, menu, cenniki, etykiety systemowe, dłuższe treści,
  zastosowania pomocnicze i operacyjne.

## UZASADNIENIE

Rozdzielenie ról usuwa konflikt bez utraty charakteru marki i zapewnia
czytelność w zastosowaniach systemowych.

## KOSZT I RYZYKO

Do czasu synchronizacji dokumentu Drive źródło zewnętrzne nadal pokazuje
konflikt. Ryzyko rozbieżności między repo a Drive.

## WPŁYW NA ŹRÓDŁA

- `sources/02_BRAND_SYSTEM/ALTERBAKE_BRAND.md` — sekcja Typografia (kanoniczna),
- Source Registry (repo) oraz Runtime Registry (`07_RUNTIME_REGISTRY.json`, `external_sources`) — wpis konfliktu STATUS_ALTERBAKE.

## WARUNEK PONOWNEGO OTWARCIA

Nowa decyzja Piotrka lub zmiana strategii marki.

## ROLLBACK

Przywrócić oznaczenie konfliktu i wstrzymać finalizację materiałów zależnych od
typografii.

## ZASTĘPUJE / ZASTĄPIONA PRZEZ

Pierwsza decyzja w tym obszarze. Nie zastępuje wcześniejszego Decision Record.
