# Jade Circuit

- Mood: technical
- Tone: composed, systems-led
- Best for: engineering architecture, implementation walkthroughs, platform reviews
- Avoid for: soft editorial story and consumer marketing
- Formality: medium
- Density: medium
- Scheme: dark or light

## Signatures

1. Mono labels tag layers, boundaries, and protocol edges.
2. Square-cornered surfaces make a diagram read like a system map.
3. Gold marks the one critical path or exception.

## CSS

```css
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;600;700&display=swap');

html[data-theme="jade-circuit"] {
  --color-bg-primary: #F5F8F5; --color-bg-secondary: #E8EFE8; --color-bg-surface: #FFFFFF; --color-bg-elevated: #FFFFFF;
  --color-text-primary: #1B2B1E; --color-text-secondary: #3E5E44; --color-text-muted: #6B8770; --color-text-inverse: #F5F8F5;
  --color-accent: #1D8348; --color-accent-secondary: #0077BB; --color-gold: #A78310; --color-accent-hover: #16663A; --color-accent-subtle: #D4EDDD;
  --color-border: color-mix(in srgb, var(--color-text-primary) 15%, transparent);
  --font-heading: 'IBM Plex Sans', Arial, sans-serif; --font-body: 'IBM Plex Sans', Arial, sans-serif; --font-mono: 'IBM Plex Mono', ui-monospace, monospace;
  --radius-sm: 0; --radius-md: clamp(0.1rem, 0.2vw, 0.2rem); --radius-lg: clamp(0.2rem, 0.4vw, 0.35rem);
  --preset-title-size: clamp(1.8rem, 4vw, 3.5rem); --preset-section-size: clamp(1.4rem, 3vw, 2.5rem); --preset-kicker-tracking: 0.12em; --preset-divider-width: 1px; --preset-stat-treatment: tabular-nums;
}
html[data-theme="jade-circuit"][data-mode="dark"] {
  --color-bg-primary: #0E1A12; --color-bg-secondary: #14231A; --color-bg-surface: #1A2E22; --color-bg-elevated: #20382A;
  --color-text-primary: #DFF0E4; --color-text-secondary: #A7C9B0; --color-text-muted: #668B70; --color-text-inverse: #0E1A12;
  --color-accent: #48BC78; --color-accent-secondary: #4AA3D8; --color-gold: #D4B02A; --color-accent-hover: #78D69B; --color-accent-subtle: #173522;
}
```
