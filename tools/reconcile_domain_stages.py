#!/usr/bin/env python3
"""Reconcile _domain.yml course stages with actual topic stage distributions.

For each course, computes the modal (most common) stage from its topic files.
If the _domain.yml stage differs, updates it to the modal stage.

Usage:
    python tools/reconcile_domain_stages.py --dry-run    # Show mismatches
    python tools/reconcile_domain_stages.py --apply       # Fix _domain.yml files
"""

import re
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "domains"

STAGE_ORDER = [
    "pre-formal",
    "concrete-operations",
    "abstract-reasoning",
    "formal-systems",
    "advanced",
    "expert",
]


def get_topic_stage(filepath):
    """Extract stage from a topic file's YAML frontmatter."""
    text = filepath.read_text(encoding="utf-8")
    match = re.search(r"^stage:\s*(\S+)", text, re.MULTILINE)
    if match:
        return match.group(1)
    return None


def analyze_course(domain_dir, course_id):
    """Count stage distribution for all topics in a course."""
    course_dir = domain_dir / course_id
    if not course_dir.is_dir():
        return None

    stages = Counter()
    for f in course_dir.glob("*.md"):
        if f.name.startswith("_"):
            continue
        stage = get_topic_stage(f)
        if stage:
            stages[stage] += 1

    return stages


def modal_stage(stages):
    """Return the most common stage. Ties broken by higher stage (more advanced)."""
    if not stages:
        return None
    max_count = max(stages.values())
    candidates = [s for s, c in stages.items() if c == max_count]
    # Break ties: pick the highest (most advanced) stage
    candidates.sort(key=lambda s: STAGE_ORDER.index(s) if s in STAGE_ORDER else -1, reverse=True)
    return candidates[0]


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("--dry-run", "--apply"):
        print("Usage: python tools/reconcile_domain_stages.py [--dry-run | --apply]")
        sys.exit(1)

    apply = sys.argv[1] == "--apply"
    mismatches = []
    total_courses = 0
    matched_courses = 0

    for domain_dir in sorted(DOMAINS_DIR.iterdir()):
        if not domain_dir.is_dir() or domain_dir.name.startswith("."):
            continue

        domain_yml = domain_dir / "_domain.yml"
        if not domain_yml.exists():
            continue

        data = yaml.safe_load(domain_yml.read_text(encoding="utf-8"))
        courses = data.get("courses", [])

        for course in courses:
            course_id = course["id"]
            declared_stage = course.get("stage", "")
            total_courses += 1

            stages = analyze_course(domain_dir, course_id)
            if stages is None or not stages:
                print(f"  WARNING: {domain_dir.name}/{course_id} — no topics found")
                continue

            actual_modal = modal_stage(stages)
            total_topics = sum(stages.values())

            if declared_stage != actual_modal:
                modal_count = stages[actual_modal]
                pct = modal_count / total_topics * 100
                mismatches.append({
                    "domain": domain_dir.name,
                    "course": course_id,
                    "declared": declared_stage,
                    "modal": actual_modal,
                    "modal_pct": pct,
                    "total": total_topics,
                    "dist": dict(stages),
                })
                print(
                    f"  MISMATCH: {domain_dir.name}/{course_id}: "
                    f"{declared_stage} -> {actual_modal} "
                    f"({modal_count}/{total_topics} = {pct:.0f}%)"
                )
            else:
                matched_courses += 1

        if apply and any(m["domain"] == domain_dir.name for m in mismatches):
            # Rewrite _domain.yml with corrected stages
            domain_mismatches = {
                m["course"]: m["modal"]
                for m in mismatches
                if m["domain"] == domain_dir.name
            }
            for course in courses:
                if course["id"] in domain_mismatches:
                    course["stage"] = domain_mismatches[course["id"]]

            # Write back preserving structure
            # Use raw text replacement to avoid yaml.dump reformatting
            text = domain_yml.read_text(encoding="utf-8")
            for course_id, new_stage in domain_mismatches.items():
                old_mismatch = [m for m in mismatches if m["domain"] == domain_dir.name and m["course"] == course_id][0]
                old_stage = old_mismatch["declared"]
                # Find the course block and replace stage within it
                # Pattern: after "id: <course_id>" line, find "stage: <old>" and replace
                pattern = rf"(- id: {re.escape(course_id)}\s*\n\s*title:.*\n\s*stage:\s*){re.escape(old_stage)}"
                text = re.sub(pattern, rf"\g<1>{new_stage}", text)

            domain_yml.write_text(text, encoding="utf-8")
            print(f"  -> Updated {domain_dir.name}/_domain.yml")

    print(f"\n{'='*60}")
    print(f"Total courses: {total_courses}")
    print(f"Already correct: {matched_courses}")
    print(f"Mismatches: {len(mismatches)}")

    if mismatches:
        print(f"\nStage distribution of mismatches:")
        for m in mismatches:
            dist_str = ", ".join(f"{s}: {c}" for s, c in sorted(m["dist"].items(), key=lambda x: STAGE_ORDER.index(x[0]) if x[0] in STAGE_ORDER else -1))
            print(f"  {m['domain']}/{m['course']}: {dist_str}")

    if not apply and mismatches:
        print(f"\nRun with --apply to fix these {len(mismatches)} mismatches.")


if __name__ == "__main__":
    main()
