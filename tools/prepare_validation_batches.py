#!/usr/bin/env python3
"""Prepare validation batches for Haiku agent review.

Extracts all draft topics into 50 JSON batch files, grouped by domain,
so each Haiku agent can validate ~220 topics without file I/O.
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required.")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "domains"
OUTPUT_DIR = ROOT / "tools" / "validation"
NUM_BATCHES = 50


def parse_topic(filepath):
    """Extract structured data from a topic file."""
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return None

    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None

    if not isinstance(data, dict):
        return None

    body = text[match.end():]

    # Extract sections
    sections = {}
    current_section = None
    current_lines = []

    for line in body.splitlines():
        if line.startswith("## "):
            if current_section:
                sections[current_section] = "\n".join(current_lines).strip()
            current_section = line[3:].strip()
            current_lines = []
        elif current_section:
            current_lines.append(line)

    if current_section:
        sections[current_section] = "\n".join(current_lines).strip()

    # Word count (excluding markdown headers and blank lines)
    body_lines = [l for l in body.strip().splitlines()
                  if l.strip() and not l.strip().startswith("#")]
    word_count = sum(len(l.split()) for l in body_lines)

    prereqs = data.get("prerequisites", [])
    prereq_list = []
    for p in prereqs:
        if isinstance(p, dict):
            prereq_list.append({"id": p.get("id", ""), "type": p.get("type", "hard")})
        elif isinstance(p, str):
            prereq_list.append({"id": p, "type": "hard"})

    return {
        "id": data.get("id", ""),
        "title": data.get("title", ""),
        "domain": data.get("domain", ""),
        "course": data.get("course", ""),
        "stage": data.get("stage", ""),
        "status": data.get("status", ""),
        "tags": data.get("tags", []),
        "prerequisites": prereq_list,
        "builds_toward": data.get("builds-toward", []),
        "core_idea": sections.get("Core Idea", ""),
        "how_best_learned": sections.get("How It's Best Learned", ""),
        "common_misconceptions": sections.get("Common Misconceptions", ""),
        "body_word_count": word_count,
        "has_explainer": "Explainer" in sections,
        "has_questions": "Questions" in sections,
    }


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Load all draft topics grouped by domain
    by_domain = defaultdict(list)
    total = 0
    skipped = 0

    for md_file in sorted(DOMAINS_DIR.rglob("*.md")):
        if md_file.name.startswith("_"):
            continue
        topic = parse_topic(md_file)
        if not topic:
            skipped += 1
            continue
        if topic["status"] != "draft":
            continue
        by_domain[topic["domain"]].append(topic)
        total += 1

    print(f"Loaded {total} draft topics across {len(by_domain)} domains ({skipped} skipped)")

    # Sort domains by topic count (descending) for balanced distribution
    domain_order = sorted(by_domain.keys(), key=lambda d: len(by_domain[d]), reverse=True)

    # Distribute topics into batches, keeping domains together where possible
    batches = [[] for _ in range(NUM_BATCHES)]
    batch_domains = [set() for _ in range(NUM_BATCHES)]

    for domain in domain_order:
        topics = by_domain[domain]

        if len(topics) <= (total // NUM_BATCHES) * 1.5:
            # Small enough to fit in one or two batches — find the emptiest
            min_idx = min(range(NUM_BATCHES), key=lambda i: len(batches[i]))
            batches[min_idx].extend(topics)
            batch_domains[min_idx].add(domain)
        else:
            # Large domain — distribute evenly across emptiest batches
            chunk_size = max(1, len(topics) // 3)
            chunks = [topics[i:i + chunk_size] for i in range(0, len(topics), chunk_size)]
            for chunk in chunks:
                min_idx = min(range(NUM_BATCHES), key=lambda i: len(batches[i]))
                batches[min_idx].extend(chunk)
                batch_domains[min_idx].add(domain)

    # Write batch files
    for i, (batch, domains) in enumerate(zip(batches, batch_domains)):
        if not batch:
            continue

        batch_data = {
            "batch_number": i + 1,
            "total_batches": NUM_BATCHES,
            "topic_count": len(batch),
            "domains": sorted(domains),
            "domain_summary": ", ".join(
                f"{d} ({sum(1 for t in batch if t['domain'] == d)})"
                for d in sorted(domains)
            ),
            "topics": batch,
        }

        out_path = OUTPUT_DIR / f"batch-{i+1:02d}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(batch_data, f, indent=2, ensure_ascii=False)

    # Summary
    non_empty = [b for b in batches if b]
    sizes = [len(b) for b in non_empty]
    print(f"\nWrote {len(non_empty)} batch files to {OUTPUT_DIR}")
    print(f"Batch sizes: min={min(sizes)}, max={max(sizes)}, avg={sum(sizes)/len(sizes):.0f}")

    # Domain distribution summary
    print("\nDomain distribution:")
    for domain in domain_order:
        count = len(by_domain[domain])
        batch_nums = [i + 1 for i, b in enumerate(batches) if any(t["domain"] == domain for t in b)]
        print(f"  {domain}: {count} topics across batches {batch_nums}")


if __name__ == "__main__":
    main()
