# Security

Slide Sage creates local HTML presentations. Installing the skill copies files only. It does not run a postinstall script, upload a deck, or add Slide Sage telemetry.

## External touch-points

Generated decks can load version-pinned chart, code-highlighting, and animation libraries from a CDN. Those requests happen in the reader's browser only when the generated deck includes the library. Presets can also load a Google Fonts stylesheet, which is selected by the preset rather than pinned as a package URL. Chart-free decks with no web fonts make no network request. CDN-backed decks need network access on first load.

The Python utilities under `scripts/` run only when a user or agent invokes them for PowerPoint extraction, PDF extraction, or image processing. Installing the skill does not execute them.

The `npx skills add` installer may record its own anonymous install telemetry. Slide Sage neither adds to nor receives that data.

Generated presentations can contain source material, speaker notes, and embedded data in readable HTML. Review a deck before sharing it and remove anything the audience should not receive.

## Reporting

Found a security issue? Use the repository's private vulnerability reporting, if enabled, or open an issue at https://github.com/rhnfzl/slide-sage/issues when public disclosure is appropriate.
