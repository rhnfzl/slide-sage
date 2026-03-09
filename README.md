# Slide Sage

[![License](https://img.shields.io/github/license/rhnfzl/slide-sage)](LICENSE)
[![GitHub Clones](https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count&url=https://gist.githubusercontent.com/rhnfzl/163f62ec409cd7427733c39fcfedbf39/raw/clone.json&logo=github)](https://github.com/rhnfzl/slide-sage)

**Create presentations with charts, diagrams, and code highlighting. Works with most AI coding tools.**

Slide Sage is an open-source skill that generates professional, data-rich HTML presentations as single files — no build tools, no frameworks, no dependencies.

## What Makes It Different

| Feature | Slide Sage | reveal.js | Slidev | Gamma/Beautiful.ai |
|---------|-----------|-----------|--------|-------------------|
| AI-native workflow | Yes | No | No | Proprietary |
| Data visualization | Chart.js, ECharts, D3 | Plugin | Vue charts | Limited |
| Architecture diagrams | CSS/HTML + SVG templates | No | Mermaid only | No |
| Code highlighting | Prism.js | highlight.js | Shiki | No |
| Single-file output | Yes | No (needs build) | No (needs build) | No (SaaS) |
| Cross-platform AI tools | Yes | N/A | N/A | N/A |
| Offline/file:// | Yes | Partial | No | No |
| Zero dependencies | Yes | npm required | npm required | Account required |

## Supported Tools

Slide Sage follows the [Agent Skills](https://agentskills.io) open standard, supported by **32+ AI coding tools**:

**CLI Agents:** Claude Code, Claude, OpenAI Codex, Amp, Gemini CLI, Goose, Roo Code, OpenHands, TRAE, Mistral AI Vibe, Autohand Code CLI, OpenCode, pi, Command Code, Emdash, Agentman, VT Code

**IDEs & Editors:** Cursor, VS Code, Junie (JetBrains), Firebender, Mux (Coder), Piebald

**Platforms:** GitHub Copilot, Databricks, Snowflake, Factory, Qodo, Ona

**Frameworks:** Spring AI, Laravel Boost, Letta

Any tool that supports Agent Skills can install Slide Sage — see below.

## Installation

### Claude Code
```bash
claude skill add rhnfzl/slide-sage
```
The skill appears as `/slide-sage` and Claude loads it automatically when you ask to create a presentation.

### OpenAI Codex CLI
```bash
# Install via the built-in skill installer
$skill-installer install https://github.com/rhnfzl/slide-sage

# Or clone into the skills directory
git clone https://github.com/rhnfzl/slide-sage.git .agents/skills/slide-sage
```


### Amp (Sourcegraph)
```bash
amp skill add rhnfzl/slide-sage
```

### Cursor

**Option A — Remote Rule (recommended):**
1. Open Cursor Settings → Rules
2. Click `+ Add Rule` next to Project Rules
3. Select "Remote Rule (Github)"
4. Paste: `https://github.com/rhnfzl/slide-sage`

**Option B — Clone into skills directory:**
```bash
git clone https://github.com/rhnfzl/slide-sage.git .agents/skills/slide-sage
```

### VS Code / GitHub Copilot
```bash
# Clone into your project's skills directory
git clone https://github.com/rhnfzl/slide-sage.git .agents/skills/slide-sage

# Or use .github/skills/ if you prefer
git clone https://github.com/rhnfzl/slide-sage.git .github/skills/slide-sage
```
Copilot discovers skills in `.agents/skills/`, `.github/skills/`, and `~/.agents/skills/` (user-level).

### Gemini CLI
```bash
# Clone into Gemini's skills directory
git clone https://github.com/rhnfzl/slide-sage.git .agents/skills/slide-sage
```

<details>
<summary><strong>More tools (Roo Code, Aider, Windsurf, Amazon Q, and others)</strong></summary>

#### Roo Code
```bash
git clone https://github.com/rhnfzl/slide-sage.git .agents/skills/slide-sage
```

#### Aider
```bash
# Load directly when starting aider
aider --read slide-sage/SKILL.md

# Or add to .aider.conf.yml for automatic loading
# read: slide-sage/SKILL.md
```

#### Windsurf
```bash
git clone https://github.com/rhnfzl/slide-sage.git
mkdir -p .windsurf/rules
cp slide-sage/SKILL.md .windsurf/rules/slide-sage.md
```

#### Amazon Q Developer
```bash
git clone https://github.com/rhnfzl/slide-sage.git
mkdir -p .amazonq/rules
cp slide-sage/SKILL.md .amazonq/rules/slide-sage.md
```

#### Other Agent Skills-compatible tools
Any tool listed in [Supported Tools](#supported-tools) can install via the standard `.agents/skills/` directory:
```bash
git clone https://github.com/rhnfzl/slide-sage.git .agents/skills/slide-sage
```

#### Any Other AI Tool
Point the tool at `SKILL.md` — it contains complete instructions any LLM can follow.

</details>

### Global Installation

To make Slide Sage available across **all your projects** (not just one), clone it into your tool's user-level skills directory:

<details>
<summary><strong>Global install paths per tool</strong></summary>

#### Claude Code
```bash
git clone https://github.com/rhnfzl/slide-sage.git ~/.claude/skills/slide-sage
```

#### OpenAI Codex CLI
```bash
git clone https://github.com/rhnfzl/slide-sage.git ~/.agents/skills/slide-sage
```

#### Amp
```bash
git clone https://github.com/rhnfzl/slide-sage.git ~/.config/agents/skills/slide-sage
```

#### Cursor
```bash
git clone https://github.com/rhnfzl/slide-sage.git ~/.cursor/skills/slide-sage
```

#### VS Code / GitHub Copilot
```bash
git clone https://github.com/rhnfzl/slide-sage.git ~/.agents/skills/slide-sage
```

#### Gemini CLI
```bash
git clone https://github.com/rhnfzl/slide-sage.git ~/.gemini/skills/slide-sage
```

#### Aider
```bash
# Clone anywhere, then add to global config
git clone https://github.com/rhnfzl/slide-sage.git ~/.skills/slide-sage
echo "read: ~/.skills/slide-sage/SKILL.md" >> ~/.aider.conf.yml
```

</details>

## Usage

Once installed, just ask:

```
Create a presentation about our Q3 results with charts showing
revenue growth ($2.1M → $2.8M) and user acquisition (45K → 62K)
```

```
Make a teaching deck about microservices with architecture diagrams
and Python code examples
```

```
Convert my pitch-deck.pptx to an interactive HTML presentation
with animated charts
```

The AI will:
1. Analyze your content and detect what's needed (charts, diagrams, code)
2. Select the right libraries automatically
3. Generate a single HTML file you can open in any browser
4. Include keyboard navigation, responsive design, and print-to-PDF support

## Features

### Data Visualization
- **Chart.js** (default) — Bar, line, pie, scatter, radar, and more
- **ECharts** — Heatmaps, sankey diagrams, treemaps, candlestick charts
- **D3.js** — Custom statistical visualizations
- All charts use **colorblind-safe palettes** by default

### Architecture Diagrams
- **SVG templates** — Token-efficient pre-designed diagrams (microservices, data pipeline, client-server, layered architecture)
- **CSS/HTML diagrams** — Sequence flows, architecture stacks, pyramids, process flows with full theme integration
- **Inline SVG** — Fully custom diagrams with interactive tooltips

### Code Slides
- **Prism.js** syntax highlighting for 15+ languages
- Dark and light themes
- Line numbers and line highlighting
- Copy button

### Presentation Features
- Keyboard navigation (arrows, space, page up/down, Home/End)
- Touch swipe support
- Progress bar and slide counter
- Presenter mode with speaker notes, timer, and next-slide preview
- PDF export via browser Print > Save as PDF
- Responsive design (works on any screen size)
- `prefers-reduced-motion` support

### Style System
- **6 curated style presets** with matching chart palettes
- **Theme builder** — Generate custom themes from brand colors
- **3 animation levels** — Minimal, balanced, dramatic
- Dark and light mode support

## File Structure

```
slide-sage/
├── SKILL.md                  # Main skill instructions (Agent Skills standard)
├── references/               # Detailed reference guides
│   ├── html-template.md      # Base HTML + JS controller
│   ├── viewport-system.md    # Responsive CSS system
│   ├── style-guide.md        # Style presets + theme builder
│   ├── viz-integration.md    # Chart library patterns
│   ├── diagram-patterns.md   # Diagram system (3 tiers)
│   ├── animation-guide.md    # Animation intensity levels
│   ├── code-highlighting.md  # Prism.js integration
│   └── presenter-mode.md     # Dual-window presenter UI
├── templates/                # Reusable templates
│   ├── diagrams/             # SVG diagram templates
│   └── comparison/           # Comparison slide layouts
├── scripts/                  # Python utilities
│   ├── extract-pptx.py       # PowerPoint content extraction
│   └── process-images.py     # Image processing pipeline
├── assets/
│   └── viewport-base.css     # Core CSS (inlined into presentations)
└── evals/
    └── evals.json            # Test cases
```

## How It Works

Slide Sage uses **progressive disclosure** — the AI reads only what it needs:

1. `SKILL.md` is always read (the workflow brain, ~400 lines)
2. Reference files are loaded on-demand based on content analysis
3. Libraries are included via CDN only when needed
4. Output is always a self-contained HTML file

This keeps context usage minimal while supporting complex presentations.

## Requirements

- Any AI coding tool (Claude Code, Codex CLI, Amp, Cursor, VS Code/Copilot, Gemini CLI, Aider, Windsurf, Amazon Q, Roo Code, and more)
- A web browser to view presentations
- Python 3.11+ with `python-pptx`, `pymupdf`, and `Pillow` (only for PPTX/PDF conversion — see `scripts/README.md`)

## License

MIT
