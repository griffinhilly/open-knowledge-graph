#!/usr/bin/env python3
"""QA analysis for the Open Knowledge Graph.

Produces a prioritized report of items needing human review:
1. Hub report — most-depended-on and most-dependent topics
2. Longest prerequisite chains per domain
3. Weakly-connected components (islands)
4. Thin courses (below topic threshold)
5. Shallow content (missing or very short body text)
6. Bidirectional pair summary (from builds-toward mismatches)

Usage:
    python tools/qa_analyze.py                # Full report to stdout
    python tools/qa_analyze.py --json         # JSON output to tools/qa_report.json
    python tools/qa_analyze.py --domain math  # Filter to one domain (substring match)
"""

import sys
import io
import re
import json
import argparse

# Force UTF-8 output on Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")
from pathlib import Path
from collections import defaultdict

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install with: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "domains"

THIN_COURSE_THRESHOLD = 20
SHALLOW_BODY_THRESHOLD = 50  # words


def parse_frontmatter(filepath):
    """Extract YAML frontmatter from a Markdown file."""
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return None, ""
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None, ""
    body = text[match.end():]
    return data, body


def word_count(text):
    """Count words in text, ignoring markdown headers and blank lines."""
    lines = [l for l in text.strip().splitlines()
             if l.strip() and not l.strip().startswith("#")]
    return len(" ".join(lines).split())


def load_all_topics(domain_filter=None):
    """Parse every topic file. Returns (all_data, all_bodies) dicts keyed by topic ID."""
    all_data = {}
    all_bodies = {}
    for filepath in sorted(DOMAINS_DIR.rglob("*.md")):
        data, body = parse_frontmatter(filepath)
        if data is None or "id" not in data:
            continue
        if domain_filter and domain_filter not in data.get("domain", ""):
            continue
        tid = data["id"]
        data["_filepath"] = str(filepath.relative_to(ROOT))
        all_data[tid] = data
        all_bodies[tid] = body
    return all_data, all_bodies


def build_graphs(all_data):
    """Build prerequisite graph (topic -> its prereqs) and reverse graph (topic -> what depends on it)."""
    prereq_of = defaultdict(list)    # topic_id -> [prereq_ids]
    depended_by = defaultdict(list)  # topic_id -> [topics that list it as prereq]
    for tid, data in all_data.items():
        for p in data.get("prerequisites", []):
            if isinstance(p, dict) and "id" in p:
                pid = p["id"]
                prereq_of[tid].append(pid)
                depended_by[pid].append(tid)
    return prereq_of, depended_by


# --- Analysis functions ---

def hub_report(all_data, depended_by, prereq_of, top_n=20):
    """Find the most-connected topics (highest in-degree and out-degree)."""
    in_degree = []   # topics most depended on
    out_degree = []  # topics with most prerequisites

    for tid, data in all_data.items():
        in_degree.append({
            "id": tid,
            "title": data.get("title", ""),
            "domain": data.get("domain", ""),
            "course": data.get("course", ""),
            "in_degree": len(depended_by.get(tid, [])),
        })
        out_degree.append({
            "id": tid,
            "title": data.get("title", ""),
            "domain": data.get("domain", ""),
            "course": data.get("course", ""),
            "out_degree": len(prereq_of.get(tid, [])),
        })

    in_degree.sort(key=lambda x: x["in_degree"], reverse=True)
    out_degree.sort(key=lambda x: x["out_degree"], reverse=True)

    return {
        "most_depended_on": in_degree[:top_n],
        "most_prerequisites": out_degree[:top_n],
    }


def longest_chains(all_data, prereq_of, per_domain=5):
    """Find the longest prerequisite chains per domain.

    Uses iterative DFS to find the longest path ending at each topic.
    Returns the top chains per domain.
    """
    # Compute depth (longest path from any root) for each topic via topological ordering
    depth = {}
    parent_on_longest = {}

    # Kahn's algorithm for topological sort
    in_count = defaultdict(int)
    all_ids = set(all_data.keys())
    for tid in all_ids:
        for pid in prereq_of.get(tid, []):
            if pid in all_ids:
                in_count[tid] += 1

    queue = [tid for tid in all_ids if in_count[tid] == 0]
    for tid in queue:
        depth[tid] = 0
        parent_on_longest[tid] = None

    topo_order = []
    while queue:
        node = queue.pop(0)
        topo_order.append(node)
        # Find topics that list `node` as a prerequisite (node's dependents)
        for tid in all_ids:
            if node in prereq_of.get(tid, []):
                if depth.get(node, 0) + 1 > depth.get(tid, 0):
                    depth[tid] = depth[node] + 1
                    parent_on_longest[tid] = node
                in_count[tid] -= 1
                if in_count[tid] == 0:
                    queue.append(tid)

    # Reconstruct chains for deepest topics per domain
    by_domain = defaultdict(list)
    for tid in all_ids:
        if tid in depth:
            domain = all_data[tid].get("domain", "unknown")
            by_domain[domain].append((depth[tid], tid))

    result = {}
    for domain, items in sorted(by_domain.items()):
        items.sort(key=lambda x: x[0], reverse=True)
        chains = []
        for chain_depth, tid in items[:per_domain]:
            chain = []
            current = tid
            while current is not None:
                chain.append({
                    "id": current,
                    "title": all_data[current].get("title", ""),
                    "course": all_data[current].get("course", ""),
                })
                current = parent_on_longest.get(current)
            chain.reverse()
            chains.append({
                "depth": chain_depth,
                "endpoint": tid,
                "chain": chain,
            })
        result[domain] = chains

    return result


def find_islands(all_data, prereq_of):
    """Find weakly-connected components. Multiple components in a domain = potential linking gaps."""
    # Build undirected adjacency
    adj = defaultdict(set)
    all_ids = set(all_data.keys())
    for tid in all_ids:
        for pid in prereq_of.get(tid, []):
            if pid in all_ids:
                adj[tid].add(pid)
                adj[pid].add(tid)

    visited = set()
    components = []

    for start in all_ids:
        if start in visited:
            continue
        # BFS
        component = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            component.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
        components.append(component)

    # Group by domain
    domain_components = defaultdict(list)
    for comp in components:
        domains_in_comp = set(all_data[tid].get("domain", "unknown") for tid in comp)
        # Assign to primary domain (most topics)
        domain_counts = defaultdict(int)
        for tid in comp:
            domain_counts[all_data[tid].get("domain", "unknown")] += 1
        primary = max(domain_counts, key=domain_counts.get)
        domain_components[primary].append({
            "size": len(comp),
            "domains": sorted(domains_in_comp),
            "sample_topics": sorted(list(comp))[:5],
        })

    # Flag domains with multiple components
    flagged = {}
    for domain, comps in sorted(domain_components.items()):
        if len(comps) > 1:
            comps.sort(key=lambda x: x["size"], reverse=True)
            flagged[domain] = {
                "component_count": len(comps),
                "components": comps,
            }

    return flagged


def thin_courses(all_data, threshold=THIN_COURSE_THRESHOLD):
    """Find courses with fewer topics than the threshold."""
    course_topics = defaultdict(list)
    for tid, data in all_data.items():
        key = f"{data.get('domain', '?')}/{data.get('course', '?')}"
        course_topics[key].append(tid)

    thin = []
    for course, topics in sorted(course_topics.items()):
        if len(topics) < threshold:
            thin.append({
                "course": course,
                "count": len(topics),
                "topics": sorted(topics),
            })
    thin.sort(key=lambda x: x["count"])
    return thin


def shallow_content(all_data, all_bodies, threshold=SHALLOW_BODY_THRESHOLD):
    """Find topics with missing or very short body text."""
    shallow = []
    for tid, body in all_bodies.items():
        wc = word_count(body)
        if wc < threshold:
            data = all_data[tid]
            has_core_idea = "## Core Idea" in body or "## core idea" in body.lower()
            shallow.append({
                "id": tid,
                "title": data.get("title", ""),
                "domain": data.get("domain", ""),
                "course": data.get("course", ""),
                "word_count": wc,
                "has_core_idea": has_core_idea,
                "filepath": data.get("_filepath", ""),
            })
    shallow.sort(key=lambda x: x["word_count"])
    return shallow


def bidirectional_pairs(all_data):
    """Find topics where A builds-toward B AND B builds-toward A."""
    pairs = []
    seen = set()
    for tid, data in all_data.items():
        for target in data.get("builds-toward", []):
            if not isinstance(target, str) or target not in all_data:
                continue
            target_data = all_data[target]
            target_builds = target_data.get("builds-toward", [])
            if tid in target_builds:
                key = tuple(sorted([tid, target]))
                if key not in seen:
                    seen.add(key)
                    pairs.append({
                        "topic_a": {
                            "id": tid,
                            "title": data.get("title", ""),
                            "domain": data.get("domain", ""),
                            "course": data.get("course", ""),
                        },
                        "topic_b": {
                            "id": target,
                            "title": target_data.get("title", ""),
                            "domain": target_data.get("domain", ""),
                            "course": target_data.get("course", ""),
                        },
                    })
    return pairs


def orphan_topics(all_data, prereq_of, depended_by):
    """Topics with no prerequisites AND nothing depends on them (true isolates)."""
    orphans = []
    for tid, data in all_data.items():
        has_prereqs = len(prereq_of.get(tid, [])) > 0
        is_depended = len(depended_by.get(tid, [])) > 0
        if not has_prereqs and not is_depended:
            orphans.append({
                "id": tid,
                "title": data.get("title", ""),
                "domain": data.get("domain", ""),
                "course": data.get("course", ""),
            })
    return orphans


# --- Output ---

def print_report(report):
    """Pretty-print the QA report to stdout."""
    print("=" * 70)
    print("  OPEN KNOWLEDGE GRAPH — QA ANALYSIS REPORT")
    print("=" * 70)

    total = report["summary"]["total_topics"]
    print(f"\n  {total} topics across {report['summary']['domain_count']} domains, "
          f"{report['summary']['edge_count']} edges\n")

    # Hubs
    print("-" * 70)
    print("  1. HUB TOPICS (most load-bearing nodes)")
    print("-" * 70)
    print("\n  Most depended-on (highest in-degree):")
    for i, h in enumerate(report["hubs"]["most_depended_on"][:15], 1):
        print(f"    {i:2}. [{h['in_degree']:3} dependents] {h['id']}")
        print(f"        {h['title']} ({h['domain']}/{h['course']})")

    print("\n  Most prerequisites (highest out-degree):")
    for i, h in enumerate(report["hubs"]["most_prerequisites"][:15], 1):
        print(f"    {i:2}. [{h['out_degree']:3} prereqs] {h['id']}")
        print(f"        {h['title']} ({h['domain']}/{h['course']})")

    # Longest chains
    print("\n" + "-" * 70)
    print("  2. LONGEST PREREQUISITE CHAINS (per domain)")
    print("-" * 70)
    for domain, chains in sorted(report["longest_chains"].items()):
        print(f"\n  {domain} (longest chain: {chains[0]['depth']} steps)")
        for c in chains[:3]:
            steps = " → ".join(t["id"] for t in c["chain"])
            # Wrap long chains
            if len(steps) > 100:
                ids = [t["id"] for t in c["chain"]]
                print(f"    [{c['depth']} steps] {ids[0]}")
                for step_id in ids[1:]:
                    print(f"      → {step_id}")
            else:
                print(f"    [{c['depth']} steps] {steps}")

    # Islands
    print("\n" + "-" * 70)
    print("  3. DISCONNECTED COMPONENTS (islands needing links)")
    print("-" * 70)
    islands = report["islands"]
    if not islands:
        print("\n  No disconnected components found — graph is fully connected!")
    else:
        for domain, info in sorted(islands.items()):
            print(f"\n  {domain}: {info['component_count']} components")
            for i, comp in enumerate(info["components"], 1):
                print(f"    Component {i}: {comp['size']} topics "
                      f"(e.g., {', '.join(comp['sample_topics'][:3])})")

    # Orphans
    print("\n" + "-" * 70)
    print("  4. ORPHAN TOPICS (no prereqs AND nothing depends on them)")
    print("-" * 70)
    orphans = report["orphans"]
    if not orphans:
        print("\n  No orphan topics found.")
    else:
        print(f"\n  {len(orphans)} orphan topics:")
        for o in orphans[:20]:
            print(f"    - {o['id']} ({o['domain']}/{o['course']})")
        if len(orphans) > 20:
            print(f"    ... and {len(orphans) - 20} more")

    # Thin courses
    print("\n" + "-" * 70)
    print(f"  5. THIN COURSES (fewer than {THIN_COURSE_THRESHOLD} topics)")
    print("-" * 70)
    thin = report["thin_courses"]
    if not thin:
        print(f"\n  All courses have {THIN_COURSE_THRESHOLD}+ topics.")
    else:
        print(f"\n  {len(thin)} courses below threshold:")
        for t in thin:
            print(f"    {t['count']:3} topics  {t['course']}")

    # Shallow content
    print("\n" + "-" * 70)
    print(f"  6. SHALLOW CONTENT (body under {SHALLOW_BODY_THRESHOLD} words)")
    print("-" * 70)
    shallow = report["shallow_content"]
    if not shallow:
        print(f"\n  All topics have {SHALLOW_BODY_THRESHOLD}+ words of body content.")
    else:
        print(f"\n  {len(shallow)} topics with thin content:")
        for s in shallow[:20]:
            core = "✓" if s["has_core_idea"] else "✗"
            print(f"    {s['word_count']:3} words  [Core Idea: {core}]  {s['id']} ({s['domain']}/{s['course']})")
        if len(shallow) > 20:
            print(f"    ... and {len(shallow) - 20} more (see --json for full list)")

    # Bidirectional pairs
    print("\n" + "-" * 70)
    print("  7. BIDIRECTIONAL PAIRS (A builds-toward B AND B builds-toward A)")
    print("-" * 70)
    pairs = report["bidirectional_pairs"]
    if not pairs:
        print("\n  No bidirectional pairs found.")
    else:
        print(f"\n  {len(pairs)} pairs to review:")
        for p in pairs[:20]:
            a, b = p["topic_a"], p["topic_b"]
            print(f"    {a['id']}  ↔  {b['id']}")
            print(f"      {a['title']} ({a['course']})  ↔  {b['title']} ({b['course']})")
        if len(pairs) > 20:
            print(f"    ... and {len(pairs) - 20} more (see --json for full list)")

    # Summary
    print("\n" + "=" * 70)
    print("  SUMMARY")
    print("=" * 70)
    issues = (len(report.get("orphans", []))
              + len(report.get("thin_courses", []))
              + len(report.get("shallow_content", []))
              + len(report.get("bidirectional_pairs", []))
              + sum(info["component_count"] - 1 for info in report.get("islands", {}).values()))
    print(f"\n  Total items flagged for review: {issues}")
    print(f"    Orphan topics:       {len(report.get('orphans', []))}")
    print(f"    Thin courses:        {len(report.get('thin_courses', []))}")
    print(f"    Shallow content:     {len(report.get('shallow_content', []))}")
    print(f"    Bidirectional pairs: {len(report.get('bidirectional_pairs', []))}")
    island_gaps = sum(info["component_count"] - 1 for info in report.get("islands", {}).values())
    print(f"    Island gaps:         {island_gaps}")
    print()


def main():
    parser = argparse.ArgumentParser(description="QA analysis for Open Knowledge Graph")
    parser.add_argument("--json", action="store_true", help="Output JSON to tools/qa_report.json")
    parser.add_argument("--domain", type=str, default=None, help="Filter to domain (substring match)")
    args = parser.parse_args()

    print("Loading topics...", file=sys.stderr)
    all_data, all_bodies = load_all_topics(domain_filter=args.domain)
    if not all_data:
        print("No topics found.", file=sys.stderr)
        return

    print(f"Loaded {len(all_data)} topics. Running analysis...", file=sys.stderr)
    prereq_of, depended_by = build_graphs(all_data)

    edge_count = sum(len(v) for v in prereq_of.values())
    domain_count = len(set(d.get("domain", "?") for d in all_data.values()))

    report = {
        "summary": {
            "total_topics": len(all_data),
            "domain_count": domain_count,
            "edge_count": edge_count,
            "domain_filter": args.domain,
        },
        "hubs": hub_report(all_data, depended_by, prereq_of),
        "longest_chains": longest_chains(all_data, prereq_of),
        "islands": find_islands(all_data, prereq_of),
        "orphans": orphan_topics(all_data, prereq_of, depended_by),
        "thin_courses": thin_courses(all_data),
        "shallow_content": shallow_content(all_data, all_bodies),
        "bidirectional_pairs": bidirectional_pairs(all_data),
    }

    if args.json:
        out_path = ROOT / "tools" / "qa_report.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"Report written to {out_path}", file=sys.stderr)
    else:
        print_report(report)


if __name__ == "__main__":
    main()
