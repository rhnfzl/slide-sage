# Ocean Deep

- Mood: confident
- Tone: professional, human
- Best for: client-facing technical work, platform overviews, product updates
- Avoid for: austere reports and very dense operating dashboards
- Formality: high
- Density: medium
- Scheme: dark or light

## Signatures

1. Deep navy fields frame a clear aqua evidence accent.
2. Coral is reserved for a change, exception, or comparison counterpart.
3. Rounded modules create a composed service-oriented hierarchy.

## CSS

```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&family=Source+Serif+4:wght@500;600;700&display=swap');

html[data-theme="ocean-deep"] {
  --color-bg-primary: #F6F9FC; --color-bg-secondary: #E8F0F8; --color-bg-surface: #FFFFFF; --color-bg-elevated: #FFFFFF;
  --color-text-primary: #112240; --color-text-secondary: #3A5478; --color-text-muted: #66809E; --color-text-inverse: #F6F9FC;
  --color-accent: #0C7C8A; --color-accent-secondary: #E06854; --color-gold: #B9912B; --color-accent-hover: #096470; --color-accent-subtle: #D0F0F4;
  --color-border: color-mix(in srgb, var(--color-text-primary) 14%, transparent);
  --font-heading: 'Source Serif 4', Georgia, serif; --font-body: 'Instrument Sans', Arial, sans-serif; --font-mono: ui-monospace, Consolas, monospace;
  --radius-sm: clamp(0.25rem, 0.5vw, 0.4rem); --radius-md: clamp(0.45rem, 0.8vw, 0.7rem); --radius-lg: clamp(0.65rem, 1.1vw, 1rem);
  --preset-title-size: clamp(1.9rem, 4.2vw, 3.7rem); --preset-section-size: clamp(1.47rem, 3.15vw, 2.62rem); --preset-kicker-tracking: 0.13em; --preset-divider-width: 2px; --preset-stat-treatment: tabular-nums;
}
html[data-theme="ocean-deep"][data-mode="dark"] {
  --color-bg-primary: #091728; --color-bg-secondary: #10233A; --color-bg-surface: #17324D; --color-bg-elevated: #20405F;
  --color-text-primary: #E5F0F9; --color-text-secondary: #ABC5DC; --color-text-muted: #6E91B2; --color-text-inverse: #091728;
  --color-accent: #38C4C9; --color-accent-secondary: #F08070; --color-gold: #D5B650; --color-accent-hover: #74E0E2; --color-accent-subtle: #123B45;
}
```
