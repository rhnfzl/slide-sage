# Slide Sage Install Layout and Render Matrix Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the bare remote install copy the complete Slide Sage payload and permanently render three representative slides at both required viewports in CI.

**Architecture:** The current Skills CLI installs a cloned root-level skill as a single file. Move the installable runtime under `skills/slide-sage/`, leaving repository and Pages metadata at the root. Tests use `file://` cloning to exercise the same installer branch without depending on a remote branch. CI renders one chart, one diagram, and one code-oriented slide at reference and short heights.

**Tech Stack:** GitHub Actions, Python assertion scripts, Bash, Node `npx skills`, Playwright.

## Global Constraints

- Work only on `feat/slide-sage-install-layout`, never directly on `main`.
- Preserve the bare install command: `npx skills add rhnfzl/slide-sage`.
- The installed directory must contain `SKILL.md`, `AGENTS.md`, `assets/`, `references/`, `templates/`, `scripts/`, `evals/`, `examples/`, and `THIRD_PARTY_NOTICES.md`.
- Keep the root Pages gallery at `index.html` and retain its three live example links.
- No em dashes in source, documentation, commits, or PR text.
- Do not add dependencies or duplicate the runtime payload.

---

### Task 1: Package the installable runtime below `skills/slide-sage`

**Files:**
- Move: `SKILL.md`, `assets/`, `evals/`, `examples/`, `references/`, `scripts/`, `templates/`, `THIRD_PARTY_NOTICES.md` into `skills/slide-sage/`
- Create: `skills/slide-sage/AGENTS.md`
- Modify: `tests/test_phase3_contract.py`, `tests/test_phase4_contract.py`, `tests/test_phase5_contract.py`, `tests/test_eval_release_contract.py`, `README.md`, `index.html`, `.gitignore`, `CHANGELOG.md`, `.github/workflows/release.yml`, `docs/UPGRADE_PLAN.md`, `docs/UPGRADE_TODO.md`

**Interfaces:**
- `SKILL_ROOT = ROOT / "skills" / "slide-sage"` is the sole test root for runtime assets.
- `npx skills add "file://${ROOT}" --agent codex --yes --copy` must install the complete nested payload under `.agents/skills/slide-sage`.
- Root `index.html` must link to `skills/slide-sage/examples/<deck>.html`.

- [x] **Step 1: Write failing tests for the nested layout and cloned install.**

```python
SKILL_ROOT = ROOT / "skills" / "slide-sage"

def test_05_cloned_source_install_copies_complete_payload() -> None:
    required = ("SKILL.md", "AGENTS.md", "assets", "references", "templates", "scripts", "evals", "examples", "THIRD_PARTY_NOTICES.md")
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
```

- [x] **Step 2: Run the changed contract test and verify it fails because `skills/slide-sage/SKILL.md` does not exist and the cloned install lacks the required payload.**

Run: `python3 tests/test_eval_release_contract.py`

- [x] **Step 3: Move the runtime files, copy the portable AGENTS guide into the runtime, and change repository-facing links and release checks to the nested root.**

```bash
git mv SKILL.md assets evals examples references scripts templates THIRD_PARTY_NOTICES.md skills/slide-sage/
```

Use the nested paths in the README, changelog, Pages links, release version check, test roots, and checklist. Document the user-authorized layout decision in the plan and TODO.

- [x] **Step 4: Run the full contract and local install suite.**

Run:

```bash
python3 tests/test_phase3_contract.py
python3 tests/test_phase4_contract.py
python3 tests/test_phase5_contract.py
python3 tests/test_eval_release_contract.py
python3 skills/slide-sage/scripts/run-evals
npx --yes skills add ./ --list --agent codex --yes
```

- [x] **Step 5: Commit the packaging fix.**

```bash
git add .
git commit -m "fix: install the complete Slide Sage payload"
```

### Task 2: Make CI render three slides at both viewports

**Files:**
- Modify: `.github/workflows/evals.yml`, `tests/test_eval_release_contract.py`, `docs/UPGRADE_TODO.md`

**Interfaces:**
- CI runs six `skills/slide-sage/scripts/render-check` commands: one chart slide, one diagram slide, and one code-oriented slide at `1123,794` and `1123,500`.
- Each command writes a uniquely named `artifacts/*.png` file, and the upload glob includes all six files.

- [x] **Step 1: Extend the failing workflow contract test.**

```python
for command in (
    "skills/slide-sage/scripts/render-check --slide 3 --viewport-size 1123,794 skills/slide-sage/examples/metrics-review.html",
    "skills/slide-sage/scripts/render-check --slide 2 --viewport-size 1123,794 skills/slide-sage/examples/architecture-teaching.html",
    "skills/slide-sage/scripts/render-check --slide 5 --viewport-size 1123,794 skills/slide-sage/examples/slide-sage-intro.html",
):
    assert command in workflow
```

Assert each matching short-height command and all six artifact names too.

- [x] **Step 2: Run the release contract test and verify the new CI expectations fail.**

Run: `python3 tests/test_eval_release_contract.py`

- [x] **Step 3: Replace the single render pair in `evals.yml` with the six required commands and update the upload glob.**

- [x] **Step 4: Run the release contract test and render all six images locally.**

Run:

```bash
python3 tests/test_eval_release_contract.py
skills/slide-sage/scripts/render-check --slide 3 --viewport-size 1123,794 skills/slide-sage/examples/metrics-review.html /tmp/metrics-reference.png
skills/slide-sage/scripts/render-check --slide 3 --viewport-size 1123,500 skills/slide-sage/examples/metrics-review.html /tmp/metrics-short.png
skills/slide-sage/scripts/render-check --slide 2 --viewport-size 1123,794 skills/slide-sage/examples/architecture-teaching.html /tmp/architecture-reference.png
skills/slide-sage/scripts/render-check --slide 2 --viewport-size 1123,500 skills/slide-sage/examples/architecture-teaching.html /tmp/architecture-short.png
skills/slide-sage/scripts/render-check --slide 5 --viewport-size 1123,794 skills/slide-sage/examples/slide-sage-intro.html /tmp/intro-reference.png
skills/slide-sage/scripts/render-check --slide 5 --viewport-size 1123,500 skills/slide-sage/examples/slide-sage-intro.html /tmp/intro-short.png
```

- [x] **Step 5: Commit the CI coverage fix.**

```bash
git add .github/workflows/evals.yml tests/test_eval_release_contract.py docs/UPGRADE_TODO.md
git commit -m "test: render representative Slide Sage decks in CI"
```

## Final verification

- [ ] Run every contract script and `git diff --check`.
- [ ] Confirm a `file://` cloned-source install contains every required runtime entry.
- [ ] Confirm the GitHub Actions workflow contains six render commands and artifact names.
- [ ] Request a whole-branch review, then open a PR without deleting the feature branch.
