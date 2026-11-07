"""Purpose: deterministic edge-review candidate lists for agent judgment.
zero.tsv  : non-pre-formal topics with no prerequisites
bt_<dom>.tsv : A lists B in builds-toward but B does not list A as a prerequisite (core domains, A or B in dom)
inv_<dom>.tsv: prerequisite staged 2+ stages above its successor (core domains)
Columns: ids, titles, courses, stages. Usage: python review/2026-11-06-develop/edge_candidates.py"""
import sys, pathlib, collections
sys.path.insert(0, 'tools')
from parse_topic import parse_topic
CORE = ['mathematics','physics','chemistry','biology','earth-and-space-sciences','computer-science','history','literature','language-and-communication','economics']
RANK = {s: i for i, s in enumerate(['proto-formal','pre-formal','concrete-operations','abstract-reasoning','formal-systems','advanced','expert'])}
O = pathlib.Path('review/2026-11-06-develop/edges')
T = {}
for f in pathlib.Path('domains').rglob('*.md'):
    if f.name.startswith('_'): continue
    r = parse_topic(f)
    if r and r[0]: fm = r[0]; fm['_path'] = f.as_posix(); T[fm['id']] = fm
pre = {i: {(p['id'] if isinstance(p, dict) else p): (p.get('type', 'hard') if isinstance(p, dict) else 'hard') for p in (fm.get('prerequisites') or [])} for i, fm in T.items()}
def row(*ids): return '\t'.join(f"{i}\t{T[i].get('title')}\t{T[i]['domain']}/{T[i]['course']}\t{T[i].get('stage')}" for i in ids) + '\n'
zero = [i for i, fm in T.items() if not pre[i] and fm.get('kind') != 'capacity' and fm.get('stage') not in ('pre-formal', 'proto-formal')]
(O/'zero.tsv').write_text(''.join(row(i) for i in sorted(zero, key=lambda i: (T[i]['domain'], T[i]['course']))), encoding='utf-8')
bt = collections.defaultdict(list); inv = collections.defaultdict(list)
for a, fm in T.items():
    for b in fm.get('builds-toward') or []:
        if b in T and a not in pre[b] and T[b]['domain'] in CORE: bt[T[b]['domain']].append((a, b))
for b, ps in pre.items():
    for a, typ in ps.items():
        if a in T and T[b]['domain'] in CORE and T[a].get('kind') != 'capacity':
            if RANK.get(T[a].get('stage'), 4) - RANK.get(T[b].get('stage'), 4) >= 2: inv[T[b]['domain']].append((a, b, typ))
for d in CORE:
    (O/f'bt_{d}.tsv').write_text(''.join(row(a, b) for a, b in sorted(bt[d], key=lambda x: (T[x[1]]['course'], x[1]))), encoding='utf-8')
    (O/f'inv_{d}.tsv').write_text(''.join(row(a, b).rstrip('\n') + f'\t{t}\n' for a, b, t in sorted(inv[d], key=lambda x: (T[x[1]]['course'], x[1]))), encoding='utf-8')
print('zero', len(zero)); print('bt', {d: len(bt[d]) for d in CORE}, sum(len(v) for v in bt.values())); print('inv', {d: len(inv[d]) for d in CORE}, sum(len(v) for v in inv.values()))
