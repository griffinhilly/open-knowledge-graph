#!/bin/bash
# Usage: validate_scoped.sh files...  |  validate_scoped.sh --list FILE
# Runs validate.py --quick; fails only if an ERROR names one of the given files
# (errors elsewhere = other agents' in-progress work).
cd /c/Users/griff/Projects/griffin/open-knowledge-graph
if [ "$1" = "--list" ]; then mine=$(cat "$2"); else mine=$(printf '%s\n' "$@"); fi
out=$(/c/Python314/python tools/validate.py --quick 2>&1)
echo "$out" | tail -1 >&2
errs=$(echo "$out" | grep -E '^\s+ERROR' | sed -E 's/^\s+ERROR\s+//; s/:.*//' | sed 's#\\#/#g')
[ -z "$errs" ] && exit 0
bad=$(comm -12 <(echo "$errs" | sort -u) <(echo "$mine" | sort -u))
if [ -n "$bad" ]; then echo "ERROR in committed file(s): $bad" >&2; exit 1; fi
echo "(errors only in files outside this commit: $(echo $errs))" >&2
exit 0
