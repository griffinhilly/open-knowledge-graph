#!/usr/bin/env python3
"""Resolve bidirectional builds-toward pairs.

For each pair where A builds-toward B AND B builds-toward A:
- Self-referential (A==A): remove the self-reference from builds-toward
- Otherwise: pick direction based on heuristics (stage, prereq count, title),
  then remove the backward builds-toward entry.

Heuristics (in priority order):
1. Earlier developmental stage comes first
2. Fewer prerequisites = more foundational = comes first
3. Title contains "intro"/"overview"/"foundations"/"basics" = comes first
4. Alphabetical fallback
"""

import re
import sys
import json
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required.")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "domains"

STAGE_ORDER = {
    "pre-formal": 0,
    "concrete-operations": 1,
    "abstract-reasoning": 2,
    "formal-systems": 3,
    "advanced": 4,
    "expert": 5,
}

FOUNDATIONAL_KEYWORDS = {"intro", "introduction", "overview", "foundations", "basics", "fundamentals", "core"}


def parse_frontmatter(filepath):
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return None, text
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None, text
    return data, text


def find_topic_file(topic_id):
    matches = list(DOMAINS_DIR.rglob(f"{topic_id}.md"))
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        return matches[0]
    return None


def remove_builds_toward_entry(filepath, target_id):
    """Remove a specific entry from a topic's builds-toward list."""
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

    if builds:
        new_builds = "builds-toward:\n" + "\n".join(f"  - {b}" for b in builds)
    else:
        new_builds = "builds-toward: []"

    bt_pattern = r"builds-toward:\s*\n(?:\s*-\s+[^\n]+\n?)+"
    bt_match = re.search(bt_pattern, fm_text)

    if bt_match:
        new_fm = fm_text[:bt_match.start()] + new_builds + "\n" + fm_text[bt_match.end():]
    else:
        bt_inline = r"builds-toward:\s*\[.*?\]"
        bt_match = re.search(bt_inline, fm_text)
        if bt_match:
            new_fm = fm_text[:bt_match.start()] + new_builds + fm_text[bt_match.end():]
        else:
            print(f"  WARNING: Could not find builds-toward block in {filepath}")
            return False

    new_text = f"---\n{new_fm}\n---\n" + text[match.end():]
    filepath.write_text(new_text, encoding="utf-8")
    return True


def is_foundational_title(title):
    words = set(title.lower().replace("-", " ").split())
    return bool(words & FOUNDATIONAL_KEYWORDS)


def decide_direction(data_a, data_b, id_a, id_b):
    """Return (first_id, second_id) — first is more foundational."""
    stage_a = STAGE_ORDER.get(data_a.get("stage", ""), 2)
    stage_b = STAGE_ORDER.get(data_b.get("stage", ""), 2)

    if stage_a != stage_b:
        return (id_a, id_b) if stage_a < stage_b else (id_b, id_a)

    prereq_a = len(data_a.get("prerequisites", []))
    prereq_b = len(data_b.get("prerequisites", []))

    if abs(prereq_a - prereq_b) >= 2:
        return (id_a, id_b) if prereq_a < prereq_b else (id_b, id_a)

    title_a = data_a.get("title", "")
    title_b = data_b.get("title", "")
    found_a = is_foundational_title(title_a)
    found_b = is_foundational_title(title_b)

    if found_a and not found_b:
        return (id_a, id_b)
    if found_b and not found_a:
        return (id_b, id_a)

    return (id_a, id_b) if id_a < id_b else (id_b, id_a)


def main():
    dry_run = "--dry-run" in sys.argv

    # Load QA report
    report_path = ROOT / "tools" / "qa_report.json"
    with open(report_path, encoding="utf-8") as f:
        report = json.load(f)

    pairs = report.get("bidirectional_pairs", [])
    print(f"Processing {len(pairs)} bidirectional pairs...\n")

    # Cache topic data
    topic_cache = {}

    self_ref_fixed = 0
    direction_fixed = 0
    errors = 0

    for pair in pairs:
        id_a = pair["topic_a"]["id"]
        id_b = pair["topic_b"]["id"]

        # Self-referential
        if id_a == id_b:
            filepath = find_topic_file(id_a)
            if not filepath:
                print(f"  ERROR: File not found for {id_a}")
                errors += 1
                continue
            if dry_run:
                print(f"  SELF-REF (would fix): {id_a}")
            else:
                if remove_builds_toward_entry(filepath, id_a):
                    print(f"  SELF-REF FIXED: removed {id_a} from own builds-toward")
                    self_ref_fixed += 1
                else:
                    print(f"  SKIP: {id_a} self-ref not found in builds-toward")
            continue

        # Load topic data
        for tid in (id_a, id_b):
            if tid not in topic_cache:
                fp = find_topic_file(tid)
                if fp:
                    data, _ = parse_frontmatter(fp)
                    topic_cache[tid] = (data, fp)
                else:
                    topic_cache[tid] = (None, None)

        data_a, fp_a = topic_cache[id_a]
        data_b, fp_b = topic_cache[id_b]

        if not data_a or not data_b:
            missing = id_a if not data_a else id_b
            print(f"  ERROR: Could not load {missing}")
            errors += 1
            continue

        first_id, second_id = decide_direction(data_a, data_b, id_a, id_b)

        # Remove second's builds-toward first (the backward direction)
        # Actually: first comes before second, so second should NOT build-toward first
        # But the pair means both build-toward each other. We want to keep first->second direction.
        # So we remove: second's builds-toward entry pointing to first
        # AND we remove: first's builds-toward entry pointing to second? No.
        # Wait — builds-toward is informational and points FORWARD. If first->second,
        # then first builds-toward second (correct) and second builds-toward first (wrong).
        # So remove: second's builds-toward entry for first.
        second_fp = fp_a if second_id == id_a else fp_b

        if dry_run:
            print(f"  WOULD FIX: {first_id} -> {second_id} (remove {first_id} from {second_id}'s builds-toward)")
        else:
            if remove_builds_toward_entry(second_fp, first_id):
                print(f"  FIXED: {first_id} -> {second_id} (removed {first_id} from {second_id}'s builds-toward)")
                direction_fixed += 1
            else:
                print(f"  SKIP: {first_id} not in {second_id}'s builds-toward")

    print(f"\nDone: {self_ref_fixed} self-refs fixed, {direction_fixed} directions resolved, {errors} errors")
    if dry_run:
        print("(DRY RUN — no files modified)")


if __name__ == "__main__":
    main()
