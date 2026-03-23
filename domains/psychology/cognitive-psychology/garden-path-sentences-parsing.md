---
id: garden-path-sentences-parsing
title: Garden-Path Sentences and Syntactic Parsing
domain: psychology
course: cognitive-psychology
prerequisites:
- id: language-comprehension
  type: hard
- id: lexical-frequency-word-processing
  type: soft
tags:
- language
- syntax
- parsing
- ambiguity
stage: formal-systems
status: draft
---

# Garden-Path Sentences and Syntactic Parsing

## Core Idea
Garden-path sentences reveal that syntactic parsing is initially automatic and sensitive to frequency-based statistics rather than just grammatical well-formedness. Readers commit to a likely parse early; when later words contradict this choice, re-parsing is required, causing comprehension difficulty.

## Questions

```yaml
- question: "A reader slows down sharply at the word 'fell' in 'The horse raced past the barn fell.' What best explains this reading difficulty?"
  type: multiple-choice
  options:
    - "'Fell' is a low-frequency word that requires extra time to retrieve from the mental lexicon"
    - "The parser committed to an active-voice parse ('a horse was racing') before seeing 'fell,' and must now reanalyze the sentence as a reduced relative clause"
    - "The sentence violates English grammar rules, and the parser flags it as unacceptable"
    - "The parser suspended judgment about structure until 'fell' arrived, then had to build the parse from scratch"
  answer: 1
  explanation: "The garden-path effect is purely structural. Active constructions are statistically far more common than reduced passive relative clauses, so the incremental parser committed to an active reading. 'Fell' cannot be the second main verb of an already-complete sentence, forcing costly reanalysis. Option A confuses lexical difficulty with structural difficulty; option C is wrong because the sentence is grammatically well-formed; option D gets the architecture backwards — the parser commits early, not late."

- question: "Which evidence most directly supports the claim that the parser is 'incremental' rather than waiting for the full sentence before assigning structure?"
  type: multiple-choice
  options:
    - "People find garden-path sentences harder to understand than semantically unusual but structurally simple sentences"
    - "EEG studies show a P600 response — a neural signature of syntactic reanalysis — arising several hundred milliseconds after the disambiguating word arrives"
    - "Garden-path sentences are rarely produced by native speakers"
    - "Re-reading a garden-path sentence eliminates all comprehension difficulty"
  answer: 1
  explanation: "The P600 is a neural event-related potential that occurs around 600ms after the disambiguating word — precisely when reanalysis is triggered. Its timing shows that the parser had already committed to a structure before the disambiguating word arrived, then detected a conflict requiring repair. This is direct neural evidence for early, incremental commitment. Option A could be explained by many factors; option D is false — re-reading helps but doesn't fully eliminate difficulty."

- question: "Garden-path sentences are initially difficult because the parser commits to a parse based on statistical frequency, not just grammatical rules."
  type: true-false
  answer: true
  explanation: "This is the core insight. Both constraint-based and serial models of parsing agree that frequency-based statistics shape early parsing commitments. Active voice is more frequent than reduced relative clauses; transitive uses of verbs are more frequent than some intransitive constructions. When the statistically favored parse is wrong, reanalysis is required. Grammar rules alone do not determine which parse is chosen first — frequency does."

- question: "Garden-path sentences are ungrammatical — they violate English syntax — which is why comprehension fails."
  type: true-false
  answer: false
  explanation: "Garden-path sentences are fully grammatical. 'The horse raced past the barn fell' is syntactically correct — it is a reduced relative clause ('the horse [that was] raced past the barn fell'). The difficulty is not grammatical unacceptability but the need to abandon an initially committed parse and assign a new one. If garden-path sentences were ungrammatical, re-reading would not make them comprehensible."

- question: "Why do garden-path sentences 'work' — why does comprehension fail initially and succeed upon re-reading? What does this reveal about the parser's normal operation?"
  type: short-answer
  answer: "On first reading, the parser incrementally commits to the most statistically common parse at each word, without waiting for the full sentence. When a later word is incompatible with the committed parse, reanalysis is required — which is cognitively costly. On re-reading, you already know the ending, so you approach the ambiguous region with the correct commitment and parse smoothly. This reveals that the parser normally bets early and confidently on likely structures rather than maintaining multiple interpretations in parallel."
  explanation: "The re-reading asymmetry is key evidence: if parsing were simply about decoding fixed grammar, re-reading wouldn't matter. The fact that re-reading dramatically helps shows that the initial difficulty was about structural commitment, not linguistic knowledge. The parser's incremental, frequency-guided design is normally efficient — most sentences confirm the initial parse — but garden-path sentences expose the cost of this efficiency when the initial bet is wrong."
```

## Explainer

You've studied language comprehension, which covers how the brain extracts meaning from sentences. Garden-path effects isolate one specific and surprising property of this system: the parser does not wait for all the evidence before committing to an interpretation. It makes early, confident bets — and when those bets are wrong, the cognitive cost is measurable. The name comes from the idiom "being led down the garden path": you follow a promising route that turns out to be a dead end.

The classic example is *"The horse raced past the barn fell."* Your parser, upon reading "the horse raced past the barn," almost certainly constructs the active-voice parse: a horse is racing. The word "fell" then contradicts this — "fell" can't be a second main verb after an already-complete sentence. The actual parse is passive: "the horse [that was] raced past the barn fell." You likely had to re-read it. Why did your parser choose the active reading so confidently? Because active voice is statistically far more common than the reduced relative clause construction. The parser uses **frequency statistics** — not just grammar rules — to assign structure, and it does so incrementally, word by word, without waiting for the full sentence to resolve ambiguity.

This reveals the parser's architecture: it is **eager** and **incremental**. Each new word immediately triggers structural commitment rather than suspending judgment until ambiguity is resolved. The competing theoretical accounts disagree about what governs these commitments. **Serial models** (like the classic garden-path model of Frazier and Fodor) hold that the parser uses simple structural heuristics — attach constituents as simply as possible, prefer the most recent attachment site — and only consults semantic or contextual information when syntactic analysis fails. **Constraint-based models** (like the unrestricted race model) hold that all sources of information — syntactic frequency, semantic plausibility, discourse context — are integrated immediately and in parallel, with the most-activated parse winning the race. Garden-path effects occur when the winning parse turns out to be wrong, not because the parser ignored context but because the statistical evidence strongly favored the wrong structure.

The practical implication is that **lexical frequency** profoundly shapes syntactic processing — a connection to your prerequisite on lexical frequency and word processing. A verb that appears more often as a transitive verb (taking an object) will cause the parser to prefer an object-attached reading over an intransitive one, and this preference can be strong enough to produce garden-path effects even in contexts where the other reading is clearly intended. Reading time studies and EEG (specifically the P600 component, a positive-going ERP at ~600ms associated with syntactic reanalysis) provide direct evidence that re-parsing is cognitively costly and neurally distinct from normal processing. Garden-path sentences are powerful tools precisely because they reveal, through the error they induce, the normally invisible real-time commitments the parser is constantly making.
