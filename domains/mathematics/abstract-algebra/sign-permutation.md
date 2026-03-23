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
status: validated
---

# Sign of a Permutation

## Core Idea
A permutation is even if it is a product of an even number of transpositions, and odd if it is a product of an odd number of transpositions. The sign is well-defined: every decomposition into transpositions has the same parity. The alternating group Aₙ is the subgroup of even permutations.

## Questions

```yaml
- question: "Student A writes σ = (1 2 3 4) as a product of 3 transpositions and concludes σ is odd. Student B writes the same permutation as a product of 5 transpositions and also concludes σ is odd. Student C insists there must exist a decomposition into 4 transpositions, making σ even. Who is correct?"
  type: multiple-choice
  options:
    - "Student C — four-cycles must be even because 4 is even"
    - "Students A and B — σ is odd, and the well-definedness theorem guarantees every decomposition has odd parity"
    - "All three could be right, depending on which transpositions are chosen"
    - "Student C — every permutation has a decomposition into an even number of transpositions"
  answer: 1
  explanation: "The well-definedness theorem is the heart of this topic: while permutations have infinitely many decompositions into transpositions, the parity of the count is always the same. For a 4-cycle (a b c d), the decomposition (a b)(a c)(a d) uses 3 transpositions — odd parity. Any other decomposition must also use an odd number. The proof goes through inversions: each transposition changes the inversion count by an odd amount, so the parity of the total change is determined by the number of transpositions applied, independent of which ones. Student C's claim is simply false — there is no even-length decomposition of a 4-cycle."

- question: "What is the sign of the permutation σ = (1 2 3)(4 5) in S₅?"
  type: multiple-choice
  options:
    - "+1 (even) — the two cycles together involve 5 elements, and 5 is odd"
    - "−1 (odd) — the 3-cycle decomposes into 2 transpositions (even) and the 2-cycle is 1 transposition (odd), giving 3 total transpositions (odd parity)"
    - "+1 (even) — the 3-cycle and the 2-cycle have opposite parities that cancel"
    - "−1 (odd) — all non-trivial permutations in S₅ are odd"
  answer: 1
  explanation: "A k-cycle decomposes into exactly k−1 transpositions. The 3-cycle (1 2 3) needs 3−1 = 2 transpositions (even); the 2-cycle (4 5) needs 2−1 = 1 transposition (odd). Total: 2 + 1 = 3 transpositions. Since 3 is odd, σ is an odd permutation with sign −1. The sign function is a homomorphism, so sgn(σ) = sgn((1 2 3)) · sgn((4 5)) = (+1)(−1) = −1. The common mistake is thinking that a 3-cycle is 'odd' because 3 is odd — but a k-cycle has parity (k−1), so a 3-cycle is *even*."

- question: "A 5-cycle such as (1 2 3 4 5) is an even permutation."
  type: true-false
  answer: true
  explanation: "A k-cycle decomposes into k−1 transpositions. For k = 5, that is 4 transpositions. Since 4 is even, a 5-cycle is an even permutation. The general rule: a k-cycle is even when k is odd, and odd when k is even. Mnemonically, 'odd-length cycles are even' — which is counterintuitive but follows directly from the k−1 transposition formula. This is why 3-cycles are even (they are in A₃ and A₄) while transpositions (2-cycles) are odd."

- question: "The sign of a permutation depends on which specific decomposition into transpositions you choose — different decompositions may yield different parities."
  type: true-false
  answer: false
  explanation: "This is the key well-definedness theorem: parity is an intrinsic property of the permutation, not of any particular decomposition. The proof uses inversions: an inversion is a pair (i, j) with i < j but σ(i) > σ(j). Each transposition changes the inversion count by an odd number, so the parity of the inversion count changes with each transposition. The total parity of the inversion count after all transpositions have been applied depends only on whether an even or odd number of transpositions was used. Since the inversion count of the identity is 0 (even), any product of transpositions equal to the identity must have even length — from which well-definedness follows."

- question: "Why does a k-cycle have sign (−1)^(k−1), and what does this tell you about whether a 3-cycle is even or odd?"
  type: short-answer
  answer: "A k-cycle (a₁ a₂ ··· aₖ) can be decomposed into exactly k−1 transpositions: (a₁ a₂)(a₁ a₃)···(a₁ aₖ). Since sign is a homomorphism and each transposition has sign −1, the sign of the k-cycle is (−1)^(k−1). For k = 3: sign = (−1)² = +1, so a 3-cycle is even. This means 3-cycles belong to the alternating group A₃ (and A₄, Aₙ for n ≥ 3)."
  explanation: "The formula (−1)^(k−1) captures the counterintuitive pattern: odd-length cycles are even permutations, and even-length cycles are odd permutations. Transpositions (k=2) have sign −1 (odd); 3-cycles have sign +1 (even); 4-cycles have sign −1 (odd). For a product of disjoint cycles, sum the (k−1) values across all cycles — if the total is even, the permutation is even."
```

## Explainer

You already know how to write permutations in cycle notation and decompose them into cycles of various lengths. The sign of a permutation extends this: it assigns a number — either +1 (even) or −1 (odd) — to each permutation based on how "entangled" the permutation is. The definition goes through **transpositions**, which are cycles of length 2 that simply swap two elements. Any permutation can be written as a product of transpositions (not uniquely), and the surprising theorem is that while the specific transpositions vary, their count always has the same parity.

To see why parity is preserved, consider what transpositions do to the number of inversions in a sequence. An **inversion** is a pair (i, j) with i < j but σ(i) > σ(j) — elements that are "out of order." Each transposition changes the number of inversions by an odd amount, so applying an even number of transpositions changes the inversion count by an even amount, and applying an odd number changes it by an odd amount. The parity of the inversion count is therefore an intrinsic property of the permutation — it does not depend on which decomposition into transpositions you choose. This is the well-definedness proof in disguise.

A useful shortcut connects cycle structure to sign. A single k-cycle can be decomposed into exactly k−1 transpositions: (a₁ a₂ ... aₖ) = (a₁ a₂)(a₁ a₃)···(a₁ aₖ). So a k-cycle is even when k is odd, and odd when k is even. For a permutation written as a product of disjoint cycles, sum the (length − 1) values across all cycles. If the total is even, the permutation is even; if odd, the permutation is odd. For example, a 3-cycle is even (3−1 = 2 transpositions), a 2-cycle (transposition) is odd, and the product of two disjoint 2-cycles is even.

The **alternating group** Aₙ is the set of all even permutations of {1, ..., n}. It is a subgroup of Sₙ of index 2, meaning exactly half the permutations in Sₙ are even. The sign function sgn: Sₙ → {+1, −1} is a group homomorphism — sgn(στ) = sgn(σ)·sgn(τ) — and Aₙ is its kernel. This structure becomes critical in the theory of determinants (where the sign of a permutation determines whether a term contributes +1 or −1) and in Galois theory, where A₄ and A₅ play starring roles because of whether they are solvable groups.
