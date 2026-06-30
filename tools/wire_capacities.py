#!/usr/bin/env python3
"""Wire pre-formal root topics to the origin-layer capacities (deterministic).

purpose : assign kind:capacity prerequisites to pre-formal roots via a fixed tag/course -> capacity
          mapping, so the assignment is reproducible (latent-vs-deterministic doctrine).
inputs  : domains/<PILOT_COURSES>/*.md (kind:topic roots); the 10 capacity nodes in
          domains/developmental-origins/precursor-capacities/
outputs : (--apply) edits each matched root's `prerequisites:` block in place, idempotently;
          (--report) prints the anti-collapse gate (signature distribution + assertions)
last_run: 2026-06-30 (A' full floor — 307/314 wired; title+tags-only match + COURSE_DEFAULTS + reconcile)

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

DISCERNMENT = "discernment-same-different"

# Pilot clusters: the cleanest-tagged courses (spec sec 0.3). Wire the remainder later.
# Target the WHOLE pre-formal floor (set in collect_targets via stage, not a course allowlist).
# (Was PILOT_COURSES = kindergarten + feelings for the 2026-06-26 pilot; finishing the floor now.)

# Deterministic rules: (regex over course+title+tags) -> [(capacity_id, edge_type)].
# A root is wired only if >=1 rule matches; DISCERNMENT is then added as a soft floor. Most roots
# carry >=1 capacity besides discrimination; a small minority (e.g. "Same and Different Sounds") are
# legitimately discrimination-primary — the anti-collapse gate allows that as a bounded share.
RULES = [
    # core-number — quantity & arithmetic
    (r"\b(count|counting|counts|cardinalit|subitiz|numeral|numerals|number|numbers|"
     r"one-to-one|tally|zero|add|adds|adding|addition|subtract|subtraction|sum|sums|"
     r"doubles|fact famil|fact-famil|fact family|fact families|number bond|place value|"
     r"tens and ones|ten frame|equal group|part-part|part-whole|missing addend|addend|addends|"
     r"even and odd|halv|quarter|"
     r"fraction|skip count|skip-count|near double|making ten|making 10|number line)\b",
     [("core-number", "hard")]),
    # grade-seriation — ordering, gradients, comparison, measurement, time, sequence
    (r"\b(compar|more|less|fewer|greater|equal|long|longer|short|shorter|heav|"
     r"light|lighter|tall|taller|order|ordering|ordinal|seriat|grade|grading|"
     r"pattern|patterns|measur|length|capacity|weight|mass|time|clock|hour|"
     r"calendar|day|days|week|elapsed|season|seasons|fast|slow|high|low|loud|"
     r"quiet|pitch|rhythm|temperature)\b",
     [("grade-seriation", "hard")]),
    # core-space — shape, geometry, spatial, body map, art-making
    (r"\b(shape|shapes|2d|3d|circle|square|triangle|rectangle|geometr|spatial|"
     r"position|above|below|beside|next to|under|left|right|body part|body parts|"
     r"major body|line in art|build|building|construct|weav|weaving|threading|"
     r"draw|drawing|paint|painting|scribbl|collage|print|printing|handprint|"
     r"handprints|footprint|footprints|stamp|mark-making|cutting|clay|"
     r"landform|landforms|geography|mountains|valleys|plains)\b",
     [("core-space", "hard")]),
    # classification-sorting — grouping, categories, types, data
    (r"\b(sort|sorting|classif|categor|attribute|group|groups|data|graph|graphs|"
     r"tally chart|instrument famil|animal group|living|nonliving|alive|weather|"
     r"solid, liquid|seasons|kinds|types|five senses|senses)\b",
     [("classification-sorting", "hard")]),
    # naming-symbol-reference — naming, labels, opposites (binaries), print symbols
    (r"\b(naming|label|color|colors|colours|opposite|letter|letters|word|words|"
     r"phonic|phonics|phonem|phoneme|phonemic|phonolog|phonological|blending|"
     r"segmenting|print|sight|vocab|rhyme|sentence|spoken|alphabet|"
     r"day and night|sunny|cloudy|rainy|snowy|hot|cold|high and low|loud and quiet|"
     r"fast and slow|long and short)\b",
     [("naming-symbol-reference", "hard")]),
    # symbolic-function — representation, story, pretend, print meaning
    (r"\b(story|stories|read|reading|book|books|character|characters|narrative|"
     r"retell|retelling|illustration|author|nursery|pretend|imagin|puppet|portrait|"
     r"make-believe|making faces|decode|decoding|listening comprehension|"
     r"storytelling|sight word|sound story)\b",
     [("symbolic-function", "hard")]),
    # core-social — emotion, people, social interaction
    (r"\b(feel|feels|feeling|feelings|emotion|emotions|angry|happy|sad|scared|surpris|"
     r"proud|calm|frustrat|patien|kind|empath|trust|safe|upset|mad|call and response|"
     r"taking turns|sharing|asking for help|families|family)\b",
     [("core-social", "hard")]),
    # core-agents — living things, animacy, goal-directed action
    (r"\b(living|nonliving|alive|animal|animals|plant|plants|seed|seeds|germinat|"
     r"grow|grows|growth|habitat|needs of living|respond|responds|responding|response|"
     r"how animals move|movement does not mean)\b",
     [("core-agents", "hard")]),
    # auditory discrimination — sound/music (discrimination is the PRIMARY capacity here)
    (r"\b(music|musical|sound|sounds|song|songs|sing|singing|listen|listening|echo|"
     r"echoing|silence|lullab|instrument|instruments)\b",
     [("discernment-same-different", "hard")]),
    # tactile/sensory discrimination — texture & touch (discrimination is PRIMARY here)
    (r"\b(texture|textures|tactile|rough|smooth)\b",
     [("discernment-same-different", "hard")]),
    # core-objects — matter, materials, object properties
    (r"\b(solid|liquid|gas|matter|material|materials)\b",
     [("core-objects", "soft")]),
]

# The 10 origin-layer capacity ids (used by the reconcile writer to know which prereqs it owns).
CAP_IDS = {"core-objects", "core-agents", "core-number", "core-space", "core-social",
           "discernment-same-different", "grade-seriation", "naming-symbol-reference",
           "classification-sorting", "symbolic-function"}

# Curated course-level defaults — applied to EVERY topic in a *content-homogeneous* course where the
# whole course genuinely presupposes a capacity. This is a DELIBERATE choice, not an accidental
# course-name regex hit (the rules below match title+tags only, never the course name — see the A'
# decision, plans/origin-layer-spec.md sec 0.6). Only courses where the default is true of all members.
COURSE_DEFAULTS = {
    "feelings-and-self-awareness": [("core-social", "hard"), ("symbolic-function", "hard")],  # spec sec 4 example
    "musical-play-and-listening": [("discernment-same-different", "hard")],  # auditory discrimination
    "first-stories-and-read-alouds": [("symbolic-function", "hard")],  # every topic is narrative/symbolic
}


def capacities_for(course, title, tags):
    # Haystack is TITLE + TAGS only — NOT course. Matching on the course name blanket-stamped every
    # topic in a course (e.g. "living-things" -> core-agents on "Major Body Parts"). Homogeneous-course
    # signal is restored deliberately via COURSE_DEFAULTS. (A' fix; dialectic 2026-06-29.)
    hay = " ".join([title or "", " ".join(tags or [])]).lower()
    caps = {}  # id -> type (hard wins over soft)
    matched = False
    for pat, cap_list in RULES:
        if re.search(pat, hay):
            matched = True
            for cid, ctype in cap_list:
                if caps.get(cid) != "hard":
                    caps[cid] = ctype
    for cid, ctype in COURSE_DEFAULTS.get(course, []):  # curated homogeneous-course defaults
        matched = True
        if caps.get(cid) != "hard":
            caps[cid] = ctype
    if not matched:
        return {}
    # Homonym guards — strip a capacity a broad token mis-fired on (dialectic-caught false positives).
    if "fact famil" in hay or "instrument famil" in hay:   # "families" = groups/relations, not social
        caps.pop("core-social", None)
    if "vocabulary build" in hay or "vocab build" in hay:  # building vocabulary is not spatial construction
        caps.pop("core-space", None)
    if "quiet time" in hay:                                 # rest/self-regulation, not a loudness gradient
        caps.pop("grade-seriation", None)
    if "subitiz" in hay:                                    # instant small-set apprehension, not sorting
        caps.pop("classification-sorting", None)
    caps.setdefault(DISCERNMENT, "soft")  # near-universal floor — only on already-matched topics
    return caps


def reconcile_prereqs(text, target_caps):
    """Rewrite the frontmatter `prerequisites:` block so its CAPACITY prereqs are EXACTLY target_caps,
    preserving all non-capacity (topic) prereqs in their original order. Add AND remove — this is the
    de-sticky reconcile that replaces the old add-only inserter. Returns (new_text, changed_bool)."""
    m = re.match(r"^(---\s*\n)(.*?)(\n---\s*\n)(.*)$", text, re.DOTALL)
    if not m:
        return text, False
    head, fm, sep, body = m.groups()
    lines = fm.split("\n")
    pidx = next((i for i, ln in enumerate(lines) if re.match(r"^prerequisites:", ln)), None)
    if pidx is None:
        return text, False

    entries = []  # (id, type) in file order
    inline_empty = bool(re.match(r"^prerequisites:\s*\[\]\s*$", lines[pidx]))
    j = pidx + 1
    if not inline_empty:
        while j < len(lines):
            ln = lines[j]
            mid = re.match(r"^- id:\s*(\S+)", ln)
            if mid:
                cid, ctype = mid.group(1), "hard"
                if j + 1 < len(lines):
                    tm = re.match(r"^\s+type:\s*(\S+)", lines[j + 1])
                    if tm:
                        ctype = tm.group(1)
                        entries.append((cid, ctype)); j += 2; continue
                entries.append((cid, ctype)); j += 1; continue
            if ln.startswith((" ", "\t")) and ln.strip():
                j += 1; continue          # stray indented continuation — skip
            break                          # blank line or next top-level key ends the block
    block_end = j

    non_cap = [(c, t) for c, t in entries if c not in CAP_IDS]
    cur_caps = {c: t for c, t in entries if c in CAP_IDS}
    if cur_caps == dict(target_caps):
        return text, False  # capacity prereqs already exact — no churn

    tgt = sorted(target_caps.items(), key=lambda kv: (kv[1] != "hard", kv[0]))
    new_entries = non_cap + tgt
    if new_entries:
        new_block = ["prerequisites:"]
        for c, t in new_entries:
            new_block += [f"- id: {c}", f"  type: {t}"]
    else:
        new_block = ["prerequisites: []"]
    new_fm = "\n".join(lines[:pidx] + new_block + lines[block_end:])
    return head + new_fm + sep + body, True


def collect_all_preformal():
    """Every pre-formal topic with its TARGET capacity set (may be empty). Empty-target topics are
    included so the reconcile can REMOVE stale capacity prereqs from now-unmatched topics."""
    rows = []
    for fp in sorted(DOMAINS_DIR.rglob("*.md")):
        if fp.name.startswith("_"):
            continue
        data, _ = _parse(fp)
        if not data or data.get("kind") == "capacity":
            continue
        if data.get("stage") != "pre-formal":
            continue
        caps = capacities_for(data.get("course"), data.get("title"), data.get("tags"))
        rows.append((fp, data, caps))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry-run)")
    ap.add_argument("--report", action="store_true", help="anti-collapse gate report only")
    args = ap.parse_args()

    all_rows = collect_all_preformal()
    targets = [(fp, data, caps) for fp, data, caps in all_rows if caps]  # matched (>=1 capacity)
    unmatched = [(fp, data) for fp, data, caps in all_rows if not caps]
    signatures = Counter()
    for fp, data, caps in targets:
        sig = tuple(sorted(caps.keys()))
        signatures[sig] += 1

    n = len(targets)
    distinct = len(signatures)
    top = signatures.most_common(1)[0][1] if signatures else 0
    top_frac = top / n if n else 0

    print(f"Pre-formal topics: {len(all_rows)}  matched: {n}  unmatched: {len(unmatched)}")
    print(f"Distinct capacity-prereq signatures: {distinct}")
    print(f"Largest signature share: {top}/{n} = {top_frac:.0%}")
    print("\nSignature distribution:")
    for sig, c in signatures.most_common():
        short = ", ".join(s.replace("discernment-same-different", "disc")
                          .replace("-", "·") for s in sig)
        print(f"  {c:3d}  {short}")

    # Show members of the dominant signature (sanity-check for under-wiring)
    top_sig = signatures.most_common(1)[0][0] if signatures else ()
    print(f"\nMembers of dominant signature {tuple('disc' if s==DISCERNMENT else s for s in top_sig)}:")
    for fp, data, caps in targets:
        if tuple(sorted(caps.keys())) == top_sig:
            print(f"  - {data.get('id')}")

    # Anti-collapse gate (spec sec 0.4a). The degenerate case is "the layer is just discrimination";
    # we catch it by bounding the discrimination-ONLY share, which allows legitimately auditory-
    # discrimination roots (e.g. "Same and Different Sounds") without forcing a spurious 2nd capacity.
    disc_only = sum(1 for _, _, caps in targets if set(caps) == {DISCERNMENT})
    disc_only_frac = disc_only / n if n else 1
    gate_ok = n > 0 and distinct >= 4 and top_frac <= 0.40 and disc_only_frac <= 0.20
    print("\nANTI-COLLAPSE GATE:")
    print(f"  >=4 distinct signatures   : {'OK' if distinct >= 4 else 'FAIL'} ({distinct})")
    print(f"  no signature >40%         : {'OK' if top_frac <= 0.40 else 'FAIL'} ({top_frac:.0%})")
    print(f"  discrimination-only <=20% : {'OK' if disc_only_frac <= 0.20 else 'FAIL'} ({disc_only_frac:.0%}, {disc_only}/{n})")
    print(f"  => {'PASS' if gate_ok else 'FAIL'}")

    if unmatched:
        print(f"\nUnmatched pre-formal topics ({len(unmatched)}) — carry no capacity prereq:")
        for fp, data in sorted(unmatched, key=lambda x: (x[1].get('course') or '', x[1].get('id') or '')):
            print(f"  [{data.get('course')}] {data.get('id')}")

    if args.report:
        return 0 if gate_ok else 1

    if not gate_ok:
        print("\nGate FAILED — not applying. (Fall back to spec runner-up iii if this persists.)")
        return 1

    if not args.apply:
        print("\n(dry-run; re-run with --apply to reconcile)")
        return 0

    # Reconcile EVERY pre-formal topic to its target (add missing caps, remove stale caps).
    changed = 0
    for fp, data, caps in all_rows:
        text = fp.read_text(encoding="utf-8")
        new_text, did = reconcile_prereqs(text, caps)
        if did:
            fp.write_text(new_text, encoding="utf-8")
            changed += 1
    print(f"\nApplied: reconciled {changed} files (of {len(all_rows)} pre-formal topics).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
