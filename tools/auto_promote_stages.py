#!/usr/bin/env python3
"""Auto-promote topics where a hard prereq is at a strictly higher stage.

Iterates until convergence (promoting one topic may expose another).
Only promotes based on HARD prereqs — soft prereq mismatches are logged
for manual/agent review.
"""
import yaml
import json
from pathlib import Path
from collections import defaultdict

DOMAINS = Path(__file__).resolve().parent.parent / "domains"
STAGE_ORDER = [
    "pre-formal", "concrete-operations", "abstract-reasoning",
    "formal-systems", "advanced", "expert",
]
STAGE_RANK = {s: i for i, s in enumerate(STAGE_ORDER)}


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Apply promotions (default: dry run)")
    args = parser.parse_args()

    topic_info = {}
    topic_path = {}
    for md in DOMAINS.rglob("*.md"):
        if md.name.startswith("_"):
            continue
        text = md.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        end = text.find("---", 3)
        if end == -1:
            continue
        try:
            fm = yaml.safe_load(text[3:end])
        except Exception:
            continue
        if not fm:
            continue
        prereqs = []
        for p in fm.get("prerequisites") or []:
            if isinstance(p, dict):
                prereqs.append((p["id"], p.get("type", "hard")))
            else:
                prereqs.append((str(p), "hard"))
        topic_info[md.stem] = {
            "stage": fm.get("stage", ""),
            "domain": fm.get("domain", ""),
            "course": fm.get("course", ""),
            "prereqs": prereqs,
        }
        topic_path[md.stem] = md

    total_promoted = 0
    promotions = []

    for iteration in range(10):
        promoted = 0
        for tid, info in topic_info.items():
            trank = STAGE_RANK.get(info["stage"], -1)
            if trank < 0:
                continue
            max_hard = -1
            max_hard_prereq = None
            for pid, ptype in info["prereqs"]:
                if ptype != "hard" or pid not in topic_info:
                    continue
                prank = STAGE_RANK.get(topic_info[pid]["stage"], -1)
                if prank > max_hard:
                    max_hard = prank
                    max_hard_prereq = pid

            if max_hard > trank:
                new_stage = STAGE_ORDER[max_hard]
                old_stage = info["stage"]
                promotions.append(
                    f"  {info['domain']}/{info['course']}/{tid}: "
                    f"{old_stage} -> {new_stage} (hard prereq: {max_hard_prereq})"
                )
                if args.apply:
                    md = topic_path[tid]
                    text = md.read_text(encoding="utf-8")
                    text = text.replace(f"stage: {old_stage}", f"stage: {new_stage}", 1)
                    md.write_text(text, encoding="utf-8")
                info["stage"] = new_stage
                promoted += 1

        total_promoted += promoted
        if promoted == 0:
            print(f"Converged after {iteration + 1} iterations")
            break
        print(f"Pass {iteration + 1}: {promoted} promotions")

    mode = "APPLIED" if args.apply else "DRY RUN"
    print(f"\n{mode}: {total_promoted} topics promoted")
    if promotions and not args.apply:
        for p in promotions[:30]:
            print(p)
        if len(promotions) > 30:
            print(f"  ... and {len(promotions) - 30} more")

    # Report remaining soft-prereq mismatches
    soft_mismatches = defaultdict(list)
    for tid, info in topic_info.items():
        trank = STAGE_RANK.get(info["stage"], -1)
        for pid, ptype in info["prereqs"]:
            if ptype != "soft" or pid not in topic_info:
                continue
            prank = STAGE_RANK.get(topic_info[pid]["stage"], -1)
            if prank > trank:
                soft_mismatches[info["domain"]].append({
                    "topic": tid,
                    "stage": info["stage"],
                    "prereq": pid,
                    "prereq_stage": topic_info[pid]["stage"],
                    "course": info["course"],
                })
                break

    if soft_mismatches:
        total_soft = sum(len(v) for v in soft_mismatches.values())
        print(f"\nRemaining soft-prereq mismatches ({total_soft} topics):")
        for domain in sorted(soft_mismatches):
            print(f"  {domain}: {len(soft_mismatches[domain])}")
        Path(DOMAINS.parent / "tools" / "stage-audit-soft.json").write_text(
            json.dumps(dict(soft_mismatches), indent=1), encoding="utf-8"
        )


if __name__ == "__main__":
    main()
