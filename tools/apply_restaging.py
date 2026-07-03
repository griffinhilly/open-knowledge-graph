#!/usr/bin/env python3
"""Apply restaging recommendations from swarm evaluation.

Reads a recommendations JSON file and updates topic YAML frontmatter.
Also reconciles _domain.yml course stages with actual topic stages.

Usage:
    python apply_restaging.py recommendations.json [--dry-run]
"""

import sys
import re
import json
import yaml
from pathlib import Path
from collections import defaultdict

DOMAINS_DIR = Path(__file__).parent.parent / "domains"

VALID_STAGES = [
    "pre-formal",
    "concrete-operations",
    "abstract-reasoning",
    "formal-systems",
    "advanced",
    "expert",
]


def apply_stage_change(filepath, new_stage):
    """Update the stage field in a topic file's YAML frontmatter."""
    filepath = Path(filepath)
    if not filepath.exists():
        print(f"  WARNING: File not found: {filepath}")
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace stage field in frontmatter
    # Match stage: <value> in YAML frontmatter (between --- markers)
    new_content = re.sub(
        r"(^---\n.*?^stage:\s*)(\S+)(.*?^---)",
        lambda m: m.group(1) + new_stage + m.group(3),
        content,
        count=1,
        flags=re.MULTILINE | re.DOTALL,
    )

    if new_content == content:
        print(f"  WARNING: No stage field found in {filepath}")
        return False

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True


def reconcile_domain_yml(domain_name):
    """Update _domain.yml course stages to match lowest topic stage per course."""
    domain_dir = DOMAINS_DIR / domain_name
    yml_path = domain_dir / "_domain.yml"

    if not yml_path.exists():
        return

    with open(yml_path, "r", encoding="utf-8") as f:
        domain_config = yaml.safe_load(f)

    if not domain_config or "courses" not in domain_config:
        return

    changed = False
    for course_entry in domain_config["courses"]:
        course_id = course_entry["id"]
        course_dir = domain_dir / course_id

        if not course_dir.exists():
            continue

        # Find the lowest stage among all topics in this course
        min_stage_idx = len(VALID_STAGES)
        for md_file in course_dir.glob("*.md"):
            if md_file.name.startswith("_"):
                continue
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()
            match = re.search(r"^stage:\s*(\S+)", content, re.MULTILINE)
            if match:
                stage = match.group(1)
                if stage in VALID_STAGES:
                    idx = VALID_STAGES.index(stage)
                    min_stage_idx = min(min_stage_idx, idx)

        if min_stage_idx < len(VALID_STAGES):
            new_stage = VALID_STAGES[min_stage_idx]
            if course_entry.get("stage") != new_stage:
                old_stage = course_entry.get("stage", "unknown")
                print(f"  _domain.yml: {domain_name}/{course_id}: {old_stage} -> {new_stage}")
                course_entry["stage"] = new_stage
                changed = True

    if changed:
        with open(yml_path, "w", encoding="utf-8") as f:
            yaml.dump(domain_config, f, default_flow_style=False, sort_keys=False, allow_unicode=True)


def main():
    if len(sys.argv) < 2:
        print("Usage: python apply_restaging.py recommendations.json [--dry-run]")
        sys.exit(1)

    rec_path = Path(sys.argv[1])
    dry_run = "--dry-run" in sys.argv

    with open(rec_path, "r", encoding="utf-8") as f:
        recommendations = json.load(f)

    if dry_run:
        print("=== DRY RUN — no changes will be made ===\n")

    # Track stats
    stats = defaultdict(lambda: defaultdict(int))
    total_changes = 0
    total_skipped = 0
    domains_touched = set()

    for rec in recommendations:
        topic_id = rec["id"]
        filepath = rec.get("filepath", "")
        current_stage = rec.get("current_stage", "")
        new_stage = rec.get("new_stage", "")
        domain = rec.get("domain", "")
        course = rec.get("course", "")

        if new_stage not in VALID_STAGES:
            print(f"  SKIP invalid stage '{new_stage}' for {topic_id}")
            total_skipped += 1
            continue

        if current_stage == new_stage:
            total_skipped += 1
            continue

        direction = "UP" if VALID_STAGES.index(new_stage) > VALID_STAGES.index(current_stage) else "DOWN"
        stats[domain][f"{current_stage} -> {new_stage}"] += 1
        domains_touched.add(domain)

        if not dry_run:
            success = apply_stage_change(filepath, new_stage)
            if success:
                total_changes += 1
            else:
                total_skipped += 1
        else:
            print(f"  {direction}: {topic_id} ({current_stage} -> {new_stage})")
            total_changes += 1

    print(f"\n{'Would apply' if dry_run else 'Applied'} {total_changes} changes, skipped {total_skipped}")

    # Print stats by domain
    print("\nChanges by domain and transition:")
    for domain in sorted(stats.keys()):
        print(f"\n  {domain}:")
        for transition, count in sorted(stats[domain].items()):
            print(f"    {transition}: {count}")

    # Reconcile _domain.yml files
    if not dry_run and domains_touched:
        print("\nReconciling _domain.yml files...")
        for domain in domains_touched:
            reconcile_domain_yml(domain)

    print("\nDone.")


if __name__ == "__main__":
    main()
