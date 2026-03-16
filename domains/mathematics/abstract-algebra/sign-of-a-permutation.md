---
id: sign-of-a-permutation
title: Sign of a Permutation
domain: mathematics
course: abstract-algebra
prerequisites:
- id: cycle-notation-and-decomposition
  type: hard
tags:
- sign
- parity
- permutations
stage: advanced
status: draft
---

# Sign of a Permutation

## Core Idea
A permutation is even if it is a product of an even number of transpositions, odd otherwise. The sign is +1 for even and −1 for odd. Sign is well-defined and sign(στ) = sign(σ)sign(τ), making the sign function a group homomorphism from S_n to {±1}.

## Explainer

From your work with cycle notation, you know every permutation in S_n can be written as a product of disjoint cycles. The **sign** (or **parity**) of a permutation adds another layer: it asks whether the permutation can be built from an even or odd number of **transpositions** — swaps of exactly two elements. The crucial theorem is that this parity is always the same regardless of which factorization into transpositions you use. There are infinitely many ways to write a given permutation as transpositions, but the count is always all-even or all-odd — never both.

The intuition: think of a permutation as rearranging elements into positions, where each transposition performs one "swap." Some arrangements require an even number of swaps to reach from the identity; others require an odd number. This is a rigid checkerboard property — there is no way to reach (12) from the identity using an even number of transpositions, and no way to reach (123) using an odd number. The parity is an intrinsic property of the permutation itself, not of the factorization.

To compute the sign using cycle notation, use the rule: a **k-cycle** is equivalent to k − 1 transpositions. So a transposition (2-cycle) contributes sign −1. A 3-cycle like (123) = (12)(13) contributes sign +1 (two transpositions, even). A 4-cycle contributes sign −1 (three transpositions, odd). For a permutation written as a product of disjoint cycles, multiply the signs: sign(σ) = ∏(−1)^(k_i − 1) over all cycles of length k_i. Fixed points are 1-cycles and contribute (−1)^0 = +1, so they do not affect parity.

The multiplicativity — sign(στ) = sign(σ)·sign(τ) — means the sign function is a **group homomorphism** from S_n to {+1, −1}. Its kernel is A_n, the **alternating group**, consisting of all even permutations. Since exactly half of all permutations are even, A_n has index 2 in S_n, making it the unique normal subgroup of index 2. This fact matters deeply: for n ≥ 5, A_n is simple (no proper normal subgroups), and this simplicity is the algebraic core of the proof that the general quintic polynomial cannot be solved by radicals.
