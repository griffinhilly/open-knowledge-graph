#!/usr/bin/env python3
"""Audit question types across the knowledge graph."""
import re, yaml, sys
from pathlib import Path
from collections import defaultdict

DOMAINS_DIR = Path(__file__).resolve().parent.parent / "domains"

stage_counts = defaultdict(lambda: defaultdict(int))
total_by_type = defaultdict(int)
sa_formal = defaultdict(int)

for f in sorted(DOMAINS_DIR.rglob("*.md")):
    text = f.read_text(encoding="utf-8")
    fm_match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not fm_match:
        continue
    try:
        fm = yaml.safe_load(fm_match.group(1))
    except Exception:
        continue
    if not isinstance(fm, dict):
        continue
    domain = fm.get("domain", "")
    stage = fm.get("stage", "")
    q_match = re.search(r"## Questions\s*\n```yaml\s*\n(.*?)\n```", text, re.DOTALL)
    if not q_match:
        continue
    try:
        questions = yaml.safe_load(q_match.group(1))
    except Exception:
        continue
    if not isinstance(questions, list):
        continue
    for q in questions:
        if not isinstance(q, dict):
            continue
        qtype = q.get("type", "unknown")
        stage_counts[stage][qtype] += 1
        total_by_type[qtype] += 1
        if qtype == "short-answer" and stage in ("formal-systems", "advanced", "expert"):
            sa_formal[domain] += 1

print("Question types total:")
for t in sorted(total_by_type.keys()):
    print(f"  {t}: {total_by_type[t]}")

print()
stages = ["pre-formal", "concrete-operations", "abstract-reasoning",
          "formal-systems", "advanced", "expert"]
print("Short-answer by stage:")
for s in stages:
    print(f"  {s}: {stage_counts[s].get('short-answer', 0)}")

print()
print("Short-answer formal+ by domain:")
for d in sorted(sa_formal.keys()):
    print(f"  {d}: {sa_formal[d]}")
print(f"  TOTAL formal+: {sum(sa_formal.values())}")
