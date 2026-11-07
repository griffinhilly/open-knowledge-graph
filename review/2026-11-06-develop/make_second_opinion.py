"""Purpose: two-reviewer rule for medium-confidence edge verdicts.
make:  python make_second_opinion.py make <verdicts.tsv>   -> edges/so_<stem>.tsv (candidates only, first verdict hidden)
merge: python make_second_opinion.py merge <verdicts.tsv>  -> edges/<stem>.agreed.tsv (both reviewers agree on verdict
       [and type for ADD]; written as confidence=high so apply_edges.py applies them); disagreements stay in judgment.
Second reviewer writes edges/so_<stem>.verdicts.tsv using EDGE-INSTRUCTIONS.md (bt-type input format).
"""
import sys, pathlib, collections
sys.path.insert(0, 'tools')
from parse_topic import parse_topic
E = pathlib.Path('review/2026-11-06-develop/edges')
mode, vf = sys.argv[1], pathlib.Path(sys.argv[2])
stem = vf.name.replace('.verdicts.tsv', '')
rows = [l.split('\t') for l in vf.read_text(encoding='utf-8').splitlines() if l.strip()]
med = [r for r in rows if len(r) >= 5 and r[0] in ('ADD', 'DROP', 'REMOVE', 'SOFTEN') and r[4] != 'high']
if mode == 'make':
    T = {}
    for f in pathlib.Path('domains').rglob('*.md'):
        if f.name.startswith('_'): continue
        r = parse_topic(f)
        if r and r[0]: T[r[0]['id']] = r[0]
    def blk(i): return f"{i}\t{T[i].get('title')}\t{T[i]['domain']}/{T[i]['course']}\t{T[i].get('stage')}" if i in T else f"{i}\t?\t?\t?"
    seen = set(); out = []
    for r in med:
        if (r[1], r[2]) in seen: continue
        seen.add((r[1], r[2])); out.append(blk(r[1]) + '\t' + blk(r[2]) + '\n')
    (E / f'so_{stem}.tsv').write_text(''.join(out), encoding='utf-8')
    print(f'{len(out)} candidates -> so_{stem}.tsv')
else:
    second = {}
    for l in (E / f'so_{stem}.verdicts.tsv').read_text(encoding='utf-8').splitlines():
        p = l.split('\t')
        if len(p) >= 4: second[(p[1], p[2])] = (p[0], p[3])
    agreed = []; c = collections.Counter()
    for r in med:
        s = second.get((r[1], r[2]))
        if not s: c['no second verdict'] += 1; continue
        same = s[0] == r[0] and (r[0] != 'ADD' or s[1] == r[3])
        if not same and r[0] == 'ADD' and s[0] == 'ADD': # agree on adding, disagree on strength -> soft
            agreed.append(['ADD', r[1], r[2], 'soft', 'high', 'two reviewers agree (strength differed; soft)']); c['agree-add-soft'] += 1; continue
        if same:
            agreed.append([r[0], r[1], r[2], r[3], 'high', 'two reviewers agree: ' + (r[5] if len(r) > 5 else '')]); c['agree'] += 1
        else:
            c['disagree'] += 1
    (E / f'{stem}.agreed.tsv').write_text(''.join('\t'.join(a) + '\n' for a in agreed), encoding='utf-8')
    print(dict(c), f'-> {stem}.agreed.tsv')
