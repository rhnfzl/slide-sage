# Presenter Mode Reference

## One notes contract

Presenter mode is optional. When it is included, every deck uses one readable JSON block after the slide markup:

```html
<script id="speaker-notes" type="application/json">
[
  {"slide": 1, "notes": "Welcome the audience and state the decision this deck supports."},
  {"slide": 2, "notes": "Explain the source before interpreting the chart."}
]
</script>
```

Serialize the data safely before writing it into HTML:

```javascript
const notesJson = JSON.stringify(notes).replace(/</g, '\\u003c');
```

The `\\u003c` escape prevents note text such as `</script>` from ending the JSON block. Notes stay readable in the HTML source and the presenter window. Do not put passwords, private links, customer data, or other secrets in a deck that will be shared.

## Installation

The canonical `SlidePresentation` class already maps `P` to `openPresenterMode()` and calls `window.openSlideSagePresenter(this)` when the function is present. Add the following script after the canonical runtime only when the user requests presenter mode.

```javascript
function readSpeakerNotes(totalSlides) {
  const source = document.getElementById('speaker-notes')?.textContent || '[]';
  try {
    const parsed = JSON.parse(source);
    if (!Array.isArray(parsed)) return Array(totalSlides).fill('');
    const bySlide = new Map(
      parsed
        .filter((entry) => Number.isInteger(entry?.slide) && typeof entry?.notes === 'string')
        .map((entry) => [entry.slide, entry.notes])
    );
    return Array.from({ length: totalSlides }, (_, index) => bySlide.get(index + 1) || '');
  } catch (error) {
    console.warn('Speaker notes JSON is invalid. Presenter mode will use empty notes.', error);
    return Array(totalSlides).fill('');
  }
}

function sourceStyleMarkup() {
  return [...document.querySelectorAll('style, link[rel="stylesheet"]')]
    .map((node) => node.outerHTML)
    .join('\n');
}

function createPresenterDocument(styles) {
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Presenter view</title>
  ${styles}
  <style>
    * { box-sizing: border-box; }
    body { margin: 0; min-height: 100vh; padding: 1rem; background: #101820; color: #edf4f8; font-family: ui-sans-serif, system-ui, sans-serif; }
    .presenter-grid { display: grid; grid-template-columns: minmax(0, 3fr) minmax(18rem, 2fr); gap: 1rem; min-height: calc(100vh - 2rem); }
    .presenter-panel { min-width: 0; padding: 1rem; border: 1px solid #375268; border-radius: 0.75rem; background: #182632; }
    .presenter-panel h1 { margin: 0 0 0.75rem; font-size: clamp(0.9rem, 1.5vw, 1.15rem); }
    .preview-frame { width: 100%; overflow: hidden; border-radius: 0.4rem; background: #101820; }
    .preview-frame .slide { position: relative !important; top: 0 !important; left: 0 !important; opacity: 1 !important; z-index: 1 !important; pointer-events: none !important; transform-origin: top left; }
    .preview-frame img { max-width: 100%; }
    .preview-empty { display: grid; min-height: 12rem; place-items: center; color: #b8cad5; }
    .notes { min-height: 10rem; white-space: pre-wrap; line-height: 1.5; }
    .controls { display: grid; gap: 0.75rem; align-content: start; }
    .timer { font-variant-numeric: tabular-nums; font-size: clamp(1.6rem, 4vw, 3rem); }
    button { padding: 0.55rem 0.75rem; border: 1px solid #4a718d; border-radius: 0.4rem; background: #203442; color: inherit; cursor: pointer; }
    button:focus-visible { outline: 3px solid #BBAA33; outline-offset: 2px; }
    .button-row { display: flex; flex-wrap: wrap; gap: 0.5rem; }
    @media (max-width: 850px) { .presenter-grid { grid-template-columns: 1fr; } }
  </style>
</head>
<body>
  <main class="presenter-grid">
    <section class="presenter-panel"><h1>Current slide</h1><div class="preview-frame" id="currentPreview"></div></section>
    <section class="presenter-panel"><h1>Next slide</h1><div class="preview-frame" id="nextPreview"></div></section>
    <section class="presenter-panel"><h1>Speaker notes</h1><div class="notes" id="notes" role="status" aria-live="polite" aria-atomic="true">No notes for this slide.</div></section>
    <section class="presenter-panel controls">
      <h1>Controls</h1>
      <div class="timer" id="timer">00:00:00</div>
      <div class="button-row"><button id="startTimer" type="button">Start timer</button><button id="pauseTimer" type="button">Pause timer</button><button id="resetTimer" type="button">Reset timer</button></div>
      <div class="button-row"><button id="previousSlide" type="button">Previous</button><button id="nextSlide" type="button">Next</button></div>
      <div id="counter" role="status" aria-live="polite" aria-atomic="true"></div>
    </section>
  </main>
  <script>
    (() => {
      let connection = null;
      let currentState = null;
      let elapsedMs = 0;
      let timerStartedAt = null;
      let timerInterval = null;
      let previewSequence = 0;

      const singleIdReferenceAttributes = new Set([
        'aria-activedescendant', 'aria-details', 'aria-errormessage', 'for', 'form', 'list'
      ]);
      const listIdReferenceAttributes = new Set([
        'aria-controls', 'aria-describedby', 'aria-flowto', 'aria-labelledby', 'aria-owns', 'headers'
      ]);
      const urlIdReferenceAttributes = new Set([
        'clip-path', 'cursor', 'fill', 'filter', 'marker-end', 'marker-mid', 'marker-start', 'mask', 'stroke'
      ]);

      const timer = document.getElementById('timer');
      const formatTime = (milliseconds) => {
        const totalSeconds = Math.floor(milliseconds / 1000);
        const hours = Math.floor(totalSeconds / 3600);
        const minutes = Math.floor((totalSeconds % 3600) / 60);
        const seconds = totalSeconds % 60;
        return [hours, minutes, seconds].map((value) => String(value).padStart(2, '0')).join(':');
      };
      const drawTimer = () => { timer.textContent = formatTime(elapsedMs); };
      const tickTimer = () => {
        if (timerStartedAt === null) return;
        elapsedMs = Date.now() - timerStartedAt;
        drawTimer();
      };
      const startTimer = () => {
        if (timerInterval !== null) return;
        timerStartedAt = Date.now() - elapsedMs;
        timerInterval = window.setInterval(tickTimer, 250);
        tickTimer();
      };
      const pauseTimer = () => {
        if (timerInterval === null) return;
        tickTimer();
        window.clearInterval(timerInterval);
        timerInterval = null;
        timerStartedAt = null;
      };
      const resetTimer = () => {
        pauseTimer();
        elapsedMs = 0;
        drawTimer();
      };

      function copyCanvasSnapshots(source, clone) {
        source.querySelectorAll('canvas').forEach((canvas, index) => {
          const copy = clone.querySelectorAll('canvas')[index];
          if (!copy) return;
          try {
            const image = document.createElement('img');
            image.src = canvas.toDataURL('image/png');
            image.alt = canvas.getAttribute('aria-label') || 'Chart preview';
            copy.replaceWith(image);
          } catch (error) {
            console.warn('Chart preview could not be captured.', error);
          }
        });
      }

      function rewriteUrlReferences(value, idMap) {
        return value.replace(/url\\(\\s*#([A-Za-z_][\\w:.-]*)\\s*\\)/g, (match, id) => {
          const replacement = idMap.get(id);
          return replacement ? 'url(#' + replacement + ')' : match;
        });
      }

      function rewriteHashReferences(value, idMap) {
        return value.replace(/(^|[^\\w-])#([A-Za-z_][\\w:.-]*)/g, (match, prefix, id) => {
          const replacement = idMap.get(id);
          return replacement ? prefix + '#' + replacement : match;
        });
      }

      function namespaceCloneIds(clone) {
        const namespace = 'presenter-preview-' + (++previewSequence);
        const idMap = new Map();
        const elements = [clone, ...clone.querySelectorAll('*')];

        elements.forEach((element) => {
          if (!element.id) return;
          const replacement = namespace + '-' + element.id;
          idMap.set(element.id, replacement);
          element.id = replacement;
        });
        return { idMap, namespace };
      }

      function rewriteCloneReferences(clone, idMap) {
        [clone, ...clone.querySelectorAll('*')].forEach((element) => {
          if (element.tagName === 'STYLE') {
            const styleText = element.textContent || '';
            const replacement = rewriteHashReferences(rewriteUrlReferences(styleText, idMap), idMap);
            if (replacement !== styleText) element.textContent = replacement;
          }
          [...element.attributes].forEach((attribute) => {
            const name = attribute.name.toLowerCase();
            const value = attribute.value;
            let replacement = value;
            if (listIdReferenceAttributes.has(name)) {
              replacement = value.split(/\\s+/).map((id) => idMap.get(id) || id).join(' ');
            } else if (singleIdReferenceAttributes.has(name)) {
              replacement = idMap.get(value) || value;
            } else if ((name === 'href' || name === 'xlink:href') && value.startsWith('#')) {
              replacement = '#' + (idMap.get(value.slice(1)) || value.slice(1));
            } else if (name === 'style') {
              replacement = rewriteHashReferences(value, idMap);
            }
            if (urlIdReferenceAttributes.has(name) || name === 'style') {
              replacement = rewriteUrlReferences(replacement, idMap);
            }
            if (replacement !== value) element.setAttribute(attribute.name, replacement);
          });
        });
      }

      function copyGlobalIdStyles(sourceSlide, clone, idMap, namespace) {
        if (!idMap.size) return;
        const copiedRules = [];
        for (const styleSheet of sourceSlide.ownerDocument.styleSheets) {
          if (styleSheet.ownerNode && sourceSlide.contains(styleSheet.ownerNode)) continue;
          try {
            for (const rule of styleSheet.cssRules) {
              const original = rule.cssText;
              const rewritten = rewriteHashReferences(rewriteUrlReferences(original, idMap), idMap);
              if (rewritten !== original) copiedRules.push(rewritten);
            }
          } catch (error) {
            // Cross-origin stylesheet text is not available. Its unchanged copy remains in the presenter head.
          }
        }
        if (!copiedRules.length) return;
        const style = document.createElement('style');
        const scope = '[data-presenter-preview-scope="' + namespace + '"]';
        style.setAttribute('data-presenter-preview-id-styles', '');
        style.textContent = '@scope (' + scope + ') {' + copiedRules.join('\\n') + '}';
        clone.prepend(style);
      }

      function scopeCloneStyles(clone, namespace) {
        const scope = '[data-presenter-preview-scope="' + namespace + '"]';
        clone.querySelectorAll('style').forEach((style) => {
          style.textContent = '@scope (' + scope + ') {' + style.textContent + '}';
        });
      }

      function renderPreview(frame, sourceSlide) {
        frame.replaceChildren();
        if (!sourceSlide) {
          frame.innerHTML = '<div class="preview-empty">End of presentation</div>';
          return;
        }
        const clone = sourceSlide.cloneNode(true);
        const { idMap, namespace } = namespaceCloneIds(clone);
        rewriteCloneReferences(clone, idMap);
        clone.classList.remove('inactive');
        clone.classList.add('active');
        clone.setAttribute('inert', '');
        clone.setAttribute('aria-hidden', 'true');
        frame.setAttribute('data-presenter-preview-scope', namespace);
        scopeCloneStyles(clone, namespace);
        copyCanvasSnapshots(sourceSlide, clone);
        copyGlobalIdStyles(sourceSlide, clone, idMap, namespace);
        frame.append(clone);
        const bounds = sourceSlide.getBoundingClientRect();
        const scale = frame.clientWidth / Math.max(bounds.width, 1);
        clone.style.width = bounds.width + 'px';
        clone.style.height = bounds.height + 'px';
        clone.style.transform = 'scale(' + scale + ')';
        frame.style.height = Math.max(1, bounds.height * scale) + 'px';
      }

      function renderPreviews() {
        if (!currentState) return;
        renderPreview(document.getElementById('currentPreview'), currentState.slides[currentState.index]);
        renderPreview(document.getElementById('nextPreview'), currentState.slides[currentState.index + 1]);
      }

      function render(state) {
        currentState = state;
        renderPreviews();
        document.getElementById('notes').textContent = state.notes[state.index] || 'No notes for this slide.';
        document.getElementById('counter').textContent = 'Slide ' + (state.index + 1) + ' of ' + state.slides.length;
        document.getElementById('previousSlide').disabled = state.index === 0;
        document.getElementById('nextSlide').disabled = state.index >= state.slides.length - 1;
      }

      document.getElementById('startTimer').addEventListener('click', startTimer);
      document.getElementById('pauseTimer').addEventListener('click', pauseTimer);
      document.getElementById('resetTimer').addEventListener('click', resetTimer);
      document.getElementById('previousSlide').addEventListener('click', () => connection?.goTo(currentState.index - 1));
      document.getElementById('nextSlide').addEventListener('click', () => connection?.goTo(currentState.index + 1));
      window.addEventListener('resize', renderPreviews);
      document.addEventListener('keydown', (event) => {
        if (event.target instanceof Element && event.target.matches('button, input, select, textarea, a[href]')) return;
        if (event.key === 'ArrowLeft' || event.key === 'PageUp') {
          event.preventDefault();
          connection?.goTo(currentState.index - 1);
        } else if (event.key === 'ArrowRight' || event.key === 'PageDown' || event.key === ' ') {
          event.preventDefault();
          connection?.goTo(currentState.index + 1);
        }
      });
      window.addEventListener('beforeunload', () => {
        if (timerInterval !== null) window.clearInterval(timerInterval);
      });

      window.slideSagePresenter = {
        connect(nextConnection) { connection = nextConnection; },
        render
      };
      window.opener?.__slideSagePresenterReady?.();
    })();
  <\/script>
</body>
</html>`;
}

function installPresenterMode() {
  let presentation = null;
  let popup = null;

  const sendState = () => {
    if (!presentation || !popup || popup.closed) return;
    popup.slideSagePresenter?.render({
      index: presentation.currentSlide,
      slides: presentation.slides,
      notes: readSpeakerNotes(presentation.totalSlides)
    });
  };

  window.openSlideSagePresenter = (instance) => {
    presentation = instance;
    if (popup && !popup.closed) {
      popup.focus();
      sendState();
      return;
    }

    popup = window.open('', 'slide-sage-presenter', 'popup,width=1280,height=800');
    if (!popup) {
      console.warn('Presenter window was blocked by the browser. Allow popups and press P again.');
      return;
    }
    const connectPresenter = () => {
      const presenter = popup?.slideSagePresenter;
      if (!presenter || !presentation) return false;
      presenter.connect({ goTo: (index) => presentation.goTo(index) });
      sendState();
      delete window.__slideSagePresenterReady;
      return true;
    };
    window.__slideSagePresenterReady = connectPresenter;
    popup.document.open();
    popup.document.write(createPresenterDocument(sourceStyleMarkup()));
    popup.document.close();
    if (popup.document.readyState === 'complete') connectPresenter();
  };

  document.addEventListener('slidechange', sendState);
}

document.addEventListener('DOMContentLoaded', installPresenterMode);
```

The presenter calls the canonical `goTo(index)` method. It does not rely on deprecated `navigate()` or nonexistent `goToSlide()` methods. Current and next previews are real cloned slide markup, and canvas charts are replaced with an image snapshot so a clone does not appear blank. Preview clones are inert and hidden from assistive technology. Their IDs, ARIA references, SVG references, and applicable source CSS rules are namespaced for each preview.

## Verification

1. Open a deck with a JSON notes block and press `P`.
2. Navigate in either window. Confirm the other view updates, including next-slide preview and notes.
3. Start, pause, reset, and restart the timer. It uses one guarded `setInterval` and calculates elapsed time from `Date.now()`.
4. Open the shared HTML source and verify that notes are expected to be readable before sharing it.
