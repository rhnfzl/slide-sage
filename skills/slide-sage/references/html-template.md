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

    <div class="slide active" id="slide-1" aria-hidden="false">
      <!-- Slide content here -->
    </div>

    <div class="slide inactive" id="slide-2" aria-hidden="true" inert>
      <!-- Slide content here -->
    </div>

    <!-- Additional slides follow the same pattern -->

  </div>

  <!-- Notes remain readable in the HTML source. Do not put secrets in a shared deck. -->
  <script id="speaker-notes" type="application/json">
    [{"slide": 1, "notes": "Opening context and outcome."}, {"slide": 2, "notes": "Key evidence and decision."}]
  </script>

  <!-- Navigation UI -->
  <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
  <div class="slide-counter" id="slideCounter"></div>
  <div class="nav-arrows">
    <button class="nav-arrow nav-prev" id="navPrev" aria-label="Previous slide">&#8592;</button>
    <button class="nav-arrow nav-next" id="navNext" aria-label="Next slide">&#8594;</button>
  </div>

  <!-- Keyboard shortcuts overlay -->
  <div class="shortcuts-overlay" id="shortcutsOverlay" role="dialog" aria-modal="true" aria-labelledby="shortcutsTitle" aria-hidden="true" inert>
    <div class="shortcuts-panel" tabindex="-1">
      <div class="shortcuts-heading-row">
        <h3 id="shortcutsTitle">Keyboard Shortcuts</h3>
        <button class="shortcuts-close" id="shortcutsClose" type="button" aria-label="Close keyboard shortcuts">&#215;</button>
      </div>
      <table>
        <tr><td><kbd>&#8594;</kbd> / <kbd>Space</kbd></td><td>Next slide</td></tr>
        <tr><td><kbd>&#8592;</kbd> / <kbd>Shift+Space</kbd></td><td>Previous slide</td></tr>
        <tr><td><kbd>Home</kbd></td><td>First slide</td></tr>
        <tr><td><kbd>End</kbd></td><td>Last slide</td></tr>
        <tr><td><kbd>Page Down</kbd></td><td>Next slide</td></tr>
        <tr><td><kbd>Page Up</kbd></td><td>Previous slide</td></tr>
        <tr><td><kbd>P</kbd></td><td>Open presenter view when included</td></tr>
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
    this.isPrinting = false;
    this.lastFocusedElement = null;
    this.shortcutsFocusFrame = null;

    this.progressFill = document.getElementById('progressFill');
    this.slideCounter = document.getElementById('slideCounter');
    this.shortcutsOverlay = document.getElementById('shortcutsOverlay');
    this.shortcutsPanel = this.shortcutsOverlay?.querySelector('.shortcuts-panel');
    this.shortcutsClose = document.getElementById('shortcutsClose');
    this.navPrev = document.getElementById('navPrev');
    this.navNext = document.getElementById('navNext');

    this.init();
  }

  init() {
    this.bindKeyboard();
    this.bindTouch();
    this.bindNavButtons();
    this.bindShortcutsDialog();
    this.bindHashChange();
    this.bindPrintPreparation();
    this.readHashAndNavigate();
    this.updateUI();
    this.ready = true;

    // Delay the first lifecycle event until chart scripts in this DOM-ready turn exist.
    window.requestAnimationFrame(() => {
      this.emitSlideChange(null);
      this.markPrintReady();
    });
  }

  bindKeyboard() {
    document.addEventListener('keydown', (e) => {
      if (this.isShortcutsVisible()) {
        if (e.key === 'Escape') {
          e.preventDefault();
          this.hideShortcuts();
        } else if (e.key === 'Tab') {
          this.trapShortcutsFocus(e);
        } else if (e.key === '?') {
          e.preventDefault();
          this.hideShortcuts();
        } else {
          e.preventDefault();
        }
        return;
      }

      // Ignore if user is typing in an input or textarea
      if (
        e.target.tagName === 'INPUT' ||
        e.target.tagName === 'TEXTAREA' ||
        e.target.tagName === 'SELECT' ||
        e.target.isContentEditable
      ) return;

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
          e.preventDefault();
          this.toggleShortcuts();
          break;
        case 'p':
        case 'P':
          e.preventDefault();
          this.openPresenterMode();
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

  bindShortcutsDialog() {
    if (!this.shortcutsOverlay) return;

    this.shortcutsClose?.addEventListener('click', () => this.hideShortcuts());
    this.shortcutsOverlay.addEventListener('click', (event) => {
      if (event.target === this.shortcutsOverlay) this.hideShortcuts();
    });
  }

  bindHashChange() {
    window.addEventListener('hashchange', () => this.readHashAndNavigate());
  }

  bindPrintPreparation() {
    window.addEventListener('beforeprint', () => {
      this.isPrinting = true;
      this.slides.forEach((slide) => {
        slide.removeAttribute('inert');
        slide.setAttribute('aria-hidden', 'false');
      });
      void this.markPrintReady();
    });
    window.addEventListener('afterprint', () => {
      this.isPrinting = false;
      this.updateUI();
    });
  }

  async markPrintReady() {
    if (document.fonts?.ready) {
      await document.fonts.ready;
    }

    if (typeof Chart !== 'undefined' && typeof Chart.getChart === 'function') {
      document.querySelectorAll('canvas').forEach((canvas) => {
        const chart = Chart.getChart(canvas);
        if (!chart) return;
        chart.stop();
        chart.options.animation = false;
        chart.update('none');
      });
    }

    if (typeof echarts !== 'undefined' && typeof echarts.getInstanceByDom === 'function') {
      document.querySelectorAll('[data-slide-sage-echarts]').forEach((element) => {
        const chart = echarts.getInstanceByDom(element);
        if (!chart) return;
        chart.setOption({ animation: false }, false);
        chart.resize();
      });
    }

    document.documentElement.dataset.slideSagePrintReady = 'true';
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
    const shouldMoveFocus = previousSlide.contains(document.activeElement);

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
    if (shouldMoveFocus) this.moveFocusToIncomingSlide(nextSlide);

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

    // Ensure only the active slide is visible and exposed to assistive technology.
    this.slides.forEach((slide, i) => {
      const isActive = i === this.currentSlide;
      if (isActive) {
        slide.classList.add('active');
        slide.classList.remove('inactive');
      } else {
        slide.classList.remove('active');
        slide.classList.add('inactive');
      }

      if (this.isPrinting || isActive) {
        slide.removeAttribute('inert');
        slide.setAttribute('aria-hidden', 'false');
      } else {
        slide.setAttribute('inert', '');
        slide.setAttribute('aria-hidden', 'true');
      }
    });
  }

  moveFocusToIncomingSlide(nextSlide) {
    const target = nextSlide.querySelector(
      'a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])'
    ) || nextSlide;
    if (target === nextSlide && !nextSlide.hasAttribute('tabindex')) {
      nextSlide.setAttribute('tabindex', '-1');
    }
    target.focus({ preventScroll: true });
  }

  isShortcutsVisible() {
    return Boolean(this.shortcutsOverlay?.classList.contains('visible'));
  }

  shortcutsFocusableElements() {
    if (!this.shortcutsOverlay) return [];
    return [...this.shortcutsOverlay.querySelectorAll(
      'a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])'
    )].filter((element) => !element.hasAttribute('hidden'));
  }

  trapShortcutsFocus(event) {
    const focusable = this.shortcutsFocusableElements();
    if (focusable.length === 0) {
      event.preventDefault();
      this.shortcutsPanel?.focus();
      return;
    }

    const first = focusable[0];
    const last = focusable[focusable.length - 1];
    if (event.shiftKey && (document.activeElement === first || !this.shortcutsOverlay.contains(document.activeElement))) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && (document.activeElement === last || !this.shortcutsOverlay.contains(document.activeElement))) {
      event.preventDefault();
      first.focus();
    }
  }

  restoreShortcutsFocus() {
    const target = this.lastFocusedElement;
    this.lastFocusedElement = null;
    if (target?.isConnected && target !== document.body && typeof target.focus === 'function') {
      target.focus({ preventScroll: true });
      return;
    }
    const fallback = (!this.navNext?.disabled && this.navNext) ||
      (!this.navPrev?.disabled && this.navPrev) ||
      this.slides[this.currentSlide];
    if (fallback === this.slides[this.currentSlide] && !fallback.hasAttribute('tabindex')) {
      fallback.setAttribute('tabindex', '-1');
    }
    fallback?.focus({ preventScroll: true });
  }

  toggleShortcuts() {
    if (this.isShortcutsVisible()) {
      this.hideShortcuts();
    } else {
      this.showShortcuts();
    }
  }

  showShortcuts() {
    if (!this.shortcutsOverlay) return;
    this.lastFocusedElement = document.activeElement instanceof HTMLElement && document.activeElement !== document.body
      ? document.activeElement
      : null;
    this.shortcutsOverlay.removeAttribute('inert');
    this.shortcutsOverlay.classList.add('visible');
    this.shortcutsOverlay.setAttribute('aria-hidden', 'false');
    this.shortcutsFocusFrame = window.requestAnimationFrame(() => {
      this.shortcutsFocusFrame = null;
      if (this.isShortcutsVisible()) (this.shortcutsClose || this.shortcutsPanel)?.focus();
    });
  }

  hideShortcuts() {
    if (!this.shortcutsOverlay || !this.isShortcutsVisible()) return;
    if (this.shortcutsFocusFrame !== null) {
      window.cancelAnimationFrame(this.shortcutsFocusFrame);
      this.shortcutsFocusFrame = null;
    }
    this.shortcutsOverlay.setAttribute('inert', '');
    this.shortcutsOverlay.classList.remove('visible');
    this.shortcutsOverlay.setAttribute('aria-hidden', 'true');
    this.restoreShortcutsFocus();
  }

  openPresenterMode() {
    if (typeof window.openSlideSagePresenter === 'function') {
      window.openSlideSagePresenter(this);
    }
  }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  new SlidePresentation();
});
```

## Speaker Notes System

Speaker notes use one JSON data block, placed after the slides and before the navigation UI:

```html
<script id="speaker-notes" type="application/json">
[
  {"slide": 1, "notes": "Welcome the audience. Mention the agenda and the time box."},
  {"slide": 2, "notes": "Read the retention number alongside the revenue evidence."}
]
</script>
```

The `slide` values are one-based and must cover the deck in order. Generate the JSON with `JSON.stringify(notes).replace(/</g, '\\u003c')` before embedding it, so note text cannot terminate the script block. Presenter mode reads the block through `textContent` and treats malformed data as empty notes.

Notes remain readable in the shared HTML source and presenter window. Do not put passwords, private links, or other secrets in them.

## Print Styles

These print-specific styles are included in every presentation:

```css
@media print {
  html,
  body,
  .slides-container {
    height: auto !important;
    overflow: visible !important;
  }

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

`assets/viewport-base.css` defines `.shortcuts-overlay`, `.shortcuts-panel`, `.shortcuts-heading-row`, `.shortcuts-close`, and `.shortcuts-dismiss`. Inline it unchanged so the dialog has a visible focus state, a keyboard-reachable close control, and viewport-safe sizing.

## CDN Script Placement

External libraries load before the closing `</body>` tag, before the SlidePresentation script:

```html
  <!-- Chart.js (when charts are needed) -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js" integrity="sha384-vsrfeLOOY6KuIYKDlmVH5UiBmgIdB1oEf7p01YgWHuqmOHfZr374+odEv96n9tNC" crossorigin="anonymous"></script>

  <!-- Prism.js (when code blocks are needed) -->
  <script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/prism.min.js" integrity="sha384-Cn/s7dpCMIb2rgIjtCYcpcv3LPJjUciybJ5G/sGMK025lFiqdJ4pRgUEgIcolGuJ" crossorigin="anonymous"></script>
  <!-- Add language grammars as needed, e.g.: -->
  <!-- <script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/components/prism-python.min.js" integrity="sha384-WJdEkJKrbsqw0evQ4GB6mlsKe5cGTxBOw4KAEIa52ZLB7DDpliGkwdme/HMa5n1m" crossorigin="anonymous"></script> -->

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
