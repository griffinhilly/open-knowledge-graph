#!/usr/bin/env python3
"""Check progress across all parallel shard workers."""

import json
import sys
from pathlib import Path

OVERNIGHT_DIR = Path(__file__).resolve().parent


def check_phase(phase):
    total_completed = 0
    total_failed = 0
    total_items = 0
    shard_details = []

    for i in range(1, 100):
        manifest_path = OVERNIGHT_DIR / f"{phase}-shard-{i}.json"
        if not manifest_path.exists():
            if i > 65:  # Allow gaps in numbering up to reasonable max
                break
            continue

        manifest = json.loads(manifest_path.read_text())
        n_items = len(manifest.get("items", []))
        total_items += n_items

        cp_path = OVERNIGHT_DIR / f"{phase}-shard-{i}-checkpoint.json"
        if cp_path.exists():
            cp = json.loads(cp_path.read_text())
            completed = len(cp.get("completed", []))
            failed = len(cp.get("failed", []))
            runs = len(cp.get("runs", []))
        else:
            completed = failed = runs = 0

        total_completed += completed
        total_failed += failed
        shard_details.append((i, n_items, completed, failed, runs))

    if not shard_details:
        print(f"  No shards found for {phase}")
        return

    pct = (total_completed / total_items * 100) if total_items > 0 else 0
    print(f"  Total: {total_completed}/{total_items} completed ({pct:.1f}%), {total_failed} failed")
    print(f"  {'Shard':>7} {'Items':>7} {'Done':>7} {'Fail':>7} {'Runs':>7} {'Pct':>7}")
    for i, n_items, completed, failed, runs in shard_details:
        spct = (completed / n_items * 100) if n_items > 0 else 0
        print(f"  {i:>7} {n_items:>7} {completed:>7} {failed:>7} {runs:>7} {spct:>6.1f}%")


def main():
    print("=" * 55)
    print("OKG Content Generation Progress")
    print("=" * 55)

    print("\nExplainers:")
    check_phase("explainer")

    print("\nQuestions (old, 3 per topic):")
    check_phase("questions")

    print("\nQuestions (new, 5 per topic):")
    check_phase("q5")

    # Check for running workers
    pids_file = OVERNIGHT_DIR / "worker-pids.txt"
    if pids_file.exists():
        import subprocess
        pids = pids_file.read_text().strip().split("\n")
        alive = 0
        for pid in pids:
            try:
                result = subprocess.run(
                    ["kill", "-0", pid.strip()],
                    capture_output=True, timeout=5,
                )
                if result.returncode == 0:
                    alive += 1
            except Exception:
                pass
        print(f"\nWorkers: {alive}/{len(pids)} alive")

    print()


if __name__ == "__main__":
    main()
