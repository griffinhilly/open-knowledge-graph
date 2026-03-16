---
id: sign-permutation
title: Sign of a Permutation
domain: mathematics
course: abstract-algebra
prerequisites:
- id: cycle-notation-decomposition
  type: hard
builds-toward:
- dihedral-groups
tags:
- sign
- even
- odd
- alternating-group
stage: advanced
status: draft
---

# Sign of a Permutation

## Core Idea
A permutation is even if it is a product of an even number of transpositions, and odd if it is a product of an odd number of transpositions. The sign is well-defined: every decomposition into transpositions has the same parity. The alternating group Aₙ is the subgroup of even permutations.

## Explainer

You already know how to write permutations in cycle notation and decompose them into cycles of various lengths. The sign of a permutation extends this: it assigns a number — either +1 (even) or −1 (odd) — to each permutation based on how "entangled" the permutation is. The definition goes through **transpositions**, which are cycles of length 2 that simply swap two elements. Any permutation can be written as a product of transpositions (not uniquely), and the surprising theorem is that while the specific transpositions vary, their count always has the same parity.

To see why parity is preserved, consider what transpositions do to the number of inversions in a sequence. An **inversion** is a pair (i, j) with i < j but σ(i) > σ(j) — elements that are "out of order." Each transposition changes the number of inversions by an odd amount, so applying an even number of transpositions changes the inversion count by an even amount, and applying an odd number changes it by an odd amount. The parity of the inversion count is therefore an intrinsic property of the permutation — it does not depend on which decomposition into transpositions you choose. This is the well-definedness proof in disguise.

A useful shortcut connects cycle structure to sign. A single k-cycle can be decomposed into exactly k−1 transpositions: (a₁ a₂ ... aₖ) = (a₁ a₂)(a₁ a₃)···(a₁ aₖ). So a k-cycle is even when k is odd, and odd when k is even. For a permutation written as a product of disjoint cycles, sum the (length − 1) values across all cycles. If the total is even, the permutation is even; if odd, the permutation is odd. For example, a 3-cycle is even (3−1 = 2 transpositions), a 2-cycle (transposition) is odd, and the product of two disjoint 2-cycles is even.

The **alternating group** Aₙ is the set of all even permutations of {1, ..., n}. It is a subgroup of Sₙ of index 2, meaning exactly half the permutations in Sₙ are even. The sign function sgn: Sₙ → {+1, −1} is a group homomorphism — sgn(στ) = sgn(σ)·sgn(τ) — and Aₙ is its kernel. This structure becomes critical in the theory of determinants (where the sign of a permutation determines whether a term contributes +1 or −1) and in Galois theory, where A₄ and A₅ play starring roles because of whether they are solvable groups.
