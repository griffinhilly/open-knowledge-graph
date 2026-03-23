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
status: validated
---

# Cycle Notation and Decomposition

## Core Idea
Cycle notation is a compact way to write permutations. Every permutation can be uniquely written as a product of disjoint cycles. Every permutation is a product of transpositions, and the parity (odd or even number of transpositions) is invariant.

## Questions

```yaml
- question: "Two students decompose the 4-cycle (1 2 3 4) into transpositions differently. Student A writes (1 2)(1 3)(1 4) — three transpositions. Student B writes (1 4)(2 4)(3 4)(1 4)(2 4) — five transpositions. Which student, if either, is correct?"
  type: multiple-choice
  options:
    - "Student A only — the unique decomposition into transpositions uses exactly three"
    - "Student B only — a 4-cycle requires exactly five transpositions by the cycle-length rule"
    - "Both are correct — the decomposition into transpositions is not unique, but both use an odd number, preserving the correct parity"
    - "Neither is correct — a 4-cycle must be written as a product of exactly two transpositions"
  answer: 2
  explanation: "The decomposition of a permutation into transpositions is never unique — there are infinitely many ways to do it. What is invariant is the parity: a given permutation always decomposes into either an even or odd number of transpositions. A 4-cycle is an odd permutation (it takes k−1 = 3 transpositions in the standard formula, and 3 is odd). Both 3 and 5 are odd, so both students have correct, valid decompositions with consistent parity. Students often assume the decomposition must be unique — this question targets that misconception directly."

- question: "Is the permutation (1 2 3) in S₃ even or odd?"
  type: multiple-choice
  options:
    - "Odd — it moves three elements, one for each transposition needed"
    - "Even — it decomposes into two transpositions: (1 2)(1 3), which is an even number"
    - "Neither — a 3-cycle is its own inverse, so parity is undefined"
    - "Odd — any single cycle is an odd permutation by definition"
  answer: 1
  explanation: "A k-cycle decomposes as (a₁ a₂ ... aₖ) = (a₁ a₂)(a₁ a₃)···(a₁ aₖ), which requires k−1 transpositions. For a 3-cycle, that is 2 transpositions — an even number — making (1 2 3) an even permutation. The confusion in option A is a natural one: 'it moves three elements' sounds like it should take three transpositions, but the formula gives k−1, not k. Option D is incorrect: 2-cycles (transpositions) are odd; 3-cycles are even."

- question: "The decomposition of a permutation into transpositions is not unique, so a given permutation can sometimes be expressed using an even number of transpositions and sometimes an odd number of transpositions."
  type: true-false
  answer: false
  explanation: "This is the parity invariance theorem, and it is the key fact about transposition decompositions. While the specific transpositions used, their number, and their order are all non-unique, the *parity* — whether the total count is even or odd — is always the same for a given permutation. No permutation is simultaneously even and odd. This invariance is not obvious and requires proof; it is the foundation for the sign function sgn: Sₙ → {+1, −1} and the alternating group Aₙ."

- question: "Disjoint cycles in a permutation can be applied in any order without changing the result, because they act on completely separate sets of elements."
  type: true-false
  answer: true
  explanation: "Two cycles are disjoint if they involve no common elements. Since they act on entirely separate elements, the operations do not interact — applying one cycle has no effect on the elements the other cycle moves. Formally, disjoint cycles commute: (a b)(c d) = (c d)(a b) when {a,b} ∩ {c,d} = ∅. This is why the disjoint cycle decomposition of a permutation is so useful for computation: you can trace each element independently through its own cycle."

- question: "Why is the parity of a permutation well-defined, even though there are infinitely many ways to write the same permutation as a product of transpositions?"
  type: short-answer
  answer: "Parity is well-defined because of a topological or algebraic invariant that is preserved by every transposition: for instance, the sign of a permutation can be defined as the sign of the Vandermonde polynomial ∏(xᵢ − xⱼ) under the action of the permutation. Each transposition flips exactly one pair (xᵢ − xⱼ) to −(xᵢ − xⱼ), changing the sign. So every transposition toggles the sign exactly once. No matter how you factor a permutation into transpositions, each factor flips the sign once — so an even-count decomposition always leaves the sign unchanged (even permutation) and an odd-count decomposition always flips it (odd permutation). Because the final sign is determined by the permutation itself, not by the decomposition, parity is invariant."
```

## Explainer

From your work with permutation groups, you know that a permutation is a bijection from a set to itself — a relabeling of positions. Writing out a permutation as a full two-row table (top row: original positions, bottom row: where each goes) is cumbersome for large sets. **Cycle notation** compresses the information by describing orbits: chains of elements that get cyclically mapped into one another. Write (1 3 5) to mean 1 → 3 → 5 → 1. Every element not listed is fixed.

Two cycles are **disjoint** if they involve completely separate elements. The fundamental theorem of cycle decomposition says every permutation factors uniquely (up to ordering the cycles and starting position within each cycle) as a product of disjoint cycles. For example, the permutation sending 1→3, 2→2, 3→5, 4→1, 5→4 in S₅ decomposes as (1 3 5 4)(2). Disjoint cycles commute — you can apply them in any order because they act on different elements. This makes composition of disjoint cycles trivial: just chase each element through its own cycle.

A **transposition** is a 2-cycle (i j), swapping two elements and fixing all others. Any longer cycle decomposes into transpositions: (a₁ a₂ ... aₖ) = (a₁ a₂)(a₁ a₃)···(a₁ aₖ). This decomposition is not unique — there are many ways to write a given permutation as a product of transpositions. But here is the invariant: the **parity** of the number of transpositions is always the same for a given permutation. A permutation is **even** if it requires an even number of transpositions, **odd** if an odd number. A k-cycle is even when k is odd, and odd when k is even. (A 3-cycle is even because it takes 2 transpositions; a 2-cycle is odd because it takes 1.)

Parity is the key to the sign of a permutation, the determinant formula for signed permutations, and the definition of the alternating group Aₙ (the subgroup of all even permutations). The sign function sgn: Sₙ → {+1, −1} is a group homomorphism, with kernel Aₙ. The fact that parity is well-defined — that no permutation is simultaneously even and odd — requires proof, but the intuition is that every algebraic operation that "toggles" parity must do so consistently. This invariance will be the engine behind the sign of a permutation and eventually the Leibniz determinant formula.


