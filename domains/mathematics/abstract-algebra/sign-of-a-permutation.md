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
status: validated
---

# Sign of a Permutation

## Core Idea
A permutation is even if it is a product of an even number of transpositions, odd otherwise. The sign is +1 for even and −1 for odd. Sign is well-defined and sign(στ) = sign(σ)sign(τ), making the sign function a group homomorphism from S_n to {±1}.

## Questions

```yaml
- question: "A student decomposes the permutation (12345) into transpositions two different ways: one decomposition uses 4 transpositions, another uses 6. What can you conclude?"
  type: multiple-choice
  options:
    - "The student made an error in at least one decomposition, since the number of transpositions must be fixed"
    - "Both decompositions are valid, and both show that (12345) is an even permutation"
    - "The sign is undefined for this permutation because different decompositions give different counts"
    - "The permutation is even by one decomposition and odd by the other, so its sign cannot be determined"
  answer: 1
  explanation: "(12345) is a 5-cycle, contributing 5 − 1 = 4 transpositions, so it is an even permutation. The theorem guarantees that every factorization into transpositions for a given permutation has the same parity — both counts here are even (4 and 6). The number of transpositions is not fixed, but the parity (even or odd) is invariant. Options C and D describe what would hold if parity were not well-defined — but the well-definedness theorem rules this out."

- question: "What is the sign of the permutation (123)(45) in S₅?"
  type: multiple-choice
  options:
    - "+1, because the permutation has two cycles and 2 is even"
    - "+1, because (123) is an even cycle and it determines the sign"
    - "−1, because the total transposition count is odd: (3−1) + (2−1) = 3"
    - "−1, because (45) is a transposition with sign −1, which cancels the positive sign of (123)"
  answer: 2
  explanation: "Each k-cycle contributes k − 1 transpositions. The 3-cycle (123) contributes 2 transpositions (sign +1); the 2-cycle (45) contributes 1 transposition (sign −1). Total: 3 transpositions, odd, so sign = −1. Option A incorrectly counts cycles rather than transpositions. Option B is incomplete — all cycles must be accounted for. Option D states the right answer with a misleading explanation; the correct computation multiplies signs: (+1)(−1) = −1."

- question: "The sign of a permutation depends on which specific decomposition into transpositions you use, so different decompositions can yield different signs for the same permutation."
  type: true-false
  answer: false
  explanation: "The well-definedness of sign is the foundational theorem underlying this topic. While a permutation has infinitely many decompositions into transpositions, the parity of the count (even or odd) is an invariant — it never changes regardless of which decomposition is chosen. Different decompositions give different counts, but always all-even or all-odd for any given permutation. The sign is a property of the permutation, not of the decomposition."

- question: "A k-cycle is an odd permutation when k is even, and an even permutation when k is odd."
  type: true-false
  answer: true
  explanation: "A k-cycle decomposes into k − 1 transpositions. When k is even, k − 1 is odd, so the k-cycle has an odd number of transpositions — it is an odd permutation. When k is odd, k − 1 is even, so the k-cycle is even. Examples: a 2-cycle (transposition) is odd; a 3-cycle is even; a 4-cycle is odd; a 5-cycle is even. This rule is worth memorizing: even-length cycles are odd permutations, and odd-length cycles are even permutations."

- question: "Why does the well-definedness of the sign function matter for the construction of the alternating group Aₙ?"
  type: short-answer
  answer: "The alternating group Aₙ is defined as the kernel of the sign homomorphism — the set of all permutations with sign +1 (even permutations). For this definition to be mathematically meaningful, the sign must be a function: each permutation must have exactly one sign value, not different values depending on how it is decomposed. If parity were not well-defined, a permutation could be 'in Aₙ' by one decomposition and 'outside it' by another, making Aₙ an incoherent set. Well-definedness is what makes Aₙ a genuine subgroup with a definite membership criterion, and the sign a genuine group homomorphism from Sₙ to {±1}."
  explanation: "This connects to deeper structural facts: Aₙ has index 2 in Sₙ (exactly half of all permutations are even), making it the unique normal subgroup of index 2. For n ≥ 5, Aₙ is simple, which is the algebraic heart of the proof that there is no general radical formula for quintic polynomials."
```

## Explainer

From your work with cycle notation, you know every permutation in S_n can be written as a product of disjoint cycles. The **sign** (or **parity**) of a permutation adds another layer: it asks whether the permutation can be built from an even or odd number of **transpositions** — swaps of exactly two elements. The crucial theorem is that this parity is always the same regardless of which factorization into transpositions you use. There are infinitely many ways to write a given permutation as transpositions, but the count is always all-even or all-odd — never both.

The intuition: think of a permutation as rearranging elements into positions, where each transposition performs one "swap." Some arrangements require an even number of swaps to reach from the identity; others require an odd number. This is a rigid checkerboard property — there is no way to reach (12) from the identity using an even number of transpositions, and no way to reach (123) using an odd number. The parity is an intrinsic property of the permutation itself, not of the factorization.

To compute the sign using cycle notation, use the rule: a **k-cycle** is equivalent to k − 1 transpositions. So a transposition (2-cycle) contributes sign −1. A 3-cycle like (123) = (12)(13) contributes sign +1 (two transpositions, even). A 4-cycle contributes sign −1 (three transpositions, odd). For a permutation written as a product of disjoint cycles, multiply the signs: sign(σ) = ∏(−1)^(k_i − 1) over all cycles of length k_i. Fixed points are 1-cycles and contribute (−1)^0 = +1, so they do not affect parity.

The multiplicativity — sign(στ) = sign(σ)·sign(τ) — means the sign function is a **group homomorphism** from S_n to {+1, −1}. Its kernel is A_n, the **alternating group**, consisting of all even permutations. Since exactly half of all permutations are even, A_n has index 2 in S_n, making it the unique normal subgroup of index 2. This fact matters deeply: for n ≥ 5, A_n is simple (no proper normal subgroups), and this simplicity is the algebraic core of the proof that the general quintic polynomial cannot be solved by radicals.
