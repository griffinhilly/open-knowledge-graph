# Flag-fix instructions: verify and correct suspected errors in existing topic text

Project root: `C:\Users\griff\Projects\griffin\open-knowledge-graph`. Writer agents flagged suspected factual errors in the EXISTING text of public topic pages (openknowledgegraph.com). The flags are claims by another agent and may themselves be wrong. Your job: decide each flag with evidence, then fix only what is really wrong.

Your input: the `## Flags` sections of the report files named in your prompt (`review/2026-11-06-develop/batches/<BATCH>.report.md`). Handle only the "suspected factual error / inconsistency in existing text" flags. Ignore prerequisite flags (another process handles them).

## For each flag
1. Read the file and find the exact text.
2. Verify with evidence. Use WebSearch / WebFetch for any name, date, figure, attribution or quotation; prefer encyclopedias, textbooks, university or museum pages, and primary sources. For conceptual claims (a definition, a formula, a logical inconsistency inside the file), reasoning plus a reliable reference is enough.
3. Verdict: `confirmed` (the text is wrong), `rejected` (the text is right; the flag is wrong), or `unclear` (evidence conflicts or is missing).
4. If confirmed, fix with the smallest edit that makes the text true. A fix is a new claim: use only what your evidence supports. If the precise figure is uncertain, rephrase to what is certain (for example "over 600" rather than an exact count) or remove the detail. Keep question YAML valid; if you change a question's answer, make its options, answer index and explanation agree.
5. Do not touch frontmatter, and do not change text that no flag points to, except the same error repeated elsewhere in the same file.

## Tools
Read, Grep, Glob, Edit, Write, WebSearch, WebFetch. No Bash, no PowerShell, no git. Edit only files named in the flags.

## Log
Write `review/2026-11-06-develop/flagfix/<NAME>.tsv`, one line per flag:
`<path>\t<short quote of the flagged text>\t<confirmed|rejected|unclear>\t<fixed|no-change>\t<evidence: source URL or reason>\t<what you changed>`

Your work will be checked by a separate reviewer. Final reply, at most 5 lines: flags handled, confirmed/rejected/unclear counts, files edited.
