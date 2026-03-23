---
id: permutation-groups
title: Permutation Groups
domain: mathematics
course: abstract-algebra
prerequisites:
- id: group-definition-examples
  type: hard
builds-toward:
- cycle-notation-decomposition
- sign-permutation
- dihedral-groups
- cayley-theorem
tags:
- permutations
- Sₙ
- symmetric-group
- bijections
stage: advanced
status: validated
---

# Permutation Groups

## Core Idea
The symmetric group Sₙ is the group of all bijections (permutations) of an n-element set under composition. Permutation groups are fundamental: every finite group is a subgroup of some symmetric group. The order of Sₙ is n!.

## Questions

```yaml
- question: "Let σ and τ be permutations of {1, 2, 3} where σ maps 1→2, 2→3, 3→1 and τ maps 1→2, 2→1, 3→3. What is the value of (σ∘τ)(1), where ∘ denotes composition (apply τ first, then σ)?"
  type: multiple-choice
  options:
    - "1"
    - "2"
    - "3"
    - "Composition is undefined because σ and τ conflict."
  answer: 2
  explanation: "To compute (σ∘τ)(1): first apply τ to 1, giving τ(1) = 2; then apply σ to that result, giving σ(2) = 3. So (σ∘τ)(1) = 3. Notice that (τ∘σ)(1) = τ(σ(1)) = τ(2) = 1, which is different. This confirms that S₃ is non-abelian: σ∘τ ≠ τ∘σ. The order in which you apply permutations matters, just as it does for rotations in 3D space."

- question: "Cayley's theorem states that every finite group is isomorphic to a subgroup of Sₙ for some n. What is the most significant practical and conceptual implication of this theorem?"
  type: multiple-choice
  options:
    - "It proves that all finite groups are abelian, since permutation groups are abelian."
    - "Every abstract finite group can be concretely realized as a group of rearrangements of some set, so no finite group is truly 'exotic' — a permutation model always exists."
    - "It shows that all groups must have order n! for some integer n."
    - "It implies that studying Sₙ is sufficient to understand all of mathematics."
  answer: 1
  explanation: "Cayley's theorem is an embedding result: it guarantees that even the most abstractly-defined finite group — specified only by its multiplication table — can be faithfully represented as permutations of some set. This provides a concrete computational handle on any abstract group. Note that S₃ is already non-abelian, so the theorem definitely does not imply all groups are abelian. The order of a group embedded in Sₙ divides n!, but need not equal n!."

- question: "The symmetric group S₃ is non-abelian, meaning that the order in which two permutations are composed affects the result."
  type: true-false
  answer: true
  explanation: "S₃ is the smallest non-abelian group. It has 3! = 6 elements, and there exist permutations σ, τ ∈ S₃ such that σ∘τ ≠ τ∘σ. For example, a cyclic rotation and a transposition in S₃ do not commute, as the computation above demonstrates. For n ≥ 3, Sₙ is always non-abelian. S₁ and S₂ are trivially abelian (they have only 1 and 2 elements, respectively)."

- question: "The symmetric group S₄ has 16 elements."
  type: true-false
  answer: false
  explanation: "The order of Sₙ is n!, the number of ways to arrange n distinct objects. For S₄: |S₄| = 4! = 4 × 3 × 2 × 1 = 24, not 16. This is a common error — 16 = 2⁴ might arise from thinking each of 4 elements has 2 choices, but each element in a permutation is sent to a distinct image, so the count is n × (n-1) × (n-2) × ⋯ × 1. S₂ has 2 elements, S₃ has 6, S₄ has 24, S₅ has 120."

- question: "Why does the order of composition matter in permutation groups (for n ≥ 3), and what algebraic property does this illustrate?"
  type: short-answer
  answer: "Permutation composition is not commutative in general: applying permutation σ then τ can give a different result than applying τ then σ. This illustrates the non-abelian property: a group G is abelian if ab = ba for all elements, and non-abelian if this fails for some pair. In Sₙ (n ≥ 3), one can always find a cyclic rotation σ and a transposition τ such that σ∘τ ≠ τ∘σ. The result of sequentially rearranging a set depends on which rearrangement is done first — just as rotating then reflecting a physical object gives a different orientation than reflecting then rotating."
  explanation: "Non-abelian structure is one of the most important features of groups in algebra and physics. Sₙ is the prototype example — students first encounter non-commutativity here, which prepares them for matrix groups, Lie groups, and the symmetry groups of particles in physics. Cayley's theorem ensures this example is not exotic: it represents every finite group."
```

## Explainer

A **permutation** of a set is simply a rearrangement — a bijection from the set to itself. If your set is {1, 2, 3}, one permutation sends 1→2, 2→3, 3→1 (a cyclic rotation) and another sends 1→2, 2→1, 3→3 (a swap, called a **transposition**). From your study of the group axioms, you can verify that the set of all permutations of an n-element set forms a group under function composition: composing two bijections gives a bijection, the identity permutation acts as the identity element, and every bijection has an inverse (the reverse mapping). This group is the **symmetric group** Sₙ.

The order of Sₙ is n!, since there are n! ways to arrange n distinct objects. S₂ has just 2 elements; S₃ has 6; S₄ has 24. Even S₃ is already non-abelian: if σ rotates {1,2,3} cyclically and τ swaps 1 and 2, then σ∘τ and τ∘σ send elements to different places. This makes Sₙ the first natural source of non-abelian groups in abstract algebra. Every multiplication table you can draw for a 6-element non-abelian group will turn out to be the table of S₃ — it is the unique non-abelian group of order 6.

The symmetric group is important far beyond combinatorics. **Cayley's theorem** states that every finite group is isomorphic to a subgroup of Sₙ for some n. This means permutation groups are *universal*: any abstract finite group can be concretely realized as a group of rearrangements. Rather than reasoning about arbitrary groups in the abstract, you can always find a copy inside some Sₙ and compute by shuffling elements of a set. This is analogous to the way every finite-dimensional vector space can be realized as ℝⁿ — a concrete coordinate model always exists.

A key subgroup of Sₙ is the **alternating group** Aₙ, consisting of all "even" permutations — those expressible as a product of an even number of transpositions. Aₙ has order n!/2 and plays a central role in Galois theory: the fact that A₅ is simple (has no normal subgroups) is the reason no general formula exists for solving quintic equations. For now, the main skill to develop is fluency with permutation composition — writing permutations explicitly, composing them left-to-right or right-to-left consistently, and recognizing that the result depends on the order of composition.
