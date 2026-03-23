---
id: orthogonal-vectors-orthonormal-bases
title: Orthogonal Vectors and Orthonormal Bases
domain: mathematics
course: linear-algebra
prerequisites:
- id: inner-product-spaces
  type: hard
- id: basis-definition
  type: hard
builds-toward:
- gram-schmidt-process
tags:
- orthogonal
- orthonormal
- bases
stage: formal-systems
status: validated
---

# Orthogonal Vectors and Orthonormal Bases

## Core Idea
Vectors u and v are orthogonal if ⟨u, v⟩ = 0. An orthonormal set has pairwise orthogonal unit vectors. An orthonormal basis enables simple coordinates: v = Σ⟨v, e_i⟩e_i. Orthonormal bases are numerically stable and reveal structure clearly.

## Questions

```yaml
- question: "You want to find the coordinates of vector v in an orthonormal basis {e₁, e₂, e₃}. What is the correct procedure?"
  type: multiple-choice
  options:
    - "Solve the linear system v = a₁e₁ + a₂e₂ + a₃e₃ for a₁, a₂, a₃ using row reduction"
    - "Compute ⟨v, e₁⟩, ⟨v, e₂⟩, ⟨v, e₃⟩ — these inner products directly give the coordinates"
    - "Normalize v and then project onto the subspace spanned by each pair of basis vectors"
    - "Apply the Gram-Schmidt process to {v, e₁, e₂, e₃} to extract the coordinates"
  answer: 1
  explanation: "With an orthonormal basis, each coordinate is simply ⟨v, eᵢ⟩ — a single inner product computed independently of the others. No system of equations is needed because orthogonality ensures the basis vectors do not 'interfere' with each other. With a non-orthonormal basis (option A), you would need row reduction because the basis vectors are entangled. The orthonormal case eliminates that entanglement entirely."

- question: "A set of vectors {u₁, u₂} satisfies ⟨u₁, u₂⟩ = 0 and both vectors are nonzero. Is {u₁, u₂} an orthonormal set?"
  type: multiple-choice
  options:
    - "Yes — the zero inner product is the only requirement for orthonormality"
    - "Not necessarily — the vectors are orthogonal but may not have unit length"
    - "Yes, provided they are also linearly independent"
    - "Not necessarily — orthonormal also requires the vectors to span R²"
  answer: 1
  explanation: "Orthonormal requires both conditions: pairwise orthogonality (⟨eᵢ, eⱼ⟩ = 0 for i ≠ j) AND unit length (⟨eᵢ, eᵢ⟩ = 1). The vectors in the question satisfy orthogonality but may have any length. For example, (2, 0) and (0, 3) are orthogonal but not orthonormal. To make them orthonormal, each would need to be divided by its norm."

- question: "In an orthonormal basis, each coordinate of a vector can be computed independently using a single inner product, without solving a system of equations."
  type: true-false
  answer: true
  explanation: "This is the central computational advantage of orthonormal bases. The formula v = Σ⟨v, eᵢ⟩eᵢ means each component ⟨v, eᵢ⟩ is computable from one dot product. Orthogonality ensures the components do not interact — knowing the 'e₁ component' of v tells you nothing about the 'e₂ component.' With a general basis this independence fails, requiring a linear system to untangle the components."

- question: "Any set of mutually orthogonal nonzero vectors is automatically an orthonormal set."
  type: true-false
  answer: false
  explanation: "Orthonormal requires unit length in addition to orthogonality. Mutually orthogonal vectors satisfy ⟨uᵢ, uⱼ⟩ = 0 for i ≠ j, but they may have any length. For example, {(2,0,0), (0,3,0), (0,0,5)} is orthogonal but not orthonormal. To obtain an orthonormal set, each vector must be normalized: eᵢ = uᵢ / ‖uᵢ‖."

- question: "What computational advantage does an orthonormal basis provide over a general basis when finding the coordinates of a vector, and why does orthogonality produce this advantage?"
  type: short-answer
  answer: "With an orthonormal basis, the coordinate corresponding to each basis vector eᵢ is simply the inner product ⟨v, eᵢ⟩ — computable directly, independently of all other coordinates. With a general basis, finding coordinates requires solving a linear system because the basis vectors are not perpendicular and their contributions to v are entangled. Orthogonality eliminates this entanglement: since ⟨eᵢ, eⱼ⟩ = 0 for i ≠ j, projecting onto eᵢ picks up only the eᵢ component of v and nothing from the other directions."
  explanation: "This independence is why orthonormal bases appear throughout numerical linear algebra, signal processing (Fourier series), and quantum mechanics. The coordinate formula v = Σ⟨v, eᵢ⟩eᵢ is simple precisely because orthogonality ensures the basis directions are genuinely independent channels."
```

## Explainer

The inner product you already know measures geometric alignment: ⟨u, v⟩ = ‖u‖‖v‖cosθ. Two vectors are **orthogonal** when ⟨u, v⟩ = 0 — they point in completely independent directions, sharing nothing. Think of the standard x- and y-axes: how far east you travel tells you nothing about how far north you've gone. Orthogonality formalizes this geometric independence in any inner product space.

An **orthonormal set** adds the requirement that each vector has length 1: ⟨eᵢ, eᵢ⟩ = 1, and ⟨eᵢ, eⱼ⟩ = 0 for i ≠ j. The standard basis {e₁, e₂, e₃} of R³ is the canonical example — three unit vectors along the coordinate axes, perfectly perpendicular to each other. But orthonormal sets appear in every inner product space, including spaces of functions where ⟨f, g⟩ = ∫f(x)g(x)dx.

The power of an orthonormal basis is the coordinate formula it enables. With a general basis, finding the coordinates of a vector v requires solving a system of equations — a potentially messy computation where the basis vectors' mutual interactions must be disentangled. With an orthonormal basis {e₁, ..., eₙ}, this collapses entirely: v = Σ⟨v, eᵢ⟩eᵢ. Each coefficient ⟨v, eᵢ⟩ is simply the projection of v onto eᵢ — one dot product, readable directly. You can compute each component independently, without the others interfering.

This independence is the structural advantage orthonormal bases provide throughout linear algebra and analysis. Errors in one component do not propagate to others (numerical stability). Each coefficient has a direct geometric meaning as the "amount of v in the eᵢ direction." When you study the Gram-Schmidt process next, you will learn to *construct* an orthonormal basis from any linearly independent set — transforming a messy basis into a clean one by systematically removing the components each new vector shares with the previous ones.
