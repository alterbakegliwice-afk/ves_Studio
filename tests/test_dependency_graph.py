"""Dependency graph tests."""
import validate_dependencies
import vlib


def test_validate_dependencies_passes():
    assert validate_dependencies.main() == 0


def test_brief_project_cycle_broken():
    sources = {s.rel: s for s in vlib.load_sources()}
    brief = sources["sources/05_DOCUMENT_SYSTEM/BRIEF_SYSTEM.md"]
    project = sources["sources/08_PROJECT_TEMPLATE/PROJECT_TEMPLATE.md"]
    # BRIEF must not depend on PROJECT_TEMPLATE
    assert all("PROJECT_TEMPLATE" not in d for d in brief.meta["dependencies"])
    # PROJECT_TEMPLATE depends on BRIEF
    assert any("BRIEF_SYSTEM" in d for d in project.meta["dependencies"])


def test_all_dependencies_resolve_to_files():
    import os
    for s in vlib.load_sources():
        for dep in s.meta.get("dependencies") or []:
            assert dep.startswith("sources/") and dep.endswith(".md")
            assert os.path.isfile(os.path.join(vlib.REPO_ROOT, dep)), dep


def test_no_active_depends_on_placeholder():
    sources = {s.rel: s for s in vlib.load_sources()}
    for s in sources.values():
        if s.status != "ACTIVE":
            continue
        for dep in s.meta.get("dependencies") or []:
            target = sources.get(dep)
            if target is not None:
                assert target.status != "ARCHITECTURE_ONLY", \
                    f"{s.rel} (ACTIVE) depends on placeholder {dep}"


def test_partial_systems_marked():
    sources = {s.rel: s for s in vlib.load_sources()}
    for rel in ("sources/05_DOCUMENT_SYSTEM/PDF_SYSTEM.md",
                "sources/05_DOCUMENT_SYSTEM/REPORT_SYSTEM.md",
                "sources/09_REVIEW_SYSTEM/DASHBOARD_REVIEW.md",
                "sources/09_REVIEW_SYSTEM/PROMPT_REVIEW.md"):
        assert sources[rel].status == "PARTIAL", rel
