# Icon Library Reference

Curated set of 33 Lucide icons for use in slide-sage presentations. All icons use stroke-based rendering on a 24x24 viewBox.

**Source**: [Lucide Icons](https://lucide.dev/) v0.577+ -- ISC License (no attribution required)

---

## Usage Patterns

### Pattern A: Sprite + `<use>` (for SVG diagrams)

Paste the sprite block as a hidden element at the top of `<body>`, then reference icons by ID inside any SVG:

```html
<!-- Hidden sprite block (paste once at top of <body>) -->
<svg style="display:none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <symbol id="icon-database" viewBox="0 0 24 24" fill="none" stroke="currentColor"
            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <ellipse cx="12" cy="5" rx="9" ry="3"/>
      <path d="M3 5V19A9 3 0 0 0 21 19V5"/>
      <path d="M3 12A9 3 0 0 0 21 12"/>
    </symbol>
    <!-- ...more symbols... -->
  </defs>
</svg>

<!-- Then use inside any SVG diagram -->
<svg viewBox="0 0 800 600">
  <use href="#icon-database" x="100" y="50" width="48" height="48" stroke="#3b82f6"/>
  <use href="#icon-cloud" x="300" y="50" width="48" height="48" stroke="#8b5cf6"/>
</svg>
```

### Pattern B: Standalone `<svg>` (for HTML content)

Inline a single icon directly in HTML, without needing the sprite:

```html
<svg class="icon" viewBox="0 0 24 24">
  <ellipse cx="12" cy="5" rx="9" ry="3"/>
  <path d="M3 5V19A9 3 0 0 0 21 19V5"/>
  <path d="M3 12A9 3 0 0 0 21 12"/>
</svg>
```

### CSS Helper

```css
.icon {
  display: inline-block;
  vertical-align: middle;
  width: 1.2em;
  height: 1.2em;
  stroke: currentColor;
  fill: none;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}
```

---

## Icon Catalog

### Infrastructure

| Icon | Name | Description |
|------|------|-------------|
| database | `icon-database` | Cylinder / data store |
| server | `icon-server` | Stacked server rack |
| hard-drive | `icon-hard-drive` | Disk drive |
| cpu | `icon-cpu` | Processor chip with pins |
| monitor | `icon-monitor` | Desktop display |

**database**
```svg
<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5V19A9 3 0 0 0 21 19V5"/><path d="M3 12A9 3 0 0 0 21 12"/>
```

**server**
```svg
<rect width="20" height="8" x="2" y="2" rx="2" ry="2"/><rect width="20" height="8" x="2" y="14" rx="2" ry="2"/><line x1="6" x2="6" y1="6" y2="6"/><line x1="6" x2="6" y1="18" y2="18"/>
```

**hard-drive**
```svg
<path d="M10 16h.01"/><path d="M2.212 11.577a2 2 0 0 0-.212.896V18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-5.527a2 2 0 0 0-.212-.896L18.55 5.11A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"/><path d="M21.946 12.013H2.054"/><path d="M6 16h.01"/>
```

**cpu**
```svg
<rect x="4" y="4" width="16" height="16" rx="2"/><rect x="8" y="8" width="8" height="8" rx="1"/><path d="M12 20v2"/><path d="M12 2v2"/><path d="M17 20v2"/><path d="M17 2v2"/><path d="M2 12h2"/><path d="M2 17h2"/><path d="M2 7h2"/><path d="M20 12h2"/><path d="M20 17h2"/><path d="M20 7h2"/><path d="M7 20v2"/><path d="M7 2v2"/>
```

**monitor**
```svg
<rect width="20" height="14" x="2" y="3" rx="2"/><line x1="8" x2="16" y1="21" y2="21"/><line x1="12" x2="12" y1="17" y2="21"/>
```

---

### Cloud / Network

| Icon | Name | Description |
|------|------|-------------|
| cloud | `icon-cloud` | Cloud shape |
| globe | `icon-globe` | Earth / worldwide |
| wifi | `icon-wifi` | Wireless signal |
| network | `icon-network` | Tree network topology |
| router | `icon-router` | Network router with antenna |

**cloud**
```svg
<path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z"/>
```

**globe**
```svg
<circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/>
```

**wifi**
```svg
<path d="M12 20h.01"/><path d="M2 8.82a15 15 0 0 1 20 0"/><path d="M5 12.859a10 10 0 0 1 14 0"/><path d="M8.5 16.429a5 5 0 0 1 7 0"/>
```

**network**
```svg
<rect x="16" y="16" width="6" height="6" rx="1"/><rect x="2" y="16" width="6" height="6" rx="1"/><rect x="9" y="2" width="6" height="6" rx="1"/><path d="M5 16v-3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3"/><path d="M12 12V8"/>
```

**router**
```svg
<rect width="20" height="8" x="2" y="14" rx="2"/><path d="M6.01 18H6"/><path d="M10.01 18H10"/><path d="M15 10v4"/><path d="M17.84 7.17a4 4 0 0 0-5.66 0"/><path d="M20.66 4.34a8 8 0 0 0-11.31 0"/>
```

---

### Security

| Icon | Name | Description |
|------|------|-------------|
| shield | `icon-shield` | Plain shield |
| shield-check | `icon-shield-check` | Shield with checkmark |
| lock | `icon-lock` | Padlock |
| key | `icon-key` | Key with circular bow |

**shield**
```svg
<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/>
```

**shield-check**
```svg
<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>
```

**lock**
```svg
<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>
```

**key**
```svg
<path d="m15.5 7.5 2.3 2.3a1 1 0 0 0 1.4 0l2.1-2.1a1 1 0 0 0 0-1.4L19 4"/><path d="m21 2-9.6 9.6"/><circle cx="7.5" cy="15.5" r="5.5"/>
```

---

### DevOps

| Icon | Name | Description |
|------|------|-------------|
| git-branch | `icon-git-branch` | Branch with nodes |
| git-commit-horizontal | `icon-git-commit-horizontal` | Commit dot on line |
| terminal | `icon-terminal` | CLI prompt |
| package | `icon-package` | 3D package box |
| container | `icon-container` | Container / Docker |

**git-branch**
```svg
<path d="M15 6a9 9 0 0 0-9 9V3"/><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/>
```

**git-commit-horizontal**
```svg
<circle cx="12" cy="12" r="3"/><line x1="3" x2="9" y1="12" y2="12"/><line x1="15" x2="21" y1="12" y2="12"/>
```

**terminal**
```svg
<path d="M12 19h8"/><path d="m4 17 6-6-6-6"/>
```

**package**
```svg
<path d="M11 21.73a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73z"/><path d="M12 22V12"/><polyline points="3.29 7 12 12 20.71 7"/><path d="m7.5 4.27 9 5.15"/>
```

**container**
```svg
<path d="M22 7.7c0-.6-.4-1.2-.8-1.5l-6.3-3.9a1.72 1.72 0 0 0-1.7 0l-10.3 6c-.5.2-.9.8-.9 1.4v6.6c0 .5.4 1.2.8 1.5l6.3 3.9a1.72 1.72 0 0 0 1.7 0l10.3-6c.5-.3.9-1 .9-1.5Z"/><path d="M10 21.9V14L2.1 9.1"/><path d="m10 14 11.9-6.9"/><path d="M14 19.8v-8.1"/><path d="M18 17.5V9.4"/>
```

---

### Code / API

| Icon | Name | Description |
|------|------|-------------|
| code | `icon-code` | Angle brackets `</>` |
| plug | `icon-plug` | Electrical plug / connector |
| webhook | `icon-webhook` | Webhook triple-arc |
| settings | `icon-settings` | Gear / cog |

**code**
```svg
<path d="m16 18 6-6-6-6"/><path d="m8 6-6 6 6 6"/>
```

**plug**
```svg
<path d="M12 22v-5"/><path d="M15 8V2"/><path d="M17 8a1 1 0 0 1 1 1v4a4 4 0 0 1-4 4h-4a4 4 0 0 1-4-4V9a1 1 0 0 1 1-1z"/><path d="M9 8V2"/>
```

**webhook**
```svg
<path d="M18 16.98h-5.99c-1.1 0-1.95.94-2.48 1.9A4 4 0 0 1 2 17c.01-.7.2-1.4.57-2"/><path d="m6 17 3.13-5.78c.53-.97.1-2.18-.5-3.1a4 4 0 1 1 6.89-4.06"/><path d="m12 6 3.13 5.73C15.66 12.7 16.9 13 18 13a4 4 0 0 1 0 8"/>
```

**settings**
```svg
<path d="M9.671 4.136a2.34 2.34 0 0 1 4.659 0 2.34 2.34 0 0 0 3.319 1.915 2.34 2.34 0 0 1 2.33 4.033 2.34 2.34 0 0 0 0 3.831 2.34 2.34 0 0 1-2.33 4.033 2.34 2.34 0 0 0-3.319 1.915 2.34 2.34 0 0 1-4.659 0 2.34 2.34 0 0 0-3.32-1.915 2.34 2.34 0 0 1-2.33-4.033 2.34 2.34 0 0 0 0-3.831A2.34 2.34 0 0 1 6.35 6.051a2.34 2.34 0 0 0 3.319-1.915"/><circle cx="12" cy="12" r="3"/>
```

---

### Data / ML

| Icon | Name | Description |
|------|------|-------------|
| brain | `icon-brain` | Brain / AI |
| activity | `icon-activity` | ECG / heartbeat line |
| bar-chart-3 | `icon-bar-chart-3` | Bar chart with axes |
| layers | `icon-layers` | Stacked layers |
| workflow | `icon-workflow` | Connected process blocks |

**brain**
```svg
<path d="M12 18V5"/><path d="M15 13a4.17 4.17 0 0 1-3-4 4.17 4.17 0 0 1-3 4"/><path d="M17.598 6.5A3 3 0 1 0 12 5a3 3 0 1 0-5.598 1.5"/><path d="M17.997 5.125a4 4 0 0 1 2.526 5.77"/><path d="M18 18a4 4 0 0 0 2-7.464"/><path d="M19.967 17.483A4 4 0 1 1 12 18a4 4 0 1 1-7.967-.517"/><path d="M6 18a4 4 0 0 1-2-7.464"/><path d="M6.003 5.125a4 4 0 0 0-2.526 5.77"/>
```

**activity**
```svg
<path d="M22 12h-2.48a2 2 0 0 0-1.93 1.46l-2.35 8.36a.25.25 0 0 1-.48 0L9.24 2.18a.25.25 0 0 0-.48 0l-2.35 8.36A2 2 0 0 1 4.49 12H2"/>
```

**bar-chart-3**
```svg
<path d="M3 3v16a2 2 0 0 0 2 2h16"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/>
```

**layers**
```svg
<path d="M12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83z"/><path d="M2 12a1 1 0 0 0 .58.91l8.6 3.91a2 2 0 0 0 1.65 0l8.58-3.9A1 1 0 0 0 22 12"/><path d="M2 17a1 1 0 0 0 .58.91l8.6 3.91a2 2 0 0 0 1.65 0l8.58-3.9A1 1 0 0 0 22 17"/>
```

**workflow**
```svg
<rect width="8" height="8" x="3" y="3" rx="2"/><path d="M7 11v4a2 2 0 0 0 2 2h4"/><rect width="8" height="8" x="13" y="13" rx="2"/>
```

---

### General

| Icon | Name | Description |
|------|------|-------------|
| users | `icon-users` | People / team |
| building | `icon-building` | Office building |
| box | `icon-box` | 3D box |
| folder | `icon-folder` | File folder |
| send | `icon-send` | Paper plane / send |
| zap | `icon-zap` | Lightning bolt |
| credit-card | `icon-credit-card` | Payment card |

**users**
```svg
<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><path d="M16 3.128a4 4 0 0 1 0 7.744"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><circle cx="9" cy="7" r="4"/>
```

**building**
```svg
<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-3a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v3"/><path d="M8 6h.01"/><path d="M12 6h.01"/><path d="M16 6h.01"/><path d="M8 10h.01"/><path d="M12 10h.01"/><path d="M16 10h.01"/><path d="M8 14h.01"/><path d="M12 14h.01"/><path d="M16 14h.01"/>
```

**box**
```svg
<path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><path d="m3.3 7 8.7 5 8.7-5"/><path d="M12 22V12"/>
```

**folder**
```svg
<path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"/>
```

**send**
```svg
<path d="M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z"/><path d="m21.854 2.147-10.94 10.939"/>
```

**zap**
```svg
<path d="M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z"/>
```

**credit-card**
```svg
<rect width="20" height="14" x="2" y="5" rx="2"/><line x1="2" x2="22" y1="10" y2="10"/>
```
