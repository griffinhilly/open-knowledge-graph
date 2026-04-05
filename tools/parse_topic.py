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
