# Scripts

Optional Python utilities for extracting content from existing presentations. These are **not required** for creating presentations - they're only needed when converting PPTX or PDF files.

## Setup

```bash
pip install -r scripts/requirements.txt
```

## Scripts

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
- Dependencies listed in `requirements.txt`
