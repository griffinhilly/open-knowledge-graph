---
id: hilbert-spaces-definition
title: 'Hilbert Spaces: Definition and Examples'
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: banach-spaces-definition
  type: hard
- id: inner-products
  type: hard
builds-toward:
- orthogonality-and-projections
tags:
- hilbert-spaces
- functional-analysis
stage: expert
status: draft
---

# Hilbert Spaces: Definition and Examples

## Core Idea
A Hilbert space is a complete normed vector space whose norm comes from an inner product: ‖x‖ = √⟨x,x⟩. Examples include L², ℓ², and ℝⁿ. The inner product structure enables orthogonality and powerful representation theorems.

## Questions

```yaml
- question: "A Hilbert space has all the properties of a Banach space. What additional structure does it have that a general Banach space does NOT necessarily possess?"
  type: multiple-choice
  options:
    - "Completeness — every Cauchy sequence converges within the space"
    - "A norm satisfying the triangle inequality"
    - "An inner product that generates the norm, enabling orthogonality between elements"
    - "Infinite dimensionality — Banach spaces are finite-dimensional while Hilbert spaces can be infinite-dimensional"
  answer: 2
  explanation: "Completeness (A) is already a defining property of Banach spaces. A norm with the triangle inequality (B) is required by any normed space. Both Banach and Hilbert spaces can be infinite-dimensional (D is false). The distinguishing feature is the inner product: a Banach space has distances (norms) but not necessarily angles. A Hilbert space adds an inner product ⟨·,·⟩ that induces the norm via ‖x‖ = √⟨x,x⟩, which means you can ask whether two elements are orthogonal — a geometric capability that general Banach spaces lack."

- question: "The space C[0,1] of continuous functions on [0,1] with norm ‖f‖ = max|f(x)| is a Banach space. Why is it NOT a Hilbert space?"
  type: multiple-choice
  options:
    - "It lacks completeness — sequences of continuous functions don't always converge in this norm"
    - "Its norm fails the triangle inequality in some edge cases"
    - "There is no inner product that generates this norm — a norm comes from an inner product only if it satisfies the parallelogram law, and this norm does not"
    - "It is only finite-dimensional, and Hilbert spaces must be infinite-dimensional"
  answer: 2
  explanation: "C[0,1] with the supremum norm is indeed complete (A is wrong). The triangle inequality holds (B is wrong). Hilbert spaces can be finite-dimensional (D is wrong). The key criterion: a norm ‖·‖ comes from an inner product if and only if it satisfies the parallelogram law: ‖x+y‖² + ‖x−y‖² = 2(‖x‖² + ‖y‖²). The supremum norm on C[0,1] fails this identity, which means no inner product can generate it. Not every Banach space norm can be 'polarized' to yield an inner product."

- question: "Every Hilbert space is a Banach space, but not every Banach space is a Hilbert space."
  type: true-false
  answer: true
  explanation: "A Hilbert space satisfies all Banach space requirements: it is a complete normed vector space. But it additionally requires a norm derived from an inner product, which is a strictly stronger condition. The inclusion is one-way. Examples like ℝⁿ, ℓ², and L²[a,b] are both; the space ℓ¹ (summable sequences) is Banach but not Hilbert because its norm cannot be derived from any inner product."

- question: "In a Hilbert space, the inner product is derived from the norm — any norm on a vector space can be used to define an inner product via the polarization identity."
  type: true-false
  answer: false
  explanation: "This reverses the relationship. In a Hilbert space, the norm is derived from the inner product (‖x‖ = √⟨x,x⟩), not the other way around. Moreover, not every norm can be polarized to yield an inner product. The polarization identity ⟨x,y⟩ = (‖x+y‖² − ‖x−y‖²)/4 only produces a valid inner product when the norm satisfies the parallelogram law. Many natural norms (like L¹ or L∞ norms) fail this condition, so those Banach spaces cannot be made into Hilbert spaces by any inner product."

- question: "What geometric capability does an inner product add to a normed vector space, and why does this matter for analysis in infinite-dimensional spaces like L²?"
  type: short-answer
  answer: "An inner product adds the ability to measure angles between vectors — specifically, to define orthogonality (⟨x,y⟩ = 0 means x and y are perpendicular). A norm tells you how large something is; an inner product tells you how aligned two elements are. In infinite-dimensional spaces like L², this enables Fourier analysis: functions can be decomposed as sums of orthogonal components (like sine and cosine), exactly as vectors decompose along orthogonal axes. Orthogonal projections, the Riesz representation theorem, and the existence of orthonormal bases all depend on having an inner product — none of these tools are available in a general Banach space."
  explanation: "The key is 'angles vs. distances.' Banach spaces give you a metric geometry; Hilbert spaces give you Euclidean-like geometry in infinite dimensions. This matters because orthogonal decomposition — breaking a function or signal into independent components — is the core operation in Fourier analysis, quantum mechanics, and spectral theory. Completeness then guarantees that infinite orthogonal series converge within the space, making the theory analytically complete."
```

## Explainer

You already know what a **Banach space** is: a vector space equipped with a norm, where every Cauchy sequence converges — completeness prevents gaps in the space. And you know what an **inner product** is: a function ⟨·,·⟩ that takes two vectors and returns a scalar, satisfying linearity, symmetry, and positive-definiteness. A Hilbert space is the marriage of these two structures: a Banach space whose norm is derived from an inner product via ‖x‖ = √⟨x,x⟩. Not every Banach space has this property — the inner product requirement is an additional constraint that adds rich geometric structure.

The geometric gain is orthogonality. In ℝ² with the standard dot product, you can ask whether two vectors are perpendicular. In a Hilbert space, you can ask the same question about any two elements, even if they are functions rather than finite-dimensional vectors. This is what distinguishes Hilbert spaces from general Banach spaces: the inner product gives you angles, not just distances. The norm tells you how large something is; the inner product tells you how aligned two things are.

The canonical examples cover three regimes of dimension. **ℝⁿ** with the dot product ⟨x,y⟩ = Σxᵢyᵢ is the finite-dimensional case — every student of linear algebra has worked in a Hilbert space. **ℓ²** is the space of infinite sequences (x₁, x₂, x₃, ...) with Σxᵢ² < ∞, with inner product ⟨x,y⟩ = Σxᵢyᵢ; completeness is non-trivial here and must be verified. **L²[a,b]** is the space of square-integrable functions on an interval, with ⟨f,g⟩ = ∫f(x)g(x)dx; this is where Fourier analysis lives, turning a function into a "sum of orthogonal components" just as a vector decomposes along orthogonal axes.

The completeness condition is what makes Hilbert spaces analytically tractable. It guarantees that orthogonal series (like Fourier series) converge within the space, and it underpins the powerful theorems to come — the projection theorem, the Riesz representation theorem, and the existence of orthonormal bases in infinite dimensions. A space without completeness might have orthogonal sequences whose sums drift toward elements that are not in the space, breaking the theory. Hilbert spaces avoid this failure, which is why they are the natural setting for quantum mechanics, signal processing, and much of modern analysis.
