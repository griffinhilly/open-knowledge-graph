"""Purpose: build writer batch manifests (one course chunk, <=30 topics each), thinnest first.
Needs per file: how (missing How It's Best Learned), mis (missing Common Misconceptions),
q:<i>:<field> (question item missing answer/explanation), ex (Explainer < 150 words).
Outputs batches/L###.tsv + batches/index.tsv. Usage: python review/2026-11-06-develop/make_batches.py"""
import json, collections, pathlib
D = pathlib.Path('review/2026-11-06-develop'); B = D/'batches'; B.mkdir(exist_ok=True)
CORE = ['mathematics','physics','chemistry','biology','earth-and-space-sciences','computer-science',
        'history','literature','language-and-communication','economics']
T = json.load(open(D/'gaps.json'))
qrem = collections.defaultdict(list)
for line in open(D/'questions_remaining.tsv', encoding='utf-8'):
    p, i, k = line.rstrip('\n').split('\t'); qrem[p].append(f'q:{i}:{k}')
needs = {}
for t in T:
    n = []
    if not t['has_how']: n.append('how')
    if not t['has_mis']: n.append('mis')
    if t['explainer_words'] < 150: n.append('ex')
    n += qrem.get(t['path'], [])
    if n: needs[t['path']] = (t, n)
def key(item):
    t, n = item
    core = t['domain'] in CORE
    return (0 if core else 1, CORE.index(t['domain']) if core else 99, t['domain'], t['course'], t['path'])
by_course = collections.defaultdict(list)
for t, n in sorted(needs.values(), key=key): by_course[(t['domain'], t['course'])].append((t, n))
# order courses: core first, then by thinness (share of topics missing both sections)
RANK = {s: i for i, s in enumerate(['proto-formal','pre-formal','concrete-operations','abstract-reasoning','formal-systems','advanced','expert'])}
size = collections.Counter((t['domain'], t['course']) for t in T)
stages = collections.defaultdict(list)
for t in T: stages[(t['domain'], t['course'])].append(RANK.get(t['stage'], 4))
def ckey(kv):
    (dom, course), items = kv
    share = sum(('how' in n and 'mis' in n) for _, n in items) / size[(dom, course)]
    st = sorted(stages[(dom, course)]); med = st[len(st)//2]
    return (0 if dom in CORE else 1, -round(share, 1), med, dom, course)
batches = []
for (dom, course), items in sorted(by_course.items(), key=ckey):
    for s in range(0, len(items), 30):
        batches.append((dom, course, items[s:s+30]))
idx = []
for i, (dom, course, items) in enumerate(batches, 1):
    name = f'L{i:03d}'
    (B/f'{name}.tsv').write_text(''.join(f"{t['path']}\t{','.join(n)}\n" for t, n in items), encoding='utf-8')
    idx.append(f"{name}\t{dom}\t{course}\t{len(items)}\t{sum('how' in n for _,n in items)}\t{sum('mis' in n for _,n in items)}\t{sum(any(x.startswith('q:') for x in n) for _,n in items)}\n")
(B/'index.tsv').write_text('batch\tdomain\tcourse\ttopics\thow\tmis\tqfix\n' + ''.join(idx), encoding='utf-8')
core_b = sum(1 for d,_,_ in batches if d in CORE)
print('files needing work', len(needs), '| batches', len(batches), '| core batches', core_b)
print('core topics', sum(len(it) for d,_,it in batches if d in CORE))
