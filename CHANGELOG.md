# Changelog

All notable changes to this skill are documented here. The version in this file,
in `.claude-plugin/plugin.json`, and in `skills/slide-sage/SKILL.md` frontmatter must match the
release tag. The release workflow fails if they drift.

## Unreleased

## 2.2.0 - 2026-07-17

A deck has two readers: the room, and the person standing up to talk from it. This
release stops Slide Sage from serving only the first one.

### Upgrade

- Existing `npx skills add` installations should run
  `npx skills add rhnfzl/slide-sage` again to receive this release.
- Manual `git clone` users should pull `v2.2.0` and keep their agent pointed at
  `skills/slide-sage/SKILL.md`.
- Nothing you have already generated needs regenerating. This release changes what
  the skill asks before it builds the next deck.

### Fixed

- Presenter mode is no longer opt-in. It ships whenever the deck has speaker notes.
  The skill was previously told never to ask about presenter mode AND to load it
  only on explicit request, so notes shipped inside a `<script id="speaker-notes">`
  block that the presenter could not open while presenting. The recall material was
  in the file and invisible to the one person who needed it.
- Delivery now says "Press P for your notes" out loud whenever a deck ships notes.
  A presenter who does not know the notes are there gets no value from them.

### Added

- Intake asks two questions when the prompt does not answer them, because neither
  can be inferred from the audience. A leadership deck can be diagram-led or
  text-rich, and the same deck can be presented or forwarded.
  - "Will you present this live, send it to be read on its own, or both?" decides
    where the context lives. `present` and `both` keep the slide clean and put the
    recall material in notes; `send` folds that context onto the slide face,
    because nobody is there to explain it.
  - "Diagram-led, balanced, or text-rich?" decides how much prose sits beside the
    visual.
- Density scales the Phase 4 slide limits instead of one fixed shape, from
  `diagram-led` (the visual plus at most three lines) through `balanced` to
  `text-rich` (the reason and the caveat on the slide face). It never relaxes the
  100vh rule; content that does not fit still splits.
- Delivery states the reader and density the deck was built at, so a wrong call
  costs one line of feedback rather than a rebuild.
- Pre-delivery Check 6 fails a deck that ships speaker notes with no way to open
  them.

### Changed

- The reasoning is written into the rule, because the next agent meets the same
  temptation: terse and dense are both wrong when guessed, and guessing
  overcorrects. A deck stripped to diagrams starves the presenter of anything to
  recall from; a padded one walls off the room. "Too much text last time" does not
  mean `diagram-led` this time, it means reader and density were never separated.

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
