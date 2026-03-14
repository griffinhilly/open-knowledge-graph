---
id: subsequences
title: Subsequences
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-n-convergence
  type: hard
builds-toward:
- bolzano-weierstrass-theorem
- limit-superior-and-inferior
tags:
- subsequences
- convergence
- selections
stage: abstract-reasoning
status: draft
---

# Subsequences

## Core Idea
A subsequence of (aₙ) is a sequence (aₙₖ) where n₁ < n₂ < n₃ < ... A key fact: if (aₙ) converges to L, then every subsequence converges to L. Conversely, existence of convergent subsequences is a weaker property that allows us to extract convergence from non-convergent sequences.

## How It's Best Learned
Given (-1)ⁿ, identify its convergent subsequences: a₂ₖ → 1 and a₂ₖ₊₁ → -1. Extract a convergent subsequence from sin(n): though sin(n) oscillates chaotically, Bolzano-Weierstrass guarantees a convergent sub-sequence exists.

## Common Misconceptions
- Thinking a subsequence must be 'regular' (e.g., every other term); any selection with increasing indices counts.
- Assuming if a sequence diverges, no subsequence converges.
- Confusing the order: convergence ⟹ all subsequences converge, but not vice versa.
