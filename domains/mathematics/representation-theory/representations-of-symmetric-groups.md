---
id: representations-of-symmetric-groups
title: Representations of Symmetric Groups
domain: mathematics
course: representation-theory
prerequisites:
- id: character-tables
  type: hard
- id: symmetric-group
  type: hard
- id: frobenius-reciprocity
  type: soft
builds-toward:
- young-diagrams-and-tableaux
tags:
- symmetric-group
- partition
- specht-module
stage: expert
status: validated
---

# Representations of Symmetric Groups

## Core Idea
The irreducible representations of the symmetric group Sₙ over ℂ are indexed by partitions of n. Each partition λ ⊢ n gives an irreducible representation Sλ (the Specht module) whose dimension equals the number of standard Young tableaux of shape λ. This parametrization connects representation theory to combinatorics: the deep structure of Sₙ-representations is encoded in the combinatorics of partitions, tableaux, and symmetric functions.

## Questions

```yaml
- question: "The number of non-isomorphic irreducible representations of S₅ is:"
  type: multiple-choice
  options:
    - "5"
    - "7"
    - "10"
    - "120"
  answer: 1
  explanation: "The number of irreducible representations equals the number of conjugacy classes, which for Sₙ equals the number of partitions of n. The partitions of 5 are: (5), (4,1), (3,2), (3,1,1), (2,2,1), (2,1,1,1), (1,1,1,1,1) — exactly 7 partitions. So S₅ has 7 irreducible representations."

- question: "Which partition of n corresponds to the trivial representation of Sₙ?"
  type: multiple-choice
  options:
    - "(1, 1, ..., 1) — the partition into all 1s"
    - "(n) — the single-row partition"
    - "(n−1, 1)"
    - "The answer depends on n"
  answer: 1
  explanation: "The partition (n) — a single row of n boxes — corresponds to the trivial representation, where every permutation acts as the identity. The partition (1,1,...,1) — a single column of n boxes — corresponds to the sign representation, where each permutation acts as multiplication by its sign. The partition (n−1,1) gives the (n−1)-dimensional standard representation."

- question: "Conjugacy classes of Sₙ are determined by cycle type, and partitions of n parametrize both conjugacy classes and irreducible representations. Is this bijection between the two sets 'natural' in any canonical sense?"
  type: short-answer
  answer: "No. While both sets are indexed by partitions of n (giving the same count), the correspondence is not canonical — there is no single 'natural' bijection that works uniformly for all n. The labeling of irreducible representations by partitions uses the construction of Specht modules, which involves specific combinatorial choices."
  explanation: "This is a subtle point. The equality |{conjugacy classes}| = |{irreducibles}| holds for any finite group (not just symmetric groups), but for Sₙ both sets happen to be naturally parametrized by partitions of n, creating a tempting but misleading identification. The conjugacy class of cycle type λ and the irreducible representation labeled by λ are related, but the relationship is indirect — it goes through the character table rather than a canonical bijection."

- question: "The dimension of the irreducible representation of Sₙ corresponding to partition λ equals the number of standard Young tableaux of shape λ."
  type: true-false
  answer: true
  explanation: "A standard Young tableau of shape λ is a filling of the Young diagram of λ with the numbers 1, ..., n such that entries increase along each row and down each column. The hook length formula gives an explicit count: dim(Sλ) = n! / ∏ h(□), where the product runs over all boxes and h(□) is the hook length. For S₃ and λ = (2,1), the two standard tableaux are [[1,2],[3]] and [[1,3],[2]], confirming dim = 2."
```

## Explainer

The symmetric group Sₙ — the group of all permutations of {1, …, n} — is one of the most important groups in mathematics, and its representation theory is correspondingly rich. The key structural fact is that conjugacy classes in Sₙ are determined by **cycle type**: two permutations are conjugate if and only if they have the same partition into disjoint cycles. Since cycle types are exactly partitions of n, the number of conjugacy classes (and hence irreducible representations) equals p(n), the number of partitions.

The irreducible representations are the **Specht modules** Sλ, one for each partition λ ⊢ n. The construction uses **Young tableaux**: fill the Young diagram of λ with the numbers 1, …, n to get a Young tableau, then use symmetrization and antisymmetrization operations on the rows and columns to build an irreducible subspace of the regular representation. The dimension of Sλ equals the number of **standard** Young tableaux of shape λ (fillings where entries increase along rows and down columns), computed by the elegant **hook length formula**: dim(Sλ) = n! / ∏ h(□).

For S₃, the partitions of 3 are (3), (2,1), (1,1,1). The partition (3) gives the trivial representation (dimension 1). The partition (1,1,1) gives the sign representation (dimension 1). The partition (2,1) gives a 2-dimensional representation — the standard representation, where S₃ acts on the plane {(x₁,x₂,x₃) : x₁+x₂+x₃ = 0} by permuting coordinates. The dimensions check: 1² + 2² + 1² = 6 = 3!.

The representation theory of Sₙ connects to a vast web of mathematics. The characters of Sₙ are given by symmetric functions (Schur functions), linking to algebraic combinatorics. The branching rules (how Sₙ-representations restrict to Sₙ₋₁) are governed by removing boxes from Young diagrams, connecting to the theory of symmetric functions and the RSK correspondence. Through Schur-Weyl duality, the representations of Sₙ are intimately related to the representations of GL_n — the combinatorics of partitions serves both.
