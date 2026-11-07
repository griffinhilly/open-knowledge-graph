#!/bin/bash
# Usage: commit_batches.sh "<message>" L001 L002 ...  — after checkers finish: blank-line fix, scope check, validate, commit.
# File lists go through a file (Windows caps command lines at ~32K chars; 795 paths overflowed it).
set -eo pipefail
cd /c/Users/griff/Projects/griffin/open-knowledge-graph
D=review/2026-11-06-develop
msg="$1"; shift
LIST=$D/.commit_files.txt
for b in "$@"; do cut -f1 $D/batches/$b.tsv; done > $LIST
/c/Python314/python - $LIST <<'PY'
import sys,re,pathlib
for p in open(sys.argv[1],encoding='utf-8').read().split():
    f=pathlib.Path(p); t=f.read_text(encoding='utf-8')
    n=re.sub(r'([^\n])\n(## )', r'\1\n\n\2', t)
    if n!=t: f.write_text(n,encoding='utf-8')
PY
/c/Python314/python $D/reorder_sections.py $LIST
for b in "$@"; do grep -qP "\told:" $D/batches/$b.check.tsv 2>/dev/null && { grep -qx "$b" $D/oldtext_ok_batches.txt || echo "$b" >> $D/oldtext_ok_batches.txt; } || true; done
/c/Python314/python $D/scope_check.py "$@" | tail -15
bash $D/validate_scoped.sh --list $LIST
git add --pathspec-from-file=$LIST
git add $D/batches/
git commit -q -F - <<MSG
$msg

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_017QZFXqPWxhZ6QqXVSbbCUx
MSG
git log --oneline -1
