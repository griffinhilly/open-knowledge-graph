"""Purpose: lesson-gap scan. Counts ## Explainer (the project's "lesson") and other body sections
per domain and course; flags missing/thin explainers. Outputs gaps.json + printed summary.
Usage: python review/2026-11-06-develop/gap_scan.py"""
import sys, json, pathlib, collections
sys.path.insert(0, 'tools')
from parse_topic import parse_topic, parse_sections
OUT = pathlib.Path('review/2026-11-06-develop')
topics = []
for f in sorted(pathlib.Path('domains').rglob('*.md')):
    if f.name.startswith('_') or '.claude' in f.parts: continue
    r = parse_topic(f)
    if not r or not r[0]: continue
    fm, body = r
    if fm.get('kind') == 'capacity': continue
    sec = parse_sections(body)
    ex = sec.get('Explainer', '') or ''
    topics.append(dict(id=fm.get('id'), path=f.as_posix(), domain=fm.get('domain'), course=fm.get('course'),
        stage=fm.get('stage'), explainer_words=len(ex.split()), has_q='Questions' in sec,
        has_how="How It's Best Learned" in sec, has_mis='Common Misconceptions' in sec,
        core_words=len((sec.get('Core Idea') or '').split()), sections=list(sec.keys())))
print('topics', len(topics))
print('section names seen:', collections.Counter(s for t in topics for s in t['sections']).most_common(12))
by = collections.defaultdict(list)
for t in topics: by[t['domain']].append(t)
print(f"{'domain':32} {'n':>5} {'noEx':>5} {'thin<150':>8} {'medEx':>6} {'noQ':>5}")
for dom, ts in sorted(by.items(), key=lambda kv: -len(kv[1])):
    ws = sorted(t['explainer_words'] for t in ts)
    print(f"{dom:32} {len(ts):5} {sum(w==0 for w in ws):5} {sum(0<w<150 for w in ws):8} {ws[len(ws)//2]:6} {sum(not t['has_q'] for t in ts):5}")
json.dump(topics, open(OUT/'gaps.json','w'), indent=0)
