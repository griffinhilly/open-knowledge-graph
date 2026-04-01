#!/usr/bin/env python3
"""Audit hedged T/F false questions to find ones where the hedge makes the statement true.

Strategy: Analyze explanation text for signals that the core claim IS true
but was marked false only because the original used absolute language.

Outputs:
  - FLIP: questions where the hedged statement is probably true (answer should be true)
  - REWRITE: questions where the hedge makes the answer ambiguous
  - OK: questions that are still clearly false despite the hedge
"""
import re
import sys
import yaml
from pathlib import Path
from collections import Counter

DOMAINS = Path("domains")
HEDGE_WORDS = ["primarily", "typically", "generally", "usually", "mostly",
               "often", "frequently", "commonly", "tends to", "tend to"]

# Patterns in explanations that suggest the hedged statement IS true
# (the original was false only because of absolute language)
CONFIRMS_PATTERN = [
    # Explanation acknowledges the general truth but corrects the absolute
    r"while (?:it is true|this is (?:largely |broadly )?true|it's true|the statement is (?:largely |broadly )?correct)",
    r"(?:it is|this is) (?:largely|broadly|mostly|generally|typically|often) (?:true|correct|accurate)",
    r"although .{5,60} (?:is|are) (?:true|correct|common|typical)",
    r"the (?:statement|claim) (?:is|would be) (?:largely|mostly|broadly) (?:true|correct|accurate)",
    r"(?:does|do|is|are) (?:indeed|in fact) .{3,40}(?:, but|; however)",
    r"while .{5,60} (?:does|do|is|are|can) .{3,40}(?:, it|; however|, the|, there)",
    # "not only/exclusively/solely" — implies it IS the primary thing
    r"not (?:only|exclusively|solely|just|merely|simply) .{3,60}(?:but also|; it also|, it also)",
    # "more than just" — implies it IS that thing, plus more
    r"more than (?:just|merely|simply)",
]

# Patterns that suggest the statement is still clearly false
REFUTES_PATTERN = [
    r"(?:the opposite|the reverse|the contrary) is (?:true|the case)",
    r"(?:in fact|actually|rather),? .{3,40} (?:is not|are not|does not|do not|isn't|aren't|doesn't|don't)",
    r"this is (?:false|incorrect|wrong|misleading|a (?:common )?misconception)",
    r"(?:is|are) (?:fundamentally|completely|entirely|wholly) (?:wrong|false|incorrect|mistaken)",
    r"has nothing to do with",
    r"(?:the|this) (?:claim|statement|assertion) (?:reverses|inverts|confuses|conflates|misidentifies)",
]

COMPILED_CONFIRMS = [re.compile(p, re.IGNORECASE) for p in CONFIRMS_PATTERN]
COMPILED_REFUTES = [re.compile(p, re.IGNORECASE) for p in REFUTES_PATTERN]


def classify_question(question_text, explanation_text):
    """Classify whether the hedged T/F false question is still false or now true."""
    expl_lower = explanation_text.lower() if explanation_text else ""

    confirm_score = sum(1 for p in COMPILED_CONFIRMS if p.search(expl_lower))
    refute_score = sum(1 for p in COMPILED_REFUTES if p.search(expl_lower))

    if refute_score > 0 and confirm_score == 0:
        return "OK"  # Clearly still false
    elif confirm_score > 0 and refute_score == 0:
        return "FLIP"  # Hedge makes it true
    elif confirm_score > refute_score:
        return "FLIP"
    elif confirm_score > 0 and refute_score > 0:
        return "REWRITE"  # Ambiguous
    else:
        return "OK"  # No strong signal either way — likely still false


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Apply FLIP fixes (change answer to true)")
    parser.add_argument("--verbose", action="store_true", help="Show all flagged questions")
    args = parser.parse_args()

    results = {"OK": [], "FLIP": [], "REWRITE": []}
    hedge_stats = Counter()

    for md in sorted(DOMAINS.rglob("*.md")):
        if md.name.startswith("_"):
            continue
        text = md.read_text(encoding="utf-8")
        match = re.search(r"```yaml\n(.*?)```", text, re.DOTALL)
        if not match:
            continue
        try:
            questions = yaml.safe_load(match.group(1))
        except Exception:
            continue
        if not questions:
            continue

        yaml_block = match.group(1)
        modified = False

        for q in questions:
            if not isinstance(q, dict):
                continue
            if q.get("type") != "true-false" or q.get("answer") is not False:
                continue
            stmt = q.get("question", "")
            expl = q.get("explanation", "")
            lower = stmt.lower()

            found_hedge = None
            for h in HEDGE_WORDS:
                if h in lower:
                    found_hedge = h
                    break
            if not found_hedge:
                continue

            hedge_stats[found_hedge] += 1
            classification = classify_question(stmt, expl)
            results[classification].append({
                "topic": md.stem,
                "hedge": found_hedge,
                "question": stmt[:120],
                "explanation": expl[:120] if expl else "",
                "file": str(md),
            })

            if classification == "FLIP" and args.apply:
                # Change answer from false to true in the yaml block
                old_entry = f'answer: false'
                # We need to find this specific question's answer line
                # Use the question text as anchor
                q_escaped = re.escape(stmt[:60])
                pattern = rf'({q_escaped}.*?answer: )false'
                new_yaml = re.sub(pattern, r'\1true', yaml_block, count=1, flags=re.DOTALL)
                if new_yaml != yaml_block:
                    text = text.replace(yaml_block, new_yaml, 1)
                    yaml_block = new_yaml
                    modified = True

        if modified and args.apply:
            md.write_text(text, encoding="utf-8")

    # Report
    print(f"Total hedged T/F false questions analyzed: {sum(len(v) for v in results.values())}")
    print(f"  OK (still false):  {len(results['OK'])}")
    print(f"  FLIP (now true):   {len(results['FLIP'])}")
    print(f"  REWRITE (ambiguous): {len(results['REWRITE'])}")
    print()
    print("By hedge word:")
    for word, count in hedge_stats.most_common():
        print(f"  {word}: {count}")

    if args.verbose or not args.apply:
        if results["FLIP"]:
            print(f"\n--- FLIP candidates ({len(results['FLIP'])}) ---")
            for r in results["FLIP"][:50]:
                print(f"  [{r['topic']}] ({r['hedge']})")
                print(f"    Q: {r['question']}")
                print(f"    E: {r['explanation']}")
                print()

        if results["REWRITE"]:
            print(f"\n--- REWRITE candidates ({len(results['REWRITE'])}) ---")
            for r in results["REWRITE"][:20]:
                print(f"  [{r['topic']}] ({r['hedge']})")
                print(f"    Q: {r['question']}")
                print()

    if args.apply:
        print(f"\nApplied {len(results['FLIP'])} answer flips (false -> true)")


if __name__ == "__main__":
    main()
