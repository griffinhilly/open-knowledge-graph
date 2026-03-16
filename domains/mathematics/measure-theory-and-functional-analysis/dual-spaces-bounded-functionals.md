---
id: dual-spaces-bounded-functionals
title: Dual Spaces and Bounded Linear Functionals
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: operator-norm
  type: hard
builds-toward:
- hahn-banach-theorem
tags:
- duality
stage: advanced
status: draft
---

# Dual Spaces and Bounded Linear Functionals

## Core Idea
The dual space X* = B(X, ℝ) consists of all bounded linear functionals on X. As a Banach space under the operator norm, X* encodes geometric and topological information about X through the Hahn-Banach and Riesz representation theorems.

## Explainer

You already know the operator norm: for a bounded linear map T: X → Y between normed spaces, ‖T‖ = sup{‖Tx‖ : ‖x‖ ≤ 1}. A **bounded linear functional** is simply a bounded linear map whose codomain is the scalar field ℝ (or ℂ). Instead of sending vectors to vectors, it sends vectors to numbers. The canonical examples are everywhere: integration f ↦ ∫ f dμ is linear and bounded under integrability conditions; evaluation at a fixed point f ↦ f(x₀) is a functional on spaces of continuous functions; the inner product with a fixed vector, y ↦ ⟨y, x⟩, is a functional on any inner product space.

The **dual space** X* is the collection of all bounded linear functionals on X, equipped with the operator norm ‖φ‖ = sup{|φ(x)| : ‖x‖ ≤ 1}. This is not just a set — it is itself a Banach space. Even if X is not complete, X* automatically is, because the scalar field is complete and bounded linear maps into a complete space inherit completeness under the operator norm. This automatic completeness is one of the principal reasons the dual space is useful: you can always take limits of functionals freely.

The deep content is that X* encodes the geometry of X from the outside. A bounded functional φ ∈ X* is a "measuring device" for X — it carves X into level hyperplanes {x : φ(x) = c}, and the Hahn-Banach theorem (your next topic) guarantees that X* is rich enough to separate any two distinct points. If φ(x) = φ(y) for every φ ∈ X*, then x = y. This means the dual collectively "sees" everything in X; no information is hidden from it.

For concrete Banach spaces, duals can be explicitly identified with familiar spaces. The dual of Lᵖ(μ) is Lᵍ(μ) where 1/p + 1/q = 1 — the Hölder conjugate pair. Every bounded functional on Lᵖ has the form f ↦ ∫ fg dμ for a unique g ∈ Lᵍ. This is a striking identification: the abstract collection of measuring devices on Lᵖ is another Lᵍ space. The duality between Lᵖ and Lᵍ is precisely the same Hölder conjugate relationship underlying the Hölder and Minkowski inequalities, now reappearing as a structural theorem about the functional-analytic architecture of these spaces.
