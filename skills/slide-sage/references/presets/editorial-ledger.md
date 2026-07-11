# Editorial Ledger

- Mood: thoughtful
- Tone: journalistic, explanatory
- Best for: teaching, strategy, research synthesis, written narrative
- Avoid for: real-time dashboards and animated keynotes
- Formality: high
- Density: medium
- Scheme: light

## Signatures

1. Serif display headings sit beside narrow measure body copy.
2. A vertical rule frames the primary claim or quote.
3. Tables and source lines are treated as editorial footnotes.

## CSS

```css
@import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=Source+Sans+3:wght@400;600;700&display=swap');

html[data-theme="editorial-ledger"] {
  --color-bg-primary: #F7F3EB; --color-bg-secondary: #EEE7DA; --color-bg-surface: #FFFDF8; --color-bg-elevated: #FFFFFF;
  --color-text-primary: #26231D; --color-text-secondary: #5E594E; --color-text-muted: #847D70; --color-text-inverse: #F7F3EB;
  --color-accent: #3344AA; --color-accent-secondary: #CC3311; --color-gold: #9A7B20; --color-accent-hover: #29368A; --color-accent-subtle: #E2E5F8;
  --color-border: color-mix(in srgb, var(--color-text-primary) 16%, transparent);
  --font-heading: 'Libre Baskerville', Georgia, serif; --font-body: 'Source Sans 3', Arial, sans-serif; --font-mono: ui-monospace, Consolas, monospace;
  --radius-sm: 0; --radius-md: 0; --radius-lg: 0;
  --preset-title-size: clamp(1.95rem, 4.3vw, 3.8rem); --preset-section-size: clamp(1.5rem, 3.2vw, 2.7rem); --preset-kicker-tracking: 0.11em; --preset-divider-width: 2px; --preset-stat-treatment: oldstyle-nums;
}
```
