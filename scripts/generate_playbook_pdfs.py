#!/usr/bin/env python3
"""Generate branded PDFs from playbook markdown content using WeasyPrint."""

import os
import re
import sys
import markdown2
from weasyprint import HTML

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_DIR = os.path.join(REPO_ROOT, "static", "pdfs")
CONTENT_DIR = os.path.join(REPO_ROOT, "content", "playbooks")

BRAND_CSS = """
@page {
    size: A4;
    margin: 2.5cm 2cm;
    @top-left {
        content: "MENSHLY GLOBAL";
        font-family: 'Oswald', sans-serif;
        font-size: 8pt;
        color: #999;
        letter-spacing: 0.15em;
    }
    @top-right {
        content: counter(page);
        font-family: 'Oswald', sans-serif;
        font-size: 8pt;
        color: #999;
    }
    @bottom-center {
        content: "Where AI Meets Revenue";
        font-family: 'Inter', sans-serif;
        font-size: 7pt;
        color: #bbb;
    }
}

@page :first {
    margin-top: 0;
    @top-left { content: none; }
    @top-right { content: none; }
    @bottom-center { content: none; }
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    font-size: 11pt;
    line-height: 1.75;
    color: #1a1a1a;
}

/* Cover Page */
.cover {
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    text-align: center;
    padding: 4cm 2cm;
}

.cover-brand {
    font-family: 'Oswald', sans-serif;
    font-size: 14pt;
    letter-spacing: 0.3em;
    color: #F9FF00;
    background: #1a1a1a;
    display: inline-block;
    padding: 8px 24px;
    margin-bottom: 48px;
}

.cover-title {
    font-family: 'Oswald', sans-serif;
    font-size: 28pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: #1a1a1a;
    margin-bottom: 24px;
}

.cover-line {
    width: 80px;
    height: 4px;
    background: #FF0004;
    margin: 24px auto;
}

.cover-price {
    font-family: 'Oswald', sans-serif;
    font-size: 18pt;
    font-weight: 700;
    color: #FF0004;
    margin-bottom: 12px;
}

.cover-meta {
    font-size: 10pt;
    color: #666;
    margin-top: 8px;
}

.cover-tagline {
    font-family: 'Oswald', sans-serif;
    font-size: 10pt;
    letter-spacing: 0.2em;
    color: #999;
    margin-top: 48px;
}

/* Content Styles */
h1 {
    font-family: 'Oswald', sans-serif;
    font-size: 22pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: -0.02em;
    margin-top: 48px;
    margin-bottom: 16px;
    padding-bottom: 8px;
    border-bottom: 3px solid #F9FF00;
    page-break-after: avoid;
}

h2 {
    font-family: 'Oswald', sans-serif;
    font-size: 16pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: -0.01em;
    margin-top: 36px;
    margin-bottom: 12px;
    page-break-after: avoid;
}

h3 {
    font-family: 'Oswald', sans-serif;
    font-size: 13pt;
    font-weight: 700;
    margin-top: 24px;
    margin-bottom: 8px;
    page-break-after: avoid;
}

p {
    margin-bottom: 12px;
}

blockquote {
    border-left: 6px solid #F9FF00;
    border-top: 2px solid #F9FF00;
    border-bottom: 2px solid #F9FF00;
    border-right: 2px solid #F9FF00;
    padding: 16px 20px;
    margin: 20px 0;
    background: #fffef0;
    font-style: normal;
    font-size: 10.5pt;
    line-height: 1.7;
}

blockquote strong {
    font-family: 'Oswald', sans-serif;
    text-transform: uppercase;
    letter-spacing: 0.02em;
    color: #1a1a1a;
}

code {
    background: #f5f5f5;
    border: 1px solid #ddd;
    padding: 1px 4px;
    font-size: 10pt;
    font-family: 'SFMono-Regular', Consolas, monospace;
}

pre {
    background: #1a1a1a;
    color: #ffffff;
    padding: 16px 20px;
    font-size: 9pt;
    line-height: 1.5;
    overflow-x: auto;
    border: 2px solid #1a1a1a;
    margin: 16px 0;
}

pre code {
    background: none;
    border: none;
    color: inherit;
    padding: 0;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0;
    font-size: 9.5pt;
}

thead {
    background: #1a1a1a;
    color: #ffffff;
}

thead th {
    padding: 8px 12px;
    font-family: 'Oswald', sans-serif;
    font-size: 9pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    text-align: left;
}

tbody tr {
    border-bottom: 1.5px solid #e0e0e0;
}

tbody tr:nth-child(even) {
    background: #fafafa;
}

tbody td {
    padding: 8px 12px;
    vertical-align: top;
}

strong {
    font-family: 'Oswald', sans-serif;
    text-transform: uppercase;
    letter-spacing: 0.01em;
}

ul, ol {
    margin-bottom: 12px;
    padding-left: 24px;
}

li {
    margin-bottom: 6px;
}

hr {
    border: none;
    border-top: 2px solid #F9FF00;
    margin: 32px 0;
}
"""

def parse_frontmatter(md_text):
    """Extract frontmatter from markdown file."""
    fm = {}
    if not md_text.startswith('---'):
        return fm, md_text
    parts = md_text.split('---', 2)
    if len(parts) >= 3:
        for line in parts[1].strip().split('\n'):
            if ':' in line:
                key, val = line.split(':', 1)
                fm[key.strip()] = val.strip().strip('"').strip("'")
        return fm, parts[2].strip()
    return fm, md_text


def generate_pdf(slug, md_path):
    """Generate a branded PDF from a playbook markdown file."""
    print(f"Processing: {slug}")
    
    with open(md_path, 'r') as f:
        raw = f.read()
    
    fm, body = parse_frontmatter(raw)
    
    title = fm.get('title', slug.replace('-', ' ').title())
    price = fm.get('price', 'FREE')
    read_time = fm.get('readTime', '60 MIN')
    excerpt = fm.get('excerpt', '')
    
    # Convert markdown to HTML
    body_html = markdown2.markdown(
        body,
        extras=[
            "tables", "fenced-code-blocks", "strike", "task_list",
            "header-ids", "break-on-newline", "code-friendly"
        ]
    )
    
    # Build the full HTML document
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
{BRAND_CSS}
</style>
</head>
<body>
<div class="cover">
    <div class="cover-brand">MENSHLY GLOBAL</div>
    <div class="cover-title">{title}</div>
    <div class="cover-line"></div>
    <div class="cover-price">{price}</div>
    <div class="cover-meta">{read_time} READ</div>
    <div class="cover-tagline">WHERE AI MEETS REVENUE</div>
</div>
{body_html}
</body>
</html>"""
    
    # Generate PDF
    output_path = os.path.join(PDF_DIR, f"{slug}.pdf")
    HTML(string=html).write_pdf(output_path)
    
    file_size = os.path.getsize(output_path) / 1024
    print(f"  Generated: {output_path} ({file_size:.0f} KB)")
    return output_path


def main():
    os.makedirs(PDF_DIR, exist_ok=True)
    
    playbooks = []
    for fname in os.listdir(CONTENT_DIR):
        if fname.endswith('.md') and not fname.startswith('_'):
            slug = fname[:-3]
            playbooks.append((slug, os.path.join(CONTENT_DIR, fname)))
    
    if not playbooks:
        print("No playbook files found!")
        sys.exit(1)
    
    print(f"Found {len(playbooks)} playbooks\n")
    
    for slug, path in playbooks:
        try:
            generate_pdf(slug, path)
        except Exception as e:
            print(f"  ERROR generating {slug}: {e}")
            import traceback
            traceback.print_exc()
    
    print(f"\nDone! PDFs saved to {PDF_DIR}")


if __name__ == '__main__':
    main()
