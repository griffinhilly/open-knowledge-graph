---
id: chromatic-number-bounds
title: Chromatic Number and Bounds
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: graph-coloring
  type: hard
builds-toward:
- brooks-theorem
- chromatic-polynomial
- edge-coloring-vizings-theorem
tags:
- chromatic-number
- bounds
- coloring
stage: abstract-reasoning
status: draft
---

# Chromatic Number and Bounds

## Core Idea
The chromatic number χ(G) is the minimum colors needed to properly color vertices. Bounds on χ(G) include the clique number (ω(G) ≤ χ(G)), degree-based bounds (χ(G) ≤ Δ(G) + 1), and tighter bounds for special graph classes. Understanding these bounds is essential for both theoretical study and practical approximation.

## How It's Best Learned
Compute lower bounds using clique size and upper bounds using greedy coloring on diverse graph families. Compare tight bounds (e.g., odd cycles) with loose bounds (e.g., sparse graphs).

## Common Misconceptions
- Assuming the clique number and chromatic number are equal (they are not; ω(G) ≤ χ(G) is strict for many graphs).
- Thinking greedy coloring always produces an optimal coloring (it often does not; the order matters).
