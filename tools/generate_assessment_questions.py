#!/usr/bin/env python3
"""Extract questions from OKG topic files and build a quiz question bank.

Parses all topic markdown files, extracts questions from ## Questions sections,
computes topic connectivity, and selects a curated question pool for the
interactive quiz. Outputs output/assessment-questions.json.

Usage:
    python tools/generate_assessment_questions.py
"""

import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install with: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "domains"
OUTPUT_DIR = ROOT / "output"

STAGES = ["pre-formal", "concrete-operations", "abstract-reasoning",
          "formal-systems", "advanced"]

STAGE_DIFFICULTY = {
    "pre-formal": 0.2,
    "concrete-operations": 0.4,
    "abstract-reasoning": 0.6,
    "formal-systems": 0.8,
    "advanced": 0.9,
}

# Quiz pool sizing
WARMUP_TOPICS_PER_DOMAIN = 6
EXPLORE_TOPICS_PER_DOMAIN_STAGE = 4
MAX_QUESTIONS_PER_TOPIC = 2


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def parse_frontmatter(filepath):
    """Extract YAML frontmatter and body from a topic file."""
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", text, re.DOTALL)
    if not match:
        return None, ""
    try:
        data = yaml.safe_load(match.group(1))
        return data, match.group(2)
    except yaml.YAMLError:
        return None, ""


def extract_questions(body):
    """Extract questions from ## Questions YAML code block."""
    match = re.search(r"## Questions\s*\n+```yaml\s*\n(.*?)```", body, re.DOTALL)
    if not match:
        return []
    try:
        questions = yaml.safe_load(match.group(1))
        return questions if isinstance(questions, list) else []
    except yaml.YAMLError:
        return []


# ---------------------------------------------------------------------------
# Loading & graph
# ---------------------------------------------------------------------------

def load_all_topics():
    """Load all topics, extracting questions where present."""
    topics = []
    for filepath in sorted(DOMAINS_DIR.rglob("*.md")):
        if filepath.name.startswith("_"):
            continue
        data, body = parse_frontmatter(filepath)
        if data and "id" in data:
            data["_questions"] = extract_questions(body)
            topics.append(data)
    return topics


def compute_connectivity(topics):
    """Compute in_degree + out_degree for each topic."""
    children = defaultdict(int)
    parents = defaultdict(int)

    for t in topics:
        tid = t["id"]
        prereqs = t.get("prerequisites") or []
        if isinstance(prereqs, list):
            for p in prereqs:
                if isinstance(p, dict) and "id" in p:
                    children[p["id"]] += 1
                    parents[tid] += 1

    conn = {}
    for t in topics:
        tid = t["id"]
        conn[tid] = children.get(tid, 0) + parents.get(tid, 0)
    return conn


# ---------------------------------------------------------------------------
# Question filtering & selection
# ---------------------------------------------------------------------------

def is_quizzable(q):
    """Check if a question is suitable for auto-graded quiz (MC or TF)."""
    qtype = q.get("type", "")
    if qtype == "multiple-choice":
        return (isinstance(q.get("options"), list) and
                len(q["options"]) >= 2 and
                isinstance(q.get("answer"), int) and
                0 <= q["answer"] < len(q["options"]))
    elif qtype == "true-false":
        return isinstance(q.get("answer"), bool)
    return False


def make_question_entry(topic, question, connectivity):
    """Build a flat question object for the quiz JSON."""
    stage = topic.get("stage", "concrete-operations")
    entry = {
        "topicId": topic["id"],
        "topicTitle": topic.get("title", topic["id"]),
        "domain": topic.get("domain", "unknown"),
        "course": topic.get("course", "unknown"),
        "stage": stage,
        "difficulty": STAGE_DIFFICULTY.get(stage, 0.5),
        "connectivity": connectivity.get(topic["id"], 0),
        "question": question["question"],
        "type": question["type"],
        "answer": question["answer"],
        "explanation": question.get("explanation", ""),
    }
    if question.get("options"):
        entry["options"] = question["options"]
    return entry


def select_pool(topics, connectivity):
    """Select warmup and exploration question pools."""
    # Group topics with quizzable questions by domain+stage
    by_domain_stage = defaultdict(list)
    for t in topics:
        quizzable = [q for q in t.get("_questions", []) if is_quizzable(q)]
        if not quizzable:
            continue
        domain = t.get("domain", "unknown")
        stage = t.get("stage", "unknown")
        by_domain_stage[(domain, stage)].append((t, quizzable))

    # Sort within each group by connectivity descending
    for key in by_domain_stage:
        by_domain_stage[key].sort(
            key=lambda x: connectivity.get(x[0]["id"], 0), reverse=True
        )

    all_domains = sorted(set(k[0] for k in by_domain_stage))

    # --- Warmup pool: easiest available stages per domain ---
    # Prefer pre-formal + concrete; fall back to lowest available stages
    warmup = []
    for domain in all_domains:
        domain_topics = []
        # Find the lowest 2 stages that have topics in this domain
        available_stages = [s for s in STAGES
                           if by_domain_stage.get((domain, s))]
        warmup_stages = available_stages[:2] if available_stages else []
        for stage in warmup_stages:
            domain_topics.extend(by_domain_stage.get((domain, stage), []))
        # Sort by connectivity descending
        domain_topics.sort(
            key=lambda x: connectivity.get(x[0]["id"], 0), reverse=True
        )
        for topic, questions in domain_topics[:WARMUP_TOPICS_PER_DOMAIN]:
            for q in questions[:MAX_QUESTIONS_PER_TOPIC]:
                warmup.append(make_question_entry(topic, q, connectivity))

    # --- Exploration pool: all stages, per domain ---
    exploration = {}
    for domain in all_domains:
        domain_questions = []
        for stage in STAGES:
            stage_topics = by_domain_stage.get((domain, stage), [])
            for topic, questions in stage_topics[:EXPLORE_TOPICS_PER_DOMAIN_STAGE]:
                for q in questions[:MAX_QUESTIONS_PER_TOPIC]:
                    domain_questions.append(
                        make_question_entry(topic, q, connectivity)
                    )
        if domain_questions:
            exploration[domain] = domain_questions

    return warmup, exploration


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def build_topic_index(topics):
    """Build a compact domain->stage->[topicIds] index for post-assessment inference.

    This lets the quiz page know every topic's domain and stage without
    embedding the full topic data.
    """
    index = defaultdict(lambda: defaultdict(list))
    for t in topics:
        domain = t.get("domain", "unknown")
        stage = t.get("stage", "unknown")
        if stage in STAGES:
            index[domain][stage].append(t["id"])

    # Convert to plain dict for JSON serialization
    return {d: dict(stages) for d, stages in sorted(index.items())}


def main():
    print("Loading topics...")
    topics = load_all_topics()
    total = len(topics)
    with_q = sum(1 for t in topics if t.get("_questions"))
    total_q = sum(len(t.get("_questions", [])) for t in topics)
    print(f"  {total} topics, {with_q} with questions, {total_q} total questions")

    print("Computing connectivity...")
    conn = compute_connectivity(topics)

    print("Selecting quiz pool...")
    warmup, exploration = select_pool(topics, conn)

    explore_total = sum(len(v) for v in exploration.values())
    print(f"  Warmup pool: {len(warmup)} questions")
    print(f"  Exploration pool: {explore_total} questions across {len(exploration)} domains")

    for domain in sorted(exploration):
        stages = set(q["stage"] for q in exploration[domain])
        print(f"    {domain}: {len(exploration[domain])} questions ({', '.join(sorted(stages))})")

    print("Building topic index...")
    topic_index = build_topic_index(topics)
    index_topics = sum(len(ids) for stages in topic_index.values() for ids in stages.values())
    print(f"  {index_topics} topics across {len(topic_index)} domains")

    output = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "stats": {
            "total_topics": total,
            "topics_with_questions": with_q,
            "total_questions": total_q,
            "warmup_pool": len(warmup),
            "exploration_pool": explore_total,
            "indexed_topics": index_topics,
        },
        "warmup": warmup,
        "exploration": exploration,
        "topicIndex": topic_index,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / "assessment-questions.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    size_kb = out_path.stat().st_size / 1024
    print(f"\nWrote {out_path.relative_to(ROOT)} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
