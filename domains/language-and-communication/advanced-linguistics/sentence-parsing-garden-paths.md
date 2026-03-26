---
id: sentence-parsing-garden-paths
title: Sentence Parsing and Garden-Path Sentences
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: psycholinguistics-intro
  type: hard
- id: syntactic-structure
  type: hard
- id: lexical-access-word-recognition
  type: soft
builds-toward:
- working-memory-sentence-comprehension
tags:
- psycholinguistics
- parsing
- comprehension
stage: expert
status: validated
---
# Sentence Parsing and Garden-Path Sentences

## Core Idea
Garden-path sentences like 'The horse raced past the barn fell' temporarily mislead comprehenders, who initially parse it as a main clause until 'fell' reveals a reduced relative clause structure. These sentences show that parsing uses incremental heuristics (minimal attachment) rather than considering all analyses simultaneously, and that comprehension involves reanalysis and recovery from initial misanalysis.

## Questions

```yaml
- question: "In the sentence 'The horse raced past the barn fell,' most readers experience difficulty at the word 'fell.' According to the garden-path model, why does this specific word cause the problem?"
  type: multiple-choice
  options:
    - "Because 'fell' is an irregular verb form that is rarely encountered in everyday language."
    - "Because 'fell' reveals that the initial parse — treating 'raced' as the main verb — is grammatically impossible, requiring the reader to discard and rebuild the entire structure."
    - "Because 'fell' introduces semantic implausibility about horses, triggering a plausibility check."
    - "Because 'fell' arrives too quickly for working memory to integrate it with earlier words."
  answer: 1
  explanation: "'Fell' is the disambiguation point — the moment where the incorrect initial parse (main clause with 'raced' as the main verb) becomes untenable. A sentence cannot have two main verbs without a conjunction, so 'fell' forces reanalysis: 'the horse' is actually the subject of a reduced relative clause ('the horse that was raced past the barn'), and 'fell' is the true main verb. The difficulty is not about 'fell' itself but about the structural reanalysis it demands — undoing what the parser had already committed to and rebuilding the entire phrase structure."

- question: "Which prediction distinguishes a serial parser (single-analysis commitment) from a parallel parser (multiple-analyses maintained simultaneously) with respect to garden-path sentences?"
  type: multiple-choice
  options:
    - "A serial parser predicts garden-path effects; a parallel parser predicts no such processing difficulty because the correct analysis was maintained all along."
    - "Both predict the same garden-path effects, but serial parsers recover faster because they only maintained one analysis."
    - "A parallel parser predicts stronger garden-path effects because maintaining multiple analyses overloads working memory."
    - "A serial parser predicts difficulty at the start of the sentence, while a parallel parser predicts difficulty at the end."
  answer: 0
  explanation: "The garden-path effect is the key empirical test between these models. If the parser maintains all grammatically possible analyses in parallel, it always has the correct analysis available when the disambiguating word arrives — no reanalysis needed, no measurable slowdown. The serial model predicts difficulty precisely because the parser committed to the wrong analysis and must now discard it. Reading-time studies and ERP data showing processing disruption exactly at the disambiguation point support the serial model with reanalysis."

- question: "The 'minimal attachment' heuristic in sentence parsing causes garden-path errors because it systematically favors syntactically simpler analyses, which happen to be wrong for sentences with reduced relative clauses."
  type: true-false
  answer: true
  explanation: "Minimal attachment is the principle that the parser builds the simplest phrase structure given the words encountered so far — fewest nodes, most direct attachment. For 'the horse raced past the barn,' the simplest analysis has 'raced' as the main verb of a simple main clause, which requires fewer structural nodes than embedding 'raced' inside a relative clause modifying 'the horse.' This heuristic is statistically optimal for most sentences in natural language — but in the unusual case of a reduced relative clause, it leads the parser down the wrong path."

- question: "Garden-path effects demonstrate a fundamental limitation of the human language-processing system: it can seldom handle sentences with reduced relative clauses."
  type: true-false
  answer: false
  explanation: "Humans can and do understand garden-path sentences — they just require reanalysis and extra processing time. The garden-path effect reveals not a limitation but an architectural feature: the parser commits early to the most probable analysis (an efficient strategy for normal language) and recovers when that analysis fails. With re-reading or additional context, comprehenders always reach the correct interpretation. The difficulty is in the recovery cost, not an inability to process reduced relative clauses."

- question: "Why does the 'minimal attachment' heuristic cause processing errors in highly skilled readers, even though those readers know the grammar that would allow them to consider alternative analyses?"
  type: short-answer
  answer: "Minimal attachment operates automatically and below conscious awareness — it is a fast heuristic applied incrementally as each word arrives, not a deliberate strategy that skilled readers can override. Knowing the grammar doesn't help because the parser commits to the simpler structure before 'fell' appears; by the time the error is revealed, reanalysis is required regardless of the reader's competence."
  explanation: "Syntactic knowledge and real-time processing are separable. A skilled reader knows that reduced relative clauses are grammatical English — they could generate them freely in writing. But the online parser doesn't consult that explicit knowledge; it applies incremental heuristics that succeed on the vast majority of sentences. The rare garden-path sentence exposes the gap between competence (knowing the grammar) and performance (processing in real time under incremental commitment)."
```

## Explainer

From your study of psycholinguistics, you know that language comprehension involves not just knowing grammar but processing sentences in real time under cognitive constraints. From your study of syntactic structure, you know that sentences have hierarchical phrase structure. Garden-path phenomena are what happen when those two facts collide: your parser commits to a syntactic structure based on early words, and that commitment turns out to be wrong.

Read this sentence slowly: *"The horse raced past the barn fell."* Most people get stuck at "fell" and need to reread. What happened? When you encountered "the horse raced," you built the parse *[NP the horse] [VP raced past the barn]*  — a main clause with "the horse" as subject and "raced" as main verb. That's a perfectly good parse of the words so far. But then "fell" arrives, and it can't be the next word in that sentence — there's no room for a second verb in a main clause. The only grammatical analysis is *[NP the horse [RC raced past the barn]] [VP fell]* — "the horse that was raced past the barn fell." This is a **reduced relative clause** (the "that was" has been deleted). Your parser took you down the wrong path and had to backtrack.

The principle behind the error is **minimal attachment**: when the parser encounters a structural ambiguity, it prefers the analysis that builds the simplest phrase structure — fewest nodes, most direct attachment. A main clause with "raced" as the main verb is structurally simpler than a relative clause modifying the subject; hence the default. **Late closure** is a related heuristic: new material is attached to the current phrase being built rather than starting a new one. These aren't flaws — they're efficient strategies that succeed the vast majority of the time. Most sentences don't have the ambiguous structure that produces garden paths; the heuristics are tuned to the statistics of normal language.

The garden-path effect has important implications for parsing models. A **serial parser** that builds one analysis at a time (like the standard explanation above) predicts the garden-path effect naturally: you commit to one parse, and when it fails, you reanalyze. A **parallel parser** that maintains all analyses simultaneously would not predict difficulty — you'd just switch to the right analysis without effort. The evidence from reading time studies and ERP (brain wave) data strongly favors the serial model with subsequent reanalysis: comprehenders show measurable difficulty exactly at the point of disambiguating "fell," suggesting they really do build and then repair the wrong structure. The cost of reanalysis depends on how far the parser has committed and how much structure must be discarded — a useful window into the computational architecture of sentence comprehension.
