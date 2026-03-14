---
id: chromatic-polynomial
title: The Chromatic Polynomial
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: chromatic-number-bounds
  type: hard
builds-toward:
- edge-coloring-vizings-theorem
- list-coloring
tags:
- chromatic-polynomial
- deletion-contraction
- counting
stage: abstract-reasoning
status: draft
---

# The Chromatic Polynomial

## Core Idea
The chromatic polynomial P(G, k) counts proper k-colorings of G. It satisfies the deletion-contraction recurrence: P(G, k) = P(G−e, k) − P(G/e, k). The chromatic number χ(G) is the smallest k where P(G, k) > 0.

## How It's Best Learned
Compute chromatic polynomials for small graphs using deletion-contraction. Verify the formula P(K_n, k) = k(k−1)^(n−1) and use it to predict coloring counts.

## Common Misconceptions
- Confusing the chromatic polynomial (counts colorings) with the chromatic number (the minimum colors needed).
- Thinking the polynomial has a nice closed form for all graphs (only special families do).
