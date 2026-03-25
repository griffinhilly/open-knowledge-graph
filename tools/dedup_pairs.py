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
DEDUP_PAIRS = [
    ("reduction-intertheoretic-relations", "reduction-emergence-science"),
    ("group-epistemology-collective", "collective-knowledge-and-group-epistemology"),
    ("eliminative-materialism-thesis", "eliminative-materialism"),
    ("incommensurability-of-paradigms", "incommensurability-kuhn"),
    ("risk-protective-factors-developmental-resilience", "resilience-and-protective-factors-development"),
    ("reading-following-simple-recipes", "reading-recipes"),
    ("intertextuality-allusion-analysis", "intertextuality-and-allusion"),
    ("gross-motor-development-and-locomotion", "gross-motor-milestones-locomotion"),
    ("prose-poetry", "prose-poetry-hybrid-form"),
    ("cosmopolitanism-global-justice", "international-justice-cosmopolitanism"),
    ("narrow-content-individuation", "narrow-intrinsic-content-mind"),
    ("unreliable-narrator-detection", "unreliable-narrator-analysis"),
    ("bonds-and-fixed-income-securities", "bonds-and-fixed-income"),
    ("subgroup-analysis-and-heterogeneity", "subgroup-analysis-heterogeneity"),
    ("sleep-architecture-development-and-circadian-rhythms", "sleep-circadian-rhythm-and-development"),
    ("mediation-analysis-epidemiology", "mediation-analysis-pathways"),
    ("apostrophe-direct-address", "apostrophe-in-poetry"),
    ("type-identity-theory-details", "type-identity-theory"),
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
        # Replace the ID in prerequisites and builds-toward
        # Only replace in prerequisite/builds-toward contexts, not in IDs or titles
        # Use word-boundary matching to avoid partial replacements
        new_text = re.sub(
            r'(?<=\bid: )' + re.escape(delete_id) + r'(?=\s|$)',
            keep_id, text)
        if new_text == text:
            # Also try in builds-toward lists (bare strings)
            new_text = re.sub(
                r'(?<=- )' + re.escape(delete_id) + r'(?=\s|$)',
                keep_id, text)
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

        print(f"  {delete_id} → {keep_id}")

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
