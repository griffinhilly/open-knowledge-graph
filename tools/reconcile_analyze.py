#!/usr/bin/env python3
"""Analyze builds-toward / prerequisite mismatches for reconciliation.

Outputs a JSON file with all mismatches categorized and contextualized,
ready for decision-making.
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

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


def build_transitive_prereqs(prereq_graph, topic_id, cache=None):
    """Get all transitive prerequisites for a topic (memoized)."""
    if cache is None:
        cache = {}
    if topic_id in cache:
        return cache[topic_id]
    result = set()
    for prereq_id in prereq_graph.get(topic_id, []):
        result.add(prereq_id)
        result |= build_transitive_prereqs(prereq_graph, prereq_id, cache)
    cache[topic_id] = result
    return result


def would_create_cycle(prereq_graph, source_id, target_id):
    """Check if adding source_id as a prereq of target_id would create a cycle.

    A cycle would occur if target_id is already a (transitive) prerequisite of source_id.
    Because then: source_id -> ... -> target_id -> source_id.
    """
    # BFS/DFS from source_id through existing prereq_graph to see if we reach target_id
    visited = set()
    stack = [source_id]
    while stack:
        node = stack.pop()
        if node == target_id:
            return True
        if node in visited:
            continue
        visited.add(node)
        for prereq in prereq_graph.get(node, []):
            stack.append(prereq)
    return False


def main():
    # Parse all topics
    all_data = {}
    all_paths = {}
    prereq_graph = defaultdict(list)

    for filepath in sorted(DOMAINS_DIR.rglob("*.md")):
        data = parse_frontmatter(filepath)
        if data is None:
            continue
        topic_id = data.get("id")
        if not topic_id:
            continue
        all_data[topic_id] = data
        all_paths[topic_id] = str(filepath.relative_to(ROOT))
        prereqs = data.get("prerequisites", [])
        if isinstance(prereqs, list):
            for p in prereqs:
                if isinstance(p, dict) and "id" in p:
                    prereq_graph[topic_id].append(p["id"])

    print(f"Loaded {len(all_data)} topics", file=sys.stderr)

    # Find all mismatches
    mismatches = []
    dangling = []

    for topic_id, data in all_data.items():
        builds = data.get("builds-toward", [])
        if not isinstance(builds, list):
            continue
        for target_id in builds:
            if not isinstance(target_id, str):
                continue
            if target_id not in all_data:
                dangling.append({
                    "source_id": topic_id,
                    "source_title": data.get("title", ""),
                    "source_domain": data.get("domain", ""),
                    "source_course": data.get("course", ""),
                    "target_id": target_id,
                    "type": "dangling"
                })
                continue

            target_data = all_data[target_id]
            target_prereqs = target_data.get("prerequisites", [])
            target_prereq_ids = [p.get("id") for p in target_prereqs if isinstance(p, dict)]

            if topic_id not in target_prereq_ids:
                # Categorize
                same_domain = data.get("domain") == target_data.get("domain")
                same_course = data.get("course") == target_data.get("course")

                # Check if adding would create a cycle
                creates_cycle = would_create_cycle(prereq_graph, topic_id, target_id)

                # Check if source is already a transitive prereq of target
                transitive_cache = {}
                transitive_prereqs = build_transitive_prereqs(prereq_graph, target_id, transitive_cache)
                already_transitive = topic_id in transitive_prereqs

                mismatches.append({
                    "source_id": topic_id,
                    "source_title": data.get("title", ""),
                    "source_domain": data.get("domain", ""),
                    "source_course": data.get("course", ""),
                    "source_stage": data.get("stage", ""),
                    "target_id": target_id,
                    "target_title": target_data.get("title", ""),
                    "target_domain": target_data.get("domain", ""),
                    "target_course": target_data.get("course", ""),
                    "target_stage": target_data.get("stage", ""),
                    "target_prereq_count": len(target_prereq_ids),
                    "same_domain": same_domain,
                    "same_course": same_course,
                    "creates_cycle": creates_cycle,
                    "already_transitive": already_transitive,
                    "type": "mismatch"
                })

    # Summary stats
    stats = {
        "total_topics": len(all_data),
        "total_mismatches": len(mismatches),
        "total_dangling": len(dangling),
        "creates_cycle": sum(1 for m in mismatches if m["creates_cycle"]),
        "already_transitive": sum(1 for m in mismatches if m["already_transitive"]),
        "same_course": sum(1 for m in mismatches if m["same_course"]),
        "same_domain_diff_course": sum(1 for m in mismatches if m["same_domain"] and not m["same_course"]),
        "cross_domain": sum(1 for m in mismatches if not m["same_domain"]),
    }

    # Domain breakdown
    domain_counts = defaultdict(int)
    for m in mismatches:
        domain_counts[m["source_domain"]] += 1
    stats["by_source_domain"] = dict(sorted(domain_counts.items(), key=lambda x: -x[1]))

    output = {
        "stats": stats,
        "mismatches": mismatches,
        "dangling": dangling
    }

    outpath = ROOT / "tools" / "reconcile_analysis.json"
    with open(outpath, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    # Print summary
    print(f"\n=== Reconciliation Analysis ===", file=sys.stderr)
    print(f"Total mismatches: {stats['total_mismatches']}", file=sys.stderr)
    print(f"Dangling refs:    {stats['total_dangling']}", file=sys.stderr)
    print(f"Creates cycle:    {stats['creates_cycle']}", file=sys.stderr)
    print(f"Already transitive: {stats['already_transitive']}", file=sys.stderr)
    print(f"Same course:      {stats['same_course']}", file=sys.stderr)
    print(f"Same domain, diff course: {stats['same_domain_diff_course']}", file=sys.stderr)
    print(f"Cross-domain:     {stats['cross_domain']}", file=sys.stderr)
    print(f"\nBy source domain:", file=sys.stderr)
    for domain, count in stats["by_source_domain"].items():
        print(f"  {domain}: {count}", file=sys.stderr)
    print(f"\nOutput: {outpath}", file=sys.stderr)


if __name__ == "__main__":
    main()
