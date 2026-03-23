---
id: parsing-reanalysis-recovery
title: Parsing, Reanalysis, and Garden-Path Recovery
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: sentence-parsing-garden-paths
  type: hard
- id: prediction-in-language-processing
  type: hard
tags:
- psycholinguistics
- parsing
- reanalysis
stage: expert
status: validated
---

# Parsing, Reanalysis, and Garden-Path Recovery

## Core Idea
Garden-path sentences initially guide readers toward an incorrect parse that must be revised when disambiguating information arrives. This reveals parsing as incremental, serial, and commitment-based; reanalysis is an active recovery mechanism when initial predictions fail.

## How It's Best Learned
Examine garden-path sentences and use eye-tracking to identify parsing difficulty at disambiguation; test reanalysis times and success rates across different types of temporary ambiguities.

## Common Misconceptions
Garden-path effects are not mere linguistic puzzles but windows into real-time parsing mechanisms; they reveal systematic biases in how the parser commits to structure.

## Questions

```yaml
- question: "Many readers initially parse 'The old man the boats' by treating 'old' as an adjective. Eye-tracking shows processing difficulty at 'the boats.' This demonstrates:"
  type: multiple-choice
  options:
    - "Readers have a general preference for adjectives regardless of syntactic context"
    - "The parser made an early probabilistic commitment to the most frequent structure (old = adjective modifying man) and must reanalyze when 'the boats' makes that structure impossible — incurring measurable processing cost"
    - "The sentence is grammatically ambiguous and therefore cannot be parsed at all"
    - "Working memory limitations prevent readers from tracking nouns across clause boundaries"
  answer: 1
  explanation: "The garden-path effect reveals that the parser is serial and commitment-based: it adopts the single most probable interpretation at each word and commits to it. Since 'old' overwhelmingly precedes a noun as an adjective in English, the parser makes that commitment. When 'the boats' arrives and makes the earlier structure impossible, the parser must reanalyze — treating 'man' as the verb and 'the old' as its subject. The processing cost (slowdown, regressive eye movements) is the signature of reanalysis work."

- question: "Readers recover from the garden-path significantly faster in 'The evidence examined by the lawyer was damning' than in 'The horse raced past the barn fell.' The most likely explanation is:"
  type: multiple-choice
  options:
    - "The first sentence is syntactically simpler — it contains fewer embedded clauses"
    - "Legal vocabulary is more familiar to most educated readers than equestrian vocabulary"
    - "Semantic plausibility provides an early recovery cue in the first sentence: since evidence cannot examine anything, the reduced-relative interpretation is strongly signaled before the disambiguation point, pre-cueing reanalysis"
    - "The second sentence contains unusually low-frequency vocabulary that slows processing independently"
  answer: 2
  explanation: "This finding demonstrates that semantic plausibility aids reanalysis. In 'The evidence examined…,' the semantics — evidence is not an agent capable of examining — signal before the end of the sentence that the reduced-relative parse ('evidence that was examined') must be correct, easing the revision. In 'The horse raced…,' both interpretations are semantically plausible (horses race and are raced), so no semantic cue aids recovery, and reanalysis depends entirely on structural revision at 'fell.'"

- question: "Readers with higher working memory capacity recover more successfully from garden-path sentences, supporting the claim that reanalysis requires holding the failed parse in memory while constructing a corrected one."
  type: true-false
  answer: true
  explanation: "Working memory capacity is one of the strongest individual-differences predictors of garden-path recovery. This is evidence that reanalysis is not a simple look-up but an active, resource-demanding process: the parser must retain the failed structure (to know what needs to be revised), identify where the structural error occurred, and rebuild a new representation — all while new words continue to arrive. Higher working memory allows more cognitive resources to be allocated to this simultaneous holding and rebuilding."

- question: "Garden-path effects occur because the parser simultaneously evaluates all possible syntactic parses and becomes confused when multiple interpretations are equally probable."
  type: true-false
  answer: false
  explanation: "This describes the parallel parsing hypothesis, which garden-path effects actually argue against. If the parser held all possible parses simultaneously, there would be no garden-path effect — the correct parse would always be active and available when disambiguating information arrived. The fact that readers show processing difficulty specifically at the disambiguation point, and require active reanalysis, is evidence for a serial, commitment-based parser that adopts a single interpretation early and pays a cost when it turns out to be wrong."

- question: "Why are garden-path sentences considered windows into real-time parsing mechanisms rather than mere linguistic curiosities? What specific architectural claim about parsing do they support?"
  type: short-answer
  answer: "Garden-path effects reveal that the parser processes sentences incrementally and serially, committing to the single most probable structural interpretation as each word arrives rather than waiting for full sentence context or entertaining multiple possibilities simultaneously. The commitment reflects systematic probabilistic biases: the parser prefers simple active clauses, attaches modifiers early, and acts on statistical regularities of the language. When these commitments turn out to be wrong, the processing cost is measurable and visible in eye-tracking data (regressive saccades, increased fixation times at the disambiguation point). The systematic nature of which sentences cause difficulty — and which contextual factors (semantic plausibility, working memory) aid recovery — reveals the architecture of the parsing system itself, not just surface properties of individual sentences."
  explanation: "This is why psycholinguists design garden-path studies deliberately: they use the errors and recovery patterns to reverse-engineer the normal parsing process. The failures are diagnostic in a way that successful, ambiguous comprehension cannot be."
```

## Explainer

From your study of garden-path sentences, you know that the human parser does not wait for a complete sentence before building syntactic structure — it processes words incrementally, committing to a structural interpretation as each word arrives. And from prediction in language processing, you know that the parser actively anticipates upcoming words based on prior context, probabilistic knowledge of the language, and real-world plausibility. Parsing, reanalysis, and garden-path recovery is where these two threads converge: what happens when incremental commitment and predictive processing lead the parser somewhere wrong?

The garden-path effect illustrates the cost of commitment. In a sentence like *The horse raced past the barn fell*, readers initially analyze *raced* as the main verb (the horse is doing the racing) — a natural early commitment, since simple active clauses are far more frequent than reduced relative clauses. When *fell* arrives, the main verb slot is already filled; the parser must **reanalyze** the structure, recognizing that *raced past the barn* is a reduced relative clause modifying *the horse* (*the horse that was raced past the barn*). This reanalysis is costly: readers slow down, make errors, and sometimes fail to recover entirely. The garden-path is the false path the parser was led down by its own probabilistic commitments.

**Reanalysis** as a cognitive operation involves several distinct sub-processes. The parser must first detect that its current structural representation is incompatible with new input — a process called **parsing failure detection**. It must then abandon or revise the committed structure, which requires accessing and re-evaluating decisions made earlier in the sentence. Finally, it must build a new, correct representation, often under continued time pressure as new words continue to arrive. Eye-tracking studies reveal that reanalysis is marked by **regressive saccades** (readers' eyes move back to earlier parts of the sentence) and **increased fixation times** at the disambiguation point — visible signatures of the cognitive work being done.

What determines whether reanalysis succeeds or fails? Several factors have been identified. **Structural complexity** matters: reanalysis is harder when the new structure requires more radical reorganization of the syntactic tree that had been built. **Distance** matters: the further back the parser must reach to find the element that needs reanalysis, the harder recovery becomes. **Working memory capacity** is a significant individual-differences predictor — readers with higher working memory span are better at reanalysis, suggesting that recovery requires holding the failed structure in mind while constructing the corrected one. And **semantic plausibility** provides a recovery cue: in *The horse raced past the barn*, the sentence is odd but interpretable in both parses; in *The evidence examined by the lawyer was damning*, the semantics (evidence cannot examine anything) provides an early signal that the reduced-relative interpretation is correct, easing reanalysis. These findings connect parsing to the broader picture of language processing as a probabilistic, resource-sensitive system that continuously trades off speed against accuracy — committing early to likely interpretations and paying a cost when those commitments turn out to be wrong.
