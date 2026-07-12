# Changelog

All notable changes to this skill are documented here. The version in this file,
in `.claude-plugin/plugin.json`, and in `skills/slide-sage/SKILL.md` frontmatter must match the
release tag. The release workflow fails if they drift.

## Unreleased

## 2.1.0 - 2026-07-12

### Upgrade

- Existing `npx skills add` installations should run
  `npx skills add rhnfzl/slide-sage` again to receive this release.
- Manual `git clone` users should pull `v2.1.0` and keep their agent pointed at
  `skills/slide-sage/SKILL.md`.

### Security

- Every CDN library a generated deck can load is now pinned with Subresource
  Integrity (`integrity` + `crossorigin`): Chart.js, Prism (and its language
  components), ECharts, D3, Rough.js, CountUp.js, Typed.js, q5, Cytoscape, and
  Frappe Charts. The browser refuses a tampered or swapped CDN file.
- Upgraded ECharts from 5.5.1 to 6.1.0 to clear XSS advisory CVE-2026-45249
  (Apache ECharts below 6.1.0). SRI protects the fetched bytes but not the
  vulnerability in the pinned release, so the version bump is the fix.

### Fixed

- Repaired broken CDN references that loaded an error stub instead of the
  library: q5 (`q5@2.1.2/q5.min.js` did not exist) now uses `q5@4.7.4/q5.js`.
- Aligned the SKILL.md library table with the version-pinned snippets (CountUp,
  Typed, and Rough previously listed mismatched versions or non-minified paths).
- Corrected gallery and README wording so a sample chart reads as sample, and
  made the CDN-versus-offline behavior explicit.

### Added

- Network / dependency-graph slides via Cytoscape.js 3, and calendar / activity
  heatmap slides via Frappe Charts 1.6, both with SRI-pinned, render-validated
  snippets and accessibility fallbacks. These replace two previously advertised
  but broken (Sigma and Frappe) capability rows.

## 2.0.1 - 2026-07-12

### Upgrade

- Existing `npx skills add` installations should run
  `npx skills add rhnfzl/slide-sage` again to receive the complete payload.
- Manual `git clone` users should pull `v2.0.1` and point their agent at
  `skills/slide-sage/SKILL.md`.

### Fixed

- `npx skills add rhnfzl/slide-sage` now installs the complete presentation
  skill, including its guides, references, templates, scripts, examples,
  evals, and assets.

## 2.0.0 - 2026-07-11

### Upgrade

- Existing `npx skills add` installations and manual `git clone` users can get
  the upgraded skill by running `npx skills add rhnfzl/slide-sage` again. Clone
  users can alternatively pull this tag and keep their agent pointed at
  `SKILL.md`.

### Added

- Packaged skill metadata, gallery examples, polished presentation presets,
  offline vendoring, static validation, PDF export, and accessibility support.
- Behavior evals with a real enhancement fixture, CI validation, and a browser
  render check for the metrics example.

## 1.0.0 - 2026-03-07

Initial public release.
