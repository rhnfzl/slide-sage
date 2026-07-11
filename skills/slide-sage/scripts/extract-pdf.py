#!/usr/bin/env python3
"""Extract content from PDF files for slide-sage conversion.

Usage:
    python extract-pdf.py input.pdf [--output extracted.json]

Extracts page content (text, images, tables, layout hints) into a structured
JSON format that the AI can use to generate an HTML presentation.

Output format matches extract-pptx.py so either can feed the same generation
pipeline.

Requirements:
    pip install pymupdf Pillow
"""

from __future__ import annotations

import argparse
import base64
import json
import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Error: PyMuPDF is required. Install with: pip install pymupdf")
    sys.exit(1)


def _detect_alignment(span_origin_x: float, block_x0: float, block_width: float) -> str:
    """Heuristic alignment detection based on text position within its block."""
    if block_width < 1:
        return "left"
    relative = (span_origin_x - block_x0) / block_width
    if relative > 0.7:
        return "right"
    if relative > 0.4:
        return "center"
    return "left"


def _detect_bullet_level(text: str, indent: float) -> tuple[str, int]:
    """Detect bullet prefix and indentation-based nesting level.

    Returns the cleaned text and the nesting level (0 = not a bullet).
    """
    stripped = text
    level = 0
    for prefix in ("\u2022", "\u2023", "-", "\u2013", "\u25a0", "\u25ba", "\u25aa", "\u2219"):
        if stripped.startswith(prefix):
            stripped = stripped[len(prefix):].strip()
            level = 1
            break

    if indent > 40:
        level = max(level, 2)
    elif indent > 20:
        level = max(level, 1)

    return stripped, level


def classify_block(paragraphs: list[dict]) -> str:
    """Classify a text block as heading, body, or bullets."""
    if not paragraphs:
        return "empty"
    first = paragraphs[0]
    if first.get("bold") and first.get("font_size", 0) and first["font_size"] >= 18:
        return "heading"
    if any(p["level"] > 0 for p in paragraphs):
        return "bullets"
    return "body"


def extract_text_blocks(page: fitz.Page) -> list[dict]:
    """Extract text blocks with font and position information."""
    elements = []
    blocks = page.get_text("dict", flags=fitz.TEXT_PRESERVE_WHITESPACE)["blocks"]

    for block in blocks:
        if block["type"] != 0:  # 0 = text block
            continue

        bbox = block["bbox"]  # (x0, y0, x1, y1)
        block_x0 = bbox[0]
        block_width = bbox[2] - bbox[0]
        paragraphs = []

        for line in block["lines"]:
            line_text = ""
            line_font_size = 0.0
            line_is_bold = False
            first_span_x = block_x0

            for span in line["spans"]:
                line_text += span["text"]
                if span["size"] > line_font_size:
                    line_font_size = span["size"]
                if "bold" in span["font"].lower():
                    line_is_bold = True

            if line["spans"]:
                first_span_x = line["spans"][0]["origin"][0]

            text = line_text.strip()
            if not text:
                continue

            indent = first_span_x - block_x0
            cleaned, level = _detect_bullet_level(text, indent)
            alignment = _detect_alignment(first_span_x, block_x0, block_width)

            paragraphs.append({
                "text": cleaned if level > 0 else text,
                "level": level,
                "alignment": alignment,
                "font_size": round(line_font_size, 1),
                "bold": line_is_bold,
            })

        if not paragraphs:
            continue

        role = classify_block(paragraphs)
        elements.append({
            "type": "text",
            "role": role,
            "paragraphs": paragraphs,
            "position": {
                "left": round(bbox[0], 1),
                "top": round(bbox[1], 1),
                "width": round(block_width, 1),
                "height": round(bbox[3] - bbox[1], 1),
            },
        })

    return elements


def extract_images(
    doc: fitz.Document, page: fitz.Page, output_dir: Path | None, image_counter: list[int]
) -> list[dict]:
    """Extract images from a PDF page."""
    elements = []
    seen_xrefs: set[int] = set()

    for img_info in page.get_images(full=True):
        xref = img_info[0]
        if xref in seen_xrefs:
            continue
        seen_xrefs.add(xref)
        try:
            base_image = doc.extract_image(xref)
        except (ValueError, RuntimeError):
            continue

        if not base_image or not base_image.get("image"):
            continue

        blob = base_image["image"]
        ext = base_image.get("ext", "png")
        content_type = f"image/{ext}"
        if ext == "jpeg":
            content_type = "image/jpeg"

        result = {
            "type": "image",
            "content_type": content_type,
            "pixel_width": base_image.get("width", 0),
            "pixel_height": base_image.get("height", 0),
        }

        if output_dir:
            if ext == "jpeg":
                ext = "jpg"
            img_name = f"image_{image_counter[0]:03d}.{ext}"
            img_path = output_dir / img_name
            img_path.write_bytes(blob)
            result["path"] = str(img_path)
        else:
            if len(blob) < 37_500:
                encoded = base64.b64encode(blob).decode("ascii")
                result["data_uri"] = f"data:{content_type};base64,{encoded}"
            else:
                result["note"] = f"Image too large for inline ({len(blob)} bytes)"

        # Try to get placement rectangle for position data
        try:
            rects = page.get_image_rects(xref)
            if rects:
                r = rects[0]
                result["position"] = {
                    "left": round(r.x0, 1),
                    "top": round(r.y0, 1),
                    "width": round(r.width, 1),
                    "height": round(r.height, 1),
                }
        except (ValueError, RuntimeError):
            pass

        image_counter[0] += 1
        elements.append(result)

    return elements


def extract_tables(page: fitz.Page) -> list[dict]:
    """Extract tables from a PDF page.

    Requires PyMuPDF >= 1.23.0 for ``page.find_tables()``.
    Gracefully returns an empty list on older versions.
    """
    elements = []
    try:
        tables = page.find_tables()
    except AttributeError:
        return elements

    for table in tables:
        rows = []
        for row in table.extract():
            cells = [cell.strip() if cell else "" for cell in row]
            rows.append(cells)

        if rows:
            tbbox = table.bbox
            elements.append({
                "type": "table",
                "rows": rows,
                "position": {
                    "left": round(tbbox[0], 1),
                    "top": round(tbbox[1], 1),
                },
            })

    return elements


def extract_page(
    doc: fitz.Document, page: fitz.Page, page_index: int, output_dir: Path | None, image_counter: list[int]
) -> dict:
    """Extract all content from a single PDF page."""
    elements = []
    elements.extend(extract_text_blocks(page))
    elements.extend(extract_tables(page))
    elements.extend(extract_images(doc, page, output_dir, image_counter))

    return {
        "slide_number": page_index + 1,
        "layout": "",
        "elements": elements,
        "notes": "",
    }


def extract_pdf(pdf_path: str, output_dir: Path | None = None) -> dict:
    """Extract full PDF content."""
    with fitz.open(pdf_path) as doc:
        if doc.is_encrypted:
            print("Error: PDF is password-protected. Decrypt it first.", file=sys.stderr)
            sys.exit(1)

        page_width = 0.0
        page_height = 0.0
        if doc.page_count > 0:
            first_page = doc[0]
            page_width = first_page.rect.width
            page_height = first_page.rect.height

        image_counter = [0]
        slides = []
        for i, page in enumerate(doc):
            slides.append(extract_page(doc, page, i, output_dir, image_counter))

    return {
        "source": str(pdf_path),
        "slide_count": len(slides),
        "dimensions": {
            "width": round(page_width, 1),
            "height": round(page_height, 1),
            "aspect_ratio": round(page_width / page_height, 3) if page_height else None,
        },
        "slides": slides,
    }


def main():
    parser = argparse.ArgumentParser(description="Extract PDF content for slide-sage")
    parser.add_argument("input", help="Path to .pdf file")
    parser.add_argument("--output", "-o", help="Output JSON path (default: stdout)")
    parser.add_argument(
        "--images-dir",
        help="Directory to save extracted images (default: embed as data URI)",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: File not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    output_dir = Path(args.images_dir) if args.images_dir else None
    if output_dir:
        output_dir.mkdir(parents=True, exist_ok=True)

    try:
        result = extract_pdf(str(input_path), output_dir)
    except RuntimeError as e:
        print(f"Error: Cannot open PDF: {e}", file=sys.stderr)
        sys.exit(1)

    if args.output:
        with open(args.output, "w") as f:
            json.dump(result, f, indent=2, default=str)
        print(f"Extracted {result['slide_count']} pages to {args.output}")
    else:
        print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()
