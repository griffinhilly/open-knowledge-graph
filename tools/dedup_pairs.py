#!/usr/bin/env python3
"""Merge duplicate topic pairs: delete the weaker file, redirect references.

Usage:
    python tools/dedup_pairs.py --dry-run
    python tools/dedup_pairs.py --apply
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required.")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "domains"

# (delete_id, keep_id) — from duplicate analysis
# Round 6: 14 literature domain duplicates (Phase 10.5 double-generation)
DEDUP_PAIRS = [
    ("children-boarding-school-narrative-tradition", "boarding-school-narrative-tradition"),
    ("fairy-tale-retelling-contemporary-children", "fairy-tale-retellings-contemporary-children"),
    ("world-literature-debates-critical", "world-literature-debates"),
    ("ai-authorship-originality-debate", "ai-generation-authorship-originality-debate"),
    ("apollinaire-calligrammes-shaped-form", "apollinaire-calligrammes"),
    ("branching-narrative-choice-design", "branching-narrative-choice"),
    ("generative-poetry-algorithmic", "generative-poetry-algorithms-text"),
    ("inform-language-authoring", "inform-language-fiction-authoring"),
    ("narrative-voice-and-authorial-style", "narrative-voice"),
    ("historical-fiction-research-imagination", "historical-fiction-research-invention"),
    ("space-opera-galactic-epic-scale", "space-opera-galactic-scale"),
    ("literary-argument-thesis-development", "literary-argument-thesis"),
    ("concrete-poetry", "concrete-poetry-visual"),
    ("arabian-nights-frame-narrative-storytelling", "arabian-nights-frame"),
]


def find_topic_file(topic_id):
    """Find the .md file for a topic ID."""
    for f in DOMAINS_DIR.rglob(f"{topic_id}.md"):
        return f
    return None


def find_references(topic_id):
    """Find all files that reference a topic ID in their frontmatter."""
    refs = []
    for f in DOMAINS_DIR.rglob("*.md"):
        text = f.read_text(encoding="utf-8")
        # Check prerequisites and builds-toward for the ID
        if topic_id in text:
            refs.append(f)
    return refs


def redirect_references(delete_id, keep_id, dry_run=True):
    """Replace all references to delete_id with keep_id in other files."""
    refs = find_references(delete_id)
    modified = 0
    for f in refs:
        # Skip the file being deleted
        if f.stem == delete_id:
            continue
        text = f.read_text(encoding="utf-8")
        # Replace the ID in prerequisites (- id: X format)
        new_text = re.sub(
            r'(?<=\bid: )' + re.escape(delete_id) + r'(?=\s|$)',
            keep_id, text)
        # Also replace in builds-toward lists (- X format)
        new_text = re.sub(
            r'(?<=- )' + re.escape(delete_id) + r'(?=\s|$)',
            keep_id, new_text)
        if new_text != text:
            if not dry_run:
                f.write_text(new_text, encoding="utf-8")
            modified += 1
            print(f"    {'Would update' if dry_run else 'Updated'}: {f.relative_to(ROOT)}")
    return modified


def main():
    parser = argparse.ArgumentParser(description="Deduplicate topic pairs")
    parser.add_argument("--apply", action="store_true", help="Apply changes (default: dry-run)")
    args = parser.parse_args()
    dry_run = not args.apply

    print(f"Deduplicating {len(DEDUP_PAIRS)} pairs ({'DRY RUN' if dry_run else 'APPLYING'})\n")

    total_deleted = 0
    total_redirected = 0

    for delete_id, keep_id in DEDUP_PAIRS:
        delete_file = find_topic_file(delete_id)
        keep_file = find_topic_file(keep_id)

        if not delete_file:
            print(f"  SKIP {delete_id}: file not found")
            continue
        if not keep_file:
            print(f"  SKIP {delete_id}: keeper {keep_id} not found")
            continue

        print(f"  {delete_id} -> {keep_id}")

        # Redirect references
        redirected = redirect_references(delete_id, keep_id, dry_run)
        total_redirected += redirected

        # Delete the file
        if not dry_run:
            delete_file.unlink()
        total_deleted += 1
        print(f"    {'Would delete' if dry_run else 'Deleted'}: {delete_file.relative_to(ROOT)}")

    print(f"\nSummary: {total_deleted} files {'to delete' if dry_run else 'deleted'}, "
          f"{total_redirected} files {'to update' if dry_run else 'updated'}")

    if dry_run:
        print("\nUse --apply to execute.")


if __name__ == "__main__":
    main()
