#!/usr/bin/env python3
"""
Generate Questions and Explainer sections for creative-nonfiction topics.
Processes all .md files in the current directory.
"""

import os
import re
import sys
from pathlib import Path

# Get all .md files in the directory
md_dir = Path(__file__).parent
md_files = sorted(md_dir.glob("*.md"))

# Skip the script itself and the _domain.yml file
md_files = [f for f in md_files if f.name not in ["generate_qa.py", "_domain.yml"]]

print(f"Found {len(md_files)} topic files")

# For each file, read it and check if it already has Questions and Explainer
for md_file in md_files[:5]:  # Start with first 5 for testing
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if already has Questions section
    if "## Questions" in content:
        print(f"SKIP: {md_file.name} - already has Questions section")
        continue

    # Extract frontmatter and Core Idea
    frontmatter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not frontmatter_match:
        print(f"ERROR: {md_file.name} - no frontmatter")
        continue

    # Find Core Idea section
    core_idea_match = re.search(r'## Core Idea\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
    if not core_idea_match:
        print(f"ERROR: {md_file.name} - no Core Idea")
        continue

    core_idea_text = core_idea_match.group(1).strip()
    title_match = re.search(r"title: '(.+?)'", frontmatter_match.group(1))
    title = title_match.group(1) if title_match else md_file.stem

    print(f"\nProcessing: {title}")
    print(f"Core Idea: {core_idea_text[:100]}...")

print("\nScript preview complete. Ready to generate questions and explainers.")
print("Use batch generation via Claude API for quality assurance.")
