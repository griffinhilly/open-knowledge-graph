#!/usr/bin/env python3
"""Wire pre-formal root topics to the origin-layer capacities (deterministic).

purpose : assign kind:capacity prerequisites to pre-formal roots via a fixed tag/course -> capacity
          mapping, so the assignment is reproducible (latent-vs-deterministic doctrine).
inputs  : domains/<PILOT_COURSES>/*.md (kind:topic roots); the 10 capacity nodes in
          domains/developmental-origins/precursor-capacities/
outputs : (--apply) edits each matched root's `prerequisites:` block in place, idempotently;
          (--report) prints the anti-collapse gate (signature distribution + assertions)
last_run: 2026-06-26 (pilot)

Spec: plans/origin-layer-spec.md sec 0.3 (pilot scope) + sec 0.4a (anti-collapse gate) + sec 4 (rules).
"""
import argparse
import re
import sys
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "domains"
sys.path.insert(0, str(ROOT / "tools"))
from parse_topic import parse_topic as _parse

DISCRIMINATION = "discrimination-same-different"

# Pilot clusters: the cleanest-tagged courses (spec sec 0.3). Wire the remainder later.
PILOT_COURSES = {"kindergarten", "feelings-and-self-awareness"}

# Deterministic rules: (regex over course+title+tags) -> [(capacity_id, edge_type)].
# A root is wired only if >=1 SPECIFIC rule matches; DISCRIMINATION is then added as a soft,
# near-universal floor (so every wired root also carries >=1 capacity != discrimination — anti-collapse).
RULES = [
    (r"\b(count|counting|cardinalit|subitiz|numeral|number|one-to-one|tally|zero)\b",
     [("core-number", "hard")]),
    (r"\b(compar|more|less|fewer|greater|equal|longer|shorter|heav|light|tall|"
     r"order|ordinal|seriat|grade|grading|pattern)\b",
     [("grade-seriation", "hard")]),
    (r"\b(shape|2d|3d|circle|square|triangle|rectangle|geometr|spatial|"
     r"position|above|below|beside|next to|under)\b",
     [("core-space", "hard")]),
    (r"\b(sort|sorting|classif|categor|attribute|group)\b",
     [("classification-sorting", "hard")]),
    (r"\b(feel|feels|feeling|feelings|emotion|emotions|angry|happy|sad|scared|surpris|proud|calm|"
     r"frustrat|patien|kind|empath|trust|safe|upset|mad)\b",
     [("core-social", "hard"), ("symbolic-function", "hard")]),
    (r"\b(story|stories|read|letter|word|phonic|phonem|phonolog|print|"
     r"naming|vocab|label|rhyme|spoken|listening|sentence|sight)\b",
     [("naming-symbol-reference", "hard"), ("symbolic-function", "soft")]),
]


def capacities_for(course, title, tags):
    hay = " ".join([course or "", title or "", " ".join(tags or [])]).lower()
    caps = {}  # id -> type (hard wins over soft)
    matched_specific = False
    for pat, cap_list in RULES:
        if re.search(pat, hay):
            matched_specific = True
            for cid, ctype in cap_list:
                if caps.get(cid) != "hard":
                    caps[cid] = ctype
    if not matched_specific:
        return {}
    caps.setdefault(DISCRIMINATION, "soft")  # floor — only on already-matched roots
    return caps


def insert_prereqs(text, caps):
    """Insert capacity prereqs into the frontmatter `prerequisites:` block, idempotently.

    caps: dict {id: type}. Returns (new_text, added_list)."""
    m = re.match(r"^(---\s*\n)(.*?)(\n---\s*\n)(.*)$", text, re.DOTALL)
    if not m:
        return text, []
    head, fm, sep, body = m.groups()
    present = set(re.findall(r"^- id:\s*(\S+)", fm, re.MULTILINE))
    to_add = [(cid, ctype) for cid, ctype in caps.items() if cid not in present]
    if not to_add:
        return text, []
    entries = "".join(f"- id: {cid}\n  type: {ctype}\n" for cid, ctype in to_add)
    if re.search(r"^prerequisites:\s*\[\]\s*$", fm, re.MULTILINE):
        fm_new = re.sub(r"^prerequisites:\s*\[\]\s*$", "prerequisites:\n" + entries.rstrip(),
                        fm, count=1, flags=re.MULTILINE)
    elif re.search(r"^prerequisites:\s*$", fm, re.MULTILINE):
        fm_new = re.sub(r"^(prerequisites:\s*\n)", r"\1" + entries, fm, count=1, flags=re.MULTILINE)
    else:
        return text, []  # unexpected shape — skip, report
    return head + fm_new + sep + body, [c for c, _ in to_add]


def collect_targets():
    targets = []
    for fp in sorted(DOMAINS_DIR.rglob("*.md")):
        if fp.name.startswith("_"):
            continue
        data, _ = _parse(fp)
        if not data or data.get("kind") == "capacity":
            continue
        if data.get("course") not in PILOT_COURSES:
            continue
        caps = capacities_for(data.get("course"), data.get("title"), data.get("tags"))
        if caps:
            targets.append((fp, data, caps))
    return targets


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry-run)")
    ap.add_argument("--report", action="store_true", help="anti-collapse gate report only")
    args = ap.parse_args()

    targets = collect_targets()
    signatures = Counter()
    for fp, data, caps in targets:
        sig = tuple(sorted(caps.keys()))
        signatures[sig] += 1

    n = len(targets)
    distinct = len(signatures)
    top = signatures.most_common(1)[0][1] if signatures else 0
    top_frac = top / n if n else 0

    print(f"Pilot roots matched: {n}")
    print(f"Distinct capacity-prereq signatures: {distinct}")
    print(f"Largest signature share: {top}/{n} = {top_frac:.0%}")
    print("\nSignature distribution:")
    for sig, c in signatures.most_common():
        short = ", ".join(s.replace("discrimination-same-different", "disc")
                          .replace("-", "·") for s in sig)
        print(f"  {c:3d}  {short}")

    # Show members of the dominant signature (sanity-check for under-wiring)
    top_sig = signatures.most_common(1)[0][0] if signatures else ()
    print(f"\nMembers of dominant signature {tuple('disc' if s==DISCRIMINATION else s for s in top_sig)}:")
    for fp, data, caps in targets:
        if tuple(sorted(caps.keys())) == top_sig:
            print(f"  - {data.get('id')}")

    # Anti-collapse gate (spec sec 0.4a)
    every_has_specific = all(set(caps) - {DISCRIMINATION} for _, _, caps in targets)
    gate_ok = n > 0 and distinct >= 4 and top_frac <= 0.40 and every_has_specific
    print("\nANTI-COLLAPSE GATE:")
    print(f"  >=4 distinct signatures : {'OK' if distinct >= 4 else 'FAIL'} ({distinct})")
    print(f"  no signature >40%       : {'OK' if top_frac <= 0.40 else 'FAIL'} ({top_frac:.0%})")
    print(f"  every root >=1 non-disc : {'OK' if every_has_specific else 'FAIL'}")
    print(f"  => {'PASS' if gate_ok else 'FAIL'}")

    if args.report:
        return 0 if gate_ok else 1

    if not gate_ok:
        print("\nGate FAILED — not applying. (Fall back to spec runner-up iii if this persists.)")
        return 1

    if not args.apply:
        print("\n(dry-run; re-run with --apply to write)")
        return 0

    changed = 0
    for fp, data, caps in targets:
        text = fp.read_text(encoding="utf-8")
        new_text, added = insert_prereqs(text, caps)
        if added:
            fp.write_text(new_text, encoding="utf-8")
            changed += 1
    print(f"\nApplied: wired {changed} root files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
