# Slide Sage - AI Presentation Skill

> Cross-platform instructions for AI coding tools (Claude Code, Codex CLI, Gemini CLI, Cursor, Copilot)

When a user asks to create a presentation, build slides, convert a PowerPoint or PDF, or make a slide deck, follow these instructions.

## Quick Start

1. Read `SKILL.md` in this directory for the full workflow
2. Read only the reference files you need from `references/`
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

## Reference Files (load on demand)

| File | When to Load |
|------|-------------|
| `references/html-template.md` | Always (base HTML structure) |
| `references/viewport-system.md` | Always (responsive CSS rules) |
| `references/style-guide.md` | When choosing visual style |
| `references/viz-integration.md` | When slides have charts or data |
| `references/diagram-patterns.md` | When slides have architecture/flow diagrams |
| `references/animation-guide.md` | When choosing animation intensity |
| `references/code-highlighting.md` | When slides have code snippets |
| `references/presenter-mode.md` | When user requests presenter view |
| `references/css-class-inventory.md` | Always (CSS class lookup + inline style rules) |

## Non-Negotiable Rules

- Every slide: `height: 100vh; overflow: hidden` - no scrolling
- All font sizes use `clamp()` - never fixed px/rem
- Include `assets/viewport-base.css` content inline
- Colorblind-safe palettes for all data visualization
- Support `prefers-reduced-motion` and `@media print`
- Keyboard navigation: arrows, space, page up/down
- Every CSS class in HTML must be defined in viewport-base.css, a template, or the `<style>` block
- Max ~3 inline styles per slide average; repeating patterns (3+ elements) must be CSS classes
- Run Pre-Delivery Validation (Phase 5) before writing the final file

## Tool Compatibility

This skill works with any AI coding tool that can:
- Read markdown files (SKILL.md, references/)
- Write HTML files
- Run bash commands (for PPT conversion scripts)

If your tool has `WebFetch`, you can verify CDN URLs are current.
If your tool lacks `WebFetch`, use the pinned CDN URLs in the reference files - they are stable.
