#!/bin/bash
# Literature expansion — 8 new courses via Haiku
# Run from project root: bash tools/overnight/run-literature-expansion.sh

set -e

COURSES=(
  "literature--stories-and-narrative"
  "literature--mythology-folklore-oral-traditions"
  "literature--literary-movements-and-periods"
  "literature--genre-fiction"
  "literature--creative-nonfiction"
  "literature--world-literature"
  "literature--childrens-and-ya-literature"
  "literature--digital-and-experimental-literature"
)

MODEL="haiku"
TOTAL=${#COURSES[@]}
DONE=0

for course in "${COURSES[@]}"; do
  DONE=$((DONE + 1))
  echo ""
  echo "=========================================="
  echo "[$DONE/$TOTAL] Generating: $course"
  echo "=========================================="
  /c/Python314/python tools/overnight/orchestrator.py --model "$MODEL" --only "$course"
  echo "[$DONE/$TOTAL] Completed: $course"
done

echo ""
echo "All $TOTAL literature courses generated."
echo "Run: /c/Python314/python tools/validate.py"
