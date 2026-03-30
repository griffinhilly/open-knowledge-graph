---
id: reducibility-and-irreducibility
title: Reducibility and Irreducibility
domain: mathematics
course: representation-theory
prerequisites:
- id: group-representations
  type: hard
- id: equivalence-of-representations
  type: hard
builds-toward:
- schurs-lemma
- maschkes-theorem
- tensor-product-of-representations
- dual-representations
tags:
- irreducible-representation
- subrepresentation
- invariant-subspace
- complete-reducibility
stage: expert
status: validated
---

# Reducibility and Irreducibility

## Core Idea
A subrepresentation of ρ: G → GL(V) is a subspace W ⊆ V that is invariant under every ρ(g). A representation is **irreducible** if its only invariant subspaces are {0} and V itself — it cannot be broken into smaller pieces. Irreducible representations are the atoms of representation theory: under favorable conditions (characteristic zero, finite groups), every representation decomposes as a direct sum of irreducibles.

## Questions

```yaml
- question: "Consider the representation of ℤ/2ℤ on ℝ² where the generator acts by ρ(1) = [[1, 1], [0, 1]]. The subspace W = span{e₁} is invariant. Is this representation reducible?"
  type: multiple-choice
  options:
    - "No — the representation is irreducible because W is only one-dimensional"
    - "Yes — it is reducible because W is a proper invariant subspace, but it is not completely reducible because there is no invariant complement to W"
    - "Yes — it is reducible and completely reducible because every subspace of ℝ² has a complement"
    - "No — the representation is irreducible because ρ(1) is not diagonalizable"
  answer: 1
  explanation: "The representation is reducible since W = span{e₁} is a proper G-invariant subspace (ρ(1)e₁ = e₁ ∈ W). However, it is NOT completely reducible: there is no G-invariant complement to W. If U were such a complement, it would be spanned by some vector v = ae₁ + be₂ with b ≠ 0, and ρ(1)v = ae₁ + be₂ + be₁ = (a+b)e₁ + be₂. For U to be invariant, (a+b)e₁ + be₂ must be a scalar multiple of ae₁ + be₂, which forces b = 0 — contradiction. This is an example of a representation that is reducible but indecomposable."

- question: "Every one-dimensional representation is irreducible."
  type: true-false
  answer: true
  explanation: "A one-dimensional vector space V has only two subspaces: {0} and V itself. Both are trivially G-invariant. Since there are no proper nontrivial subspaces, the definition of irreducibility is vacuously satisfied. One-dimensional representations are always irreducible, regardless of the group or the field."

- question: "Why are irreducible representations considered the 'atoms' of representation theory?"
  type: short-answer
  answer: "Under Maschke's theorem conditions (finite group, characteristic zero or coprime to |G|), every representation decomposes uniquely as a direct sum of irreducible representations. So irreducibles are the building blocks from which all representations are constructed, analogous to prime numbers in arithmetic."
  explanation: "The analogy to prime factorization is precise: just as every positive integer factors uniquely into primes, every (finite-dimensional, semisimple) representation decomposes uniquely into irreducibles. Classifying all representations of a group therefore reduces to two problems: finding all irreducible representations, and understanding how they combine via direct sums. The first problem is solved by character theory; the second by tools like induced representations and tensor products."

- question: "A representation is called completely reducible if it is a direct sum of irreducible subrepresentations. Which of the following is NOT a condition that guarantees complete reducibility?"
  type: multiple-choice
  options:
    - "G is a finite group and the field has characteristic zero"
    - "G is a finite group and char(F) does not divide |G|"
    - "The representation is unitary (preserves an inner product)"
    - "The representation has prime dimension"
  answer: 3
  explanation: "Having prime dimension does not guarantee complete reducibility — a representation of prime dimension p could be indecomposable but reducible (containing a proper invariant subspace with no invariant complement). The other three conditions do guarantee complete reducibility: the first two are forms of Maschke's theorem, and unitarity allows you to take orthogonal complements of invariant subspaces, which are automatically invariant."
```

## Explainer

The idea of breaking a representation into simpler pieces is the heart of the subject. Given a representation ρ: G → GL(V), a **subrepresentation** (or invariant subspace) is a subspace W ⊆ V such that ρ(g)(W) ⊆ W for every g ∈ G — the action of G keeps W within itself. In matrix terms, if we choose a basis where the first k vectors span W, every ρ(g) takes block upper-triangular form with a k×k block in the top-left corner. That block defines a representation of G on W.

A representation is **irreducible** (or simple) if its only invariant subspaces are {0} and V. This means there is no way to decompose the action into smaller independent pieces. For a one-dimensional representation, this is automatic. For higher dimensions, irreducibility is a strong condition: it says the group action thoroughly "mixes" the space, so that no proper subspace is left alone by all group elements simultaneously.

When a representation is reducible (has a proper invariant subspace W), the natural question is whether V decomposes as a direct sum V = W ⊕ U where U is also invariant. If so, the representation splits into two independent pieces. A representation is **completely reducible** (or semisimple) if it decomposes as a direct sum of irreducible subrepresentations. This is not automatic — the example of [[1,1],[0,1]] for ℤ/2ℤ over a field of characteristic 2 shows a reducible representation with no invariant complement.

The remarkable fact, which you will see formalized as Maschke's theorem, is that for finite groups over fields of characteristic zero (or more generally, characteristic not dividing |G|), complete reducibility is guaranteed. This means the study of all representations reduces to the study of irreducible ones plus the combinatorics of how they assemble via direct sums. Irreducible representations are thus the atoms from which the entire representation theory of a group is built — finding and classifying them is the central problem.
