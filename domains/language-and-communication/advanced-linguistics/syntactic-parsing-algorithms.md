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
