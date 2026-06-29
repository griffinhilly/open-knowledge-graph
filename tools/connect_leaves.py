#!/usr/bin/env python3
"""Find leaf topics (0 successors) and propose missing prerequisite edges.

For each leaf topic, searches for candidate successors in the same course
and domain using tag overlap, title keyword similarity, and stage progression.
Proposes high-confidence connections and optionally applies them.

Usage:
    python tools/connect_leaves.py --domains social-sciences philosophy
    python tools/connect_leaves.py --domains social-sciences --apply --min-score 0.35
    python tools/connect_leaves.py --all --dry-run
"""

import argparse
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

STAGES_ORDER = ["pre-formal", "concrete-operations", "abstract-reasoning",
                "formal-systems", "advanced", "expert"]
STAGE_IDX = {s: i for i, s in enumerate(STAGES_ORDER)}

# Words to ignore in title similarity
STOPWORDS = {"and", "of", "the", "in", "a", "an", "to", "for", "on", "with",
             "its", "as", "by", "is", "vs", "from", "or", "at", "into"}


def parse_all_topics():
    """Parse all topic files, return dict of id -> {data, filepath}."""
    topics = {}
    for f in sorted(DOMAINS_DIR.rglob("*.md")):
        text = f.read_text(encoding="utf-8")
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
        if not match:
            continue
        try:
            data = yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            continue
        if not isinstance(data, dict):
            continue
        tid = data.get("id")
        if not tid:
            continue
        if data.get("kind") == "capacity":
            continue  # origin layer: never treat capacities as leaves to connect (cycle risk)
        topics[tid] = {"data": data, "filepath": f}
    return topics


def build_successor_counts(topics):
    """Count how many topics list each topic as a prerequisite."""
    counts = defaultdict(int)
    for tid, info in topics.items():
        prereqs = info["data"].get("prerequisites", [])
        if isinstance(prereqs, list):
            for p in prereqs:
                if isinstance(p, dict) and p.get("id"):
                    counts[p["id"]] += 1
    return counts


def title_words(title):
    """Extract meaningful words from a title."""
    words = set(re.findall(r"[a-z]+", title.lower()))
    return words - STOPWORDS


def score_candidate(leaf_data, cand_data):
    """Score a candidate successor for a leaf topic. Returns (score, reasons)."""
    reasons = []

    # Tag overlap (Jaccard)
    leaf_tags = set(leaf_data.get("tags", []))
    cand_tags = set(cand_data.get("tags", []))
    if leaf_tags and cand_tags:
        tag_jaccard = len(leaf_tags & cand_tags) / len(leaf_tags | cand_tags)
        tag_overlap_count = len(leaf_tags & cand_tags)
    else:
        tag_jaccard = 0.0
        tag_overlap_count = 0

    # Title word overlap (Jaccard)
    leaf_words = title_words(leaf_data.get("title", ""))
    cand_words = title_words(cand_data.get("title", ""))
    if leaf_words and cand_words:
        title_jaccard = len(leaf_words & cand_words) / len(leaf_words | cand_words)
    else:
        title_jaccard = 0.0

    # Same course bonus
    same_course = leaf_data.get("course") == cand_data.get("course")

    # Stage progression
    leaf_stage = STAGE_IDX.get(leaf_data.get("stage", ""), 0)
    cand_stage = STAGE_IDX.get(cand_data.get("stage", ""), 0)
    # Candidate should be at same or later stage
    if cand_stage < leaf_stage:
        return 0.0, []  # Wrong direction

    # Composite score
    score = (
        0.40 * tag_jaccard +
        0.25 * title_jaccard +
        0.25 * (1.0 if same_course else 0.0) +
        0.10 * min((cand_stage - leaf_stage) / 2.0, 1.0)  # slight bonus for 1-2 stage gap
    )

    if score > 0:
        reasons.append(f"tags:{tag_overlap_count}/{len(leaf_tags | cand_tags)}")
        reasons.append(f"title:{title_jaccard:.2f}")
        if same_course:
            reasons.append("same-course")
        if cand_stage > leaf_stage:
            reasons.append(f"stage:+{cand_stage - leaf_stage}")

    return score, reasons


def find_proposals(topics, successor_counts, target_domains, min_score=0.30, max_per_leaf=2):
    """Find proposed connections for leaf topics in target domains."""
    proposals = []

    # Index: existing prerequisites for quick lookup
    existing_prereqs = defaultdict(set)
    for tid, info in topics.items():
        prereqs = info["data"].get("prerequisites", [])
        if isinstance(prereqs, list):
            for p in prereqs:
                if isinstance(p, dict) and p.get("id"):
                    existing_prereqs[tid].add(p["id"])

    # Find leaves in target domains
    leaves = []
    for tid, info in topics.items():
        domain = info["data"].get("domain", "")
        if domain in target_domains and successor_counts.get(tid, 0) == 0:
            leaves.append(tid)

    print(f"  Found {len(leaves)} leaf topics in target domains\n")

    for leaf_id in sorted(leaves):
        leaf_info = topics[leaf_id]
        leaf_data = leaf_info["data"]
        leaf_domain = leaf_data.get("domain", "")

        # Search candidates: same domain only (cross-domain is Phase 2)
        candidates = []
        for cand_id, cand_info in topics.items():
            if cand_id == leaf_id:
                continue
            cand_data = cand_info["data"]
            # Same domain only
            if cand_data.get("domain", "") != leaf_domain:
                continue
            # Skip if already connected in either direction
            if leaf_id in existing_prereqs[cand_id]:
                continue
            if cand_id in existing_prereqs[leaf_id]:
                continue

            score, reasons = score_candidate(leaf_data, cand_data)
            if score >= min_score:
                candidates.append((score, cand_id, reasons))

        # Take top N candidates
        candidates.sort(reverse=True)
        for score, cand_id, reasons in candidates[:max_per_leaf]:
            proposals.append({
                "leaf_id": leaf_id,
                "leaf_course": leaf_data.get("course", ""),
                "successor_id": cand_id,
                "successor_course": topics[cand_id]["data"].get("course", ""),
                "score": score,
                "reasons": reasons,
                "domain": leaf_domain,
            })

    return proposals


def would_create_cycle(graph, from_id, to_id):
    """Check if adding edge from_id → to_id (to_id lists from_id as prereq) creates a cycle.

    A cycle exists if there's already a path from from_id to to_id in the prereq graph
    (i.e., from_id transitively depends on to_id). Adding to_id → from_id would then close the loop.
    """
    # BFS: can we reach to_id starting from from_id's existing prereqs?
    # If from_id transitively depends on to_id, adding to_id→from_id closes a cycle.
    visited = set()
    queue = list(graph.get(from_id, []))
    while queue:
        node = queue.pop(0)
        if node == to_id:
            return True
        if node not in visited:
            visited.add(node)
            queue.extend(graph.get(node, []))
    return False


def apply_proposals(proposals, topics):
    """Apply proposals by adding leaf as prerequisite to successor's file.
    Skips proposals that would introduce cycles."""
    # Build current prereq graph
    graph = defaultdict(list)
    for tid, info in topics.items():
        prereqs = info["data"].get("prerequisites", [])
        if isinstance(prereqs, list):
            for p in prereqs:
                if isinstance(p, dict) and p.get("id"):
                    graph[tid].append(p["id"])

    applied = 0
    skipped_cycles = 0
    for prop in proposals:
        succ_id = prop["successor_id"]
        leaf_id = prop["leaf_id"]
        filepath = topics[succ_id]["filepath"]

        text = filepath.read_text(encoding="utf-8")
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
        if not match:
            continue

        fm_text = match.group(1)
        data = yaml.safe_load(fm_text)
        if not isinstance(data, dict):
            continue

        # Add leaf as soft prerequisite
        prereqs = data.get("prerequisites", [])
        if not isinstance(prereqs, list):
            continue

        # Double-check not already present
        existing_ids = {p.get("id") for p in prereqs if isinstance(p, dict)}
        if leaf_id in existing_ids:
            continue

        # Check if this edge would create a cycle
        if would_create_cycle(graph, leaf_id, succ_id):
            skipped_cycles += 1
            continue

        prereqs.append({"id": leaf_id, "type": "soft"})
        data["prerequisites"] = prereqs

        # Update graph for subsequent checks
        graph[succ_id].append(leaf_id)

        # Rewrite frontmatter
        new_fm = yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)
        body = text[match.end():]
        new_text = f"---\n{new_fm}---\n{body}"
        filepath.write_text(new_text, encoding="utf-8")
        applied += 1

    if skipped_cycles:
        print(f"  Skipped {skipped_cycles} proposals that would create cycles")
    return applied


def find_cycles(topics):
    """Quick cycle detection on current prerequisite graph."""
    graph = defaultdict(list)
    for tid, info in topics.items():
        prereqs = info["data"].get("prerequisites", [])
        if isinstance(prereqs, list):
            for p in prereqs:
                if isinstance(p, dict) and p.get("id"):
                    graph[tid].append(p["id"])

    WHITE, GRAY, BLACK = 0, 1, 2
    color = defaultdict(int)
    cycles = []

    def dfs(node, path):
        color[node] = GRAY
        for neighbor in graph.get(node, []):
            if color[neighbor] == GRAY:
                idx = path.index(neighbor) if neighbor in path else -1
                if idx >= 0:
                    cycles.append(path[idx:] + [neighbor])
            elif color[neighbor] == WHITE:
                dfs(neighbor, path + [neighbor])
        color[node] = BLACK

    for node in graph:
        if color[node] == WHITE:
            dfs(node, [node])

    return cycles


def main():
    parser = argparse.ArgumentParser(description="Connect leaf topics with missing edges")
    parser.add_argument("--domains", nargs="+", help="Target domains (default: 5 worst)")
    parser.add_argument("--all", action="store_true", help="Target all domains")
    parser.add_argument("--apply", action="store_true", help="Apply proposals (default: dry-run)")
    parser.add_argument("--min-score", type=float, default=0.30, help="Minimum score threshold")
    parser.add_argument("--max-per-leaf", type=int, default=2, help="Max connections per leaf")
    args = parser.parse_args()

    if args.all:
        target_domains = None  # all
    elif args.domains:
        target_domains = set(args.domains)
    else:
        target_domains = {
            "social-sciences", "health-and-human-development",
            "philosophy", "literature", "practical-life-skills"
        }

    print("Parsing all topics...")
    topics = parse_all_topics()
    print(f"  {len(topics)} topics loaded\n")

    print("Building successor counts...")
    successor_counts = build_successor_counts(topics)

    all_domains = {info["data"].get("domain", "") for info in topics.values()}
    if target_domains is None:
        target_domains = all_domains

    print(f"Finding proposals for {len(target_domains)} domains "
          f"(min_score={args.min_score}, max_per_leaf={args.max_per_leaf})...")
    proposals = find_proposals(topics, successor_counts, target_domains,
                               min_score=args.min_score, max_per_leaf=args.max_per_leaf)

    if not proposals:
        print("\nNo proposals found above threshold.")
        return 0

    # Deduplicate symmetric pairs: if A→B and B→A both proposed, keep one direction
    seen_pairs = {}
    deduped = []
    symmetric_count = 0
    for p in proposals:
        pair = tuple(sorted([p["leaf_id"], p["successor_id"]]))
        if pair in seen_pairs:
            symmetric_count += 1
            # Keep the one where leaf stage <= successor stage (correct direction)
            existing = seen_pairs[pair]
            existing_leaf_stage = STAGE_IDX.get(topics[existing["leaf_id"]]["data"].get("stage", ""), 0)
            existing_succ_stage = STAGE_IDX.get(topics[existing["successor_id"]]["data"].get("stage", ""), 0)
            new_leaf_stage = STAGE_IDX.get(topics[p["leaf_id"]]["data"].get("stage", ""), 0)
            new_succ_stage = STAGE_IDX.get(topics[p["successor_id"]]["data"].get("stage", ""), 0)
            # Prefer larger stage gap (leaf earlier, successor later)
            if (new_succ_stage - new_leaf_stage) > (existing_succ_stage - existing_leaf_stage):
                seen_pairs[pair] = p
        else:
            seen_pairs[pair] = p

    deduped = list(seen_pairs.values())

    # Flag potential duplicates (very high similarity)
    potential_dupes = []
    connections = []
    for p in deduped:
        leaf_words = title_words(topics[p["leaf_id"]]["data"].get("title", ""))
        succ_words = title_words(topics[p["successor_id"]]["data"].get("title", ""))
        title_sim = len(leaf_words & succ_words) / len(leaf_words | succ_words) if (leaf_words | succ_words) else 0
        if title_sim >= 0.75 or (p["score"] >= 0.55 and title_sim >= 0.50):
            potential_dupes.append(p)
        else:
            connections.append(p)

    if symmetric_count:
        print(f"  Removed {symmetric_count} symmetric pairs")
    if potential_dupes:
        print(f"  Flagged {len(potential_dupes)} potential duplicates (score≥0.65, title_sim≥0.60)")

    proposals = connections

    # Report potential duplicates
    if potential_dupes:
        print(f"\n{'='*70}")
        print(f"POTENTIAL DUPLICATES ({len(potential_dupes)}) — review for dedup, not connection:\n")
        potential_dupes.sort(key=lambda p: p["score"], reverse=True)
        for p in potential_dupes[:30]:
            print(f"  {p['score']:.3f}  {p['leaf_id'][:42]} ↔ {p['successor_id'][:42]}")

    # Summary by domain
    domain_counts = defaultdict(int)
    domain_scores = defaultdict(list)
    for p in proposals:
        domain_counts[p["domain"]] += 1
        domain_scores[p["domain"]].append(p["score"])

    print(f"\n{'='*70}")
    print(f"PROPOSALS: {len(proposals)} connections across {len(domain_counts)} domains\n")
    for domain in sorted(domain_counts.keys()):
        scores = domain_scores[domain]
        avg = sum(scores) / len(scores)
        print(f"  {domain}: {domain_counts[domain]} proposals (avg score: {avg:.3f})")
    print()

    # Show top proposals
    proposals.sort(key=lambda p: p["score"], reverse=True)
    print(f"Top 20 proposals:")
    print(f"  {'Score':>5}  {'Leaf':40} → {'Successor':40}  Reasons")
    print(f"  {'-'*5}  {'-'*40}   {'-'*40}  {'-'*30}")
    for p in proposals[:20]:
        reasons = ", ".join(p["reasons"])
        print(f"  {p['score']:.3f}  {p['leaf_id'][:40]:40} → {p['successor_id'][:40]:40}  {reasons}")
    print()

    # Score distribution
    high = sum(1 for p in proposals if p["score"] >= 0.50)
    medium = sum(1 for p in proposals if 0.35 <= p["score"] < 0.50)
    low = sum(1 for p in proposals if p["score"] < 0.35)
    print(f"Score distribution: {high} high (≥0.50), {medium} medium (0.35-0.50), {low} low (<0.35)")

    if not args.apply:
        print(f"\nDry run complete. Use --apply to write changes.")
        print(f"Suggested: --apply --min-score 0.35  ({high + medium} proposals)")
        return 0

    # Apply
    print(f"\nApplying {len(proposals)} proposals...")
    applied = apply_proposals(proposals, topics)
    print(f"  {applied} files modified\n")

    # Re-parse and check for cycles
    print("Checking for introduced cycles...")
    topics = parse_all_topics()
    cycles = find_cycles(topics)
    if cycles:
        print(f"  WARNING: {len(cycles)} cycles detected!")
        for c in cycles[:5]:
            print(f"    {' -> '.join(c)}")
        print("  Run validate.py and fix before committing.")
        return 1
    else:
        print("  No cycles introduced.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
