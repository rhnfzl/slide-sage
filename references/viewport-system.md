# Viewport System Reference

Responsive CSS system for slide presentations that guarantees no scrolling, no overflow, and consistent rendering across screen sizes.

## Core Rule

Every slide must fill exactly one viewport height and never scroll:

```css
.slide {
  height: 100vh;
  height: 100dvh; /* dynamic viewport height — accounts for mobile browser chrome */
  overflow: hidden;
}
```

The `overflow: hidden` is non-negotiable. If content does not fit, split into multiple slides. Never add scrolling to a slide.

## Typography Scale

All text sizes use `clamp()` for fluid scaling between mobile and large displays:

```css
h1 { font-size: clamp(1.8rem, 4vw, 3.5rem); }
h2 { font-size: clamp(1.4rem, 3vw, 2.5rem); }
h3 { font-size: clamp(1.1rem, 2.2vw, 1.8rem); }

/* Body text — paragraphs, list items */
p, li { font-size: clamp(0.85rem, 1.5vw, 1.2rem); }

/* Small text — captions, footnotes, labels */
small, .caption, figcaption { font-size: clamp(0.7rem, 1.1vw, 0.9rem); }
```

Line heights:
- Headings: `line-height: 1.2`
- Body text: `line-height: 1.5`
- Small text: `line-height: 1.4`

## Spacing Scale

CSS custom properties with `clamp()` for responsive spacing:

```css
:root {
  --spacing-xs: clamp(0.25rem, 0.5vw, 0.5rem);
  --spacing-sm: clamp(0.5rem, 1vw, 0.75rem);
  --spacing-md: clamp(0.75rem, 1.5vw, 1.25rem);
  --spacing-lg: clamp(1rem, 2.5vw, 2rem);
  --spacing-xl: clamp(1.5rem, 3.5vw, 3rem);
}
```

Usage: Apply spacing to padding, margin, and gap properties. Never use fixed pixel values for layout spacing in slides.

## Content Density Limits

These are hard limits. If content exceeds these, split into multiple slides.

| Slide Type | Maximum Content |
|---|---|
| Title | 1 heading + 1 subtitle + optional tagline |
| Content | 1 heading + 4-6 bullet points OR 2 paragraphs |
| Feature grid | 1 heading + max 6 cards (2x3 or 3x2) |
| Code | 1 heading + 10-12 lines of code |
| Chart | 1 heading + 1 chart (max 55vh) + optional caption |
| Quote | 1 quote (max 3 lines) + attribution |
| Image | 1 heading + 1 image (max-height: min(50vh, 400px)) + optional caption |
| Comparison | 1 heading + 2 columns |

### Split Rule

Content exceeds limits? Split into multiple slides. Never add scrolling. Examples:
- 8 bullet points -> split into two slides of 4
- 20 lines of code -> split into two code slides
- 2 charts -> one chart per slide

## Image Sizing

Images must never overflow the slide. Use these constraints:

```css
.slide img {
  max-height: min(50vh, 400px);
  max-width: 100%;
  width: auto;
  height: auto;
  object-fit: contain;
}
```

For full-bleed background images:

```css
.slide.image-bg {
  background-size: cover;
  background-position: center;
}
```

## Height Breakpoints

Short viewports (laptops, split-screen) require progressive reduction:

### @media (max-height: 700px)

```css
@media (max-height: 700px) {
  h1 { font-size: clamp(1.5rem, 3.5vw, 2.8rem); }
  h2 { font-size: clamp(1.2rem, 2.5vw, 2rem); }
  h3 { font-size: clamp(1rem, 2vw, 1.5rem); }
  p, li { font-size: clamp(0.8rem, 1.3vw, 1.05rem); }

  .slide { padding: var(--spacing-sm) var(--spacing-md); }
  .slide-content { max-height: 88vh; }

  /* Tighter spacing */
  :root {
    --spacing-md: clamp(0.5rem, 1.2vw, 1rem);
    --spacing-lg: clamp(0.75rem, 2vw, 1.5rem);
    --spacing-xl: clamp(1rem, 2.5vw, 2rem);
  }
}
```

### @media (max-height: 600px)

```css
@media (max-height: 600px) {
  h1 { font-size: clamp(1.3rem, 3vw, 2.2rem); }
  h2 { font-size: clamp(1.1rem, 2.2vw, 1.7rem); }
  h3 { font-size: clamp(0.95rem, 1.8vw, 1.3rem); }
  p, li { font-size: clamp(0.75rem, 1.2vw, 0.95rem); }
  small, .caption { font-size: clamp(0.65rem, 1vw, 0.8rem); }

  .slide { padding: var(--spacing-xs) var(--spacing-sm); }
  .slide-content { max-height: 90vh; }

  /* Reduce image sizes */
  .slide img { max-height: min(40vh, 300px); }
}
```

### @media (max-height: 500px) -- Emergency Compact Mode

```css
@media (max-height: 500px) {
  h1 { font-size: clamp(1.1rem, 2.5vw, 1.8rem); }
  h2 { font-size: clamp(0.95rem, 2vw, 1.4rem); }
  h3 { font-size: clamp(0.85rem, 1.6vw, 1.1rem); }
  p, li { font-size: clamp(0.7rem, 1.1vw, 0.85rem); }

  .slide {
    padding: var(--spacing-xs);
    gap: var(--spacing-xs);
  }
  .slide-content { max-height: 92vh; }

  /* Aggressively reduce vertical space */
  h1, h2, h3 { margin-bottom: var(--spacing-xs); }
  ul, ol { gap: 0.1rem; }
  .slide img { max-height: min(30vh, 200px); }
}
```

## Container Max-Height Patterns

For flex layouts where children must fit within the viewport:

```css
.slide-content {
  display: flex;
  flex-direction: column;
  max-width: min(90%, 1100px);
  max-height: 85vh;
  overflow: hidden;
}

/* Grid cards — cap individual card height */
.feature-grid {
  display: grid;
  gap: var(--spacing-md);
  max-height: 65vh;
}

.feature-grid .card {
  overflow: hidden;
  min-height: 0; /* allow flex shrink */
}

/* Chart containers */
.chart-container {
  max-height: 55vh;
  width: 100%;
  position: relative;
}

/* Code blocks */
.code-block {
  max-height: 55vh;
  overflow: hidden;
  font-size: clamp(0.7rem, 1.2vw, 0.95rem);
}
```

## CSS Layout — Viewport Filling Rules

Hard rules for making slide content fill the viewport correctly. These prevent the most common layout bugs in scroll-snap presentations.

### Rule 1: Never `flex: 1` on Bordered Elements

**NEVER** apply `flex: 1` (or any flex-grow) to elements with visible borders, backgrounds, or outlines:

- `.card`, `.code-block`, `table`, `.callout`, `.badge`
- Any element with `border`, `background`, or `box-shadow`

These elements have intrinsic content sizes. Growing them creates huge empty bordered areas — the border stretches to fill the viewport while the content stays small inside.

**Only apply `flex: 1` to borderless layout containers:** `.grid-2`, `.grid-3`, `.flex-row`, `.flex-col`, `.diagram-container`, plain wrapper `<div>` elements.

### Rule 2: Always `min-height: 0` on Flex Children

Flex items default to `min-height: auto` (not `0`). This means a flex child will never shrink below its intrinsic content size, even with `flex: 1`. If `.slide-content` contains a large element (code block, table, image), the slide overflows instead of constraining.

**Always pair `flex: 1` with `min-height: 0`:**

```css
.slide-content > .grid-2,
.slide-content > .diagram-container {
  flex: 1;
  min-height: 0; /* CRITICAL — allows shrinking below content size */
}
```

### Rule 3: `align-content: center` + `align-items: start` on Grids

When a CSS Grid container gets `flex: 1` to fill available space:

- Add `align-content: center` — centers the group of rows within the expanded grid
- Add `align-items: start` — prevents individual grid items (cards) from stretching to fill row height
- Without `align-items: start`, cards stretch their borders to match the tallest possible row

```css
.slide-content > .grid-2 {
  flex: 1;
  min-height: 0;
  align-content: center;
  align-items: start;
}
```

### Rule 4: Trace CSS Selectors Through Real HTML

Before writing any CSS rule that uses `:has()`, `:not()`, or complex descendant selectors:

1. Pick 3-4 actual slides from the presentation
2. Manually walk through the HTML: "Does `.reveal.card.card-accent` on slide 5 match this selector? Yes/No — What happens?"
3. Check for elements with **multiple classes** (e.g., `class="reveal card card-accent"` matches BOTH `.reveal` and `.card` rules)
4. Only commit the CSS after all traces pass

### Rule 5: One Layout Change, Then Verify

For visual/CSS layout changes:

- Make ONE targeted change
- Verify in browser
- Then proceed to the next change

Do NOT stack multiple speculative layout changes. Layout interactions are hard to predict from code alone.

### Rule 6: Research Before CSS Implementation

For layout problems (viewport filling, spacing, responsive sizing):

- Search for proven patterns FIRST (flexbox centering, grid alignment)
- Then implement the researched approach
- Do not guess-and-iterate on CSS layout

### Proven Pattern: Viewport-Filling Slide Content

```css
/* Base: center content vertically */
.slide-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  overflow: hidden;
}

/* Borderless layout containers grow to fill space */
.slide-content > .grid-2,
.slide-content > .grid-3,
.slide-content > .diagram-container {
  flex: 1;
  min-height: 0;
}

/* Grids: center rows, don't stretch items */
.slide-content > .grid-2,
.slide-content > .grid-3 {
  align-content: center;
  align-items: start;
}

/* .animate-in wrappers grow only if they contain expandable layouts */
.slide-content > .animate-in:not(.card):not(.code-block):has(
  .grid-2, .grid-3, .diagram-container
) {
  flex: 1;
  min-height: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
```

**Key: `:has()` selector must NEVER include `.card`, `.code-block`, or `table`** — these cause the wrapper to grow, which then stretches the bordered child.

---

## CSS Function Warning

**NEVER negate a CSS `clamp()`, `min()`, or `max()` function directly.** This is invalid CSS:

```css
/* WRONG -- this does not work */
margin-top: -clamp(1rem, 2vw, 2rem);
```

Instead, wrap in `calc()` with `-1` multiplication:

```css
/* CORRECT */
margin-top: calc(-1 * clamp(1rem, 2vw, 2rem));
```

This applies to all CSS math functions: `clamp()`, `min()`, `max()`, `calc()` nesting.

## Width Breakpoints (Secondary)

Width breakpoints handle narrow devices. Height breakpoints take priority for presentations.

```css
/* Tablet and below */
@media (max-width: 768px) {
  .grid-2, .grid-3 { grid-template-columns: 1fr; }
  .flex-row { flex-direction: column; }
}

/* Mobile */
@media (max-width: 480px) {
  .slide { padding: var(--spacing-sm); }
  .nav-arrows { display: none; }
}
```

## Checklist Before Generating Slides

1. Every `.slide` has `overflow: hidden`
2. No slide exceeds the content density limit for its type
3. All font sizes use `clamp()`
4. All spacing uses CSS custom properties with `clamp()`
5. Images have `max-height` constraints
6. Height breakpoints are included
7. CSS function negation uses `calc(-1 * ...)`
8. If content overflows, split -- never scroll
