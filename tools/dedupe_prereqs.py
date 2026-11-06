"""Purpose: merge duplicate prerequisite ids in topic frontmatter (keeps one entry; hard wins over soft).
Rewrites only the `prerequisites:` block of affected files. Usage: python tools/dedupe_prereqs.py [--apply]
last_run: 2026-11-06"""
import pathlib, re, sys
import yaml
BLOCK = re.compile(r"(?m)^prerequisites:[ \t]*\n((?:[ \t-].*\n)*)")
n = 0
for f in sorted(pathlib.Path("domains").rglob("*.md")):
    if f.name.startswith("_"): continue
    t = f.read_text(encoding="utf-8")
    end = t.find("\n---", 4)
    m = BLOCK.search(t, 0, end)
    if not m: continue
    items = yaml.safe_load("x:\n" + m.group(1))["x"] or []
    seen = {}
    for it in items:
        pid, typ = (it.get("id"), it.get("type", "hard")) if isinstance(it, dict) else (it, "hard")
        if pid in seen:
            if typ == "hard": seen[pid] = "hard"
        else:
            seen[pid] = typ
    if len(seen) == len(items): continue
    n += 1
    new = "".join(f"- id: {pid}\n  type: {typ}\n" for pid, typ in seen.items())
    if "--apply" in sys.argv:
        f.write_text(t[:m.start(1)] + new + t[m.end(1):], encoding="utf-8")
print(("deduped" if "--apply" in sys.argv else "would dedupe"), n, "files")
