# Serif Signal

- Mood: dramatic
- Tone: keynote, optimistic
- Best for: launches, technical narratives, conference talks
- Avoid for: implementation reference and dense data tables
- Formality: medium
- Density: low
- Scheme: dark

## Signatures

1. Large serif statements occupy most of the canvas.
2. A single bright signal color marks the narrative turn.
3. Cards are rare; diagrams and one line of evidence carry the slide.

## CSS

```css
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Playfair+Display:ital,wght@0,600;0,700;1,600&family=Work+Sans:wght@400;500;600&display=swap');

html[data-theme="serif-signal"] {
  --color-bg-primary: #17131E; --color-bg-secondary: #231B2E; --color-bg-surface: #2E2440; --color-bg-elevated: #3A2F50;
  --color-text-primary: #F5EFFA; --color-text-secondary: #CDBFDC; --color-text-muted: #8F7EA1; --color-text-inverse: #17131E;
  --color-accent: #EE7733; --color-accent-secondary: #4AA3D8; --color-gold: #D4B02A; --color-accent-hover: #F5A36E; --color-accent-subtle: #3D291F;
  --color-border: color-mix(in srgb, var(--color-text-primary) 16%, transparent);
  --font-heading: 'Playfair Display', Georgia, serif; --font-body: 'Work Sans', Arial, sans-serif; --font-mono: 'DM Mono', ui-monospace, monospace;
  --radius-sm: clamp(0.25rem, 0.5vw, 0.4rem); --radius-md: clamp(0.5rem, 0.9vw, 0.75rem); --radius-lg: clamp(0.75rem, 1.3vw, 1.1rem);
  --preset-title-size: clamp(2.15rem, 4.8vw, 4.2rem); --preset-section-size: clamp(1.68rem, 3.6vw, 3rem); --preset-kicker-tracking: 0.2em; --preset-divider-width: 3px; --preset-stat-treatment: tabular-nums;
}
```
