# CSS Class Inventory

Authoritative list of every CSS class available in slide-sage presentations. When generating HTML, you may ONLY use classes from this inventory or classes you explicitly define in the presentation's `<style>` block.

**Using a class not in this list and not defined in `<style>`? That is a bug.**

---

## viewport-base.css Classes (Always Available)

| Class | Purpose | Element |
|-------|---------|---------|
| `.slide` | Full-viewport slide container (100vh, overflow: hidden) | `<div>` |
| `.slide.active` | Currently visible slide (opacity: 1, z-index: 1) | modifier |
| `.slide.inactive` | Hidden slide (opacity: 0, pointer-events: none) | modifier |
| `.slide-content` | Content wrapper (max-width: 90%, max-height: 85vh) | `<div>` |
| `.text-center` | Center-align text | any |
| `.flex-row` | Horizontal flex layout | container |
| `.flex-col` | Vertical flex layout | container |
| `.gap-sm` | Small gap (`var(--spacing-sm)`) | flex/grid |
| `.gap-md` | Medium gap (`var(--spacing-md)`) | flex/grid |
| `.gap-lg` | Large gap (`var(--spacing-lg)`) | flex/grid |
| `.grid-2` | 2-column grid | container |
| `.grid-3` | 3-column grid | container |
| `.progress-bar` | Fixed bottom progress bar | `<div>` |
| `.progress-fill` | Progress bar fill element | `<div>` |
| `.slide-counter` | Bottom-right slide number (e.g., "3 / 12") | `<div>` |
| `.nav-arrows` | Arrow navigation container | `<div>` |
| `.nav-arrow` | Individual prev/next button | `<button>` |
| `.nav-arrow:disabled` | Disabled state at start/end | modifier |
| `.visually-hidden` | Screen-reader-only content, including chart data tables | any |
| `.chart-render-fallback` | Visible chart data table until the chart initializes | `<div>` |
| `.shortcuts-overlay` | Modal keyboard-shortcuts backdrop | `<div>` |
| `.shortcuts-panel` | Keyboard-shortcuts dialog content | `<div>` |
| `.shortcuts-heading-row` | Dialog title and close-button row | `<div>` |
| `.shortcuts-close` | Keyboard-shortcuts close control | `<button>` |
| `.shortcuts-dismiss` | Dialog dismissal guidance | `<p>` |
| `.caption` | Small caption text (0.7-0.9rem, opacity: 0.7) | `<small>`, `<figcaption>` |
| `.eyebrow`, `.kicker` | Preset-aware mono label with preset tracking | `<span>` |
| `.accent-rule`, `.presentation-divider` | Preset-aware accent divider | `<div>` |
| `.stat-value`, `.metric-value` | Preset-aware numeric treatment | `<span>`, `<strong>` |

## Viewport System Classes (From viewport-system.md)

| Class | Purpose | Element |
|-------|---------|---------|
| `.feature-grid` | Auto-fit grid for feature cards | container |
| `.card` | Surface card with padding and border | `<div>` |
| `.image-bg` | Full-bleed background image slide | `.slide` modifier |

## Animation Classes (From animation-guide.md)

| Class | Purpose | Element |
|-------|---------|---------|
| `.animate-in` | Base animation trigger (activated by JS on slide enter) | any content element |
| `.anim-minimal` | Minimal animation mode (body-level) | `<body>` |
| `.anim-balanced` | Balanced animation mode (body-level) | `<body>` |
| `.anim-dramatic` | Dramatic animation mode (body-level) | `<body>` |
| `.gradient-bg` | Animated gradient background | `.slide` modifier |
| `.digit-roller` | Counter animation container | `<span>` |
| `.digit` | Individual digit in roller | `<span>` |
| `.typed-cursor` | Blinking cursor for typing effect | `<span>` |
| `.chart-container` | Chart wrapper (responsive height) | `<div>` |
| `.code-block` | Code display block | `<div>`, `<pre>` |
| `.line` | Individual code line | `<div>` |
| `.line.highlighted` | Highlighted code line | modifier |
| `.chart-highlight` | Chart emphasis effect | `<div>` |
| `.chart-legend-item` | Chart legend entry | `<div>` |
| `.stat-number` | Statistic number display | `<span>` |
| `.title-slide` | Title slide variant | `.slide` modifier |
| `.title-slide .content` | Title slide content wrapper | `<div>` |

---

## Comparison Template Classes

Only available when using the corresponding template from `templates/comparison/`.

### Split View (`split-view.html`)

`.compare-heading`, `.compare-container`, `.compare-col`, `.col-a`, `.col-b`, `.compare-sub-heading`, `.compare-list`, `.vs-divider`

### Feature Matrix (`feature-matrix.html`)

`.matrix-heading`, `.matrix-wrapper`, `.feature-matrix`, `.feature-name-col`, `.feature-label`, `.highlight-header`, `.highlight-col`, `.badge`, `.feature-name`

Data attributes: `td[data-check="yes"]`, `td[data-check="no"]`, `td[data-check="partial"]`

### Three-Column Comparison (`three-column-comparison.html`)

`.tri-compare-heading`, `.tri-compare-container`, `.tri-col`, `.tri-col-a`, `.tri-col-b`, `.tri-col-c`, `.tri-col-heading`, `.tri-col-list`

### KPI Dashboard (`kpi-dashboard.html`)

`.kpi-heading`, `.kpi-container`, `.kpi-card`, `.kpi-value`, `.kpi-label`, `.kpi-trend`, `.trend-arrow`, `.trend-text`, `.trend-up`, `.trend-down`, `.trend-neutral`

### Process Steps (`process-steps.html`)

`.process-heading`, `.process-container`, `.process-step`, `.step-connector`, `.step-circle`, `.step-number`, `.step-check`, `.step-title`, `.step-desc`, `.step-completed`, `.step-active`, `.step-upcoming`

### Horizontal Timeline (`timeline-horizontal.html`)

`.timeline-heading`, `.timeline-container`, `.timeline-track`, `.timeline-milestones`, `.milestone`, `.milestone-dot`, `.milestone-content`, `.milestone-label`, `.milestone-desc`

---

## Manual Syntax Highlighting Classes (From code-highlighting.md)

For domain-specific pseudo-code that Prism.js cannot tokenize (HTTP endpoints, file trees, data flows).

| Class | Purpose | Element |
|-------|---------|---------|
| `.syn-kw` | Keyword highlighting | `<span>` |
| `.syn-fn` | Function name | `<span>` |
| `.syn-str` | String literal | `<span>` |
| `.syn-num` | Number | `<span>` |
| `.syn-cm` | Comment (italic) | `<span>` |
| `.syn-method` | Method/builtin name | `<span>` |
| `.syn-verb` | HTTP verb (bold green) | `<span>` |
| `.syn-path` | File path or URL | `<span>` |
| `.syn-param` | Parameter name | `<span>` |

---

## Need a Class Not Listed Here?

**Define it in `<style>` FIRST, then use it in HTML.** Always use theme variables.

```css
/* In the presentation's <style> block */
.section-header {
    font-family: var(--font-mono);
    font-size: clamp(0.7rem, 1.1vw, 0.9rem);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--color-accent);
    border-bottom: 2px solid var(--color-accent);
    padding-bottom: var(--spacing-xs);
    margin-bottom: var(--spacing-md);
}
```

```html
<!-- Then in HTML -->
<span class="section-header">Architecture Overview</span>
```

### Rules for Custom Classes

1. **Define before use** - The class must exist in `<style>` before any HTML references it
2. **Use theme variables** - `var(--color-accent)` not `#3366cc`, `var(--spacing-md)` not `1.25rem`
3. **Use `clamp()` for sizing** - Never fixed px/rem for font-size or spacing
4. **Use modifier pattern for variants** - `.card.highlight` not `.card-highlight` and `.highlighted-card`

**Never use a class without defining it. Never use inline styles for something that appears on 2+ elements.**
