#!/usr/bin/env python3
"""Validate the Open Knowledge Graph.

Checks:
1. YAML frontmatter schema compliance
2. ID matches filename
3. All prerequisite references resolve to existing topics
4. No cycles in the prerequisite graph
5. builds-toward consistency (warning only)
6. Course directories match domain config
7. No duplicate IDs
8. Questions section schema (warning only)
"""

import argparse
import sys
import os
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

REQUIRED_FIELDS = {"id", "title", "domain", "course", "prerequisites"}
VALID_STATUSES = {"stub", "draft", "review", "validated"}
VALID_STAGES = {"pre-formal", "concrete-operations", "abstract-reasoning", "formal-systems", "advanced", "expert"}
VALID_PREREQ_TYPES = {"hard", "soft"}
VALID_QUESTION_TYPES = {"multiple-choice", "true-false", "short-answer"}

errors = []
warnings = []
topics_with_questions = 0


def error(filepath, msg):
    rel = filepath.relative_to(ROOT)
    errors.append(f"  ERROR  {rel}: {msg}")


def warn(filepath, msg):
    rel = filepath.relative_to(ROOT)
    warnings.append(f"  WARN   {rel}: {msg}")


def parse_frontmatter(filepath):
    """Extract YAML frontmatter from a Markdown file."""
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        error(filepath, "No YAML frontmatter found (must start with ---)")
        return None
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as e:
        error(filepath, f"Invalid YAML: {e}")
        return None
    if not isinstance(data, dict):
        error(filepath, "Frontmatter is not a YAML mapping")
        return None
    return data


def validate_questions(filepath, text):
    """Validate the ## Questions section if present. Returns True if questions found."""
    # Check if a ## Questions section exists
    questions_match = re.search(r"^## Questions\s*\n", text, re.MULTILINE)
    if not questions_match:
        return False

    # Extract the YAML code block within the Questions section
    # Look for ```yaml ... ``` after the ## Questions header
    section_text = text[questions_match.end():]
    # Stop at the next ## heading or end of file
    next_section = re.search(r"^## ", section_text, re.MULTILINE)
    if next_section:
        section_text = section_text[:next_section.start()]

    yaml_block = re.search(r"```ya?ml\s*\n(.*?)```", section_text, re.DOTALL)
    if not yaml_block:
        warn(filepath, "Questions section exists but contains no YAML code block")
        return True

    try:
        questions = yaml.safe_load(yaml_block.group(1))
    except yaml.YAMLError as e:
        warn(filepath, f"Questions section has invalid YAML: {e}")
        return True

    if not isinstance(questions, list):
        warn(filepath, "Questions YAML must be a list of question objects")
        return True

    if len(questions) < 2 or len(questions) > 5:
        warn(filepath, f"Questions should have 2-5 items, found {len(questions)}")

    for i, q in enumerate(questions):
        if not isinstance(q, dict):
            warn(filepath, f"questions[{i}] must be a mapping")
            continue

        # Required fields
        if "question" not in q:
            warn(filepath, f"questions[{i}] missing 'question' field")
        elif not isinstance(q["question"], str):
            warn(filepath, f"questions[{i}] 'question' must be a string")

        if "type" not in q:
            warn(filepath, f"questions[{i}] missing 'type' field")
        elif q["type"] not in VALID_QUESTION_TYPES:
            warn(filepath, f"questions[{i}] type '{q['type']}' not in {VALID_QUESTION_TYPES}")

        if "answer" not in q:
            warn(filepath, f"questions[{i}] missing 'answer' field")

        if "explanation" not in q:
            warn(filepath, f"questions[{i}] missing 'explanation' field")
        elif not isinstance(q["explanation"], str):
            warn(filepath, f"questions[{i}] 'explanation' must be a string")

        # Type-specific validation
        qtype = q.get("type")
        answer = q.get("answer")

        if qtype == "multiple-choice":
            options = q.get("options")
            if options is None:
                warn(filepath, f"questions[{i}] multiple-choice missing 'options'")
            elif not isinstance(options, list):
                warn(filepath, f"questions[{i}] 'options' must be a list")
            elif len(options) < 3 or len(options) > 5:
                warn(filepath, f"questions[{i}] multiple-choice should have 3-5 options, found {len(options)}")
            else:
                for j, opt in enumerate(options):
                    if not isinstance(opt, str):
                        warn(filepath, f"questions[{i}] options[{j}] must be a string")

            if answer is not None:
                if not isinstance(answer, int):
                    warn(filepath, f"questions[{i}] multiple-choice 'answer' must be an integer (0-indexed)")
                elif options and isinstance(options, list) and (answer < 0 or answer >= len(options)):
                    warn(filepath, f"questions[{i}] answer index {answer} out of range for {len(options)} options")

        elif qtype == "true-false":
            if answer is not None and not isinstance(answer, bool):
                warn(filepath, f"questions[{i}] true-false 'answer' must be a boolean (true/false)")

        elif qtype == "short-answer":
            if answer is not None and not isinstance(answer, str):
                warn(filepath, f"questions[{i}] short-answer 'answer' must be a string")

    return True


def validate_topic(filepath, data, domain_courses):
    """Validate a single topic's frontmatter."""
    # Required fields
    for field in REQUIRED_FIELDS:
        if field not in data:
            error(filepath, f"Missing required field: {field}")

    topic_id = data.get("id")
    expected_id = filepath.stem

    # ID matches filename
    if topic_id and topic_id != expected_id:
        error(filepath, f"ID '{topic_id}' does not match filename '{expected_id}'")

    # Domain exists
    domain = data.get("domain")
    if domain:
        domain_dir = DOMAINS_DIR / domain
        if not domain_dir.is_dir():
            error(filepath, f"Domain '{domain}' has no directory at {domain_dir}")

    # Course exists as subdirectory
    course = data.get("course")
    if course and domain:
        course_dir = DOMAINS_DIR / domain / course
        if not course_dir.is_dir():
            error(filepath, f"Course '{course}' has no directory under {domain}/")
        if domain_courses and course not in domain_courses:
            warn(filepath, f"Course '{course}' not listed in _domain.yml")

    # Prerequisites format
    prereqs = data.get("prerequisites", [])
    if not isinstance(prereqs, list):
        error(filepath, "prerequisites must be a list")
    else:
        for i, prereq in enumerate(prereqs):
            if not isinstance(prereq, dict):
                error(filepath, f"prerequisites[{i}] must be a mapping with 'id' and 'type'")
                continue
            if "id" not in prereq:
                error(filepath, f"prerequisites[{i}] missing 'id'")
            if "type" not in prereq:
                error(filepath, f"prerequisites[{i}] missing 'type'")
            elif prereq["type"] not in VALID_PREREQ_TYPES:
                error(filepath, f"prerequisites[{i}] type '{prereq['type']}' not in {VALID_PREREQ_TYPES}")

    # builds-toward format
    builds = data.get("builds-toward", [])
    if not isinstance(builds, list):
        error(filepath, "builds-toward must be a list of strings")
    else:
        for item in builds:
            if not isinstance(item, str):
                error(filepath, f"builds-toward entry '{item}' must be a string")

    # Status
    status = data.get("status")
    if status and status not in VALID_STATUSES:
        error(filepath, f"status '{status}' not in {VALID_STATUSES}")

    # Stage
    stage = data.get("stage")
    if stage and stage not in VALID_STAGES:
        error(filepath, f"stage '{stage}' not in {VALID_STAGES}")

    # Tags
    tags = data.get("tags", [])
    if not isinstance(tags, list):
        error(filepath, "tags must be a list of strings")


def find_cycles(graph):
    """Detect cycles using DFS. Returns list of cycles found."""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = defaultdict(int)
    cycles = []
    parent = {}

    def dfs(node, path):
        color[node] = GRAY
        for neighbor in graph.get(node, []):
            if color[neighbor] == GRAY:
                # Found a cycle -- extract it
                cycle_start = path.index(neighbor) if neighbor in path else -1
                if cycle_start >= 0:
                    cycles.append(path[cycle_start:] + [neighbor])
            elif color[neighbor] == WHITE:
                dfs(neighbor, path + [neighbor])
        color[node] = BLACK

    for node in graph:
        if color[node] == WHITE:
            dfs(node, [node])

    return cycles


def load_domain_courses(domain_dir):
    """Load course IDs from _domain.yml if it exists."""
    domain_file = domain_dir / "_domain.yml"
    if not domain_file.exists():
        return set()
    try:
        data = yaml.safe_load(domain_file.read_text(encoding="utf-8"))
        courses = data.get("courses", [])
        return {c["id"] for c in courses if isinstance(c, dict) and "id" in c}
    except Exception:
        return set()


def main():
    parser = argparse.ArgumentParser(description="Validate the Open Knowledge Graph")
    parser.add_argument("--quick", action="store_true",
                        help="Errors-only mode: schema + cycles + duplicate IDs. "
                             "Skips builds-toward, question validation, and warnings. (~12s)")
    args = parser.parse_args()
    quick = args.quick

    mode = "quick" if quick else "full"
    print(f"Validating Open Knowledge Graph ({mode})...\n")

    # Collect all topic files
    all_topics = {}  # id -> filepath
    all_data = {}    # id -> frontmatter dict
    prereq_graph = defaultdict(list)  # id -> [prerequisite ids]

    # Load domain configs
    domain_courses = {}
    for domain_dir in DOMAINS_DIR.iterdir():
        if domain_dir.is_dir():
            domain_courses[domain_dir.name] = load_domain_courses(domain_dir)

    # Find all .md files in domains/
    topic_files = sorted(DOMAINS_DIR.rglob("*.md"))

    if not topic_files:
        print("  No topic files found in domains/\n")
        print("RESULT: Nothing to validate.")
        return 0

    # Parse and validate each file
    global topics_with_questions
    for filepath in topic_files:
        data = parse_frontmatter(filepath)
        if data is None:
            continue

        topic_id = data.get("id")
        domain = data.get("domain", "")
        courses = domain_courses.get(domain, set())
        validate_topic(filepath, data, courses)

        # Validate Questions section if present (skip in quick mode)
        if not quick:
            text = filepath.read_text(encoding="utf-8")
            if validate_questions(filepath, text):
                topics_with_questions += 1

        if topic_id:
            if topic_id in all_topics:
                error(filepath, f"Duplicate ID '{topic_id}' (also in {all_topics[topic_id].relative_to(ROOT)})")
            else:
                all_topics[topic_id] = filepath
                all_data[topic_id] = data

    # Check prerequisite references
    for topic_id, data in all_data.items():
        prereqs = data.get("prerequisites", [])
        if not isinstance(prereqs, list):
            continue
        for prereq in prereqs:
            if not isinstance(prereq, dict):
                continue
            prereq_id = prereq.get("id")
            if not quick and prereq_id and prereq_id not in all_topics:
                warn(all_topics[topic_id], f"Prerequisite '{prereq_id}' not found (may not exist yet)")
            if prereq_id:
                prereq_graph[topic_id].append(prereq_id)

    # Check builds-toward consistency (skip in quick mode)
    if not quick:
        for topic_id, data in all_data.items():
            builds = data.get("builds-toward", [])
            if not isinstance(builds, list):
                continue
            for target_id in builds:
                if not isinstance(target_id, str):
                    continue
                if target_id not in all_topics:
                    warn(all_topics[topic_id], f"builds-toward '{target_id}' not found")
                elif target_id in all_data:
                    # Check that the target lists this topic as a prerequisite
                    target_prereqs = all_data[target_id].get("prerequisites", [])
                    target_prereq_ids = [p.get("id") for p in target_prereqs if isinstance(p, dict)]
                    if topic_id not in target_prereq_ids:
                        warn(all_topics[topic_id],
                             f"builds-toward '{target_id}' but that topic doesn't list '{topic_id}' as prerequisite")

    # Check for cycles
    cycles = find_cycles(prereq_graph)
    for cycle in cycles:
        cycle_str = " -> ".join(cycle)
        errors.append(f"  ERROR  Cycle detected: {cycle_str}")

    # Course-stage audit: find courses staged below their cross-course prereqs
    if not quick:
        STAGE_RANK = {s: i for i, s in enumerate(["pre-formal", "concrete-operations",
                      "abstract-reasoning", "formal-systems", "advanced", "expert"])}
        course_stages = {}
        for domain_dir2 in DOMAINS_DIR.iterdir():
            if not domain_dir2.is_dir():
                continue
            yml2 = domain_dir2 / "_domain.yml"
            if yml2.exists():
                ydata = yaml.safe_load(yml2.read_text(encoding="utf-8"))
                for c in ydata.get("courses", []):
                    course_stages[c["id"]] = c.get("stage", "unknown")

        for cid, cstage in course_stages.items():
            crank = STAGE_RANK.get(cstage, -1)
            if crank < 0:
                continue
            prereq_ranks = []
            for tid, data in all_data.items():
                if data.get("course") != cid:
                    continue
                for p in (data.get("prerequisites") or []):
                    pid = p.get("id", "") if isinstance(p, dict) else str(p)
                    if pid in all_data and all_data[pid].get("course") != cid:
                        pr = STAGE_RANK.get(all_data[pid].get("stage", ""), -1)
                        if pr >= 0:
                            prereq_ranks.append(pr)
            if len(prereq_ranks) >= 3:
                prereq_ranks.sort()
                median = prereq_ranks[len(prereq_ranks) // 2]
                if median > crank:
                    stage_names = {v: k for k, v in STAGE_RANK.items()}
                    warnings.append(f"  WARN   Course '{cid}' staged at {cstage} but median cross-course prereq is {stage_names[median]}")

    # Report
    print(f"  Scanned {len(topic_files)} files, {len(all_topics)} valid topics")
    if not quick:
        print(f"  Topics with questions: {topics_with_questions} of {len(all_topics)}")
    print()

    # Stats by course (skip in quick mode)
    if not quick:
        course_counts = defaultdict(int)
        for data in all_data.values():
            course = data.get("course", "unknown")
            course_counts[course] += 1
        if course_counts:
            print("  Topics by course:")
            for course, count in sorted(course_counts.items()):
                print(f"    {course}: {count}")
            print()

        # Orphan check (topics with no prerequisites and not listed as prerequisite by anyone)
        all_prereq_targets = set()
        for prereqs in prereq_graph.values():
            all_prereq_targets.update(prereqs)
        roots = [tid for tid in all_topics if tid not in all_prereq_targets and not prereq_graph.get(tid)]
        if roots:
            print(f"  Root topics (no prerequisites, not depended on): {len(roots)}")
            for r in sorted(roots)[:10]:
                print(f"    - {r}")
            if len(roots) > 10:
                print(f"    ... and {len(roots) - 10} more")
            print()

    if warnings:
        print(f"Warnings ({len(warnings)}):")
        for w in warnings:
            print(w)
        print()

    if errors:
        print(f"Errors ({len(errors)}):")
        for e in errors:
            print(e)
        print()
        print(f"RESULT: FAILED ({len(errors)} errors, {len(warnings)} warnings)")
        return 1
    else:
        print(f"RESULT: PASSED ({len(warnings)} warnings)")
        return 0


if __name__ == "__main__":
    sys.exit(main())
