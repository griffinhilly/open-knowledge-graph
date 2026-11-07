"""Show parsed frontmatter differences (prereqs/builds-toward/other) vs HEAD for given files."""
import sys,subprocess,yaml
for f in sys.argv[1:]:
    old=subprocess.run(['git','show','HEAD:'+f],capture_output=True,text=True,encoding='utf-8').stdout
    new=open(f,encoding='utf-8').read()
    fo=yaml.safe_load(old.split('---')[1]); fn=yaml.safe_load(new.split('---')[1])
    po={p['id']:p.get('type') for p in fo.get('prerequisites') or []}; pn={p['id']:p.get('type') for p in fn.get('prerequisites') or []}
    d=[f"-{k}" for k in po if k not in pn]+[f"+{k}({pn[k]})" for k in pn if k not in po]+[f"~{k}->{pn[k]}" for k in po if k in pn and po[k]!=pn[k]]
    bo=fo.get('builds-toward') or []; bn=fn.get('builds-toward') or []
    d+= [f"bt-{k}" for k in bo if k not in bn]+[f"bt+{k}" for k in bn if k not in bo]
    other=[k for k in set(fo)|set(fn) if k not in ('prerequisites','builds-toward') and fo.get(k)!=fn.get(k)]
    if other: d.append(f"OTHER CHANGED {other}")
    print(f.split('/')[-1], ' '.join(d))
