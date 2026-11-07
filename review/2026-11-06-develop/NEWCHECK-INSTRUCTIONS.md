# New-topic checker: independent fact-check of newly created topic files

Project root: `C:\Users\griff\Projects\griffin\open-knowledge-graph`. Another agent created new topic files for domain `<DOMAIN>`; they are listed in the table in `review/2026-11-06-develop/newtopics/<DOMAIN>.report.md`. They will be published on openknowledgegraph.com. You are the independent checker: treat every line as a draft from someone else.

## For each new file, check
1. **Gap is real.** Grep `domains/` for the topic's key terms. If an existing topic already covers the same unit, log `duplicate-of <id>` and do not edit; the orchestrator will drop the file.
2. **Every factual claim** in Core Idea, How It's Best Learned, Common Misconceptions, Questions (question, options, answer, explanation) and Explainer. Count claims as you go. Use WebSearch/WebFetch for every name, date, figure, formula, constant and attribution; conceptual claims need sound reasoning or a reliable reference. Questions: the marked answer must be right, the other options wrong, and the explanation consistent.
3. **Frontmatter.** id = file name; every prerequisite and builds-toward id exists (Glob); hard prerequisites are really required; stage is not below any hard prerequisite's stage and fits where the content is usually first taught; `status: validated`.
4. **Format and style.** Sections in order (Core Idea, How It's Best Learned, Common Misconceptions, Questions, Explainer); Questions is a ```yaml list of 3–5 items, each with question/type/answer/explanation, multiple-choice answer a 0-based index; misconception bullets as `- <belief>. (<correction>)`. No "It's not X, it's Y"; none of: delve, leverage, foster, crucial, pivotal, essential, comprehensive, landscape, journey, "at its core", "in essence".

## Fix
Log your verdict before fixing (the log measures the draft's error rate). Fix with minimal edits; a fix is a new claim, so use only what your evidence supports. If a claim can't be made right with confidence, delete it. If a whole file is unsound, log `reject` and leave it.

## Tools
Read, Grep, Glob, Edit, Write, WebSearch, WebFetch. No Bash, no PowerShell, no git. Edit only the new files.

## Log
Write `review/2026-11-06-develop/newtopics/<DOMAIN>.check.tsv`, one line per file:
`<path>\t<claims checked>\t<claims wrong>\t<ok|fixed|reject|duplicate-of id>\t<notes: what was wrong, sources>`

Final reply, at most 6 lines: files checked, claims checked, claims wrong, fixed/rejected/duplicates.
