# HTML Presentation Template Reference

Base HTML structure for AI-generated slide presentations. This is the canonical template that slide-sage uses to build every presentation.

## Complete HTML5 Boilerplate

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{PRESENTATION_TITLE}}</title>
  <style>
    /* viewport-base.css gets inlined here */
    {{VIEWPORT_BASE_CSS}}

    /* Presentation-specific styles go here */
    {{PRESENTATION_CSS}}
  </style>
</head>
<body>
  <div class="slides-container" id="slides">

    <div class="slide" id="slide-1">
      <!-- Slide content here -->
    </div>
    <!-- NOTES: Speaker notes for slide 1 go here. These are HTML comments and are hidden from view. -->

    <div class="slide" id="slide-2">
      <!-- Slide content here -->
    </div>
    <!-- NOTES: Speaker notes for slide 2. -->

    <!-- Additional slides follow the same pattern -->

  </div>

  <!-- Navigation UI -->
  <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
  <div class="slide-counter" id="slideCounter"></div>
  <div class="nav-arrows">
    <button class="nav-arrow nav-prev" id="navPrev" aria-label="Previous slide">&#8592;</button>
    <button class="nav-arrow nav-next" id="navNext" aria-label="Next slide">&#8594;</button>
  </div>

  <!-- Keyboard shortcuts overlay -->
  <div class="shortcuts-overlay" id="shortcutsOverlay" role="dialog" aria-label="Keyboard shortcuts" aria-hidden="true">
    <div class="shortcuts-panel">
      <h3>Keyboard Shortcuts</h3>
      <table>
        <tr><td><kbd>&#8594;</kbd> / <kbd>Space</kbd></td><td>Next slide</td></tr>
        <tr><td><kbd>&#8592;</kbd> / <kbd>Shift+Space</kbd></td><td>Previous slide</td></tr>
        <tr><td><kbd>Home</kbd></td><td>First slide</td></tr>
        <tr><td><kbd>End</kbd></td><td>Last slide</td></tr>
        <tr><td><kbd>Page Down</kbd></td><td>Next slide</td></tr>
        <tr><td><kbd>Page Up</kbd></td><td>Previous slide</td></tr>
        <tr><td><kbd>?</kbd></td><td>Toggle this help</td></tr>
      </table>
      <p class="shortcuts-dismiss">Press <kbd>?</kbd> or <kbd>Esc</kbd> to close</p>
    </div>
  </div>

  <!-- CDN scripts go here (Chart.js, Highlight.js, etc.) -->
  {{CDN_SCRIPTS}}

  <script>
    {{SLIDE_PRESENTATION_JS}}
  </script>
</body>
</html>
```

## SlidePresentation JavaScript Class

This is the complete JS class. Copy it verbatim into every presentation.

```javascript
class SlidePresentation {
  constructor() {
    this.slides = document.querySelectorAll('.slide');
    this.totalSlides = this.slides.length;
    this.currentSlide = 0;
    this.touchStartX = 0;
    this.touchEndX = 0;
    this.swipeThreshold = 50;
    this.reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    this.ready = false;

    this.progressFill = document.getElementById('progressFill');
    this.slideCounter = document.getElementById('slideCounter');
    this.shortcutsOverlay = document.getElementById('shortcutsOverlay');
    this.navPrev = document.getElementById('navPrev');
    this.navNext = document.getElementById('navNext');

    this.init();
  }

  init() {
    this.bindKeyboard();
    this.bindTouch();
    this.bindNavButtons();
    this.bindHashChange();
    this.readHashAndNavigate();
    this.updateUI();
    this.ready = true;

    // Delay the first lifecycle event until chart scripts in this DOM-ready turn exist.
    window.requestAnimationFrame(() => this.emitSlideChange(null));
  }

  bindKeyboard() {
    document.addEventListener('keydown', (e) => {
      // Ignore if user is typing in an input or textarea
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

      switch (e.key) {
        case 'ArrowRight':
        case 'ArrowDown':
          e.preventDefault();
          this.next();
          break;
        case 'ArrowLeft':
        case 'ArrowUp':
          e.preventDefault();
          this.prev();
          break;
        case ' ':
          e.preventDefault();
          if (e.shiftKey) {
            this.prev();
          } else {
            this.next();
          }
          break;
        case 'PageDown':
          e.preventDefault();
          this.next();
          break;
        case 'PageUp':
          e.preventDefault();
          this.prev();
          break;
        case 'Home':
          e.preventDefault();
          this.goTo(0);
          break;
        case 'End':
          e.preventDefault();
          this.goTo(this.totalSlides - 1);
          break;
        case '?':
          this.toggleShortcuts();
          break;
        case 'Escape':
          this.hideShortcuts();
          break;
      }
    });
  }

  bindTouch() {
    const container = document.getElementById('slides');

    container.addEventListener('touchstart', (e) => {
      this.touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });

    container.addEventListener('touchend', (e) => {
      this.touchEndX = e.changedTouches[0].screenX;
      this.handleSwipe();
    }, { passive: true });
  }

  handleSwipe() {
    const diff = this.touchStartX - this.touchEndX;
    if (Math.abs(diff) < this.swipeThreshold) return;

    if (diff > 0) {
      this.next();
    } else {
      this.prev();
    }
  }

  bindNavButtons() {
    if (this.navPrev) {
      this.navPrev.addEventListener('click', () => this.prev());
    }
    if (this.navNext) {
      this.navNext.addEventListener('click', () => this.next());
    }
  }

  bindHashChange() {
    window.addEventListener('hashchange', () => this.readHashAndNavigate());
  }

  readHashAndNavigate() {
    const hash = window.location.hash;
    const match = hash.match(/^#slide-(\d+)$/);
    if (match) {
      const index = parseInt(match[1], 10) - 1;
      if (index >= 0 && index < this.totalSlides) {
        this.goTo(index, false);
      }
    }
  }

  next() {
    if (this.currentSlide < this.totalSlides - 1) {
      this.goTo(this.currentSlide + 1);
    }
  }

  prev() {
    if (this.currentSlide > 0) {
      this.goTo(this.currentSlide - 1);
    }
  }

  goTo(index, updateHash = true) {
    if (index < 0 || index >= this.totalSlides) return;
    if (index === this.currentSlide) return;

    const previousSlide = this.slides[this.currentSlide];
    const nextSlide = this.slides[index];

    previousSlide.classList.remove('active');
    previousSlide.classList.add('inactive');

    nextSlide.classList.remove('inactive');
    nextSlide.classList.add('active');

    if (this.reducedMotion) {
      previousSlide.style.transition = 'none';
      nextSlide.style.transition = 'none';
    }

    this.currentSlide = index;

    if (updateHash) {
      history.replaceState(null, '', `#slide-${index + 1}`);
    }

    this.updateUI();

    if (this.ready) {
      this.emitSlideChange(previousSlide);
    }
  }

  emitSlideChange(previousSlide) {
    document.dispatchEvent(new CustomEvent('slidechange', {
      detail: {
        slide: this.slides[this.currentSlide],
        index: this.currentSlide,
        previousSlide,
        reducedMotion: this.reducedMotion
      }
    }));
  }

  updateUI() {
    // Update progress bar
    if (this.progressFill) {
      const progress = ((this.currentSlide + 1) / this.totalSlides) * 100;
      this.progressFill.style.width = `${progress}%`;
    }

    // Update slide counter
    if (this.slideCounter) {
      this.slideCounter.textContent = `${this.currentSlide + 1} / ${this.totalSlides}`;
    }

    // Update nav button states
    if (this.navPrev) {
      this.navPrev.disabled = this.currentSlide === 0;
    }
    if (this.navNext) {
      this.navNext.disabled = this.currentSlide === this.totalSlides - 1;
    }

    // Ensure only active slide is visible
    this.slides.forEach((slide, i) => {
      if (i === this.currentSlide) {
        slide.classList.add('active');
        slide.classList.remove('inactive');
      } else {
        slide.classList.remove('active');
        slide.classList.add('inactive');
      }
    });
  }

  toggleShortcuts() {
    if (this.shortcutsOverlay) {
      const nowVisible = this.shortcutsOverlay.classList.toggle('visible');
      this.shortcutsOverlay.setAttribute('aria-hidden', String(!nowVisible));
    }
  }

  hideShortcuts() {
    if (this.shortcutsOverlay) {
      this.shortcutsOverlay.classList.remove('visible');
      this.shortcutsOverlay.setAttribute('aria-hidden', 'true');
    }
  }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  new SlidePresentation();
});
```

## Speaker Notes System

Speaker notes are embedded as HTML comments immediately after each `.slide` div. They use the `<!-- NOTES: -->` prefix convention:

```html
<div class="slide" id="slide-1">
  <div class="slide-content">
    <h1>Welcome</h1>
    <p>Introduction to the topic</p>
  </div>
</div>
<!-- NOTES: Welcome the audience. Mention the agenda: 3 main sections, Q&A at end. Estimated time: 30 minutes. -->

<div class="slide" id="slide-2">
  <div class="slide-content">
    <h2>Key Metrics</h2>
    <ul>
      <li>Revenue grew 23% YoY</li>
      <li>Customer retention at 94%</li>
    </ul>
  </div>
</div>
<!-- NOTES: Emphasize the revenue growth - this is a record quarter. The retention number is up from 89% last year. Source: Q4 finance report. -->
```

Notes are:
- Invisible in the browser (HTML comments are not rendered)
- Preserved in the source for presenter reference
- Visible when printing if a "notes" print mode is added later

## Print Styles

These print-specific styles are included in every presentation:

```css
@media print {
  /* Each slide gets its own page */
  .slide {
    page-break-after: always;
    height: 100vh;
    overflow: visible;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .slide:last-child {
    page-break-after: avoid;
  }

  /* Hide navigation UI */
  .progress-bar,
  .slide-counter,
  .nav-arrows,
  .shortcuts-overlay {
    display: none !important;
  }

  /* Force backgrounds to print */
  .slide {
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
    color-adjust: exact;
  }

  /* Reasonable margins */
  @page {
    margin: 1cm;
    size: landscape;
  }

  /* Make all slides visible for print */
  .slide.inactive {
    display: flex !important;
    opacity: 1 !important;
    position: relative !important;
    transform: none !important;
  }

  /* Reset transitions */
  * {
    transition: none !important;
    animation: none !important;
  }
}
```

## Shortcuts Overlay Styles

```css
.shortcuts-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  opacity: 0;
  pointer-events: none;
  transition: opacity var(--transition-speed, 0.3s) ease;
}

.shortcuts-overlay.visible {
  opacity: 1;
  pointer-events: auto;
}

.shortcuts-panel {
  background: var(--color-surface);
  color: var(--color-text);
  border-radius: var(--radius);
  padding: 2rem;
  max-width: 420px;
  width: 90%;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4);
}

.shortcuts-panel h3 {
  margin: 0 0 1.2rem 0;
  font-size: clamp(1rem, 2vw, 1.2rem);
  color: var(--color-heading);
}

.shortcuts-panel table {
  width: 100%;
  border-collapse: collapse;
}

.shortcuts-panel td {
  padding: 0.4rem 0;
  font-size: clamp(0.75rem, 1.3vw, 0.9rem);
}

.shortcuts-panel td:first-child {
  white-space: nowrap;
  padding-right: 1.5rem;
}

.shortcuts-panel kbd {
  background: color-mix(in srgb, var(--color-text) 10%, transparent);
  border: 1px solid color-mix(in srgb, var(--color-text) 20%, transparent);
  border-radius: 4px;
  padding: 2px 6px;
  font-family: var(--font-mono, monospace);
  font-size: clamp(0.7rem, 1.1vw, 0.8rem);
}

.shortcuts-dismiss {
  margin: 1rem 0 0 0;
  font-size: clamp(0.7rem, 1.1vw, 0.8rem);
  opacity: 0.6;
  text-align: center;
}
```

## CDN Script Placement

External libraries load before the closing `</body>` tag, before the SlidePresentation script:

```html
  <!-- Chart.js (when charts are needed) -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js"></script>

  <!-- Prism.js (when code blocks are needed) -->
  <script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/prism.min.js"></script>
  <!-- Add language grammars as needed, e.g.: -->
  <!-- <script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-python.min.js"></script> -->

  <!-- SlidePresentation class (always last) -->
  <script>
    class SlidePresentation { ... }
    document.addEventListener('DOMContentLoaded', () => {
      new SlidePresentation();

      // Initialize Prism.js if loaded
      if (typeof Prism !== 'undefined') {
        Prism.highlightAll();
      }
    });
  </script>
</body>
```

Only include CDN scripts that the presentation actually uses. Do not load Chart.js if there are no charts, or Highlight.js if there is no code.
