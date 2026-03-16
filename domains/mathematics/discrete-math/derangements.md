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

## Explainer

You already know what a permutation is: a rearrangement of n objects. A **derangement** is a permutation with one extra restriction — no object is allowed to land back in its own original position. Think of it as a secret-Santa gift exchange where no one is allowed to draw their own name. Every possible assignment is a permutation of participants; a derangement is one where nobody gives a gift to themselves.

The count of derangements D(n) can be derived using the inclusion-exclusion principle you've studied. Let A_i be the set of permutations where element i *is* in its original position (a "fixed point"). We want to count permutations where none of the A_i events occur — the complement. Inclusion-exclusion gives D(n) = n! − C(n,1)(n−1)! + C(n,2)(n−2)! − ⋯, which simplifies to the elegant formula D(n) = n! · Σ (−1)^k / k! for k = 0 to n. For large n, this sum converges to e⁻¹ ≈ 0.368, meaning roughly 37% of all permutations are derangements regardless of how large n grows.

There's also a satisfying recurrence: D(n) = (n − 1)[D(n − 1) + D(n − 2)]. You can derive it by considering where element 1 goes. It must go somewhere other than position 1 — say, position k. Now element k has two choices: go to position 1 (giving a derangement of the remaining n − 2 elements, contributing D(n − 2)) or not go to position 1 (effectively giving a derangement of n − 1 elements, contributing D(n − 1)). Since there are n − 1 choices for k, the total is (n − 1)(D(n − 1) + D(n − 2)).

Derangements appear throughout combinatorics in problems involving "forbidden positions." Any time you need to count arrangements where certain pairs are prohibited, the derangement framework generalizes naturally. The deeper lesson is how inclusion-exclusion turns a complicated constraint (nothing in its original slot) into a tractable alternating sum — and how a combinatorial identity and a limiting probability (1/e) can emerge from the same algebraic object.
