---
id: permutations-and-arrangements
title: Permutations and Ordered Arrangements
domain: mathematics
course: discrete-math
prerequisites:
- id: counting-principles-fundamentals
  type: hard
builds-toward:
- combinations-and-selections
- derangements
tags:
- combinatorics
- permutations
stage: formal-systems
status: draft
---

# Permutations and Ordered Arrangements

## Core Idea
A permutation is an ordered arrangement of objects where the sequence matters. The number of permutations of n distinct objects taken r at a time is P(n,r) = n!/(n-r)!. Permutations count the ways to select and arrange r items from n items when order is significant.

## How It's Best Learned
Use visual representations like seating arrangements, password creation, or race rankings. Compare small cases (2–3 objects) and count manually before deriving the formula.

## Common Misconceptions
- Confusing permutations with combinations (order matters in permutations!).
- Misapplying the factorial formula.
- Not reducing n!/(n-r)! correctly.
