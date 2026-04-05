#!/usr/bin/env python3
"""Generate adaptive placement assessment data from the Open Knowledge Graph.

Analyzes topic connectivity and prerequisite chains to select optimal probe
topics for an adaptive assessment. Outputs output/assessment-data.json.

Usage:
    python tools/generate_assessment.py
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
          "formal-systems", "advanced", "expert"]

# Domains preferred for calibration probes (universally encountered)
PREFERRED_CALIBRATION_DOMAINS = ["mathematics", "language-and-communication",
                                  "physics", "biology", "chemistry"]

# Courses that are part of standard K-12 / early-college curricula.
# Topics from these courses are more universally recognizable for calibration.
STANDARD_CURRICULUM_COURSES = {
    "kindergarten", "1st-grade", "2nd-grade", "3rd-grade", "4th-grade",
    "5th-grade", "prealgebra", "algebra-1", "geometry", "algebra-2",
    "precalculus", "calculus-1", "calculus-2", "probability-and-statistics",
    "differential-equations", "linear-algebra",
    "introductory-physics", "mechanics", "general-chemistry-1",
    "general-chemistry-2", "introductory-biology", "cell-biology",
    "general-biology", "world-history", "us-history",
    "modern-physics", "electromagnetism",
}

DOMAIN_PROBES_PER_STAGE = 3
FRONTIER_CHAINS_PER_DOMAIN = 3


# ---------------------------------------------------------------------------
# Loading & graph construction
# ---------------------------------------------------------------------------

from parse_topic import parse_topic as parse_frontmatter


def extract_core_idea(body):
    """Pull the first 1-2 sentences from the ## Core Idea section."""
    match = re.search(r"## Core Idea\s*\n+(.*?)(?=\n## |\Z)", body, re.DOTALL)
    if not match:
        return ""
    text = match.group(1).strip()
    # Replace newlines with spaces to get contiguous text
    text = re.sub(r"\s+", " ", text)
    # Extract first 1-2 sentences
    sentences = re.split(r"(?<=[.!?])\s+", text)
    if len(sentences) >= 2:
        return sentences[0] + " " + sentences[1]
    return sentences[0] if sentences else ""


def load_topics():
    """Load all topic files and return a list of topic dicts."""
    topics = []
    for filepath in sorted(DOMAINS_DIR.rglob("*.md")):
        if filepath.name.startswith("_"):
            continue
        data, body = parse_frontmatter(filepath)
        if data and "id" in data:
            data["_body"] = body
            data["_filepath"] = str(filepath)
            topics.append(data)
    return topics


def build_graph(topics):
    """Build adjacency data structures from topic list.

    Returns:
        topic_map: dict mapping id -> topic dict
        children: dict mapping id -> set of ids that depend on it (forward edges)
        parents:  dict mapping id -> set of ids it depends on (backward edges)
        in_degree:  dict mapping id -> number of topics that list it as prereq
        out_degree: dict mapping id -> number of prereqs it has
    """
    topic_map = {t["id"]: t for t in topics}
    children = defaultdict(set)   # id -> set of ids that have it as prereq
    parents = defaultdict(set)    # id -> set of its prerequisite ids

    for t in topics:
        tid = t["id"]
        prereqs = t.get("prerequisites") or []
        if isinstance(prereqs, list):
            for p in prereqs:
                if isinstance(p, dict) and "id" in p:
                    pid = p["id"]
                    parents[tid].add(pid)
                    children[pid].add(tid)

    # Connectivity = in-degree (how many depend on me) + out-degree (how many I depend on)
    # in_degree = number of children (topics that list me as prereq)
    # out_degree = number of parents (my own prereqs)
    in_degree = {tid: len(children.get(tid, set())) for tid in topic_map}
    out_degree = {tid: len(parents.get(tid, set())) for tid in topic_map}

    return topic_map, children, parents, in_degree, out_degree


def connectivity(tid, in_degree, out_degree):
    """Total connectivity = in-degree + out-degree."""
    return in_degree.get(tid, 0) + out_degree.get(tid, 0)


# ---------------------------------------------------------------------------
# Probe selection
# ---------------------------------------------------------------------------

def topic_entry(t, in_deg, out_deg, include_connectivity=False):
    """Build a JSON-serializable dict for a topic."""
    entry = {
        "id": t["id"],
        "title": t.get("title", t["id"]),
        "stage": t.get("stage", "unknown"),
        "domain": t.get("domain", "unknown"),
        "course": t.get("course", "unknown"),
        "description": extract_core_idea(t.get("_body", "")),
    }
    if include_connectivity:
        entry["connectivity"] = in_deg.get(t["id"], 0) + out_deg.get(t["id"], 0)
    return entry


def select_calibration_probes(topics, topic_map, in_deg, out_deg):
    """Select 5 calibration probes, one per developmental stage.

    Prefers validated, high-connectivity topics from universal domains.
    """
    probes = []
    for stage in STAGES:
        candidates = [t for t in topics if t.get("stage") == stage]
        if not candidates:
            continue

        def score(t):
            """Higher is better. Balances connectivity with universality."""
            conn = connectivity(t["id"], in_deg, out_deg)
            # Bonus for preferred domains
            domain_bonus = 200 if t.get("domain") in PREFERRED_CALIBRATION_DOMAINS else 0
            # Bonus for validated status
            status_bonus = 100 if t.get("status") == "validated" else 0
            # Extra bonus for mathematics (most universal)
            math_bonus = 50 if t.get("domain") == "mathematics" else 0
            # Bonus for standard-curriculum courses (universally recognizable)
            course_bonus = 150 if t.get("course") in STANDARD_CURRICULUM_COURSES else 0
            return conn + domain_bonus + status_bonus + math_bonus + course_bonus

        candidates.sort(key=score, reverse=True)
        best = candidates[0]
        probes.append(topic_entry(best, in_deg, out_deg))

    return probes


def select_domain_probes(topics, topic_map, in_deg, out_deg):
    """Select 2-3 high-connectivity probes per domain per stage level."""
    # Group topics by domain and stage
    domain_stage = defaultdict(list)
    for t in topics:
        domain = t.get("domain", "unknown")
        stage = t.get("stage")
        if stage in STAGES:
            domain_stage[(domain, stage)].append(t)

    result = defaultdict(list)
    for (domain, stage), candidates in sorted(domain_stage.items()):
        candidates.sort(
            key=lambda t: connectivity(t["id"], in_deg, out_deg),
            reverse=True,
        )
        for t in candidates[:DOMAIN_PROBES_PER_STAGE]:
            result[domain].append(topic_entry(t, in_deg, out_deg, include_connectivity=True))

    # Sort each domain's probes by stage order, then by connectivity desc
    stage_order = {s: i for i, s in enumerate(STAGES)}
    for domain in result:
        result[domain].sort(
            key=lambda e: (stage_order.get(e["stage"], 99), -e["connectivity"])
        )

    return dict(result)


# ---------------------------------------------------------------------------
# Frontier chain construction
# ---------------------------------------------------------------------------

def build_longest_chains(topic_map, children, parents, in_deg, out_deg):
    """For each domain, find the 2-3 longest prerequisite chains through hubs.

    Uses topological-order dynamic programming to find longest paths in the DAG,
    then selects chains that pass through high-connectivity nodes.
    """
    # Group topics by domain
    by_domain = defaultdict(set)
    for tid, t in topic_map.items():
        by_domain[t.get("domain", "unknown")].add(tid)

    # Compute topological order via Kahn's algorithm on the full graph
    # (parents = prerequisites, children = dependents)
    all_ids = set(topic_map.keys())
    in_count = {tid: 0 for tid in all_ids}
    for tid in all_ids:
        for pid in parents.get(tid, set()):
            if pid in all_ids:
                in_count[tid] += 1

    queue = [tid for tid in all_ids if in_count[tid] == 0]
    topo_order = []
    while queue:
        # Process in sorted order for determinism
        queue.sort()
        node = queue.pop(0)
        topo_order.append(node)
        for child in children.get(node, set()):
            if child in all_ids:
                in_count[child] -= 1
                if in_count[child] == 0:
                    queue.append(child)

    # DP: longest path ending at each node + backtrack pointer
    dist = {tid: 1 for tid in all_ids}  # length of longest path ending here
    predecessor = {tid: None for tid in all_ids}

    for node in topo_order:
        for child in children.get(node, set()):
            if child not in all_ids:
                continue
            # Weight edges through high-connectivity nodes more
            hub_weight = 1  # base step
            if dist[node] + hub_weight > dist[child]:
                dist[child] = dist[node] + hub_weight
                predecessor[child] = node

    # For each domain, find longest chains
    result = {}
    for domain, domain_ids in sorted(by_domain.items()):
        # Find the terminal nodes (longest paths) within this domain
        # Score each node: path length * hub-quality
        scored = []
        for tid in domain_ids:
            # Only consider nodes that actually have a chain (dist > 1)
            if dist.get(tid, 1) > 1:
                # Prefer chains that end at high-connectivity nodes
                chain_len = dist.get(tid, 1)
                scored.append((chain_len, -connectivity(tid, in_deg, out_deg), tid))

        scored.sort(reverse=True)

        # Extract chains, avoiding too much overlap
        chains = []
        used_nodes = set()
        for _, _, end_node in scored:
            if len(chains) >= FRONTIER_CHAINS_PER_DOMAIN:
                break

            # Reconstruct chain
            chain = []
            node = end_node
            while node is not None:
                chain.append(node)
                node = predecessor.get(node)
            chain.reverse()

            # Only keep chains with at least 3 nodes
            if len(chain) < 3:
                continue

            # Filter chain to domain topics only (prereqs may cross domains)
            domain_chain = [n for n in chain if n in domain_ids]
            if len(domain_chain) < 3:
                continue

            # Avoid chains that heavily overlap with already-selected chains
            overlap = len(set(domain_chain) & used_nodes)
            if overlap > len(domain_chain) * 0.5:
                continue

            used_nodes.update(domain_chain)
            chains.append(domain_chain)

        if chains:
            result[domain] = chains

    return result


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("Loading topics...")
    topics = load_topics()
    if not topics:
        print("No topics found. Check that domains/ directory exists.")
        sys.exit(1)
    print(f"  Loaded {len(topics)} topics")

    print("Building prerequisite graph...")
    topic_map, children, parents, in_deg, out_deg = build_graph(topics)
    total_edges = sum(len(v) for v in parents.values())
    print(f"  {total_edges} prerequisite edges")

    print("\nSelecting calibration probes (1 per stage)...")
    calibration = select_calibration_probes(topics, topic_map, in_deg, out_deg)
    for p in calibration:
        print(f"  [{p['stage']}] {p['title']} ({p['domain']}/{p['course']})")

    print("\nSelecting domain probes...")
    domain_probes = select_domain_probes(topics, topic_map, in_deg, out_deg)
    total_domain_probes = sum(len(v) for v in domain_probes.values())
    print(f"  {total_domain_probes} probes across {len(domain_probes)} domains")
    for domain, probes in sorted(domain_probes.items()):
        stages_present = sorted(set(p["stage"] for p in probes),
                                key=lambda s: STAGES.index(s) if s in STAGES else 99)
        print(f"  {domain}: {len(probes)} probes ({', '.join(stages_present)})")

    print("\nBuilding frontier chains...")
    frontier_chains = build_longest_chains(topic_map, children, parents, in_deg, out_deg)
    total_chains = sum(len(v) for v in frontier_chains.values())
    print(f"  {total_chains} chains across {len(frontier_chains)} domains")
    for domain, chains in sorted(frontier_chains.items()):
        lengths = [len(c) for c in chains]
        print(f"  {domain}: {len(chains)} chains (lengths: {', '.join(str(l) for l in lengths)})")

    # Assemble output
    output = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "total_topics": len(topics),
        "calibration": calibration,
        "domain_probes": domain_probes,
        "frontier_chains": frontier_chains,
    }

    # Write output
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / "assessment-data.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nWrote {out_path.relative_to(ROOT)}")
    print(f"\nSummary:")
    print(f"  Calibration probes:  {len(calibration)}")
    print(f"  Domain probes:       {total_domain_probes} across {len(domain_probes)} domains")
    print(f"  Frontier chains:     {total_chains} across {len(frontier_chains)} domains")


if __name__ == "__main__":
    main()
