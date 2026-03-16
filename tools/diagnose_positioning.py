#!/usr/bin/env python3
"""Diagnose radial graph positioning issues.

Finds topics with the largest angular displacement from their domain sector center.
Reports the worst offenders with details on why they drifted.
"""

import sys
import math
from pathlib import Path
from collections import defaultdict

# Reuse the radial layout module
sys.path.insert(0, str(Path(__file__).resolve().parent))
from visualize_radial import (
    load_all_topics, load_domain_configs, compute_depths,
    build_radial_layout, DOMAIN_ORDER, STAGE_BANDS, get_topic_stage,
)


def angular_distance(a, b):
    """Shortest angular distance between two angles (radians), signed."""
    diff = (b - a + math.pi) % (2 * math.pi) - math.pi
    return diff


def analyze_positioning(positions, sectors, all_data, configs, depths):
    """Find topics furthest from their domain sector."""

    results = []

    for tid, pos in positions.items():
        data = all_data[tid]
        domain = data.get("domain", "")
        if domain not in sectors:
            continue

        sector = sectors[domain]
        sector_mid = sector["mid"]
        sector_half = (sector["end"] - sector["start"]) / 2

        # Current angle
        theta = pos["theta"]
        if theta < 0:
            theta += 2 * math.pi

        # Distance from sector center
        drift = angular_distance(sector_mid, theta)
        drift_normalized = abs(drift) / sector_half if sector_half > 0 else 0

        # Count prerequisites by domain
        prereq_domains = defaultdict(int)
        total_prereqs = 0
        for p in data.get("prerequisites", []):
            if isinstance(p, dict) and "id" in p:
                pid = p["id"]
                if pid in all_data:
                    prereq_domains[all_data[pid].get("domain", "")] += 1
                    total_prereqs += 1

        # Count dependents by domain
        dependent_domains = defaultdict(int)
        total_dependents = 0
        for other_tid, other_data in all_data.items():
            for p in other_data.get("prerequisites", []):
                if isinstance(p, dict) and p.get("id") == tid:
                    dependent_domains[other_data.get("domain", "")] += 1
                    total_dependents += 1

        cross_prereqs = sum(c for d, c in prereq_domains.items() if d != domain)
        cross_dependents = sum(c for d, c in dependent_domains.items() if d != domain)

        stage = get_topic_stage(data, configs)

        results.append({
            "id": tid,
            "title": data.get("title", tid),
            "domain": domain,
            "course": data.get("course", ""),
            "stage": stage,
            "depth": depths.get(tid, 0),
            "drift_rad": drift,
            "drift_deg": math.degrees(drift),
            "drift_normalized": drift_normalized,
            "total_prereqs": total_prereqs,
            "cross_prereqs": cross_prereqs,
            "prereq_domains": dict(prereq_domains),
            "total_dependents": total_dependents,
            "cross_dependents": cross_dependents,
            "dependent_domains": dict(dependent_domains),
            "total_connections": total_prereqs + total_dependents,
            "x": pos["x"],
            "y": pos["y"],
            "r": pos["r"],
        })

    return results


def main():
    print("Loading topics...")
    all_data = load_all_topics()
    configs = load_domain_configs()
    print(f"Loaded {len(all_data)} topics across {len(configs)} domains")

    print("Computing depths...")
    depths = compute_depths(all_data)

    print("Computing radial layout...")
    positions, sectors, domain_order = build_radial_layout(all_data, configs, depths)

    print("Analyzing positioning...\n")
    results = analyze_positioning(positions, sectors, all_data, configs, depths)

    # Sort by normalized drift (how far outside their sector they are)
    results.sort(key=lambda r: r["drift_normalized"], reverse=True)

    # Topics outside their sector (drift_normalized > 1.0)
    outside = [r for r in results if r["drift_normalized"] > 1.0]
    print(f"=== TOPICS OUTSIDE THEIR DOMAIN SECTOR: {len(outside)} ===\n")

    # Show top 40 worst offenders
    print(f"{'#':>3}  {'Topic ID':<45} {'Domain':<30} {'Drift°':>7}  {'Norm':>5}  {'Conn':>4}  {'XPre':>4}  {'XDep':>4}  Why")
    print("-" * 160)
    for i, r in enumerate(results[:40]):
        # Figure out which domain it drifted toward
        theta = r["drift_rad"]
        drift_dir = "CW" if theta < 0 else "CCW"

        # Biggest cross-domain pull
        all_cross = {}
        for d, c in r["prereq_domains"].items():
            if d != r["domain"]:
                all_cross[d] = all_cross.get(d, 0) + c
        for d, c in r["dependent_domains"].items():
            if d != r["domain"]:
                all_cross[d] = all_cross.get(d, 0) + c

        if all_cross:
            top_pull = max(all_cross, key=all_cross.get)
            pull_str = f"{drift_dir} -> {top_pull} ({all_cross[top_pull]} edges)"
        else:
            pull_str = "no cross-domain edges"

        marker = "***" if r["drift_normalized"] > 1.0 else ""
        print(f"{i+1:3}  {r['id']:<45} {r['domain']:<30} {r['drift_deg']:>+7.1f}  {r['drift_normalized']:>5.2f}  {r['total_connections']:>4}  {r['cross_prereqs']:>4}  {r['cross_dependents']:>4}  {pull_str} {marker}")

    # Summary stats
    print(f"\n=== SUMMARY ===")
    print(f"Total topics positioned: {len(results)}")
    print(f"Outside their sector (norm > 1.0): {len(outside)}")
    print(f"Moderately displaced (norm 0.8-1.0): {len([r for r in results if 0.8 <= r['drift_normalized'] <= 1.0])}")

    # Per-domain breakdown of displaced topics
    print(f"\n=== PER-DOMAIN DISPLACEMENT (topics outside sector) ===")
    domain_outside = defaultdict(int)
    domain_total = defaultdict(int)
    for r in results:
        domain_total[r["domain"]] += 1
        if r["drift_normalized"] > 1.0:
            domain_outside[r["domain"]] += 1

    for d in domain_order:
        if d in domain_total:
            n_out = domain_outside.get(d, 0)
            n_tot = domain_total[d]
            pct = n_out / n_tot * 100 if n_tot else 0
            bar = "#" * int(pct / 2)
            print(f"  {d:<35} {n_out:>4}/{n_tot:<5} ({pct:4.1f}%) {bar}")


if __name__ == "__main__":
    main()
