# Scripts

Optional utilities for checking, exporting, and converting presentations. Generated HTML decks work in a browser without these scripts.

## Setup

```bash
pip install -r scripts/requirements.txt
```

## Delivery checks

### validate

Check a generated deck before sharing it. The validator has no third-party Python dependencies and checks CSS class integrity, inline-style density, and theme-variable references.

```bash
scripts/validate presentation.html
scripts/validate examples/slide-sage-intro.html examples/metrics-review.html
```

### render-check

Render a selected slide with Playwright and fail on browser errors, missing theme tokens, or overflow. It is the CI-ready browser check for representative slides.

```bash
scripts/render-check --slide 3 --viewport-size 1123,794 examples/metrics-review.html artifacts/metrics.png
scripts/render-check --slide 3 --viewport-size 1123,500 examples/metrics-review.html artifacts/metrics-short.png
```

### run-evals

Run the fixture-backed acceptance evals. To check an agent-produced deck, select its eval and pass the generated HTML path.

```bash
scripts/run-evals
scripts/run-evals --id quick-status-update --output generated-status.html
```

### export-pdf

Render a deck to PDF with Playwright. It waits for the deck's print-ready marker, then prints a deterministic file path. Browser Print remains a fallback when Playwright is unavailable.

```bash
scripts/export-pdf presentation.html
scripts/export-pdf presentation.html ./out/presentation.pdf --no-open
```

The script uses an installed `playwright` command when available, otherwise it runs the pinned Playwright CLI through `npx`. On the first run, it installs the matching Chromium binary before rendering.

### inline-vendor.py

Create an opt-in offline HTML copy by embedding the supported, version-pinned Chart.js, ECharts, D3, and Prism libraries. It strips Google Fonts imports so the chosen preset falls back to local system fonts. The script refuses unsupported static remote assets rather than claiming a deck is offline when it is not.

```bash
scripts/inline-vendor.py presentation.html
scripts/inline-vendor.py presentation.html --output presentation.offline.html
```

The offline HTML copy embeds the applicable notice document in a non-rendered template. Preserve [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md) too when distributing related source or support files.

## Conversion and image scripts

### extract-pptx.py

Extract content from PowerPoint files into structured JSON.

```bash
python scripts/extract-pptx.py presentation.pptx
python scripts/extract-pptx.py presentation.pptx --output extracted.json
python scripts/extract-pptx.py presentation.pptx --images-dir ./images
```

### extract-pdf.py

Extract content from PDF files into structured JSON.

```bash
python scripts/extract-pdf.py document.pdf
python scripts/extract-pdf.py document.pdf --output extracted.json
python scripts/extract-pdf.py document.pdf --images-dir ./images
```

### process-images.py

Resize, crop, and optimize images for embedding in presentations.

```bash
python scripts/process-images.py resize input.jpg --max-width 800 --output resized.jpg
python scripts/process-images.py circle input.jpg --size 200 --output avatar.png
python scripts/process-images.py rounded input.jpg --radius 20 --output rounded.png
python scripts/process-images.py shadow input.jpg --output shadow.png
python scripts/process-images.py batch input_dir/ --max-width 600 --output output_dir/
python scripts/process-images.py base64 input.jpg
```

## Requirements

- Python 3.11+
- Dependencies listed in `requirements.txt` for PPTX/PDF conversion and image processing
- Playwright CLI or `npx` only for `export-pdf`
