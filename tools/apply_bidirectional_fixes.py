#!/usr/bin/env python3
"""Apply bidirectional pair resolutions.

For each pair, removes the backwards builds-toward entry.
For "drop both" pairs, removes builds-toward in both directions.
"""

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

# Format: (topic_A, topic_B, direction)
# direction: "A->B" means A comes first, remove B's builds-toward A
#            "B->A" means B comes first, remove A's builds-toward B
#            "drop" means remove builds-toward in both directions
DECISIONS = [
    # Arts & Aesthetics
    ("design-systems-and-consistency", "responsive-design-principles", "drop"),
    ("responsive-design-principles", "user-centered-design-thinking", "B->A"),
    ("chiaroscuro", "portraiture-fundamentals", "A->B"),
    ("chiaroscuro", "still-life-composition", "A->B"),
    # Biology
    ("biodiversity-metrics", "island-biogeography", "A->B"),
    ("cladistics-and-systematics", "molecular-evolution", "A->B"),
    ("keystone-species", "trophic-levels-and-food-webs", "B->A"),
    # Chemistry
    ("enols-and-enolate-chemistry", "nucleophilic-acyl-substitution", "B->A"),
    # Computer Science
    ("disk-scheduling", "io-management", "B->A"),
    # Earth & Space
    ("nebulae-and-star-formation", "planetary-formation", "A->B"),
    ("radiometric-dating", "stratigraphy", "B->A"),
    # Economics
    ("monetary-policy-tools", "phillips-curve", "A->B"),
    # Formal Sciences
    ("adjoint-functors", "limits-and-colimits", "B->A"),
    # Health & Human Dev
    ("bone-remodeling-and-homeostasis", "endocrine-glands-and-hormones", "B->A"),
    ("adolescent-brain-and-behavioral-development", "moral-development-in-children", "drop"),
    # History
    ("mongol-conquest-effects", "silk-road-medieval-era", "B->A"),
    ("congress-of-vienna", "nationalism-and-nation-states", "A->B"),
    # Language & Literature
    ("narrative-writing", "pathos-and-emotional-appeal", "B->A"),
    ("narrative-voice", "stream-of-consciousness", "A->B"),
    ("intertextuality-and-allusion", "literary-argument-writing", "A->B"),
    ("literary-argument-writing", "thematic-development", "B->A"),
    ("imagery-in-poetry", "poetic-voice-and-tone", "A->B"),
    # Mathematics
    ("estimating-lengths", "measuring-in-feet-and-meters", "B->A"),
    ("money-word-problems", "two-step-word-problems", "drop"),
    ("estimation-in-multiplication", "two-digit-by-one-digit-multiplication", "B->A"),
    ("multiplication-division-relationship", "unknown-factor-problems", "A->B"),
    ("dividing-decimals", "fractions-as-division", "B->A"),
    # Music
    ("contrapuntal-composition", "texture-in-composition", "B->A"),
    ("improvisation-frameworks", "lead-sheet-notation", "B->A"),
    ("ostinato-and-ground-bass", "theme-and-variations", "A->B"),
    ("augmented-sixth-chords", "modulation-techniques", "A->B"),
    ("chromatic-mediant-chords", "modulation-techniques", "A->B"),
    ("dominant-seventh-resolution", "four-part-writing", "A->B"),
    ("four-part-writing", "species-counterpoint", "B->A"),
    ("compound-meter", "rhythm-and-syncopation", "B->A"),
    # Philosophy
    ("a-priori-and-a-posteriori", "cartesian-skepticism", "A->B"),
    ("essentialism-and-accidentalism", "possible-worlds-semantics", "A->B"),
    # Physics
    ("calorimetry", "latent-heat", "A->B"),
    # Social Sciences
    ("geopolitics-and-power", "resource-geography", "B->A"),
]


def find_topic_file(topic_id):
    """Find the .md file for a topic ID."""
    matches = list(DOMAINS_DIR.rglob(f"{topic_id}.md"))
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        print(f"  WARNING: Multiple files for {topic_id}: {matches}")
        return matches[0]
    return None


def remove_builds_toward_entry(filepath, target_id, dry_run=False):
    """Remove a specific entry from a topic's builds-toward list.

    Returns True if a change was made.
    """
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return False

    fm_text = match.group(1)
    data = yaml.safe_load(fm_text)
    builds = data.get("builds-toward", [])

    if target_id not in builds:
        return False

    builds.remove(target_id)

    # Reconstruct the builds-toward line(s) in the frontmatter
    if builds:
        # Replace the builds-toward block
        new_builds = "builds-toward:\n" + "\n".join(f"  - {b}" for b in builds)
    else:
        new_builds = "builds-toward: []"

    # Match the builds-toward block in raw text (handles both inline and multi-line)
    # Pattern: "builds-toward:" followed by list items until next key or end of frontmatter
    # List items may or may not have leading whitespace before the dash
    bt_pattern = r"builds-toward:\s*\n(?:\s*-\s+[^\n]+\n?)+"
    bt_match = re.search(bt_pattern, fm_text)

    if bt_match:
        new_fm = fm_text[:bt_match.start()] + new_builds + "\n" + fm_text[bt_match.end():]
    else:
        # Try inline format: builds-toward: [...]
        bt_inline = r"builds-toward:\s*\[.*?\]"
        bt_match = re.search(bt_inline, fm_text)
        if bt_match:
            new_fm = fm_text[:bt_match.start()] + new_builds + fm_text[bt_match.end():]
        else:
            print(f"  WARNING: Could not find builds-toward block in {filepath}")
            return False

    new_text = f"---\n{new_fm}\n---\n" + text[match.end():]

    if not dry_run:
        filepath.write_text(new_text, encoding="utf-8")
    return True


def main():
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("DRY RUN — no files will be modified\n")

    removals = []  # (filepath, target_to_remove)

    for topic_a, topic_b, direction in DECISIONS:
        if direction == "A->B":
            # A comes first; remove B's builds-toward A
            removals.append((topic_b, topic_a))
        elif direction == "B->A":
            # B comes first; remove A's builds-toward B
            removals.append((topic_a, topic_b))
        elif direction == "drop":
            # Remove both directions
            removals.append((topic_a, topic_b))
            removals.append((topic_b, topic_a))

    print(f"Processing {len(removals)} builds-toward removals from {len(DECISIONS)} pair decisions...\n")

    changed = 0
    skipped = 0
    errors = 0

    for source_id, target_to_remove in removals:
        filepath = find_topic_file(source_id)
        if filepath is None:
            print(f"  ERROR: File not found for {source_id}")
            errors += 1
            continue

        result = remove_builds_toward_entry(filepath, target_to_remove, dry_run=dry_run)
        rel = filepath.relative_to(ROOT)
        if result:
            print(f"  {'WOULD REMOVE' if dry_run else 'REMOVED'}: {target_to_remove} from {rel} builds-toward")
            changed += 1
        else:
            print(f"  SKIP: {target_to_remove} not in {rel} builds-toward")
            skipped += 1

    print(f"\nDone: {changed} changes, {skipped} skipped, {errors} errors")


if __name__ == "__main__":
    main()
