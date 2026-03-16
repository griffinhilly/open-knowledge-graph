---
id: cycle-notation-decomposition
title: Cycle Notation and Decomposition
domain: mathematics
course: abstract-algebra
prerequisites:
- id: permutation-groups
  type: hard
builds-toward:
- sign-permutation
- dihedral-groups
tags:
- cycles
- disjoint-cycles
- transpositions
stage: advanced
status: draft
---

# Cycle Notation and Decomposition

## Core Idea
Cycle notation is a compact way to write permutations. Every permutation can be uniquely written as a product of disjoint cycles. Every permutation is a product of transpositions, and the parity (odd or even number of transpositions) is invariant.

## Explainer

From your work with permutation groups, you know that a permutation is a bijection from a set to itself — a relabeling of positions. Writing out a permutation as a full two-row table (top row: original positions, bottom row: where each goes) is cumbersome for large sets. **Cycle notation** compresses the information by describing orbits: chains of elements that get cyclically mapped into one another. Write (1 3 5) to mean 1 → 3 → 5 → 1. Every element not listed is fixed.

Two cycles are **disjoint** if they involve completely separate elements. The fundamental theorem of cycle decomposition says every permutation factors uniquely (up to ordering the cycles and starting position within each cycle) as a product of disjoint cycles. For example, the permutation sending 1→3, 2→2, 3→5, 4→1, 5→4 in S₅ decomposes as (1 3 5 4)(2). Disjoint cycles commute — you can apply them in any order because they act on different elements. This makes composition of disjoint cycles trivial: just chase each element through its own cycle.

A **transposition** is a 2-cycle (i j), swapping two elements and fixing all others. Any longer cycle decomposes into transpositions: (a₁ a₂ ... aₖ) = (a₁ a₂)(a₁ a₃)···(a₁ aₖ). This decomposition is not unique — there are many ways to write a given permutation as a product of transpositions. But here is the invariant: the **parity** of the number of transpositions is always the same for a given permutation. A permutation is **even** if it requires an even number of transpositions, **odd** if an odd number. A k-cycle is even when k is odd, and odd when k is even. (A 3-cycle is even because it takes 2 transpositions; a 2-cycle is odd because it takes 1.)

Parity is the key to the sign of a permutation, the determinant formula for signed permutations, and the definition of the alternating group Aₙ (the subgroup of all even permutations). The sign function sgn: Sₙ → {+1, −1} is a group homomorphism, with kernel Aₙ. The fact that parity is well-defined — that no permutation is simultaneously even and odd — requires proof, but the intuition is that every algebraic operation that "toggles" parity must do so consistently. This invariance will be the engine behind the sign of a permutation and eventually the Leibniz determinant formula.


