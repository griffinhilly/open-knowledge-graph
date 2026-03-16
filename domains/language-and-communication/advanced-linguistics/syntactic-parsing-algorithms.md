---
id: syntactic-parsing-algorithms
title: Syntactic Parsing Algorithms and Models
domain: language-and-communication
course: advanced-linguistics
prerequisites:
- id: neural-language-models-theory
  type: hard
- id: minimalist-program-core-concepts
  type: hard
tags:
- computational-linguistics
- parsing
- algorithms
stage: advanced
status: draft
---

# Syntactic Parsing Algorithms and Models

## Core Idea
Parsing algorithms assign syntactic structure to sentences; methods range from chart parsing (dynamic programming) to shift-reduce transition-based models to neural sequence-to-sequence models. Different strategies (bottom-up vs. top-down, deterministic vs. non-deterministic) have different computational properties and varying psychological plausibility.

## How It's Best Learned
Implement simple parsers (chart, shift-reduce); evaluate parser output on treebanks; study how neural parsers learn distributed representations of context without explicit linguisic rules.

## Common Misconceptions
Parsing is not merely pattern-matching; successful parsers implement systematic disambiguation strategies and exploit linguistic structure, not just surface patterns.

## Explainer

Parsing is the problem of recovering structure from a sequence. You are given a string of words and must determine which syntactic structure it expresses. This sounds deceptively simple — but natural language is massively **ambiguous**. The sentence "I saw the man with the telescope" has at least two readings (did you use the telescope to see, or does the man have a telescope?). A parser must find a principled way to handle such ambiguity, either by maintaining multiple competing analyses simultaneously or by committing early and being prepared to backtrack.

**Chart parsing**, the classical dynamic-programming approach, avoids redundant computation by storing intermediate results in a data structure called a chart. Instead of re-analyzing the substring "the man" every time it appears as a potential constituent, the parser records the analysis once and retrieves it. The **CYK algorithm** (Cocke-Younger-Kasami) is the canonical example: it works bottom-up, combining smaller constituents into larger ones, and runs in O(n³) time for a sentence of length n. Chart parsers are complete (they find all analyses) and systematic, but they can be slow for long sentences and produce exponentially many analyses for ambiguous inputs. From your study of the minimalist program you know that linguistic structure is binary-branching; chart parsers respect this, but they don't exploit the specific organizational principles (like the requirement that heads project) that linguistic theory specifies.

**Shift-reduce parsing** (also called transition-based parsing) takes a different approach: instead of exploring all analyses simultaneously, it makes greedy sequential decisions. At each step, the parser either shifts the next word onto a stack or reduces the top elements of the stack into a constituent. It is fast — linear time — but depends entirely on the quality of its decisions. In human psycholinguistics, this maps onto the **garden-path phenomenon**: sentences like "The horse raced past the barn fell" are hard because readers make a shift-reduce commitment early (treating "raced" as the main verb) and must expensively backtrack when "fell" contradicts that analysis.

**Neural parsers**, which you've prepared for through your study of neural language models, learn parsing decisions from annotated treebanks rather than explicit grammatical rules. A sequence-to-sequence model can produce constituency trees or dependency graphs by treating parsing as a sequence prediction problem. The striking finding is that neural models achieve state-of-the-art parsing accuracy despite having no explicit linguistic rules — they learn statistical regularities in how words co-occur in syntactic positions. This creates a productive tension with the linguistically-motivated approaches: neural parsers work exceptionally well empirically, but it is often unclear *what* they have learned. Probing studies attempt to interrogate neural representations — do the hidden states implicitly encode phrase structure? The answers are partial and debated, which is why the field increasingly pursues hybrid models that combine the empirical success of neural methods with the interpretability and theoretical commitments of symbolic linguistic structure.
