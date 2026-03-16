#!/usr/bin/env python3
"""Trace the positioning math for a specific topic."""

import sys
import math
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).resolve().parent))
from visualize_radial import (
    load_all_topics, load_domain_configs, compute_depths,
    build_radial_layout, STAGE_BANDS, DOMAIN_ORDER, get_topic_stage,
)


def main():
    tid = sys.argv[1] if len(sys.argv) > 1 else "organic-chemistry-intro"

    all_data = load_all_topics()
    configs = load_domain_configs()
    depths = compute_depths(all_data)
    positions, sectors, domain_order = build_radial_layout(all_data, configs, depths)

    data = all_data[tid]
    pos = positions[tid]
    domain = data.get("domain", "")
    stage = get_topic_stage(data, configs)
    sector = sectors[domain]

    print(f"=== {tid} ===")
    print(f"Domain: {domain}, Course: {data.get('course','')}, Stage: {stage}")
    print(f"Depth: {depths[tid]}")
    print(f"Stage band: {STAGE_BANDS[stage]}")
    print()

    # Depth context within this stage
    stage_depths = [depths[t] for t, d in all_data.items() if get_topic_stage(d, configs) == stage]
    d_min, d_max = min(stage_depths), max(stage_depths)
    depth_frac = (depths[tid] - d_min) / (d_max - d_min) if d_max > d_min else 0.5
    print(f"Depth range in {stage}: {d_min}-{d_max}")
    print(f"Depth fraction: {depth_frac:.3f}")
    band_min, band_max = STAGE_BANDS[stage]
    target_r = (band_min + depth_frac * (band_max - band_min)) * 500
    print(f"Target radius: {target_r:.1f} (band {band_min*500:.0f}-{band_max*500:.0f})")
    print()

    # Sector info
    sector_mid_deg = math.degrees(sector["mid"])
    sector_start_deg = math.degrees(sector["start"])
    sector_end_deg = math.degrees(sector["end"])
    print(f"Domain sector: {sector_start_deg:.1f} - {sector_end_deg:.1f} deg (mid: {sector_mid_deg:.1f})")
    print()

    # Final position
    final_r = math.hypot(pos["x"], pos["y"])
    final_theta = math.degrees(math.atan2(pos["y"], pos["x"]))
    if final_theta < 0:
        final_theta += 360
    print(f"Final position: r={final_r:.1f}, theta={final_theta:.1f} deg")
    print(f"Final (x,y): ({pos['x']:.1f}, {pos['y']:.1f})")
    print()

    # Edge analysis: what's pulling this topic?
    prereqs = []
    for p in data.get("prerequisites", []):
        if isinstance(p, dict) and p.get("id") in all_data:
            pid = p["id"]
            pd = all_data[pid]
            cross = pd.get("domain", "") != domain
            strength = 0.008 if cross else 0.003
            prereqs.append((pid, pd.get("domain",""), cross, strength, p.get("type","hard")))

    successors = []
    for other_tid, other_data in all_data.items():
        for p in other_data.get("prerequisites", []):
            if isinstance(p, dict) and p.get("id") == tid:
                cross = other_data.get("domain", "") != domain
                strength = 0.008 if cross else 0.003
                successors.append((other_tid, other_data.get("domain",""), cross, strength, p.get("type","hard")))

    print(f"=== PREREQUISITES ({len(prereqs)}) ===")
    same_pre_force = sum(s for _, _, c, s, _ in prereqs if not c)
    cross_pre_force = sum(s for _, _, c, s, _ in prereqs if c)
    for pid, pd, cross, strength, ptype in prereqs:
        label = "CROSS" if cross else "same"
        print(f"  {pid:<45} {pd:<25} {label} strength={strength} ({ptype})")
    print(f"  Total pull: same-domain={same_pre_force:.4f}, cross-domain={cross_pre_force:.4f}")

    print(f"\n=== SUCCESSORS ({len(successors)}) ===")
    succ_by_domain = defaultdict(lambda: {"count": 0, "cross": 0, "same": 0})
    for sid, sd, cross, strength, stype in successors:
        succ_by_domain[sd]["count"] += 1
        if cross:
            succ_by_domain[sd]["cross"] += strength
        else:
            succ_by_domain[sd]["same"] += strength

    for d in sorted(succ_by_domain, key=lambda d: -succ_by_domain[d]["count"]):
        info = succ_by_domain[d]
        total = info["cross"] + info["same"]
        label = "CROSS" if d != domain else "same"
        print(f"  {d:<35} {info['count']:>3} topics  force={total:.4f} ({label})")

    total_same = sum(s for _, _, c, s, _ in successors if not c)
    total_cross = sum(s for _, _, c, s, _ in successors if c)
    print(f"\n  Total successor pull: same-domain={total_same:.4f}, cross-domain={total_cross:.4f}")
    print(f"  Ratio cross/same: {total_cross/total_same:.1f}x" if total_same > 0 else "")

    # Where are the cross-domain successors pulling toward?
    print(f"\n=== NET FORCE DIRECTION ===")
    print(f"  Same-domain (chemistry) force: {same_pre_force + total_same:.4f}")
    print(f"  Cross-domain force: {cross_pre_force + total_cross:.4f}")
    print(f"  Cross/Same ratio: {(cross_pre_force + total_cross) / (same_pre_force + total_same):.1f}x" if (same_pre_force + total_same) > 0 else "")


if __name__ == "__main__":
    main()
