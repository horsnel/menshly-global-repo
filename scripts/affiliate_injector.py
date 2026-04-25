#!/usr/bin/env python3
"""Affiliate Link Injector for Menshly Global articles.

Reads affiliate data from data/affiliates.yaml and data/affiliate_links.json,
and provides functions to inject affiliate links into article markdown content.

Affiliate links are embedded naturally within the article text:
- Tool mentions get linked to affiliate URLs
- A "Recommended Tools" section is appended with affiliate links
- Playbook articles get affiliate tool cards
"""

import json
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
AFFILIATES_YAML = PROJECT_ROOT / "data" / "affiliates.yaml"
AFFILIATES_JSON = PROJECT_ROOT / "data" / "affiliate_links.json"


def _load_affiliates() -> dict:
    """Load all affiliate link data from both YAML and JSON files."""
    affiliates = {}

    # Load from JSON
    if AFFILIATES_JSON.exists():
        try:
            data = json.loads(AFFILIATES_JSON.read_text())
            for link in data.get("links", []):
                key = link["name"].lower().replace(".", "").replace(" ", "")
                affiliates[key] = {
                    "name": link["name"],
                    "url": link["url"],
                    "category": link.get("category", ""),
                    "description": link.get("description", ""),
                }
        except (json.JSONDecodeError, Exception) as e:
            print(f"  Warning: Could not load affiliates JSON: {e}")

    # Load from YAML (simple parser)
    if AFFILIATES_YAML.exists():
        try:
            text = AFFILIATES_YAML.read_text()
            current_key = None
            current_data = {}
            for line in text.split("\n"):
                stripped = line.strip()
                if stripped.startswith("#") or not stripped:
                    continue
                # Top-level key (not indented)
                if not line.startswith(" ") and ":" in stripped:
                    if current_key:
                        affiliates[current_key] = current_data
                    key = stripped.split(":")[0].strip()
                    current_key = key.lower().replace(".", "").replace(" ", "")
                    current_data = {}
                # Nested value
                elif current_key and stripped:
                    if ":" in stripped:
                        k, v = stripped.split(":", 1)
                        k = k.strip()
                        v = v.strip().strip('"').strip("'")
                        if k in ("name", "url", "description"):
                            current_data[k] = v
            if current_key:
                affiliates[current_key] = current_data
        except Exception as e:
            print(f"  Warning: Could not load affiliates YAML: {e}")

    return affiliates


AFFILIATES = _load_affiliates()


def get_affiliate_url(tool_name: str) -> str | None:
    """Get the affiliate URL for a tool name."""
    key = tool_name.lower().replace(".", "").replace(" ", "").replace("-", "")
    affiliate = AFFILIATES.get(key)
    if affiliate:
        return affiliate["url"]
    # Try partial match
    for k, v in AFFILIATES.items():
        if tool_name.lower() in v.get("name", "").lower():
            return v["url"]
    return None


def get_affiliate_data(tool_name: str) -> dict | None:
    """Get full affiliate data for a tool name."""
    key = tool_name.lower().replace(".", "").replace(" ", "").replace("-", "")
    if key in AFFILIATES:
        return AFFILIATES[key]
    for k, v in AFFILIATES.items():
        if tool_name.lower() in v.get("name", "").lower():
            return v
    return None


def inject_affiliate_links(content: str, suggested_affiliates: list[str] = None) -> str:
    """Inject affiliate links into article markdown content.

    Finds tool mentions and wraps them with affiliate links.
    Only links the FIRST mention of each tool to avoid over-linking.

    Args:
        content: The markdown article content
        suggested_affiliates: List of affiliate tool names to prioritize

    Returns:
        Modified markdown content with affiliate links
    """
    linked_tools = set()  # Track which tools we've already linked

    # Build a list of tool names to look for (prioritize suggested)
    all_tools = []
    if suggested_affiliates:
        for name in suggested_affiliates:
            data = get_affiliate_data(name)
            if data:
                all_tools.append(data)

    # Add remaining affiliates
    for key, data in AFFILIATES.items():
        if data not in all_tools:
            all_tools.append(data)

    for tool in all_tools:
        name = tool.get("name", "")
        url = tool.get("url", "")
        if not name or not url:
            continue

        # Skip already-linked tools
        if name.lower() in linked_tools:
            continue

        # Pattern 1: Bold tool mention like **Make.com** or **Make.com — $16/mo**
        pattern_bold = rf'(\*\*{re.escape(name)}[^*]*\*\*)'
        match = re.search(pattern_bold, content)
        if match:
            matched_text = match.group(1)
            # Check if already linked
            idx = match.start()
            if idx > 0 and content[idx-2:idx] == "](" :
                continue
            # Replace with linked version
            replacement = f'[{matched_text}]({url})'
            content = content[:match.start()] + replacement + content[match.end():]
            linked_tools.add(name.lower())
            continue

        # Pattern 2: Plain tool mention (not already in a link)
        pattern_plain = rf'(?<!\[)(?<!\(){re.escape(name)}(?![$\w])(?!\]\()'
        match = re.search(pattern_plain, content)
        if match:
            # Only link the first occurrence
            replacement = f'[{name}]({url})'
            content = content[:match.start()] + replacement + content[match.end():]
            linked_tools.add(name.lower())

    return content


def generate_tools_section(suggested_affiliates: list[str] = None) -> str:
    """Generate a 'Recommended Tools' section with affiliate links.

    This section is appended to articles to drive affiliate conversions.

    Args:
        suggested_affiliates: List of affiliate tool names to include

    Returns:
        Markdown string with the tools section
    """
    tools = []
    if suggested_affiliates:
        for name in suggested_affiliates:
            data = get_affiliate_data(name)
            if data:
                tools.append(data)

    # If fewer than 3, add some defaults
    default_categories = ["automation", "ai", "productivity"]
    if len(tools) < 3:
        for key, data in AFFILIATES.items():
            if data not in tools and data.get("category") in default_categories:
                tools.append(data)
                if len(tools) >= 5:
                    break

    if not tools:
        return ""

    lines = [
        "## Recommended Tools",
        "",
        "These are the tools we recommend for building and scaling AI automation businesses:",
        "",
    ]

    for tool in tools[:8]:
        name = tool.get("name", "")
        url = tool.get("url", "")
        desc = tool.get("description", "")
        if name and url:
            lines.append(f"- **[{name}]({url})** — {desc}")

    lines.append("")
    return "\n".join(lines)


def generate_playbook_affiliate_cta(playbook_slug: str, suggested_affiliates: list[str] = None) -> str:
    """Generate a playbook-specific affiliate CTA section for opportunity/intelligence articles.

    This creates a visual callout that links to tools mentioned in the playbook
    with affiliate links.
    """
    tools = []
    if suggested_affiliates:
        for name in suggested_affiliates:
            data = get_affiliate_data(name)
            if data:
                tools.append(data)

    if not tools:
        return ""

    lines = [
        "{{% accent-box %}}",
        "**Tool Stack for This Playbook:**",
        "",
    ]

    for tool in tools[:6]:
        name = tool.get("name", "")
        url = tool.get("url", "")
        if name and url:
            lines.append(f"- [{name}]({url})")

    lines.append("{{% /accent-box %}}")
    lines.append("")
    return "\n".join(lines)
