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
stage: advanced
status: draft
---

# Parsing, Reanalysis, and Garden-Path Recovery

## Core Idea
Garden-path sentences initially guide readers toward an incorrect parse that must be revised when disambiguating information arrives. This reveals parsing as incremental, serial, and commitment-based; reanalysis is an active recovery mechanism when initial predictions fail.

## How It's Best Learned
Examine garden-path sentences and use eye-tracking to identify parsing difficulty at disambiguation; test reanalysis times and success rates across different types of temporary ambiguities.

## Common Misconceptions
Garden-path effects are not mere linguistic puzzles but windows into real-time parsing mechanisms; they reveal systematic biases in how the parser commits to structure.

## Explainer

From your study of garden-path sentences, you know that the human parser does not wait for a complete sentence before building syntactic structure — it processes words incrementally, committing to a structural interpretation as each word arrives. And from prediction in language processing, you know that the parser actively anticipates upcoming words based on prior context, probabilistic knowledge of the language, and real-world plausibility. Parsing, reanalysis, and garden-path recovery is where these two threads converge: what happens when incremental commitment and predictive processing lead the parser somewhere wrong?

The garden-path effect illustrates the cost of commitment. In a sentence like *The horse raced past the barn fell*, readers initially analyze *raced* as the main verb (the horse is doing the racing) — a natural early commitment, since simple active clauses are far more frequent than reduced relative clauses. When *fell* arrives, the main verb slot is already filled; the parser must **reanalyze** the structure, recognizing that *raced past the barn* is a reduced relative clause modifying *the horse* (*the horse that was raced past the barn*). This reanalysis is costly: readers slow down, make errors, and sometimes fail to recover entirely. The garden-path is the false path the parser was led down by its own probabilistic commitments.

**Reanalysis** as a cognitive operation involves several distinct sub-processes. The parser must first detect that its current structural representation is incompatible with new input — a process called **parsing failure detection**. It must then abandon or revise the committed structure, which requires accessing and re-evaluating decisions made earlier in the sentence. Finally, it must build a new, correct representation, often under continued time pressure as new words continue to arrive. Eye-tracking studies reveal that reanalysis is marked by **regressive saccades** (readers' eyes move back to earlier parts of the sentence) and **increased fixation times** at the disambiguation point — visible signatures of the cognitive work being done.

What determines whether reanalysis succeeds or fails? Several factors have been identified. **Structural complexity** matters: reanalysis is harder when the new structure requires more radical reorganization of the syntactic tree that had been built. **Distance** matters: the further back the parser must reach to find the element that needs reanalysis, the harder recovery becomes. **Working memory capacity** is a significant individual-differences predictor — readers with higher working memory span are better at reanalysis, suggesting that recovery requires holding the failed structure in mind while constructing the corrected one. And **semantic plausibility** provides a recovery cue: in *The horse raced past the barn*, the sentence is odd but interpretable in both parses; in *The evidence examined by the lawyer was damning*, the semantics (evidence cannot examine anything) provides an early signal that the reduced-relative interpretation is correct, easing reanalysis. These findings connect parsing to the broader picture of language processing as a probabilistic, resource-sensitive system that continuously trades off speed against accuracy — committing early to likely interpretations and paying a cost when those commitments turn out to be wrong.
