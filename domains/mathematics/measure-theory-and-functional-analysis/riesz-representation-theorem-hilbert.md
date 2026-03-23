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
stage: expert
status: validated
---

# Riesz Representation Theorem (Hilbert)

## Core Idea
Every bounded linear functional f on a Hilbert space H has the form f(x) = ⟨x, y⟩ for a unique y ∈ H. This natural isomorphism H ≅ H* is special to Hilbert spaces and fails in general Banach spaces.

## Questions

```yaml
- question: "The Riesz Representation Theorem guarantees that for every bounded linear functional f: H → ℝ on a Hilbert space H, there exists:"
  type: multiple-choice
  options:
    - "A sequence of vectors whose inner products with x converge to f(x) for every x"
    - "A unique y ∈ H such that f(x) = ⟨x, y⟩ for all x ∈ H"
    - "An orthonormal basis {eₙ} such that f is determined by the values f(eₙ)"
    - "A closed subspace K ⊂ H such that f(x) = ‖proj_K x‖"
  answer: 1
  explanation: "The theorem says every bounded linear functional is exactly inner product with a unique fixed vector y — no approximation, no basis dependence. Option C is true (knowing f on a basis determines f), but it is not what the Riesz theorem says; the theorem's content is that this determining data has the specific form of an inner product with a single vector. Option D confuses the representation with projection, which computes distance, not a linear functional."

- question: "The Banach space L^p (with 1 < p < ∞, p ≠ 2) has dual (L^p)* ≅ L^q where 1/p + 1/q = 1. Why does the Hilbert-space Riesz Representation Theorem not apply to L^p?"
  type: multiple-choice
  options:
    - "L^p is infinite-dimensional, and the theorem requires finite-dimensional spaces"
    - "L^p has no inner product, so the self-duality H ≅ H* fails — the dual L^q is a genuinely different space unless p = 2"
    - "Bounded linear functionals on L^p are not continuous, so the theorem's hypotheses fail"
    - "The theorem only applies to real Hilbert spaces, not function spaces"
  answer: 1
  explanation: "The self-duality H ≅ H* is a special consequence of the inner product, not just the norm. In L^p with p ≠ 2, there is no inner product, and the dual is the different space L^q (conjugate exponent). When p = 2, L^p = L² is a Hilbert space, q = 2 as well, and indeed L^2 ≅ (L^2)* — the theorem applies. The inner product structure is essential: it is what allows 'measurements' (functionals) to be identified with 'states' (vectors) in the same space."

- question: "The Riesz Representation Theorem shows that every Banach space is self-dual (isomorphic to its dual space), since bounded linear functionals on any normed space can be represented as inner products."
  type: true-false
  answer: false
  explanation: "This is the most important misconception to correct. Self-duality is SPECIFIC to Hilbert spaces — it depends on the existence of an inner product. General Banach spaces are not self-dual: the dual of L^p is L^q (conjugate exponent), which is a different space unless p = 2. The Riesz theorem characterizes a special feature of Hilbert geometry, not a universal property of Banach spaces. The inner product is the structure that collapses the distinction between a space and its dual."

- question: "The self-duality H ≅ H* of a Hilbert space depends on the inner product structure, not merely on the completeness or the norm."
  type: true-false
  answer: true
  explanation: "A Hilbert space is a Banach space (complete normed space) with the extra structure of an inner product. The Riesz theorem uses the inner product crucially: the proof constructs y via orthogonal decomposition relative to ker(f), which requires orthogonality — an inner product concept. Two Banach spaces can be isometric (same norm structure) while having different duals. The inner product is the additional ingredient that identifies vectors with functionals."

- question: "Explain geometrically why every bounded linear functional f on a Hilbert space has the form f(x) = ⟨x, y⟩ for some unique y. What role does orthogonality play in the proof?"
  type: short-answer
  answer: "A nonzero bounded functional f has a kernel ker(f) — the closed subspace of all vectors it maps to zero. The key geometric fact is that any closed subspace of a Hilbert space has an orthogonal complement. So H = ker(f) ⊕ ker(f)^⊥, and ker(f)^⊥ is one-dimensional (since f is scalar-valued). Pick a unit vector z in ker(f)^⊥. Any vector x decomposes as x = (x − f(x)/f(z)·z) + f(x)/f(z)·z — the first part is in ker(f), the second is a scalar multiple of z. Setting y = f(z)·z̄ (conjugated in the complex case), we get f(x) = ⟨x, y⟩. Uniqueness holds because if ⟨x, y⟩ = ⟨x, y'⟩ for all x, then y = y'. The whole proof hinges on orthogonal decomposition — which requires an inner product, not just a norm."
  explanation: "The geometric picture is: 'evaluating f at x' is the same as 'projecting x onto the direction y and scaling.' Orthogonality provides the decomposition that makes this possible. In a general Banach space, you have no such decomposition, which is why the identification of functionals with vectors fails."
```

## Explainer

From your study of **dual spaces and bounded functionals**, you know that H* — the dual of a Hilbert space H — is the space of all bounded linear maps f: H → ℝ (or ℂ). These are the "measurements" you can make: each f takes a vector and returns a number, linearly and continuously. The abstract question is: what do all possible bounded functionals look like? The Riesz Representation Theorem answers this completely — every bounded functional is just an inner product with a fixed vector.

The geometric intuition comes from your understanding of **orthogonality in Hilbert spaces**. A bounded linear functional f: H → ℝ has a kernel — the closed subspace of all x with f(x) = 0. If f is not identically zero, its kernel has a one-dimensional orthogonal complement. Any vector y in that complement, appropriately normalized, satisfies f(x) = ⟨x, y⟩ for all x. In other words, "measuring x with f" is equivalent to "projecting x onto the direction y." The inner product already computes the projection, so inner products and bounded functionals are the same thing.

More carefully: fix a nonzero bounded functional f. The kernel ker(f) is a closed subspace, so by your orthogonal decomposition results, H = ker(f) ⊕ ker(f)^⊥. The orthogonal complement is one-dimensional — pick any unit vector z in it. Every x ∈ H decomposes as x = (x − f(x)/f(z) · z) + f(x)/f(z) · z. The first part lies in ker(f), the second is a scalar multiple of z. Setting y = f(z)·z̄ (conjugated in the complex case), you get f(x) = ⟨x, y⟩. Uniqueness follows because if ⟨x, y⟩ = ⟨x, y'⟩ for all x, then y = y'.

The consequence is the isomorphism H ≅ H*: the map y ↦ ⟨·, y⟩ is a bijection from H onto H*. This is why Hilbert spaces are called **self-dual** — a Hilbert space "knows" its own dual. This fails in general Banach spaces: the dual of L^p is L^q (with 1/p + 1/q = 1), which is a different space unless p = 2. The inner product is the special structure that collapses this distinction. For applications — including quantum mechanics, where states live in L² and observables are bounded functionals — this self-duality is indispensable: every observable corresponds to a unique state vector, and vice versa.
