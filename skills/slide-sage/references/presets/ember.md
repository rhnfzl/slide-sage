# Ember

- Mood: decisive
- Tone: warm, urgent
- Best for: operating reviews, delivery metrics, action-oriented updates
- Avoid for: dense reference manuals and long teaching decks
- Formality: medium
- Density: high
- Scheme: dark or light

## Signatures

1. Oversized tabular numerals lead KPI slides.
2. Warm accent rules divide decision blocks.
3. Compact cards carry only one metric or action each.

## CSS

```css
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;600;700;800&display=swap');

html[data-theme="ember"] {
  --color-bg-primary: #FBF8F4; --color-bg-secondary: #F4EDE4; --color-bg-surface: #FFFFFF; --color-bg-elevated: #FFFFFF;
  --color-text-primary: #2C2218; --color-text-secondary: #6B5740; --color-text-muted: #927C65; --color-text-inverse: #FBF8F4;
  --color-accent: #CC6B20; --color-accent-secondary: #009988; --color-gold: #B47D0A; --color-accent-hover: #A95112; --color-accent-subtle: #FDE4CA;
  --color-border: color-mix(in srgb, var(--color-text-primary) 15%, transparent);
  --font-heading: 'Manrope', Arial, sans-serif; --font-body: 'Manrope', Arial, sans-serif; --font-mono: 'DM Mono', ui-monospace, monospace;
  --radius-sm: clamp(0.2rem, 0.4vw, 0.35rem); --radius-md: clamp(0.35rem, 0.65vw, 0.55rem); --radius-lg: clamp(0.45rem, 0.8vw, 0.7rem);
  --preset-title-size: clamp(1.98rem, 4.4vw, 3.85rem); --preset-section-size: clamp(1.54rem, 3.3vw, 2.75rem); --preset-kicker-tracking: 0.18em; --preset-divider-width: 3px; --preset-stat-treatment: tabular-nums;
}
html[data-theme="ember"][data-mode="dark"] {
  --color-bg-primary: #1A1410; --color-bg-secondary: #241C15; --color-bg-surface: #2E231A; --color-bg-elevated: #3A2C20;
  --color-text-primary: #F5E9D8; --color-text-secondary: #D0B99C; --color-text-muted: #927B63; --color-text-inverse: #1A1410;
  --color-accent: #E89838; --color-accent-secondary: #43B7A7; --color-gold: #D4A01A; --color-accent-hover: #F4B967; --color-accent-subtle: #3F2A17;
}
```
