"""Contract checks for executable evals and release automation."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "slide-sage"


def read(relative_path: str) -> str:
    path = SKILL_ROOT / relative_path
    assert path.is_file(), relative_path
    return path.read_text(encoding="utf-8")


def read_repository(relative_path: str) -> str:
    path = ROOT / relative_path
    assert path.is_file(), relative_path
    return path.read_text(encoding="utf-8")


def test_00_runtime_payload_uses_the_nested_skill_root() -> None:
    assert (SKILL_ROOT / "SKILL.md").is_file(), "skills/slide-sage/SKILL.md"


def test_01_eval_bundle_uses_the_reference_schema_and_real_enhancement_fixture() -> None:
    data = json.loads(read("evals/evals.json"))
    assert isinstance(data, dict)
    assert data["skill_name"] == "slide-sage"
    evals = data["evals"]
    assert [case["id"] for case in evals] == list(range(len(evals)))
    assert "mermaid" not in json.dumps(data).lower()

    for case in evals:
        assert case["name"]
        assert case["prompt"]
        assert case["expected_output"]
        assert case["assertions"]
        for assertion in case["assertions"]:
            assert isinstance(assertion, dict)
            assert assertion["description"]
            assert assertion["required_strings"]
            assert all(required.strip() for required in assertion["required_strings"])
        assert isinstance(case["files"], list)
        assert "output_fixture" in case
        output_fixture = case["output_fixture"]
        assert output_fixture.startswith("evals/fixtures/outputs/")
        assert read(output_fixture).lstrip().lower().startswith("<!doctype html>")
        assert "checks" in case
        checks = case["checks"]
        assert checks["slide_count"]
        assert "required_strings" not in checks

    enhancement = next(case for case in evals if case["name"] == "incremental-enhancement")
    fixture = "evals/fixtures/incremental-enhancement.html"
    assert enhancement["files"] == [fixture]
    fixture_source = read(fixture)
    assert fixture_source.count('<section class="slide ') == 2
    assert 'data-theme="ocean-deep"' in fixture_source
    for token in ("SlidePresentation", 'id="navPrev"', 'id="navNext"', 'id="progressFill"', 'id="slideCounter"'):
        assert token in fixture_source

    output_source = read(enhancement["output_fixture"])
    for token in (
        "height: 100vh",
        "overflow: hidden",
        ".slide.inactive { display: none; }",
        "classList.toggle('inactive'",
        "slide.setAttribute('aria-hidden'",
        "slide.removeAttribute('inert')",
        "slide.setAttribute('inert', '')",
    ):
        assert token in output_source


def test_02_local_eval_runner_checks_the_bundle_and_bad_input() -> None:
    runner = SKILL_ROOT / "scripts" / "run-evals"
    assert runner.is_file()
    assert runner.stat().st_mode & 0o111

    result = subprocess.run(
        [str(runner)], cwd=SKILL_ROOT, check=False, capture_output=True, text=True
    )
    assert result.returncode == 0, result.stderr + result.stdout
    assert "PASS 0 ml-startup-pitch" in result.stdout
    assert "5 fixture acceptance checks passed" in result.stdout

    fixture = SKILL_ROOT / "evals" / "fixtures" / "outputs" / "quick-status-update.html"
    result = subprocess.run(
        [str(runner), "--id", "quick-status-update", "--output", str(fixture)],
        cwd=SKILL_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr + result.stdout
    assert "PASS 3 quick-status-update" in result.stdout
    assert "PASS 3 quick-status-update assertion 2" in result.stdout
    assert "1 fixture acceptance checks passed" in result.stdout

    with TemporaryDirectory() as directory:
        invalid = Path(directory) / "evals.json"
        invalid.write_text('{"skill_name":"slide-sage","evals":[]}', encoding="utf-8")
        result = subprocess.run(
            [str(runner), "--path", str(invalid)],
            cwd=SKILL_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
    assert result.returncode == 1
    assert "at least one eval" in result.stderr

    with TemporaryDirectory() as directory:
        deck = Path(directory) / "too-short.html"
        deck.write_text('<!doctype html><section class="slide">Only one slide</section>', encoding="utf-8")
        result = subprocess.run(
            [str(runner), "--id", "quick-status-update", "--output", str(deck)],
            cwd=SKILL_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
    assert result.returncode == 1
    assert "expected exactly 5 slides" in result.stderr

    with TemporaryDirectory() as directory:
        deck = Path(directory) / "missing-assertion-evidence.html"
        deck.write_text(
            fixture.read_text(encoding="utf-8").replace("Inferred style: Ember preset", ""),
            encoding="utf-8",
        )
        result = subprocess.run(
            [str(runner), "--id", "quick-status-update", "--output", str(deck)],
            cwd=SKILL_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
    assert result.returncode == 1
    assert "assertion 2" in result.stderr
    assert "Inferred style: Ember preset" in result.stderr


def test_03_ci_runs_the_eval_runner_and_a_real_example_render_check() -> None:
    workflow = read_repository(".github/workflows/evals.yml")
    assert "pull_request:" in workflow
    assert "python3 skills/slide-sage/scripts/run-evals" in workflow
    assert "skills/slide-sage/scripts/validate skills/slide-sage/examples/metrics-review.html" in workflow
    assert "skills/slide-sage/scripts/render-check --slide 3 --viewport-size 1123,794 skills/slide-sage/examples/metrics-review.html" in workflow
    assert "skills/slide-sage/scripts/render-check --slide 3 --viewport-size 1123,500 skills/slide-sage/examples/metrics-review.html" in workflow
    assert "metrics-chart-reference.png" in workflow
    assert "metrics-chart-short.png" in workflow
    assert "actions/upload-artifact@v4" in workflow

    render_check = SKILL_ROOT / "scripts" / "render-check"
    assert render_check.is_file()
    assert render_check.stat().st_mode & 0o111
    source = render_check.read_text(encoding="utf-8")
    for token in ("screenshot", "data-slide-sage-print-ready", "--viewport-size", "--slide", "keyboard.press"):
        assert token in source


def test_04_release_workflow_guards_versions_and_changelog_documents_upgrade() -> None:
    changelog = read_repository("CHANGELOG.md")
    assert "## 2.0.0 - 2026-07-11" in changelog
    assert "npx skills add rhnfzl/slide-sage" in changelog
    assert "git clone" in changelog

    workflow = read_repository(".github/workflows/release.yml")
    for token in (
        "tags:",
        "v[0-9]+.[0-9]+.[0-9]+",
        ".claude-plugin/plugin.json",
        "skills/slide-sage/SKILL.md",
        "CHANGELOG.md",
        "gh release create",
    ):
        assert token in workflow


def test_05_cloned_source_install_copies_complete_payload() -> None:
    required = (
        "SKILL.md",
        "AGENTS.md",
        "assets",
        "references",
        "templates",
        "scripts",
        "evals",
        "examples",
        "THIRD_PARTY_NOTICES.md",
    )
    with TemporaryDirectory() as directory:
        result = subprocess.run(
            ["npx", "--yes", "skills", "add", f"file://{ROOT}", "--agent", "codex", "--yes", "--copy"],
            cwd=directory,
            check=False,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, result.stderr + result.stdout
        installed = Path(directory) / ".agents" / "skills" / "slide-sage"
        assert all((installed / item).exists() for item in required)


if __name__ == "__main__":
    tests = [value for name, value in sorted(globals().items()) if name.startswith("test_")]
    for test in tests:
        test()
    print(f"{len(tests)} eval and release contract checks passed")
