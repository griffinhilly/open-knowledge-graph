---
id: combinations-and-selections
title: Combinations and Unordered Selections
domain: mathematics
course: discrete-math
prerequisites:
- id: permutations-and-arrangements
  type: hard
builds-toward:
- binomial-coefficients
- multinomial-theorem
tags:
- combinatorics
- combinations
stage: formal-systems
status: draft
---

# Combinations and Unordered Selections

## Core Idea
A combination is an unordered selection of objects where the sequence does not matter. The number of combinations of n objects taken r at a time is C(n,r) = n! / (r!(n-r)!). Combinations count selections where we care only about which items are chosen, not their order.

## How It's Best Learned
Compare permutations and combinations side-by-side using the same scenario (e.g., selecting committee members). Show why dividing by r! removes the ordering.

## Common Misconceptions
- Mixing up C(n,r) and P(n,r).
- Incorrectly applying the formula or mishandling cancellation.
- Not recognizing when a problem requires unordered selection.
