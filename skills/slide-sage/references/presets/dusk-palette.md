# Dusk Palette

- Mood: expressive
- Tone: reflective, creative
- Best for: product design, narrative research, concept proposals
- Avoid for: incident response and dense operational dashboards
- Formality: medium
- Density: low
- Scheme: light or dark

## Signatures

1. Soft rounded cards carry comparison and quote content.
2. A muted secondary tint creates section changes without gradients.
3. Display headings use generous line breaks and restrained labels.

## CSS

```css
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&display=swap');

html[data-theme="dusk-palette"] {
  --color-bg-primary: #FBF8FA; --color-bg-secondary: #F2ECF0; --color-bg-surface: #FFFFFF; --color-bg-elevated: #FFFFFF;
  --color-text-primary: #2C1F2A; --color-text-secondary: #664E62; --color-text-muted: #92768B; --color-text-inverse: #FBF8FA;
  --color-accent: #8B3A8B; --color-accent-secondary: #D4567A; --color-gold: #B98A2B; --color-accent-hover: #703070; --color-accent-subtle: #F0D8F0;
  --color-border: color-mix(in srgb, var(--color-text-primary) 13%, transparent);
  --font-heading: 'Fraunces', Georgia, serif; --font-body: 'DM Sans', Arial, sans-serif; --font-mono: ui-monospace, Consolas, monospace;
  --radius-sm: clamp(0.35rem, 0.6vw, 0.55rem); --radius-md: clamp(0.6rem, 1vw, 0.9rem); --radius-lg: clamp(0.9rem, 1.4vw, 1.3rem);
  --preset-title-size: clamp(1.95rem, 4.3vw, 3.8rem); --preset-section-size: clamp(1.5rem, 3.2vw, 2.7rem); --preset-kicker-tracking: 0.13em; --preset-divider-width: 0; --preset-stat-treatment: normal;
}
html[data-theme="dusk-palette"][data-mode="dark"] {
  --color-bg-primary: #1A1218; --color-bg-secondary: #251A23; --color-bg-surface: #30232E; --color-bg-elevated: #3D2D3A;
  --color-text-primary: #F2E5EF; --color-text-secondary: #CDB0C6; --color-text-muted: #8F7288; --color-text-inverse: #1A1218;
  --color-accent: #C074C0; --color-accent-secondary: #E47898; --color-gold: #D6A340; --color-accent-hover: #D99AD9; --color-accent-subtle: #351D34;
}
```
