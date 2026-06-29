#!/usr/bin/env python3
"""Print coverage statistics for the Open Knowledge Graph."""

import sys
import re
from pathlib import Path
from collections import defaultdict

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install with: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "domains"


def parse_frontmatter(filepath):
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None


def main():
    topics = []
    n_capacity = 0
    for filepath in sorted(DOMAINS_DIR.rglob("*.md")):
        data = parse_frontmatter(filepath)
        if data and "id" in data:
            # Origin layer: kind:capacity nodes are a private substrate — excluded from headline
            # counts (which report taught topics only) and reported separately below.
            if data.get("kind") == "capacity":
                n_capacity += 1
                continue
            data["_filepath"] = filepath
            topics.append(data)

    if not topics:
        print("No topics found.")
        return

    # Overall stats
    print(f"Total topics: {len(topics)}")
    if n_capacity:
        print(f"  (+ {n_capacity} origin-layer capacities, excluded from counts)")

    # By domain
    by_domain = defaultdict(list)
    for t in topics:
        by_domain[t.get("domain", "unknown")].append(t)
    print(f"Domains: {len(by_domain)}")
    for domain, ts in sorted(by_domain.items()):
        print(f"  {domain}: {len(ts)} topics")

    # By course
    print("\nBy course:")
    by_course = defaultdict(list)
    for t in topics:
        by_course[t.get("course", "unknown")].append(t)
    for course, ts in sorted(by_course.items()):
        print(f"  {course}: {len(ts)} topics")

    # By status
    print("\nBy status:")
    by_status = defaultdict(int)
    for t in topics:
        by_status[t.get("status", "draft")] += 1
    for status, count in sorted(by_status.items()):
        print(f"  {status}: {count}")

    # Edge stats
    total_hard = 0
    total_soft = 0
    max_prereqs = 0
    max_prereq_topic = ""
    for t in topics:
        prereqs = t.get("prerequisites", [])
        if isinstance(prereqs, list):
            n = len(prereqs)
            if n > max_prereqs:
                max_prereqs = n
                max_prereq_topic = t.get("id", "?")
            for p in prereqs:
                if isinstance(p, dict):
                    if p.get("type") == "hard":
                        total_hard += 1
                    else:
                        total_soft += 1

    print(f"\nPrerequisite edges: {total_hard + total_soft} ({total_hard} hard, {total_soft} soft)")
    print(f"Most prerequisites: {max_prereq_topic} ({max_prereqs})")

    # Topics with no prerequisites (roots)
    roots = [t["id"] for t in topics
             if not t.get("prerequisites") or len(t["prerequisites"]) == 0]
    print(f"\nRoot topics (no prerequisites): {len(roots)}")

    # Topics not referenced as prerequisite by anyone (leaves)
    all_prereq_ids = set()
    for t in topics:
        for p in t.get("prerequisites", []):
            if isinstance(p, dict) and "id" in p:
                all_prereq_ids.add(p["id"])
    topic_ids = {t["id"] for t in topics}
    leaves = topic_ids - all_prereq_ids
    print(f"Leaf topics (nothing depends on them): {len(leaves)}")

    # Dangling references
    dangling = all_prereq_ids - topic_ids
    if dangling:
        print(f"\nDangling prerequisite references ({len(dangling)}):")
        for d in sorted(dangling):
            print(f"  - {d}")


if __name__ == "__main__":
    main()
