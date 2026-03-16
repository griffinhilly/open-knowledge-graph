---
id: splitting-fields
title: Splitting Fields
domain: mathematics
course: abstract-algebra
prerequisites:
- id: algebraic-transcendental-elements
  type: hard
builds-toward:
- galois-groups
- finite-fields
tags:
- splitting-field
- root
- complete-factorization
stage: advanced
status: draft
---

# Splitting Fields

## Core Idea
A splitting field of a polynomial f(x) ∈ F[x] is the smallest field extension of F in which f splits into linear factors. Splitting fields exist and are unique up to isomorphism.

## Explainer

You've already worked with algebraic and transcendental elements, so you know that adjoining a root α of an irreducible polynomial p(x) to a field F produces the extension F(α). A **splitting field** is the result of doing this repeatedly — adjoining every root until the polynomial completely factors into linear pieces.

Start with a concrete case. Over ℚ, the polynomial f(x) = x² − 2 doesn't split: it has no rational roots. But ℚ(√2) = {a + b√2 : a, b ∈ ℚ} is the smallest extension where f factors as (x − √2)(x + √2). Notice that adjoining one root automatically provided the other, because −√2 = −(√2) is already in ℚ(√2). That's the splitting field: ℚ(√2). For x² + 1 over ℝ, the splitting field is ℂ = ℝ(i), since x² + 1 = (x − i)(x + i) and both roots land in ℂ.

For a degree-n polynomial, you might need to adjoin up to n roots. Each adjunction creates a tower of extensions: F ⊆ F(α₁) ⊆ F(α₁, α₂) ⊆ · · · ⊆ F(α₁, …, αₙ). The degree of the splitting field over F divides n! — the factorial bound arises because the first root creates an extension of degree at most n, the second of degree at most n−1, and so on. In practice the degree is often much smaller if roots are algebraically related, as in the x² − 2 example above.

The **uniqueness up to isomorphism** is what makes splitting fields a well-defined concept rather than an artifact of construction order. Two different towers of root adjunctions may look different, but they produce fields that are structurally identical — any two splitting fields of f over F are isomorphic by a map fixing F. This uniqueness is the foundation for defining Galois groups: once you know the splitting field is a canonical object, you can meaningfully ask how many automorphisms it has, and that count gives you the Galois group.
