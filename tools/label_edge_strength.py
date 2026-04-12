#!/usr/bin/env python3
"""Label prereq edges as hard or soft via Haiku.

Purpose
-------
The OKG has ~37K prerequisite edges. They're already ~54% hard / 46% soft
from the original manual annotation pass, but the classification is uneven
and some "hard" labels are judgment calls that deserve re-review. This
script runs Haiku over every edge, gets a hard/soft verdict, and writes
the results to a JSON file for sample QA before any source files are
touched.

Design
------
- **Per-topic batching**: One API call per topic (not per edge), asking
  Haiku to classify all of that topic's prereqs in a single response.
  Cuts cost and latency.
- **Dry-run by default**: Without `--apply`, the script only writes
  `data/edge-strength-labels.json` and never modifies topic markdown.
- **Sample flag**: `--sample N` runs on N random topics first so you
  can eyeball ~200 edges before committing to the full pass.
- **Apply flag**: `--apply` reads a previously-written labels JSON and
  rewrites each topic's prerequisites block with the new types. Never
  generates labels and applies in one pass — always two separate runs,
  one to label, one to apply, with human QA between.
- **Resume**: `--resume` skips topics already labeled in the output file.

Cost estimate
-------------
~15K topics × 1 call/topic via Haiku = ~$5-15 total (per plan doc).
Do NOT run without explicit approval.

Usage
-----
    # 1. Sample 200 topics (~600 edges), eyeball the output:
    python tools/label_edge_strength.py --sample 200

    # 2. If sample looks good (<10% error), run the full pass:
    python tools/label_edge_strength.py --resume

    # 3. After reviewing data/edge-strength-labels.json, apply:
    python tools/label_edge_strength.py --apply

QA protocol
-----------
After a sample run, open data/edge-strength-labels.json and pick 200
random edges. For each, judge whether Haiku's verdict matches what a
human expert would call it. If the error rate is <10%, the full labeling
pass is trusted and `--apply` is safe. If the error rate is >=10%, revise
the PROMPT constant below and re-run the sample. Document the error rate
and any prompt revisions in MEMORY.md before applying.
"""

from __future__ import annotations

import argparse
import json
import os
import random
import sys
import time
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required.")
    sys.exit(1)

try:
    from anthropic import Anthropic
except ImportError:
    Anthropic = None  # Only required when actually calling the API

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "domains"
DATA_DIR = ROOT / "data"
LABELS_OUTPUT = DATA_DIR / "edge-strength-labels.json"

MODEL = "claude-haiku-4-5-20251001"
MAX_RETRIES = 3

PROMPT = """You are classifying prerequisite relationships in a knowledge graph.

Topic: {topic_title}
Domain: {domain}
Course: {course}

Prerequisites to classify:
{prereq_list}

For each prerequisite, decide whether it is:
- "hard": the topic cannot be meaningfully learned without already knowing this prerequisite. Skipping it would make the topic incomprehensible.
- "soft": the prerequisite is helpful context or a related concept, but a motivated learner could work through the topic without it.

Return ONLY a JSON object mapping each prerequisite's ID to "hard" or "soft".
Example: {{"derivative-of-a-function": "hard", "chain-rule": "soft"}}

Do not include explanations or any text outside the JSON object."""


def load_all_topics() -> dict:
    """Load every topic file as {topic_id: (filepath, frontmatter, body)}."""
    topics = {}
    for md in sorted(DOMAINS_DIR.rglob("*.md")):
        if md.name.startswith("_"):
            continue
        text = md.read_text(encoding="utf-8", errors="replace")
        if not text.startswith("---"):
            continue
        try:
            parts = text.split("---", 2)
            if len(parts) < 3:
                continue
            fm = yaml.safe_load(parts[1]) or {}
        except Exception:
            continue
        if "id" not in fm:
            continue
        topics[fm["id"]] = (md, fm, parts[2])
    return topics


def build_prereq_list(fm: dict) -> list[dict]:
    """Extract {id, current_type, hint} entries from a topic's prerequisites."""
    out = []
    for p in fm.get("prerequisites") or []:
        if isinstance(p, dict) and "id" in p:
            out.append({
                "id": p["id"],
                "current_type": p.get("type", "hard"),
            })
    return out


def call_haiku(client, topic_id: str, fm: dict, prereqs: list[dict]) -> dict:
    """Call Haiku, return {prereq_id: "hard"|"soft"} or empty dict on failure."""
    prompt = PROMPT.format(
        topic_title=fm.get("title", topic_id),
        domain=fm.get("domain", "unknown"),
        course=fm.get("course", "unknown"),
        prereq_list="\n".join(f"- {p['id']}" for p in prereqs),
    )

    for attempt in range(MAX_RETRIES):
        try:
            resp = client.messages.create(
                model=MODEL,
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}],
            )
            text = resp.content[0].text.strip()
            # Strip any code fence
            if text.startswith("```"):
                text = text.strip("`").lstrip("json").strip()
            data = json.loads(text)
            if not isinstance(data, dict):
                continue
            # Normalize values
            clean = {}
            for k, v in data.items():
                if isinstance(v, str) and v.lower() in ("hard", "soft"):
                    clean[k] = v.lower()
            return clean
        except Exception as e:
            if attempt == MAX_RETRIES - 1:
                print(f"  [FAIL] {topic_id}: {e}")
                return {}
            time.sleep(1 + attempt)
    return {}


def label_topics(topics: dict, topic_ids: list[str], existing: dict) -> dict:
    """Run Haiku over the given topic IDs, merge with existing labels."""
    if Anthropic is None:
        print("ERROR: `anthropic` package not installed. pip install anthropic")
        sys.exit(1)
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set.")
        sys.exit(1)

    client = Anthropic()
    labels = dict(existing)  # {topic_id: {prereq_id: type}}

    total = len(topic_ids)
    print(f"Labeling {total} topics via {MODEL}...")
    start = time.time()

    for i, tid in enumerate(topic_ids, 1):
        _, fm, _ = topics[tid]
        prereqs = build_prereq_list(fm)
        if not prereqs:
            continue
        result = call_haiku(client, tid, fm, prereqs)
        if result:
            labels[tid] = result
        if i % 50 == 0 or i == total:
            elapsed = time.time() - start
            rate = i / elapsed if elapsed > 0 else 0
            print(f"  {i}/{total}  ({rate:.1f}/s, {labels.__len__()} labeled)")
        # Persist incrementally so interruptions don't lose progress
        if i % 100 == 0:
            DATA_DIR.mkdir(exist_ok=True)
            LABELS_OUTPUT.write_text(json.dumps(labels, indent=2))

    DATA_DIR.mkdir(exist_ok=True)
    LABELS_OUTPUT.write_text(json.dumps(labels, indent=2))
    return labels


def apply_labels(topics: dict, labels: dict) -> tuple[int, int]:
    """Rewrite topic markdown files with the new type labels.
    Returns (files_changed, edges_changed)."""
    files_changed = 0
    edges_changed = 0

    for tid, topic_labels in labels.items():
        if tid not in topics:
            continue
        filepath, fm, body = topics[tid]
        prereqs = fm.get("prerequisites") or []
        changed = False
        for p in prereqs:
            if isinstance(p, dict) and "id" in p and p["id"] in topic_labels:
                new_type = topic_labels[p["id"]]
                if p.get("type") != new_type:
                    p["type"] = new_type
                    changed = True
                    edges_changed += 1
        if changed:
            fm["prerequisites"] = prereqs
            fm_text = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True)
            filepath.write_text(f"---\n{fm_text}---{body}", encoding="utf-8")
            files_changed += 1

    return files_changed, edges_changed


def main():
    parser = argparse.ArgumentParser(description="Label prereq edges as hard/soft via Haiku")
    parser.add_argument("--sample", type=int, default=None,
                        help="Label a random sample of N topics (for QA). Default: full pass.")
    parser.add_argument("--resume", action="store_true",
                        help="Skip topics already present in the existing labels file.")
    parser.add_argument("--apply", action="store_true",
                        help="Apply existing labels file to topic markdown. No API calls.")
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed for --sample selection.")
    args = parser.parse_args()

    print("Loading topics...")
    topics = load_all_topics()
    print(f"Loaded {len(topics)} topics")

    existing: dict = {}
    if LABELS_OUTPUT.exists():
        existing = json.loads(LABELS_OUTPUT.read_text())
        print(f"Found existing labels for {len(existing)} topics")

    if args.apply:
        if not existing:
            print("ERROR: no labels file to apply. Run labeling first.")
            sys.exit(1)
        print("Applying labels to source markdown files...")
        fc, ec = apply_labels(topics, existing)
        print(f"Done: {fc} files rewritten, {ec} edge types changed.")
        return

    # Selecting which topics to label
    candidates = [tid for tid in topics if build_prereq_list(topics[tid][1])]
    if args.resume:
        candidates = [tid for tid in candidates if tid not in existing]
    if args.sample:
        random.seed(args.seed)
        candidates = random.sample(candidates, min(args.sample, len(candidates)))

    if not candidates:
        print("Nothing to label. (Use --apply to write existing labels to source files.)")
        return

    label_topics(topics, candidates, existing)
    print(f"\nLabels written to {LABELS_OUTPUT}")
    print("Next: eyeball a 200-edge sample, then run with --apply if the error rate is <10%.")


if __name__ == "__main__":
    main()
