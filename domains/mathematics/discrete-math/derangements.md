---
id: derangements
title: Derangements and Fixed-Point-Free Permutations
domain: mathematics
course: discrete-math
prerequisites:
- id: permutations-and-arrangements
  type: hard
- id: inclusion-exclusion-principle
  type: soft
tags:
- combinatorics
- permutations
stage: formal-systems
status: draft
---

# Derangements and Fixed-Point-Free Permutations

## Core Idea
A derangement is a permutation where no element appears in its original position. The number of derangements D(n) satisfies the recurrence D(n) = (n-1)[D(n-1) + D(n-2)]. Derangements can be counted using the inclusion-exclusion principle.

## How It's Best Learned
Start with small cases (n=2,3,4) and count derangements by hand. Then derive the formula using inclusion-exclusion.

## Common Misconceptions
- Assuming D(n) = n! / 2 or other incorrect formulas.
- Confusing derangements with permutations with no fixed points in a general context.
- Not recognizing the connection to inclusion-exclusion.
