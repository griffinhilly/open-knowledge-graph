---
id: inner-product-spaces
title: Inner Product Spaces
domain: mathematics
course: linear-algebra
prerequisites:
- id: dot-product
  type: hard
- id: vector-spaces
  type: hard
builds-toward:
- orthogonal-vectors-orthonormal-bases
tags:
- inner product
- spaces
- orthogonality
stage: formal-systems
status: validated
---

# Inner Product Spaces

## Core Idea
An inner product on a vector space V is a function ⟨·,·⟩: V × V → ℝ satisfying positivity (⟨v,v⟩ ≥ 0), symmetry, and linearity in the second argument. The dot product is the standard inner product on R^n. Inner products induce norms and enable defining orthogonality and projections.

## Questions

```yaml
- question: "Which inner product axiom guarantees that ⟨v, v⟩ = 0 implies v = 0?"
  type: multiple-choice
  options: ["Symmetry", "Bilinearity", "Positive definiteness", "The Cauchy-Schwarz inequality"]
  answer: 2
  explanation: "Positive definiteness states that ⟨v, v⟩ ≥ 0 for all v, with equality if and only if v = 0. This is what makes the induced norm ‖v‖ = √⟨v,v⟩ a true norm — it ensures only the zero vector has zero length. Without positive definiteness, the 'norm' could vanish for nonzero vectors, breaking the geometric interpretation."

- question: "Every inner product on a vector space is just the standard dot product."
  type: true-false
  answer: false
  explanation: "The dot product is the standard inner product on ℝⁿ, but many other valid inner products exist on the same or different spaces. For example, on the space of continuous functions on [a, b], the integral ⟨f, g⟩ = ∫_a^b f(x)g(x) dx defines an inner product. Different inner products on the same space define different notions of length and orthogonality, and the 'right' inner product depends on the application."

- question: "How does an inner product define orthogonality in an abstract vector space where there is no visual geometry?"
  type: short-answer
  answer: "Two vectors u and v are defined to be orthogonal if ⟨u, v⟩ = 0. The inner product axioms are chosen precisely so that this algebraic condition generalizes the geometric notion of perpendicularity from ℝ² and ℝ³ to any vector space."
  explanation: "In ℝ², perpendicular vectors have dot product zero — this is a theorem provable from geometry. In an abstract vector space with an inner product, orthogonality is defined by the same algebraic condition. This allows concepts like orthogonal projections, Gram-Schmidt orthogonalization, and Fourier series to work in function spaces and other abstract settings."
```

## Explainer

You already know the dot product on ℝⁿ: multiply corresponding components and add. What you may not have considered is that the dot product is just one example of a broader structure. An inner product is an abstract operation ⟨·, ·⟩ on a vector space that captures the essential features of the dot product through three axioms: it must be symmetric (⟨u, v⟩ = ⟨v, u⟩), linear in each argument, and positive definite (⟨v, v⟩ ≥ 0, with equality only when v = 0). Any operation satisfying these axioms is an inner product, and the resulting structure is called an inner product space.

The payoff of abstracting the dot product is that geometric concepts — length, angle, and orthogonality — transfer to spaces that have no visual geometry. Given an inner product, you can define the norm (length) of a vector as ‖v‖ = √⟨v, v⟩, and the angle between two vectors via cos θ = ⟨u, v⟩/(‖u‖ ‖v‖). Two vectors are orthogonal when ⟨u, v⟩ = 0. These definitions reproduce familiar geometry in ℝⁿ and generalize it to function spaces, polynomial spaces, and any other vector space where an appropriate inner product exists.

A concrete non-dot-product example: on the space of continuous functions on [0, 1], define ⟨f, g⟩ = ∫₀¹ f(x)g(x) dx. This satisfies all three axioms. Two functions are orthogonal in this space when their product integrates to zero over [0, 1]. The sine and cosine functions that appear in Fourier series are orthogonal in exactly this sense — Fourier series is essentially decomposing a function into orthogonal components, which is the same idea as decomposing a vector in ℝⁿ into its projections onto orthogonal basis vectors.

Positive definiteness is the most subtle axiom and the one most worth understanding deeply. It ensures that ⟨v, v⟩ = 0 forces v = 0 — no nonzero vector has zero "length". Without this, the induced norm would not be a genuine norm, and the analogy with geometric length would collapse. The other axioms (symmetry and linearity) ensure the inner product behaves algebraically like multiplication; positive definiteness ensures the geometric interpretation holds.
