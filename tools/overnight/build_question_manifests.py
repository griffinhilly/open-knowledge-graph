#!/usr/bin/env python3
"""Build prioritized shard manifests for bulk question generation.

Prioritization:
  1. Pre-formal + concrete-operations (assessment Phase 1 warm-up)
  2. Abstract-reasoning with high successor counts (propagation hubs)
  3. Abstract-reasoning remainder
  4. Formal-systems by successor count
  5. Advanced by successor count

Within each shard, topics are ordered by priority so the most valuable
ones get processed first even if the shard doesn't finish.

Usage:
    python tools/overnight/build_question_manifests.py [--shards N] [--batch-size N]
    python tools/overnight/build_question_manifests.py --dry-run
"""

import json
import re
import argparse
from pathlib import Path
from collections import defaultdict

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required.")
    raise SystemExit(1)

ROOT = Path(__file__).resolve().parent.parent.parent
DOMAINS_DIR = ROOT / "domains"
OVERNIGHT_DIR = ROOT / "tools" / "overnight"

STAGE_PRIORITY = {
    "pre-formal": 50,
    "concrete-operations": 40,
    "abstract-reasoning": 20,
    "formal-systems": 10,
    "advanced": 0,
}

QUESTIONS_PROMPT = """\
You are adding Questions sections to topics in the Open Knowledge Graph.

## Example

Read domains/economics/microeconomics/supply-and-demand-basics.md to see a \
completed topic with excellent questions. Notice how each question targets the \
KEY INSIGHT of the topic — the thing that separates genuine understanding from \
surface familiarity — and how the true-false question directly attacks the most \
common misconception.

## Your task

For each topic ID below:
1. Find and read the topic file: domains/*/*/{{topic-id}}.md
2. If it already has a ## Questions section, SKIP it
3. Read the Core Idea, any Common Misconceptions, and the Explainer to \
identify the KEY INSIGHT — the conceptual "aha" that makes everything else click
4. Write 5 questions that test whether someone truly grasps that key insight
5. Add the ## Questions section. If the file has a ## Explainer section, \
insert Questions BEFORE it. Otherwise add at the END of the file.

## Question format

```yaml
- question: "..."
  type: multiple-choice
  options:
    - "..."
    - "..."
    - "..."
    - "..."
  answer: 0
  explanation: "..."

- question: "..."
  type: multiple-choice
  options:
    - "..."
    - "..."
    - "..."
    - "..."
  answer: 0
  explanation: "..."

- question: "..."
  type: true-false
  answer: true
  explanation: "..."

- question: "..."
  type: true-false
  answer: false
  explanation: "..."

- question: "..."
  type: short-answer
  answer: "..."
  explanation: "..."
```

## Question design rules

- **5 questions per topic**: 2 multiple-choice, 2 true-false, 1 short-answer
- **Every question must test UNDERSTANDING, not recall.** A student who memorized \
the definition but doesn't understand the concept should get it wrong.
- **At least one MC question should present a scenario** where the common \
misconception gives a different answer than the correct understanding. Make the \
misconception option plausible — it should be the most tempting wrong answer.
- **True-false statements should be subtle.** Avoid trivially true definitions. \
The best T/F questions state something that SOUNDS right but is wrong (or vice versa). \
One should be true, one should be false.
- **The short-answer question should ask "why" or "how"** — not "what is the \
definition of." It should require the student to explain the key insight in \
their own words.
- **Explanations are REQUIRED** and should teach — explain WHY the answer is \
correct and WHY the common wrong answer is wrong.
- **MC options**: 4 options, 0-indexed answer. Distractors should represent \
real misconceptions, not obviously silly answers.
- Do NOT modify any existing content in the file — only add the new section.
- Use the Edit tool to insert/append.

Topics to process:
{items}"""


def scan_topics():
    """Scan all topics and return metadata."""
    topics = []
    for filepath in sorted(DOMAINS_DIR.rglob("*.md")):
        if filepath.name.startswith("_"):
            continue
        text = filepath.read_text(encoding="utf-8")
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
        if not match:
            continue
        try:
            data = yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            continue
        if not data or "id" not in data:
            continue

        topics.append({
            "id": data["id"],
            "stage": data.get("stage", "abstract-reasoning"),
            "has_questions": "## Questions" in text,
            "has_explainer": "## Explainer" in text,
        })
    return topics


def build_successor_counts():
    """Count how many topics list each topic as a prerequisite."""
    ref_counts = defaultdict(int)
    for filepath in sorted(DOMAINS_DIR.rglob("*.md")):
        if filepath.name.startswith("_"):
            continue
        text = filepath.read_text(encoding="utf-8")
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
        if not match:
            continue
        try:
            data = yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            continue
        if not data:
            continue
        for p in data.get("prerequisites", []):
            if isinstance(p, dict) and "id" in p:
                ref_counts[p["id"]] += 1
    return ref_counts


def prioritize(topics, successor_counts):
    """Sort topics by priority: stage weight + successor count."""
    for t in topics:
        t["priority"] = STAGE_PRIORITY.get(t["stage"], 10) + successor_counts.get(t["id"], 0)
    topics.sort(key=lambda t: t["priority"], reverse=True)
    return topics


def split_into_shards(items, n_shards):
    """Round-robin split preserving priority order within each shard."""
    shards = [[] for _ in range(n_shards)]
    for i, item in enumerate(items):
        shards[i % n_shards].append(item)
    return shards


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--shards", type=int, default=60, help="Number of parallel shards")
    parser.add_argument("--batch-size", type=int, default=10, help="Topics per batch")
    parser.add_argument("--dry-run", action="store_true", help="Show stats without writing")
    parser.add_argument("--prefix", default="q5", help="Manifest filename prefix")
    args = parser.parse_args()

    print("Scanning topics...")
    topics = scan_topics()
    print(f"Found {len(topics)} total topics")

    # Filter to those needing questions
    need_questions = [t for t in topics if not t["has_questions"]]
    print(f"Need questions: {len(need_questions)}")

    # Check existing checkpoints for already-completed items
    completed = set()
    for cp_file in OVERNIGHT_DIR.glob(f"{args.prefix}-shard-*-checkpoint.json"):
        try:
            cp = json.loads(cp_file.read_text())
            completed.update(cp.get("completed", []))
        except Exception:
            pass
    if completed:
        before = len(need_questions)
        need_questions = [t for t in need_questions if t["id"] not in completed]
        print(f"Excluding {before - len(need_questions)} already completed from prior checkpoints")

    # Prioritize
    print("Computing successor counts...")
    successor_counts = build_successor_counts()
    need_questions = prioritize(need_questions, successor_counts)

    # Show tier breakdown
    tiers = [
        ("Pre-formal + Concrete", lambda t: t["stage"] in ("pre-formal", "concrete-operations")),
        ("Abstract-reasoning (3+ successors)", lambda t: t["stage"] == "abstract-reasoning" and successor_counts.get(t["id"], 0) >= 3),
        ("Abstract-reasoning (0-2 successors)", lambda t: t["stage"] == "abstract-reasoning" and successor_counts.get(t["id"], 0) < 3),
        ("Formal-systems", lambda t: t["stage"] == "formal-systems"),
        ("Advanced", lambda t: t["stage"] == "advanced"),
    ]
    cumulative = 0
    for name, pred in tiers:
        count = sum(1 for t in need_questions if pred(t))
        cumulative += count
        print(f"  {name}: {count} (cumulative: {cumulative})")

    if args.dry_run:
        print(f"\nDRY RUN: would create {args.shards} shard manifests")
        print(f"  ~{len(need_questions) // args.shards} topics per shard")
        print(f"  ~{len(need_questions) // args.shards // args.batch_size + 1} batches per shard")
        return

    # Build shards
    topic_ids = [t["id"] for t in need_questions]
    shards = split_into_shards(topic_ids, args.shards)

    print(f"\nCreating {args.shards} shard manifests (batch_size={args.batch_size}):")

    for i, shard in enumerate(shards):
        shard_num = i + 1
        manifest = {
            "name": f"{args.prefix}-shard-{shard_num}",
            "mode": "batch",
            "working_dir": "~/Projects/griffin/open-knowledge-graph",
            "model": "sonnet",
            "batch_size": args.batch_size,
            "max_turns_per_batch": 150,
            "max_budget_usd": 50.0,
            "allowed_tools": "Bash,Read,Edit,Write,Glob,Grep",
            "retry_wait_minutes": 5,
            "max_retries": 50,
            "checkpoint_file": f"tools/overnight/{args.prefix}-shard-{shard_num}-checkpoint.json",
            "prompt_template": QUESTIONS_PROMPT,
            "items": shard,
        }
        path = OVERNIGHT_DIR / f"{args.prefix}-shard-{shard_num}.json"
        path.write_text(json.dumps(manifest, indent=2))
        print(f"  {args.prefix}-shard-{shard_num}.json: {len(shard)} topics")

    print(f"\nWrote {args.shards} manifests.")
    print(f"Total topics: {len(topic_ids)}")
    print(f"\nTo launch:")
    print(f"  bash tools/overnight/run-parallel.sh {args.prefix}")
    print(f"\nTo check progress:")
    print(f"  python tools/overnight/check_progress.py")


if __name__ == "__main__":
    main()
