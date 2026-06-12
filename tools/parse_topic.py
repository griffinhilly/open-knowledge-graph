#!/usr/bin/env python3
"""Shared topic file parsing for the Open Knowledge Graph toolchain.

Every CI-pipeline tool and most offline tools need to parse topic markdown
files.  This module provides the canonical implementations so parsing
behaviour is consistent across the entire toolchain.

Functions
---------
parse_topic(filepath)   -> (data, body)     core parser
parse_frontmatter(filepath) -> data         convenience — metadata only
parse_sections(body)    -> {name: content}   ## heading splitter
extract_questions(body) -> [question_dicts]  ## Questions YAML block
meta_description(text)  -> str               plain-text summary for <meta>
seo_meta_tags(...)      -> str               canonical + description + og block
"""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install with: pip install pyyaml")
    sys.exit(1)

_FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)", re.DOTALL)
_SECTION_RE = re.compile(r"^##\s+(.+)$")
_QUESTIONS_RE = re.compile(r"## Questions\s*\n+```ya?ml\s*\n(.*?)```", re.DOTALL)

# Canonical site root for all generated pages (no trailing slash).
# Custom domain since Jun 2026; griffinhilly.github.io/open-knowledge-graph
# 301-redirects here once the Pages custom domain + DNS are configured.
SITE_BASE_URL = "https://openknowledgegraph.com"

# Cloudflare Web Analytics beacon (cookieless RUM). The token is public by
# design (it appears in page source on every site using CF analytics).
# Manual installation — Cloudflare-side auto-injection must stay OFF or
# every visit double-counts. Rides along in seo_meta_tags(); pages that
# build their own <head> without it (tag pages, assessment) must include
# ANALYTICS_SNIPPET directly.
ANALYTICS_SNIPPET = (
    "<script defer src='https://static.cloudflareinsights.com/beacon.min.js' "
    "data-cf-beacon='{\"token\": \"18b44399b1e04e75a329f39affeb8307\"}'></script>"
)

_MD_TAG_RE = re.compile(r"</?[a-zA-Z][^<>]*>")  # HTML tags only, not "x < 5"
_MD_QUOTE_RE = re.compile(r"^\s*>\s?", re.MULTILINE)
_MD_STRIP_RE = re.compile(r"[*_`#\[\]]|\(http[^)]*\)")


def meta_description(text, limit=160):
    """Reduce markdown *text* to a plain-text snippet for <meta name=description>.

    Strips HTML tags, blockquote markers, and markdown syntax (preserving
    inline notation like ``A -> B``), collapses whitespace, and cuts at a
    word boundary within *limit* characters (adding an ellipsis when cut).
    """
    plain = _MD_TAG_RE.sub("", text or "")
    plain = _MD_QUOTE_RE.sub("", plain)
    plain = _MD_STRIP_RE.sub("", plain)
    plain = " ".join(plain.split())
    if len(plain) <= limit:
        return plain
    cut = plain[:limit].rsplit(" ", 1)[0].rstrip(",;:.")
    return cut + "…"


def seo_meta_tags(title, description, path, og_type="website", image=None):
    """Build the shared SEO <head> block: description, canonical, Open Graph.

    *path* is the page location relative to the site root, e.g.
    ``""`` (index), ``"quiz.html"``, or ``"topics/fractions.html"``.
    *image* is an absolute og:image URL; defaults to the site-wide share
    card (rendered by tools/render_og_cards.py at 1200x630).
    Caller is responsible for inserting the returned string inside <head>.
    """
    import html as _html
    url = SITE_BASE_URL + "/" + path.lstrip("/")
    img = image or (SITE_BASE_URL + "/og/default.png")
    t = _html.escape(title, quote=True)
    d = _html.escape(description, quote=True)
    return f"""<meta name="description" content="{d}">
<link rel="canonical" href="{url}">
<meta property="og:site_name" content="Open Knowledge Graph">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
{ANALYTICS_SNIPPET}"""


def parse_topic(filepath):
    """Parse a topic markdown file.

    Returns (data, body) where *data* is the YAML frontmatter dict and
    *body* is everything after the closing ``---``.
    Returns (None, "") on any parse failure.
    """
    text = filepath.read_text(encoding="utf-8")
    match = _FM_RE.match(text)
    if not match:
        return None, ""
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None, ""
    if not isinstance(data, dict):
        return None, ""
    return data, match.group(2)


def parse_frontmatter(filepath):
    """Extract just the YAML frontmatter dict.  Returns dict or None."""
    data, _ = parse_topic(filepath)
    return data


def parse_sections(body):
    """Split markdown *body* on ``## Heading`` lines.

    Returns ``{heading_text: content_below}`` with leading/trailing
    whitespace stripped from each section's content.
    """
    sections = {}
    current_section = None
    current_lines = []
    for line in body.splitlines():
        header_match = _SECTION_RE.match(line)
        if header_match:
            if current_section:
                sections[current_section] = "\n".join(current_lines).strip()
            current_section = header_match.group(1).strip()
            current_lines = []
        elif current_section:
            current_lines.append(line)
    if current_section:
        sections[current_section] = "\n".join(current_lines).strip()
    return sections


def extract_questions(body):
    """Extract the question list from a ``## Questions`` YAML code block.

    Returns a list of question dicts, or an empty list when the section
    is missing, empty, or contains unparseable YAML.
    """
    match = _QUESTIONS_RE.search(body)
    if not match:
        return []
    try:
        questions = yaml.safe_load(match.group(1))
        return questions if isinstance(questions, list) else []
    except yaml.YAMLError:
        return []
