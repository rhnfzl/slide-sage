# Monochrome Pro

- Mood: restrained
- Tone: executive, direct
- Best for: board updates, decisions, formal summaries
- Avoid for: playful teaching and high-energy product launches
- Formality: high
- Density: low
- Scheme: light or dark

## Signatures

1. Thin rules and generous whitespace replace decorative containers.
2. One cyan accent marks active evidence or the decision point.
3. Mono labels are sparse and functional.

## CSS

```css
@import url('https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,500;6..72,600;6..72,700&family=Work+Sans:wght@400;500;600;700&display=swap');

html[data-theme="monochrome-pro"] {
  --color-bg-primary: #FAFAF8; --color-bg-secondary: #F0F0ED; --color-bg-surface: #FFFFFF; --color-bg-elevated: #FFFFFF;
  --color-text-primary: #171717; --color-text-secondary: #525252; --color-text-muted: #7C7C78; --color-text-inverse: #FAFAF8;
  --color-accent: #0077BB; --color-accent-secondary: #009988; --color-gold: #BBAA33; --color-accent-hover: #005F96; --color-accent-subtle: #D4E8F7;
  --color-border: color-mix(in srgb, var(--color-text-primary) 16%, transparent);
  --font-heading: 'Newsreader', Georgia, serif; --font-body: 'Work Sans', Arial, sans-serif; --font-mono: ui-monospace, Consolas, monospace;
  --radius-sm: 0; --radius-md: 0; --radius-lg: 0;
  --preset-title-size: clamp(1.85rem, 4.1vw, 3.6rem); --preset-section-size: clamp(1.45rem, 3.1vw, 2.6rem); --preset-kicker-tracking: 0.17em; --preset-divider-width: 1px; --preset-stat-treatment: tabular-nums;
}
html[data-theme="monochrome-pro"][data-mode="dark"] {
  --color-bg-primary: #101010; --color-bg-secondary: #181818; --color-bg-surface: #202020; --color-bg-elevated: #292929;
  --color-text-primary: #F2F2EF; --color-text-secondary: #C8C8C2; --color-text-muted: #85857E; --color-text-inverse: #101010;
  --color-accent: #38C8D8; --color-accent-secondary: #52B99A; --color-gold: #D0BC54; --color-accent-hover: #78E1E9; --color-accent-subtle: #12323A;
}
```
