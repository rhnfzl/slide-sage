"""Fast contract checks for the Phase 4 delivery and accessibility upgrade."""

from __future__ import annotations

from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "slide-sage"


def read(relative_path: str) -> str:
    return (SKILL_ROOT / relative_path).read_text(encoding="utf-8")


def test_prism_is_pinned_to_130_with_sri_in_executable_snippets() -> None:
    sources = {
        "SKILL.md": read("SKILL.md"),
        "references/html-template.md": read("references/html-template.md"),
        "references/code-highlighting.md": read("references/code-highlighting.md"),
    }
    for path, content in sources.items():
        assert "prismjs@1.29.0" not in content, path
        assert "prismjs@1.30.0" in content, path
    assert 'integrity="sha384-' in sources["references/html-template.md"]
    assert 'integrity="sha384-' in sources["references/code-highlighting.md"]
    assert 'crossorigin="anonymous"' in sources["references/code-highlighting.md"]


def test_pdf_export_and_opt_in_offline_delivery_are_real() -> None:
    export_pdf = SKILL_ROOT / "scripts" / "export-pdf"
    inline_vendor = SKILL_ROOT / "scripts" / "inline-vendor.py"
    assert export_pdf.is_file()
    assert export_pdf.stat().st_mode & 0o111
    export_source = export_pdf.read_text(encoding="utf-8")
    assert "playwright" in export_source
    assert '"${playwright_cmd[@]}" pdf' in export_source
    assert "--viewport-size '1123,794'" in export_source
    assert inline_vendor.is_file()
    assert "Chart.js" in inline_vendor.read_text(encoding="utf-8")
    notices = read("THIRD_PARTY_NOTICES.md")
    for notice in ("ECharts", "D3", "Prism", "Google Fonts"):
        assert notice in notices


def test_canonical_template_supports_keyboard_and_chart_accessibility() -> None:
    css = read("assets/viewport-base.css")
    template = read("references/html-template.md")
    viz = read("references/viz-integration.md")
    for token in (":focus-visible", ".visually-hidden", "inert"):
        assert token in css or token in template
    assert "aria-modal=\"true\"" in template
    assert "trapShortcutsFocus" in template
    assert "restoreShortcutsFocus" in template
    assert 'aria-hidden="true" inert' in template
    assert "this.shortcutsOverlay.removeAttribute('inert')" in template
    assert "this.shortcutsOverlay.setAttribute('inert', '')" in template
    assert "role=\"img\"" in viz
    assert "<noscript>" in viz
    assert "visually-hidden" in viz


def test_presenter_notes_have_one_json_contract_and_real_timing() -> None:
    template = read("references/html-template.md")
    presenter = read("references/presenter-mode.md")
    assert 'type="application/json"' in template
    assert 'id="speaker-notes"' in template
    assert "goTo(" in presenter
    assert "setInterval" in presenter
    assert "cloneNode" in presenter
    assert "readable" in presenter.lower()


def test_presenter_previews_stay_inert_and_keep_internal_references_valid() -> None:
    presenter = read("references/presenter-mode.md")
    assert 'role="status" aria-live="polite"' in presenter
    assert "namespaceCloneIds" in presenter
    assert "copyGlobalIdStyles" in presenter
    assert "aria-errormessage" in presenter
    assert "url(#" in presenter
    assert "clone.setAttribute('inert', '')" in presenter
    assert "clone.setAttribute('aria-hidden', 'true')" in presenter
    assert "window.addEventListener('resize', renderPreviews)" in presenter
    assert r"value.split(/\\s+/)" in presenter
    assert r"/url\\(\\s*#" in presenter


def test_examples_inherit_the_accessible_runtime_and_chart_fallbacks() -> None:
    base_css = read("assets/viewport-base.css")
    examples = (
        "examples/slide-sage-intro.html",
        "examples/metrics-review.html",
        "examples/architecture-teaching.html",
    )
    for example in examples:
        content = read(example)
        assert base_css in content, example
        assert 'id="speaker-notes" type="application/json"' in content, example
        assert "<!-- NOTES:" not in content, example
        assert 'aria-modal="true"' in content, example
        assert 'id="shortcutsClose"' in content, example
        assert 'id="shortcutsOverlay"' in content and 'aria-hidden="true" inert' in content, example
        assert "shortcutsOverlay.removeAttribute('inert')" in content, example
        assert "shortcutsOverlay.setAttribute('inert', '')" in content, example
    for example in examples[:2]:
        content = read(example)
        assert "chart-render-fallback" in content, example
        assert "visually-hidden" in content, example
        assert "<noscript>" in content, example
        assert "fallback.hidden = true" in content, example


def test_static_validator_is_documented() -> None:
    validator = SKILL_ROOT / "scripts" / "validate"
    assert validator.is_file()
    assert validator.stat().st_mode & 0o111
    content = validator.read_text(encoding="utf-8")
    for check in ("class", "inline", "theme"):
        assert check in content.lower()
    assert "scripts/validate" in read("scripts/README.md")
    result = subprocess.run(
        [str(validator), "examples/metrics-review.html"],
        cwd=SKILL_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr + result.stdout


def test_static_validator_accepts_documented_prism_markup() -> None:
    validator = SKILL_ROOT / "scripts" / "validate"
    with TemporaryDirectory() as directory:
        deck = Path(directory) / "prism-deck.html"
        deck.write_text(
            "<style>" + read("assets/viewport-base.css") + "</style>"
            '<section class="slide active"><pre class="code-block line-numbers"><code class="language-python">print(1)</code></pre></section>',
            encoding="utf-8",
        )
        result = subprocess.run(
            [str(validator), str(deck)],
            cwd=SKILL_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
    assert result.returncode == 0, result.stderr + result.stdout


def test_offline_converter_rejects_unvendored_css_imports() -> None:
    converter = SKILL_ROOT / "scripts" / "inline-vendor.py"
    with TemporaryDirectory() as directory:
        fixtures = (
            '<!doctype html><style>@import "//example.invalid/theme.css";</style><p>Deck</p>',
            '<!doctype html><img src=https://example.invalid/image.png>',
            '<!doctype html><script src=//example.invalid/library.js></script>',
            '<!doctype html><link rel=stylesheet href=https://example.invalid/theme.css>',
            '<!doctype html><script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/plugins/autoloader/prism-autoloader.min.js"></script>',
        )
        for index, source in enumerate(fixtures):
            deck = Path(directory) / f"remote-asset-{index}.html"
            deck.write_text(source, encoding="utf-8")
            result = subprocess.run(
                [str(converter), str(deck)],
                cwd=SKILL_ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            assert result.returncode == 1
            assert "cannot vendor" in result.stderr


if __name__ == "__main__":
    tests = [value for name, value in sorted(globals().items()) if name.startswith("test_")]
    for test in tests:
        test()
    print(f"{len(tests)} Phase 4 contract checks passed")
