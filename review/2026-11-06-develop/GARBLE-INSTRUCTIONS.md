# Garble-fix instructions: repair text broken by an old mechanical rewrite

Project root: `C:\Users\griff\Projects\griffin\open-knowledge-graph`. Months ago a script "softened absolutes" in topic files by blind word swaps: every→most, all→most, always→typically/usually, only→mainly/primarily, cannot→can rarely, never→seldom. It broke grammar and often meaning: "Most integral domain is a field", "if and mainly if", "most player's strategy", "they is expected". Some of these sit in true/false questions, where the swap can flip whether the statement is true.

Your input: `review/2026-11-06-develop/flagfix/<PART>` — lines `path:line:text` found by a regex. Many matches are fine English ("Most energy is lost as heat"). Only fix real damage.

## For each match
1. Read the surrounding text (and, for a question, its options, answer and explanation).
2. Decide: `garbled` (the swap broke grammar or meaning) or `fine`.
3. If garbled, restore the intended statement. Usually that means the original absolute ("Every integral domain…", "if and only if"), but only if the absolute is TRUE. If the absolute is false, write a correct hedged version with good grammar. For a true/false question, make the statement, the `answer` and the `explanation` agree, and keep the statement's truth value matching its explanation.
4. Check the whole file for other garbled spots from the same rewrite and fix those too.

## Tools and limits
Read, Grep, Glob, Edit, Write. No Bash, no PowerShell, no git. Edit only files named in your input. Never touch frontmatter. Keep YAML valid (quote strings containing `: `).

## Log
Write `review/2026-11-06-develop/flagfix/garble_<NAME>.tsv`, one line per match handled:
`<path>\t<line>\t<garbled|fine>\t<old text (short)>\t<new text (short)>`

Your work will be checked by a separate reviewer. Final reply, at most 4 lines: matches, garbled fixed, fine, files edited.
