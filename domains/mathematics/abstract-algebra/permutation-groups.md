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
status: draft
---

# Permutation Groups

## Core Idea
The symmetric group Sₙ is the group of all bijections (permutations) of an n-element set under composition. Permutation groups are fundamental: every finite group is a subgroup of some symmetric group. The order of Sₙ is n!.

## Explainer

A **permutation** of a set is simply a rearrangement — a bijection from the set to itself. If your set is {1, 2, 3}, one permutation sends 1→2, 2→3, 3→1 (a cyclic rotation) and another sends 1→2, 2→1, 3→3 (a swap, called a **transposition**). From your study of the group axioms, you can verify that the set of all permutations of an n-element set forms a group under function composition: composing two bijections gives a bijection, the identity permutation acts as the identity element, and every bijection has an inverse (the reverse mapping). This group is the **symmetric group** Sₙ.

The order of Sₙ is n!, since there are n! ways to arrange n distinct objects. S₂ has just 2 elements; S₃ has 6; S₄ has 24. Even S₃ is already non-abelian: if σ rotates {1,2,3} cyclically and τ swaps 1 and 2, then σ∘τ and τ∘σ send elements to different places. This makes Sₙ the first natural source of non-abelian groups in abstract algebra. Every multiplication table you can draw for a 6-element non-abelian group will turn out to be the table of S₃ — it is the unique non-abelian group of order 6.

The symmetric group is important far beyond combinatorics. **Cayley's theorem** states that every finite group is isomorphic to a subgroup of Sₙ for some n. This means permutation groups are *universal*: any abstract finite group can be concretely realized as a group of rearrangements. Rather than reasoning about arbitrary groups in the abstract, you can always find a copy inside some Sₙ and compute by shuffling elements of a set. This is analogous to the way every finite-dimensional vector space can be realized as ℝⁿ — a concrete coordinate model always exists.

A key subgroup of Sₙ is the **alternating group** Aₙ, consisting of all "even" permutations — those expressible as a product of an even number of transpositions. Aₙ has order n!/2 and plays a central role in Galois theory: the fact that A₅ is simple (has no normal subgroups) is the reason no general formula exists for solving quintic equations. For now, the main skill to develop is fluency with permutation composition — writing permutations explicitly, composing them left-to-right or right-to-left consistently, and recognizing that the result depends on the order of composition.
