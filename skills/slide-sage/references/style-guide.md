# Slide Sage Style Guide

Slide Sage chooses a presentation personality from the audience's desired tone, then applies a complete preset. A preset is more than a palette: it supplies type, density, card treatment, and one or two signature layout devices so two decks do not become the same layout with different colors.

## Tier 1: data visualization palette

Use this categorical palette for charts regardless of the visual preset. It is colorblind-safe and keeps series meaning stable between decks.

```css
:root {
  --cat-1: #0077BB;
  --cat-2: #CC3311;
  --cat-3: #009988;
  --cat-4: #EE7733;
  --cat-5: #3344AA;
  --cat-6: #EE3377;
  --cat-7: #BBAA33;
  --cat-8: #888888;
  --chart-positive: #2A9D5C;
  --chart-negative: #CC3311;
  --chart-neutral: #888888;
  --chart-highlight: #EE7733;
}
```

Use sequential palettes for heatmaps and diverging palettes for positive-vs-negative comparisons. Do not use a red-to-green scale as the only carrier of chart meaning. Labels, patterns, or direct values must still distinguish a series.

## Tier 2: Tone-first matching

| Preset | Mood | Tone | Best for | Avoid for | Formality | Density | Scheme |
|---|---|---|---|---|---|---|---|
| [Arctic Dawn](presets/arctic-dawn.md) | precise | calm, evidence-led | research, metrics | emotional keynote | high | medium | light or dark |
| [Ember](presets/ember.md) | decisive | warm, urgent | operating reviews | detailed reference deck | medium | high | dark or light |
| [Jade Circuit](presets/jade-circuit.md) | technical | composed, systems-led | architecture, engineering | soft editorial story | medium | medium | dark or light |
| [Dusk Palette](presets/dusk-palette.md) | expressive | reflective, creative | product design, narrative | dense dashboards | medium | low | light or dark |
| [Monochrome Pro](presets/monochrome-pro.md) | restrained | executive, direct | board updates, decisions | playful teaching | high | low | light or dark |
| [Ocean Deep](presets/ocean-deep.md) | confident | professional, human | client-facing technical work | austere reports | high | medium | dark or light |
| [Editorial Ledger](presets/editorial-ledger.md) | thoughtful | journalistic, explanatory | teaching, strategy, research | real-time dashboard | high | medium | light |
| [Serif Signal](presets/serif-signal.md) | dramatic | keynote, optimistic | launches, technical narrative | implementation reference | medium | low | dark |

### Selection rule

Choose the preset from the requested tone first. Use the content type only as a tie-breaker. A metrics review can use Arctic Dawn for a measured research tone or Ember for an urgent operating review. Do not map industries to a fixed preset.

If the prompt gives no style direction, state the inferred tone and chosen preset in one sentence. For a non-interactive run, choose a sensible default and continue.

## Applying a preset

1. Include only the selected preset's font import, if its font is appropriate for the delivery environment.
2. Set `data-theme` and `data-mode` on `<html>`.
3. Inline the selected preset CSS after `viewport-base.css`.
4. Use the supplied `--preset-*` tokens for title scale, kicker treatment, dividers, cards, and stat presentation.
5. Keep Tier 1 chart colors independent from the preset's accent color.

The shared base CSS bridges the preset vocabulary to its components:

```css
--color-bg: var(--color-bg-primary);
--color-text: var(--color-text-primary);
--color-heading: var(--color-text-primary);
--color-surface: var(--color-bg-surface);
--radius: var(--radius-lg);
```

## Custom themes

When a user supplies brand colors, use the same vocabulary as every named preset. Keep a system-font fallback because corporate CSP rules can block web fonts.

```css
html[data-theme="custom"] {
  --color-bg-primary: hsl(var(--brand-hue) 12% 98%);
  --color-bg-secondary: hsl(var(--brand-hue) 14% 94%);
  --color-bg-surface: #FFFFFF;
  --color-bg-elevated: #FFFFFF;
  --color-text-primary: hsl(var(--brand-hue) 25% 13%);
  --color-text-secondary: hsl(var(--brand-hue) 14% 35%);
  --color-text-muted: hsl(var(--brand-hue) 10% 52%);
  --color-text-inverse: #FFFFFF;
  --color-accent: var(--brand-primary);
  --color-accent-secondary: var(--brand-secondary, var(--cat-3));
  --color-gold: var(--cat-7);
  --color-border: color-mix(in srgb, var(--color-text-primary) 14%, transparent);
  --font-heading: Georgia, 'Times New Roman', serif;
  --font-body: ui-sans-serif, system-ui, sans-serif;
  --font-mono: ui-monospace, Consolas, monospace;
  --radius-sm: clamp(0.2rem, 0.4vw, 0.35rem);
  --radius-md: clamp(0.35rem, 0.7vw, 0.6rem);
  --radius-lg: clamp(0.5rem, 1vw, 0.85rem);
}
```

## Visual depth

Use visual polish to emphasize the story, not decorate every surface.

- Use one intentional reveal sequence per slide at most.
- Use a background grid only when it clarifies a technical or data-led tone.
- Use a glow on one key element, not every card.
- Prefer dividers, whitespace, and typographic hierarchy before adding cards.
- A visual treatment must earn its place by clarifying hierarchy, comparison, or state.

## Title rule

Name the whole presentation, not a subsystem. If a deck spans architecture, delivery, security, and operating metrics, choose an umbrella title that covers all four.
