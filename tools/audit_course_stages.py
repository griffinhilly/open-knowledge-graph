#!/usr/bin/env python3
"""Audit course stages against cross-course prerequisite flow.

Finds courses staged below their dependencies — where the median stage of
cross-course prereqs is higher than the course's declared stage.

Usage:
    python tools/audit_course_stages.py          # report only
    python tools/audit_course_stages.py --fix    # fix _domain.yml stages
"""
import yaml
from pathlib import Path
from collections import Counter

DOMAINS = Path(__file__).resolve().parent.parent / "domains"
STAGE_ORDER = [
    "pre-formal", "concrete-operations", "abstract-reasoning",
    "formal-systems", "advanced", "expert",
]
STAGE_RANK = {s: i for i, s in enumerate(STAGE_ORDER)}


def load_graph():
    topic_info = {}
    course_stage = {}

    for domain_dir in DOMAINS.iterdir():
        if not domain_dir.is_dir():
            continue
        yml = domain_dir / "_domain.yml"
        if yml.exists():
            data = yaml.safe_load(yml.read_text(encoding="utf-8"))
            for c in data.get("courses", []):
                course_stage[c["id"]] = c.get("stage", "unknown")
        for course_dir in domain_dir.iterdir():
            if not course_dir.is_dir():
                continue
            for md in course_dir.glob("*.md"):
                if md.name.startswith("_"):
                    continue
                text = md.read_text(encoding="utf-8")
                if not text.startswith("---"):
                    continue
                end = text.find("---", 3)
                if end == -1:
                    continue
                try:
                    fm = yaml.safe_load(text[3:end])
                except Exception:
                    continue
                if not fm:
                    continue
                topic_info[md.stem] = {
                    "course": fm.get("course", ""),
                    "domain": fm.get("domain", ""),
                    "stage": fm.get("stage", ""),
                    "prereqs": [
                        (p["id"] if isinstance(p, dict) else p)
                        for p in (fm.get("prerequisites") or [])
                    ],
                }
    return topic_info, course_stage


def find_misstaged(topic_info, course_stage):
    """Find courses staged below the median of their cross-course prereqs."""
    results = []

    for course_id, cstage in sorted(course_stage.items()):
        if cstage == "unknown":
            continue
        crank = STAGE_RANK.get(cstage, -1)

        course_topics = {
            tid for tid, info in topic_info.items() if info["course"] == course_id
        }

        prereq_ranks = []
        for tid in course_topics:
            for pid in topic_info[tid]["prereqs"]:
                if pid not in topic_info:
                    continue
                pinfo = topic_info[pid]
                if pinfo["course"] == course_id:
                    continue
                prank = STAGE_RANK.get(pinfo["stage"], -1)
                if prank >= 0:
                    prereq_ranks.append(prank)

        if len(prereq_ranks) < 3:
            continue

        prereq_ranks.sort()
        median_rank = prereq_ranks[len(prereq_ranks) // 2]

        if median_rank > crank:
            domain = next(
                (info["domain"] for info in topic_info.values() if info["course"] == course_id),
                "?",
            )
            higher_count = sum(1 for s in prereq_ranks if s > crank)
            results.append({
                "course": course_id,
                "domain": domain,
                "current_stage": cstage,
                "suggested_stage": STAGE_ORDER[median_rank],
                "higher_count": higher_count,
                "total_cross": len(prereq_ranks),
                "median_stage": STAGE_ORDER[median_rank],
            })

    return results


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--fix", action="store_true", help="Apply stage fixes to _domain.yml")
    args = parser.parse_args()

    topic_info, course_stage = load_graph()
    misstaged = find_misstaged(topic_info, course_stage)

    if not misstaged:
        print("No misstaged courses found.")
        return

    print(f"Found {len(misstaged)} courses staged below their cross-course prereqs:\n")
    for r in misstaged:
        pct = r["higher_count"] / r["total_cross"] * 100
        print(f"  {r['domain']}/{r['course']}")
        print(f"    Current: {r['current_stage']} → Suggested: {r['suggested_stage']}")
        print(f"    {r['higher_count']}/{r['total_cross']} ({pct:.0f}%) cross-course prereqs from higher stage")
        print()

    if args.fix:
        for r in misstaged:
            yml_path = DOMAINS / r["domain"] / "_domain.yml"
            if not yml_path.exists():
                continue
            text = yml_path.read_text(encoding="utf-8")
            old = f"  stage: {r['current_stage']}"
            new = f"  stage: {r['suggested_stage']}"
            # Only replace after the course ID line
            marker = f"- id: {r['course']}"
            idx = text.find(marker)
            if idx == -1:
                continue
            before = text[:idx]
            after = text[idx:]
            after = after.replace(old, new, 1)
            yml_path.write_text(before + after, encoding="utf-8")
            print(f"  FIXED: {r['course']} → {r['suggested_stage']}")


if __name__ == "__main__":
    main()
