#!/bin/bash
# Remaining 6 literature courses (mythology already running separately)
set -e
cd /c/Users/griff/Projects/griffin/open-knowledge-graph

COURSES=(
  "literature--literary-movements-and-periods"
  "literature--genre-fiction"
  "literature--creative-nonfiction"
  "literature--world-literature"
  "literature--childrens-and-ya-literature"
  "literature--digital-and-experimental-literature"
)

TOTAL=${#COURSES[@]}
DONE=0

for course in "${COURSES[@]}"; do
  DONE=$((DONE + 1))
  echo ""
  echo "=========================================="
  echo "[$DONE/$TOTAL] Generating: $course"
  echo "=========================================="
  /c/Python314/python tools/overnight/orchestrator.py --model haiku --only "$course"
  echo "[$DONE/$TOTAL] Completed: $course"
done

echo ""
echo "All $TOTAL remaining literature courses generated."
echo "Run validation: /c/Python314/python tools/validate.py"
