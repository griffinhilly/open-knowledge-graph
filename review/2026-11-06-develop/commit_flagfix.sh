#!/bin/bash
# Usage: commit_flagfix.sh NAME "<message>" BATCH...  — commits flag-fix edits in the given (already committed) batches.
set -eo pipefail
cd /c/Users/griff/Projects/griffin/open-knowledge-graph
D=review/2026-11-06-develop; name=$1; msg=$2; shift 2
ff=$(for b in "$@"; do cut -f1 $D/batches/$b.tsv; done | while read f; do git diff --quiet -- "$f" || echo "$f"; done)
[ -z "$ff" ] && { echo "no changes"; exit 0; }
/c/Python314/python $D/fm_diff.py $ff | grep -q 'OTHER CHANGED\|+\|~' && { echo "frontmatter changed!"; /c/Python314/python $D/fm_diff.py $ff | grep -v ' $'; exit 1; } || true
/c/Python314/python $D/yaml_check.py $ff
git add $ff $D/flagfix/$name.tsv
git commit -q -F - <<MSG
$msg

Each flag verified against sources by a separate agent; log $D/flagfix/$name.tsv.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_017QZFXqPWxhZ6QqXVSbbCUx
MSG
git log --oneline -1; echo "files: $(echo "$ff" | wc -l)"
