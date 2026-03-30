---
id: character-tables
title: Character Tables
domain: mathematics
course: representation-theory
prerequisites:
- id: orthogonality-relations
  type: hard
builds-toward:
- representations-of-symmetric-groups
tags:
- character-table
- conjugacy-class
- irreducible-character
stage: expert
status: validated
---

# Character Tables

## Core Idea
A character table is a square matrix whose rows correspond to irreducible representations and whose columns to conjugacy classes of a finite group G, with entries χᵢ(Cⱼ). The orthogonality relations constrain these entries so tightly that the table encodes the full representation theory of G. Computing the character table is often the first concrete goal when studying a group's representations.

## Questions

```yaml
- question: "The character table of a finite group G is always a square matrix. Why?"
  type: short-answer
  answer: "The number of rows equals the number of non-isomorphic irreducible representations, and the number of columns equals the number of conjugacy classes. These two numbers are always equal for finite groups over ℂ, making the table square."
  explanation: "This equality is a deep fact. The irreducible characters form an orthonormal basis for the space of class functions on G, and the dimension of this space equals the number of conjugacy classes (since a class function is determined by its values on conjugacy classes). So the number of irreducible characters must equal the number of conjugacy classes."

- question: "In the character table of S₃, the dimensions of the irreducible representations are 1, 1, and 2. What relation must these dimensions satisfy?"
  type: multiple-choice
  options:
    - "Their sum equals |S₃| = 6"
    - "Their product equals |S₃| = 6"
    - "The sum of their squares equals |S₃| = 6"
    - "The sum of their cubes equals |S₃| = 6"
  answer: 2
  explanation: "The sum-of-squares formula states that Σ dᵢ² = |G|, where dᵢ = χᵢ(e) is the dimension of the i-th irreducible representation. For S₃: 1² + 1² + 2² = 1 + 1 + 4 = 6 = |S₃|. This follows from decomposing the regular representation: it contains each irreducible Vᵢ with multiplicity dᵢ, so its dimension |G| = Σ dᵢ²."

- question: "Every entry in the character table of a finite group is an algebraic integer."
  type: true-false
  answer: true
  explanation: "Each χᵢ(g) is a sum of eigenvalues of ρᵢ(g). Since g has finite order n, ρᵢ(g)ⁿ = I, so each eigenvalue is an nth root of unity — and roots of unity are algebraic integers. A sum of algebraic integers is an algebraic integer. This arithmetic constraint, combined with the orthogonality relations, is a powerful tool for computing character tables: entries must be algebraic integers that satisfy specific inner product equations."

- question: "Can two non-isomorphic groups have identical character tables?"
  type: multiple-choice
  options:
    - "No — the character table determines the group up to isomorphism"
    - "Yes — for example, the dihedral group D₄ and the quaternion group Q₈ have the same character table"
    - "Yes — but only for abelian groups"
    - "No — because the orthogonality relations uniquely determine the table from the group"
  answer: 1
  explanation: "D₄ and Q₈ are non-isomorphic groups of order 8 (D₄ has elements of order 4 while Q₈ has a unique element of order 2), yet they have identical character tables — both have five conjugacy classes and irreducible representations of dimensions 1, 1, 1, 1, 2. This shows the character table does not determine the group: it captures the 'representation-theoretic' structure but loses some information about the group's element-level structure."
```

## Explainer

The **character table** of a finite group G organizes all irreducible character values into a single matrix. The rows are indexed by the non-isomorphic irreducible representations ρ₁, …, ρₖ, the columns by the conjugacy classes C₁, …, Cₖ (with C₁ = {e} by convention), and the entry in row i, column j is χᵢ(Cⱼ). Since the number of irreducible representations equals the number of conjugacy classes, this table is always square.

The orthogonality relations provide powerful constraints for computing the table. Row orthogonality says Σⱼ |Cⱼ|/|G| · χᵢ(Cⱼ) conjugate(χₘ(Cⱼ)) = δᵢₘ, and column orthogonality gives Σᵢ χᵢ(Cⱼ) conjugate(χᵢ(Cₗ)) = |G|/|Cⱼ| · δⱼₗ. Combined with the sum-of-squares formula Σ dᵢ² = |G| (where dᵢ = χᵢ(e) is the dimension) and the fact that entries are sums of roots of unity, these constraints often determine the table completely or reduce it to a small number of cases.

For S₃, the table has three rows and three columns. The conjugacy classes are {e}, {(12),(13),(23)}, {(123),(132)} with sizes 1, 3, 2. The trivial representation gives row (1, 1, 1). The sign representation gives row (1, −1, 1). The remaining irreducible has dimension 2 (since 1² + 1² + d² = 6 forces d = 2), and the orthogonality relations determine its character values: (2, 0, −1). The complete table is a 3×3 matrix that encodes everything about how S₃ acts on vector spaces.

A subtle point: the character table does not uniquely determine the group. The dihedral group D₄ and the quaternion group Q₈ are non-isomorphic groups of order 8 with identical character tables. The table captures the representation-theoretic structure faithfully but loses information about the multiplication table of the group. Nevertheless, the character table determines many group-theoretic properties: the order of the group, the sizes of conjugacy classes, whether the group is abelian (all irreducibles are one-dimensional), whether it is simple (no row is a sum of the trivial character and another), and more.
