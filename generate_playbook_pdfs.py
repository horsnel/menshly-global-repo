#!/usr/bin/env python3
"""
Generate professional PDF playbooks from Hugo markdown content files.
Uses weasyprint + markdown-it-py with Menshly Global branding.
"""

import os
import re
import sys
from pathlib import Path

from markdown_it import MarkdownIt
from weasyprint import HTML, CSS

# ─── Configuration ───────────────────────────────────────────────────────────

CONTENT_DIR = Path("/home/z/my-project/menshly-repo/content/playbooks")
OUTPUT_DIR = Path("/home/z/my-project/menshly-repo/static/pdfs")

PLAYBOOKS = [
    {"slug": "ai-side-hustle-blueprint", "price": "$19"},
    {"slug": "chatgpt-prompt-engineering-guide", "price": "$49"},
    {"slug": "ai-automation-agency-playbook", "price": "$47"},
    {"slug": "automation-agency-starter-kit", "price": "$29"},
]

# ─── Brand Colors ────────────────────────────────────────────────────────────

BLACK = "#1A1A1A"
YELLOW = "#F9FF00"
RED = "#FF0004"
WHITE = "#FFFFFF"
LIGHT_GRAY = "#F5F5F5"
MED_GRAY = "#E0E0E0"
DARK_GRAY = "#4A4A4A"

# ─── CSS Stylesheet ──────────────────────────────────────────────────────────

PDF_CSS = CSS(string="""
/* ─── Page Setup ──────────────────────────────────────────────────────────── */
@page {
    size: A4;
    margin: 2.5cm 2cm 2.5cm 2cm;

    @bottom-center {
        content: counter(page);
        font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif;
        font-size: 9pt;
        color: #999999;
    }
}

@page :first {
    margin: 0;
    @bottom-center { content: none; }
}

/* ─── Cover Page ──────────────────────────────────────────────────────────── */
.cover-page {
    page: cover;
    width: 210mm;
    height: 297mm;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #1A1A1A;
    color: #FFFFFF;
    text-align: center;
    page-break-after: always;
    position: relative;
    overflow: hidden;
}

.cover-yellow-bar {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 12mm;
    background-color: #F9FF00;
}

.cover-yellow-bar-bottom {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 12mm;
    background-color: #F9FF00;
}

.cover-brand {
    font-family: 'Oswald', 'Impact', 'Arial Black', sans-serif;
    font-size: 14pt;
    font-weight: 700;
    letter-spacing: 6pt;
    color: #F9FF00;
    margin-top: 20mm;
    margin-bottom: 15mm;
    text-transform: uppercase;
}

.cover-title {
    font-family: 'Oswald', 'Impact', 'Arial Black', sans-serif;
    font-size: 32pt;
    font-weight: 700;
    line-height: 1.15;
    color: #FFFFFF;
    max-width: 85%;
    margin: 0 auto 10mm auto;
    text-transform: uppercase;
}

.cover-tagline {
    font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif;
    font-size: 11pt;
    color: #CCCCCC;
    max-width: 70%;
    margin: 0 auto 15mm auto;
    line-height: 1.5;
}

.cover-price {
    font-family: 'Oswald', 'Impact', 'Arial Black', sans-serif;
    font-size: 24pt;
    font-weight: 700;
    color: #F9FF00;
    margin-top: 10mm;
    margin-bottom: 5mm;
}

.cover-price-label {
    font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif;
    font-size: 9pt;
    color: #999999;
    text-transform: uppercase;
    letter-spacing: 2pt;
}

.cover-red-stripe {
    width: 60mm;
    height: 3pt;
    background-color: #FF0004;
    margin: 8mm auto;
}

/* ─── Body Content ────────────────────────────────────────────────────────── */
body {
    font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif;
    font-size: 10.5pt;
    line-height: 1.65;
    color: #1A1A1A;
}

/* ─── Headings ────────────────────────────────────────────────────────────── */
h1 {
    font-family: 'Oswald', 'Impact', 'Arial Black', sans-serif;
    font-size: 22pt;
    font-weight: 700;
    color: #1A1A1A;
    margin-top: 24pt;
    margin-bottom: 12pt;
    text-transform: uppercase;
    letter-spacing: 1pt;
    border-bottom: 4pt solid #F9FF00;
    padding-bottom: 8pt;
    page-break-after: avoid;
}

h2 {
    font-family: 'Oswald', 'Impact', 'Arial Black', sans-serif;
    font-size: 15pt;
    font-weight: 700;
    color: #1A1A1A;
    margin-top: 18pt;
    margin-bottom: 8pt;
    letter-spacing: 0.5pt;
    page-break-after: avoid;
}

h3 {
    font-family: 'Oswald', 'Impact', 'Arial Black', sans-serif;
    font-size: 12pt;
    font-weight: 700;
    color: #1A1A1A;
    margin-top: 14pt;
    margin-bottom: 6pt;
    page-break-after: avoid;
}

h4, h5, h6 {
    font-family: 'Oswald', 'Impact', 'Arial Black', sans-serif;
    font-size: 10.5pt;
    font-weight: 700;
    color: #4A4A4A;
    margin-top: 10pt;
    margin-bottom: 4pt;
}

/* ─── Paragraphs & Text ──────────────────────────────────────────────────── */
p {
    margin-top: 0;
    margin-bottom: 8pt;
    orphans: 3;
    widows: 3;
}

strong, b {
    font-weight: 700;
    color: #1A1A1A;
}

em, i {
    font-style: italic;
}

a {
    color: #FF0004;
    text-decoration: none;
}

/* ─── Lists ───────────────────────────────────────────────────────────────── */
ul, ol {
    margin-top: 4pt;
    margin-bottom: 8pt;
    padding-left: 18pt;
}

li {
    margin-bottom: 3pt;
}

/* ─── Tables ──────────────────────────────────────────────────────────────── */
table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 8pt;
    margin-bottom: 12pt;
    font-size: 9.5pt;
}

thead {
    background-color: #1A1A1A;
    color: #FFFFFF;
}

thead th {
    font-family: 'Oswald', 'Impact', 'Arial Black', sans-serif;
    font-weight: 700;
    font-size: 9pt;
    text-transform: uppercase;
    letter-spacing: 0.5pt;
    padding: 8pt 8pt;
    text-align: left;
    border: 1pt solid #1A1A1A;
}

tbody td {
    padding: 6pt 8pt;
    border: 1pt solid #E0E0E0;
    vertical-align: top;
}

tbody tr:nth-child(even) {
    background-color: #F9F9F9;
}

tbody tr:hover {
    background-color: #F9FF00;
}

/* ─── Blockquotes ─────────────────────────────────────────────────────────── */
blockquote {
    margin: 12pt 0;
    padding: 10pt 16pt;
    border-left: 5pt solid #F9FF00;
    background-color: #FAFAFA;
    font-style: normal;
}

blockquote p {
    margin-bottom: 4pt;
}

/* ─── Accent Boxes (from Hugo shortcodes) ─────────────────────────────────── */
.accent-box {
    margin: 12pt 0;
    padding: 12pt 16pt;
    border-left: 5pt solid #F9FF00;
    background-color: #1A1A1A;
    color: #FFFFFF;
}

.accent-box strong, .accent-box b {
    color: #F9FF00;
}

.accent-box p {
    margin-bottom: 4pt;
    color: #EEEEEE;
}

/* ─── Code Blocks ─────────────────────────────────────────────────────────── */
pre {
    background-color: #F5F5F5;
    border: 1pt solid #E0E0E0;
    border-radius: 4pt;
    padding: 12pt 14pt;
    margin: 10pt 0;
    overflow-x: auto;
    font-size: 8.5pt;
    line-height: 1.5;
    page-break-inside: avoid;
}

pre code {
    font-family: 'Courier New', 'Consolas', 'Monaco', monospace;
    font-size: 8.5pt;
    color: #1A1A1A;
    background: none;
    padding: 0;
}

code {
    font-family: 'Courier New', 'Consolas', 'Monaco', monospace;
    font-size: 9pt;
    background-color: #F0F0F0;
    padding: 1pt 4pt;
    border-radius: 2pt;
    color: #1A1A1A;
}

/* ─── Horizontal Rules ────────────────────────────────────────────────────── */
hr {
    border: none;
    border-top: 2pt solid #E0E0E0;
    margin: 20pt 0;
}

/* ─── Checkbox lists ──────────────────────────────────────────────────────── */
.task-list-item {
    list-style: none;
    margin-left: -18pt;
}

.task-list-item input[type="checkbox"] {
    margin-right: 6pt;
}

/* ─── Page break utility ──────────────────────────────────────────────────── */
.page-break {
    page-break-before: always;
}

/* ─── Avoid breaks inside these elements ──────────────────────────────────── */
h1, h2, h3 {
    page-break-after: avoid;
}

pre, table, blockquote {
    page-break-inside: avoid;
}
""")


# ─── Helper Functions ─────────────────────────────────────────────────────────

def strip_frontmatter(text: str) -> tuple[str, dict]:
    """Strip YAML frontmatter from markdown and return (content, metadata)."""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL)
    if not match:
        return text, {}

    meta = {}
    for line in match.group(1).splitlines():
        if ':' in line:
            key, val = line.split(':', 1)
            meta[key.strip()] = val.strip().strip('"').strip("'")

    content = text[match.end():]
    return content, meta


def process_hugo_shortcodes(html: str) -> str:
    """Process Hugo shortcodes like {{% accent-box %}}."""
    # Replace accent-box shortcodes with styled divs
    html = re.sub(
        r'\{\{%\s*accent-box\s*%\}\}(.*?)\{\{%\s*/accent-box\s*%\}\}',
        r'<div class="accent-box">\1</div>',
        html,
        flags=re.DOTALL,
    )
    return html


def render_markdown(md_text: str) -> str:
    """Convert markdown to HTML using markdown-it-py."""
    md = MarkdownIt("commonmark", {"html": True}).enable("table").enable("strikethrough")
    return md.render(md_text)


def build_cover_html(title: str, price: str, excerpt: str, read_time: str) -> str:
    """Build the cover page HTML."""
    return f"""
    <div class="cover-page">
        <div class="cover-yellow-bar"></div>
        <div class="cover-brand">MENSHLY GLOBAL</div>
        <div class="cover-title">{title}</div>
        <div class="cover-red-stripe"></div>
        <div class="cover-tagline">{excerpt}</div>
        <div class="cover-price">{price}</div>
        <div class="cover-price-label">One-time purchase &middot; Lifetime access</div>
        <div class="cover-yellow-bar-bottom"></div>
    </div>
    """


def generate_pdf(slug: str, price: str) -> str:
    """Generate a PDF for a single playbook."""
    md_path = CONTENT_DIR / f"{slug}.md"
    pdf_path = OUTPUT_DIR / f"{slug}.pdf"

    if not md_path.exists():
        print(f"  ERROR: Markdown file not found: {md_path}")
        return ""

    # Read and process markdown
    raw = md_path.read_text(encoding="utf-8")
    content, meta = strip_frontmatter(raw)

    title = meta.get("title", slug.replace("-", " ").title())
    excerpt = meta.get("excerpt", "")
    read_time = meta.get("readTime", "")

    # Convert markdown to HTML
    body_html = render_markdown(content)
    body_html = process_hugo_shortcodes(body_html)

    # Build full HTML document
    cover = build_cover_html(title, price, excerpt, read_time)

    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — Menshly Global</title>
</head>
<body>
    {cover}
    <div class="body-content">
        {body_html}
    </div>
</body>
</html>"""

    # Generate PDF
    print(f"  Generating: {pdf_path.name} ...")
    doc = HTML(string=html_doc)
    doc.write_pdf(pdf_path, stylesheets=[PDF_CSS])

    size = pdf_path.stat().st_size
    print(f"    ✓ Done ({size:,} bytes)")
    return str(pdf_path)


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=== Menshly Global Playbook PDF Generator ===\n")

    results = []
    for playbook in PLAYBOOKS:
        slug = playbook["slug"]
        price = playbook["price"]
        print(f"Processing: {slug}")
        pdf_path = generate_pdf(slug, price)
        if pdf_path:
            results.append(pdf_path)
        print()

    print(f"=== Complete: {len(results)}/{len(PLAYBOOKS)} PDFs generated ===\n")

    for path in results:
        p = Path(path)
        size_kb = p.stat().st_size / 1024
        print(f"  {p.name:50s} {size_kb:>8.1f} KB  ({p.stat().st_size:,} bytes)")

    return results


if __name__ == "__main__":
    main()
