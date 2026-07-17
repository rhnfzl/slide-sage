# Slide Sage - AI Presentation Skill

> Cross-platform instructions for AI coding tools (Claude Code, Codex CLI, Gemini CLI, Cursor, Copilot)

When a user asks to create a presentation, build slides, convert a PowerPoint or PDF, or make a slide deck, follow these instructions.

## Quick Start

1. Read `skills/slide-sage/SKILL.md` for the full workflow
2. Read only the reference files you need from `skills/slide-sage/references/`
3. Generate a single HTML file with inline CSS/JS
4. All chart/diagram libraries loaded from CDN

## What This Skill Does

Creates **data-rich, interactive HTML presentations** as single files. Specializes in:
- Data visualization (Chart.js, ECharts, D3.js charts)
- Architecture diagrams (CSS/HTML diagrams, SVG templates, inline SVG)
- Code slides with syntax highlighting (Prism.js)
- Professional styling with colorblind-safe palettes
- Keyboard navigation, touch support, presenter mode

## Workflow

1. **Detect mode**: New presentation / PPT/PDF conversion / enhancement of existing HTML
2. **Gap-driven intake**: Apply the intake rule below before generating
3. **Content analysis**: Identify what libraries are needed (charts? diagrams? code?)
4. **Read relevant references**: Only load the reference files needed for this presentation
5. **Generate**: Single HTML file with all CSS/JS inline, libraries from CDN
6. **Deliver**: Save file, mention how to open (browser) and export (Print > Save as PDF)

## Intake rule

Infer audience and style from a detailed prompt and state the choice in one line. Ask only when the prompt is genuinely thin. Never block in one-shot, subagent, or CI runs: choose sensible defaults and state them in one line. Offer a visual preview only when style is unspecified and a browser is available.

When an interactive response would materially change the deck, ask one focused question. The visual preview is optional and must not delay generation.

### Reader and density (ask when the prompt does not say)

Two answers decide whether a deck lands, and **neither can be inferred from the audience**. A leadership deck can be diagram-led or text-rich; the same deck can be presented or forwarded. A prompt almost never states either, so both are usually genuine gaps.

- **"Will you present this live, send it to be read on its own, or both?"** decides WHERE the context lives. `present` and `both` keep the slide clean and put the recall material in speaker notes, which means presenter mode ships. `send` folds that context onto the slide face, because nobody is there to explain it.
- **"Diagram-led, balanced, or text-rich?"** decides HOW MUCH prose sits beside the visual. `diagram-led` is the visual plus at most 3 lines. `balanced` (default) is a lead sentence, the visual, then 4 to 6 points. `text-rich` puts the reason and the caveat on the slide face.

Terse and dense are both wrong when guessed, and guessing overcorrects. A deck stripped to diagrams starves the presenter of anything to recall from; a padded deck walls off the room it is shown to. "Too much text last time" does not mean `diagram-led` this time, it means reader and density were never separated. Ask instead of swinging.

Notes the presenter cannot open during the talk do not exist. Never ship a `speaker-notes` block without presenter mode.

## Reference Files (load on demand)

| File | When to Load |
|------|-------------|
| `skills/slide-sage/references/html-template.md` | Always (base HTML structure) |
| `skills/slide-sage/references/viewport-system.md` | Always (responsive CSS rules) |
| `skills/slide-sage/references/style-guide.md` | When choosing visual style |
| `skills/slide-sage/references/viz-integration.md` | When slides have charts or data |
| `skills/slide-sage/references/diagram-patterns.md` | When slides have architecture/flow diagrams |
| `skills/slide-sage/references/animation-guide.md` | When choosing animation intensity |
| `skills/slide-sage/references/code-highlighting.md` | When slides have code snippets |
| `skills/slide-sage/references/presenter-mode.md` | Whenever the deck has speaker notes (reader is `present` or `both`). Not optional. |
| `skills/slide-sage/references/css-class-inventory.md` | Always (CSS class lookup + inline style rules) |

## Non-Negotiable Rules

- Every slide: `height: 100vh; overflow: hidden` - no scrolling
- All font sizes use `clamp()` - never fixed px/rem
- Include `skills/slide-sage/assets/viewport-base.css` content inline
- Colorblind-safe palettes for all data visualization
- Support `prefers-reduced-motion` and `@media print`
- Keyboard navigation: arrows, space, page up/down
- Every CSS class in HTML must be defined in viewport-base.css, a template, or the `<style>` block
- Max ~3 inline styles per slide average; repeating patterns (3+ elements) must be CSS classes
- Run Pre-Delivery Validation (Phase 5) before writing the final file

## Tool Compatibility

This skill works with any AI coding tool that can:
- Read markdown files (`skills/slide-sage/SKILL.md`, `skills/slide-sage/references/`)
- Write HTML files
- Run bash commands (for PPT conversion scripts)

If your tool has `WebFetch`, you can verify CDN URLs are current.
If your tool lacks `WebFetch`, use the pinned CDN URLs in the reference files - they are stable.
