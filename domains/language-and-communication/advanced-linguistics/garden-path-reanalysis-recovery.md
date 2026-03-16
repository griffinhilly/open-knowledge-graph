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

## Explainer

From your study of sentence parsing and psycholinguistics, you know that the parser — the mental system that assigns grammatical structure to incoming words — works incrementally, building interpretations word by word without waiting for the sentence to end. This incremental commitment is efficient but creates a specific failure mode: sometimes the structure built so far turns out to be wrong. Garden-path sentences are the experimental probe that reveals this failure most clearly.

Consider the classic example: *The horse raced past the barn fell.* Most readers hit the word *fell* and experience a brief but genuine comprehension failure — the sentence seems ungrammatical. This is the **garden-path effect**: you have been "led down the garden path" to an incorrect parse. What went wrong? After reading *the horse raced past the barn*, the parser has built a structure where *raced* is the main verb and the sentence is essentially complete. *fell* then has no home — there is no open position for it. The correct parse requires treating *raced past the barn* as a **reduced relative clause** (*the horse [that was] raced past the barn*), making *fell* the main verb. But the parser never considered this alternative initially, because the simpler analysis — main verb rather than reduced relative — was committed to first.

**Reanalysis** is the process of tearing down the committed structure and rebuilding it. This is computationally costly because the parser must: (1) detect that the current structure fails, (2) identify where the misparse began, (3) locate an alternative structural analysis, and (4) rebuild from the point of failure. The difficulty of reanalysis is not uniform — it depends on how much structure must be undone and whether the alternative parse was ever active as a competitor. If the garden path is "shallow" (a small local revision), recovery is fast. If it requires revising the main clause structure (a "global" garden path), recovery is slow and sometimes incomplete — some readers reject grammatical garden-path sentences as ungrammatical because they cannot successfully reanalyze.

The garden-path phenomenon reveals two fundamental parsing principles. First, the parser uses a **minimal attachment** strategy: when two structural analyses are available, it initially chooses the one requiring fewer syntactic nodes. This is a heuristic for computational efficiency — simpler structures are processed faster. Second, the parser is **commitment-based**: it does not maintain all possible analyses simultaneously (that would be computationally explosive) but instead commits early to the most preferred structure and revises only under pressure from disconfirming evidence. Garden-path sentences are the experiments that expose both the heuristic (which structure was preferred) and the cost of violating it (how hard reanalysis is). Reading-time studies show that these costs are real and measurable: self-paced reading paradigms and eye-tracking reveal exactly where processing difficulty spikes, making garden paths one of psycholinguistics' most productive empirical tools.
