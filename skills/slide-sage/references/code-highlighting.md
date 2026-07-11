# Code Highlighting Reference (Prism.js)

## Setup

### CDN URLs (pinned versions)

```html
<!-- Core -->
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/prism.min.js" integrity="sha384-Cn/s7dpCMIb2rgIjtCYcpcv3LPJjUciybJ5G/sGMK025lFiqdJ4pRgUEgIcolGuJ" crossorigin="anonymous"></script>

<!-- Theme: Tomorrow Night -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/themes/prism-tomorrow.min.css" integrity="sha384-wFjoQjtV1y5jVHbt0p35Ui8aV8GVpEZkyF99OXWqP/eNJDU93D3Ugxkoyh6Y2I4A" crossorigin="anonymous">
```

### Language Grammars (load after core)

```html
<!-- JavaScript -->
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/components/prism-javascript.min.js" integrity="sha384-D44bgYYKvaiDh4cOGlj1dbSDpSctn2FSUj118HZGmZEShZcO2v//Q5vvhNy206pp" crossorigin="anonymous"></script>

<!-- TypeScript -->
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/components/prism-typescript.min.js" integrity="sha384-PeOqKNW/piETaCg8rqKFy+Pm6KEk7e36/5YZE5XO/OaFdO+/Aw3O8qZ9qDPKVUgx" crossorigin="anonymous"></script>

<!-- Python -->
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/components/prism-python.min.js" integrity="sha384-WJdEkJKrbsqw0evQ4GB6mlsKe5cGTxBOw4KAEIa52ZLB7DDpliGkwdme/HMa5n1m" crossorigin="anonymous"></script>

<!-- HTML / Markup (included in core, but explicit load available) -->
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/components/prism-markup.min.js" integrity="sha384-HkMr0bZB9kBW4iVtXn6nd35kO/L/dQtkkUBkL9swzTEDMdIe5ExJChVDSnC79aNA" crossorigin="anonymous"></script>

<!-- CSS -->
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/components/prism-css.min.js" integrity="sha384-0mV13Neu0xhJFylI+HV43C+XiR13bGSeL7D0/7e6hK7sJgvyvK6HVjeQwmvXTstY" crossorigin="anonymous"></script>

<!-- JSON -->
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/components/prism-json.min.js" integrity="sha384-RhrmFFMb0ZCHImjFMpR/UE3VEtIVTCtNrtKQqXCzqXZNJala02N3UbVhi+qzw3CY" crossorigin="anonymous"></script>

<!-- Bash / Shell -->
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/components/prism-bash.min.js" integrity="sha384-9WmlN8ABpoFSSHvBGGjhvB3E/D8UkNB9HpLJjBQFC2VSQsM1odiQDv4NbEo+7l15" crossorigin="anonymous"></script>

<!-- SQL -->
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/components/prism-sql.min.js" integrity="sha384-/MKWdycCDliku23mP5sYXbZNuXrzgmQO/jsVxwPFn99dVOaXRyKsqDjarqpueGAp" crossorigin="anonymous"></script>

<!-- YAML -->
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/components/prism-yaml.min.js" integrity="sha384-AKAiycghK0jDCjD+aavMHzDkLzRR7Yzcwh3+xL/295cvyVMe+cxQfyQC8xxGGcI8" crossorigin="anonymous"></script>

<!-- Java -->
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/components/prism-java.min.js" integrity="sha384-DioAMZB4yk91W6LuFit5wJDh8c5Ov09f/MBvja94y0PodMqTpTZeBeejqpRUru7D" crossorigin="anonymous"></script>

<!-- Go -->
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/components/prism-go.min.js" integrity="sha384-YxCco6ByOY5rJ3jD18514fa8w5so07zigIyV6tZa3CWSE5vYrbDSuFkZ5zOknnZ6" crossorigin="anonymous"></script>

<!-- Rust -->
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/components/prism-rust.min.js" integrity="sha384-JyDgFjMbyrE/TGiEUSXW3CLjQOySrsoiUNAlXTFdIsr/XUfaB7E+eYlR+tGQ9bCO" crossorigin="anonymous"></script>

<!-- C -->
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/components/prism-c.min.js" integrity="sha384-gaD4ncierlmWk42Z3BmTp37/z+Dqt8V4Wf74UjTvFeo+M+SgnEI6Ysd98pWhksQv" crossorigin="anonymous"></script>

<!-- C++ (depends on C) -->
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/components/prism-cpp.min.js" integrity="sha384-NiOrAquf32LSG3Vuig99LKS03EZPUuM8a51NOp+XXsqx08hUVo3wbNWALY7K/2J8" crossorigin="anonymous"></script>

<!-- Ruby -->
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/components/prism-ruby.min.js" integrity="sha384-xVcnao4LK2LGPWtbEMXzbqrmtM8Ycfrz6nH7gthLCLwCrQGhNFScUV7UGjDotjVu" crossorigin="anonymous"></script>

<!-- PHP -->
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/components/prism-php.min.js" integrity="sha384-+grZ1BKjM0uVvu5qwWIjfNJct1eZpnnIv7QAo1Qva9uEWA584H7dSk7sZSgwbvT7" crossorigin="anonymous"></script>
```

**Note**: C++ (`prism-cpp`) depends on C (`prism-c`). Load C first.

---

## HTML Structure

```html
<pre class="code-block"><code class="language-python">
def hello():
    print("Hello, World!")
</code></pre>
```

- The `language-*` class on `<code>` tells Prism which grammar to apply.
- Content inside `<code>` must be HTML-escaped (`<` as `&lt;`, `>` as `&gt;`, `&` as `&amp;`).
- Keep code to **10-12 visible lines max** per slide for readability.

---

## Dark Theme CSS (Custom - One Dark Pro / Tomorrow Night inspired)

```css
/* === Slide-Sage Dark Code Theme === */

pre.code-block {
  background: color-mix(in srgb, var(--color-bg-primary) 82%, #000000);
  color: var(--color-text-primary);
}

pre.code-block code {
  color: inherit;
  text-shadow: none;
}

/* Comments */
.token.comment,
.token.prolog,
.token.doctype,
.token.cdata {
  color: #6a6a8a;
  font-style: italic;
}

/* Punctuation */
.token.punctuation {
  color: #abb2bf;
}

/* Namespaces */
.token.namespace {
  opacity: 0.8;
}

/* Keywords */
.token.keyword,
.token.tag,
.token.boolean,
.token.constant,
.token.deleted {
  color: #c678dd;
}

/* Strings */
.token.string,
.token.char,
.token.attr-value,
.token.inserted {
  color: #98c379;
}

/* Template strings / interpolation */
.token.template-string,
.token.template-punctuation {
  color: #98c379;
}

/* Functions */
.token.function,
.token.class-name {
  color: #61afef;
}

/* Numbers */
.token.number {
  color: #d19a66;
}

/* Operators */
.token.operator,
.token.entity,
.token.url {
  color: #56b6c2;
}

/* Variables */
.token.variable,
.token.property {
  color: #e06c75;
}

/* Selectors (CSS), Symbols (Ruby), Important */
.token.selector,
.token.symbol,
.token.important {
  color: #c678dd;
}

/* Attribute names (HTML) */
.token.attr-name {
  color: #d19a66;
}

/* Regex */
.token.regex {
  color: #56b6c2;
}

/* Built-in / Builtin */
.token.builtin {
  color: #e5c07b;
}

/* Annotations / Decorators */
.token.annotation,
.token.decorator {
  color: #d19a66;
}

/* Bold / Italic tokens */
.token.bold {
  font-weight: bold;
}
.token.italic {
  font-style: italic;
}

/* Selection */
pre.code-block::selection,
pre.code-block ::selection {
  background: rgba(97, 175, 239, 0.25);
}
```

---

## Light Theme CSS

Named light presets already set `data-mode="light"` on `<html>`. Do not add a separate `.light-theme` class.

```css
/* === Slide-Sage Light Code Theme === */

html[data-mode="light"] pre.code-block {
  background: #fafafa;
  color: #383a42;
}

html[data-mode="light"] pre.code-block code {
  color: #383a42;
  text-shadow: none;
}

/* Comments */
html[data-mode="light"] .token.comment,
html[data-mode="light"] .token.prolog,
html[data-mode="light"] .token.doctype,
html[data-mode="light"] .token.cdata {
  color: #a0a1a7;
  font-style: italic;
}

/* Punctuation */
html[data-mode="light"] .token.punctuation {
  color: #383a42;
}

/* Namespaces */
html[data-mode="light"] .token.namespace {
  opacity: 0.8;
}

/* Keywords */
html[data-mode="light"] .token.keyword,
html[data-mode="light"] .token.tag,
html[data-mode="light"] .token.boolean,
html[data-mode="light"] .token.constant,
html[data-mode="light"] .token.deleted {
  color: #a626a4;
}

/* Strings */
html[data-mode="light"] .token.string,
html[data-mode="light"] .token.char,
html[data-mode="light"] .token.attr-value,
html[data-mode="light"] .token.inserted {
  color: #50a14f;
}

/* Template strings */
html[data-mode="light"] .token.template-string,
html[data-mode="light"] .token.template-punctuation {
  color: #50a14f;
}

/* Functions */
html[data-mode="light"] .token.function,
html[data-mode="light"] .token.class-name {
  color: #4078f2;
}

/* Numbers */
html[data-mode="light"] .token.number {
  color: #986801;
}

/* Operators */
html[data-mode="light"] .token.operator,
html[data-mode="light"] .token.entity,
html[data-mode="light"] .token.url {
  color: #0184bc;
}

/* Variables */
html[data-mode="light"] .token.variable,
html[data-mode="light"] .token.property {
  color: #e45649;
}

/* Selectors, Symbols, Important */
html[data-mode="light"] .token.selector,
html[data-mode="light"] .token.symbol,
html[data-mode="light"] .token.important {
  color: #a626a4;
}

/* Attribute names */
html[data-mode="light"] .token.attr-name {
  color: #986801;
}

/* Regex */
html[data-mode="light"] .token.regex {
  color: #0184bc;
}

/* Built-in */
html[data-mode="light"] .token.builtin {
  color: #c18401;
}

/* Annotations / Decorators */
html[data-mode="light"] .token.annotation,
html[data-mode="light"] .token.decorator {
  color: #986801;
}

/* Bold / Italic tokens */
html[data-mode="light"] .token.bold {
  font-weight: bold;
}
html[data-mode="light"] .token.italic {
  font-style: italic;
}

/* Selection */
html[data-mode="light"] pre.code-block::selection,
html[data-mode="light"] pre.code-block ::selection {
  background: rgba(64, 120, 242, 0.2);
}
```

---

## Code Slide Layout

```html
<div class="slide">
  <div class="slide-content">
    <h2>API Endpoint</h2>
    <pre class="code-block"><code class="language-javascript">
// max 10-12 visible lines
const app = express();

app.get('/api/users', async (req, res) => {
  const users = await db.query('SELECT * FROM users');
  res.json(users);
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
    </code></pre>
  </div>
</div>
```

---

## Code Block Styling

```css
.code-block {
  border-radius: var(--radius, 8px);
  padding: clamp(0.8rem, 1.5vw, 1.5rem);
  font-size: clamp(0.65rem, 1.2vw, 0.95rem);
  line-height: 1.6;
  max-height: min(55vh, 400px);
  overflow: hidden; /* never scroll within a slide */
  font-family: 'Fira Code', 'JetBrains Mono', 'Source Code Pro', monospace;
  margin: 0;
  tab-size: 2;
  -moz-tab-size: 2;
  white-space: pre;
  word-wrap: normal;
  word-break: normal;
  border: 1px solid var(--color-border);
}

.code-block code {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
  display: block;
  overflow: hidden;
}
```

---

## Monospace Font Loading

```html
<link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
```

Fallback stack: `'Fira Code', 'JetBrains Mono', 'Source Code Pro', 'Cascadia Code', 'Consolas', 'Monaco', monospace`

---

## Line Numbers (Optional Plugin)

### CDN

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/plugins/line-numbers/prism-line-numbers.min.css" integrity="sha384-nUkTNLI8COlMCRJ0FHIdX76If83145OTCLUx4gQyfnO0gGeO/sD9czGEUBxtkcUv" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/plugins/line-numbers/prism-line-numbers.min.js" integrity="sha384-6QJu8apxMmB9TiPVWzYKF5pRgKcz7snO0/QU+MrWmgBLECQjoa6erxX2VQ5t41Jd" crossorigin="anonymous"></script>
```

### Usage

Add the `line-numbers` class to the `<pre>` element:

```html
<pre class="code-block line-numbers"><code class="language-python">
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
</code></pre>
```

### Styling

```css
pre.code-block.line-numbers {
  padding-left: 3.5em;
  counter-reset: linenumber;
}

.line-numbers .line-numbers-rows {
  border-right: 1px solid var(--color-border);
  padding-right: 0.8em;
}

.line-numbers .line-numbers-rows > span::before {
  color: var(--color-text-muted);
  font-size: 0.85em;
}
```

---

## Line Highlight (Optional Plugin)

### CDN

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/plugins/line-highlight/prism-line-highlight.min.css" integrity="sha384-bCq+nBO5hUxeJTxGcpLbGAP5hqUhRUl9xclGVWMifyWonUxPS1+fO1JzOplEJsLP" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/plugins/line-highlight/prism-line-highlight.min.js" integrity="sha384-aA5pbfEm+kZPOE/CKuBywvgtAzs4ZrQPlTwexPyFEwQ96E9rTPN1B0ObNmCn9tgH" crossorigin="anonymous"></script>
```

### Usage

Use the `data-line` attribute on `<pre>` to highlight specific lines:

```html
<!-- Highlight line 3 and lines 5-7 -->
<pre class="code-block" data-line="3,5-7"><code class="language-javascript">
const express = require('express');
const app = express();
const PORT = 3000; // highlighted

app.get('/', (req, res) => { // highlighted
  res.send('Hello!');         // highlighted
});                           // highlighted

app.listen(PORT);
</code></pre>
```

### Styling

```css
pre[data-line] {
  position: relative;
}

.line-highlight {
  background: color-mix(in srgb, var(--color-accent) 12%, transparent);
  border-left: 3px solid var(--color-accent);
  margin-left: -1.5rem;
  padding-left: calc(1.5rem - 3px);
}
```

---

## Copy Button (Vanilla JS)

```javascript
document.querySelectorAll('.code-block').forEach(block => {
  const btn = document.createElement('button');
  btn.className = 'copy-btn';
  btn.textContent = 'Copy';
  btn.onclick = () => {
    navigator.clipboard.writeText(block.querySelector('code').textContent).then(() => {
      btn.textContent = 'Copied!';
      setTimeout(() => btn.textContent = 'Copy', 2000);
    });
  };
  block.style.position = 'relative';
  block.appendChild(btn);
});
```

### Copy Button Styling

```css
.copy-btn {
  position: absolute;
  top: 8px;
  right: 8px;
  background: color-mix(in srgb, var(--color-text) 10%, transparent);
  border: 1px solid color-mix(in srgb, var(--color-text) 20%, transparent);
  color: var(--color-text-secondary);
  border-radius: 4px;
  padding: 4px 10px;
  font-size: 0.75rem;
  cursor: pointer;
  transition: all 0.2s;
  z-index: 2;
  font-family: inherit;
}

.copy-btn:hover {
  background: color-mix(in srgb, var(--color-text) 20%, transparent);
  color: var(--color-text);
}
```

---

## Diff Highlighting Pattern

For showing code changes with added/removed lines:

```css
.line-added {
  background: rgba(80, 200, 120, 0.15);
  display: block;
}

.line-removed {
  background: rgba(224, 108, 117, 0.15);
  text-decoration: line-through;
  display: block;
  opacity: 0.7;
}

```

### Usage in HTML

```html
<pre class="code-block"><code class="language-javascript">
function greet(name) {
<span class="line-removed">  console.log("Hello " + name);</span>
<span class="line-added">  console.log(`Hello, ${name}!`);</span>
}
</code></pre>
```

---

## Integration with Presentation Theme

Code block backgrounds should complement the slide background. Use CSS custom properties from the slide-sage style system:

```css
.code-block {
  background: var(--code-bg, color-mix(in srgb, var(--color-bg-primary) 82%, #000000));
  color: var(--code-fg, var(--color-text-primary));
  border: 1px solid var(--code-border, var(--color-border));
}
```

### Complete Script Loading Order

```html
<!-- 1. Font -->
<link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">

<!-- 2. Prism theme (base, will be overridden by inline CSS) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/themes/prism-tomorrow.min.css" integrity="sha384-wFjoQjtV1y5jVHbt0p35Ui8aV8GVpEZkyF99OXWqP/eNJDU93D3Ugxkoyh6Y2I4A" crossorigin="anonymous">

<!-- 3. Optional plugin CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/plugins/line-numbers/prism-line-numbers.min.css" integrity="sha384-nUkTNLI8COlMCRJ0FHIdX76If83145OTCLUx4gQyfnO0gGeO/sD9czGEUBxtkcUv" crossorigin="anonymous">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/plugins/line-highlight/prism-line-highlight.min.css" integrity="sha384-bCq+nBO5hUxeJTxGcpLbGAP5hqUhRUl9xclGVWMifyWonUxPS1+fO1JzOplEJsLP" crossorigin="anonymous">

<!-- 4. Inline theme overrides (dark/light from above) -->
<style>/* ... custom theme CSS ... */</style>

<!-- 5. Prism core (at end of body) -->
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/prism.min.js" integrity="sha384-Cn/s7dpCMIb2rgIjtCYcpcv3LPJjUciybJ5G/sGMK025lFiqdJ4pRgUEgIcolGuJ" crossorigin="anonymous"></script>

<!-- 6. Language grammars (only those needed) -->
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/components/prism-python.min.js" integrity="sha384-WJdEkJKrbsqw0evQ4GB6mlsKe5cGTxBOw4KAEIa52ZLB7DDpliGkwdme/HMa5n1m" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/components/prism-javascript.min.js" integrity="sha384-D44bgYYKvaiDh4cOGlj1dbSDpSctn2FSUj118HZGmZEShZcO2v//Q5vvhNy206pp" crossorigin="anonymous"></script>

<!-- 7. Optional plugins -->
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/plugins/line-numbers/prism-line-numbers.min.js" integrity="sha384-6QJu8apxMmB9TiPVWzYKF5pRgKcz7snO0/QU+MrWmgBLECQjoa6erxX2VQ5t41Jd" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.30.0/plugins/line-highlight/prism-line-highlight.min.js" integrity="sha384-aA5pbfEm+kZPOE/CKuBywvgtAzs4ZrQPlTwexPyFEwQ96E9rTPN1B0ObNmCn9tgH" crossorigin="anonymous"></script>

<!-- 8. Copy button script -->
<script>/* ... copy button JS from above ... */</script>
```

---

## Mandatory Initialization

**CRITICAL**: Prism.js does NOT auto-highlight in all contexts. Always call `Prism.highlightAll()` after the DOM is ready:

```javascript
document.addEventListener('DOMContentLoaded', () => {
  if (typeof Prism !== 'undefined') {
    Prism.highlightAll();
  }
});
```

This must go in the presentation's `<script>` block, AFTER the Prism.js CDN scripts.

### Common Mistakes

| Mistake | Fix |
|---------|-----|
| `<code>` without `language-*` class | Always add `class="language-python"` (or appropriate language) |
| Code not highlighted (monochrome) | Check that `Prism.highlightAll()` is called after DOM load |
| Using `<pre><code>` without `.code-block` on `<pre>` | Always use `<pre class="code-block"><code class="language-xxx">` |
| Inline code snippets in a code block | Use `<code class="inline-code">` for short inline references |

---

## Inline Code Styling

For short code references within slide text (e.g., function names, variable names, API endpoints), use the `.inline-code` class instead of a full code block:

```html
<p>The <code class="inline-code">FallbackModel</code> wraps both providers:</p>
<p>Set <code class="inline-code">previous_response_id: 'auto'</code> for caching.</p>
```

**Never** place a multi-line code block below content cards or comparison layouts - if code is needed alongside a comparison, put it on the next slide.

---

## Manual Syntax Classes (Domain-Specific Pseudo-Code)

For content Prism.js cannot tokenize - HTTP endpoints, file trees, data flow diagrams, config snippets - use manual CSS helper classes. These complement Prism.js (Tier 1) as a lighter-weight Tier 2 approach.

### Dark Theme CSS

```css
/* === Manual Syntax Highlighting (One Dark Pro palette) === */
.syn-kw     { color: #c678dd; }                          /* keywords */
.syn-fn     { color: #61afef; }                          /* function names */
.syn-str    { color: #98c379; }                          /* strings */
.syn-num    { color: #d19a66; }                          /* numbers */
.syn-cm     { color: #6a6a8a; font-style: italic; }     /* comments */
.syn-method { color: #e5c07b; }                          /* method/builtin names */
.syn-verb   { color: #98c379; font-weight: 600; }       /* HTTP verbs */
.syn-path   { color: #d19a66; }                          /* file paths, URLs */
.syn-param  { color: #56b6c2; }                          /* parameters */
```

### Light Theme CSS

```css
html[data-mode="light"] .syn-kw     { color: #a626a4; }
html[data-mode="light"] .syn-fn     { color: #4078f2; }
html[data-mode="light"] .syn-str    { color: #50a14f; }
html[data-mode="light"] .syn-num    { color: #986801; }
html[data-mode="light"] .syn-cm     { color: #a0a1a7; font-style: italic; }
html[data-mode="light"] .syn-method { color: #c18401; }
html[data-mode="light"] .syn-verb   { color: #50a14f; font-weight: 600; }
html[data-mode="light"] .syn-path   { color: #986801; }
html[data-mode="light"] .syn-param  { color: #0184bc; }
```

### Usage Examples

**HTTP endpoints:**

```html
<pre class="code-block"><span class="syn-verb">POST</span> <span class="syn-path">/api/v1/chat/send</span>  <span class="syn-cm">SSE stream</span>
<span class="syn-verb">GET</span>  <span class="syn-path">/api/v1/health</span>      <span class="syn-cm">K8s probe</span>
<span class="syn-verb">PUT</span>  <span class="syn-path">/api/v1/config/:id</span>  <span class="syn-cm">Update config</span></pre>
```

**File/directory tree:**

```html
<pre class="code-block"><span class="syn-path">src/</span>
├── <span class="syn-path">api/</span>       <span class="syn-cm"># HTTP routes</span>
├── <span class="syn-path">agent/</span>     <span class="syn-cm"># Agent logic</span>
├── <span class="syn-path">models/</span>    <span class="syn-cm"># Data models</span>
└── <span class="syn-path">utils/</span>     <span class="syn-cm"># Shared helpers</span></pre>
```

**Data flow pseudo-code:**

```html
<pre class="code-block"><span class="syn-kw">INPUT</span>  <span class="syn-path">user_query</span>
  <span class="syn-fn">embed</span>(<span class="syn-param">query</span>) → <span class="syn-num">768d</span> vector
  <span class="syn-fn">search</span>(<span class="syn-param">index</span>, <span class="syn-param">top_k</span>=<span class="syn-num">10</span>)
  <span class="syn-fn">rerank</span>(<span class="syn-param">results</span>)
<span class="syn-kw">OUTPUT</span> <span class="syn-path">ranked_candidates</span></pre>
```

### When to Use Prism.js vs Manual `.syn-*`

| Content | Approach | Example |
|---------|----------|---------|
| Python, JS, TypeScript, Go, Rust | Prism.js | `class="language-python"` |
| SQL queries | Prism.js | `class="language-sql"` |
| Bash/shell commands | Prism.js | `class="language-bash"` |
| YAML/JSON config | Prism.js | `class="language-yaml"` |
| HTTP endpoints | Manual `.syn-*` | `.syn-verb` + `.syn-path` |
| File/directory trees | Manual `.syn-*` | `.syn-path` + `.syn-cm` |
| Data flow pseudo-code | Manual `.syn-*` | `.syn-kw` + `.syn-fn` |
| Architecture labels | Manual `.syn-*` | `.syn-kw` for section names |
| Plain text diagrams | Manual `.syn-*` | `.syn-kw` for labels |

**Rule of thumb:** If Prism.js has a grammar for the language, use Prism.js. For everything else, use `.syn-*` classes.
