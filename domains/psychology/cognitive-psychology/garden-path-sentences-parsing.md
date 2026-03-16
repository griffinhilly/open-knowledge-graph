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

## Explainer

You've studied language comprehension, which covers how the brain extracts meaning from sentences. Garden-path effects isolate one specific and surprising property of this system: the parser does not wait for all the evidence before committing to an interpretation. It makes early, confident bets — and when those bets are wrong, the cognitive cost is measurable. The name comes from the idiom "being led down the garden path": you follow a promising route that turns out to be a dead end.

The classic example is *"The horse raced past the barn fell."* Your parser, upon reading "the horse raced past the barn," almost certainly constructs the active-voice parse: a horse is racing. The word "fell" then contradicts this — "fell" can't be a second main verb after an already-complete sentence. The actual parse is passive: "the horse [that was] raced past the barn fell." You likely had to re-read it. Why did your parser choose the active reading so confidently? Because active voice is statistically far more common than the reduced relative clause construction. The parser uses **frequency statistics** — not just grammar rules — to assign structure, and it does so incrementally, word by word, without waiting for the full sentence to resolve ambiguity.

This reveals the parser's architecture: it is **eager** and **incremental**. Each new word immediately triggers structural commitment rather than suspending judgment until ambiguity is resolved. The competing theoretical accounts disagree about what governs these commitments. **Serial models** (like the classic garden-path model of Frazier and Fodor) hold that the parser uses simple structural heuristics — attach constituents as simply as possible, prefer the most recent attachment site — and only consults semantic or contextual information when syntactic analysis fails. **Constraint-based models** (like the unrestricted race model) hold that all sources of information — syntactic frequency, semantic plausibility, discourse context — are integrated immediately and in parallel, with the most-activated parse winning the race. Garden-path effects occur when the winning parse turns out to be wrong, not because the parser ignored context but because the statistical evidence strongly favored the wrong structure.

The practical implication is that **lexical frequency** profoundly shapes syntactic processing — a connection to your prerequisite on lexical frequency and word processing. A verb that appears more often as a transitive verb (taking an object) will cause the parser to prefer an object-attached reading over an intransitive one, and this preference can be strong enough to produce garden-path effects even in contexts where the other reading is clearly intended. Reading time studies and EEG (specifically the P600 component, a positive-going ERP at ~600ms associated with syntactic reanalysis) provide direct evidence that re-parsing is cognitively costly and neurally distinct from normal processing. Garden-path sentences are powerful tools precisely because they reveal, through the error they induce, the normally invisible real-time commitments the parser is constantly making.
