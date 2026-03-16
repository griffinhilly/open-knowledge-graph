---
id: hahn-banach-theorem
title: Hahn-Banach Theorem
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: linear-functionals-dual-spaces
  type: hard
builds-toward:
- weak-convergence-banach
tags:
- functional-analysis
stage: abstract-reasoning
status: draft
---

# Hahn-Banach Theorem

## Core Idea
The Hahn-Banach theorem states that any bounded linear functional on a subspace of a normed space extends to a bounded functional on the whole space with the same norm. This is a cornerstone result ensuring the dual space is rich and enabling point separation.

## Explainer

From your study of linear functionals and dual spaces, you know that the dual X* of a normed space X is the collection of all bounded linear functionals φ: X → ℝ, equipped with the operator norm ||φ|| = sup{ |φ(x)| : ||x|| ≤ 1 }. A natural question arises: if you have only defined a functional on a *subspace* of X, can you extend it to the whole space without distorting it? The **Hahn-Banach theorem** answers yes: if Y is a subspace of a normed space X and φ: Y → ℝ is a bounded linear functional, then there exists a bounded linear functional Φ: X → ℝ such that Φ(y) = φ(y) for all y ∈ Y, and ||Φ|| = ||φ||. The extension is norm-preserving — it doesn't enlarge the functional.

Why is this non-trivial? In finite-dimensional spaces, you can always extend a linear functional by choosing values on a basis — the problem is algebraically straightforward. But in infinite-dimensional Banach spaces, a subspace can be dense in the whole space, and extensions must be compatible with limits in a topologically subtle way. The proof uses Zorn's lemma (a form of the axiom of choice) to handle the infinite-dimensional case: you extend one dimension at a time and invoke maximality to assert the process terminates at a full extension.

The theorem has two standard formulations. The **analytic form** (above) handles normed spaces. The **geometric form** says that a convex set and a point outside it can be separated by a hyperplane — a **separating hyperplane** whose existence is guaranteed by Hahn-Banach. Both versions express the same underlying richness of the dual space. In finite dimensions, this geometric fact is visually obvious (draw a tangent hyperplane to a convex set); Hahn-Banach lifts it to infinite dimensions.

The consequences are far-reaching. Most importantly, Hahn-Banach guarantees that the dual space separates points: for any two distinct x₁, x₂ ∈ X, there exists a functional φ ∈ X* with φ(x₁) ≠ φ(x₂). This means the dual contains enough functionals to distinguish every element. Without Hahn-Banach, the dual might be trivially small — containing only the zero functional — and the entire theory of weak convergence, reflexivity, and duality in Banach spaces would collapse. It is in this sense the theorem is called a cornerstone: not because it gives you a formula, but because it certifies the dual space is rich enough to do mathematics with.
