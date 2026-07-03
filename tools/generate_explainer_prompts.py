"""
Generate a JSONL batch file for producing missing ## Explainer sections.

Reads tools/tmp_missing_explainers.txt (one relative path per line),
parses each topic file's YAML frontmatter and body sections, and writes
tools/tmp_explainer_prompts.jsonl with one JSON object per line containing
all the context an LLM needs to generate the explainer.

Usage:
    C:/Python314/python tools/generate_explainer_prompts.py
"""

import json
import re
import sys
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MISSING_LIST = PROJECT_ROOT / "tools" / "tmp_missing_explainers.txt"
OUTPUT_FILE = PROJECT_ROOT / "tools" / "tmp_explainer_prompts.jsonl"


def parse_frontmatter(text: str) -> dict:
    """Extract YAML frontmatter fields from a topic markdown file.

    Uses simple regex parsing instead of a YAML library to avoid
    external dependencies and handle the specific format used in this project.
    """
    fm_match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not fm_match:
        return {}
    fm_text = fm_match.group(1)
    result = {}

    # id, title, domain, course, stage, status — single-value fields
    for field in ("id", "title", "domain", "course", "stage", "status"):
        m = re.search(rf"^{field}:\s*(.+)$", fm_text, re.MULTILINE)
        if m:
            val = m.group(1).strip().strip('"').strip("'")
            result[field] = val

    # prerequisites — list of {id, type} dicts
    prereqs = []
    prereq_block = re.search(
        r"^prerequisites:\s*\n((?:[ -].*\n)*)", fm_text, re.MULTILINE
    )
    if prereq_block:
        block = prereq_block.group(1)
        # Find each - id: ... / type: ... pair
        for m in re.finditer(
            r"-\s*id:\s*(.+?)\n\s*type:\s*(.+?)(?:\n|$)", block
        ):
            prereqs.append({"id": m.group(1).strip(), "type": m.group(2).strip()})
    result["prerequisites"] = prereqs

    return result


def extract_section(text: str, heading: str) -> str:
    """Extract the content of a ## heading section from the markdown body."""
    pattern = rf"^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)"
    m = re.search(pattern, text, re.MULTILINE | re.DOTALL)
    if m:
        return m.group(1).strip()
    return ""


def main():
    if not MISSING_LIST.exists():
        print(f"ERROR: {MISSING_LIST} not found")
        sys.exit(1)

    paths = [
        line.strip()
        for line in MISSING_LIST.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    print(f"Read {len(paths)} topic paths from {MISSING_LIST.name}")

    records = []
    errors = []
    domain_counter = Counter()
    course_counter = Counter()

    for rel_path in paths:
        full_path = PROJECT_ROOT / rel_path
        if not full_path.exists():
            errors.append(f"File not found: {rel_path}")
            continue

        text = full_path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)

        if not fm.get("id"):
            errors.append(f"No id in frontmatter: {rel_path}")
            continue

        core_idea = extract_section(text, "Core Idea")
        how_learned = extract_section(text, "How It's Best Learned")
        misconceptions = extract_section(text, "Common Misconceptions")

        domain = fm.get("domain", "unknown")
        course = fm.get("course", "unknown")
        stage = fm.get("stage", "unknown")

        domain_counter[domain] += 1
        course_counter[f"{domain}/{course}"] += 1

        record = {
            "path": rel_path,
            "topic_id": fm["id"],
            "title": fm.get("title", fm["id"]),
            "domain": domain,
            "course": course,
            "stage": stage,
            "core_idea": core_idea,
            "prerequisites": fm.get("prerequisites", []),
        }
        # Include optional sections if present — useful context for generation
        if how_learned:
            record["how_best_learned"] = how_learned
        if misconceptions:
            record["common_misconceptions"] = misconceptions

        records.append(record)

    # Write JSONL
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    print(f"\nWrote {len(records)} prompts to {OUTPUT_FILE.name}")

    if errors:
        print(f"\n{len(errors)} errors:")
        for e in errors:
            print(f"  - {e}")

    # Summary by domain
    print(f"\n--- Breakdown by domain ({len(domain_counter)} domains) ---")
    for domain, count in domain_counter.most_common():
        print(f"  {domain}: {count}")

    # Summary by course
    print(f"\n--- Breakdown by course ({len(course_counter)} courses) ---")
    for course, count in course_counter.most_common():
        print(f"  {course}: {count}")

    # Stage breakdown
    stage_counter = Counter(r["stage"] for r in records)
    print(f"\n--- Breakdown by stage ({len(stage_counter)} stages) ---")
    for stage, count in stage_counter.most_common():
        print(f"  {stage}: {count}")


if __name__ == "__main__":
    main()
