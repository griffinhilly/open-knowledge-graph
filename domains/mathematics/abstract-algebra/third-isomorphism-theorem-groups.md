---
id: third-isomorphism-theorem-groups
title: Third Isomorphism Theorem for Groups
domain: mathematics
course: abstract-algebra
prerequisites:
- id: first-isomorphism-theorem-groups
  type: hard
tags:
- isomorphism-theorem
- normal-subgroups
stage: advanced
status: validated
---

# Third Isomorphism Theorem for Groups

## Core Idea
If N and M are normal subgroups of G with N ⊆ M, then M/N is a normal subgroup of G/N, and (G/N)/(M/N) ≅ G/M.

## Questions

```yaml
- question: "Let G = ℤ, N = 12ℤ, M = 4ℤ (so 12ℤ ⊆ 4ℤ). What does the Third Isomorphism Theorem say about (ℤ/12ℤ)/(4ℤ/12ℤ)?"
  type: multiple-choice
  options:
    - "It is isomorphic to ℤ/12ℤ, since we are quotienting a subgroup of ℤ/12ℤ"
    - "It is isomorphic to ℤ/4ℤ ≅ ℤ₄, since the 12ℤ's cancel, leaving ℤ/4ℤ"
    - "It is isomorphic to ℤ/48ℤ, since 12 × 4 = 48"
    - "It cannot be determined without explicitly computing the elements of ℤ/12ℤ"
  answer: 1
  explanation: "The Third Isomorphism Theorem gives (G/N)/(M/N) ≅ G/M. With G = ℤ, N = 12ℤ, M = 4ℤ, we get (ℤ/12ℤ)/(4ℤ/12ℤ) ≅ ℤ/4ℤ ≅ ℤ₄. The 12ℤ's cancel, leaving ℤ/4ℤ. Concretely: inside ℤ₁₂ = {0,1,...,11}, the subgroup 4ℤ/12ℤ = {0,4,8} has three elements, so the quotient has 12/3 = 4 cosets — confirming ℤ₄."

- question: "In the proof of the Third Isomorphism Theorem, the map φ: G/N → G/M defined by φ(gN) = gM is well-defined because:"
  type: multiple-choice
  options:
    - "Every group homomorphism between quotient groups is automatically well-defined by the universal property of quotients"
    - "N ⊆ M implies that if gN = g′N then g′g⁻¹ ∈ N ⊆ M, so gM = g′M — the coset representative choice does not affect the output"
    - "The map is well-defined because G/N and G/M have a canonical bijection between their underlying sets"
    - "Well-definedness follows from the fact that ker(φ) = M/N is a normal subgroup of G/N"
  answer: 1
  explanation: "Well-definedness requires showing φ doesn't depend on the choice of coset representative. If gN = g′N then g′g⁻¹ ∈ N. Because N ⊆ M, this means g′g⁻¹ ∈ M, so gM = g′M, so φ(gN) = φ(g′N). The containment N ⊆ M is precisely what makes this work — cosets of N are finer than cosets of M, so the 're-coset' map is consistent. Without N ⊆ M the map would not be well-defined."

- question: "The Third Isomorphism Theorem is an independent result requiring its own proof technique, separate from the other isomorphism theorems."
  type: true-false
  answer: false
  explanation: "The Third Isomorphism Theorem follows directly from the First Isomorphism Theorem. The proof constructs a surjective homomorphism φ: G/N → G/M, identifies its kernel as M/N, and applies the First Isomorphism Theorem to conclude (G/N)/ker(φ) = (G/N)/(M/N) ≅ G/M. The isomorphism theorems form a coherent family built on the First Theorem and the kernel-image correspondence — they are not independent facts."

- question: "The condition N ⊆ M in the Third Isomorphism Theorem ensures that every coset of M is a union of cosets of N, making M/N a well-defined subgroup inside G/N."
  type: true-false
  answer: true
  explanation: "Because N ⊆ M, the cosets of N partition G more finely than the cosets of M — each coset of M is a disjoint union of cosets of N. This is the geometric content of the containment condition: N-cosets are 'smaller' and fit inside M-cosets. This guarantees that M/N = {mN : m ∈ M} is a well-defined collection of cosets in G/N, and that the map φ(gN) = gM respects coset structure."

- question: "Explain the 'cancellation' intuition for the Third Isomorphism Theorem (G/N)/(M/N) ≅ G/M, and why it is appropriate to think of it as analogous to cancelling fractions."
  type: short-answer
  answer: "Just as (a/b)/(c/b) = a/c because the b's cancel, the theorem says that dividing G/N by M/N gives G/M — the N's cancel. The intuition is that factoring out N from both the group and the subgroup, then taking the quotient, is equivalent to simply factoring out M from G directly. The N that was introduced into both layers washes out, leaving G/M."
  explanation: "The fraction analogy is more than a mnemonic — it reflects the actual algebraic structure. The 'cancellation' is validated by the explicit isomorphism constructed in the proof: φ(gN) = gM is surjective with kernel M/N, so by the First Isomorphism Theorem (G/N)/(M/N) ≅ G/M. The practical payoff is that computing the potentially complicated double quotient (G/N)/(M/N) can be replaced by the simpler computation G/M."
```

## Explainer

The Third Isomorphism Theorem is easiest to understand through a familiar arithmetic analogy. Consider the integers ℤ, with the subgroups 2ℤ ⊆ 6ℤ. Here N = 6ℤ and M = 2ℤ. The quotient ℤ/6ℤ ≅ ℤ₆ is the integers mod 6. Inside ℤ₆, the subgroup 2ℤ/6ℤ = {0, 2, 4} ≅ ℤ₃ is the even residues mod 6. The theorem says (ℤ/6ℤ)/(2ℤ/6ℤ) ≅ ℤ/2ℤ — that is, ℤ₆ modulo its subgroup {0, 2, 4} gives ℤ₂. Check: ℤ₆/{0,2,4} has cosets {0,2,4} and {1,3,5}, giving a two-element group. And ℤ/2ℤ ≅ ℤ₂. The theorem is confirmed.

The intuition is cancellation, like fractions: (G/N)/(M/N) behaves like "G over M", with the N's cancelling. The N that was introduced into the denominator of both quotient groups washes out, leaving G/M. This is why the Third Isomorphism Theorem is sometimes stated as a "cancellation law" for quotient groups.

To prove it, the **First Isomorphism Theorem** is the main tool. You already know that if φ: G → H is a surjective homomorphism with kernel K, then G/K ≅ H. Here, define a map φ: G/N → G/M by φ(gN) = gM — that is, "re-coset" each coset of N into a coset of M. Because N ⊆ M, every coset of M is a union of cosets of N, so this map is well-defined. It is clearly surjective (every coset gM is hit). Its kernel consists of all cosets gN such that gM = eM, i.e., g ∈ M, i.e., gN ∈ M/N. So ker(φ) = M/N. By the First Isomorphism Theorem, (G/N)/ker(φ) ≅ G/M, which is exactly (G/N)/(M/N) ≅ G/M.

The practical significance is that the Third Isomorphism Theorem lets you "factor" quotient groups: instead of computing (G/N)/(M/N) directly, you can compute the simpler G/M. It also reinforces a general lesson in abstract algebra: the isomorphism theorems are not independent facts to memorize but a coherent family of tools built on the First Isomorphism Theorem and the kernel-image correspondence.
