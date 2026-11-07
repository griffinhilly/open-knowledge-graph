import re,yaml,collections,pathlib
keys=collections.Counter(); shapes=collections.Counter(); ex={}
for line in open('review/2026-11-06-develop/broken_question_files.txt'):
    p=pathlib.Path(line.strip().replace(chr(92),'/'))
    t=p.read_text(encoding='utf-8')
    m=re.search(r'^## Questions\s*\n(.*?)(?=^## |\Z)',t,re.M|re.S)
    b=re.search(r'```ya?ml\n(.*?)```',m.group(1),re.S) if m else None
    if not b: shapes['noblock']+=1; ex.setdefault('noblock',p); continue
    try: q=yaml.safe_load(b.group(1))
    except Exception: shapes['yamlerr']+=1; ex.setdefault('yamlerr',p); continue
    shapes[type(q).__name__]+=1
    if isinstance(q,list):
        for it in q:
            if isinstance(it,dict): k=tuple(sorted(it.keys())); keys[k]+=1; ex.setdefault(k,p)
    else: ex.setdefault(type(q).__name__,p)
print(shapes)
for k,n in keys.most_common(14): print(n,k)
for k,v in ex.items():
    if not isinstance(k,tuple): print(k,v)
print('---- examples')
for k in [('explanation','question','type'),('answer','question','type'),('answer','explanation','question')]:
    p=ex[k]; t=p.read_text(encoding='utf-8'); m=re.search(r'^## Questions\s*\n(.*?)(?=^## |\Z)',t,re.M|re.S)
    q=yaml.safe_load(re.search(r'```ya?ml\n(.*?)```',m.group(1),re.S).group(1))
    it=[i for i in q if isinstance(i,dict) and tuple(sorted(i.keys()))==k][0]
    print(k,p); print({a:(str(b)[:90]) for a,b in it.items()})
