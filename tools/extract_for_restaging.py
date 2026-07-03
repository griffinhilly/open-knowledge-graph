#!/usr/bin/env python3
"""Extract topic data for restaging evaluation.

Reads all topic files from target courses, extracts key fields,
and outputs JSON organized by domain/course for swarm evaluation.
"""

import os
import re
import json
import yaml
from pathlib import Path

DOMAINS_DIR = Path(__file__).parent.parent / "domains"

# Courses to evaluate, organized by expected direction
# promote: currently advanced/formal-systems, may contain expert topics
# demote: currently expert, may contain advanced/formal-systems topics
# both: needs evaluation in both directions
TARGET_COURSES = {
    # PROMOTE candidates (advanced → expert)
    "mathematics": {
        "real-analysis": "promote",
        "abstract-algebra": "promote",
        "topology": "promote",
        "complex-analysis": "promote",
        "number-theory": "promote",
        "probability-and-mathematical-statistics": "promote",
        "differential-equations": "promote",
        "numerical-analysis": "promote",
        "graph-theory-and-combinatorics": "promote",
    },
    "computer-science": {
        "theory-of-computation": "promote",
        "artificial-intelligence": "promote",
        "compilers": "promote",
        "distributed-systems": "promote",
    },
    "chemistry": {
        "physical-chemistry": "promote",
        "analytical-chemistry": "promote",
    },
    "physics": {
        "quantum-mechanics": "promote",
        "modern-physics": "promote",
    },
    # DEMOTE candidates (expert → advanced or formal-systems)
    "health-and-human-development": {
        "epidemiology": "demote",
        "pathophysiology": "demote",
        "public-health": "demote",
    },
    "engineering": {
        "control-systems": "demote",
        "signals-and-systems": "demote",
    },
    "psychology": {
        "clinical-psychology": "demote",
        "cognitive-neuroscience": "demote",
        "psychometrics": "demote",
    },
    "literature": {
        "critical-theory": "demote",
        "comparative-literature": "demote",
    },
    "history": {
        "historiography": "demote",
    },
    "philosophy": {
        "philosophy-of-science": "demote",
    },
    "arts-and-aesthetics": {
        "aesthetic-theory": "demote",
    },
    "music": {
        "advanced-music-theory": "demote",
    },
    "language-and-communication": {
        "advanced-linguistics": "demote",
    },
    # BOTH directions
    "biology": {
        "neuroscience": "both",
        "immunology": "both",
    },
    "social-sciences": {
        "sociological-theory": "promote",
        "international-relations-theory": "promote",
        "research-methods-social-science": "promote",
    },
    # Light touch — check for outliers
    "formal-sciences-and-logic": {
        "category-theory": "demote",
        "model-theory": "demote",
    },
    "economics": {
        "development-economics": "demote",
    },
}


def parse_topic_file(filepath):
    """Parse a topic markdown file and extract key fields."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Split frontmatter from body
    if not content.startswith("---"):
        return None

    parts = content.split("---", 2)
    if len(parts) < 3:
        return None

    try:
        meta = yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return None

    if not meta or not isinstance(meta, dict):
        return None

    body = parts[2]

    # Extract Core Idea section
    core_idea = ""
    match = re.search(
        r"## Core Idea\s*\n(.*?)(?=\n## |\Z)", body, re.DOTALL
    )
    if match:
        core_idea = match.group(1).strip()
        # Truncate to ~300 chars to keep data manageable
        if len(core_idea) > 400:
            core_idea = core_idea[:400] + "..."

    # Extract prerequisite info
    prereqs = meta.get("prerequisites", [])
    prereq_ids = []
    if isinstance(prereqs, list):
        for p in prereqs:
            if isinstance(p, dict):
                prereq_ids.append(p.get("id", ""))
            elif isinstance(p, str):
                prereq_ids.append(p)

    return {
        "id": meta.get("id", ""),
        "title": meta.get("title", ""),
        "domain": meta.get("domain", ""),
        "course": meta.get("course", ""),
        "stage": meta.get("stage", ""),
        "prereq_count": len(prereq_ids),
        "prereq_ids": prereq_ids,
        "core_idea": core_idea,
        "filepath": str(filepath),
    }


def main():
    results = {}
    total = 0
    skipped = 0

    for domain, courses in TARGET_COURSES.items():
        domain_dir = DOMAINS_DIR / domain
        if not domain_dir.exists():
            print(f"WARNING: Domain dir not found: {domain_dir}")
            continue

        results[domain] = {}

        for course, direction in courses.items():
            course_dir = domain_dir / course
            if not course_dir.exists():
                print(f"WARNING: Course dir not found: {course_dir}")
                continue

            topics = []
            for md_file in sorted(course_dir.glob("*.md")):
                if md_file.name.startswith("_"):
                    continue
                topic = parse_topic_file(md_file)
                if topic:
                    topics.append(topic)
                    total += 1
                else:
                    skipped += 1

            results[domain][course] = {
                "direction": direction,
                "topic_count": len(topics),
                "topics": topics,
            }
            print(f"  {domain}/{course}: {len(topics)} topics ({direction})")

    # Write output
    output_path = DOMAINS_DIR.parent / "tools" / "restaging_data.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=1, ensure_ascii=False)

    print(f"\nTotal: {total} topics extracted, {skipped} skipped")
    print(f"Output: {output_path}")

    # Print summary by direction
    promote_count = sum(
        data["topic_count"]
        for domain_data in results.values()
        for data in domain_data.values()
        if data["direction"] == "promote"
    )
    demote_count = sum(
        data["topic_count"]
        for domain_data in results.values()
        for data in domain_data.values()
        if data["direction"] == "demote"
    )
    both_count = sum(
        data["topic_count"]
        for domain_data in results.values()
        for data in domain_data.values()
        if data["direction"] == "both"
    )
    print(f"\nBy direction: {promote_count} promote, {demote_count} demote, {both_count} both")


if __name__ == "__main__":
    main()
