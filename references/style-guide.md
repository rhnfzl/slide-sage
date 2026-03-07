# Slide-Sage Style Guide

Three-tier style system for data visualization presentations.

---

## Tier 1: Data-Viz-First Palettes

### Categorical Palette (8 Colors, Colorblind-Safe)

Tested against deuteranopia, protanopia, and tritanopia. Derived from research-backed approaches (Wong 2011, Okabe-Ito conventions) with custom adjustments for screen projection.

| Index | Name        | Hex       | CSS Variable             | Usage                    |
|-------|-------------|-----------|--------------------------|--------------------------|
| 1     | Cerulean    | `#0077BB` | `--cat-1`                | Primary series           |
| 2     | Vermillion  | `#CC3311` | `--cat-2`                | Secondary series         |
| 3     | Teal        | `#009988` | `--cat-3`                | Tertiary series          |
| 4     | Tangerine   | `#EE7733` | `--cat-4`                | Fourth series            |
| 5     | Indigo      | `#3344AA` | `--cat-5`                | Fifth series             |
| 6     | Magenta     | `#EE3377` | `--cat-6`                | Sixth series             |
| 7     | Sand        | `#BBAA33` | `--cat-7`                | Seventh series           |
| 8     | Gray        | `#888888` | `--cat-8`                | Eighth / neutral series  |

```css
:root {
  --cat-1: #0077BB;
  --cat-2: #CC3311;
  --cat-3: #009988;
  --cat-4: #EE7733;
  --cat-5: #3344AA;
  --cat-6: #EE3377;
  --cat-7: #BBAA33;
  --cat-8: #888888;
}
```

**Colorblind simulation notes:**
- Deuteranopia: All 8 remain distinguishable. Cerulean/Indigo separate by lightness; Vermillion/Tangerine separate by saturation.
- Protanopia: Teal stays distinct from blues; Vermillion shifts to dark gold but separates from Sand by lightness.
- Tritanopia: Magenta and Vermillion remain distinct; Teal separates from Cerulean by warmth shift.

### Sequential Palettes

5 steps from lightest to darkest for heatmaps and gradients.

**Blue sequence:**
```css
:root {
  --seq-blue-1: #D4E8F7;
  --seq-blue-2: #8FC2E4;
  --seq-blue-3: #4A9ACE;
  --seq-blue-4: #1B6FAA;
  --seq-blue-5: #0A3D6B;
}
```

**Green sequence:**
```css
:root {
  --seq-green-1: #D5ECD4;
  --seq-green-2: #8DC98B;
  --seq-green-3: #4BA54A;
  --seq-green-4: #257A25;
  --seq-green-5: #0D4F12;
}
```

**Amber sequence:**
```css
:root {
  --seq-amber-1: #FDF0D5;
  --seq-amber-2: #F5CE6E;
  --seq-amber-3: #E5A822;
  --seq-amber-4: #B47D0A;
  --seq-amber-5: #6E4C04;
}
```

### Diverging Palettes

7 steps with a neutral midpoint for comparison and deviation data.

**Teal-to-Coral:**
```css
:root {
  --div-tc-1: #00736E;
  --div-tc-2: #3FA39A;
  --div-tc-3: #8DD0C7;
  --div-tc-4: #F0F0F0; /* neutral midpoint */
  --div-tc-5: #F4A582;
  --div-tc-6: #D65F4A;
  --div-tc-7: #A12A1A;
}
```

**Blue-to-Orange:**
```css
:root {
  --div-bo-1: #1A4E8A;
  --div-bo-2: #4D8AC4;
  --div-bo-3: #9CC3E0;
  --div-bo-4: #F5F5F0; /* neutral midpoint */
  --div-bo-5: #FBD08E;
  --div-bo-6: #E8913A;
  --div-bo-7: #B55A11;
}
```

### Chart-Specific Assignments

```css
:root {
  /* Semantic chart colors */
  --chart-positive: #2A9D5C;    /* Growth, increase, success */
  --chart-negative: #CC3311;    /* Decline, decrease, loss */
  --chart-neutral: #888888;     /* Baseline, unchanged */
  --chart-highlight: #EE7733;   /* Callout, annotation, focus */
}
```

---

## Tier 2: Aesthetic + Data Harmony (6 Named Presets)

### 1. Arctic Dawn

Cool blues and teals on white/near-white. Clean scientific feel.

```css
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Inter+Tight:wght@300;400;500;600&display=swap');

[data-theme="arctic-dawn"] {
  /* --- Light Mode (default) --- */
  --color-bg-primary: #FAFCFE;
  --color-bg-secondary: #EDF3F8;
  --color-bg-surface: #FFFFFF;
  --color-bg-elevated: #FFFFFF;
  --color-border: #D0DCE8;
  --color-border-subtle: #E6EDF4;

  --color-text-primary: #1A2B3C;
  --color-text-secondary: #4A6178;
  --color-text-muted: #7B94AB;
  --color-text-inverse: #FAFCFE;

  --color-accent: #0077BB;
  --color-accent-hover: #005F96;
  --color-accent-subtle: #D4E8F7;

  --color-success: #1A8A5C;
  --color-warning: #C47F17;
  --color-error: #C22E2E;

  --font-heading: 'Plus Jakarta Sans', sans-serif;
  --font-body: 'Inter Tight', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --shadow-sm: 0 1px 3px rgba(26, 43, 60, 0.06);
  --shadow-md: 0 4px 12px rgba(26, 43, 60, 0.08);
  --shadow-lg: 0 8px 24px rgba(26, 43, 60, 0.10);
}

[data-theme="arctic-dawn"][data-mode="dark"] {
  --color-bg-primary: #0F1923;
  --color-bg-secondary: #162230;
  --color-bg-surface: #1B2D3E;
  --color-bg-elevated: #213748;
  --color-border: #2D4A60;
  --color-border-subtle: #1E3549;

  --color-text-primary: #E0EAF2;
  --color-text-secondary: #9BB3C8;
  --color-text-muted: #5F7D96;
  --color-text-inverse: #0F1923;

  --color-accent: #4AA3D8;
  --color-accent-hover: #6BB8E4;
  --color-accent-subtle: #153044;

  --color-success: #3EAF7A;
  --color-warning: #DBA13C;
  --color-error: #E05656;

  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.20);
  --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.28);
  --shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.35);
}
```

**Chart palette:**
```js
const arcticDawnChart = ['#0077BB', '#009988', '#3344AA', '#5EAFD6', '#66C2B5', '#8FC2E4', '#B0D4EC', '#D4E8F7'];
```

---

### 2. Ember

Warm ambers and oranges on dark charcoal. Data-heavy dashboard feel.

```css
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=DM+Sans:wght@400;500;600;700&display=swap');

[data-theme="ember"] {
  /* --- Light Mode --- */
  --color-bg-primary: #FBF8F4;
  --color-bg-secondary: #F4EDE4;
  --color-bg-surface: #FFFFFF;
  --color-bg-elevated: #FFFFFF;
  --color-border: #E0D3C3;
  --color-border-subtle: #EDE4D8;

  --color-text-primary: #2C2218;
  --color-text-secondary: #6B5740;
  --color-text-muted: #9A8670;
  --color-text-inverse: #FBF8F4;

  --color-accent: #D97B1E;
  --color-accent-hover: #BF6810;
  --color-accent-subtle: #FDEBD0;

  --color-success: #3D8B4C;
  --color-warning: #D4A017;
  --color-error: #C0392B;

  --font-heading: 'Outfit', sans-serif;
  --font-body: 'DM Sans', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  --radius-sm: 3px;
  --radius-md: 6px;
  --radius-lg: 10px;
  --shadow-sm: 0 1px 3px rgba(44, 34, 24, 0.07);
  --shadow-md: 0 4px 12px rgba(44, 34, 24, 0.10);
  --shadow-lg: 0 8px 24px rgba(44, 34, 24, 0.12);
}

[data-theme="ember"][data-mode="dark"] {
  --color-bg-primary: #1A1410;
  --color-bg-secondary: #241C15;
  --color-bg-surface: #2C221A;
  --color-bg-elevated: #362A20;
  --color-border: #4D3D2E;
  --color-border-subtle: #3A2E22;

  --color-text-primary: #F0E6D8;
  --color-text-secondary: #C4AE94;
  --color-text-muted: #7D6A54;
  --color-text-inverse: #1A1410;

  --color-accent: #E89838;
  --color-accent-hover: #F0AC55;
  --color-accent-subtle: #3A2A14;

  --color-success: #5BB06C;
  --color-warning: #E5B93A;
  --color-error: #E05A50;

  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.25);
  --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.32);
  --shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.40);
}
```

**Chart palette:**
```js
const emberChart = ['#D97B1E', '#E89838', '#CC3311', '#F0AC55', '#B47D0A', '#EE7733', '#A65D12', '#FBD08E'];
```

---

### 3. Jade Circuit

Greens and golds on dark slate. Tech/engineering aesthetic.

```css
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700&family=IBM+Plex+Sans:wght@300;400;500;600;700&display=swap');

[data-theme="jade-circuit"] {
  /* --- Light Mode --- */
  --color-bg-primary: #F5F8F5;
  --color-bg-secondary: #E8EFE8;
  --color-bg-surface: #FFFFFF;
  --color-bg-elevated: #FFFFFF;
  --color-border: #C5D5C5;
  --color-border-subtle: #DAE5DA;

  --color-text-primary: #1B2B1E;
  --color-text-secondary: #3E5E44;
  --color-text-muted: #6D8A72;
  --color-text-inverse: #F5F8F5;

  --color-accent: #1D8348;
  --color-accent-hover: #16663A;
  --color-accent-subtle: #D4EDDD;

  --color-gold: #B8960C;
  --color-success: #1D8348;
  --color-warning: #B8960C;
  --color-error: #B93030;

  --font-heading: 'Sora', sans-serif;
  --font-body: 'IBM Plex Sans', sans-serif;
  --font-mono: 'IBM Plex Mono', monospace;

  --radius-sm: 2px;
  --radius-md: 4px;
  --radius-lg: 8px;
  --shadow-sm: 0 1px 2px rgba(27, 43, 30, 0.06);
  --shadow-md: 0 3px 10px rgba(27, 43, 30, 0.09);
  --shadow-lg: 0 6px 20px rgba(27, 43, 30, 0.11);
}

[data-theme="jade-circuit"][data-mode="dark"] {
  --color-bg-primary: #0E1A12;
  --color-bg-secondary: #14231A;
  --color-bg-surface: #1A2E22;
  --color-bg-elevated: #20382A;
  --color-border: #2E5038;
  --color-border-subtle: #243D2C;

  --color-text-primary: #DFF0E4;
  --color-text-secondary: #9EC4A6;
  --color-text-muted: #5A8464;
  --color-text-inverse: #0E1A12;

  --color-accent: #3EAF6E;
  --color-accent-hover: #5CC488;
  --color-accent-subtle: #152E1E;

  --color-gold: #D4B02A;
  --color-success: #3EAF6E;
  --color-warning: #D4B02A;
  --color-error: #E05656;

  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.22);
  --shadow-md: 0 3px 10px rgba(0, 0, 0, 0.30);
  --shadow-lg: 0 6px 20px rgba(0, 0, 0, 0.38);
}
```

**Chart palette:**
```js
const jadeCircuitChart = ['#1D8348', '#B8960C', '#009988', '#3EAF6E', '#6DC98B', '#D4B02A', '#5ECEA0', '#8DD8B4'];
```

---

### 4. Dusk Palette

Muted purples and pinks on cream/dark. Creative/design aesthetic.

```css
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@400;500;600;700&family=Nunito+Sans:wght@300;400;500;600;700&display=swap');

[data-theme="dusk-palette"] {
  /* --- Light Mode --- */
  --color-bg-primary: #FBF8FA;
  --color-bg-secondary: #F2ECF0;
  --color-bg-surface: #FFFFFF;
  --color-bg-elevated: #FFFFFF;
  --color-border: #DED2DA;
  --color-border-subtle: #EBE2E8;

  --color-text-primary: #2C1F2A;
  --color-text-secondary: #664E62;
  --color-text-muted: #957A90;
  --color-text-inverse: #FBF8FA;

  --color-accent: #8B3A8B;
  --color-accent-hover: #703070;
  --color-accent-subtle: #F0D8F0;

  --color-pink: #D4567A;
  --color-success: #4A9A5A;
  --color-warning: #C49225;
  --color-error: #C43A3A;

  --font-heading: 'Bricolage Grotesque', sans-serif;
  --font-body: 'Nunito Sans', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --shadow-sm: 0 1px 4px rgba(44, 31, 42, 0.06);
  --shadow-md: 0 4px 14px rgba(44, 31, 42, 0.08);
  --shadow-lg: 0 8px 28px rgba(44, 31, 42, 0.10);
}

[data-theme="dusk-palette"][data-mode="dark"] {
  --color-bg-primary: #1A1218;
  --color-bg-secondary: #241A22;
  --color-bg-surface: #2E222C;
  --color-bg-elevated: #382A36;
  --color-border: #503E4D;
  --color-border-subtle: #3E2E3C;

  --color-text-primary: #F0E4EE;
  --color-text-secondary: #C4A8C0;
  --color-text-muted: #7D6278;
  --color-text-inverse: #1A1218;

  --color-accent: #B864B8;
  --color-accent-hover: #D080D0;
  --color-accent-subtle: #2E1A2E;

  --color-pink: #E47898;
  --color-success: #6BB87A;
  --color-warning: #DBA83A;
  --color-error: #E05656;

  --shadow-sm: 0 1px 4px rgba(0, 0, 0, 0.24);
  --shadow-md: 0 4px 14px rgba(0, 0, 0, 0.30);
  --shadow-lg: 0 8px 28px rgba(0, 0, 0, 0.38);
}
```

**Chart palette:**
```js
const duskPaletteChart = ['#8B3A8B', '#D4567A', '#5C4DB0', '#B864B8', '#E47898', '#7B68C8', '#A090D8', '#C4A8D0'];
```

---

### 5. Monochrome Pro

Pure grayscale with one electric accent (cyan). Ultra-minimal.

```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600;700&display=swap');
/* Note: Geist Mono via: https://fonts.googleapis.com/css2?family=Geist+Mono:wght@400;500;600&display=swap */
@import url('https://fonts.googleapis.com/css2?family=Geist+Mono:wght@400;500;600&display=swap');

[data-theme="monochrome-pro"] {
  /* --- Light Mode --- */
  --color-bg-primary: #FAFAFA;
  --color-bg-secondary: #F0F0F0;
  --color-bg-surface: #FFFFFF;
  --color-bg-elevated: #FFFFFF;
  --color-border: #D4D4D4;
  --color-border-subtle: #E5E5E5;

  --color-text-primary: #171717;
  --color-text-secondary: #525252;
  --color-text-muted: #8A8A8A;
  --color-text-inverse: #FAFAFA;

  --color-accent: #06B6D4;
  --color-accent-hover: #0891B2;
  --color-accent-subtle: #CFFAFE;

  --color-success: #4A9A5A;
  --color-warning: #B0860A;
  --color-error: #B91C1C;

  --font-heading: 'Geist', sans-serif;
  --font-body: 'Geist', sans-serif;
  --font-mono: 'Geist Mono', monospace;

  --radius-sm: 2px;
  --radius-md: 4px;
  --radius-lg: 6px;
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.04);
  --shadow-md: 0 2px 8px rgba(0, 0, 0, 0.06);
  --shadow-lg: 0 4px 16px rgba(0, 0, 0, 0.08);
}

[data-theme="monochrome-pro"][data-mode="dark"] {
  --color-bg-primary: #0A0A0A;
  --color-bg-secondary: #141414;
  --color-bg-surface: #1A1A1A;
  --color-bg-elevated: #242424;
  --color-border: #333333;
  --color-border-subtle: #262626;

  --color-text-primary: #EDEDED;
  --color-text-secondary: #A3A3A3;
  --color-text-muted: #666666;
  --color-text-inverse: #0A0A0A;

  --color-accent: #22D3EE;
  --color-accent-hover: #67E8F9;
  --color-accent-subtle: #0A2A30;

  --color-success: #5CC46C;
  --color-warning: #D4A01A;
  --color-error: #EF4444;

  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.30);
  --shadow-md: 0 2px 8px rgba(0, 0, 0, 0.40);
  --shadow-lg: 0 4px 16px rgba(0, 0, 0, 0.50);
}
```

**Chart palette:**
```js
const monochromeProChart = ['#06B6D4', '#404040', '#737373', '#22D3EE', '#171717', '#A3A3A3', '#D4D4D4', '#525252'];
```

---

### 6. Ocean Deep

Navy, aqua, coral on deep blue/white. Corporate-distinctive.

```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&family=Source+Sans+3:wght@300;400;500;600;700&display=swap');

[data-theme="ocean-deep"] {
  /* --- Light Mode --- */
  --color-bg-primary: #F6F9FC;
  --color-bg-secondary: #E8F0F8;
  --color-bg-surface: #FFFFFF;
  --color-bg-elevated: #FFFFFF;
  --color-border: #C8D8E8;
  --color-border-subtle: #DDE8F2;

  --color-text-primary: #112240;
  --color-text-secondary: #3A5478;
  --color-text-muted: #6882A0;
  --color-text-inverse: #F6F9FC;

  --color-accent: #0C7C8A;
  --color-accent-hover: #096470;
  --color-accent-subtle: #D0F0F4;

  --color-coral: #E06854;
  --color-success: #2A8A5C;
  --color-warning: #C48A1A;
  --color-error: #C43838;

  --font-heading: 'Instrument Sans', sans-serif;
  --font-body: 'Source Sans 3', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --shadow-sm: 0 1px 3px rgba(17, 34, 64, 0.06);
  --shadow-md: 0 4px 12px rgba(17, 34, 64, 0.08);
  --shadow-lg: 0 8px 24px rgba(17, 34, 64, 0.10);
}

[data-theme="ocean-deep"][data-mode="dark"] {
  --color-bg-primary: #0A1628;
  --color-bg-secondary: #101E34;
  --color-bg-surface: #162844;
  --color-bg-elevated: #1C3252;
  --color-border: #264166;
  --color-border-subtle: #1C3454;

  --color-text-primary: #E0EAF6;
  --color-text-secondary: #94B4D4;
  --color-text-muted: #537A9E;
  --color-text-inverse: #0A1628;

  --color-accent: #2AB8C8;
  --color-accent-hover: #50D0DE;
  --color-accent-subtle: #0E2A30;

  --color-coral: #F08070;
  --color-success: #4AB87A;
  --color-warning: #DBA83A;
  --color-error: #E85C5C;

  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.25);
  --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.32);
  --shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.40);
}
```

**Chart palette:**
```js
const oceanDeepChart = ['#0C7C8A', '#E06854', '#112240', '#2AB8C8', '#F08070', '#3A5478', '#50D0DE', '#94B4D4'];
```

---

## Tier 3: Theme Builder

Instructions for deriving a full theme from 1-2 brand colors using HSL manipulation.

### Step 1: Extract Brand HSL

```js
// Convert brand hex to HSL
function hexToHSL(hex) {
  let r = parseInt(hex.slice(1, 3), 16) / 255;
  let g = parseInt(hex.slice(3, 5), 16) / 255;
  let b = parseInt(hex.slice(5, 7), 16) / 255;
  let max = Math.max(r, g, b), min = Math.min(r, g, b);
  let h, s, l = (max + min) / 2;
  if (max === min) { h = s = 0; }
  else {
    let d = max - min;
    s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
    switch (max) {
      case r: h = ((g - b) / d + (g < b ? 6 : 0)) / 6; break;
      case g: h = ((b - r) / d + 2) / 6; break;
      case b: h = ((r - g) / d + 4) / 6; break;
    }
  }
  return [Math.round(h * 360), Math.round(s * 100), Math.round(l * 100)];
}
```

### Step 2: Derive Color Roles from Brand Hue

Given `brandH` (hue), `brandS` (saturation), `brandL` (lightness):

```
Accent:            hsl(brandH, brandS, brandL)          — the brand color itself
Accent Hover:      hsl(brandH, brandS, brandL - 10)     — darker for hover
Accent Subtle:     hsl(brandH, brandS - 20, 92)         — very light tint

Surface Light:     hsl(brandH, 8, 99)                    — near-white with brand warmth
Secondary Light:   hsl(brandH, 10, 95)                   — subtle tinted background
Border Light:      hsl(brandH, 12, 82)                   — border with brand hint

Surface Dark:      hsl(brandH, 15, 11)                   — deep dark with brand warmth
Secondary Dark:    hsl(brandH, 18, 14)                   — slightly lighter dark
Border Dark:       hsl(brandH, 20, 22)                   — dark border with brand hint

Text Primary L:    hsl(brandH, 25, 12)                   — near-black with warmth
Text Secondary L:  hsl(brandH, 15, 35)                   — mid-tone text
Text Muted L:      hsl(brandH, 10, 55)                   — light text

Text Primary D:    hsl(brandH, 15, 90)                   — near-white with warmth
Text Secondary D:  hsl(brandH, 12, 68)                   — mid-tone light text
Text Muted D:      hsl(brandH, 8, 42)                    — muted dark text
```

### Step 3: Auto Light/Dark Mode Generation

```js
function generateTheme(brandHex, secondaryHex = null) {
  const [h, s, l] = hexToHSL(brandHex);
  const [h2, s2, l2] = secondaryHex ? hexToHSL(secondaryHex) : [h, s, l];

  return {
    light: {
      '--color-bg-primary':      `hsl(${h}, 8%, 99%)`,
      '--color-bg-secondary':    `hsl(${h}, 10%, 95%)`,
      '--color-bg-surface':      '#FFFFFF',
      '--color-bg-elevated':     '#FFFFFF',
      '--color-border':          `hsl(${h}, 12%, 82%)`,
      '--color-border-subtle':   `hsl(${h}, 10%, 90%)`,
      '--color-text-primary':    `hsl(${h}, 25%, 12%)`,
      '--color-text-secondary':  `hsl(${h}, 15%, 35%)`,
      '--color-text-muted':      `hsl(${h}, 10%, 55%)`,
      '--color-accent':          `hsl(${h}, ${s}%, ${l}%)`,
      '--color-accent-hover':    `hsl(${h}, ${s}%, ${Math.max(l - 10, 15)}%)`,
      '--color-accent-subtle':   `hsl(${h}, ${Math.max(s - 20, 10)}%, 92%)`,
    },
    dark: {
      '--color-bg-primary':      `hsl(${h}, 15%, 7%)`,
      '--color-bg-secondary':    `hsl(${h}, 18%, 10%)`,
      '--color-bg-surface':      `hsl(${h}, 15%, 12%)`,
      '--color-bg-elevated':     `hsl(${h}, 15%, 15%)`,
      '--color-border':          `hsl(${h}, 20%, 22%)`,
      '--color-border-subtle':   `hsl(${h}, 16%, 16%)`,
      '--color-text-primary':    `hsl(${h}, 15%, 90%)`,
      '--color-text-secondary':  `hsl(${h}, 12%, 68%)`,
      '--color-text-muted':      `hsl(${h}, 8%, 42%)`,
      '--color-accent':          `hsl(${h}, ${Math.min(s + 5, 100)}%, ${Math.min(l + 15, 75)}%)`,
      '--color-accent-hover':    `hsl(${h}, ${Math.min(s + 5, 100)}%, ${Math.min(l + 25, 82)}%)`,
      '--color-accent-subtle':   `hsl(${h}, ${Math.max(s - 10, 15)}%, 14%)`,
    }
  };
}
```

### Step 4: Chart Palette Derivation (5-Step Process)

Given the brand color HSL `(H, S, L)`:

```
Step 1 — Base:        hsl(H, S, 45)               The brand at chart-optimal lightness
Step 2 — Complement:  hsl((H + 180) % 360, S, 45) Opposite hue for contrast
Step 3 — Triadic A:   hsl((H + 120) % 360, S - 10, 50) First triadic
Step 4 — Triadic B:   hsl((H + 240) % 360, S - 10, 50) Second triadic
Step 5 — Analogous:   hsl((H + 30) % 360, S, 48)  Adjacent hue for gradual series

Then add 3 lighter variants:
Step 6: Step 1 at L=65
Step 7: Step 2 at L=65
Step 8: Step 3 at L=65
```

```js
function deriveChartPalette(brandHex) {
  const [h, s, l] = hexToHSL(brandHex);
  return [
    `hsl(${h}, ${s}%, 45%)`,
    `hsl(${(h + 180) % 360}, ${s}%, 45%)`,
    `hsl(${(h + 120) % 360}, ${Math.max(s - 10, 20)}%, 50%)`,
    `hsl(${(h + 240) % 360}, ${Math.max(s - 10, 20)}%, 50%)`,
    `hsl(${(h + 30) % 360}, ${s}%, 48%)`,
    `hsl(${h}, ${s}%, 65%)`,
    `hsl(${(h + 180) % 360}, ${s}%, 65%)`,
    `hsl(${(h + 120) % 360}, ${Math.max(s - 10, 20)}%, 68%)`,
  ];
}
```

### Step 5: CSS Custom Property Template

```css
/* Generated theme from brand color: [BRAND_HEX] */
[data-theme="custom"] {
  /* Surfaces */
  --color-bg-primary: {{bg_primary}};
  --color-bg-secondary: {{bg_secondary}};
  --color-bg-surface: {{bg_surface}};
  --color-bg-elevated: {{bg_elevated}};
  --color-border: {{border}};
  --color-border-subtle: {{border_subtle}};

  /* Text */
  --color-text-primary: {{text_primary}};
  --color-text-secondary: {{text_secondary}};
  --color-text-muted: {{text_muted}};
  --color-text-inverse: {{text_inverse}};

  /* Accent */
  --color-accent: {{accent}};
  --color-accent-hover: {{accent_hover}};
  --color-accent-subtle: {{accent_subtle}};

  /* Semantic */
  --color-success: #2A9D5C;
  --color-warning: #C49225;
  --color-error: #C43838;

  /* Typography — choose from approved fonts */
  --font-heading: {{heading_font}};
  --font-body: {{body_font}};
  --font-mono: 'JetBrains Mono', monospace;

  /* Shape */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;

  /* Elevation */
  --shadow-sm: 0 1px 3px {{shadow_color_sm}};
  --shadow-md: 0 4px 12px {{shadow_color_md}};
  --shadow-lg: 0 8px 24px {{shadow_color_lg}};
}
```

### Font Pairing Recommendations

When building a custom theme, choose one pairing. All are available on Google Fonts:

| Heading                | Body              | Vibe                     |
|------------------------|-------------------|--------------------------|
| Plus Jakarta Sans      | Inter Tight       | Clean scientific         |
| Outfit                 | DM Sans           | Dashboard / data-heavy   |
| Sora                   | IBM Plex Sans     | Engineering / technical  |
| Bricolage Grotesque    | Nunito Sans       | Creative / design        |
| Geist                  | Geist             | Ultra-minimal            |
| Instrument Sans        | Source Sans 3     | Corporate-distinctive    |
| Albert Sans            | Figtree           | Friendly / approachable  |
| Schibsted Grotesk      | Karla             | Editorial / data-story   |

---

## Visual Depth Techniques

These techniques add visual polish and depth to presentations. They are **on by default** for Balanced and Dramatic animation levels. For Minimal, only card accents are applied.

### Background Grid

A subtle grid overlay adds texture without distraction. Uses the presentation's accent color at 2-3% opacity.

Applied by adding `.bg-grid` class to `.slides-container`. The grid is generated via `::before` pseudo-element with `pointer-events: none`.

**Per-preset accent RGB values** (needed for `rgba()` in the grid):

| Preset | `--accent-rgb` value |
|--------|---------------------|
| Arctic Dawn (dark) | `74, 163, 216` |
| Ember (dark) | `232, 152, 56` |
| Jade Circuit (dark) | `62, 175, 110` |
| Dusk Palette (dark) | `184, 100, 184` |
| Monochrome Pro (dark) | `34, 211, 238` |
| Ocean Deep (dark) | `42, 184, 200` |

### Glow Effects

Use `.glow` for a static accent glow on key cards or diagram nodes. Use `.glow-pulse` for a breathing animation on the most important element per slide (max 1-2 per slide).

### Card Accent Borders

Use `.card-accent` (left border) or `.card-top-accent` (top border) to visually distinguish cards. Use `.card-gold` for secondary accent.

### Badge System

Use `.badge` for inline labels (segment numbers, phase indicators, status tags). Variants: `.badge-gold`, `.badge-blue`, `.badge-orange`.

### Staggered Reveal Animations

Add `.reveal` class to child elements of `.slide-content`. Elements automatically stagger with 0.1s delay increments (up to 8 children) when the slide becomes active.

### Typography Refinements

| Element | Property | Value | Effect |
|---------|----------|-------|--------|
| `h1`, `h2` | `letter-spacing` | `-0.02em` | Tighter headings for impact |
| `.section-label` | `letter-spacing` | `0.15em` | Wide spacing for section markers |
| `.section-label` | `text-transform` | `uppercase` | Uppercase monospace labels |

### Animation Level Matrix

| Technique | Minimal | Balanced | Dramatic |
|-----------|---------|----------|----------|
| Background grid | No | Yes | Yes |
| Card accents | Yes | Yes | Yes |
| Staggered reveals | No | Yes | Yes |
| Glow effects | No | No | Yes |
| Glow pulse | No | No | Yes |
| Section labels | Yes | Yes | Yes |
| Badges | Yes | Yes | Yes |
