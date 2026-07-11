"""Fast contract checks for the Phase 3 output-quality upgrade."""

from __future__ import annotations

from pathlib import Path
import re
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def test_theme_bridge_and_defaults() -> None:
    css = read("assets/viewport-base.css")
    for declaration in (
        "--color-bg: var(--color-bg-primary)",
        "--color-text: var(--color-text-primary)",
        "--color-heading: var(--color-text-primary)",
        "--color-surface: var(--color-bg-surface)",
    ):
        assert declaration in css
    assert "#0f0f1a" not in css
    assert "rgba(255, 255, 255" not in css
    for consumer in (
        "font-size: var(--preset-title-size)",
        "font-size: var(--preset-section-size)",
        "letter-spacing: var(--preset-kicker-tracking)",
        "height: var(--preset-divider-width)",
        "font-variant-numeric: var(--preset-stat-treatment)",
    ):
        assert consumer in css
    for example in ("examples/architecture-teaching.html", "examples/metrics-review.html", "examples/slide-sage-intro.html"):
        assert css in read(example), example
    for template in (ROOT / "templates" / "comparison").glob("*.html"):
        assert '[data-theme="light"]' not in template.read_text(encoding="utf-8")
    assert '[data-theme="light"]' not in read("references/code-highlighting.md")


def test_eight_tone_first_presets() -> None:
    presets = sorted((ROOT / "references" / "presets").glob("*.md"))
    assert len(presets) == 8
    style_guide = read("references/style-guide.md")
    assert "Tone-first matching" in style_guide
    assert "Inter" not in style_guide
    required_tokens = (
        "--color-bg-primary:",
        "--color-bg-secondary:",
        "--color-bg-surface:",
        "--color-bg-elevated:",
        "--color-text-primary:",
        "--color-text-secondary:",
        "--color-text-muted:",
        "--color-text-inverse:",
        "--color-accent:",
        "--color-accent-secondary:",
        "--color-gold:",
        "--font-heading:",
        "--font-body:",
        "--preset-title-size:",
        "--preset-section-size:",
        "--preset-kicker-tracking:",
        "--preset-divider-width:",
        "--preset-stat-treatment:",
    )
    for preset in presets:
        content = preset.read_text(encoding="utf-8")
        for field in ("Mood:", "Tone:", "Best for:", "Avoid for:", "Formality:", "Density:", "Scheme:"):
            assert field in content
        for token in required_tokens:
            assert token in content, f"{preset.name}: {token}"


def test_skill_requires_truthful_chart_data_and_anti_slop() -> None:
    skill = read("SKILL.md")
    assert "Anti-slop" in skill
    assert "SAMPLE DATA" in skill
    assert "representative/realistic" not in skill
    assert "ask for the numbers" in skill


def test_diagram_templates_use_current_palette_and_parse() -> None:
    templates = sorted((ROOT / "templates" / "diagrams").glob("*.svg"))
    assert len(templates) == 17
    legacy = ("#4A90D9", "#50C878", "#F5A623", "#DC5A5A", "#9B59B6")
    for template in templates:
        content = template.read_text(encoding="utf-8")
        ElementTree.fromstring(content)
        assert all(color not in content for color in legacy), template.name
        assert "--diagram-label" in content, template.name
        identifiers = set(re.findall(r'\bid="([^"]+)"', content))
        references = set(re.findall(r"url\(#([^)]+)\)", content))
        assert len(identifiers) == len(re.findall(r'\bid="([^"]+)"', content)), template.name
        assert references <= identifiers, template.name
    microservices = read("templates/diagrams/microservices.svg")
    assert 'id="shadow"' not in microservices
    for name in ("client-server.svg", "cloud-three-tier.svg", "microservices.svg", "ml-pipeline.svg"):
        assert "var(--diagram-shadow, #000000)" in read(f"templates/diagrams/{name}")


def test_template_exposes_slide_lifecycle_and_chart_replay_guidance() -> None:
    template = read("references/html-template.md")
    viz = read("references/viz-integration.md")
    assert "slidechange" in template
    assert "CustomEvent" in template
    assert "animation: false" in viz
    assert "slidechange" in viz
    for example in ("examples/metrics-review.html", "examples/slide-sage-intro.html"):
        content = read(example)
        assert "chart.reset()" in content
        assert "animation: false" in content


def test_named_examples_and_code_snippets_follow_the_theme_contract() -> None:
    examples = {
        "examples/metrics-review.html": "ember",
        "examples/architecture-teaching.html": "jade-circuit",
        "examples/slide-sage-intro.html": "ocean-deep",
    }
    for path, theme in examples.items():
        content = read(path)
        assert f'html[data-theme="{theme}"]' in content
        assert "fonts.googleapis.com" in content
    code = read("references/code-highlighting.md")
    assert 'html[data-mode="light"]' in code
    assert not re.search(r"^\s*\.light-theme", code, re.MULTILINE)
    assert "rgba(255, 255, 255" not in code


if __name__ == "__main__":
    tests = [value for name, value in sorted(globals().items()) if name.startswith("test_")]
    for test in tests:
        test()
    print(f"{len(tests)} Phase 3 contract checks passed")
