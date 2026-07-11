# Slide Sage Upgrade - Build Checklist

Working checklist for the autonomous build. Source of truth for scope: `docs/UPGRADE_PLAN.md`.
Mark each item `[x]` when done AND reviewed (Codex second-eye + CodeRabbit both clean or findings addressed).

## Ground rules for the build session

- Branch first: `feat/upgrade-<phase>` off `main`. Never commit the upgrade directly to `main`.
- Review gate on every meaningful change (a coherent commit-sized unit, not every file save):
  1. Codex second-eye: dispatch the `second-eye-reviewer-codex` agent on the diff.
  2. CodeRabbit: run the `coderabbit-review` skill on the branch/diff.
  3. Address findings (or record why not) before marking the item done.
- Keep decisions consistent with `docs/UPGRADE_PLAN.md` "Locked decisions" table. Do not re-open forks.
- Update this file as you go: check items, add sub-items discovered during build, note blockers inline.
- Non-interactive: proceed autonomously on reversible steps; stop only for a genuinely destructive or scope-changing action.

## Progress log

- 2026-07-11: Ship 1 implementation committed; review fixes in progress after Codex and CodeRabbit findings.
- 2026-07-11: CodeRabbit reference-loading finding declined because the project contract requires the three base references for every deck.
- 2026-07-11: Added installed-payload inspection as a stricter verification sub-item without changing the locked packaging decision.
- 2026-07-11: Ship 1 items 1-12 passed Codex second-eye and CodeRabbit review. Pages workflow is ready; item 13 awaits repository Pages activation after merge.
- (append dated one-line entries here as phases complete)

---

## Phase 1 - Packaging, install, listing (Ship 1)

- [x] 1. Add `.claude-plugin/marketplace.json` (`source: "./"`, owner rhnfzl) + `.claude-plugin/plugin.json` (name/desc/version/author/license MIT/keywords)
- [x] 2. Add `skills.sh.json` (one grouping, human-facing title/description)
- [x] 3. Add SKILL.md frontmatter `license: MIT` + `metadata: {version, author}`
- [x] 4. Rewrite README install to lead with `npx skills add rhnfzl/slide-sage`; remove `claude skill add`; collapse per-tool matrix into one `<details>`
- [x] 5. Delete `CLONE.md` and `.github/workflows/clone-count.yml`; replace badge row (skills.sh install + Release + License)
- [x] 6. `.gitignore` `.claude/` and `.agent-harness/`; track `AGENTS.md`
- [x] 7. Add `SECURITY.md` + condensed Trust section in README
- [x] 8. Verify locally: `npx skills add ./ --list` resolves one skill with all support dirs
  - [x] Install into an isolated temporary agent home and assert `references/`, `templates/`, `assets/`, and `scripts/` are present

## Phase 2 - README, banner, visual proof (Ship 1)

- [x] 9. Rewrite README to reference-repo anatomy (~120-150 lines, banner + 3 badges + one-liner + quickstart + why + what's-in-the-box + trust); scrub em dashes; engineer/tech-lead audience
- [x] 10. Drop competitor comparison table; add one honest positioning paragraph + gallery link (name pptx skill for native PPTX)
- [x] 11. Build `examples/slide-sage-intro.html` + 2-3 more decks (metrics review, architecture teaching) using the skill itself; add `!examples/**/*.html` gitignore negation
- [x] 12. Compose banner `assets/banner.webp` from the demo deck's best slides
- [ ] 13. GitHub Pages `index.html` gallery linking live example decks; wire into README

## Phase 3 - Output quality (Ship 2)

- [ ] 14. Fix theme-variable seam: bridge base `--color-*` and preset `--color-*-primary`; replace `rgba(255,255,255,x)` with `color-mix`; delete dead `[data-theme=light]` blocks
- [ ] 15. Full preset rebuild: `references/presets/<slug>.md` + compact index (mood/tone/best_for/avoid_for/formality/density/scheme); 8-10 presets each with 2-3 structural signatures; drop Inter + catppuccin default; add serif-display + editorial presets; keep system-font fallbacks; tone-first matching
- [ ] 16. Add anti-slop doctrine + no-fake-data rule to SKILL.md (interactive: ask for numbers; non-interactive: labeled SAMPLE data, never silent, never block)
- [ ] 17. Re-palette `templates/diagrams/*.svg` to Tier-1 colorblind palette; per-diagram filter-id prefixes; overlay-based cylinder shading; label fill as variable
- [ ] 18. Chart animation on slide-enter: `slidechange`/`onSlideEnter` lifecycle; init charts `animation:false`, replay/CountUp on active; respect `prefers-reduced-motion`

## Phase 4 - Reliability, a11y, honest offline (Ship 2)

- [ ] 19. Bump Prism 1.29.0 -> 1.30.0 (SKILL.md, html-template.md, code-highlighting.md) + SRI integrity/crossorigin
- [ ] 20. Playwright PDF export script + settle chart animations before print; fix print CSS; browser-print stays fallback; open file + emit absolute path at end of run
- [ ] 21. Opt-in inline-vendored offline mode (bake pinned libs); correct README offline claim; add license notices (ECharts NOTICE Apache-2.0, D3 ISC, Prism MIT, Google Fonts OFL)
- [ ] 22. Accessibility: focus-visible, inert/aria-hidden on inactive slides, dialog role + focus trap on shortcuts overlay; chart-data a11y (role=img + aria-label + visually-hidden data table + noscript fallback)
- [ ] 23. Fix presenter mode: JSON `<script>` notes format; rename to real `goTo()`; timer -> setInterval on Date.now(); real scaled previews; privacy note about readable notes
- [ ] 24. Render-verification step: screenshot 2-3 slides when browser available (check overflow + console); static `scripts/validate` fallback (class integrity, inline-style audit, theme-var usage)

## Phase 5 - Behavior, evals, release (Ship 3)

- [ ] 25. Gap-driven interview + hard non-interactive rule; align AGENTS.md and SKILL.md wording; optional visual-preview only when style unspecified + browser available
- [ ] 26. Rewrite frontmatter description: all 3 modes + trigger vocab (slide deck, pitch deck, PowerPoint, pptx, convert, PDF) + short not-for clause; move library catalog out
- [ ] 27. Migrate `evals/evals.json` to reference schema (skill_name/id/expected_output/assertions); remove Mermaid refs; add enhancement fixture; name a concrete runner (GH Action + local script)
- [ ] 28. `CHANGELOG.md` + tag-driven `release.yml` with version-consistency guard; CHANGELOG re-install note for existing users; wire one example-deck render-check into CI; cut first tagged release

## Phase 6 - Cross-repo consistency (Ship 3)

- [ ] 29. Align `../human-html` and `../explore-unknowns` to the same packaging convention; apply only consistency deltas, do not rewrite their content

## Definition of done

- [ ] All items checked and reviewed
- [ ] `npx skills add rhnfzl/slide-sage` installs a working, full-payload skill
- [ ] README renders with banner; Pages gallery live
- [ ] Evals run green via the named runner
- [ ] First release tagged; PR(s) opened for your review
