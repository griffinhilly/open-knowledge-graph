---
id: riesz-representation-theorem-hilbert
title: Riesz Representation Theorem (Hilbert)
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: orthogonality-hilbert-spaces
  type: hard
- id: dual-spaces-bounded-functionals
  type: hard
builds-toward:
- bessel-parseval
tags:
- hilbert-spaces
- duality
stage: advanced
status: draft
---

# Riesz Representation Theorem (Hilbert)

## Core Idea
Every bounded linear functional f on a Hilbert space H has the form f(x) = ⟨x, y⟩ for a unique y ∈ H. This natural isomorphism H ≅ H* is special to Hilbert spaces and fails in general Banach spaces.

## Explainer

From your study of **dual spaces and bounded functionals**, you know that H* — the dual of a Hilbert space H — is the space of all bounded linear maps f: H → ℝ (or ℂ). These are the "measurements" you can make: each f takes a vector and returns a number, linearly and continuously. The abstract question is: what do all possible bounded functionals look like? The Riesz Representation Theorem answers this completely — every bounded functional is just an inner product with a fixed vector.

The geometric intuition comes from your understanding of **orthogonality in Hilbert spaces**. A bounded linear functional f: H → ℝ has a kernel — the closed subspace of all x with f(x) = 0. If f is not identically zero, its kernel has a one-dimensional orthogonal complement. Any vector y in that complement, appropriately normalized, satisfies f(x) = ⟨x, y⟩ for all x. In other words, "measuring x with f" is equivalent to "projecting x onto the direction y." The inner product already computes the projection, so inner products and bounded functionals are the same thing.

More carefully: fix a nonzero bounded functional f. The kernel ker(f) is a closed subspace, so by your orthogonal decomposition results, H = ker(f) ⊕ ker(f)^⊥. The orthogonal complement is one-dimensional — pick any unit vector z in it. Every x ∈ H decomposes as x = (x − f(x)/f(z) · z) + f(x)/f(z) · z. The first part lies in ker(f), the second is a scalar multiple of z. Setting y = f(z)·z̄ (conjugated in the complex case), you get f(x) = ⟨x, y⟩. Uniqueness follows because if ⟨x, y⟩ = ⟨x, y'⟩ for all x, then y = y'.

The consequence is the isomorphism H ≅ H*: the map y ↦ ⟨·, y⟩ is a bijection from H onto H*. This is why Hilbert spaces are called **self-dual** — a Hilbert space "knows" its own dual. This fails in general Banach spaces: the dual of L^p is L^q (with 1/p + 1/q = 1), which is a different space unless p = 2. The inner product is the special structure that collapses this distinction. For applications — including quantum mechanics, where states live in L² and observables are bounded functionals — this self-duality is indispensable: every observable corresponds to a unique state vector, and vice versa.
