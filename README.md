<p align="center">
  <img src="skills/slide-sage/assets/banner.webp" alt="Slide Sage presentation examples" width="960">
</p>

# Slide Sage

[![skills.sh](https://skills.sh/b/rhnfzl/slide-sage)](https://skills.sh/rhnfzl/slide-sage)
[![Release](https://img.shields.io/github/v/release/rhnfzl/slide-sage)](https://github.com/rhnfzl/slide-sage/releases)
[![License](https://img.shields.io/github/license/rhnfzl/slide-sage)](LICENSE)

**Turn technical material into a presentation people can follow.**

Slide Sage is an open-source Agent Skill for engineers, tech leads, data teams, and technical PMs. It creates data-rich HTML slide decks with charts, architecture diagrams, and code, then packages each deck as a browser-ready file.

Browse the [live gallery](https://rhnfzl.github.io/slide-sage/) for chart, diagram, and code examples, or inspect its [source](index.html).

## Quickstart

One command auto-detects your installed agents:

```bash
npx skills add rhnfzl/slide-sage
```

The installer copies the complete `slide-sage` payload, including its references, templates, scripts, examples, and evals.

Then ask your agent:

```text
Create a metrics review for engineering leadership using these numbers:
deployment frequency 18 to 31 per week, lead time 4.2 to 2.6 days,
and change failure rate 11% to 7%.
```

<details>
<summary>Other install routes and manual use</summary>

- Claude Code plugin: `/plugin marketplace add rhnfzl/slide-sage`, then `/plugin install slide-sage@rhnfzl`
- Manual: clone this repository and link `skills/slide-sage` into your agent's skills directory
- Any compatible tool: point it at `skills/slide-sage/SKILL.md`

</details>

## Why this exists

1. **Technical presentations need evidence.** Slide Sage treats metrics, charts, diagrams, and code as first-class content instead of decoration.
2. **Generated slides need guardrails.** Every slide is constrained to the viewport, uses responsive type, supports keyboard navigation, and includes reduced-motion and print behavior.
3. **The output should stay portable.** A deck opens directly in a browser. Richer decks use pinned CDN libraries by default, and `skills/slide-sage/scripts/inline-vendor.py` can make a supported-library copy local when offline delivery matters.

## What it makes

| Mode | Use it for |
|---|---|
| New presentation | Metrics reviews, architecture walkthroughs, teaching decks, technical pitches |
| PowerPoint or PDF conversion | Turning existing material into an interactive HTML deck |
| HTML enhancement | Improving an existing deck without discarding its content or visual language |

## What's in the box

| Piece | What it does |
|---|---|
| `skills/slide-sage/SKILL.md` | Chooses the workflow, content shape, visual style, and delivery checks |
| `skills/slide-sage/assets/viewport-base.css` | Enforces one-screen slides, responsive type, navigation, print, and accessibility basics |
| `skills/slide-sage/references/` | Focused guidance for charts, diagrams, code, animation, themes, and presenter mode |
| `skills/slide-sage/templates/` | Reusable comparison layouts, SVG diagrams, and icons |
| `skills/slide-sage/scripts/` | Source, render, and eval checks, PDF export, opt-in offline vendoring, and conversion helpers |
| `skills/slide-sage/examples/` | Finished decks showing metrics, architecture, and code treatment |
| `skills/slide-sage/evals/` | Behavior cases for new, conversion, and enhancement workflows |

## A deck stays a file

Slide Sage does not require a presentation runtime, account, or hosted editor. The generated HTML contains its CSS and presentation logic. Optional libraries are included only when the content needs them.

Use Slide Sage when the final delivery can be HTML or PDF and the material benefits from interactive charts or technical visuals. If native, editable PowerPoint output is the requirement, use Anthropic's `pptx` skill instead.

## How it works

1. The agent identifies whether the task is a new deck, a conversion, or an enhancement.
2. It reads only the references needed for the material, then chooses a tone-led visual preset.
3. It generates one HTML file and checks the viewport, CSS classes, data labeling, and delivery path.

## Built-in quality bar

- Every slide fits `100vh` with no internal scrolling
- All text scales with `clamp()` and short-height breakpoints
- Charts use colorblind-safe palettes and descriptive canvas labels
- Diagrams prefer CSS/HTML, then reusable SVG templates, then custom inline SVG
- Code uses language-aware highlighting and stays within a readable line budget
- Arrow keys, space, page keys, Home, End, and touch gestures navigate the deck
- `prefers-reduced-motion` and print styles are included
- Pre-delivery source checks cover CSS classes, inline styles, and theme variables with `skills/slide-sage/scripts/validate presentation.html`

## Examples

| Deck | Shows |
|---|---|
| [Slide Sage introduction](skills/slide-sage/examples/slide-sage-intro.html) | Product story, chart, diagram, and code in one deck |
| [Engineering metrics review](skills/slide-sage/examples/metrics-review.html) | KPI hierarchy and a labeled sample trend chart |
| [Event-driven architecture](skills/slide-sage/examples/architecture-teaching.html) | A technical teaching flow with CSS diagrams and code |

Open any example in a browser. Use arrow keys to navigate, `?` for shortcuts, and `skills/slide-sage/scripts/export-pdf skills/slide-sage/examples/metrics-review.html` for a PDF. Browser Print > Save as PDF remains a fallback.

## Requirements

A modern browser is enough for generated decks. Python 3.11+ plus the packages in `skills/slide-sage/scripts/requirements.txt` is needed only for PowerPoint/PDF conversion and image processing. `skills/slide-sage/scripts/export-pdf` uses an installed Playwright CLI or its pinned `npx` fallback, and downloads matching Chromium on the first export when it is not already available.

## Trust

- Installing copies files. It does not run code or add a postinstall hook.
- Slide Sage adds no telemetry or analytics.
- Package CDN imports are browser-only, version-pinned, and included only when a deck uses them. A deck that uses charts or web fonts needs a network connection for those; it is fully offline only when it has no charts or after `skills/slide-sage/scripts/inline-vendor.py` bakes the libraries in. That script is opt-in, embeds only its supported pinned libraries, removes web-font imports, and refuses remaining static remote assets.
- Python scripts run only on explicit invocation.
- Speaker notes and embedded data remain readable inside a shared HTML file.

Read [SECURITY.md](SECURITY.md) for the complete external-touchpoint rationale.

## Agent support

Slide Sage follows the [Agent Skills](https://agentskills.io) format. `npx skills add` installs it for supported agents including Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI, OpenCode, Amp, and others.

## License

[MIT](LICENSE)
