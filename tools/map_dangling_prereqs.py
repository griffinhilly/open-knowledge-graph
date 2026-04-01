"""Map dangling prerequisite IDs to actual topic file IDs.

Outputs a mapping table for human review before applying fixes.
"""
import os
import re
import yaml
from pathlib import Path
from difflib import SequenceMatcher

DOMAINS_DIR = Path("domains")

def load_all_topic_ids():
    """Return dict of id -> filepath for all topics."""
    topics = {}
    for md in DOMAINS_DIR.rglob("*.md"):
        if md.name.startswith("_"):
            continue
        topic_id = md.stem
        topics[topic_id] = str(md)
    return topics

def find_dangling_prereqs(all_ids):
    """Find all prerequisite references that don't match any topic file."""
    dangling = {}  # dangling_id -> list of (file, type)
    for md in DOMAINS_DIR.rglob("*.md"):
        if md.name.startswith("_"):
            continue
        try:
            text = md.read_text(encoding="utf-8")
        except:
            continue
        # Parse YAML frontmatter
        if not text.startswith("---"):
            continue
        end = text.find("---", 3)
        if end == -1:
            continue
        try:
            fm = yaml.safe_load(text[3:end])
        except:
            continue
        if not fm or "prerequisites" not in fm:
            continue
        for prereq in fm["prerequisites"]:
            if isinstance(prereq, dict) and "id" in prereq:
                pid = prereq["id"]
                if pid not in all_ids:
                    if pid not in dangling:
                        dangling[pid] = []
                    dangling[pid].append((str(md), prereq.get("type", "hard")))
    return dangling

def find_best_match(dangling_id, all_ids):
    """Find the best matching actual topic ID for a dangling reference."""
    candidates = []

    # Exact substring matches (dangling is prefix or suffix of actual)
    for actual_id in all_ids:
        if actual_id.startswith(dangling_id + "-") or actual_id.endswith("-" + dangling_id):
            candidates.append((actual_id, 0.9, "substring"))
        elif dangling_id in actual_id or actual_id in dangling_id:
            candidates.append((actual_id, 0.7, "contains"))

    # Fuzzy match on full ID
    for actual_id in all_ids:
        ratio = SequenceMatcher(None, dangling_id, actual_id).ratio()
        if ratio > 0.6:
            candidates.append((actual_id, ratio, "fuzzy"))

    # Deduplicate, keep best score per ID
    best = {}
    for cid, score, method in candidates:
        if cid not in best or score > best[cid][0]:
            best[cid] = (score, method)

    # Sort by score descending
    ranked = sorted(best.items(), key=lambda x: -x[1][0])
    return ranked[:5]  # top 5 candidates

def apply_fixes(fixes, dry_run=True):
    """Apply prerequisite ID replacements across topic files.

    fixes: dict of {dangling_id: replacement_id}
    Returns count of files modified.
    """
    modified = 0
    for md in DOMAINS_DIR.rglob("*.md"):
        if md.name.startswith("_"):
            continue
        try:
            text = md.read_text(encoding="utf-8")
        except:
            continue
        new_text = text
        for old_id, new_id in fixes.items():
            # Replace in prerequisite id fields: "  id: old_id" or "- id: old_id"
            new_text = re.sub(
                rf'((?:- )?id: ){re.escape(old_id)}(\s)',
                rf'\g<1>{new_id}\2',
                new_text
            )
            # Also in builds-toward lists: "  - old_id"
            new_text = re.sub(
                rf'(  - ){re.escape(old_id)}(\s)',
                rf'\g<1>{new_id}\2',
                new_text
            )
        if new_text != text:
            modified += 1
            if not dry_run:
                md.write_text(new_text, encoding="utf-8")
    return modified


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Apply high-confidence fixes (>=0.85)")
    parser.add_argument("--threshold", type=float, default=0.85, help="Min score for auto-fix")
    parser.add_argument("--remove-unmatched", action="store_true", help="Remove prereqs with no good match")
    args = parser.parse_args()

    all_ids = load_all_topic_ids()
    dangling = find_dangling_prereqs(all_ids)

    total_refs = sum(len(v) for v in dangling.values())
    print(f"Found {total_refs} dangling refs across {len(dangling)} unique IDs\n")

    fixes = {}
    medium = []
    unmatched = []

    for did in sorted(dangling.keys()):
        refs = dangling[did]
        matches = find_best_match(did, all_ids)

        if matches and matches[0][1][0] >= args.threshold:
            best_id = matches[0][0]
            best_score = matches[0][1][0]
            fixes[did] = best_id
            print(f"FIX: {did} -> {best_id} ({best_score:.2f}, {len(refs)} refs)")
        elif matches and matches[0][1][0] >= 0.70:
            medium.append((did, len(refs), matches[:3]))
            print(f"REVIEW: {did} ({len(refs)} refs)")
            for mid, (score, method) in matches[:3]:
                print(f"    {score:.2f} [{method}] -> {mid}")
        else:
            unmatched.append((did, len(refs)))
            print(f"NO_MATCH: {did} ({len(refs)} refs)")

    fix_refs = sum(len(dangling[d]) for d in fixes)
    med_refs = sum(r for _, r, _ in medium)
    unm_refs = sum(r for _, r in unmatched)

    print(f"\n--- SUMMARY ---")
    print(f"Auto-fix:   {len(fixes)} IDs, {fix_refs} refs")
    print(f"Review:     {len(medium)} IDs, {med_refs} refs")
    print(f"Unmatched:  {len(unmatched)} IDs, {unm_refs} refs")

    if args.apply and fixes:
        print(f"\nApplying {len(fixes)} fixes...")
        count = apply_fixes(fixes, dry_run=False)
        print(f"Modified {count} files.")
        # Verify
        dangling_after = find_dangling_prereqs(all_ids)
        remaining = sum(len(v) for v in dangling_after.values())
        print(f"Remaining dangling refs: {remaining}")


if __name__ == "__main__":
    main()
