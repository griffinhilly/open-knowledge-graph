---
id: sobolev-spaces-introduction
title: Introduction to Sobolev Spaces
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lp-spaces
  type: hard
- id: partial-derivatives
  type: hard
tags:
- sobolev-spaces
- pde
stage: advanced
status: draft
---

# Introduction to Sobolev Spaces

## Core Idea
Sobolev space W^{k,p} consists of Lᵖ functions whose weak derivatives up to order k are in Lᵖ. These spaces are essential for PDE theory, allowing rigorous treatment of differential equations with non-classical solutions.

## Explainer

From Lᵖ spaces you know how to measure the "size" of a function using integrated powers of its absolute value. From partial derivatives you know classical differentiation. **Sobolev spaces** combine these two ideas to create function spaces that track both the behavior of a function *and* the behavior of its derivatives — all within the Lᵖ framework.

The central challenge Sobolev spaces address is this: many important differential equations (like Poisson's equation −Δu = f) have solutions that are not twice continuously differentiable in the classical sense, yet they are still "morally" solutions. The fix is **weak derivatives**. A function g is the weak derivative of f if, for every smooth test function φ that vanishes on the boundary, ∫ f φ' dx = −∫ g φ dx. This equation is just integration by parts rearranged — if f were smooth, its classical derivative would satisfy this. The weak derivative g need only be in Lᵖ; it does not need to exist in the pointwise classical sense. A function like |x| has a weak derivative (the sign function), even though it lacks a classical derivative at zero.

The **Sobolev space W^{k,p}** consists of all Lᵖ functions whose weak derivatives up to order k are also in Lᵖ. The norm combines the Lᵖ norms of f and all its weak derivatives up to order k: ‖f‖_{W^{k,p}} = (Σ_{|α|≤k} ‖D^α f‖_pᵖ)^{1/p}. The most important case is **H^k = W^{k,2}**, which is a Hilbert space and the natural setting for variational problems and spectral theory for differential operators.

Sobolev spaces matter because PDEs are most naturally formulated as: find u ∈ W^{1,2} such that a bilinear form equals a linear functional. This **weak formulation** is far more tractable than demanding classical solutions. The Lax-Milgram theorem then guarantees existence and uniqueness of weak solutions, and Sobolev embedding theorems tell you under what conditions a weak solution is actually a classical one. This machinery — weak formulation, existence via functional analysis, regularity via embeddings — is the backbone of modern PDE theory.
