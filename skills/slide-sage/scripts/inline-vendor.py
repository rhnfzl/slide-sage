#!/usr/bin/env python3
"""Create an opt-in offline copy of a Slide Sage HTML presentation.

The converter inlines only known, version-pinned libraries. It removes Google
Fonts imports so the selected preset's system-font fallback is used offline.
Unsupported static remote assets cause a clear failure instead of a false
offline guarantee.
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlopen


PRISM_PREFIX = "https://cdn.jsdelivr.net/npm/prismjs@1.30.0/"
PRISM_SAFE_SCRIPT_SUFFIXES = {
    "prism.min.js",
    "plugins/line-highlight/prism-line-highlight.min.js",
    "plugins/line-numbers/prism-line-numbers.min.js",
}
NOTICE_PATH = Path(__file__).resolve().parents[1] / "THIRD_PARTY_NOTICES.md"
GOOGLE_FONT_PREFIXES = (
    "https://fonts.googleapis.com/",
    "https://fonts.gstatic.com/",
)
EXACT_SCRIPTS = {
    "https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js": "Chart.js 4.4.7",
    "https://cdn.jsdelivr.net/npm/echarts@6.1.0/dist/echarts.min.js": "ECharts 6.1.0",
    "https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js": "D3 7.9.0",
}
ATTRIBUTE_RE = re.compile(
    r"(?P<name>[\w:-]+)\s*=\s*(?:(?P<quote>[\"'])(?P<quoted>.*?)(?P=quote)|(?P<bare>[^\s\"'=<>`]+))",
    re.DOTALL,
)
SCRIPT_TAG_RE = re.compile(
    r"<script\b(?P<attrs>[^>]*)>\s*</script\s*>", re.IGNORECASE | re.DOTALL
)
LINK_TAG_RE = re.compile(r"<link\b(?P<attrs>[^>]*)/?>", re.IGNORECASE | re.DOTALL)
GOOGLE_IMPORT_RE = re.compile(
    r"@import\s+(?:url\(\s*)?[\"']?https://fonts\.googleapis\.com/[^\"')\s]+[\"']?\s*\)?\s*;",
    re.IGNORECASE,
)
REMOTE_TAG_RE = re.compile(
    r"<(?:script|link|img|object|embed|iframe|source)\b[^>]*\b(?:src|href)\s*=\s*[\"']?(?:(?:https?:)?//)",
    re.IGNORECASE,
)
REMOTE_CSS_URL_RE = re.compile(r"url\(\s*[\"']?(?:(?:https?:)?//)", re.IGNORECASE)
REMOTE_CSS_IMPORT_RE = re.compile(
    r"@import\s+(?:url\(\s*)?[\"']?(?:(?:https?:)?//)", re.IGNORECASE
)


def attributes(raw: str) -> dict[str, str]:
    return {
        match.group("name").lower(): html.unescape(match.group("quoted") or match.group("bare"))
        for match in ATTRIBUTE_RE.finditer(raw)
    }


def is_google_font_url(url: str) -> bool:
    return url.startswith(GOOGLE_FONT_PREFIXES)


def known_script_label(url: str) -> str | None:
    if url in EXACT_SCRIPTS:
        return EXACT_SCRIPTS[url]
    prism_suffix = url.removeprefix(PRISM_PREFIX)
    if prism_suffix in PRISM_SAFE_SCRIPT_SUFFIXES or (
        prism_suffix.startswith("components/prism-") and prism_suffix.endswith(".min.js")
    ):
        return "Prism 1.30.0"
    return None


def is_known_stylesheet(url: str) -> bool:
    return url.startswith(PRISM_PREFIX) and url.endswith(".css")


def fetch_text(url: str) -> str:
    try:
        with urlopen(url, timeout=30) as response:
            encoding = response.headers.get_content_charset() or "utf-8"
            return response.read().decode(encoding)
    except (OSError, URLError, UnicodeDecodeError) as error:
        raise RuntimeError(f"Could not fetch pinned library {url}: {error}") from error


def escape_inline(source: str, closing_tag: str) -> str:
    return source.replace(f"</{closing_tag}", f"<\\/{closing_tag}")


def inline_scripts(document: str, included: set[str]) -> str:
    def replace(match: re.Match[str]) -> str:
        attrs = attributes(match.group("attrs"))
        url = attrs.get("src")
        if not url:
            return match.group(0)
        label = known_script_label(url)
        if not label:
            return match.group(0)
        included.add(label)
        source = escape_inline(fetch_text(url), "script")
        return f'<script data-slide-sage-inline="{label}">\n{source}\n</script>'

    return SCRIPT_TAG_RE.sub(replace, document)


def inline_stylesheets(document: str, included: set[str]) -> str:
    def replace(match: re.Match[str]) -> str:
        attrs = attributes(match.group("attrs"))
        url = attrs.get("href")
        if not url:
            return match.group(0)
        if is_google_font_url(url):
            return ""
        rel = {part.lower() for part in attrs.get("rel", "").split()}
        if "stylesheet" not in rel or not is_known_stylesheet(url):
            return match.group(0)
        included.add("Prism 1.30.0")
        source = escape_inline(fetch_text(url), "style")
        return f'<style data-slide-sage-inline="Prism 1.30.0">\n{source}\n</style>'

    document = LINK_TAG_RE.sub(replace, document)
    return GOOGLE_IMPORT_RE.sub("", document)


def assert_no_unsupported_remote_assets(document: str) -> None:
    if (
        REMOTE_TAG_RE.search(document)
        or REMOTE_CSS_URL_RE.search(document)
        or REMOTE_CSS_IMPORT_RE.search(document)
    ):
        raise RuntimeError(
            "The presentation still contains a static remote asset that Slide Sage "
            "cannot vendor. Download it locally or remove it before retrying."
        )


def inject_notices(document: str, included: set[str]) -> str:
    if not included:
        return document
    libraries = ", ".join(sorted(included))
    try:
        notices = NOTICE_PATH.read_text(encoding="utf-8")
    except OSError as error:
        raise RuntimeError(f"Could not read third-party notices at {NOTICE_PATH}: {error}") from error
    notice = (
        f'<template id="slide-sage-third-party-notices" data-libraries="{html.escape(libraries, quote=True)}">\n'
        f"<pre>{html.escape(notices)}</pre>\n"
        "</template>"
    )
    if "</head>" in document.lower():
        return re.sub(r"</head>", f"{notice}\n</head>", document, count=1, flags=re.IGNORECASE)
    return f"{notice}\n{document}"


def output_path_for(input_path: Path, output: str | None) -> Path:
    if output:
        return Path(output).expanduser().resolve()
    return input_path.with_name(f"{input_path.stem}.offline{input_path.suffix}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inline known pinned libraries and strip web-font imports for offline use."
    )
    parser.add_argument("presentation", help="Input HTML presentation")
    parser.add_argument("--output", "-o", help="Output HTML path")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = Path(args.presentation).expanduser().resolve(strict=True)
    output_path = output_path_for(input_path, args.output)
    if input_path == output_path:
        raise RuntimeError("The offline output path must be different from the input presentation.")
    document = input_path.read_text(encoding="utf-8")
    included: set[str] = set()
    document = inline_scripts(document, included)
    document = inline_stylesheets(document, included)
    assert_no_unsupported_remote_assets(document)
    document = inject_notices(document, included)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(document, encoding="utf-8")
    print(f"Offline presentation ready: {output_path}")
    if not included:
        print("No supported CDN libraries were present. The output still uses only local assets.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError) as error:
        print(f"inline-vendor: {error}", file=sys.stderr)
        raise SystemExit(1)
