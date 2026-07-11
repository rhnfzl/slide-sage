# Arctic Dawn

- Mood: precise
- Tone: calm, evidence-led
- Best for: research reviews, metrics, scientific teaching
- Avoid for: emotional launches and high-energy keynotes
- Formality: high
- Density: medium
- Scheme: light or dark

## Signatures

1. Hairline dividers separate evidence blocks instead of heavy cards.
2. Labels use a compact mono kicker above a measured serif heading.
3. Charts sit on open space with direct captions, not decorative panels.

## CSS

```css
@import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@500;600;700&family=Atkinson+Hyperlegible:wght@400;700&display=swap');

html[data-theme="arctic-dawn"] {
  --color-bg-primary: #FAFCFE; --color-bg-secondary: #EDF3F8; --color-bg-surface: #FFFFFF; --color-bg-elevated: #FFFFFF;
  --color-text-primary: #1A2B3C; --color-text-secondary: #4A6178; --color-text-muted: #6F869B; --color-text-inverse: #FAFCFE;
  --color-accent: #0077BB; --color-accent-secondary: #009988; --color-gold: #BBAA33; --color-accent-hover: #005F96; --color-accent-subtle: #D4E8F7;
  --color-border: color-mix(in srgb, var(--color-text-primary) 15%, transparent);
  --font-heading: 'Source Serif 4', Georgia, 'Times New Roman', serif; --font-body: 'Atkinson Hyperlegible', Arial, sans-serif; --font-mono: ui-monospace, Consolas, monospace;
  --radius-sm: clamp(0.1rem, 0.25vw, 0.2rem); --radius-md: clamp(0.2rem, 0.45vw, 0.35rem); --radius-lg: clamp(0.3rem, 0.65vw, 0.5rem);
  --preset-title-size: clamp(1.85rem, 4.1vw, 3.6rem); --preset-section-size: clamp(1.45rem, 3.1vw, 2.6rem); --preset-kicker-tracking: 0.16em; --preset-divider-width: 1px; --preset-stat-treatment: tabular-nums;
}
html[data-theme="arctic-dawn"][data-mode="dark"] {
  --color-bg-primary: #10202E; --color-bg-secondary: #162C3D; --color-bg-surface: #1E374B; --color-bg-elevated: #284458;
  --color-text-primary: #EAF2F7; --color-text-secondary: #B0C6D6; --color-text-muted: #7D9AAC; --color-text-inverse: #10202E;
  --color-accent: #4AA3D8; --color-accent-secondary: #48B7A9; --color-gold: #D4B02A; --color-accent-hover: #78C1E7; --color-accent-subtle: #15384A;
}
```
