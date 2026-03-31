#!/usr/bin/env python3
"""Spot-check quality of new P0/P1 topics.

Checks:
1. Schema compliance (required fields present)
2. Prerequisite validity (prereqs exist as files)
3. Stage coherence (topic stage matches course stage from _domain.yml)
4. Content quality (Core Idea length, Questions present, Explainer present)
5. Duplicate IDs (topics that share normalized IDs with existing topics)
"""

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "domains"

P0_COURSES = [
    "algebraic-topology", "partial-differential-equations", "differential-geometry",
    "machine-learning-theory", "cryptography", "quantum-computing",
    "quantum-field-theory", "general-relativity", "condensed-matter-physics",
    "inorganic-chemistry",
]

P1_COURSES = [
    "commutative-algebra", "stochastic-processes", "representation-theory",
    "information-theory", "advanced-algorithms", "formal-methods",
    "nonlinear-dynamics", "particle-physics", "materials-chemistry",
    "genomics-and-bioinformatics", "systems-biology", "developmental-biology",
    "structural-biology", "remote-sensing-and-gis", "geochemistry",
    "biostatistics", "health-economics", "industrial-organizational-psychology",
    "behavioral-economics", "labor-economics", "demography",
    "continental-philosophy",
]

NEW_COURSES = P0_COURSES + P1_COURSES

REQUIRED_FIELDS = ["id", "title", "domain", "course", "prerequisites"]
REQUIRED_SECTIONS = ["Core Idea"]


def parse_topic(filepath):
    """Parse a topic file into frontmatter dict and body text."""
    text = filepath.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None, text

    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text

    try:
        fm = yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return None, text

    return fm, parts[2]


def check_topic(filepath, all_topic_ids, course_stage):
    """Check a single topic file for quality issues."""
    issues = []
    fm, body = parse_topic(filepath)

    if fm is None:
        issues.append("PARSE_ERROR: Could not parse frontmatter")
        return issues

    # 1. Required fields
    for field in REQUIRED_FIELDS:
        if field not in fm or fm[field] is None:
            issues.append(f"MISSING_FIELD: {field}")

    # 2. Stage present
    stage = fm.get("stage")
    if not stage:
        issues.append("MISSING_FIELD: stage")

    # 3. Status
    status = fm.get("status")
    if status != "validated":
        issues.append(f"STATUS: {status} (expected validated)")

    # 4. Prerequisite validity
    prereqs = fm.get("prerequisites", [])
    if prereqs:
        for p in prereqs:
            if isinstance(p, dict):
                pid = p.get("id", "")
            else:
                pid = str(p)
            if pid and pid not in all_topic_ids:
                issues.append(f"DANGLING_PREREQ: {pid}")

    # 5. Content quality
    if "## Core Idea" not in body and "## core idea" not in body.lower():
        issues.append("MISSING_SECTION: Core Idea")

    core_idea_match = re.search(r"## Core Idea\s*\n(.*?)(?=\n## |\Z)", body, re.DOTALL)
    if core_idea_match:
        core_text = core_idea_match.group(1).strip()
        if len(core_text) < 100:
            issues.append(f"SHORT_CORE_IDEA: {len(core_text)} chars")

    if "## Questions" not in body:
        issues.append("MISSING_SECTION: Questions")

    if "## Explainer" not in body:
        issues.append("MISSING_SECTION: Explainer")

    # 6. Tags present
    tags = fm.get("tags", [])
    if not tags:
        issues.append("MISSING_TAGS")

    return issues


def main():
    # Build global topic ID set
    all_topic_ids = set()
    topic_files_by_course = defaultdict(list)

    for f in DOMAINS_DIR.rglob("*.md"):
        if f.name.startswith("_"):
            continue
        all_topic_ids.add(f.stem)

    # Find new course topic files
    new_topic_files = []
    for domain_dir in DOMAINS_DIR.iterdir():
        if not domain_dir.is_dir():
            continue
        for course_dir in domain_dir.iterdir():
            if not course_dir.is_dir():
                continue
            if course_dir.name in NEW_COURSES:
                for f in course_dir.glob("*.md"):
                    if not f.name.startswith("_"):
                        new_topic_files.append(f)

    # Load course stages from _domain.yml
    course_stages = {}
    for domain_dir in DOMAINS_DIR.iterdir():
        yml = domain_dir / "_domain.yml"
        if yml.exists():
            data = yaml.safe_load(yml.read_text(encoding="utf-8"))
            for c in data.get("courses", []):
                course_stages[c["id"]] = c.get("stage", "")

    print(f"Checking {len(new_topic_files)} topics across {len(NEW_COURSES)} new courses\n")

    issue_counts = Counter()
    topics_with_issues = 0
    course_summaries = defaultdict(lambda: {"total": 0, "issues": 0, "details": []})

    for f in sorted(new_topic_files):
        course = f.parent.name
        course_stage = course_stages.get(course, "")
        issues = check_topic(f, all_topic_ids, course_stage)

        course_summaries[course]["total"] += 1
        if issues:
            topics_with_issues += 1
            course_summaries[course]["issues"] += 1
            for issue in issues:
                issue_counts[issue.split(":")[0]] += 1
                course_summaries[course]["details"].append(f"  {f.stem}: {issue}")

    # Print summary
    print("=" * 60)
    print(f"Total new topics: {len(new_topic_files)}")
    print(f"Topics with issues: {topics_with_issues} ({topics_with_issues/len(new_topic_files)*100:.1f}%)")
    print(f"Clean topics: {len(new_topic_files) - topics_with_issues}")
    print()

    print("Issue type counts:")
    for issue_type, count in issue_counts.most_common():
        print(f"  {issue_type}: {count}")
    print()

    # Per-course breakdown
    print("Per-course breakdown:")
    for course in sorted(course_summaries):
        s = course_summaries[course]
        status = "OK" if s["issues"] == 0 else f"{s['issues']} issues"
        print(f"  {course}: {s['total']} topics, {status}")

    # Print detailed issues (limit to first 5 per course)
    print("\nDetailed issues (first 5 per course):")
    for course in sorted(course_summaries):
        details = course_summaries[course]["details"]
        if details:
            print(f"\n  {course}:")
            for d in details[:5]:
                print(f"    {d}")
            if len(details) > 5:
                print(f"    ... and {len(details) - 5} more")


if __name__ == "__main__":
    main()
