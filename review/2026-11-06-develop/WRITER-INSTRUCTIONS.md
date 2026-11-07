# Writer instructions: fill pedagogy sections in Open Knowledge Graph topics

Project root: `C:\Users\griff\Projects\griffin\open-knowledge-graph`. Each topic is a public page on openknowledgegraph.com (CC BY-SA). A topic file is Markdown with YAML frontmatter, then sections in this order: `## Core Idea`, `## How It's Best Learned`, `## Common Misconceptions`, `## Questions` (a ```yaml block), `## Explainer`.

Your batch file is `review/2026-11-06-develop/batches/<BATCH>.tsv`. Each line: `<file path>\t<needs>`, where needs is a comma list of:
- `how`: the file has no `## How It's Best Learned`. Write one.
- `mis`: the file has no `## Common Misconceptions`. Write one.
- `ex`: the Explainer is under 150 words. Extend it to roughly 300–450 words, keeping the existing text.
- `q:<i>:answer` or `q:<i>:explanation`: question item number `i` (0-based) in the Questions YAML lacks that field. Add it.

## Tools
Use ONLY Read, Grep, Glob, Edit, Write. No Bash, no PowerShell, no git. Edit only the files on your list (plus your report file).

## Before you start
Read the model file `domains/physics/conceptual-physics/acceleration-and-velocity.md`. Then Glob your course folder and Read one or two files that already have both sections, to match the course's register.

## What to write
**How It's Best Learned**: 2–4 sentences, roughly 30–70 words. Say concretely what helps a learner who already has the prerequisites: a representation, an activity, a worked example to start from, a sequence, a comparison. It must be specific to this topic. If you propose a worked exercise, work it yourself first and make sure every step succeeds as written. Generic study advice ("practice problems", "review regularly", "use flashcards") is not acceptable unless made specific to the topic.

**Common Misconceptions**: 2–4 bullets in this form:
`- <the mistaken belief, stated the way a learner would hold it>. (<the correction, one or two sentences>)`
Use confusions that learners of this topic really have. Each correction must be true as stated.

Insert `## How It's Best Learned` directly after the Core Idea section, then `## Common Misconceptions`, both before `## Questions`. If one of the two already exists, put the new one in its correct place relative to it. Leave one blank line between sections.

**Question fills**: for short-answer, `answer` is a concise model answer (1–3 sentences); `explanation` says why it is right. For other types, follow the schema: multiple-choice `answer` is a 0-based integer, true-false `answer` is `true`/`false`. Keep the YAML valid: match the block's indentation, and double-quote any string that contains `: `, ` #`, or starts with a special character.

## Accuracy (an independent checker reviews every line you write)
- Add no names, dates, figures, quotations, studies or statistics unless the file's Core Idea or Explainer already states them, or you are certain of them. Prefer conceptual content. Never write "studies show" or invent research.
- Empirical findings in the social sciences (economics, history, psychology) are often contested. State them as findings of a study or literature, with hedges ("evidence suggests", "in many studies"), never as settled law, unless the consensus is overwhelming.
- No absolute words (always, never, all, only) unless strictly true.
- Older text in this corpus contains errors. Do not copy a claim from the file's older text into your sections unless you know it is true.
- Do not contradict the file's own Core Idea or Explainer. If you think existing text in the file is wrong, do not fix it; note it in your report.

## Style
Plain and direct, like the model file. Never use "It's not X, it's Y" or "not just X, but Y". Avoid: delve, leverage, foster, crucial, pivotal, essential, comprehensive, seamless, landscape, journey, "it's worth noting", "at its core", "in essence", "simply", "genuinely", "load-bearing". At most one em dash per section. Do not mention AI, this process, these instructions, or the batch.

## Do not change
Frontmatter, Core Idea, Explainer (unless `ex`), existing questions (only add missing fields), or anything outside your list.

## Report
Write `review/2026-11-06-develop/batches/<BATCH>.report.md`:
- One line per file: `<path> | done | <short note or blank>` (or `skipped: <reason>`).
- A `## Flags` section: suspected factual errors in existing text (path, quote, why), and suspected wrong or missing prerequisites (`<prereq id> -> <topic id>`, why). Write "none" if none.

Final reply, at most 6 lines: `Status: DONE | DONE_WITH_CONCERNS | BLOCKED`, files done/skipped, flag count.
