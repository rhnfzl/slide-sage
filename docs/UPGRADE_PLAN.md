# Slide Sage Upgrade Plan

Status: approved baseline, implementation in progress
Date: 2026-07-11
Owner: Rehan

## What this is, in plain language

Slide Sage is an open-source agent skill that turns a prompt into a data-rich, single-file
HTML slide deck. It works, but three things hold it back: it is harder to install and list
than it should be, its README shows a visual product with zero visuals, and the decks it
generates have real quality bugs (presets that barely differ, a theme system that does not
actually recolor slides, charts that print blank, no check that a slide even fits on screen).

This plan brings Slide Sage up to the bar set by the author's other two skills
(`explore-unknowns`, `human-html`): one-command install via `npx skills add rhnfzl/slide-sage`,
a clean skills.sh listing, a readable banner-led README aimed at engineers and tech leads, and
a genuinely better deck coming out the other end.

It is a phased plan so value ships early. Nothing here starts until you confirm.

## The three goals (from the request)

1. **Easy install + proper skills.sh listing.** `npx skills add rhnfzl/slide-sage` works and the
   repo is discoverable and well-presented on skills.sh, with a banner in the README.
2. **README and repo that read well** for the real audience: engineers, tech leads, data/ML folks,
   and technical PMs who present metrics reviews, architecture decks, and teaching material using
   AI coding tools.
3. **A better skill.** Steal-like-an-artist improvements (from `zarazhangrui/frontend-slides` and the
   wider field) to output quality, reliability, and honesty, without losing Slide Sage's identity:
   data-rich, single-file, cross-platform.

## How this plan was built

- **Repo-explorer** cloned and read `zarazhangrui/frontend-slides` (+ `beautiful-html-templates`).
- **8-agent Fable 5 workflow** (854K tokens): reference-bar analysis of the two model repos,
  steal-analysis of frontend-slides, a 4-lens shortcomings audit (skill design, frontend quality,
  distribution, audience fit), skills.sh mechanics from the vercel-labs CLI source, competitor scan,
  and a synthesis critic that produced 22 ranked changes, 8 contradictions, 8 gaps, and 7 design forks.
- **Recursive Tavily research** (2 waves, 73 cited claims): competing skills/tools, HTML-presentation
  UX best practices, skills.sh distribution norms, and the documented pain points of AI decks.
- **Direct source verification** of the single highest-stakes claim (see the correction below).
- **A grill-me session** (three AskUserQuestion rounds) that locked every design fork.

## Superseded correction to the research (historical context)

The synthesis ranked "the root-level `SKILL.md` ships broken via npx because the installer drops all
support directories" as the #1 change and prescribed relocating the skill into `skills/slide-sage/`.

**The following source-reading conclusion was later superseded by cloned-source verification. It is retained only to explain the decision change.**

- The support-dir-dropping filter is on the **blob fast-path only**, and that path runs solely for
  `BLOB_ALLOWED_OWNERS = ['vercel', 'vercel-labs', 'heygen-com']` (`src/add.ts:1152`).
- For `rhnfzl`, the CLI **skips blob and does a full `git clone`** (`src/add.ts:1177`), then
  `discoverSkills` sets the skill path to the repo root and `installSkillForAgent` calls
  `copyDirectory` (`src/installer.ts:462`), which copies the **entire** skill directory recursively,
  excluding only `.git`, `metadata.json`, `__pycache__`, `__pypackages__`.
- The source reading therefore inferred that `references/`, `templates/`, `assets/`, and `scripts/` **do** ship on
  `npx skills add rhnfzl/slide-sage`. Cloned-source verification disproved that inference for the root layout.

**Historical consequence (superseded):** the original plan treated packaging metadata and copied junk as
the only gap and rejected restructuring. Do not use that conclusion for current implementation work.

### 2026-07-11 current layout decision

Cloned-source verification with Skills CLI 1.5.16 later showed the actual install copied only a root
`SKILL.md`, despite the earlier source reading. The user explicitly authorized reopening the root-layout
decision. The runtime now lives at `skills/slide-sage/`, with `SKILL.md`, `AGENTS.md`, and every runtime
dependency in that directory. This is the authoritative packaging decision: keep the root marketplace
source at `./`, and do not retain a root `SKILL.md` because root discovery would recreate the incomplete
installation.

## Locked decisions (grill-me results)

| # | Decision | Choice | Rationale |
|---|----------|--------|-----------|
| A | Appetite | **Full phased overhaul** | Matches "live up to its mark"; phased so value ships early |
| B | Slide canvas | **Keep fluid 100vh default, add opt-in fixed 16:9 mode** | Projector/PDF determinism without discarding the working fluid system |
| C | Offline claim | **CDN default (quality first), opt-in inline-vendored mode, honest README** | User: "offline-first preference, but online OK if it improves quality" |
| D | README top | **Concise, text-first anatomy matching the two reference repos** | Consistency across the author's skills; visual proof lives in a gallery, not the README body |
| E | Packaging | **Nested runtime at `skills/slide-sage/`** (retain root marketplace metadata) | Cloned-source installs copy the discovered skill directory; a root `SKILL.md` would win discovery and omit support files |
| F | Interview | **Gap-driven + hard non-interactive rule** | Current mandatory interview fails the skill's own evals and hangs in CI/subagent runs |
| G | Sister repos | **Audit all three together for consistency** | Local at `../explore-unknowns` and `../human-html`; make them a coherent set |
| H | PDF export | **Playwright export script + force animations to settle; browser-print stays as fallback** | Export fidelity is the #1 documented AI-deck pain point |
| I | Presets | **Full preset rebuild: 8-10 opinionated presets, per-preset type + layout** | Today's presets are the same layout recolored |
| J | No-fake-data | **Interactive: ask for the numbers. Non-interactive: clearly-labeled SAMPLE data, never silent invention, never block** | Hallucinated numbers are the #1 documented failure; reconciles with the non-interactive rule (F) |
| K | Render check | **Screenshot 2-3 slides when a browser is available; static validator as the always-on fallback** | Viewport-fitting is declared non-negotiable but nothing ever looks at the rendered deck |
| L | Banner/gallery | **Build a demo deck about Slide Sage using Slide Sage; banner + gallery come from its slides; host on GitHub Pages** | The product demonstrates itself; strongest proof |

Deferred-to-default (not controversial, no fork): speaker notes move to a JSON `<script>` block (fixes
the two references that currently disagree on placement); the current competitor comparison table is
dropped (the reference repos have none, and the existing rows are misleading); an anti-slop design
doctrine is added to the skill.

## Research evidence that drives the quality work

- **Export fidelity is the #1 pain point** across every AI-deck tool; browser Print-to-PDF (today's only
  path) is exactly what users complain about; decktape/Playwright headless rendering is the reliable norm.
- **Hallucinated data** caused real damage (a VP made territory decisions off invented metrics for 3 months).
- **Generic, same-every-time output** is the second-biggest complaint; explicit anti-slop rules are now
  table stakes.
- **The slides-as-code field uses a fixed design canvas** (reveal.js 960x700, Slidev 980x552 16:9) scaled
  with CSS transform, not fluid 100vh. Hence the opt-in 16:9 mode.
- **skills.sh indexes GitHub automatically** (no registration step), ranks by weekly install count from
  `npx skills add` telemetry + recency; the listing surfaces `name`/`description` and install count, so the
  frontmatter description and the `skills.sh.json` description are the storefront copy.

---

## Phased plan

Each item lists the change, why it matters, the files it touches, and how we know it is done.

### Phase 1 - Packaging, install, and listing (Goal 1)

Nested-runtime packaging. Keeps the one command as the headline, preserves root marketplace metadata, and stops shipping incomplete payloads.

1. **Add the packaging/metadata files the reference repos have.**
   - `.claude-plugin/marketplace.json` (`"source": "./"`, owner `rhnfzl`) and `.claude-plugin/plugin.json`
     (name, description, version, author, license MIT, keywords) mirroring human-html's shape.
   - `skills.sh.json` with a single grouping whose `title`/`description` are human-facing storefront copy.
   - Add `skills/slide-sage/SKILL.md` frontmatter `license: MIT` and `metadata: { version, author }`.
   - *Why:* required for a clean skills.sh listing and the version-consistency guard the release workflow uses.
   - *Done when:* `npx skills add ./ --list` (local) resolves `skills/slide-sage` as one skill with all support dirs,
     the cloned-source install copies the payload, and the three manifests validate.

2. **Rewrite the README install section to a single hero command.**
   - Lead with `npx skills add rhnfzl/slide-sage` (auto-detects Claude Code, Codex, Cursor, Copilot, Gemini,
     Amp, and 30+ agents). Remove the nonexistent `claude skill add` command. Collapse the ~140-line per-tool
     matrix into one `<details>` block.
   - *Why:* the current headline command errors on first copy; the one command that already works is never mentioned.
   - *Done when:* the first install instruction a visitor sees is the working `npx` command.

3. **Repo hygiene and security.**
   - Delete `CLONE.md` and `.github/workflows/clone-count.yml` (the workflow curls and executes an unpinned
     third-party script from a moving branch inside a job holding a PAT with gist scope: a credential-exposure risk).
   - Replace the clone-count badge with a skills.sh install badge + Release + License.
   - Add `.claude/` and `.agent-harness/` to `.gitignore` so the local sqlite and settings never get committed
     or copied into installs. Track `AGENTS.md` (today it is gitignored, so its cross-platform instructions never ship).
   - *Done when:* `git ls-files` shows no `CLONE.md`, no clone-count workflow, no `.agent-harness`, and `AGENTS.md` is tracked.

4. **SECURITY.md + a condensed Trust section in the README.**
   - Document each external touch-point: CDN imports are browser-only and version-pinned; Python scripts run
     only on explicit user invocation; no telemetry beyond the CLI's own anonymous install ping; install copies files.
   - *Why:* skills.sh security scanners (Snyk partnership) flag CDN URLs and executable scripts; an in-repo
     rationale is what human and automated auditors look for.

### Phase 2 - README, banner, and visual proof (Goal 2)

5. **Rewrite the README to the reference-repo anatomy, reader-first.**
   - Banner, three badges, a bold one-liner, the `npx` quickstart, a plain-language "why this exists", a
     "what's in the box" table, and Trust. Target ~120-150 lines. Scrub em dashes. Target the engineer/tech-lead audience.
   - Drop the competitor comparison table; replace with one honest positioning paragraph and a link to the gallery,
     stating plainly when to reach for Anthropic's pptx skill instead.
   - *Done when:* the README opens with a banner and reads top-to-bottom without install clutter.

6. **Build a demo deck about Slide Sage, using Slide Sage.**
   - `skills/slide-sage/examples/slide-sage-intro.html` plus 2-3 more example decks (a metrics review, an architecture teaching deck).
   - Add the nested examples gitignore negation so they are tracked.
   - *Why:* the product demonstrates itself; this is the banner + gallery source and the strongest credibility asset.

7. **Banner + GitHub Pages gallery.**
   - Banner (`skills/slide-sage/assets/banner.webp`) composed from the demo deck's best slides.
   - A Pages `index.html` gallery linking the live example decks (one per showcased preset: chart slide, diagram slide, code slide).
   - *Done when:* the README banner renders and the Pages gallery is live and linked.

### Phase 3 - Output quality: the deck actually gets better

8. **Fix the broken theme-variable seam.** (correctness, not polish)
   - Unify the two variable vocabularies (base `--color-*` vs preset `--color-*-primary`) with a bridge block
     so applying a preset actually recolors slides. Replace hardcoded `rgba(255,255,255,x)` literals with `color-mix`.
     Delete the dead `[data-theme=light]` blocks no preset ever sets.
   - *Files:* `skills/slide-sage/assets/viewport-base.css`, `skills/slide-sage/references/style-guide.md`.
   - *Why:* today presets barely change the output and light presets render white text on white.

9. **Full preset rebuild (8-10 opinionated presets).**
   - Restructure presets as `skills/slide-sage/references/presets/<slug>.md` behind a compact index carrying
     `mood/tone/best_for/avoid_for/formality/density/scheme`. Give each preset 2-3 structural signatures beyond
     color (hairline dividers vs cards, oversized stat numerals, mono kicker labels, per-preset type scale).
   - Drop the Inter default and the catppuccin base theme; add at least one serif-display and one editorial preset;
     keep genuine system-font fallbacks (audience presents in locked-down corporate CSP environments that block web fonts).
   - Switch preset matching from industry-mapping to tone-first.
   - *Why:* two decks in different presets are currently the same deck recolored; Inter is the exact "AI look" font anti-slop guides ban.

10. **Anti-slop design doctrine + no-fake-data rule in `skills/slide-sage/SKILL.md`.**
    - Banned fonts/hexes, committed palettes, one orchestrated reveal per slide.
    - No-fake-data: charts plot user-provided numbers whenever they exist. Interactive run with a chart implied but
      no data provided -> ask for the numbers. Non-interactive/subagent/CI run -> use obviously-labeled SAMPLE data
      (visible badge + speaker note "SAMPLE DATA, replace before sharing"), never invent silently, never block.
    - *Why:* directly targets the top-two documented failures (generic look, hallucinated data).

11. **Re-palette and de-bug the SVG diagram templates.**
    - Recolor all `skills/slide-sage/templates/diagrams/*.svg` to the Tier-1 colorblind-safe categorical palette; prefix every filter
      `id` per-diagram to avoid collisions when two diagrams share one deck; derive cylinder shading from a
      semi-transparent overlay instead of a second hardcoded hex; make label fill a variable.
    - *Why:* out of the box the diagrams use a dated flat palette that clashes with every preset and has real
      id-collision and hardcoded-hex bugs.

12. **Chart animation on slide-enter.**
    - Add a `slidechange`/`onSlideEnter` lifecycle to the `SlidePresentation` class; init charts with
      `animation:false` and replay the animation / start CountUp when the slide becomes active, respecting
      `prefers-reduced-motion`.
    - *Files:* `skills/slide-sage/references/html-template.md`, `skills/slide-sage/references/viz-integration.md`.
    - *Why:* charts currently finish animating on load, before the audience ever reaches the slide.

### Phase 4 - Reliability, accessibility, and honest offline

13. **Prism security bump + SRI.** Bump Prism `1.29.0 -> 1.30.0` across `skills/slide-sage/SKILL.md`, html-template.md, and
    code-highlighting.md (1.29.0 carries CVE-2024-53382, DOM-clobbering to XSS), and add SRI
    `integrity`+`crossorigin` to the canonical CDN snippets. One-line-per-file, ships in every generated deck.

14. **Playwright PDF export + delivery contract.**
    - `skills/slide-sage/scripts/export-pdf` that headless-renders to a reliable PDF; force chart animations to complete before print
      so nothing prints blank. Keep browser Print-to-PDF documented as the zero-dependency fallback and fix its
      print CSS. Always open the file and send the absolute path at the end of a run.
    - *Why:* PDF export is claimed but not engineered; the audience presents minutes after generating.

15. **Opt-in offline (inline-vendored) mode + honest README.**
    - Add an opt-in mode that bakes the pinned libraries into the HTML (Chart.js UMD ~65KB is fine for a single file),
      so offline is genuinely true when requested. Keep CDN as the default (quality-first, per decision C).
    - Correct the README: offline is true today for chart-free decks or via the inline mode; CDN decks need a network
      for charts.
    - Add the license notices vendoring requires: ECharts Apache-2.0 NOTICE, D3 ISC, Prism MIT, Google Fonts OFL.
    - *Why:* the offline/single-file line is currently false with CDN charts; this makes the differentiator real and legal.

16. **Implement the accessibility claims that are currently aspirational.**
    - `focus-visible` outlines, `inert`/`aria-hidden` on inactive slides, `dialog` role + focus trap on the shortcuts overlay.
    - Chart-data accessibility: `role="img"` + `aria-label` on canvases, a visually-hidden data-table fallback, and a
      `noscript`/no-canvas fallback (which doubles as the honest offline degradation path: a table when the chart cannot render).
    - *Why:* `skills/slide-sage/SKILL.md` promises visible focus and WCAG AA that the CSS/JS do not implement; screen-reader access to chart data is entirely uncovered.

17. **Fix presenter mode.**
    - One speaker-notes format (JSON `<script>` block) so the two contradicting references agree; rename the presenter
      integration to the actual `goTo()` method; switch the timer from `requestAnimationFrame` to `setInterval` on
      `Date.now()`; render real scaled slide previews. Add a privacy note: speaker notes ship readable inside the shared file.
    - *Files:* `skills/slide-sage/references/presenter-mode.md`, `skills/slide-sage/references/html-template.md`.

18. **Render-verification step.**
    - When a browser/Playwright tool is available, screenshot 2-3 representative slides (chart slides especially) at a
      reference viewport and a short viewport, check `scrollHeight > clientHeight` and console errors, and fix before delivery.
    - Ship a small static validator (`skills/slide-sage/scripts/validate`) as the always-available fallback: class-integrity, inline-style
      audit, theme-variable usage.
    - *Why:* converts the "NON-NEGOTIABLE" viewport rule into an enforced check; catches the one failure class you cannot see from source.

### Phase 5 - Behavior, evals, and release

19. **Gap-driven interview + non-interactive rule.**
    - Infer audience/style when the prompt is detailed and state the choice in one line; ask only when genuinely thin.
      Hard rule: never block in one-shot/subagent/CI runs (pick sensible defaults and note them). Align AGENTS.md and
      `skills/slide-sage/SKILL.md` to identical wording. Optional visual-preview step only when style is unspecified and a browser is available.
    - *Why:* the current mandatory interview contradicts AGENTS.md, fails the skill's own evals, and stalls forever in CI.

20. **Frontmatter description rewrite for triggering.**
    - Cover all three modes (new / PPT-PDF conversion / enhancement) with trigger vocabulary (slide deck, pitch deck,
      PowerPoint, pptx, convert, PDF) plus a short "not for" clause; move the library catalog out of the description.
    - *Why:* the description omits the conversion mode entirely, which hurts auto-triggering.

21. **Migrate and actually run the evals.**
    - Rewrite `skills/slide-sage/evals/evals.json` to the reference schema (skill_name wrapper, id, expected_output, checkable assertions),
      remove the stale Mermaid references (Mermaid was replaced by CSS/HTML diagrams two commits ago), add a fixture for
      the enhancement case, and name a concrete runner (a GitHub Action + a local script) so the evals are executable,
      not documentation.
    - *Why:* the current evals expect removed Mermaid output, reference a nonexistent file, and nothing runs them.

22. **Release automation + migration note.**
    - `CHANGELOG.md`, a tag-driven `release.yml` with a version-consistency guard (matches the reference repos), and a
      CHANGELOG entry telling the existing installs and git-clone users how to get the upgraded skill
      (`npx skills add rhnfzl/slide-sage` re-install). Cut the first tagged release.
    - Wire one render-check of an example deck into CI so a preset/theme regression cannot ship silently.

### Phase 6 - Cross-repo consistency (parallel, light touch)

23. **Align all three repos** (`slide-sage`, `../human-html`, `../explore-unknowns`).
    - Confirm the three share marketplace metadata, manifests, `skills.sh.json`, SECURITY, CHANGELOG, and release automation.
      Slide Sage's runtime is `skills/slide-sage/SKILL.md` and must not regain a root `SKILL.md`; apply only the needed
      consistency deltas to the other two and do not rewrite their content.
    - *Why:* they become a coherent "rhnfzl skills" set with valid install behavior, even where their runtime layouts differ.

---

## Sequencing and what ships when

- **Ship 1 (Phases 1-2):** clean `npx` install, proper listing, banner-led README, live example gallery. This alone
  satisfies Goals 1 and 2 and is safe to release on its own.
- **Ship 2 (Phases 3-4):** the decks get visibly better and more reliable (theme fix, presets, charts, export, a11y, offline).
- **Ship 3 (Phase 5-6):** behavior, evals, release automation, and cross-repo consistency.

## Risks and how the plan handles them

- **Full preset rebuild is the largest single effort.** Mitigation: keep the current 6 as a fallback set until the new
  presets pass the render-check; ship presets incrementally.
- **Playwright and inline-vendored mode add optional dependencies.** Both are opt-in; the zero-dependency browser-print
  and CDN paths remain the defaults, so nothing new is forced on users.
- **Opt-in 16:9 mode touches the 754-line CSS.** Mitigation: it is additive (a mode class), the fluid default is untouched.
- **Cross-repo work could scope-creep.** Mitigation: Phase 6 is consistency-only, deltas not rewrites.

## Out of scope (for now)

- Live real-time collaboration, hosted SaaS, or accounts (Slide Sage stays local-first, single-file).
- Native high-fidelity PPTX export (documented as a known limitation; point users to Anthropic's pptx skill for that need).
- Relocating another repo to a `skills/<name>/` subfolder. Slide Sage's user-authorized runtime layout is already resolved above.

## Open implementation details (decided at build time, not blocking)

- Exact fixed-canvas dimensions for the 16:9 mode (1280x720 vs 1920x1080) and the scale strategy.
- The precise 8-10 preset lineup and their signature devices.
- Whether the static validator is Python or Node (lean Python to match existing `scripts/`).
- Banner composition and the Pages gallery layout.
