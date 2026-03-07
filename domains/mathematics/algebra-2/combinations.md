---
id: combinations
title: Combinations
domain: mathematics
course: algebra-2
prerequisites:
  - id: permutations
    type: hard
builds-toward:
  - binomial-theorem
  - probability-with-combinatorics
tags: [combinatorics, combinations, counting, order-irrelevant]
stage: abstract-reasoning
status: draft
---

# Combinations

## Core Idea
A combination is a selection of objects where order does not matter. The number of combinations of n objects taken r at a time is C(n,r) = n!/(r!(n-r)!). C(n,r) = P(n,r)/r! because each combination of r objects can be arranged in r! ways. C(n,r) = C(n, n-r) by symmetry. Combinations count subsets, committee selections, and any scenario where only the group membership matters, not the arrangement.

## How It's Best Learned
Contrast directly with permutations using the same scenario: choosing 3 people from 10 for a committee (combination) vs. choosing president, VP, and secretary (permutation). Derive C(n,r) from P(n,r) by dividing out the redundant orderings. Practice identifying whether a problem requires permutations or combinations. Connect to Pascal's Triangle and the binomial coefficients.

## Common Misconceptions
- Using permutations when combinations are appropriate (and vice versa).
- Thinking C(n,r) and P(n,r) are the same.
- Forgetting that C(n,0) = 1 (there is exactly one way to choose nothing).
- Not recognizing the symmetry C(n,r) = C(n, n-r).
