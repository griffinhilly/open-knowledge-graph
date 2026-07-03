#!/bin/bash
# Parallel overnight content generation for Open Knowledge Graph
# Launches workers concurrently, each processing its own shard.
#
# Usage:
#   cd ~/Projects/griffin/open-knowledge-graph
#   bash tools/overnight/run-parallel.sh q5            # All q5 shards
#   bash tools/overnight/run-parallel.sh q5 1 20       # Shards 1-20 only
#   bash tools/overnight/run-parallel.sh q5 21 40      # Shards 21-40 only
#
# Check progress:
#   python tools/overnight/check_progress.py

set -e
cd "$(dirname "$0")/../.."

PYTHON="/c/Python314/python"
RUNNER="$HOME/.claude/scripts/overnight.py"
PHASE="${1:-explainers}"
START="${2:-0}"
END="${3:-9999}"

echo "=============================================="
echo "OKG Parallel Content Generation — $(date)"
echo "Phase: $PHASE (shards $START-$END)"
echo "=============================================="

PATTERN="${PHASE}-shard-*.json"

PIDS=()
LAUNCHED=0

for manifest in tools/overnight/$PATTERN; do
    # Skip checkpoint files
    [[ "$manifest" == *checkpoint* ]] && continue
    if [ ! -f "$manifest" ]; then
        echo "No manifests found matching $PATTERN"
        exit 1
    fi

    # Extract shard number from filename
    temp="${manifest##*shard-}"
    SHARD_NUM="${temp%%.*}"

    # Filter by range
    if [ "$SHARD_NUM" -lt "$START" ] || [ "$SHARD_NUM" -gt "$END" ]; then
        continue
    fi

    LAUNCHED=$((LAUNCHED + 1))
    LOGFILE="tools/overnight/${PHASE}-worker-${SHARD_NUM}.out"
    echo "Starting shard $SHARD_NUM: $manifest -> $LOGFILE"
    nohup $PYTHON "$RUNNER" "$manifest" > "$LOGFILE" 2>&1 &
    PIDS+=($!)
    sleep 1  # Stagger launches slightly
done

if [ "$LAUNCHED" -eq 0 ]; then
    echo "No shards matched range $START-$END"
    exit 1
fi

echo ""
echo "Launched $LAUNCHED workers. PIDs: ${PIDS[*]}"
echo "PIDs saved to tools/overnight/worker-pids.txt"
printf "%s\n" "${PIDS[@]}" > tools/overnight/worker-pids.txt

echo ""
echo "Monitor progress:"
echo "  $PYTHON tools/overnight/check_progress.py"
echo ""
echo "View worker logs:"
echo "  tail -f tools/overnight/${PHASE}-worker-*.out"
echo ""
echo "Kill all workers:"
echo "  cat tools/overnight/worker-pids.txt | xargs kill"
