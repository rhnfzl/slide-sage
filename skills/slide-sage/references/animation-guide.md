# Slide-Sage Animation Guide

Three intensity levels with copy-paste-ready code. All animations respect `prefers-reduced-motion`.

---

## Global Setup

### Animation Level Control

```js
// Set animation level on document root
// Values: 'minimal', 'balanced', 'dramatic'
document.documentElement.dataset.animLevel = 'balanced';
```

### Reduced Motion Safety (MANDATORY)

This must be included in EVERY presentation. It overrides all animation levels.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

### Base CSS Classes

```css
/* Animation level containers */
.anim-minimal .slide * { animation: none !important; transition: opacity 0.15s ease; }
.anim-balanced .slide * { /* uses balanced keyframes below */ }
.anim-dramatic .slide * { /* uses dramatic keyframes below */ }

/* Hide animated elements before slide enters (balanced + dramatic only) */
[data-anim-level="balanced"] .animate-in,
[data-anim-level="dramatic"] .animate-in {
  opacity: 0;
}

/* Show all immediately in minimal mode */
[data-anim-level="minimal"] .animate-in {
  opacity: 1 !important;
}
```

---

## Level 1: Minimal

Default for technical audiences. Content appears instantly. No distractions.

### Slide Transitions

```css
/* Option A: Instant cut (true zero animation) */
.anim-minimal .slide {
  display: none;
}
.anim-minimal .slide.active {
  display: block;
}

/* Option B: Simple opacity fade (150ms) */
.anim-minimal .slide {
  opacity: 0;
  position: absolute;
  inset: 0;
  transition: opacity 0.15s ease;
  pointer-events: none;
}
.anim-minimal .slide.active {
  opacity: 1;
  position: relative;
  pointer-events: auto;
}
```

### Content Entrance

```css
/* All content visible immediately on slide enter */
.anim-minimal .slide.active .animate-in {
  opacity: 1;
  transform: none;
}
```

### Chart Animation

```js
// Chart.js config for minimal mode
const minimalChartOptions = {
  animation: false,       // No animation at all
  transitions: {
    active: { animation: { duration: 0 } }
  },
  hover: { animationDuration: 0 },
  responsiveAnimationDuration: 0
};
```

### Numbers

```css
/* Static display - no counting effect */
.anim-minimal .stat-number {
  /* Number is just rendered as-is in the HTML */
}
```

### Hover Effects

```css
.anim-minimal .card:hover,
.anim-minimal .chart-legend-item:hover {
  opacity: 1;
  transition: opacity 0.15s ease;
}

.anim-minimal .card,
.anim-minimal .chart-legend-item {
  opacity: 0.85;
  transition: opacity 0.15s ease;
}

.anim-minimal a:hover,
.anim-minimal .interactive:hover {
  color: var(--color-accent-hover);
  transition: color 0.15s ease;
}
```

---

## Level 2: Balanced

Professional polish without excess. Smooth entrances that guide the eye.

### Slide Transitions

```css
/* Slide transition: translateX or opacity fade, 300ms */
.anim-balanced .slide {
  opacity: 0;
  transform: translateX(30px);
  position: absolute;
  inset: 0;
  transition: opacity 0.3s ease-out, transform 0.3s ease-out;
  pointer-events: none;
}
.anim-balanced .slide.active {
  opacity: 1;
  transform: translateX(0);
  position: relative;
  pointer-events: auto;
}

/* Alternative: pure fade */
.anim-balanced.fade-only .slide {
  transform: none;
  transition: opacity 0.3s ease-out;
}
```

### Content Entrance (Staggered Fade-In-Up)

```css
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.anim-balanced .slide.active .animate-in {
  animation: fadeInUp 0.5s ease forwards;
}

/* Stagger children */
.anim-balanced .slide.active .animate-in:nth-child(1) { animation-delay: 0s; }
.anim-balanced .slide.active .animate-in:nth-child(2) { animation-delay: 0.1s; }
.anim-balanced .slide.active .animate-in:nth-child(3) { animation-delay: 0.2s; }
.anim-balanced .slide.active .animate-in:nth-child(4) { animation-delay: 0.3s; }
.anim-balanced .slide.active .animate-in:nth-child(5) { animation-delay: 0.4s; }
.anim-balanced .slide.active .animate-in:nth-child(6) { animation-delay: 0.5s; }
.anim-balanced .slide.active .animate-in:nth-child(7) { animation-delay: 0.6s; }
.anim-balanced .slide.active .animate-in:nth-child(8) { animation-delay: 0.7s; }

/* Generic stagger helper using CSS custom property */
.anim-balanced .slide.active .animate-in {
  animation-delay: calc(var(--stagger-index, 0) * 0.1s);
}
```

### Chart Animation

```js
// Apply this on slidechange after the chart was initialized with animation: false.
const balancedChartOptions = {
  animation: {
    duration: 800,
    easing: 'easeOutQuart'
  },
  transitions: {
    active: {
      animation: { duration: 200 }
    }
  }
};
```

### Number Counter (CountUp.js)

```html
<!-- CDN -->
<script src="https://cdn.jsdelivr.net/npm/countup.js@2.8.0/dist/countUp.umd.min.js" integrity="sha384-BqV2KvVZRFB68l6NJ8nNRT9pasWg2JUfbs8tBkuQm+KafN2y+nWPg+wPMaAm5CYl" crossorigin="anonymous"></script>
```

```js
// Initialize CountUp for balanced mode
function initCountUp(elementId, endValue, options = {}) {
  const defaults = {
    duration: 1.5,
    useEasing: true,
    useGrouping: true,
    separator: ',',
    decimal: '.',
  };
  const merged = { ...defaults, ...options };
  const counter = new countUp.CountUp(elementId, endValue, merged);
  if (!counter.error) {
    counter.start();
  }
  return counter;
}

// Usage
// <span id="stat-revenue">0</span>
// initCountUp('stat-revenue', 1250000, { prefix: '$' });
// initCountUp('stat-growth', 23.5, { decimalPlaces: 1, suffix: '%' });
```

### Hover Effects

```css
.anim-balanced .card {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.anim-balanced .card:hover {
  transform: scale(1.02);
  box-shadow: var(--shadow-lg);
}

.anim-balanced .chart-legend-item {
  transition: opacity 0.2s ease, transform 0.2s ease;
}
.anim-balanced .chart-legend-item:hover {
  opacity: 1;
  transform: translateX(4px);
}
```

### Code Block Line Highlight

```css
.anim-balanced .code-block .line {
  transition: background-color 0.3s ease;
}
.anim-balanced .code-block .line.highlighted {
  background-color: var(--color-accent-subtle);
}
.anim-balanced .code-block .line:not(.highlighted) {
  opacity: 0.5;
}
```

```js
// Highlight specific lines on focus/scroll
function highlightCodeLines(blockEl, lineNumbers) {
  const lines = blockEl.querySelectorAll('.line');
  lines.forEach((line, i) => {
    line.classList.toggle('highlighted', lineNumbers.includes(i + 1));
  });
}
```

---

## Level 3: Dramatic

High-energy presentations. Conference keynotes, pitch decks, storytelling.

### Slide Transitions (3D Perspective)

```css
.anim-dramatic .slide-container {
  perspective: 1200px;
  overflow: hidden;
}

/* Option A: 3D rotateY */
@keyframes slideIn3D {
  from {
    opacity: 0;
    transform: rotateY(-15deg) translateX(80px) scale(0.95);
  }
  to {
    opacity: 1;
    transform: rotateY(0) translateX(0) scale(1);
  }
}

.anim-dramatic .slide {
  opacity: 0;
  position: absolute;
  inset: 0;
  pointer-events: none;
}
.anim-dramatic .slide.active {
  animation: slideIn3D 0.5s cubic-bezier(0.22, 1, 0.36, 1) forwards;
  position: relative;
  pointer-events: auto;
}

/* Option B: Scale-up fade */
@keyframes scaleUpFade {
  from {
    opacity: 0;
    transform: scale(0.92);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.anim-dramatic.scale-mode .slide.active {
  animation: scaleUpFade 0.5s cubic-bezier(0.22, 1, 0.36, 1) forwards;
}
```

### Content Entrance (Spring Physics)

```css
@keyframes springIn {
  0% {
    opacity: 0;
    transform: translateY(40px) scale(0.95);
  }
  60% {
    opacity: 1;
    transform: translateY(-8px) scale(1.02);
  }
  80% {
    transform: translateY(3px) scale(0.995);
  }
  100% {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.anim-dramatic .slide.active .animate-in {
  animation: springIn 0.7s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
}

/* Stagger with longer delays for dramatic effect */
.anim-dramatic .slide.active .animate-in:nth-child(1) { animation-delay: 0s; }
.anim-dramatic .slide.active .animate-in:nth-child(2) { animation-delay: 0.12s; }
.anim-dramatic .slide.active .animate-in:nth-child(3) { animation-delay: 0.24s; }
.anim-dramatic .slide.active .animate-in:nth-child(4) { animation-delay: 0.36s; }
.anim-dramatic .slide.active .animate-in:nth-child(5) { animation-delay: 0.48s; }
.anim-dramatic .slide.active .animate-in:nth-child(6) { animation-delay: 0.60s; }
.anim-dramatic .slide.active .animate-in:nth-child(7) { animation-delay: 0.72s; }
.anim-dramatic .slide.active .animate-in:nth-child(8) { animation-delay: 0.84s; }

/* Generic stagger helper */
.anim-dramatic .slide.active .animate-in {
  animation-delay: calc(var(--stagger-index, 0) * 0.12s);
}
```

### Chart Animation (Sequential Draw)

```js
// Apply this on slidechange after the chart was initialized with animation: false.
// It creates a sequential dataset reveal for dramatic mode.
const dramaticChartOptions = {
  animation: {
    duration: 1200,
    easing: 'easeOutQuart',
    delay: (context) => {
      // Stagger by dataset index
      let delay = 0;
      if (context.type === 'data' && context.mode === 'default') {
        delay = context.datasetIndex * 400 + context.dataIndex * 50;
      }
      return delay;
    },
  },
  transitions: {
    active: {
      animation: { duration: 300 }
    }
  }
};

// For bar/line charts, prepare each dataset just before reset() and update().
function prepareDramaticChartForEntry(chart) {
  // Override per-dataset animation
  if (chart.data && chart.data.datasets) {
    chart.options.animation = dramaticChartOptions.animation;
    chart.data.datasets.forEach((ds, i) => {
      ds.animation = {
        delay: i * 500,
        duration: 1000,
        easing: 'easeOutQuart'
      };
    });
  }
  return chart;
}
```

### Number Counter (Dramatic with Decimal Scroll)

```html
<!-- CountUp.js CDN -->
<script src="https://cdn.jsdelivr.net/npm/countup.js@2.8.0/dist/countUp.umd.min.js" integrity="sha384-BqV2KvVZRFB68l6NJ8nNRT9pasWg2JUfbs8tBkuQm+KafN2y+nWPg+wPMaAm5CYl" crossorigin="anonymous"></script>
```

```js
// Dramatic CountUp - longer duration, started by slide entry
function initDramaticCountUp(elementId, endValue, options = {}) {
  const defaults = {
    duration: 2.5,
    useEasing: true,
    useGrouping: true,
    separator: ',',
    decimal: '.',
  };
  const merged = { ...defaults, ...options };
  const counter = new countUp.CountUp(elementId, endValue, merged);
  if (!counter.error) {
    counter.start();
  }
  return counter;
}

// Decimal scroll visual effect (CSS-driven digit roller)
// Usage: <span class="digit-roller" data-value="42.7"></span>
```

```css
/* Digit roller effect for dramatic numbers */
.digit-roller {
  display: inline-flex;
  overflow: hidden;
  height: 1.2em;
}
.digit-roller .digit {
  display: inline-block;
  animation: digitScroll 2.5s cubic-bezier(0.22, 1, 0.36, 1) forwards;
}
@keyframes digitScroll {
  0% { transform: translateY(100%); opacity: 0; }
  20% { opacity: 1; }
  100% { transform: translateY(0); opacity: 1; }
}
.digit-roller .digit:nth-child(1) { animation-delay: 0s; }
.digit-roller .digit:nth-child(2) { animation-delay: 0.08s; }
.digit-roller .digit:nth-child(3) { animation-delay: 0.16s; }
.digit-roller .digit:nth-child(4) { animation-delay: 0.24s; }
.digit-roller .digit:nth-child(5) { animation-delay: 0.32s; }
.digit-roller .digit:nth-child(6) { animation-delay: 0.40s; }
.digit-roller .digit:nth-child(7) { animation-delay: 0.48s; }
```

```js
// JS helper to split number into digit spans
function initDigitRoller(el) {
  const value = el.dataset.value;
  el.innerHTML = value.split('').map(
    (char, i) => `<span class="digit" style="animation-delay:${i * 0.08}s">${char}</span>`
  ).join('');
}
document.querySelectorAll('.digit-roller').forEach(initDigitRoller);
```

### Background Gradient Animation

```css
@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

.anim-dramatic .slide.gradient-bg {
  background: linear-gradient(
    135deg,
    var(--color-bg-primary),
    var(--color-accent-subtle),
    var(--color-bg-secondary),
    var(--color-accent-subtle)
  );
  background-size: 300% 300%;
  animation: gradientShift 12s ease infinite;
}
```

### Particle Background (q5.js)

```html
<!-- q5.js CDN (lightweight p5.js alternative) -->
<script src="https://cdn.jsdelivr.net/npm/q5@4.7.4/q5.js" integrity="sha384-ur7nimB9JM1iKrMbK3laywwS1x3TDbDAJ88FYeph7TJTSIN3tg27nGktp/CHHN1Y" crossorigin="anonymous"></script>
```

```js
// Subtle floating particles for dramatic title slides
function initParticles(canvasParent) {
  new Q5('global', canvasParent);

  const particles = [];
  const count = 40;

  function setup() {
    createCanvas(canvasParent.offsetWidth, canvasParent.offsetHeight);
    for (let i = 0; i < count; i++) {
      particles.push({
        x: random(width),
        y: random(height),
        size: random(2, 5),
        speedX: random(-0.3, 0.3),
        speedY: random(-0.2, -0.6),
        alpha: random(30, 80),
      });
    }
  }

  function draw() {
    clear();
    for (const p of particles) {
      fill(255, 255, 255, p.alpha);
      noStroke();
      ellipse(p.x, p.y, p.size);
      p.x += p.speedX;
      p.y += p.speedY;
      if (p.y < -10) { p.y = height + 10; p.x = random(width); }
      if (p.x < -10 || p.x > width + 10) { p.x = random(width); }
    }
  }

  window.setup = setup;
  window.draw = draw;
}

// Usage: initParticles(document.querySelector('.title-slide'));
```

```css
/* Particle canvas positioning */
.title-slide {
  position: relative;
}
.title-slide canvas {
  position: absolute;
  inset: 0;
  z-index: 0;
  pointer-events: none;
}
.title-slide .content {
  position: relative;
  z-index: 1;
}
```

### Typed.js Title Effect

```html
<!-- Typed.js CDN -->
<script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.16/dist/typed.umd.js" integrity="sha384-cMrTlShXEGSdSFA359p+3aVUxK/R+0TAfbRZMcTlAn8yqzxEDj05QsS65nTFMMj4" crossorigin="anonymous"></script>
```

```js
// Typing effect for dramatic title slides
function initTypedTitle(elementSelector, strings, options = {}) {
  const defaults = {
    strings: strings,
    typeSpeed: 40,
    backSpeed: 20,
    startDelay: 300,
    showCursor: true,
    cursorChar: '|',
    loop: false,
  };
  const merged = { ...defaults, ...options };
  return new Typed(elementSelector, merged);
}

// Usage:
// <h1 class="typed-title"></h1>
// initTypedTitle('.typed-title', ['Revenue grew 340% in Q3']);

// Multi-line typed effect
// initTypedTitle('.typed-title', [
//   'First line appears...',
//   'Then replaced by this.'
// ], { backDelay: 1500 });
```

```css
/* Typed.js cursor styling */
.typed-cursor {
  color: var(--color-accent);
  font-weight: 300;
  animation: typedBlink 0.7s infinite;
}
@keyframes typedBlink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}
```

### Hover Effects (Glow)

```css
.anim-dramatic .card {
  transition: transform 0.3s cubic-bezier(0.22, 1, 0.36, 1),
              box-shadow 0.3s ease,
              filter 0.3s ease;
}
.anim-dramatic .card:hover {
  transform: scale(1.04) translateY(-4px);
  box-shadow:
    var(--shadow-lg),
    0 0 20px color-mix(in srgb, var(--color-accent) 25%, transparent);
  filter: brightness(1.05);
}

/* Chart element glow on hover */
.anim-dramatic .chart-container canvas {
  transition: filter 0.3s ease;
}
.anim-dramatic .chart-highlight {
  filter: drop-shadow(0 0 8px var(--color-accent));
}
```

---

## Integration Patterns

### Slide Engine Hook

```js
// The canonical SlidePresentation class emits this event after each entry.
function onSlideEnter(slideEl, { reducedMotion = false } = {}) {
  const level = reducedMotion ? 'minimal' : (document.documentElement.dataset.animLevel || 'balanced');

  // Reset all animate-in elements
  const items = slideEl.querySelectorAll('.animate-in');
  items.forEach((el, i) => {
    el.style.setProperty('--stagger-index', i);
    if (level !== 'minimal') {
      // Force re-trigger animation by removing/re-adding class
      el.style.animation = 'none';
      el.offsetHeight; // trigger reflow
      el.style.animation = '';
    }
  });

  // Initialize counters on this slide
  slideEl.querySelectorAll('[data-countup]').forEach(el => {
    const value = parseFloat(el.dataset.countup);
    const opts = JSON.parse(el.dataset.countupOptions || '{}');

    if (level === 'minimal') {
      // Just display the number
      el.textContent = value.toLocaleString();
    } else if (level === 'dramatic') {
      el.textContent = '0';
      initDramaticCountUp(el.id, value, opts);
    } else {
      el.textContent = '0';
      initCountUp(el.id, value, opts);
    }
  });

  // Initialize typed.js on title slides (dramatic only)
  if (level === 'dramatic') {
    slideEl.querySelectorAll('[data-typed]').forEach(el => {
      const text = el.dataset.typed;
      el.textContent = '';
      initTypedTitle(el, [text]);
    });
  }
}

document.addEventListener('slidechange', ({ detail }) => {
  onSlideEnter(detail.slide, detail);
});
```

### Animation Level Switcher UI

```html
<!-- Optional: let presenter switch animation level -->
<div class="anim-switcher" style="position:fixed;bottom:8px;right:8px;z-index:9999;font-size:11px;">
  <button onclick="setAnimLevel('minimal')">Min</button>
  <button onclick="setAnimLevel('balanced')">Bal</button>
  <button onclick="setAnimLevel('dramatic')">Max</button>
</div>
```

```js
function setAnimLevel(level) {
  document.documentElement.dataset.animLevel = level;
  // Update body class for CSS selectors
  document.body.classList.remove('anim-minimal', 'anim-balanced', 'anim-dramatic');
  document.body.classList.add(`anim-${level}`);
}

// Auto-detect reduced motion preference
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  setAnimLevel('minimal');
}
```

### Chart.js Animation Config Helper

```js
// Returns the right Chart.js animation config for the current level
function getChartAnimationConfig(reducedMotion = false) {
  const level = reducedMotion ? 'minimal' : (document.documentElement.dataset.animLevel || 'balanced');

  switch (level) {
    case 'minimal':
      return {
        animation: false,
        transitions: { active: { animation: { duration: 0 } } },
        hover: { animationDuration: 0 },
        responsiveAnimationDuration: 0
      };

    case 'balanced':
      return {
        animation: {
          duration: 800,
          easing: 'easeOutQuart'
        },
        transitions: {
          active: { animation: { duration: 200 } }
        }
      };

    case 'dramatic':
      return {
        animation: {
          duration: 1200,
          easing: 'easeOutQuart',
          delay: (ctx) => {
            let delay = 0;
            if (ctx.type === 'data' && ctx.mode === 'default') {
              delay = ctx.datasetIndex * 400 + ctx.dataIndex * 50;
            }
            return delay;
          }
        },
        transitions: {
          active: { animation: { duration: 300 } }
        }
      };

    default:
      return { animation: false };
  }
}

// Create charts with animation: false. Apply this configuration from the
// slidechange listener immediately before chart.reset() and chart.update().
```

### CDN Reference Summary

```html
<!-- CountUp.js - number animation (balanced + dramatic) -->
<script src="https://cdn.jsdelivr.net/npm/countup.js@2.8.0/dist/countUp.umd.min.js" integrity="sha384-BqV2KvVZRFB68l6NJ8nNRT9pasWg2JUfbs8tBkuQm+KafN2y+nWPg+wPMaAm5CYl" crossorigin="anonymous"></script>

<!-- Typed.js - typing effect (dramatic only) -->
<script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.16/dist/typed.umd.js" integrity="sha384-cMrTlShXEGSdSFA359p+3aVUxK/R+0TAfbRZMcTlAn8yqzxEDj05QsS65nTFMMj4" crossorigin="anonymous"></script>

<!-- q5.js - particle effects (dramatic only) -->
<script src="https://cdn.jsdelivr.net/npm/q5@4.7.4/q5.js" integrity="sha384-ur7nimB9JM1iKrMbK3laywwS1x3TDbDAJ88FYeph7TJTSIN3tg27nGktp/CHHN1Y" crossorigin="anonymous"></script>

<!-- Chart.js - data visualization (all levels) -->
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js" integrity="sha384-vsrfeLOOY6KuIYKDlmVH5UiBmgIdB1oEf7p01YgWHuqmOHfZr374+odEv96n9tNC" crossorigin="anonymous"></script>
```

---

## Quick Reference Table

| Feature              | Minimal            | Balanced               | Dramatic                    |
|----------------------|--------------------|------------------------|-----------------------------|
| Slide transition     | Instant / 150ms    | 300ms ease-out         | 500ms 3D / scale            |
| Content entrance     | Immediate          | fadeInUp 500ms stagger | springIn 700ms stagger      |
| Chart animation      | `false`            | 800ms easeOutQuart     | 1200ms sequential delay     |
| Number display       | Static             | CountUp 1.5s           | CountUp 2.5s + digit scroll |
| Hover                | Opacity only       | Scale + shadow         | Scale + glow + brightness   |
| Background           | Static             | Static                 | Gradient shift / particles  |
| Title effect         | Static text        | Static text            | Typed.js typing             |
| Code blocks          | Static             | Line highlight         | Line highlight              |
| `prefers-reduced-motion` | Always this level | Falls back to minimal | Falls back to minimal     |
