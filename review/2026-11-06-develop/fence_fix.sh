#!/bin/bash
# strip a stray trailing ``` (odd fence count) from listed files that are committed-clean and not in launched batches
cd /c/Users/griff/Projects/griffin/open-knowledge-graph
D=review/2026-11-06-develop
for b in $(cat $D/launched.txt); do cut -f1 $D/batches/$b.tsv; done | sort -u > $D/.busy_now.txt
/c/Python314/python - <<'PY'
import re,pathlib,subprocess
busy=set(open('review/2026-11-06-develop/.busy_now.txt').read().split())
dirty=set(subprocess.run(['git','diff','--name-only'],capture_output=True,text=True).stdout.split())
done=[]
for p in open('review/2026-11-06-develop/flagfix/stray_fence.txt').read().split():
    if p in dirty: continue
    f=pathlib.Path(p); t=f.read_text(encoding='utf-8')
    if t.count('```')%2==1 and re.search(r'\n```\s*\Z',t):
        f.write_text(re.sub(r'\n```\s*\Z','\n',t),encoding='utf-8'); done.append(p)
open('review/2026-11-06-develop/.fence_done.txt','w').write('\n'.join(done)+'\n'); print('fence fixed',len(done))
PY
