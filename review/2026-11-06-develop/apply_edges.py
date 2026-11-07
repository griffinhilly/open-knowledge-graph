"""Purpose: apply high-confidence edge verdicts from edges/*.verdicts.tsv (and newtopics proposals) to topic frontmatter.
Applied automatically (confidence == high only):
  ADD a b hard|soft  -> add a to b's prerequisites (skipped if it would create a cycle, if a/b missing,
                        or if hard and a is staged above b -> judgment list)
  DROP a b           -> remove b from a's builds-toward
  REMOVE a b         -> remove a from b's prerequisites
  SOFTEN a b         -> a's type in b's prerequisites hard -> soft
Everything else (medium confidence, JUDGE, KEEP, NONE) goes to edges/judgment.tsv or is counted.
Files listed in --busy FILE (one path per line; batches being written right now) are deferred, not touched.
Ledger edges/applied.tsv records every applied change so reruns skip them.
Usage: python review/2026-11-06-develop/apply_edges.py [--apply] [--busy busy.txt] verdict files...
"""
import sys, re, pathlib, collections
import yaml
sys.path.insert(0, 'tools')
from parse_topic import parse_topic

RANK = {s: i for i, s in enumerate(['proto-formal', 'pre-formal', 'concrete-operations', 'abstract-reasoning', 'formal-systems', 'advanced', 'expert'])}
E = pathlib.Path('review/2026-11-06-develop/edges')
args = [a for a in sys.argv[1:]]
apply = '--apply' in args
busy = set()
if '--busy' in args:
    busy = {l.strip() for l in open(args[args.index('--busy') + 1]) if l.strip()}
files = [a for i, a in enumerate(args) if not a.startswith('--') and (i == 0 or args[i - 1] != '--busy')]

T, P = {}, {}
for f in pathlib.Path('domains').rglob('*.md'):
    if f.name.startswith('_'): continue
    r = parse_topic(f)
    if r and r[0]:
        T[r[0]['id']] = r[0]; P[r[0]['id']] = f
pre = {i: {(p['id'] if isinstance(p, dict) else p): (p.get('type', 'hard') if isinstance(p, dict) else 'hard') for p in (fm.get('prerequisites') or [])} for i, fm in T.items()}
bt = {i: list(fm.get('builds-toward') or []) for i, fm in T.items()}


def reaches(src, dst):
    """True if dst is an ancestor of src (src draws on dst transitively)."""
    seen, stack = set(), [src]
    while stack:
        n = stack.pop()
        if n == dst: return True
        if n in seen: continue
        seen.add(n); stack.extend(pre.get(n, {}))
    return False


ledger_path = E / 'applied.tsv'
done = set(ledger_path.read_text(encoding='utf-8').splitlines()) if ledger_path.exists() else set()
applied, judgment, deferred, skipped = [], [], [], collections.Counter()
touched = set()
for vf in files:
    for line in pathlib.Path(vf).read_text(encoding='utf-8').splitlines():
        parts = line.split('\t')
        if len(parts) < 5 or parts[0] not in ('ADD', 'DROP', 'REMOVE', 'SOFTEN', 'JUDGE', 'KEEP', 'NONE'):
            skipped['unparsed'] += 1; continue
        v, a, b, typ, conf = parts[:5]; reason = parts[5] if len(parts) > 5 else ''
        key = '\t'.join([v, a, b, typ])
        if key in done: skipped['already applied'] += 1; continue
        if v in ('KEEP', 'NONE'): skipped[v] += 1; continue
        if v == 'JUDGE' or conf != 'high':
            judgment.append(line); continue
        if a not in T or b not in T:
            skipped['unknown id'] += 1; judgment.append(line + '\t[unknown id]'); continue
        target = b if v in ('ADD', 'REMOVE', 'SOFTEN') else a
        if P[target].as_posix() in busy:
            deferred.append(line); continue
        if v == 'ADD':
            if a in pre[b]: skipped['already present'] += 1; continue
            if typ not in ('hard', 'soft'): typ = 'soft'
            if reaches(a, b): skipped['would cycle'] += 1; judgment.append(line + '\t[would create cycle]'); continue
            if typ == 'hard' and RANK.get(T[a].get('stage'), 4) > RANK.get(T[b].get('stage'), 4):
                judgment.append(line + '\t[hard prereq staged above successor]'); continue
            pre[b][a] = typ
        elif v == 'REMOVE':
            if a not in pre[b]: skipped['absent'] += 1; continue
            if len(pre[b]) == 1 and T[b].get('stage') not in ('pre-formal', 'proto-formal'):
                judgment.append(line + '	[would leave no prerequisites]'); continue
            del pre[b][a]
        elif v == 'SOFTEN':
            if pre[b].get(a) != 'hard': skipped['not hard'] += 1; continue
            pre[b][a] = 'soft'
        elif v == 'DROP':
            if b not in bt[a]: skipped['absent'] += 1; continue
            bt[a].remove(b)
        applied.append(key); touched.add(target)

BLOCK = {'prerequisites': re.compile(r'(?m)^prerequisites:[ \t]*(\[\])?\n((?:[ \t-].*\n)*)'),
         'builds-toward': re.compile(r'(?m)^builds-toward:[ \t]*(\[\])?\n((?:[ \t-].*\n)*)')}
if apply:
    for tid in touched:
        f = P[tid]; t = f.read_text(encoding='utf-8')
        end = t.find('\n---', 4)
        for field, rx in BLOCK.items():
            m = rx.search(t, 0, end)
            if field == 'prerequisites':
                body = ''.join(f'- id: {i}\n  type: {ty}\n' for i, ty in pre[tid].items())
            else:
                body = ''.join(f'- {i}\n' for i in bt[tid])
            new = f'{field}:\n{body}' if body else f'{field}: []\n'
            if m:
                t = t[:m.start()] + new + t[m.end():]
            elif body:
                end = t.find('\n---', 4)
                t = t[:end + 1] + new + t[end + 1:]
            end = t.find('\n---', 4)
        f.write_text(t, encoding='utf-8')
    (E / 'touched.txt').write_text(''.join(P[t].as_posix() + chr(10) for t in touched), encoding='utf-8')
    with open(ledger_path, 'a', encoding='utf-8') as fh:
        fh.write(''.join(k + '\n' for k in applied))
    with open(E / 'judgment.tsv', 'a', encoding='utf-8') as fh:
        fh.write(''.join(j + '\n' for j in judgment))
    (E / 'deferred.tsv').write_text(''.join(d + '\n' for d in deferred), encoding='utf-8')
print(f"{'applied' if apply else 'would apply'} {len(applied)} | to judgment {len(judgment)} | deferred (busy) {len(deferred)} | files {len(touched)}")
print('by verdict:', collections.Counter(k.split('\t')[0] for k in applied))
print('skipped:', dict(skipped))
