# Changelog

All notable changes to this skill are documented here. The version in this file,
in `.claude-plugin/plugin.json`, and in `skills/slide-sage/SKILL.md` frontmatter must match the
release tag. The release workflow fails if they drift.

## Unreleased

## 2.0.1 - 2026-07-12

### Fixed

- `npx skills add rhnfzl/slide-sage` now installs the complete presentation
  skill, including its guides, references, templates, scripts, examples,
  evals, and assets.

## 2.0.0 - 2026-07-11

### Upgrade

- Existing `npx skills add` installations and manual `git clone` users can get
  the upgraded skill by running `npx skills add rhnfzl/slide-sage` again. Clone
  users can alternatively pull this tag and keep their agent pointed at
  `skills/slide-sage/SKILL.md`.

### Added

- Packaged skill metadata, gallery examples, polished presentation presets,
  offline vendoring, static validation, PDF export, and accessibility support.
- Behavior evals with a real enhancement fixture, CI validation, and a browser
  render check for the metrics example.

## 1.0.0 - 2026-03-07

Initial public release.
