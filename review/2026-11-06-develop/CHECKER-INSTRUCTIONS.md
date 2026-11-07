# Checker instructions: independent fact-check of newly written topic sections

Project root: `C:\Users\griff\Projects\griffin\open-knowledge-graph`. Another agent just wrote new sections into public topic pages (openknowledgegraph.com). You are the independent checker. Treat the new text as a draft from someone else: check it, do not trust it.

Your batches: `review/2026-11-06-develop/batches/<BATCH>.tsv` (one or more, listed in your prompt). Each line is `<file path>\t<needs>`. Needs tell you what is NEW in each file:
- `how` = the `## How It's Best Learned` section is new.
- `mis` = the `## Common Misconceptions` section is new.
- `ex` = the Explainer was extended (check the whole Explainer).
- `q:<i>:answer` / `q:<i>:explanation` = that field of question item `i` (0-based) in the Questions YAML is new.
Only the new parts are in scope for the counts. If older text in the file is clearly wrong (a wrong answer key, a false formula or date, leftover drafting chatter) and you are certain, fix it with a minimal edit and log it on its own line with field `old:<section>`; otherwise just note it. Never touch frontmatter.

## Tools
Use ONLY Read, Grep, Glob, Edit, Write. No Bash, no PowerShell, no git. You may look facts up in other topic files with Grep. Edit only the files on your list.

## Check every claim in the new parts
For each new part, count its distinct factual claims (each misconception bullet = the belief claim + the correction claim; each how-sentence that asserts something = a claim; each question field = one claim). Then judge each:
1. **Correct?** Is the correction true as stated, with no overstated absolute (always/never/only/all)? Are any names, dates, figures, formulas and attributions right? Is the answer to a question actually right, and does it match the question's options/type?
2. **Real?** Is the misconception one that learners of this topic plausibly hold (not a strawman nobody believes)?
3. **Consistent?** Does it agree with the file's own Core Idea and Explainer?
4. **Specific?** Is "How It's Best Learned" specific to this topic, not generic study advice?
5. **Format.** Sections in order Core Idea → How It's Best Learned → Common Misconceptions → Questions → Explainer; bullets as `- <belief>. (<correction>)`; Questions YAML still valid (indentation consistent; strings with `: ` or ` #` quoted).
6. **Style.** No "It's not X, it's Y"; none of: delve, leverage, foster, crucial, pivotal, essential, comprehensive, seamless, landscape, journey, "it's worth noting", "at its core", "in essence", "genuinely", "load-bearing"; no mention of AI or the writing process.

## Fix
Record your verdict BEFORE fixing (the log measures the draft's error rate). Then fix with minimal edits. A fix is a new claim: make it conservative and certain. If a bullet or sentence can't be made right with confidence, delete it (keep at least 2 bullets per misconceptions section; if you can't, delete the whole section and say so). Do not rewrite text that is correct just to change its style, except for the banned phrases.

## Log
Write `review/2026-11-06-develop/batches/<BATCH>.check.tsv` for each batch, one line per new part:
`<path>\t<how|mis|ex|q:i:field>\t<claims checked>\t<claims wrong>\t<ok|fixed|cut>\t<note on what was wrong, or blank>`
A "wrong" claim is a factual error, a strawman, an inconsistency or a broken format. Style-only fixes go in the note but don't count as wrong.

Final reply, at most 6 lines: per batch, parts checked, claims checked, claims wrong, parts fixed/cut; and anything systemic you noticed about the writer.
