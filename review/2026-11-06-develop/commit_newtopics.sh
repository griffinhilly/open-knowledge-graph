#!/bin/bash
# Usage: commit_newtopics.sh DOMAIN  — commits checked new topic files for DOMAIN (untracked files in domains/DOMAIN, minus rejects/duplicates), then applies proposed edges.
set -eo pipefail
cd /c/Users/griff/Projects/griffin/open-knowledge-graph
D=review/2026-11-06-develop; dom=$1
files=$(git status --short --untracked-files=all domains/$dom | grep '^??' | cut -c4- | grep '\.md$')
bad=$(grep -P '\t(reject|duplicate-of)' $D/newtopics/$dom.check.tsv | cut -f1 | sed 's#.*[\/]##' || true)
for b in $bad; do files=$(echo "$files" | grep -v "/$b\$" || true); echo "excluded: $b"; done
n=$(echo "$files" | grep -c . || true); echo "new files: $n"
/c/Python314/python $D/yaml_check.py $files | tail -1
bash $D/validate_scoped.sh $files
summary=$(/c/Python314/python $D/stats.py | grep -c . >/dev/null; awk -F'\t' '{c+=$2; w+=$3} END {print c" claims checked, "w" wrong (fixed)"}' $D/newtopics/$dom.check.tsv)
git add $files $D/newtopics/$dom.*
git commit -q -F - <<MSG
New topics: $n $dom topics filling standard-syllabus gaps, fact-checked

Gap analysis and sources: $D/newtopics/$dom.report.md. Independent check
(with web lookups): $summary.

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_017QZFXqPWxhZ6QqXVSbbCUx
MSG
git log --oneline -1
grep -P '^ADD\t' $D/newtopics/$dom.report.md | awk -F'\t' 'BEGIN{OFS="\t"} {print $1,$2,$3,$4,"high",$5}' > $D/edges/newtopic_$dom.verdicts.tsv || true
[ -s $D/edges/newtopic_$dom.verdicts.tsv ] && bash $D/commit_edges.sh "Edges from existing topics to the new $dom topics" $D/edges/newtopic_$dom.verdicts.tsv || echo "no proposed edges"
