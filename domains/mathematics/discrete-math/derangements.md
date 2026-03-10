---
id: derangements
title: 'Derangements: Permutations with No Fixed Points'
domain: mathematics
course: discrete-math
prerequisites:
- id: permutations
  type: hard
- id: inclusion-exclusion-principle
  type: hard
- id: mathematical-induction
  type: soft
tags:
- derangements
- permutations
- counting
- combinatorics
- fixed-points
stage: formal-systems
status: draft
---

# Derangements: Permutations with No Fixed Points

## Core Idea
A derangement of n elements is a permutation where no element appears in its original position. The number of derangements is Dₙ = n! ∑(−1)ᵏ/k! for k from 0 to n, derived by applying the inclusion-exclusion principle to subtract permutations fixing at least one element. As n increases, the probability that a random permutation is a derangement approaches 1/e ≈ 36.8%, an elegant and surprising result. Derangements satisfy the recurrence Dₙ = (n−1)(Dₙ₋₁ + Dₙ₋₂).

## How It's Best Learned
Build the sequence iteratively: D₁=0, D₂=1, D₃=2, verifying the recurrence. Then derive the closed form using inclusion-exclusion. The classic 'hat-check' or 'mixed-up letters' story motivates the problem before any formalism.

## Common Misconceptions
- Confusing derangements with all permutations — the condition is strict: every single element must move.
- Thinking the limit 1/e means exactly 1/e of all permutations are derangements for every n — it's an asymptotic result.
