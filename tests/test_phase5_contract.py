"""Fast contract checks for the Phase 5 behavior upgrade."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "slide-sage"
INTAKE_RULE = (
    "Infer audience and style from a detailed prompt and state the choice in one line. "
    "Ask only when the prompt is genuinely thin. "
    "Never block in one-shot, subagent, or CI runs: choose sensible defaults and state them in one line. "
    "Offer a visual preview only when style is unspecified and a browser is available."
)


def read(relative_path: str) -> str:
    return (SKILL_ROOT / relative_path).read_text(encoding="utf-8")


def frontmatter_description(content: str) -> str:
    frontmatter = content.split("---", 2)[1]
    return next(line.removeprefix("description: ") for line in frontmatter.splitlines() if line.startswith("description: "))


def test_gap_driven_intake_is_identical_and_never_blocks() -> None:
    for path in ("AGENTS.md", "SKILL.md"):
        content = read(path)
        assert INTAKE_RULE in content, path
        assert "Always-Ask Questions" not in content, path
        assert "mandatory, every presentation" not in content, path
    assert "In a one-shot, non-interactive, subagent, or CI run, continue with clearly-labeled `SAMPLE DATA` only." in read("SKILL.md")


def test_intake_asks_reader_and_density() -> None:
    """Audience does not imply either one, so both are asked rather than guessed.

    Guessing them overcorrects: a deck stripped to diagrams starves the presenter of
    recall material, and a padded one walls off the room.
    """
    for path in ("AGENTS.md", "SKILL.md"):
        content = read(path)
        assert "Reader and density" in content, path
        assert "Will you present this live, send it to be read on its own, or both?" in content, path
        assert "Diagram-led, balanced, or text-rich?" in content, path


def test_presenter_mode_ships_whenever_speaker_notes_exist() -> None:
    """Speaker notes with no way to open them are the bug this guards.

    A `<script id="speaker-notes">` block is invisible unless presenter mode is wired,
    which left the presenter recalling from memory while their own notes sat in the file.
    """
    for path in ("AGENTS.md", "SKILL.md"):
        content = read(path)
        assert "When user requests presenter view" not in content, path
        assert "If user explicitly requests presenter view" not in content, path
        assert "without presenter mode" in content, path


def test_frontmatter_triggers_all_modes_without_a_library_catalog() -> None:
    description = frontmatter_description(read("SKILL.md"))
    for trigger in ("slide deck", "pitch deck", "PowerPoint", "pptx", "convert", "PDF"):
        assert trigger in description, trigger
    assert "existing HTML presentation" in description
    assert "Not for" in description
    for library in ("Chart.js", "ECharts", "D3", "Prism.js"):
        assert library not in description, library


def test_cross_platform_guide_includes_pdf_conversion() -> None:
    agents = read("AGENTS.md")
    assert "convert a PowerPoint or PDF" in agents
    assert "PPT/PDF conversion" in agents


if __name__ == "__main__":
    tests = [value for name, value in sorted(globals().items()) if name.startswith("test_")]
    for test in tests:
        test()
    print(f"{len(tests)} Phase 5 contract checks passed")
