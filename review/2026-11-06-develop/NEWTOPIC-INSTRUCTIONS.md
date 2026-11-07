# New-topic instructions: find and fill genuine gaps in one core subject

Project root: `C:\Users\griff\Projects\griffin\open-knowledge-graph`. You own one domain: `domains/<DOMAIN>/`. Its courses are listed in `domains/<DOMAIN>/_domain.yml`. Each topic is `domains/<DOMAIN>/<course>/<id>.md`. The full format is in `meta/schema.md`. Read it first, then read two existing topics in your domain as models.

## Step 1: find gaps
For each course, Glob the topic files and Grep their `title:` lines. Compare against the standard syllabus a teacher would recognize for that level: for example Common Core / AP / IB for school courses, and the standard textbook table of contents for undergraduate and graduate courses. Name the syllabus you compare against.

A gap is a topic that the standard syllabus teaches as its own unit and that no existing topic covers, under any title. Before proposing one, Grep the whole `domains/` tree for its key terms, because it may live in another course or domain. **Do not add filler.** Fewer real gaps beat many weak ones. Aim for the 10–25 clearest gaps in the domain; zero is acceptable if the coverage is complete.

## Step 2: write each new topic
Create `domains/<DOMAIN>/<course>/<id>.md`. The id is lowercase-hyphenated, globally unique (Glob `domains/**/<id>.md` to confirm none exists), and equal to the file name. Frontmatter, with keys in this order:
```
id, title, domain, course, prerequisites (list of {id, type: hard|soft}), builds-toward (list of ids), tags, stage, status: validated
```
- Every prerequisite and builds-toward id must be an existing file (check with Glob). An edge `A -> B` means "B draws upon A". **hard** = must know first, **soft** = helps.
- `stage`: one of pre-formal, concrete-operations, abstract-reasoning, formal-systems, advanced, expert. It is where the content is typically first met, and must not be below the stage of its hard prerequisites.
- Body sections, in order: `# <title>`, `## Core Idea` (2–4 sentences), `## How It's Best Learned` (2–4 sentences), `## Common Misconceptions` (2–4 bullets: `- <belief>. (<correction>)`), `## Questions` (a ```yaml list of 3–5 questions; see meta/schema.md for the multiple-choice / true-false / short-answer format; each with `explanation`), `## Explainer` (a 300–450-word mini-lesson).

## Accuracy (an independent checker reviews every claim)
Use only facts you are certain of. Every name, date, figure, formula and attribution must be right. No invented studies or quotes. No absolute words unless strictly true. Style: plain and direct, like the model topics. Never use "It's not X, it's Y"; avoid delve, leverage, foster, crucial, pivotal, essential, comprehensive, landscape, journey, "at its core", "in essence"; at most one em dash per paragraph.

## Tools and limits
Use ONLY Read, Grep, Glob, Write. No Bash, no PowerShell, no git. **Do not edit existing files.** If an existing topic should list your new topic as a prerequisite, record it instead (below).

## Report
Write `review/2026-11-06-develop/newtopics/<DOMAIN>.report.md`:
1. The syllabus or syllabi compared against, per course.
2. A table: new id | course | why it is a gap (which syllabus unit) | prerequisites.
3. `## Proposed edges into existing topics`: lines `ADD\t<new id>\t<existing id>\t<hard|soft>\t<reason>`, meaning the existing topic should list the new one as a prerequisite.
4. Gaps you considered and rejected (already covered by <id>).

Final reply, at most 6 lines: `Status`, new topic count, proposed-edge count.
