---
id: reflexive-spaces
title: Reflexive Spaces
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: weak-convergence
  type: hard
tags:
- duality
stage: advanced
status: draft
---

# Reflexive Spaces

## Core Idea
A Banach space X is reflexive if the natural embedding X → X** is surjective. Reflexive spaces have the Bolzano-Weierstrass property: every bounded sequence has a weakly convergent subsequence.

## Explainer

From your study of weak convergence, you know that a sequence (xₙ) in a Banach space X converges weakly to x if f(xₙ) → f(x) for every bounded linear functional f ∈ X*. The **dual space** X* consists of all bounded linear functionals on X. Now consider the dual of the dual: X** = (X*)* consists of all bounded linear functionals on X*. There is a natural map J: X → X** defined by J(x)(f) = f(x) — it sends each element x ∈ X to the functional on X* that evaluates at x. This map J is always an isometric embedding (it preserves norms and is injective), so X sits inside X** in a canonical way. A Banach space X is called **reflexive** when J is also surjective — meaning X and X** are not merely isomorphic in some abstract sense, but isomorphic via this specific natural map.

The significance of reflexivity is best understood through what it buys you: the **Banach-Alaoglu-style compactness**. In a finite-dimensional space, every bounded sequence has a convergent subsequence (Bolzano-Weierstrass). In infinite dimensions, strong convergence of bounded sequences fails — the sequence of standard basis vectors in ℓ² is bounded but has no strongly convergent subsequence. But in a reflexive space, every bounded sequence has a **weakly convergent** subsequence. This is the correct infinite-dimensional analogue of Bolzano-Weierstrass, and it is the workhorse of existence proofs throughout functional analysis and PDE theory.

The canonical examples clarify the concept. The spaces Lᵖ(μ) for 1 < p < ∞ are reflexive, with dual Lᵍ where 1/p + 1/q = 1. The spaces L¹ and L∞ are not reflexive: (L¹)* = L∞ but (L∞)* is strictly larger than L¹. Hilbert spaces are reflexive (by the Riesz representation theorem, H* ≅ H, so H** ≅ H). Every finite-dimensional Banach space is reflexive trivially.

Reflexivity matters in optimization: to prove a functional attains its minimum on a closed convex set, you extract a minimizing sequence, use reflexivity to find a weakly convergent subsequence, and appeal to the weak lower semicontinuity of the functional. Without reflexivity, that subsequence might not exist. The condition is also tied to geometry — a Banach space is reflexive if and only if its closed unit ball is compact in the weak topology, making the connection between the algebraic structure (the double-dual map) and the topological structure (weak compactness) precise.
