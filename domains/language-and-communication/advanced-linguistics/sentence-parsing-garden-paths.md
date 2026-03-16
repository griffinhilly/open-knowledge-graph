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
builds-toward:
- working-memory-sentence-comprehension
tags:
- psycholinguistics
- parsing
- comprehension
stage: advanced
status: draft
---

# Sentence Parsing and Garden-Path Sentences

## Core Idea
Garden-path sentences like 'The horse raced past the barn fell' temporarily mislead comprehenders, who initially parse it as a main clause until 'fell' reveals a reduced relative clause structure. These sentences show that parsing uses incremental heuristics (minimal attachment) rather than considering all analyses simultaneously, and that comprehension involves reanalysis and recovery from initial misanalysis.

## Explainer

From your study of psycholinguistics, you know that language comprehension involves not just knowing grammar but processing sentences in real time under cognitive constraints. From your study of syntactic structure, you know that sentences have hierarchical phrase structure. Garden-path phenomena are what happen when those two facts collide: your parser commits to a syntactic structure based on early words, and that commitment turns out to be wrong.

Read this sentence slowly: *"The horse raced past the barn fell."* Most people get stuck at "fell" and need to reread. What happened? When you encountered "the horse raced," you built the parse *[NP the horse] [VP raced past the barn]*  — a main clause with "the horse" as subject and "raced" as main verb. That's a perfectly good parse of the words so far. But then "fell" arrives, and it can't be the next word in that sentence — there's no room for a second verb in a main clause. The only grammatical analysis is *[NP the horse [RC raced past the barn]] [VP fell]* — "the horse that was raced past the barn fell." This is a **reduced relative clause** (the "that was" has been deleted). Your parser took you down the wrong path and had to backtrack.

The principle behind the error is **minimal attachment**: when the parser encounters a structural ambiguity, it prefers the analysis that builds the simplest phrase structure — fewest nodes, most direct attachment. A main clause with "raced" as the main verb is structurally simpler than a relative clause modifying the subject; hence the default. **Late closure** is a related heuristic: new material is attached to the current phrase being built rather than starting a new one. These aren't flaws — they're efficient strategies that succeed the vast majority of the time. Most sentences don't have the ambiguous structure that produces garden paths; the heuristics are tuned to the statistics of normal language.

The garden-path effect has important implications for parsing models. A **serial parser** that builds one analysis at a time (like the standard explanation above) predicts the garden-path effect naturally: you commit to one parse, and when it fails, you reanalyze. A **parallel parser** that maintains all analyses simultaneously would not predict difficulty — you'd just switch to the right analysis without effort. The evidence from reading time studies and ERP (brain wave) data strongly favors the serial model with subsequent reanalysis: comprehenders show measurable difficulty exactly at the point of disambiguating "fell," suggesting they really do build and then repair the wrong structure. The cost of reanalysis depends on how far the parser has committed and how much structure must be discarded — a useful window into the computational architecture of sentence comprehension.
