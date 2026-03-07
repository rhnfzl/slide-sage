#!/usr/bin/env python3
"""Process images for slide-sage presentations.

Provides utilities for resizing, cropping, and optimizing images
to be embedded in HTML presentations.

Usage:
    python process-images.py resize input.jpg --max-width 800 --output resized.jpg
    python process-images.py circle input.jpg --size 200 --output avatar.png
    python process-images.py batch input_dir/ --max-width 600 --output output_dir/
    python process-images.py base64 input.jpg

Requirements:
    pip install Pillow
"""

from __future__ import annotations

import argparse
import base64
import sys
from io import BytesIO
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFilter
except ImportError:
    print("Error: Pillow is required. Install with: pip install Pillow")
    sys.exit(1)


def resize_image(
    img: Image.Image,
    max_width: int = 800,
    max_height: int = 600,
) -> Image.Image:
    """Resize image to fit within max dimensions while maintaining aspect ratio."""
    img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
    return img


def circle_crop(img: Image.Image, size: int = 200) -> Image.Image:
    """Crop image into a circle (for avatars/profile photos)."""
    img = img.convert("RGBA")

    min_dim = min(img.width, img.height)
    left = (img.width - min_dim) // 2
    top = (img.height - min_dim) // 2
    img = img.crop((left, top, left + min_dim, top + min_dim))
    img = img.resize((size, size), Image.Resampling.LANCZOS)

    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size - 1, size - 1), fill=255)

    result = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    result.paste(img, (0, 0), mask)
    return result


def add_rounded_corners(img: Image.Image, radius: int = 20) -> Image.Image:
    """Add rounded corners to an image."""
    img = img.convert("RGBA")
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle(
        (0, 0, img.width - 1, img.height - 1),
        radius=radius,
        fill=255,
    )
    result = Image.new("RGBA", img.size, (0, 0, 0, 0))
    result.paste(img, (0, 0), mask)
    return result


def add_shadow(
    img: Image.Image,
    offset: tuple = (5, 5),
    blur: int = 10,
    shadow_color: tuple = (0, 0, 0, 80),
) -> Image.Image:
    """Add a drop shadow to an image."""
    img = img.convert("RGBA")
    shadow_size = (
        img.width + abs(offset[0]) + blur * 2,
        img.height + abs(offset[1]) + blur * 2,
    )
    shadow = Image.new("RGBA", shadow_size, (0, 0, 0, 0))
    shadow_layer = Image.new("RGBA", img.size, shadow_color)

    paste_x = max(offset[0], 0) + blur
    paste_y = max(offset[1], 0) + blur
    shadow.paste(shadow_layer, (paste_x, paste_y))
    shadow = shadow.filter(ImageFilter.GaussianBlur(blur))

    img_x = max(-offset[0], 0) + blur
    img_y = max(-offset[1], 0) + blur
    shadow.paste(img, (img_x, img_y), img)
    return shadow


def add_padding(
    img: Image.Image,
    padding: int = 40,
    bg_color: tuple = (0, 0, 0, 0),
) -> Image.Image:
    """Add padding around an image (transparent by default).

    Useful when screenshots need breathing room in the slide layout,
    or when a colored background border is needed around a screenshot.

    Args:
        img: Source image.
        padding: Pixels of padding on each side.
        bg_color: RGBA tuple for the padding area. Default is transparent.
            Use e.g. (15, 15, 15, 255) for a dark solid background.
    """
    img = img.convert("RGBA")
    w, h = img.size
    new = Image.new("RGBA", (w + 2 * padding, h + 2 * padding), bg_color)
    new.paste(img, (padding, padding), img)
    return new


def to_base64(img: Image.Image, fmt: str = "PNG", quality: int = 85) -> str:
    """Convert image to base64 data URI string."""
    buffer = BytesIO()
    save_kwargs: dict = {"format": fmt}
    if fmt.upper() in ("JPEG", "JPG", "WEBP"):
        save_kwargs["quality"] = quality
    if fmt.upper() == "PNG":
        save_kwargs["optimize"] = True
    img.save(buffer, **save_kwargs)
    encoded = base64.b64encode(buffer.getvalue()).decode("ascii")
    mime = f"image/{fmt.lower()}"
    if fmt.upper() == "JPG":
        mime = "image/jpeg"
    return f"data:{mime};base64,{encoded}"


def process_file(
    input_path: Path,
    command: str,
    output_path: Path | None = None,
    **kwargs,
) -> str | None:
    """Process a single image file."""
    img = Image.open(input_path)

    if command == "resize":
        img = resize_image(
            img,
            max_width=kwargs.get("max_width", 800),
            max_height=kwargs.get("max_height", 600),
        )
    elif command == "circle":
        img = circle_crop(img, size=kwargs.get("size", 200))
    elif command == "rounded":
        img = add_rounded_corners(img, radius=kwargs.get("radius", 20))
    elif command == "shadow":
        img = add_shadow(img)
    elif command == "padding":
        img = add_padding(
            img,
            padding=kwargs.get("padding", 40),
            bg_color=kwargs.get("bg_color", (0, 0, 0, 0)),
        )
    elif command == "base64":
        fmt = input_path.suffix.lstrip(".").upper()
        if fmt == "JPG":
            fmt = "JPEG"
        if fmt not in ("PNG", "JPEG", "WEBP", "GIF"):
            fmt = "PNG"
        return to_base64(img, fmt=fmt, quality=kwargs.get("quality", 85))

    if output_path:
        if img.mode == "RGBA" and output_path.suffix.lower() in (".jpg", ".jpeg"):
            bg = Image.new("RGB", img.size, (255, 255, 255))
            bg.paste(img, mask=img.split()[3])
            img = bg
        img.save(output_path, quality=kwargs.get("quality", 85))
        print(f"Saved: {output_path} ({img.width}x{img.height})")

    return None


def main():
    parser = argparse.ArgumentParser(description="Process images for slide-sage")
    subparsers = parser.add_subparsers(dest="command", required=True)

    resize_p = subparsers.add_parser("resize", help="Resize image to fit within bounds")
    resize_p.add_argument("input", help="Input image path")
    resize_p.add_argument("--max-width", type=int, default=800)
    resize_p.add_argument("--max-height", type=int, default=600)
    resize_p.add_argument("--output", "-o", required=True)
    resize_p.add_argument("--quality", type=int, default=85)

    circle_p = subparsers.add_parser("circle", help="Crop image into circle")
    circle_p.add_argument("input", help="Input image path")
    circle_p.add_argument("--size", type=int, default=200)
    circle_p.add_argument("--output", "-o", required=True)

    batch_p = subparsers.add_parser("batch", help="Batch resize a directory")
    batch_p.add_argument("input", help="Input directory")
    batch_p.add_argument("--max-width", type=int, default=800)
    batch_p.add_argument("--max-height", type=int, default=600)
    batch_p.add_argument("--output", "-o", required=True)
    batch_p.add_argument("--quality", type=int, default=85)

    b64_p = subparsers.add_parser("base64", help="Convert image to base64 data URI")
    b64_p.add_argument("input", help="Input image path")
    b64_p.add_argument("--quality", type=int, default=85)

    rounded_p = subparsers.add_parser("rounded", help="Add rounded corners")
    rounded_p.add_argument("input", help="Input image path")
    rounded_p.add_argument("--radius", type=int, default=20)
    rounded_p.add_argument("--output", "-o", required=True)

    shadow_p = subparsers.add_parser("shadow", help="Add drop shadow")
    shadow_p.add_argument("input", help="Input image path")
    shadow_p.add_argument("--output", "-o", required=True)

    pad_p = subparsers.add_parser("padding", help="Add padding around image")
    pad_p.add_argument("input", help="Input image path")
    pad_p.add_argument("--padding", type=int, default=40, help="Pixels of padding per side")
    pad_p.add_argument("--output", "-o", required=True)

    args = parser.parse_args()

    if args.command == "batch":
        input_dir = Path(args.input)
        output_dir = Path(args.output)
        output_dir.mkdir(parents=True, exist_ok=True)
        extensions = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp"}
        for img_path in sorted(input_dir.iterdir()):
            if img_path.suffix.lower() in extensions:
                out = output_dir / img_path.name
                process_file(
                    img_path,
                    "resize",
                    output_path=out,
                    max_width=args.max_width,
                    max_height=args.max_height,
                    quality=args.quality,
                )
    elif args.command == "base64":
        result = process_file(Path(args.input), "base64", quality=args.quality)
        if result:
            print(result)
    else:
        output_path = Path(args.output) if hasattr(args, "output") else None
        kwargs = {k: v for k, v in vars(args).items() if k not in ("input", "command", "output")}
        process_file(Path(args.input), args.command, output_path=output_path, **kwargs)


if __name__ == "__main__":
    main()
