#!/usr/bin/env python3
"""Build parallel shard manifests for overnight content generation.

Splits remaining work across N parallel workers, each with its own
manifest and checkpoint file.

Usage:
    python tools/overnight/build_parallel_manifests.py [--workers N] [--batch-size N]
"""

import json
import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required.")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent.parent
DOMAINS_DIR = ROOT / "domains"
OVERNIGHT_DIR = ROOT / "tools" / "overnight"

STAGE_PRIORITY = {
    "pre-formal": 0,
    "concrete-operations": 1,
    "abstract-reasoning": 2,
    "formal-systems": 3,
    "advanced": 4,
}

EXPLAINER_PROMPT = (
    "You are adding Explainer sections to topics in the Open Knowledge Graph.\n\n"
    "First, read domains/economics/microeconomics/supply-and-demand-basics.md as an example "
    "of a completed topic with an Explainer section.\n\n"
    "For each of these topic IDs, do the following:\n"
    "1. Find and read the topic file (search in domains/ using the topic ID as the filename, e.g. domains/*/*/{{topic-id}}.md)\n"
    "2. If it already has a ## Explainer section, SKIP it\n"
    "3. Otherwise, add a new section at the END of the file:\n\n"
    "## Explainer\n\n"
    "[3-5 paragraphs that TEACH the concept to someone who has completed the prerequisites]\n\n"
    "Rules:\n"
    "- Explainers should build intuition, not just restate the Core Idea\n"
    "- Use concrete examples and analogies\n"
    "- Connect to prerequisites the learner already knows\n"
    "- Build from simple to complex within the explanation\n"
    "- Use **bold** for key terms on first introduction\n"
    "- Do NOT modify any existing content in the file — only append the new section\n"
    "- Use the Edit tool to append to the end of the file\n\n"
    "Topics to process:\n{items}"
)

QUESTIONS_PROMPT = (
    "You are adding Questions sections to topics in the Open Knowledge Graph.\n\n"
    "First, read domains/economics/microeconomics/supply-and-demand-basics.md as an example "
    "of a completed topic with a Questions section.\n\n"
    "For each of these topic IDs, do the following:\n"
    "1. Find and read the topic file (search in domains/ using the topic ID as the filename, e.g. domains/*/*/{{topic-id}}.md)\n"
    "2. If it already has a ## Questions section, SKIP it\n"
    "3. Otherwise, add a new ## Questions section. If the file has a ## Explainer section, "
    "insert Questions BEFORE it. Otherwise, add it at the END of the file.\n\n"
    "The format MUST be exactly:\n\n"
    "## Questions\n\n"
    "```yaml\n"
    "- question: \"...\"\n"
    "  type: multiple-choice\n"
    "  options:\n"
    "    - \"...\"\n"
    "    - \"...\"\n"
    "    - \"...\"\n"
    "    - \"...\"\n"
    "  answer: 0\n"
    "  explanation: \"...\"\n\n"
    "- question: \"...\"\n"
    "  type: true-false\n"
    "  answer: true\n"
    "  explanation: \"...\"\n\n"
    "- question: \"...\"\n"
    "  type: short-answer\n"
    "  answer: \"...\"\n"
    "  explanation: \"...\"\n"
    "```\n\n"
    "Rules:\n"
    "- 3 questions per topic (one multiple-choice, one true-false, one short-answer)\n"
    "- Questions must test UNDERSTANDING, not memorization\n"
    "- At least one question should target a common misconception\n"
    "- Multiple-choice: 4 plausible options, answer is the 0-based index of the correct one\n"
    "- Explanations are REQUIRED and should explain WHY the answer is correct\n"
    "- Do NOT modify any existing content in the file — only add the new section\n"
    "- Use the Edit tool to insert/append\n\n"
    "Topics to process:\n{items}"
)


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
            "has_explainer": "## Explainer" in text,
            "has_questions": "## Questions" in text,
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


def split_into_shards(items, n_shards):
    """Round-robin split to ensure each shard gets a mix."""
    shards = [[] for _ in range(n_shards)]
    for i, item in enumerate(items):
        shards[i % n_shards].append(item)
    return shards


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=5, help="Number of parallel workers")
    parser.add_argument("--batch-size", type=int, default=10, help="Topics per batch")
    args = parser.parse_args()

    n_workers = args.workers
    batch_size = args.batch_size

    print("Scanning topics...")
    topics = scan_topics()
    print(f"Found {len(topics)} topics")

    # Load already-completed items from existing checkpoints
    completed_explainers = set()
    completed_questions = set()

    # Check main checkpoint
    main_cp = OVERNIGHT_DIR / "explainer-checkpoint.json"
    if main_cp.exists():
        cp = json.loads(main_cp.read_text())
        completed_explainers.update(cp.get("completed", []))

    # Check shard checkpoints
    for i in range(1, 20):
        cp_path = OVERNIGHT_DIR / f"explainer-shard-{i}-checkpoint.json"
        if cp_path.exists():
            cp = json.loads(cp_path.read_text())
            completed_explainers.update(cp.get("completed", []))
        cp_path = OVERNIGHT_DIR / f"questions-shard-{i}-checkpoint.json"
        if cp_path.exists():
            cp = json.loads(cp_path.read_text())
            completed_questions.update(cp.get("completed", []))

    # Explainers: all topics missing them, excluding already completed
    need_explainer = [
        t["id"] for t in topics
        if not t["has_explainer"] and t["id"] not in completed_explainers
    ]
    print(f"Topics needing explainers: {len(need_explainer)} (excl. {len(completed_explainers)} already done)")

    # Questions: prioritized by hub connectivity + stage
    print("Computing successor counts for question priority...")
    successor_counts = build_successor_counts()

    need_questions = [t for t in topics if not t["has_questions"] and t["id"] not in completed_questions]
    need_questions.sort(
        key=lambda t: successor_counts.get(t["id"], 0) + (4 - STAGE_PRIORITY.get(t["stage"], 2)) * 5,
        reverse=True,
    )
    need_questions_ids = [t["id"] for t in need_questions]
    print(f"Topics needing questions: {len(need_questions_ids)}")

    # Split into shards
    explainer_shards = split_into_shards(need_explainer, n_workers)
    questions_shards = split_into_shards(need_questions_ids, n_workers)

    print(f"\nSplitting into {n_workers} shards (batch_size={batch_size}):")
    for i, shard in enumerate(explainer_shards, 1):
        print(f"  Explainer shard {i}: {len(shard)} topics ({len(shard) // batch_size + 1} batches)")

    # Write shard manifests
    for i in range(n_workers):
        shard_num = i + 1

        # Explainer shard
        manifest = {
            "name": f"explainers-shard-{shard_num}",
            "mode": "batch",
            "working_dir": "~/open-knowledge-graph",
            "model": "sonnet",
            "batch_size": batch_size,
            "max_turns_per_batch": 120,
            "max_budget_usd": 50.0,
            "allowed_tools": "Bash,Read,Edit,Write,Glob,Grep",
            "retry_wait_minutes": 5,
            "max_retries": 50,
            "checkpoint_file": f"tools/overnight/explainer-shard-{shard_num}-checkpoint.json",
            "prompt_template": EXPLAINER_PROMPT,
            "items": explainer_shards[i],
        }
        path = OVERNIGHT_DIR / f"explainer-shard-{shard_num}.json"
        path.write_text(json.dumps(manifest, indent=2))

        # Questions shard
        manifest = {
            "name": f"questions-shard-{shard_num}",
            "mode": "batch",
            "working_dir": "~/open-knowledge-graph",
            "model": "sonnet",
            "batch_size": batch_size,
            "max_turns_per_batch": 120,
            "max_budget_usd": 50.0,
            "allowed_tools": "Bash,Read,Edit,Write,Glob,Grep",
            "retry_wait_minutes": 5,
            "max_retries": 50,
            "checkpoint_file": f"tools/overnight/questions-shard-{shard_num}-checkpoint.json",
            "prompt_template": QUESTIONS_PROMPT,
            "items": questions_shards[i],
        }
        path = OVERNIGHT_DIR / f"questions-shard-{shard_num}.json"
        path.write_text(json.dumps(manifest, indent=2))

    print(f"\nWrote {n_workers * 2} manifest files.")
    print(f"\nTo launch all workers:")
    print(f"  bash tools/overnight/run-parallel.sh")
    print(f"\nTo check progress:")
    print(f"  python tools/overnight/check_progress.py")


if __name__ == "__main__":
    main()
