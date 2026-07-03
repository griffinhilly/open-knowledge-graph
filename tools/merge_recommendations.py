#!/usr/bin/env python3
"""Merge all batch recommendation files into a single file for apply_restaging.py."""

import json
from pathlib import Path

BATCH_DIR = Path(__file__).parent / "restaging_batches"
OUTPUT = Path(__file__).parent / "restaging_recommendations_merged.json"

all_recs = []
changes = 0
no_change = 0
errors = 0

for rec_file in sorted(BATCH_DIR.glob("*_recommendations.json")):
    with open(rec_file, "r", encoding="utf-8") as f:
        try:
            recs = json.load(f)
        except json.JSONDecodeError as e:
            print(f"ERROR parsing {rec_file.name}: {e}")
            errors += 1
            continue

    if not isinstance(recs, list):
        print(f"WARNING: {rec_file.name} is not a list, skipping")
        errors += 1
        continue

    batch_changes = 0
    batch_total = 0
    for rec in recs:
        if not isinstance(rec, dict):
            continue
        batch_total += 1
        # Only include actual changes
        current = rec.get("current_stage", "")
        new = rec.get("new_stage", "")
        if current != new and new:
            all_recs.append(rec)
            batch_changes += 1
        else:
            no_change += 1

    changes += batch_changes
    print(f"{rec_file.name}: {batch_changes}/{batch_total} changes")

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(all_recs, f, indent=1, ensure_ascii=False)

print(f"\nTotal: {changes} changes, {no_change} no-change, {errors} errors")
print(f"Output: {OUTPUT}")
