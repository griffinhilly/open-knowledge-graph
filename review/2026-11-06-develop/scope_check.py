"""Purpose: deterministic scope check for writer/checker batches. For each file in the given batches,
compare the working copy with git HEAD and fail if anything outside the allowed change set moved:
  - frontmatter must be identical
  - Core Idea identical; Explainer identical unless needs has `ex`
  - existing question items keep every existing field value; only listed fields may be added
  - each needed section (how/mis) now exists, sections in canonical order
  - Questions YAML still parses
Usage: python review/2026-11-06-develop/scope_check.py L001 L002 ...   (exit 1 on any violation)
"""
import re, subprocess, sys, pathlib
import yaml
sys.path.insert(0, 'tools')
from parse_topic import parse_sections

ORDER = ["Core Idea", "How It's Best Learned", "Common Misconceptions", "Questions", "Explainer"]
B = pathlib.Path('review/2026-11-06-develop/batches')


def split(text):
    m = re.match(r'^---\n(.*?)\n---\n(.*)$', text.replace('\r\n', '\n'), re.S)
    return (m.group(1), m.group(2)) if m else (None, text)


def questions(body):
    m = re.search(r'^## Questions\s*\n(.*?)(?=^## |\Z)', body, re.M | re.S)
    if not m: return None
    f = re.search(r'```ya?ml[ \t]*\n(.*?)```', m.group(1), re.S)
    return yaml.safe_load(f.group(1)) if f else None


def check(path, needs):
    probs = []
    old = subprocess.run(['git', 'show', f'HEAD:{path}'], capture_output=True, text=True, encoding='utf-8').stdout
    new = pathlib.Path(path).read_text(encoding='utf-8')
    if old.replace('\r\n', '\n') == new.replace('\r\n', '\n'):
        return ['unchanged']
    fo, bo = split(old); fn, bn = split(new)
    if fo != fn: probs.append('frontmatter changed')
    so, sn = parse_sections(bo), parse_sections(bn)
    if so.get('Core Idea', '').strip() != sn.get('Core Idea', '').strip(): probs.append('Core Idea changed')
    if 'ex' not in needs and so.get('Explainer', '').strip() != sn.get('Explainer', '').strip(): probs.append('Explainer changed')
    for k, sec in (('how', "How It's Best Learned"), ('mis', 'Common Misconceptions')):
        if k in needs and not sn.get(sec, '').strip(): probs.append(f'missing {sec}')
        if k not in needs and so.get(sec, '').strip() != sn.get(sec, '').strip(): probs.append(f'{sec} changed')
    heads = [h for h in re.findall(r'^## (.+?)\s*$', bn, re.M) if h in ORDER]
    if heads != sorted(heads, key=ORDER.index): probs.append(f'section order {heads}')
    if len(heads) != len(set(heads)): probs.append('duplicate section')
    try:
        qo, qn = questions(bo), questions(bn)
    except yaml.YAMLError as e:
        return probs + [f'Questions YAML error: {str(e)[:80]}']
    allowed = {(int(x.split(':')[1]), x.split(':')[2]) for x in needs if x.startswith('q:')}
    if isinstance(qo, list) and isinstance(qn, list):
        if len(qo) != len(qn): probs.append('question count changed')
        for i, (a, b) in enumerate(zip(qo, qn)):
            if not (isinstance(a, dict) and isinstance(b, dict)): continue
            for k, v in a.items():
                if b.get(k) != v: probs.append(f'q{i}.{k} changed')
            for k in set(b) - set(a):
                if (i, k) not in allowed: probs.append(f'q{i}.{k} added unexpectedly')
        for i, k in allowed:
            if i < len(qn) and isinstance(qn[i], dict) and k not in qn[i]: probs.append(f'q{i}.{k} still missing')
    elif qo != qn:
        probs.append('Questions changed shape')
    return probs


ACCEPT = set()
_acc = pathlib.Path('review/2026-11-06-develop/scope_accepted.tsv')
if _acc.exists():
    ACCEPT = {tuple(l.split('	')[:2]) for l in _acc.read_text(encoding='utf-8').splitlines() if l.strip()}


OLDTEXT_OK = set()
_ob = pathlib.Path('review/2026-11-06-develop/oldtext_ok_batches.txt')
if _ob.exists():
    OLDTEXT_OK = {l.strip() for l in _ob.read_text(encoding='utf-8').splitlines() if l.strip()}


def main():
    bad = 0; total = 0; unchanged = 0
    for name in sys.argv[1:]:
        for line in (B / f'{name}.tsv').read_text(encoding='utf-8').splitlines():
            path, needs = line.split('\t'); needs = needs.split(',')
            total += 1
            p = check(path, needs)
            if p == ['unchanged']:
                unchanged += 1; print(f'{name} UNCHANGED {path}'); continue
            p = [x for x in p if (path, x) not in ACCEPT]
            if name in OLDTEXT_OK:  # checker fixed older text in this batch (reported); keep structural checks
                p = [x for x in p if not (x.endswith(' changed') and x != 'question count changed' and x != 'frontmatter changed')]
            if p:
                bad += 1; print(f'{name} FAIL {path}: {"; ".join(p)}')
    print(f'files {total}, violations {bad}, unchanged {unchanged}')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
