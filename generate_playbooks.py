#!/usr/bin/env python3
"""
Menshly Global Playbook PDF Generator v2
Generates professional multi-page PDFs from markdown source files.
Brand: Black #1A1A1A, Acid Yellow #F9FF00, Red #FF0004, White #FFFFFF
"""

import re
import os
import yaml
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch, mm
from reportlab.lib.colors import HexColor, black, white, Color
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, Flowable, Frame, PageTemplate, 
    BaseDocTemplate, NextPageTemplate, Image
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import io

# ─── Brand Colours ────────────────────────────────────────────────────
BLACK       = HexColor("#1A1A1A")
YELLOW      = HexColor("#F9FF00")
RED         = HexColor("#FF0004")
WHITE       = HexColor("#FFFFFF")
GREY_BG     = HexColor("#F5F5F5")
GREY_LINE   = HexColor("#CCCCCC")
DARK_GREY   = HexColor("#444444")
LIGHT_YELLOW = HexColor("#FFFFD0")
CODE_BG     = HexColor("#1E1E1E")

PAGE_W, PAGE_H = letter
MARGIN = 0.75 * inch
CONTENT_W = PAGE_W - 2 * MARGIN

# ─── Font Registration ───────────────────────────────────────────────
FONT_HEADING = "Helvetica-Bold"
FONT_BODY = "Helvetica"
FONT_BODY_BOLD = "Helvetica-Bold"
FONT_MONO = "Courier"

def try_register_fonts():
    global FONT_HEADING, FONT_BODY, FONT_BODY_BOLD
    font_map = {
        "/usr/share/fonts/truetype/oswald/Oswald-Bold.ttf": "Oswald-Bold",
        "/usr/share/fonts/truetype/oswald/Oswald-SemiBold.ttf": "Oswald-SemiBold",
        "/usr/share/fonts/truetype/inter/Inter-Regular.ttf": "Inter",
        "/usr/share/fonts/truetype/inter/Inter-Bold.ttf": "Inter-Bold",
        "/usr/share/fonts/truetype/inter/Inter-Medium.ttf": "Inter-Medium",
    }
    for path, name in font_map.items():
        if os.path.exists(path):
            try:
                pdfmetrics.registerFont(TTFont(name, path))
                if "Oswald" in name:
                    FONT_HEADING = name
                elif "Inter" in name and "Bold" not in name:
                    FONT_BODY = name
                elif "Inter-Bold" in name:
                    FONT_BODY_BOLD = name
            except:
                pass

try_register_fonts()

# ─── Markdown Parser ─────────────────────────────────────────────────

def strip_frontmatter(text):
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2].strip()
    return text

def strip_shortcodes(text):
    text = re.sub(r'\{\{%\s*accent-box\s*%\}\}(.*?)\{\{%\s*/accent-box\s*%\}\}',
                  lambda m: process_accent_box(m.group(1)), text, flags=re.DOTALL)
    text = re.sub(r'\{\{%\s*/?[\w-]+\s*%\}\}', '', text)
    text = re.sub(r'\{\{<\s*/?[\w-]+\s*>\}\}', '', text)
    return text

def process_accent_box(content):
    content = content.strip()
    lines = [l.strip() for l in content.split('\n') if l.strip()]
    if lines:
        return "\n\n**HACK:** " + " ".join(lines) + "\n\n"
    return ""

def parse_frontmatter(text):
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            try:
                data = yaml.safe_load(parts[1])
                return data if data else {}
            except:
                return {}
    return {}

def escape_xml(text):
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text

def inline_md_to_xml(text):
    """Convert inline markdown to ReportLab XML."""
    # Inline code
    text = re.sub(r'`([^`]+)`', 
                  r'<font face="Courier" size="9" backColor="#F0F0F0"> \1 </font>', text)
    # Bold+italic
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<b><i>\1</i></b>', text)
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # Italic
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<i>\1</i>', text)
    return text

# ─── Custom Flowables ─────────────────────────────────────────────────

class H1Banner(Flowable):
    """H1 heading: black bg with yellow text and red accent."""
    def __init__(self, text, width=None):
        Flowable.__init__(self)
        self.text = text
        self.width = width or CONTENT_W
        self.height = 48

    def draw(self):
        # Black background
        self.canv.setFillColor(BLACK)
        self.canv.roundRect(0, 0, self.width, self.height, 3, fill=1, stroke=0)
        # Red accent bar on left
        self.canv.setFillColor(RED)
        self.canv.rect(0, 0, 5, self.height, fill=1, stroke=0)
        # Yellow text
        self.canv.setFillColor(YELLOW)
        self.canv.setFont(FONT_HEADING, 17)
        self.canv.drawString(16, 17, self.text)


class SectionNumber(Flowable):
    """Large section number with yellow background pill."""
    def __init__(self, number_text, width=None):
        Flowable.__init__(self)
        self.number_text = number_text
        self.width = width or CONTENT_W
        self.height = 36

    def draw(self):
        # Yellow pill
        self.canv.setFillColor(YELLOW)
        self.canv.roundRect(0, 2, 80, 32, 16, fill=1, stroke=0)
        # Black number text
        self.canv.setFillColor(BLACK)
        self.canv.setFont(FONT_HEADING, 16)
        self.canv.drawCentredString(40, 12, self.number_text)


class YellowDivider(Flowable):
    """Acid yellow divider line."""
    def __init__(self, width=None, thickness=3):
        Flowable.__init__(self)
        self.width = width or CONTENT_W
        self.height = thickness + 4
        self.thickness = thickness

    def draw(self):
        self.canv.setFillColor(YELLOW)
        self.canv.rect(0, 2, self.width, self.thickness, fill=1, stroke=0)


class AccentBox(Flowable):
    """HACK/TIP box with yellow left border and light yellow background."""
    def __init__(self, title, text, width=None):
        Flowable.__init__(self)
        self.title = title
        self.text = text
        self.box_width = width or CONTENT_W
        style = ParagraphStyle('hackbox', fontName=FONT_BODY, fontSize=9.5,
                               leading=13.5, textColor=BLACK)
        self.para = Paragraph(inline_md_to_xml(escape_xml(self.text)), style)
        w, h = self.para.wrap(self.box_width - 36, 10000)
        self.para_h = h
        self.height = h + 28

    def draw(self):
        # Background
        self.canv.setFillColor(LIGHT_YELLOW)
        self.canv.roundRect(0, 0, self.box_width, self.height, 5, fill=1, stroke=0)
        # Yellow left bar
        self.canv.setFillColor(YELLOW)
        self.canv.roundRect(0, 0, 6, self.height, 3, fill=1, stroke=0)
        # Title
        self.canv.setFillColor(RED)
        self.canv.setFont(FONT_HEADING, 10)
        self.canv.drawString(16, self.height - 16, self.title)
        # Text
        self.para.drawOn(self.canv, 16, 6)


class CodeBlock(Flowable):
    """Code block with dark background and syntax highlighting feel."""
    def __init__(self, code_text, width=None):
        Flowable.__init__(self)
        self.code_text = code_text
        self.box_width = width or CONTENT_W
        lines = code_text.split('\n')
        self.line_count = len(lines)
        self.height = max(28, self.line_count * 11.5 + 20)

    def draw(self):
        # Dark background
        self.canv.setFillColor(CODE_BG)
        self.canv.roundRect(0, 0, self.box_width, self.height, 4, fill=1, stroke=0)
        # Yellow left accent
        self.canv.setFillColor(YELLOW)
        self.canv.rect(0, 0, 3, self.height, fill=1, stroke=0)
        # Code text
        self.canv.setFillColor(HexColor("#D4D4D4"))
        self.canv.setFont(FONT_MONO, 7.5)
        y = self.height - 14
        for line in self.code_text.split('\n'):
            if y < 6:
                break
            # Truncate very long lines
            display = line[:100] if len(line) > 100 else line
            self.canv.drawString(14, y, display)
            y -= 11.5


class RedDivider(Flowable):
    """Small red accent divider."""
    def __init__(self, width=None):
        Flowable.__init__(self)
        self.width = width or CONTENT_W
        self.height = 6

    def draw(self):
        self.canv.setFillColor(RED)
        self.canv.rect(0, 2, 60, 2, fill=1, stroke=0)


# ─── Styles ───────────────────────────────────────────────────────────

def create_styles():
    styles = {}
    styles['h2'] = ParagraphStyle(
        'H2', fontName=FONT_HEADING, fontSize=14, leading=19,
        textColor=BLACK, spaceAfter=8, spaceBefore=20
    )
    styles['h3'] = ParagraphStyle(
        'H3', fontName=FONT_HEADING, fontSize=11.5, leading=15,
        textColor=BLACK, spaceAfter=6, spaceBefore=14
    )
    styles['body'] = ParagraphStyle(
        'Body', fontName=FONT_BODY, fontSize=10.5, leading=15,
        textColor=BLACK, spaceAfter=8, alignment=TA_JUSTIFY
    )
    styles['body_bold'] = ParagraphStyle(
        'BodyBold', fontName=FONT_BODY_BOLD, fontSize=10.5, leading=15,
        textColor=BLACK, spaceAfter=8
    )
    styles['list_item'] = ParagraphStyle(
        'ListItem', fontName=FONT_BODY, fontSize=10.5, leading=15,
        textColor=BLACK, leftIndent=24, spaceAfter=4, bulletIndent=10
    )
    styles['list_item_sub'] = ParagraphStyle(
        'ListItemSub', fontName=FONT_BODY, fontSize=10, leading=14,
        textColor=DARK_GREY, leftIndent=44, spaceAfter=3, bulletIndent=30
    )
    styles['blockquote'] = ParagraphStyle(
        'BlockQuote', fontName=FONT_BODY, fontSize=10, leading=14,
        textColor=DARK_GREY, leftIndent=28, rightIndent=14,
        spaceAfter=8, spaceBefore=4, borderPadding=8
    )
    styles['table_header'] = ParagraphStyle(
        'TableHeader', fontName=FONT_HEADING, fontSize=9, leading=12,
        textColor=WHITE, alignment=TA_LEFT
    )
    styles['table_cell'] = ParagraphStyle(
        'TableCell', fontName=FONT_BODY, fontSize=9, leading=12,
        textColor=BLACK
    )
    styles['checkbox'] = ParagraphStyle(
        'Checkbox', fontName=FONT_BODY, fontSize=10.5, leading=15,
        textColor=BLACK, leftIndent=28, spaceAfter=4
    )
    styles['toc_h1'] = ParagraphStyle(
        'TOCH1', fontName=FONT_HEADING, fontSize=12, leading=22,
        textColor=BLACK, leftIndent=0, spaceAfter=2
    )
    styles['toc_h2'] = ParagraphStyle(
        'TOCH2', fontName=FONT_BODY, fontSize=10.5, leading=17,
        textColor=DARK_GREY, leftIndent=24, spaceAfter=1
    )
    styles['toc_h3'] = ParagraphStyle(
        'TOCH3', fontName=FONT_BODY, fontSize=9.5, leading=15,
        textColor=DARK_GREY, leftIndent=48, spaceAfter=1
    )
    styles['disclaimer'] = ParagraphStyle(
        'Disclaimer', fontName=FONT_BODY, fontSize=8, leading=11,
        textColor=HexColor("#999999"), alignment=TA_CENTER
    )
    return styles


# ─── Markdown to Flowables ────────────────────────────────────────────

def parse_table(table_lines, styles):
    if len(table_lines) < 2:
        return []

    def parse_row(line):
        return [c.strip() for c in line.strip('|').split('|')]

    headers = parse_row(table_lines[0])
    rows = [parse_row(line) for line in table_lines[2:]]
    col_count = len(headers)
    
    table_data = []
    header_row = [Paragraph(inline_md_to_xml(escape_xml(h)), styles['table_header']) for h in headers]
    table_data.append(header_row)

    for row in rows:
        padded = row + [''] * (col_count - len(row))
        data_row = [Paragraph(inline_md_to_xml(escape_xml(c)), styles['table_cell']) for c in padded[:col_count]]
        table_data.append(data_row)

    # Column widths
    col_width = CONTENT_W / col_count
    col_widths = [col_width] * col_count
    if col_count >= 3:
        col_widths[0] = col_width * 1.3
        remaining = CONTENT_W - col_widths[0]
        col_widths[1:] = [remaining / (col_count - 1)] * (col_count - 1)

    table = Table(table_data, colWidths=col_widths, repeatRows=1)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), BLACK),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, GREY_LINE),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, GREY_BG]),
        ('LINEBELOW', (0, 0), (-1, 0), 2, YELLOW),
    ]))

    return [Spacer(1, 8), table, Spacer(1, 10)]


def markdown_to_flowables(md_text, styles):
    flowables = []
    lines = md_text.split('\n')
    i = 0
    in_code_block = False
    code_block_lines = []

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # ── Code blocks ──
        if stripped.startswith('```'):
            if in_code_block:
                code_text = '\n'.join(code_block_lines)
                flowables.append(CodeBlock(code_text))
                code_block_lines = []
                in_code_block = False
                i += 1
                continue
            else:
                in_code_block = True
                i += 1
                continue

        if in_code_block:
            code_block_lines.append(line)
            i += 1
            continue

        # ── Table ──
        if stripped.startswith('|') and '|' in stripped[1:]:
            table_lines = [stripped]
            while i + 1 < len(lines) and lines[i + 1].strip().startswith('|'):
                i += 1
                table_lines.append(lines[i].strip())
            flowables.extend(parse_table(table_lines, styles))
            i += 1
            continue

        # ── Horizontal rule ──
        if stripped in ('---', '***', '___'):
            flowables.append(Spacer(1, 10))
            flowables.append(YellowDivider())
            flowables.append(Spacer(1, 10))
            i += 1
            continue

        # ── H1 ──
        if stripped.startswith('# ') and not stripped.startswith('## '):
            heading_text = stripped[2:].strip()
            heading_text = re.sub(r'\*\*(.+?)\*\*', r'\1', heading_text)
            flowables.append(Spacer(1, 14))
            flowables.append(H1Banner(heading_text))
            flowables.append(Spacer(1, 12))
            i += 1
            continue

        # ── H2 ──
        if stripped.startswith('## ') and not stripped.startswith('### '):
            heading_text = stripped[3:].strip()
            heading_text = re.sub(r'\*\*(.+?)\*\*', r'\1', heading_text)
            xml_text = inline_md_to_xml(escape_xml(heading_text))
            flowables.append(Spacer(1, 8))
            flowables.append(RedDivider())
            flowables.append(Paragraph(xml_text, styles['h2']))
            flowables.append(Spacer(1, 4))
            i += 1
            continue

        # ── H3 ──
        if stripped.startswith('### ') and not stripped.startswith('#### '):
            heading_text = stripped[4:].strip()
            heading_text = re.sub(r'\*\*(.+?)\*\*', r'\1', heading_text)
            xml_text = inline_md_to_xml(escape_xml(heading_text))
            flowables.append(Paragraph(xml_text, styles['h3']))
            flowables.append(Spacer(1, 3))
            i += 1
            continue

        # ── Checkbox ──
        if stripped.startswith('- [ ]') or stripped.startswith('- [x]'):
            checked = '[x]' in stripped[:6]
            content = stripped[5:].strip()
            marker = '&#9745;' if checked else '&#9744;'
            xml_content = inline_md_to_xml(escape_xml(content))
            flowables.append(Paragraph(
                f'<font size="13">{marker}</font>  {xml_content}',
                styles['checkbox']
            ))
            i += 1
            continue

        # ── Blockquote ──
        if stripped.startswith('>'):
            content = stripped.lstrip('> ').strip()
            if not content:
                flowables.append(Spacer(1, 4))
            else:
                xml_content = inline_md_to_xml(escape_xml(content))
                flowables.append(Paragraph(xml_content, styles['blockquote']))
            i += 1
            continue

        # ── Unordered list ──
        if stripped.startswith('- ') or stripped.startswith('* '):
            content = stripped[2:].strip()
            xml_content = inline_md_to_xml(escape_xml(content))
            flowables.append(Paragraph(
                f'<bullet>&bull;</bullet>{xml_content}',
                styles['list_item']
            ))
            i += 1
            continue

        # ── Sub-list items ──
        if (line.startswith('  - ') or line.startswith('  * ') or
            line.startswith('   - ') or line.startswith('   * ')):
            content = line.strip()[2:].strip()
            xml_content = inline_md_to_xml(escape_xml(content))
            flowables.append(Paragraph(
                f'<bullet>&#8211;</bullet>{xml_content}',
                styles['list_item_sub']
            ))
            i += 1
            continue

        # ── Ordered list ──
        ol_match = re.match(r'^(\d+)\.\s+(.*)', stripped)
        if ol_match:
            num = ol_match.group(1)
            content = ol_match.group(2).strip()
            xml_content = inline_md_to_xml(escape_xml(content))
            flowables.append(Paragraph(
                f'<bullet>{num}.</bullet>{xml_content}',
                styles['list_item']
            ))
            i += 1
            continue

        # ── Empty line ──
        if not stripped:
            i += 1
            continue

        # ── Regular paragraph ──
        para_lines = [stripped]
        while i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            if (not next_line or next_line.startswith('#') or
                next_line.startswith('- ') or next_line.startswith('* ') or
                next_line.startswith('>') or next_line.startswith('```') or
                next_line.startswith('|') or next_line == '---' or
                re.match(r'^\d+\.', next_line)):
                break
            para_lines.append(next_line)
            i += 1

        para_text = ' '.join(para_lines)

        # Check for HACK boxes
        if para_text.startswith('**HACK:**'):
            hack_content = para_text.replace('**HACK:**', '').strip()
            flowables.append(AccentBox("HACK", hack_content))
        else:
            xml_text = inline_md_to_xml(escape_xml(para_text))
            flowables.append(Paragraph(xml_text, styles['body']))

        i += 1

    return flowables


# ─── Cover Page ───────────────────────────────────────────────────────

def create_brand_mark():
    """Create a brand mark image for the cover page."""
    from reportlab.graphics.shapes import Drawing, Rect, String
    from reportlab.graphics import renderPM
    
    d = Drawing(600, 600)
    d.add(Rect(0, 0, 600, 600, fillColor=BLACK, strokeColor=None))
    # Three yellow bars forming an 'M' shape
    d.add(Rect(70, 120, 90, 300, fillColor=YELLOW, strokeColor=None))
    d.add(Rect(200, 120, 90, 300, fillColor=YELLOW, strokeColor=None))
    d.add(Rect(330, 120, 90, 300, fillColor=YELLOW, strokeColor=None))
    # Red accent
    d.add(Rect(70, 85, 350, 12, fillColor=RED, strokeColor=None))
    # Text
    d.add(String(70, 480, 'MENSHLY', fontSize=48, fillColor=YELLOW, fontName='Helvetica-Bold'))
    d.add(String(70, 425, 'GLOBAL', fontSize=48, fillColor=WHITE, fontName='Helvetica-Bold'))
    # Bottom accent
    d.add(Rect(70, 60, 350, 6, fillColor=YELLOW, strokeColor=None))
    
    img_path = '/tmp/menshly_brand_cover.png'
    renderPM.drawToFile(d, img_path, fmt='PNG', dpi=300)
    return img_path


def build_cover_page(title, price, read_time, tagline="Where AI Meets Revenue"):
    elements = []
    elements.append(Spacer(1, 0.8 * inch))

    # Brand mark image
    try:
        img_path = create_brand_mark()
        img = Image(img_path, width=1.6 * inch, height=1.6 * inch)
        img.hAlign = 'CENTER'
        elements.append(img)
    except:
        pass

    elements.append(Spacer(1, 0.3 * inch))

    # Brand name
    brand_style = ParagraphStyle(
        'Brand', fontName=FONT_HEADING, fontSize=16, leading=20,
        textColor=YELLOW, alignment=TA_CENTER, spaceAfter=6
    )
    elements.append(Paragraph("MENSHLY GLOBAL", brand_style))

    elements.append(Spacer(1, 0.1 * inch))

    # Yellow divider
    elements.append(YellowDivider(width=3 * inch, thickness=2))

    elements.append(Spacer(1, 0.3 * inch))

    # "PLAYBOOK" label
    label_style = ParagraphStyle(
        'Label', fontName=FONT_BODY, fontSize=10, leading=12,
        textColor=HexColor("#888888"), alignment=TA_CENTER, spaceAfter=14,
    )
    elements.append(Paragraph("P L A Y B O O K", label_style))

    # Title
    title_style = ParagraphStyle(
        'CoverTitle', fontName=FONT_HEADING, fontSize=26, leading=32,
        textColor=WHITE, alignment=TA_CENTER, spaceAfter=12
    )
    elements.append(Paragraph(escape_xml(title.upper()), title_style))

    elements.append(Spacer(1, 0.25 * inch))

    # Price
    price_style = ParagraphStyle(
        'Price', fontName=FONT_HEADING, fontSize=40, leading=48,
        textColor=YELLOW, alignment=TA_CENTER, spaceAfter=14
    )
    elements.append(Paragraph(escape_xml(price), price_style))

    elements.append(Spacer(1, 0.05 * inch))

    # Read time
    time_style = ParagraphStyle(
        'ReadTime', fontName=FONT_BODY, fontSize=11, leading=14,
        textColor=HexColor("#999999"), alignment=TA_CENTER, spaceAfter=4
    )
    elements.append(Paragraph(escape_xml(read_time), time_style))

    elements.append(Spacer(1, 1.2 * inch))

    # Tagline
    tag_style = ParagraphStyle(
        'Tagline', fontName=FONT_BODY, fontSize=10, leading=14,
        textColor=HexColor("#777777"), alignment=TA_CENTER
    )
    elements.append(Paragraph(f'<i>"{escape_xml(tagline)}"</i>', tag_style))

    elements.append(Spacer(1, 0.15 * inch))

    # Bottom divider
    elements.append(YellowDivider(width=3 * inch, thickness=2))

    # Copyright
    elements.append(Spacer(1, 0.15 * inch))
    copy_style = ParagraphStyle(
        'Copy', fontName=FONT_BODY, fontSize=7, leading=10,
        textColor=HexColor("#555555"), alignment=TA_CENTER
    )
    elements.append(Paragraph("Copyright 2026 Menshly Global. All rights reserved.", copy_style))

    return elements


# ─── Back Cover ───────────────────────────────────────────────────────

def build_intro_page(title, excerpt, styles):
    """Build a 'How to Use This Playbook' introduction page."""
    elements = []
    elements.append(Spacer(1, 0.3 * inch))
    
    intro_title = ParagraphStyle(
        'IntroTitle', fontName=FONT_HEADING, fontSize=20, leading=24,
        textColor=BLACK, alignment=TA_LEFT, spaceAfter=12
    )
    elements.append(Paragraph("HOW TO USE THIS PLAYBOOK", intro_title))
    elements.append(YellowDivider())
    elements.append(Spacer(1, 16))
    
    body = styles['body']
    
    elements.append(Paragraph(
        "This playbook is designed for execution, not casual reading. Every section contains "
        "specific, actionable procedures that build on each other. Follow them in order. "
        "Complete each procedure before moving to the next. The check-ins at the end of "
        "each module are not suggestions — they are requirements.", body
    ))
    
    elements.append(Spacer(1, 8))
    
    elements.append(Paragraph("<b>Three rules for getting the most from this playbook:</b>", body))
    elements.append(Spacer(1, 4))
    
    rules = [
        "<b>1. Do not skip procedures.</b> Each one builds on the previous. Skipping is the "
        "number one reason people fail to get results from playbooks like this one.",
        "<b>2. Complete every check-in.</b> The check-in lists at the end of each module "
        "are your quality control. If you cannot check every box, go back and complete "
        "the missing items before moving forward.",
        "<b>3. Execute, don't just read.</b> Reading without doing is entertainment, not "
        "execution. Commit to taking action on every procedure before you turn the page."
    ]
    
    for rule in rules:
        elements.append(Paragraph(
            f'<bullet>&bull;</bullet>{rule}',
            styles['list_item']
        ))
    
    elements.append(Spacer(1, 12))
    
    if excerpt:
        # Excerpt box
        excerpt_style = ParagraphStyle(
            'Excerpt', fontName=FONT_BODY, fontSize=10, leading=14,
            textColor=DARK_GREY, leftIndent=8, rightIndent=8,
            spaceAfter=8, spaceBefore=4, alignment=TA_JUSTIFY
        )
        excerpt_text = escape_xml(excerpt)
        elements.append(AccentBox("ABOUT THIS PLAYBOOK", excerpt))
    
    elements.append(Spacer(1, 16))
    elements.append(YellowDivider())
    elements.append(Spacer(1, 8))
    
    # Key icons / format explanation
    format_style = ParagraphStyle(
        'Format', fontName=FONT_BODY, fontSize=9, leading=13,
        textColor=DARK_GREY, spaceAfter=4
    )
    elements.append(Paragraph("<b>Formatting Guide:</b>", body))
    elements.append(Spacer(1, 4))
    
    format_items = [
        '<font backColor="#1E1E1E" color="#D4D4D4"> Code blocks </font> contain exact configurations, scripts, and technical details.',
        '<font color="#F9FF00"> Yellow boxes </font> contain pro tips and shortcuts that save you time.',
        '<font color="#FF0004"> Red accents </font> mark critical steps and warnings.',
        'Checkbox items mark required completion steps at the end of each module.',
    ]
    for item in format_items:
        elements.append(Paragraph(
            f'<bullet>&bull;</bullet>{item}',
            styles['list_item']
        ))
    
    return elements


def build_closing_page(styles):
    """Build a 'Your Next Steps' closing page before the back cover."""
    elements = []
    elements.append(Spacer(1, 0.3 * inch))
    
    closing_title = ParagraphStyle(
        'ClosingTitle', fontName=FONT_HEADING, fontSize=20, leading=24,
        textColor=BLACK, alignment=TA_LEFT, spaceAfter=12
    )
    elements.append(Paragraph("YOUR NEXT STEPS", closing_title))
    elements.append(YellowDivider())
    elements.append(Spacer(1, 16))
    
    body = styles['body']
    
    elements.append(Paragraph(
        "You now have everything you need to start building, selling, and delivering AI-powered "
        "services. The frameworks, scripts, procedures, and tools in this playbook are "
        "battle-tested and proven. The only variable left is your execution.", body
    ))
    
    elements.append(Spacer(1, 10))
    
    next_steps = [
        "<b>This week:</b> Complete the foundation module. Set up your Command Center, "
        "configure your tools, and establish your financial infrastructure. This takes "
        "2-4 hours and costs nothing but your time.",
        "<b>Next week:</b> Build your first automation. Use the Five-Phase Build Process "
        "and the detailed walkthrough in this playbook. Test it thoroughly using the "
        "testing protocol.",
        "<b>Within 30 days:</b> Launch your outreach campaign. Send 50 personalized "
        "emails to prospects in your target market. Book your first discovery calls. "
        "Close your first client.",
        "<b>Ongoing:</b> Deliver exceptional work. Over-communicate with clients. "
        "Build systems that run without you. Scale by hiring and delegating."
    ]
    
    for step in next_steps:
        elements.append(Paragraph(
            f'<bullet>&bull;</bullet>{step}',
            styles['list_item']
        ))
    
    elements.append(Spacer(1, 16))
    elements.append(YellowDivider())
    elements.append(Spacer(1, 12))
    
    # Motivational close
    close_style = ParagraphStyle(
        'Close', fontName=FONT_HEADING, fontSize=14, leading=18,
        textColor=BLACK, alignment=TA_CENTER, spaceAfter=12
    )
    elements.append(Paragraph(
        '"The difference between who you are and who you want to be is what you do."',
        close_style
    ))
    
    elements.append(Spacer(1, 12))
    
    # CTA
    cta_style = ParagraphStyle(
        'CTA', fontName=FONT_BODY, fontSize=11, leading=15,
        textColor=DARK_GREY, alignment=TA_CENTER
    )
    elements.append(Paragraph(
        "Start today. Execute the first procedure. Build momentum.",
        cta_style
    ))
    
    return elements


def build_back_cover():
    elements = []
    elements.append(Spacer(1, 1.5 * inch))

    # Brand mark
    try:
        img_path = create_brand_mark()
        img = Image(img_path, width=1.4 * inch, height=1.4 * inch)
        img.hAlign = 'CENTER'
        elements.append(img)
    except:
        pass

    elements.append(Spacer(1, 0.3 * inch))

    # Brand
    brand_style = ParagraphStyle(
        'BackBrand', fontName=FONT_HEADING, fontSize=24, leading=28,
        textColor=YELLOW, alignment=TA_CENTER, spaceAfter=12
    )
    elements.append(Paragraph("MENSHLY GLOBAL", brand_style))

    elements.append(Spacer(1, 0.15 * inch))
    elements.append(YellowDivider(width=2 * inch, thickness=2))
    elements.append(Spacer(1, 0.25 * inch))

    # Tagline
    tag_style = ParagraphStyle(
        'BackTag', fontName=FONT_BODY, fontSize=12, leading=16,
        textColor=HexColor("#999999"), alignment=TA_CENTER, spaceAfter=30
    )
    elements.append(Paragraph('<i>"Where AI Meets Revenue"</i>', tag_style))

    # URL placeholder
    url_style = ParagraphStyle(
        'URL', fontName=FONT_BODY, fontSize=10, leading=14,
        textColor=HexColor("#777777"), alignment=TA_CENTER, spaceAfter=30
    )
    elements.append(Paragraph("menshly.com", url_style))

    elements.append(Spacer(1, 1 * inch))

    # Disclaimer
    disc_style = ParagraphStyle(
        'Disc', fontName=FONT_BODY, fontSize=7.5, leading=10,
        textColor=HexColor("#555555"), alignment=TA_CENTER
    )
    elements.append(Paragraph(
        "This playbook is for informational and educational purposes only. "
        "The strategies, tools, and procedures described are based on market conditions "
        "at the time of writing and may change. Results vary based on individual effort, "
        "market conditions, and execution quality. Menshly Global makes no guarantees "
        "regarding revenue outcomes. All product names, logos, and brands are property "
        "of their respective owners. Use of any tool or service mentioned in this playbook "
        "is subject to that tool's terms of service and pricing, which may differ from "
        "what is described herein.",
        disc_style
    ))

    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph(
        "Copyright 2026 Menshly Global. All rights reserved. "
        "No part of this publication may be reproduced, distributed, or transmitted "
        "in any form without the prior written permission of Menshly Global. "
        "Unauthorized reproduction or distribution is a violation of applicable laws.",
        disc_style
    ))

    return elements


# ─── TOC Builder ──────────────────────────────────────────────────────

def build_toc(md_text, styles):
    toc_entries = []
    lines = md_text.split('\n')
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('# ') and not stripped.startswith('## '):
            text = stripped[2:].strip()
            text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
            toc_entries.append(('h1', text))
        elif stripped.startswith('## ') and not stripped.startswith('### '):
            text = stripped[3:].strip()
            text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
            toc_entries.append(('h2', text))
        elif stripped.startswith('### ') and not stripped.startswith('#### '):
            text = stripped[4:].strip()
            text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
            toc_entries.append(('h3', text))

    elements = []
    elements.append(Spacer(1, 0.3 * inch))

    toc_title_style = ParagraphStyle(
        'TOCTitle', fontName=FONT_HEADING, fontSize=22, leading=26,
        textColor=BLACK, alignment=TA_LEFT, spaceAfter=16
    )
    elements.append(Paragraph("TABLE OF CONTENTS", toc_title_style))
    elements.append(YellowDivider())
    elements.append(Spacer(1, 20))

    for level, text in toc_entries:
        style_key = f'toc_{level}'
        if style_key in styles:
            if level == 'h1':
                xml_text = f'<font color="{YELLOW.hexval()}">&#9632;</font>  {escape_xml(text)}'
            elif level == 'h2':
                xml_text = f'<font color="{RED.hexval()}">&#8226;</font>  {escape_xml(text)}'
            else:
                xml_text = f'    {escape_xml(text)}'
            elements.append(Paragraph(xml_text, styles[style_key]))

    return elements


# ─── Page Templates ───────────────────────────────────────────────────

def cover_page_template(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(BLACK)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    # Top accent
    canvas.setFillColor(YELLOW)
    canvas.rect(0, PAGE_H - 5, PAGE_W, 5, fill=1, stroke=0)
    # Bottom accent
    canvas.setFillColor(RED)
    canvas.rect(0, 0, PAGE_W, 3, fill=1, stroke=0)
    canvas.restoreState()

def body_page_template(canvas, doc):
    canvas.saveState()
    # Top yellow line
    canvas.setFillColor(YELLOW)
    canvas.rect(MARGIN, PAGE_H - MARGIN + 10, CONTENT_W, 2, fill=1, stroke=0)
    # Header
    canvas.setFillColor(DARK_GREY)
    canvas.setFont(FONT_BODY, 7)
    canvas.drawString(MARGIN, PAGE_H - MARGIN + 16, "MENSHLY GLOBAL")
    canvas.drawRightString(PAGE_W - MARGIN, PAGE_H - MARGIN + 16, "Where AI Meets Revenue")
    # Footer line
    canvas.setStrokeColor(GREY_LINE)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN, MARGIN - 18, PAGE_W - MARGIN, MARGIN - 18)
    # Page number
    canvas.setFillColor(BLACK)
    canvas.setFont(FONT_BODY, 9)
    canvas.drawCentredString(PAGE_W / 2, MARGIN - 30, str(doc.page))
    # Yellow dot
    canvas.setFillColor(YELLOW)
    canvas.circle(PAGE_W / 2 - 16, MARGIN - 27, 2.5, fill=1, stroke=0)
    # Red dot
    canvas.setFillColor(RED)
    canvas.circle(PAGE_W / 2 + 16, MARGIN - 27, 1.5, fill=1, stroke=0)
    canvas.restoreState()

def toc_page_template(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(YELLOW)
    canvas.rect(MARGIN, PAGE_H - MARGIN + 10, CONTENT_W, 2, fill=1, stroke=0)
    canvas.setFillColor(DARK_GREY)
    canvas.setFont(FONT_BODY, 7)
    canvas.drawString(MARGIN, PAGE_H - MARGIN + 16, "MENSHLY GLOBAL")
    canvas.drawRightString(PAGE_W - MARGIN, PAGE_H - MARGIN + 16, "Table of Contents")
    canvas.setStrokeColor(GREY_LINE)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN, MARGIN - 18, PAGE_W - MARGIN, MARGIN - 18)
    canvas.setFillColor(BLACK)
    canvas.setFont(FONT_BODY, 9)
    canvas.drawCentredString(PAGE_W / 2, MARGIN - 30, str(doc.page))
    canvas.restoreState()

def back_cover_template(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(BLACK)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.setFillColor(YELLOW)
    canvas.rect(0, PAGE_H - 5, PAGE_W, 5, fill=1, stroke=0)
    canvas.setFillColor(RED)
    canvas.rect(0, 0, PAGE_W, 3, fill=1, stroke=0)
    canvas.restoreState()


# ─── Main PDF Builder ─────────────────────────────────────────────────

def generate_playbook(md_path, pdf_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    fm = parse_frontmatter(raw_text)
    title = fm.get('title', 'Untitled Playbook')
    price = fm.get('price', '')
    read_time = fm.get('readTime', '')

    content = strip_frontmatter(raw_text)
    content = strip_shortcodes(content)
    content = re.sub(r'\{\{<\s*toc\s*>\}\}', '', content)

    styles = create_styles()

    doc = BaseDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN, bottomMargin=MARGIN,
        title=title,
        author="Menshly Global",
        subject=title,
        creator="Menshly Global PDF Generator"
    )

    cover_frame = Frame(MARGIN, MARGIN, CONTENT_W, PAGE_H - 2 * MARGIN, id='cover')
    toc_frame = Frame(MARGIN, MARGIN, CONTENT_W, PAGE_H - 2 * MARGIN, id='toc')
    body_frame = Frame(MARGIN, MARGIN, CONTENT_W, PAGE_H - 2 * MARGIN, id='body')
    back_frame = Frame(MARGIN, MARGIN, CONTENT_W, PAGE_H - 2 * MARGIN, id='back')

    cover_tpl = PageTemplate(id='cover', frames=[cover_frame], onPage=cover_page_template)
    toc_tpl = PageTemplate(id='toc', frames=[toc_frame], onPage=toc_page_template)
    body_tpl = PageTemplate(id='body', frames=[body_frame], onPage=body_page_template)
    back_tpl = PageTemplate(id='back', frames=[back_frame], onPage=back_cover_template)

    doc.addPageTemplates([cover_tpl, toc_tpl, body_tpl, back_tpl])

    story = []

    # ── Cover ──
    story.append(NextPageTemplate('toc'))
    story.extend(build_cover_page(title, price, read_time))
    story.append(PageBreak())

    # ── TOC ──
    story.append(NextPageTemplate('body'))
    story.extend(build_toc(content, styles))
    story.append(PageBreak())

    # ── Intro Page ──
    excerpt = fm.get('excerpt', '')
    story.extend(build_intro_page(title, excerpt, styles))
    story.append(PageBreak())

    # ── Body ──
    body_flowables = markdown_to_flowables(content, styles)
    story.extend(body_flowables)

    # ── Closing Page ──
    story.append(PageBreak())
    story.extend(build_closing_page(styles))

    # ── Back Cover ──
    story.append(NextPageTemplate('back'))
    story.append(PageBreak())
    story.extend(build_back_cover())

    doc.build(story)
    return os.path.getsize(pdf_path)


# ─── Main ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    playbooks = [
        {
            "name": "AI Automation Agency Playbook",
            "md": "/home/z/my-project/menshly-repo/content/playbooks/ai-automation-agency-playbook.md",
            "pdf": "/home/z/my-project/menshly-repo/static/pdfs/ai-automation-agency-playbook.pdf",
        },
        {
            "name": "Automation Agency Starter Kit",
            "md": "/home/z/my-project/menshly-repo/content/playbooks/automation-agency-starter-kit.md",
            "pdf": "/home/z/my-project/menshly-repo/static/pdfs/automation-agency-starter-kit.pdf",
        },
        {
            "name": "AI Side Hustle Blueprint",
            "md": "/home/z/my-project/menshly-repo/content/playbooks/ai-side-hustle-blueprint.md",
            "pdf": "/home/z/my-project/menshly-repo/static/pdfs/ai-side-hustle-blueprint.pdf",
        },
        {
            "name": "ChatGPT Prompt Engineering Guide",
            "md": "/home/z/my-project/menshly-repo/content/playbooks/chatgpt-prompt-engineering-guide.md",
            "pdf": "/home/z/my-project/menshly-repo/static/pdfs/chatgpt-prompt-engineering-guide.pdf",
        },
    ]

    print("=" * 60)
    print("  MENSHLY GLOBAL - Playbook PDF Generator v2")
    print("=" * 60)
    print()

    all_ok = True
    for pb in playbooks:
        print(f"Generating: {pb['name']}...")
        try:
            size = generate_playbook(pb['md'], pb['pdf'])
            size_kb = size / 1024
            status = "OK" if size_kb >= 100 else f"WARN ({size_kb:.0f}KB < 100KB)"
            if size_kb < 100:
                all_ok = False
            print(f"  -> {os.path.basename(pb['pdf'])} ({size_kb:.1f} KB) [{status}]")
        except Exception as e:
            import traceback
            print(f"  -> ERROR: {e}")
            traceback.print_exc()
            all_ok = False

    print()
    # Print page counts
    try:
        import fitz
        print("Page counts:")
        for pb in playbooks:
            if os.path.exists(pb['pdf']):
                doc = fitz.open(pb['pdf'])
                print(f"  {os.path.basename(pb['pdf'])}: {doc.page_count} pages")
                doc.close()
    except ImportError:
        pass

    print()
    print("Final PDF file sizes:")
    for pb in playbooks:
        if os.path.exists(pb['pdf']):
            size = os.path.getsize(pb['pdf'])
            print(f"  {os.path.basename(pb['pdf'])}: {size/1024:.1f} KB")
        else:
            print(f"  {os.path.basename(pb['pdf'])}: MISSING")

    print()
    if all_ok:
        print("All 4 PDFs generated successfully (100KB+ each)!")
    else:
        print("Some PDFs are under 100KB - may need more content density.")
