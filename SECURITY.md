# Security

Slide Sage creates local HTML presentations. Installing the skill copies files only. It does not run a postinstall script, upload a deck, or add Slide Sage telemetry.

## External touch-points

Generated decks can load version-pinned chart, code-highlighting, and animation libraries from a CDN. Those requests happen in the reader's browser only when the generated deck includes the library. Presets can also load a Google Fonts stylesheet. Chart-free decks with no web fonts make no network request. CDN-backed decks need network access on first load.

`scripts/inline-vendor.py` is an opt-in conversion step. When invoked, it downloads only its documented, version-pinned libraries, embeds them in a new HTML file, removes Google Fonts imports, and refuses unsupported static remote assets. It embeds [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) in the generated HTML. It cannot prove that arbitrary custom JavaScript will never make a network request.

The utilities under `scripts/` run only when a user or agent invokes them for source validation, PDF export, PowerPoint extraction, PDF extraction, or image processing. `export-pdf` opens the deck in a local Playwright browser and may download the matching Chromium binary on its first run. Installing the skill does not execute any script.

The `npx skills add` installer may record its own anonymous install telemetry. Slide Sage neither adds to nor receives that data.

Generated presentations can contain source material, speaker notes, and embedded data in readable HTML. Review a deck before sharing it and remove anything the audience should not receive.

## Reporting

Found a security issue? Use the repository's private vulnerability reporting, if enabled, or open an issue at https://github.com/rhnfzl/slide-sage/issues when public disclosure is appropriate.
