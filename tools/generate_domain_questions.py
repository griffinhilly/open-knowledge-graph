#!/usr/bin/env python3
"""Extract ALL questions from OKG topic files, grouped by domain.

Outputs one JSON file per domain to output/questions/{domain}.json.
Each file contains every question from every topic in that domain,
organized for use by the domain-quiz page.

Usage:
    python tools/generate_domain_questions.py
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install with: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "domains"
OUTPUT_DIR = ROOT / "output" / "questions"


from parse_topic import parse_topic as parse_frontmatter, extract_questions


def load_domain_config(domain_dir):
    """Load _domain.yml and return course list with titles and stages."""
    config_path = domain_dir / "_domain.yml"
    if not config_path.exists():
        return []
    data = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    courses = []
    for c in data.get("courses", []):
        if isinstance(c, dict) and "id" in c:
            courses.append({
                "id": c["id"],
                "title": c.get("title", c["id"]),
                "stage": c.get("stage", "formal-systems"),
            })
    return courses


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    total_domains = 0
    total_questions = 0

    for domain_dir in sorted(DOMAINS_DIR.iterdir()):
        if not domain_dir.is_dir():
            continue
        config_path = domain_dir / "_domain.yml"
        if not config_path.exists():
            continue

        domain = domain_dir.name
        courses_config = load_domain_config(domain_dir)
        course_meta = {c["id"]: c for c in courses_config}

        # Collect all questions from all topic files in this domain
        questions = []
        course_counts = defaultdict(int)

        for filepath in sorted(domain_dir.rglob("*.md")):
            if filepath.name.startswith("_"):
                continue

            data, body = parse_frontmatter(filepath)
            if not data or "id" not in data:
                continue

            topic_id = data["id"]
            topic_title = data.get("title", topic_id)
            course = data.get("course", "")
            stage = data.get("stage", "formal-systems")

            raw_questions = extract_questions(body)
            for q in raw_questions:
                if not isinstance(q, dict) or "question" not in q:
                    continue

                entry = {
                    "topicId": topic_id,
                    "topicTitle": topic_title,
                    "course": course,
                    "stage": stage,
                    "question": q["question"],
                    "type": q.get("type", "multiple-choice"),
                }

                if entry["type"] == "multiple-choice":
                    entry["options"] = q.get("options", [])
                    entry["answer"] = q.get("answer", 0)
                elif entry["type"] == "true-false":
                    entry["answer"] = q.get("answer", False)
                elif entry["type"] == "short-answer":
                    entry["modelAnswer"] = q.get("answer", "")

                entry["explanation"] = q.get("explanation", "")
                questions.append(entry)
                course_counts[course] += 1

        # Build course list with question counts
        courses_out = []
        for c in courses_config:
            cid = c["id"]
            count = course_counts.get(cid, 0)
            courses_out.append({
                "id": cid,
                "title": c["title"],
                "stage": c["stage"],
                "questionCount": count,
            })

        output = {
            "domain": domain,
            "courses": courses_out,
            "questions": questions,
        }

        out_path = OUTPUT_DIR / f"{domain}.json"
        out_path.write_text(
            json.dumps(output, ensure_ascii=False, separators=(",", ":")),
            encoding="utf-8",
        )

        size_kb = out_path.stat().st_size / 1024
        total_domains += 1
        total_questions += len(questions)
        print(f"  {domain}: {len(questions)} questions, {len(courses_out)} courses ({size_kb:.0f} KB)")

    print(f"\nWrote {total_domains} domain files ({total_questions} total questions)")


if __name__ == "__main__":
    main()
