# Edge-review instructions: judge candidate prerequisite edges (read-only)

Project root: `C:\Users\griff\Projects\griffin\open-knowledge-graph`. Topics are files `domains/<domain>/<course>/<id>.md` with YAML frontmatter: `prerequisites` (list of `{id, type: hard|soft}`), `builds-toward` (informational forward links), `stage`.

**Edge meaning:** `A -> B` (A listed in B's prerequisites) means "B draws upon A". It does NOT mean "A is earlier in time"; `stage` is the separate time axis. **hard** = a learner must know A first; **soft** = A helps but is not required. Mutual reinforcement is never bidirectional: pick the dominant direction. Stages, low to high: pre-formal, concrete-operations, abstract-reasoning, formal-systems, advanced, expert.

## Tools
Use ONLY Read, Grep, Glob, Write. No Bash, no PowerShell, no git. **Do not edit any topic file.** You only write your verdict file.

## Your input
`review/2026-11-06-develop/edges/<INPUT>`, a TSV with one candidate per line, with blocks of `id, title, domain/course, stage` (and for `inv_*`, a final `type` column):
- `bt_*.tsv` (A block, then B block): A lists B in `builds-toward`, but B does not list A as a prerequisite. Decide:
  - `ADD` A as a prerequisite of B (give `hard` or `soft`), when B really draws on A.
  - `DROP` the link (remove B from A's builds-toward), when B does not draw on A.
  - `JUDGE` when it's a real judgment call for a human.
- `zero.tsv` (one block): topic T has no prerequisites. Propose 1–4 prerequisites that exist in the graph (`ADD <prereq id> -> T`), or `NONE` if T is truly an entry point. Use Grep/Glob to find real ids; never invent an id.
- `inv_*.tsv` (A block, B block, type): A is a prerequisite of B but staged 2+ stages higher. Decide `REMOVE` (the edge is wrong), `SOFTEN` (hard -> soft), `KEEP` (legitimate under "draws upon"), or `JUDGE`.

Read the files when titles are not enough. Look at B's Core Idea and Explainer to decide what B really draws on. Be conservative: `ADD hard` only when B cannot be understood without A.

## Output
Write `review/2026-11-06-develop/edges/<INPUT stem>.verdicts.tsv`, one line per candidate (for `zero.tsv`, one line per proposed prerequisite or one `NONE` line):
`<VERDICT>\t<A id>\t<B id>\t<hard|soft|->\t<high|medium>\t<reason, one short sentence>`
`high` means you would bet on it; anything less is `medium`. Every candidate line gets a verdict line. Work through the file in order and write as you go (append in chunks of ~50 lines), so partial work survives.

Your output will be checked by a separate reviewer. Final reply, at most 5 lines: counts per verdict, and anything odd.
