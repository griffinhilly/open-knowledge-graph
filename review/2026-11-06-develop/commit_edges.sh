#!/bin/bash
# Usage: commit_edges.sh "<message>" verdict files...   — applies high-confidence verdicts to files NOT in launched batches, commits only those.
set -eo pipefail
cd /c/Users/griff/Projects/griffin/open-knowledge-graph
D=review/2026-11-06-develop
msg="$1"; shift
{ for b in $(cat $D/launched.txt); do cut -f1 $D/batches/$b.tsv; done; cat $D/busy_extra.txt 2>/dev/null; } > $D/busy.txt
ls $D/../../domains >/dev/null
before=$(git diff --name-only -- domains 2>/dev/null | sort)
/c/Python314/python $D/apply_edges.py --apply --busy $D/busy.txt "$@"
for v in "$@"; do basename "$v" >> $D/edges/applied_files.txt; done
after=$(git diff --name-only -- domains 2>/dev/null | sort)
files=$(cat $D/edges/touched.txt | grep -v -x -F -f $D/busy.txt || true)
# also files already dirty before but not busy (shouldn't happen) are excluded on purpose
[ -z "$files" ] && { echo "no edge files changed"; exit 0; }
/c/Python314/python $D/fm_diff.py $files | grep -q 'OTHER CHANGED' && { echo "non-edge frontmatter change!"; exit 1; } || true
bash $D/validate_scoped.sh $files
git add $files $D/edges/*.verdicts.tsv $D/edges/applied.tsv $D/edges/applied_files.txt $D/edges/judgment.tsv
git commit -q -F - <<MSG
$msg

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_017QZFXqPWxhZ6QqXVSbbCUx
MSG
git log --oneline -1; echo "files: $(echo "$files" | wc -l)"
