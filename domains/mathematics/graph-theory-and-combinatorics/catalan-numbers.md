---
id: catalan-numbers
title: Catalan Numbers and Recursive Structures
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: generating-functions-advanced
  type: soft
tags:
- combinatorics
- sequences
stage: abstract-reasoning
status: draft
---

# Catalan Numbers and Recursive Structures

## Core Idea
The Catalan numbers Cₙ = (1/(n+1))C(2n,n) count binary trees, proper parenthesizations, non-crossing matchings, plane partitions, and more. The generating function C(x) = (1 - √(1-4x))/2x satisfies xC(x)² - C(x) + 1 = 0, encoding recursive structure. Catalan numbers exemplify how generating functions reveal hidden recursive patterns.

## How It's Best Learned
Derive the Catalan recurrence Cₙ₊₁ = Σ CᵢCₙ₋ᵢ by analyzing how structures decompose, then verify the closed form via generating functions.

## Common Misconceptions
Catalan numbers appear in many contexts, but each involves a specific recursive decomposition; not every sequence of sizes gives Catalan numbers.
