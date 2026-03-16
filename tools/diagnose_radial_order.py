#!/usr/bin/env python3
"""Diagnose radial ordering violations.

Finds prerequisite edges where the prerequisite has a greater radius
(more advanced position) than its successor — visual contradictions
in the "inner=foundational, outer=advanced" layout.
"""

import sys
import math
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).resolve().parent))
from visualize_radial import (
    load_all_topics, load_domain_configs, compute_depths,
    STAGE_BANDS, get_topic_stage, DOMAIN_ORDER,
)

# Numeric ordering for stages (lower = more foundational)
STAGE_RANK = {
    "pre-formal": 0,
    "concrete-operations": 1,
    "abstract-reasoning": 2,
    "formal-systems": 3,
    "advanced": 4,
}


def main():
    print("Loading topics...")
    all_data = load_all_topics()
    configs = load_domain_configs()
    print(f"Loaded {len(all_data)} topics")

    print("Computing depths...")
    depths = compute_depths(all_data)

    # Compute stage for every topic
    topic_stages = {}
    for tid, data in all_data.items():
        topic_stages[tid] = get_topic_stage(data, configs)

    # Find all prerequisite edges where prereq stage > successor stage
    violations = []
    total_edges = 0
    for tid, data in all_data.items():
        for p in data.get("prerequisites", []):
            if isinstance(p, dict) and "id" in p:
                pid = p["id"]
                if pid not in all_data:
                    continue
                total_edges += 1
                prereq_stage = topic_stages.get(pid, "abstract-reasoning")
                succ_stage = topic_stages.get(tid, "abstract-reasoning")
                prereq_rank = STAGE_RANK.get(prereq_stage, 2)
                succ_rank = STAGE_RANK.get(succ_stage, 2)

                if prereq_rank > succ_rank:
                    ptype = p.get("type", "hard")
                    prereq_domain = all_data[pid].get("domain", "")
                    succ_domain = data.get("domain", "")
                    cross = prereq_domain != succ_domain
                    violations.append({
                        "prereq_id": pid,
                        "prereq_title": all_data[pid].get("title", pid),
                        "prereq_stage": prereq_stage,
                        "prereq_domain": prereq_domain,
                        "succ_id": tid,
                        "succ_title": data.get("title", tid),
                        "succ_stage": succ_stage,
                        "succ_domain": succ_domain,
                        "stage_gap": prereq_rank - succ_rank,
                        "type": ptype,
                        "cross_domain": cross,
                    })

    print(f"\nTotal prerequisite edges: {total_edges}")
    print(f"Radial ordering violations (prereq more advanced than successor): {len(violations)}")
    print(f"Violation rate: {len(violations)/total_edges*100:.1f}%\n")

    # Break down by type
    hard_v = [v for v in violations if v["type"] == "hard"]
    soft_v = [v for v in violations if v["type"] == "soft"]
    cross_v = [v for v in violations if v["cross_domain"]]
    same_v = [v for v in violations if not v["cross_domain"]]

    print(f"Hard prerequisite violations: {len(hard_v)}")
    print(f"Soft prerequisite violations: {len(soft_v)}")
    print(f"Cross-domain violations: {len(cross_v)}")
    print(f"Same-domain violations: {len(same_v)}")

    # Break down by stage gap
    print(f"\nBy stage gap (prereq rank - successor rank):")
    for gap in sorted(set(v["stage_gap"] for v in violations)):
        count = len([v for v in violations if v["stage_gap"] == gap])
        print(f"  Gap {gap}: {count} violations")

    # Worst offenders: prerequisites that appear in the most violations
    prereq_violation_count = defaultdict(int)
    for v in violations:
        prereq_violation_count[v["prereq_id"]] += 1

    worst = sorted(prereq_violation_count.items(), key=lambda x: -x[1])[:30]
    print(f"\n=== TOP 30 PREREQUISITE TOPICS CAUSING VIOLATIONS ===")
    print(f"{'#':>3}  {'Topic ID':<45} {'Stage':<20} {'Domain':<30} {'Violations':>10}")
    print("-" * 115)
    for i, (pid, count) in enumerate(worst):
        data = all_data[pid]
        stage = topic_stages[pid]
        domain = data.get("domain", "")
        print(f"{i+1:3}  {pid:<45} {stage:<20} {domain:<30} {count:>10}")

    # Show specific violation examples for top 5
    print(f"\n=== DETAILED EXAMPLES (top 5 offenders) ===")
    for pid, count in worst[:5]:
        data = all_data[pid]
        stage = topic_stages[pid]
        print(f"\n  {pid} (stage: {stage}, domain: {data.get('domain','')})")
        my_violations = [v for v in violations if v["prereq_id"] == pid]
        for v in my_violations[:5]:
            marker = "CROSS" if v["cross_domain"] else "same"
            print(f"    -> {v['succ_id']} (stage: {v['succ_stage']}, domain: {v['succ_domain']}, {v['type']}, {marker})")
        if len(my_violations) > 5:
            print(f"    ... and {len(my_violations) - 5} more")

    # Per-domain summary
    print(f"\n=== PER-DOMAIN VIOLATION COUNTS ===")
    domain_violations = defaultdict(int)
    domain_edges = defaultdict(int)
    for v in violations:
        domain_violations[v["prereq_domain"]] += 1
    for tid, data in all_data.items():
        for p in data.get("prerequisites", []):
            if isinstance(p, dict) and "id" in p and p["id"] in all_data:
                domain_edges[all_data[p["id"]].get("domain", "")] += 1

    for d in DOMAIN_ORDER:
        n_v = domain_violations.get(d, 0)
        n_e = domain_edges.get(d, 0)
        pct = n_v / n_e * 100 if n_e else 0
        bar = "#" * int(pct)
        print(f"  {d:<35} {n_v:>4}/{n_e:<5} ({pct:4.1f}%) {bar}")


if __name__ == "__main__":
    main()
