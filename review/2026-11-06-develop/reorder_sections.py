"""Purpose: put topic body sections in canonical order (Core Idea, How It's Best Learned, Common Misconceptions,
Questions, Explainer) for files whose sections are all known but out of order. Usage: reorder_sections.py LISTFILE"""
import re, sys, pathlib
ORDER = ["Core Idea", "How It's Best Learned", "Common Misconceptions", "Questions", "Explainer"]
n = 0
for p in open(sys.argv[1], encoding='utf-8').read().split():
    f = pathlib.Path(p); t = f.read_text(encoding='utf-8')
    m = re.match(r'(---\n.*?\n---\n.*?)(?=^## )', t, re.S | re.M)
    if not m: continue
    head = m.group(1); parts = [x for x in re.split(r'(?m)^(?=## )', t[len(head):]) if x.strip()]
    keys = [x.split('\n', 1)[0][3:].strip() for x in parts]
    if any(k not in ORDER for k in keys) or len(set(keys)) != len(keys): continue
    if keys == sorted(keys, key=ORDER.index): continue
    parts.sort(key=lambda x: ORDER.index(x.split('\n', 1)[0][3:].strip()))
    f.write_text(head + ''.join(x.rstrip('\n') + '\n\n' for x in parts).rstrip('\n') + '\n', encoding='utf-8'); n += 1
print('reordered', n)
