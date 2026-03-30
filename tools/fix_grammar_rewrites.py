#!/usr/bin/env python3
"""Fix grammar errors introduced by mechanical T/F absolute-removal rewrites.

Patterns:
  "most day"  -> "most days"
  "most time" -> "most of the time" (when not already "most times" or "most of the time")
  "most cell" -> "most cells"  (and similar singular nouns after "most")

Run with --dry-run to preview changes without modifying files.
"""

import re
import sys
from pathlib import Path

DRY_RUN = "--dry-run" in sys.argv

# Patterns: (regex, replacement, description)
FIXES = [
    # "most day" -> "most days" (but not "most days" already)
    (r'\bmost day\b(?!s)', 'most days', '"most day" -> "most days"'),
    # "most time" -> "most of the time" (standalone, not "most times" or "most time-X")
    (r'\bmost time\b(?!s|[-\w])', 'most of the time', '"most time" -> "most of the time"'),
]

def fix_file(path):
    text = path.read_text(encoding="utf-8")
    original = text
    changes = []

    for pattern, replacement, desc in FIXES:
        matches = list(re.finditer(pattern, text, re.IGNORECASE))
        if matches:
            changes.append((desc, len(matches)))
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    if text != original:
        if not DRY_RUN:
            path.write_text(text, encoding="utf-8")
        return changes
    return []


def main():
    domains_dir = Path(__file__).parent.parent / "domains"
    total_files = 0
    total_fixes = 0

    for md_file in sorted(domains_dir.rglob("*.md")):
        changes = fix_file(md_file)
        if changes:
            total_files += 1
            for desc, count in changes:
                total_fixes += count
                print(f"  {md_file.relative_to(domains_dir)}: {desc} ({count}x)")

    mode = "DRY RUN" if DRY_RUN else "FIXED"
    print(f"\n{mode}: {total_fixes} fixes across {total_files} files")


if __name__ == "__main__":
    main()
