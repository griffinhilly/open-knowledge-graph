# Re-check instructions: independent residual-error audit of published new sections

Project root: `C:\Users\griff\Projects\griffin\open-knowledge-graph`. Tonight, agents wrote new `## How It's Best Learned` and `## Common Misconceptions` sections into public topic pages (openknowledgegraph.com), and a checker fixed them. You are a fresh, independent auditor. Your job is to MEASURE how many errors remain, not to trust either earlier agent.

Your input: `review/2026-11-06-develop/recheck/<PART>.tsv`, one line per sampled part: `<path>\t<how|mis>`.

## For each line
1. Read the file. Read the named section (How It's Best Learned or Common Misconceptions) and the Core Idea for context.
2. List every distinct factual claim in that section (each misconception bullet = belief claim + correction claim). Count them.
3. Check every claim against reliable sources. Use WebSearch/WebFetch for every name, date, figure, formula, attribution and empirical finding; work every exercise or calculation yourself. For a purely conceptual claim, sound reasoning plus a standard reference is enough.
4. A claim is wrong if it is factually false, overstated (an absolute that has real counterexamples), a strawman misconception, contradicts the page, or is an exercise that fails when worked.

## Do not edit any file. This is a measurement.

## Log
Write `review/2026-11-06-develop/recheck/<PART>.result.tsv`, one line per part:
`<path>\t<how|mis>\t<claims checked>\t<claims wrong>\t<for each wrong claim: quote + why + source URL>`
Write as you go (rewrite the full file every ~10 parts).

Tools: Read, Grep, Glob, Write, WebSearch, WebFetch. No Bash, no git, no Edit of topic files.
Final reply, at most 4 lines: parts checked, claims checked, claims wrong, and the worst error.
