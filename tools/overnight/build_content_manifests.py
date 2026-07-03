#!/usr/bin/env python3
"""Build overnight manifests for Explainer and Questions generation.

Scans all topics, identifies missing content, and produces two manifests:
1. explainer-manifest.json — all topics missing Explainers (run first)
2. questions-manifest.json — topics missing Questions, prioritized by
   hub connectivity + developmental stage (younger stages first)

Usage:
    python tools/overnight/build_content_manifests.py
"""

import json
import re
import sys
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

# Developmental stages ordered from youngest to oldest
STAGE_PRIORITY = {
    "pre-formal": 0,
    "concrete-operations": 1,
    "abstract-reasoning": 2,
    "formal-systems": 3,
    "advanced": 4,
}


def scan_topics():
    """Scan all topics and return metadata + content presence."""
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

        tid = data["id"]
        has_explainer = "## Explainer" in text
        has_questions = "## Questions" in text
        prereqs = data.get("prerequisites", [])
        n_prereqs = len(prereqs) if isinstance(prereqs, list) else 0
        stage = data.get("stage", "abstract-reasoning")

        topics.append({
            "id": tid,
            "domain": data.get("domain", ""),
            "course": data.get("course", ""),
            "stage": stage,
            "has_explainer": has_explainer,
            "has_questions": has_questions,
            "n_prereqs": n_prereqs,
        })

    return topics


def build_successor_counts(topics):
    """Count how many topics list each topic as a prerequisite (successor count = hub-ness)."""
    successor_count = defaultdict(int)
    for t in topics:
        # We need to re-read prereqs to get the actual IDs
        pass
    # More efficient: scan files for prerequisite references
    all_ids = {t["id"] for t in topics}
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


def priority_score(topic, successor_counts):
    """Compute priority score for questions generation.
    Higher = process first.

    Combines:
    - Successor count (hub-ness): more successors = higher priority
    - Stage: younger stages get a boost
    """
    hub_score = successor_counts.get(topic["id"], 0)
    stage_boost = (4 - STAGE_PRIORITY.get(topic["stage"], 2)) * 5  # 0-20 points
    return hub_score + stage_boost


def main():
    print("Scanning topics...")
    topics = scan_topics()
    print(f"Found {len(topics)} topics")

    print("Computing successor counts...")
    successor_counts = build_successor_counts(topics)

    # Explainer manifest: all topics missing explainers
    need_explainer = [t["id"] for t in topics if not t["has_explainer"]]
    print(f"Topics needing explainers: {len(need_explainer)}")

    # Questions manifest: all topics missing questions, prioritized
    need_questions = [t for t in topics if not t["has_questions"]]
    need_questions.sort(key=lambda t: priority_score(t, successor_counts), reverse=True)
    need_questions_ids = [t["id"] for t in need_questions]
    print(f"Topics needing questions: {len(need_questions_ids)}")

    # Print top 20 question priorities for verification
    print("\nTop 20 question priorities:")
    for t in need_questions[:20]:
        sc = successor_counts.get(t["id"], 0)
        sp = priority_score(t, successor_counts)
        print(f"  {t['id']:50s} successors={sc:3d} stage={t['stage']:25s} score={sp}")

    # Stage distribution for questions
    stage_dist = defaultdict(int)
    for t in need_questions:
        stage_dist[t["stage"]] += 1
    print("\nQuestions stage distribution:")
    for stage in sorted(stage_dist, key=lambda s: STAGE_PRIORITY.get(s, 99)):
        print(f"  {stage}: {stage_dist[stage]}")

    # Build explainer manifest
    explainer_manifest = {
        "name": "generate-explainers",
        "mode": "batch",
        "working_dir": "~/open-knowledge-graph",
        "model": "opus",
        "batch_size": 5,
        "max_turns_per_batch": 80,
        "max_budget_usd": 50.0,
        "allowed_tools": "Bash,Read,Edit,Write,Glob,Grep",
        "retry_wait_minutes": 15,
        "max_retries": 30,
        "checkpoint_file": "tools/overnight/explainer-checkpoint.json",
        "prompt_template": (
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
        ),
        "items": need_explainer,
    }

    # Build questions manifest
    questions_manifest = {
        "name": "generate-questions",
        "mode": "batch",
        "working_dir": "~/open-knowledge-graph",
        "model": "opus",
        "batch_size": 3,
        "max_turns_per_batch": 80,
        "max_budget_usd": 50.0,
        "allowed_tools": "Bash,Read,Edit,Write,Glob,Grep",
        "retry_wait_minutes": 15,
        "max_retries": 30,
        "checkpoint_file": "tools/overnight/questions-checkpoint.json",
        "prompt_template": (
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
        ),
        "items": need_questions_ids,
    }

    # Write manifests
    exp_path = OVERNIGHT_DIR / "explainer-manifest.json"
    with open(exp_path, "w", encoding="utf-8") as f:
        json.dump(explainer_manifest, f, indent=2)
    print(f"\nWrote {exp_path} ({len(need_explainer)} items)")

    q_path = OVERNIGHT_DIR / "questions-manifest.json"
    with open(q_path, "w", encoding="utf-8") as f:
        json.dump(questions_manifest, f, indent=2)
    print(f"Wrote {q_path} ({len(need_questions_ids)} items)")

    print(f"\nTo run:")
    print(f"  nohup python ~/.claude/scripts/overnight.py tools/overnight/explainer-manifest.json &")
    print(f"  # When explainers finish:")
    print(f"  nohup python ~/.claude/scripts/overnight.py tools/overnight/questions-manifest.json &")


if __name__ == "__main__":
    main()
