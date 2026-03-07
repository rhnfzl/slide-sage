# Presenter Mode Reference

## Default: HTML Comment Notes

Speaker notes are embedded as HTML comments inside each slide. They are invisible during the presentation and extracted by the presenter mode JavaScript.

### Format

```html
<div class="slide" id="slide-1">
  <div class="slide-content">
    <h1>Welcome</h1>
  </div>
  <!-- NOTES:
  - Greet the audience
  - Mention the agenda
  - 2 minutes for this slide
  -->
</div>
```

```html
<div class="slide" id="slide-2">
  <div class="slide-content">
    <h2>Architecture Overview</h2>
    <p>Our system uses a microservices architecture.</p>
  </div>
  <!-- NOTES:
  Key points:
  - 12 microservices in production
  - Each service owns its database
  - Communication via async message queue
  - Mention the migration from monolith took 8 months
  -->
</div>
```

Notes are **invisible** in the presentation view. Only the presenter window displays them.

---

## Note Extraction JavaScript

```javascript
function extractNotes() {
  const slides = document.querySelectorAll('.slide');
  const notes = [];
  slides.forEach(slide => {
    const html = slide.innerHTML;
    const match = html.match(/<!--\s*NOTES:([\s\S]*?)-->/);
    notes.push(match ? match[1].trim() : '');
  });
  return notes;
}
```

This returns an array of strings, one per slide. Slides without `<!-- NOTES: -->` comments get an empty string.

---

## Full Presenter Mode

### Activation

Press **'P'** to open the presenter window. The main presentation window continues to display slides fullscreen while the presenter window shows the dual-panel control view.

### Architecture

Uses the **BroadcastChannel API** for synchronization between the main window and presenter window. BroadcastChannel works on `file://` protocol (unlike postMessage which requires specific origin targeting), making it ideal for local HTML presentations.

---

### Main Window Integration

Add these methods to the `SlidePresentation` class (~30 lines):

```javascript
// Add to SlidePresentation class

initPresenter() {
  this.presenterChannel = new BroadcastChannel('slide-sage-presenter');
  this.presenterChannel.onmessage = (e) => {
    if (e.data.type === 'navigate') {
      this.goToSlide(e.data.slide);
    }
  };
}

openPresenterView() {
  const notes = extractNotes();
  const presenterHTML = generatePresenterHTML(this.slides.length, notes);
  const presenterWindow = window.open('', 'slide-sage-presenter', 'width=1000,height=700');
  presenterWindow.document.write(presenterHTML);
  presenterWindow.document.close();

  // Send initial state
  this.presenterChannel.postMessage({
    type: 'init',
    currentSlide: this.currentSlide,
    totalSlides: this.slides.length
  });
}

// Modify the existing navigate method to broadcast state
navigate(index) {
  // ... existing navigation code ...
  this.currentSlide = index;

  if (this.presenterChannel) {
    this.presenterChannel.postMessage({
      type: 'update',
      slide: this.currentSlide,
      totalSlides: this.slides.length
    });
  }
}
```

### Keyboard Binding

Add to the existing keydown handler:

```javascript
// Inside the keydown event listener
if (e.key === 'p' || e.key === 'P') {
  e.preventDefault();
  this.openPresenterView();
}
```

---

### Presenter Window HTML Generator

Complete `generatePresenterHTML` function that returns a self-contained HTML document:

```javascript
function generatePresenterHTML(totalSlides, notes) {
  const notesJSON = JSON.stringify(notes);

  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Slide Sage - Presenter View</title>
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: #1a1a2e;
    color: #e0e0e8;
    height: 100vh;
    overflow: hidden;
    display: grid;
    grid-template-columns: 60% 40%;
    grid-template-rows: 55% 45%;
    gap: 2px;
  }

  /* === Quadrant: Current Slide (top-left) === */
  .current-slide {
    grid-column: 1;
    grid-row: 1;
    background: #16162a;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 6px;
    margin: 8px 4px 4px 8px;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  .current-slide .panel-label {
    padding: 6px 12px;
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #61afef;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    flex-shrink: 0;
  }

  .current-slide .preview-area {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 8px;
    font-size: 1.8rem;
    color: #abb2bf;
    font-weight: 600;
  }

  /* === Quadrant: Next Slide (top-right) === */
  .next-slide {
    grid-column: 2;
    grid-row: 1;
    background: #16162a;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 6px;
    margin: 8px 8px 4px 4px;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  .next-slide .panel-label {
    padding: 6px 12px;
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #98c379;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    flex-shrink: 0;
  }

  .next-slide .preview-area {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 8px;
    font-size: 1.4rem;
    color: rgba(171, 178, 191, 0.6);
    font-weight: 500;
  }

  /* === Quadrant: Speaker Notes (bottom-left) === */
  .notes-panel {
    grid-column: 1;
    grid-row: 2;
    background: #16162a;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 6px;
    margin: 4px 4px 8px 8px;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  .notes-panel .panel-label {
    padding: 6px 12px;
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #c678dd;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    flex-shrink: 0;
  }

  .notes-content {
    flex: 1;
    padding: 12px 16px;
    font-size: 1.1rem;
    line-height: 1.7;
    color: #d4d4dc;
    overflow-y: auto;
    white-space: pre-wrap;
    word-wrap: break-word;
  }

  .notes-content::-webkit-scrollbar {
    width: 6px;
  }
  .notes-content::-webkit-scrollbar-track {
    background: transparent;
  }
  .notes-content::-webkit-scrollbar-thumb {
    background: rgba(255,255,255,0.15);
    border-radius: 3px;
  }

  .no-notes {
    color: rgba(255,255,255,0.25);
    font-style: italic;
  }

  /* === Quadrant: Controls (bottom-right) === */
  .controls-panel {
    grid-column: 2;
    grid-row: 2;
    background: #16162a;
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 6px;
    margin: 4px 8px 8px 4px;
    display: flex;
    flex-direction: column;
    padding: 12px 16px;
    gap: 14px;
    overflow: hidden;
  }

  /* Timer */
  .timer-section {
    text-align: center;
  }

  .timer-display {
    font-size: 2.4rem;
    font-weight: 700;
    font-variant-numeric: tabular-nums;
    color: #e5c07b;
    letter-spacing: 0.05em;
    margin-bottom: 6px;
  }

  .timer-buttons {
    display: flex;
    gap: 6px;
    justify-content: center;
  }

  .timer-buttons button {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    color: #d4d4dc;
    padding: 4px 14px;
    border-radius: 4px;
    font-size: 0.8rem;
    cursor: pointer;
    transition: all 0.15s;
  }

  .timer-buttons button:hover {
    background: rgba(255,255,255,0.15);
    color: #fff;
  }

  .timer-buttons button.active {
    background: rgba(97, 175, 239, 0.2);
    border-color: #61afef;
    color: #61afef;
  }

  /* Slide Counter */
  .slide-counter {
    text-align: center;
    font-size: 1.2rem;
    color: #abb2bf;
  }

  .slide-counter .current {
    font-size: 1.8rem;
    font-weight: 700;
    color: #61afef;
  }

  .slide-counter .separator {
    margin: 0 4px;
    color: rgba(255,255,255,0.3);
  }

  .slide-counter .total {
    font-size: 1.3rem;
    color: rgba(255,255,255,0.5);
  }

  /* Navigation */
  .nav-buttons {
    display: flex;
    gap: 8px;
    justify-content: center;
  }

  .nav-buttons button {
    background: rgba(97, 175, 239, 0.15);
    border: 1px solid rgba(97, 175, 239, 0.3);
    color: #61afef;
    padding: 8px 24px;
    border-radius: 6px;
    font-size: 0.9rem;
    cursor: pointer;
    transition: all 0.15s;
    flex: 1;
    max-width: 140px;
  }

  .nav-buttons button:hover {
    background: rgba(97, 175, 239, 0.25);
    color: #fff;
  }

  .nav-buttons button:disabled {
    opacity: 0.3;
    cursor: not-allowed;
  }

  /* Clock */
  .clock {
    text-align: center;
    font-size: 1rem;
    color: rgba(255,255,255,0.4);
    margin-top: auto;
  }

  /* Progress bar */
  .progress-bar {
    width: 100%;
    height: 3px;
    background: rgba(255,255,255,0.08);
    border-radius: 2px;
    overflow: hidden;
  }

  .progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #61afef, #c678dd);
    transition: width 0.3s ease;
    border-radius: 2px;
  }
</style>
</head>
<body>

<!-- Top-left: Current Slide -->
<div class="current-slide">
  <div class="panel-label">Current Slide</div>
  <div class="preview-area" id="current-preview">Slide 1</div>
</div>

<!-- Top-right: Next Slide -->
<div class="next-slide">
  <div class="panel-label">Next Slide</div>
  <div class="preview-area" id="next-preview">Slide 2</div>
</div>

<!-- Bottom-left: Speaker Notes -->
<div class="notes-panel">
  <div class="panel-label">Speaker Notes</div>
  <div class="notes-content" id="notes-content">
    <span class="no-notes">No notes for this slide.</span>
  </div>
</div>

<!-- Bottom-right: Controls -->
<div class="controls-panel">
  <div class="timer-section">
    <div class="timer-display" id="timer">00:00:00</div>
    <div class="timer-buttons">
      <button id="btn-start" onclick="startTimer()">Start</button>
      <button id="btn-pause" onclick="pauseTimer()">Pause</button>
      <button id="btn-reset" onclick="resetTimer()">Reset</button>
    </div>
  </div>

  <div class="progress-bar">
    <div class="progress-fill" id="progress-fill" style="width: 0%"></div>
  </div>

  <div class="slide-counter">
    <span class="current" id="counter-current">1</span>
    <span class="separator">of</span>
    <span class="total" id="counter-total">${totalSlides}</span>
  </div>

  <div class="nav-buttons">
    <button id="btn-prev" onclick="navigatePrev()">Previous</button>
    <button id="btn-next" onclick="navigateNext()">Next</button>
  </div>

  <div class="clock" id="clock">--:--:--</div>
</div>

<script>
  // === State ===
  const totalSlides = ${totalSlides};
  const notes = ${notesJSON};
  let currentSlide = 0;

  // === BroadcastChannel Sync ===
  const channel = new BroadcastChannel('slide-sage-presenter');

  channel.onmessage = (e) => {
    if (e.data.type === 'update' || e.data.type === 'init' || e.data.type === 'navigate') {
      const slideIndex = e.data.slide !== undefined ? e.data.slide : e.data.currentSlide;
      if (slideIndex !== undefined) {
        currentSlide = slideIndex;
        updatePresenterView(currentSlide);
      }
    }
  };

  function navigateFromPresenter(slideIndex) {
    if (slideIndex < 0 || slideIndex >= totalSlides) return;
    currentSlide = slideIndex;
    channel.postMessage({ type: 'navigate', slide: slideIndex });
    updatePresenterView(slideIndex);
  }

  function navigatePrev() {
    if (currentSlide > 0) navigateFromPresenter(currentSlide - 1);
  }

  function navigateNext() {
    if (currentSlide < totalSlides - 1) navigateFromPresenter(currentSlide + 1);
  }

  // === Update View ===
  function updatePresenterView(slideIndex) {
    // Current slide indicator
    document.getElementById('current-preview').textContent = 'Slide ' + (slideIndex + 1);

    // Next slide indicator
    const nextEl = document.getElementById('next-preview');
    if (slideIndex + 1 < totalSlides) {
      nextEl.textContent = 'Slide ' + (slideIndex + 2);
      nextEl.style.opacity = '1';
    } else {
      nextEl.textContent = 'End of presentation';
      nextEl.style.opacity = '0.4';
    }

    // Notes
    const notesEl = document.getElementById('notes-content');
    if (notes[slideIndex] && notes[slideIndex].length > 0) {
      notesEl.textContent = notes[slideIndex];
      notesEl.classList.remove('no-notes');
    } else {
      notesEl.innerHTML = '<span class="no-notes">No notes for this slide.</span>';
    }

    // Counter
    document.getElementById('counter-current').textContent = slideIndex + 1;

    // Progress
    const pct = totalSlides > 1 ? ((slideIndex) / (totalSlides - 1)) * 100 : 100;
    document.getElementById('progress-fill').style.width = pct + '%';

    // Nav button states
    document.getElementById('btn-prev').disabled = (slideIndex === 0);
    document.getElementById('btn-next').disabled = (slideIndex === totalSlides - 1);
  }

  // === Timer ===
  let timerStart = null;
  let timerRunning = false;
  let elapsed = 0;

  function startTimer() {
    timerStart = Date.now() - elapsed;
    timerRunning = true;
    document.getElementById('btn-start').classList.add('active');
    document.getElementById('btn-pause').classList.remove('active');
    tick();
  }

  function pauseTimer() {
    timerRunning = false;
    elapsed = Date.now() - timerStart;
    document.getElementById('btn-start').classList.remove('active');
    document.getElementById('btn-pause').classList.add('active');
  }

  function resetTimer() {
    timerRunning = false;
    elapsed = 0;
    timerStart = null;
    updateTimerDisplay(0);
    document.getElementById('btn-start').classList.remove('active');
    document.getElementById('btn-pause').classList.remove('active');
  }

  function tick() {
    if (!timerRunning) return;
    elapsed = Date.now() - timerStart;
    updateTimerDisplay(elapsed);
    requestAnimationFrame(tick);
  }

  function updateTimerDisplay(ms) {
    const s = Math.floor(ms / 1000);
    const m = Math.floor(s / 60);
    const h = Math.floor(m / 60);
    document.getElementById('timer').textContent =
      String(h).padStart(2, '0') + ':' +
      String(m % 60).padStart(2, '0') + ':' +
      String(s % 60).padStart(2, '0');
  }

  // === Clock ===
  function updateClock() {
    const now = new Date();
    document.getElementById('clock').textContent =
      now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
  }
  setInterval(updateClock, 1000);
  updateClock();

  // === Keyboard shortcuts in presenter window ===
  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
      e.preventDefault();
      navigateNext();
    } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
      e.preventDefault();
      navigatePrev();
    } else if (e.key === 't' || e.key === 'T') {
      if (timerRunning) pauseTimer(); else startTimer();
    } else if (e.key === 'r' || e.key === 'R') {
      resetTimer();
    }
  });

  // === Initial render ===
  updatePresenterView(currentSlide);
</script>
</body>
</html>`;
}
```

---

## Summary of Key Bindings

### Main Presentation Window
| Key | Action |
|-----|--------|
| `P` | Open presenter view |
| Arrow keys / Space | Navigate slides (existing) |

### Presenter Window
| Key | Action |
|-----|--------|
| Left Arrow / PageUp | Previous slide |
| Right Arrow / Space / PageDown | Next slide |
| `T` | Toggle timer (start/pause) |
| `R` | Reset timer |

---

## BroadcastChannel Message Protocol

### Message Types

| Type | Direction | Payload | Purpose |
|------|-----------|---------|---------|
| `init` | Main -> Presenter | `{ currentSlide, totalSlides }` | Initial state when presenter opens |
| `update` | Main -> Presenter | `{ slide, totalSlides }` | Slide changed in main window |
| `navigate` | Either direction | `{ slide }` | Navigation request |

### Channel Name

```
'slide-sage-presenter'
```

Constant across all presentations. Only one presenter session should be active at a time.

---

## Integration Checklist

1. Add `extractNotes()` function to the presentation script
2. Add `generatePresenterHTML()` function to the presentation script
3. Add `initPresenter()`, `openPresenterView()` methods to SlidePresentation class
4. Modify `navigate()` to broadcast via BroadcastChannel
5. Add `'P'` key binding to open presenter view
6. Call `initPresenter()` in the constructor

---

## Fallback: No BroadcastChannel

For very old browsers that lack BroadcastChannel support (pre-2016), a localStorage-based fallback:

```javascript
// Fallback using localStorage events
function sendViaStorage(data) {
  localStorage.setItem('slide-sage-presenter', JSON.stringify({
    ...data,
    timestamp: Date.now()
  }));
}

window.addEventListener('storage', (e) => {
  if (e.key === 'slide-sage-presenter') {
    const data = JSON.parse(e.newValue);
    handleMessage(data);
  }
});
```

**Note**: localStorage events only fire in *other* windows/tabs (not the one that set the value), which matches the presenter mode use case. However, BroadcastChannel is preferred and supported in all modern browsers.
