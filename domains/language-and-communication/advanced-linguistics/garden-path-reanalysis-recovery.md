---
id: garden-path-reanalysis-recovery
title: Garden-Path Effects and Reanalysis During Parsing
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: sentence-parsing-garden-paths
  type: hard
- id: psycholinguistics-intro
  type: hard
tags:
- garden-path
- parsing
- reanalysis
stage: advanced
status: draft
---

# Garden-Path Effects and Reanalysis During Parsing

## Core Idea
Garden-path sentences lead readers/listeners to an initial incorrect parse (e.g., 'The horse raced past the barn fell' initially parses 'raced' as main verb). Upon encountering disconfirming material, readers reanalyze. The difficulty in reanalysis reveals parsing strategy: the parser builds the simplest structure compatible with input (minimal attachment) and resists revision. Recovery speed depends on factors like plausibility and reanalysis cost, illuminating the interaction between grammar and processing.

## How It's Best Learned
Test garden-path sentences and near-misses in comprehension experiments, measuring reading times to diagnose parsing difficulty and reanalysis cost. Compare predictions of different parsing models.

## Common Misconceptions
- Garden-path effects do not indicate grammatical ambiguity; they reveal processing strategies.
- Recovery from garden paths requires reanalysis; the difficulty of recovery depends on parsing mechanisms.

## Questions

```yaml
- question: "A reader encounters 'The horse raced past the barn fell.' After reading the word 'raced,' what has the parser done, and why does this create difficulty when 'fell' is reached?"
  type: multiple-choice
  options:
    - "The parser has not yet assigned any structure because it processes whole sentences before building syntactic representations"
    - "The parser has flagged 'raced' as ambiguous and is simultaneously maintaining two structural analyses, causing processing overload at 'fell'"
    - "The parser has committed to treating 'raced' as the main verb using the minimal-attachment heuristic, leaving no open syntactic slot for 'fell'"
    - "The parser recognized the reduced relative clause immediately and was surprised when 'fell' did not arrive sooner"
  answer: 2
  explanation: "The parser works incrementally and commits early. After 'the horse raced past the barn,' it has built a structure where 'raced' is the main verb and the sentence is effectively complete. When 'fell' arrives, there is no open slot for it, triggering a reanalysis. The correct parse — 'the horse [that was] raced past the barn' as a reduced relative clause, with 'fell' as the main verb — was available but was never initially considered because the main-verb analysis is simpler (minimal attachment). Option B would predict parallel processing, which the commitment-based model rejects."

- question: "Two garden-path sentences are presented: (A) 'The actress the director praised left the stage' and (B) 'While the boy fed the dog the cat scratched its ear.' Based on the principle that global reanalysis (revising main-clause structure) is more costly than local reanalysis, which prediction follows?"
  type: multiple-choice
  options:
    - "Sentence A is harder because 'the actress' followed immediately by 'the director' creates a noun-pile that takes extra time to resolve"
    - "Both sentences impose equal processing costs because all garden paths require the same structural revision effort"
    - "Sentence B is harder because the comma-less attachment creates a local ambiguity that global reanalysis cannot recover from"
    - "Sentence A imposes a more costly reanalysis because the parser must revise the main clause structure to accommodate the center-embedded relative"
  answer: 3
  explanation: "Sentence A contains a center-embedded relative clause ('the actress [whom] the director praised'), which requires the parser to revise the main-clause assignment — 'the actress' is not the subject of 'the director,' it is the head of the relative clause. This is a global revision requiring the parser to undo and rebuild the core sentence structure. Sentence B involves a simpler local attachment ambiguity resolved by the second noun phrase. The cost of reanalysis tracks how much committed structure must be dismantled."

- question: "Garden-path effects demonstrate that sentences like 'The horse raced past the barn fell' are grammatically ambiguous, since competent readers consistently misparse them."
  type: true-false
  answer: false
  explanation: "Garden-path effects reveal processing strategies, not grammatical ambiguity. 'The horse raced past the barn fell' has exactly one correct grammatical parse (reduced relative clause as subject, 'fell' as main verb). The consistent misparse reveals that the parser uses a commitment-based minimal-attachment heuristic — choosing the simpler structure even when it turns out to be wrong — not that the sentence has two legitimate readings. Grammatical ambiguity (like 'I saw the man with the telescope') means multiple correct parses exist; garden-path sentences typically have only one correct parse."

- question: "The minimal attachment principle predicts that when two structural analyses are available, the parser initially commits to the one requiring fewer syntactic nodes, even if the alternative is more semantically plausible in context."
  type: true-false
  answer: true
  explanation: "Minimal attachment is a structural heuristic that operates before semantic plausibility is fully computed. Experiments show that even when the reduced-relative reading of a garden-path sentence is more plausible (e.g., 'the horse raced past the barn' — horses are frequently raced), readers still experience the garden-path effect, because the structural preference for fewest nodes overrides semantic expectations at the initial commit point. This is what makes garden paths a probe for parser architecture: they expose a structural bias that operates independently of meaning."

- question: "Why is the garden-path phenomenon more informative about how the parsing system is built than simply observing that people sometimes misunderstand sentences?"
  type: short-answer
  answer: "Ordinary misunderstanding could reflect distraction, noise, or low familiarity with vocabulary. Garden-path effects are systematic and predictable failures in fully competent speakers encountering grammatical sentences in controlled conditions. Their systematicity reveals the architecture of the parsing system: that it works incrementally (word by word, not whole-sentence), that it commits to one analysis rather than maintaining alternatives in parallel, and that it follows the minimal attachment heuristic. Because the failure mode is patterned and the recovery cost is measurable via reading-time spikes in eye-tracking or self-paced reading, garden paths serve as controlled experiments that expose parser design in ways that successful comprehension never could."
  explanation: "The key methodological point is that errors are often more diagnostic than successes. A parser that never failed would be a black box; garden-path sentences pry it open by producing failures at predictable points, with predictable difficulty profiles, that map onto specific theoretical commitments about how parsing is organized."
```

## Explainer

From your study of sentence parsing and psycholinguistics, you know that the parser — the mental system that assigns grammatical structure to incoming words — works incrementally, building interpretations word by word without waiting for the sentence to end. This incremental commitment is efficient but creates a specific failure mode: sometimes the structure built so far turns out to be wrong. Garden-path sentences are the experimental probe that reveals this failure most clearly.

Consider the classic example: *The horse raced past the barn fell.* Most readers hit the word *fell* and experience a brief but genuine comprehension failure — the sentence seems ungrammatical. This is the **garden-path effect**: you have been "led down the garden path" to an incorrect parse. What went wrong? After reading *the horse raced past the barn*, the parser has built a structure where *raced* is the main verb and the sentence is essentially complete. *fell* then has no home — there is no open position for it. The correct parse requires treating *raced past the barn* as a **reduced relative clause** (*the horse [that was] raced past the barn*), making *fell* the main verb. But the parser never considered this alternative initially, because the simpler analysis — main verb rather than reduced relative — was committed to first.

**Reanalysis** is the process of tearing down the committed structure and rebuilding it. This is computationally costly because the parser must: (1) detect that the current structure fails, (2) identify where the misparse began, (3) locate an alternative structural analysis, and (4) rebuild from the point of failure. The difficulty of reanalysis is not uniform — it depends on how much structure must be undone and whether the alternative parse was ever active as a competitor. If the garden path is "shallow" (a small local revision), recovery is fast. If it requires revising the main clause structure (a "global" garden path), recovery is slow and sometimes incomplete — some readers reject grammatical garden-path sentences as ungrammatical because they cannot successfully reanalyze.

The garden-path phenomenon reveals two fundamental parsing principles. First, the parser uses a **minimal attachment** strategy: when two structural analyses are available, it initially chooses the one requiring fewer syntactic nodes. This is a heuristic for computational efficiency — simpler structures are processed faster. Second, the parser is **commitment-based**: it does not maintain all possible analyses simultaneously (that would be computationally explosive) but instead commits early to the most preferred structure and revises only under pressure from disconfirming evidence. Garden-path sentences are the experiments that expose both the heuristic (which structure was preferred) and the cost of violating it (how hard reanalysis is). Reading-time studies show that these costs are real and measurable: self-paced reading paradigms and eye-tracking reveal exactly where processing difficulty spikes, making garden paths one of psycholinguistics' most productive empirical tools.
