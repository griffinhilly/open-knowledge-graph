---
id: permutations
title: Permutations
domain: mathematics
course: algebra-2
prerequisites:
  - id: factorial
    type: hard
builds-toward:
  - combinations
  - probability-with-combinatorics
tags: [combinatorics, permutations, counting, order-matters]
stage: abstract-reasoning
status: draft
---

# Permutations

## Core Idea
A permutation is an arrangement of objects where order matters. The number of permutations of n objects taken r at a time is P(n,r) = n!/(n-r)!. For all n objects: P(n,n) = n!. The fundamental counting principle underlies permutations: if there are n1 choices for the first position, n2 for the second, etc., the total is n1 * n2 * ... Permutations with repetition, circular permutations, and permutations with identical objects are common extensions.

## How It's Best Learned
Start with concrete examples: how many ways to arrange 3 books on a shelf? Use the fundamental counting principle to derive the formula. Contrast with combinations (where order does not matter). Practice with word problems: race placements, seating arrangements, license plates.

## Common Misconceptions
- Confusing permutations (order matters) with combinations (order does not matter).
- Using the formula incorrectly when objects repeat.
- Thinking P(n,r) = n^r (that is the number of arrangements with replacement, not permutations).
- Not recognizing when a problem is a permutation problem vs. a combination problem.
