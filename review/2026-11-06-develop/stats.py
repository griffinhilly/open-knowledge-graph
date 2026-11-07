"""Purpose: tally fact-check results from batches/*.check.tsv, flagfix/*.tsv, newtopics/*.check.tsv. Usage: python stats.py"""
import pathlib, collections
D = pathlib.Path(__file__).parent
oldfix = [0]; claims = wrong = parts = 0; verd = collections.Counter(); per = {}
for f in sorted((D / 'batches').glob('*.check.tsv')):
    c = w = 0
    for l in f.read_text(encoding='utf-8').splitlines():
        p = l.split('\t')
        if len(p) < 5 or not p[2].strip().isdigit(): continue
        if p[1].strip().startswith('old'): oldfix[0] += 1; continue
        c += int(p[2]); w += int(p[3]) if p[3].strip().isdigit() else 0; parts += 1; verd[p[4].strip()] += 1
    per[f.name.split('.')[0]] = (c, w); claims += c; wrong += w
print(f'lesson batches checked: {len(per)} | parts {parts} | claims {claims} | wrong {wrong} ({100*wrong/max(claims,1):.1f}%) | verdicts {dict(verd)}')
print('checker fixes to older text (old: lines):', oldfix[0])
print('  per batch:', ' '.join(f'{b}:{w}/{c}' for b, (c, w) in per.items()))
ff = collections.Counter()
for f in (D / 'flagfix').glob('*.tsv'):
    for l in f.read_text(encoding='utf-8').splitlines():
        p = l.split('\t')
        if len(p) >= 4: ff[p[2].strip()] += 1
print('older-text flags verified:', dict(ff))
nc = collections.Counter(); nclaims = nwrong = 0
for f in (D / 'newtopics').glob('*.check.tsv'):
    for l in f.read_text(encoding='utf-8').splitlines():
        p = l.split('\t')
        if len(p) >= 4 and p[1].strip().isdigit():
            nclaims += int(p[1]); nwrong += int(p[2]) if p[2].strip().isdigit() else 0; nc[p[3].split()[0] if p[3].strip() else '?'] += 1
print(f'new topics checked: {sum(nc.values())} | claims {nclaims} | wrong {nwrong} | verdicts {dict(nc)}')
