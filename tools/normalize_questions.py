"""Purpose: repair malformed ## Questions blocks into the schema format (meta/schema.md "Questions Format").
Mechanical fixes only — never invents content:
  - top-level dict {multiple-choice: [...], true-false: [...]} -> flat list with `type` set
  - YAML list with no ```yaml fence -> fenced
  - key aliases: statement -> question, correct_answer / correct -> answer
  - type aliases: mc/tf/sa -> multiple-choice/true-false/short-answer; missing type inferred
    (options -> multiple-choice, boolean or "True"/"False" answer -> true-false, else short-answer)
  - true-false answers given as strings -> booleans; MC answers given as a letter or the option text -> index
Items still missing `answer` or `explanation` afterwards are listed (they need written content).
Inputs: domains/**/*.md.  Outputs: rewrites only files it changes (with --apply); prints a summary.
last_run: 2026-11-06
Usage: python tools/normalize_questions.py [--apply] [--list-remaining FILE]
"""
import pathlib, re, sys
import yaml

TYPE_ALIAS = {"mc": "multiple-choice", "multiple_choice": "multiple-choice", "multiplechoice": "multiple-choice",
              "tf": "true-false", "true_false": "true-false", "truefalse": "true-false", "true/false": "true-false",
              "sa": "short-answer", "short_answer": "short-answer", "shortanswer": "short-answer"}
TYPE_KEYS = {"multiple-choice", "true-false", "short-answer"}
KEY_ORDER = ["question", "type", "options", "answer", "explanation"]
SECTION_RE = re.compile(r"(^## Questions[ \t]*\n)(.*?)(?=^## |\Z)", re.M | re.S)
FENCE_RE = re.compile(r"```ya?ml[ \t]*\n(.*?)```", re.S)


def fix_item(it, forced_type=None):
    it = dict(it)
    if "question" not in it and "statement" in it:
        it["question"] = it.pop("statement")
    for alias in ("correct_answer", "correct"):
        if "answer" not in it and alias in it:
            it["answer"] = it.pop(alias)
    t = forced_type or it.get("type")
    if isinstance(t, str):
        t = TYPE_ALIAS.get(t.strip().lower(), t.strip().lower())
    ans = it.get("answer")
    if t not in TYPE_KEYS:
        if "options" in it:
            t = "multiple-choice"
        elif isinstance(ans, bool) or (isinstance(ans, str) and ans.strip().lower() in ("true", "false")):
            t = "true-false"
        else:
            t = "short-answer"
    it["type"] = t
    if t == "true-false" and isinstance(ans, str) and ans.strip().lower() in ("true", "false"):
        it["answer"] = ans.strip().lower() == "true"
    if t == "multiple-choice" and isinstance(ans, str) and isinstance(it.get("options"), list):
        opts = [str(o) for o in it["options"]]
        a = ans.strip()
        if len(a) == 1 and a.upper() in "ABCDE" and "ABCDE".index(a.upper()) < len(opts):
            it["answer"] = "ABCDE".index(a.upper())
        elif a in opts:
            it["answer"] = opts.index(a)
        elif a.isdigit():
            it["answer"] = int(a)
    ordered = {k: it[k] for k in KEY_ORDER if k in it}
    ordered.update({k: v for k, v in it.items() if k not in ordered})
    return ordered


def normalize(questions):
    if isinstance(questions, dict):
        flat = []
        for k, items in questions.items():
            kt = TYPE_ALIAS.get(str(k).lower(), str(k).lower())
            for it in items or []:
                if isinstance(it, dict):
                    flat.append(fix_item(it, kt if kt in TYPE_KEYS else None))
        return flat
    return [fix_item(it) if isinstance(it, dict) else it for it in questions]


def process(path, apply):
    text = path.read_text(encoding="utf-8")
    m = SECTION_RE.search(text)
    if not m:
        return None, []
    body = m.group(2)
    fence = FENCE_RE.search(body)
    raw = fence.group(1) if fence else body
    try:
        qs = yaml.safe_load(raw)
    except yaml.YAMLError:
        return "yaml-error", []
    if not isinstance(qs, (list, dict)) or not qs:
        return None, []
    new = normalize(qs)
    remaining = [(i, k) for i, q in enumerate(new) if isinstance(q, dict)
                 for k in ("question", "answer", "explanation") if k not in q]
    if new == qs and fence:
        return None, remaining
    dumped = yaml.safe_dump(new, sort_keys=False, allow_unicode=True, width=10000, default_flow_style=False)
    dumped = re.sub(r"\n(?=- )", "\n\n", dumped)  # blank line between questions, like hand-written files
    new_body = "\n```yaml\n" + dumped + "```\n\n"
    if fence:
        new_section = body[:fence.start()].rstrip("\n") + new_body if body[:fence.start()].strip() else new_body
    else:
        new_section = new_body
    if apply:
        path.write_text(text[:m.start(2)] + new_section + text[m.end(2):], encoding="utf-8")
    return "changed", remaining


def main():
    apply = "--apply" in sys.argv
    changed, errs, remaining = 0, [], []
    for f in sorted(pathlib.Path("domains").rglob("*.md")):
        if f.name.startswith("_"):
            continue
        status, rem = process(f, apply)
        if status == "changed":
            changed += 1
        elif status == "yaml-error":
            errs.append(f.as_posix())
        remaining += [(f.as_posix(), i, k) for i, k in rem]
    print(f"{'changed' if apply else 'would change'}: {changed} files; YAML parse errors (untouched): {len(errs)}")
    print(f"items still missing a field: {len(remaining)} in {len({r[0] for r in remaining})} files")
    if "--list-remaining" in sys.argv:
        out = sys.argv[sys.argv.index("--list-remaining") + 1]
        pathlib.Path(out).write_text("".join(f"{p}\t{i}\t{k}\n" for p, i, k in remaining), encoding="utf-8")
    for e in errs[:20]:
        print("  yaml-error:", e)


if __name__ == "__main__":
    main()
