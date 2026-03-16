---
id: banach-spaces
title: Banach Spaces
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: normed-vector-spaces
  type: hard
- id: completeness-metric-spaces
  type: hard
builds-toward:
- bounded-linear-operators
tags:
- functional-analysis
stage: advanced
status: draft
---

# Banach Spaces

## Core Idea
A Banach space is a complete normed vector space where every Cauchy sequence converges. Lᵖ spaces, C[a,b], and sequence spaces ℓᵖ are canonical examples, providing natural settings for analysis and optimization.

## Explainer

You already know two ingredients: a **normed vector space** (a vector space equipped with a notion of length ‖v‖ satisfying the triangle inequality), and **completeness** from metric spaces (the property that every Cauchy sequence converges). A **Banach space** is simply a normed vector space that is complete under the metric induced by the norm, d(u, v) = ‖u − v‖. The name honors Stefan Banach, who systematized functional analysis in the 1930s.

Why does completeness matter for a normed space? The norm lets you measure whether a sequence of vectors is "trying to converge" — a **Cauchy sequence** is one where ‖xₙ − xₘ‖ → 0 as n, m → ∞. Completeness guarantees that sequences that *should* converge actually *do* converge, and that their limit stays in the space. Without it, you can construct sequences of well-behaved functions that converge to something pathological or outside the space, which breaks the analytic machinery you want to build. The rational numbers ℚ are the classic non-complete example: sequences of rationals can converge to irrationals. Banach spaces are the functional-analytic equivalent of the real numbers — closed under limits.

The canonical Banach spaces give the concept concrete shape. The space **C[a,b]** of continuous functions on a closed interval, with the supremum norm ‖f‖ = sup|f(x)|, is complete: a uniformly convergent sequence of continuous functions converges to a continuous function. The sequence spaces **ℓᵖ** (p-summable sequences) are Banach spaces, with ℓ∞ (bounded sequences) at one extreme and ℓ¹ (absolutely summable) at another. The function spaces **Lᵖ** are Banach spaces for 1 ≤ p ≤ ∞, a fact whose proof is the Riesz-Fischer theorem.

Banach spaces are the natural setting for most of infinite-dimensional linear analysis. Fixed-point theorems (Banach's own contraction mapping theorem), spectral theory, and optimization theory all require completeness as a baseline assumption. The structural theorems of functional analysis — the open mapping theorem, the closed graph theorem, the Hahn-Banach theorem — all take Banach spaces as their domain. When you move to Hilbert spaces later, you are adding an inner product to this Banach structure; but Banach spaces capture what you can do with the norm alone.
