---
id: orthonormal-bases
title: Orthonormal Bases
domain: mathematics
course: linear-algebra
prerequisites:
- id: orthogonality-in-linear-algebra
  type: hard
- id: basis-and-dimension
  type: hard
builds-toward:
- gram-schmidt-process
- spectral-theorem
tags:
- orthonormal
- ONB
- orthogonal matrix
- coordinates
- Fourier coefficients
stage: formal-systems
status: validated
---

# Orthonormal Bases

## Core Idea
An orthonormal basis (ONB) is a basis in which every vector has unit norm and every pair of distinct vectors is orthogonal. Orthonormal bases make coordinate computation trivial: the coordinate of a vector v with respect to basis vector uᵢ is simply ⟨v, uᵢ⟩. A matrix whose columns form an orthonormal basis is called an orthogonal matrix Q, satisfying QᵀQ = I (so Qᵀ = Q⁻¹). Orthogonal matrices preserve lengths and angles, making them the natural matrices for rotations and reflections. Orthonormal bases are the 'gold standard' basis choice in both theory and computation.

## How It's Best Learned
Verify that QᵀQ = I for rotation matrices and reflection matrices in R². Observe that computing coordinates in an orthonormal basis via dot products is far simpler than solving a linear system as required for non-orthogonal bases.

## Common Misconceptions
- An 'orthogonal matrix' has orthonormal columns, not merely orthogonal ones — the columns must also have unit length.
- Qᵀ = Q⁻¹ only when Q is a square orthogonal matrix; for a non-square matrix with orthonormal columns, QᵀQ = I but QQᵀ ≠ I.
- Students confuse orthogonal sets (merely pairwise perpendicular) with orthonormal bases (perpendicular AND unit length AND spanning).

## Questions

```yaml
- question: "A square matrix Q has columns that are pairwise orthogonal (each pair is perpendicular). A student concludes that Q is an orthogonal matrix, so Qᵀ = Q⁻¹. Is the student correct?"
  type: multiple-choice
  options:
    - "Yes — pairwise orthogonality of columns is sufficient for Qᵀ = Q⁻¹"
    - "No — the columns must also have unit length; without normalization, QᵀQ ≠ I"
    - "No — Q must also be symmetric for the property to hold"
    - "Yes — for square matrices, orthogonal columns always satisfy QᵀQ = I"
  answer: 1
  explanation: "The term 'orthogonal matrix' is confusingly named: it requires orthonormal columns, not merely orthogonal ones. QᵀQ = I requires that columns have unit length AND are pairwise perpendicular. If columns are perpendicular but not unit length, QᵀQ is a diagonal matrix with the squared norms on the diagonal — not the identity. The student identified one of the two required conditions and missed the other."

- question: "You are working in ℝⁿ with an orthonormal basis {u₁, u₂, ..., uₙ}. How do you find the coordinate of a vector v with respect to u₃?"
  type: multiple-choice
  options:
    - "Solve the linear system Uc = v for c, then take the third component"
    - "Compute ⟨v, u₃⟩ — the inner product of v with u₃"
    - "Project v onto the span of {u₁, u₂} and subtract from v, then normalize"
    - "Compute ‖v‖ / ‖u₃‖"
  answer: 1
  explanation: "This is the defining computational advantage of an orthonormal basis. For a general basis, finding coordinates requires solving a linear system. For an ONB, the coordinate with respect to uᵢ is simply ⟨v, uᵢ⟩. This works because when you expand v = c₁u₁ + ... + cₙuₙ and take the inner product with u₃, all terms vanish by orthogonality except ⟨c₃u₃, u₃⟩ = c₃·1 = c₃. The unit-length condition is what eliminates the denominator."

- question: "If Q is an orthogonal matrix, then the transformation v ↦ Qv preserves both lengths and angles."
  type: true-false
  answer: true
  explanation: "Orthogonal matrices preserve the inner product: ⟨Qu, Qv⟩ = ⟨u, v⟩. Since lengths are determined by ‖v‖ = √⟨v,v⟩ and angles by cos θ = ⟨u,v⟩/(‖u‖‖v‖), preserving inner products implies preserving both. This is why rotations and reflections are orthogonal matrices — they are precisely the rigid motions of space."

- question: "Any set of nonzero pairwise-orthogonal vectors forms an orthonormal basis for its span."
  type: true-false
  answer: false
  explanation: "An orthonormal basis requires three properties: (1) pairwise orthogonality, (2) unit length for every vector, and (3) spanning. A set of pairwise-orthogonal nonzero vectors satisfies (1) and (3) but not necessarily (2). For example, {(2,0), (0,3)} is pairwise orthogonal but neither vector has unit length, so it is not orthonormal. Dividing each vector by its norm gives the orthonormal version {(1,0), (0,1)}."

- question: "Why does computing coordinates in an orthonormal basis reduce to taking dot products, whereas in a general basis it requires solving a linear system?"
  type: short-answer
  answer: "In a general basis, the basis vectors are not perpendicular, so when you expand v = c₁b₁ + ... + cₙbₙ and take the inner product with one basis vector bᵢ, the cross-terms ⟨cⱼbⱼ, bᵢ⟩ for j ≠ i don't vanish — they produce a system of equations coupling all coordinates simultaneously. In an ONB, ⟨uᵢ, uⱼ⟩ = 0 for i ≠ j, so every cross-term drops out, leaving ⟨v, uᵢ⟩ = cᵢ directly. Orthogonality decouples the coordinates; normalization removes the denominators."
  explanation: "The key structure is the Gram matrix: for a general basis, coordinates require inverting [⟨bᵢ,bⱼ⟩]ᵢⱼ. For an ONB, the Gram matrix is the identity, so the coordinates are just dot products. This decoupling is the computational miracle that makes orthonormal bases the preferred choice whenever flexibility of basis choice exists."
```

## Explainer

From your work on orthogonality and bases, you know two ideas separately: vectors can be perpendicular to each other (orthogonality), and a basis is a linearly independent spanning set. An **orthonormal basis** (ONB) combines both properties at once and adds a normalization condition: every basis vector has length exactly 1, and every pair of distinct basis vectors is perpendicular. The standard basis {e₁, e₂, e₃} in ℝ³ is the simplest example — unit vectors along each axis, mutually perpendicular.

The great computational payoff of an ONB is coordinate extraction via inner products. Recall that with a general basis, finding coordinates requires solving a linear system. With an ONB {u₁, u₂, ..., uₙ}, the coordinate of any vector v with respect to uᵢ is simply the inner product ⟨v, uᵢ⟩. No system-solving required — just n dot products. This works because orthogonality eliminates all cross-terms: when you expand v in the basis and take the inner product with uᵢ, every term involving a different basis vector drops to zero. The formula v = ⟨v, u₁⟩u₁ + ⟨v, u₂⟩u₂ + ... + ⟨v, uₙ⟩uₙ is one of the most useful formulas in linear algebra.

When the column vectors of a square matrix Q form an ONB, something remarkable happens: QᵀQ = I, so Qᵀ = Q⁻¹. This means you can invert Q just by transposing it — no row reduction needed. Such matrices are called **orthogonal matrices**. Geometrically, they represent transformations that preserve lengths and angles: ‖Qv‖ = ‖v‖ and ⟨Qu, Qv⟩ = ⟨u, v⟩. Every rotation and reflection is an orthogonal matrix. This length-preservation property is what makes orthogonal matrices the natural choice for representing rigid motions and for numerically stable computations.

The standard basis is one ONB, but there are infinitely many others. Any rotation of the standard basis produces another ONB. This flexibility is central to applications: in Fourier analysis, the sines and cosines form an ONB for function spaces; in data analysis (PCA), you find an ONB aligned with the directions of maximum variance. The Gram-Schmidt process (your next topic) provides the algorithm for constructing an ONB from any linearly independent set. Once you have it, coordinates become dot products, inverses become transposes, and the geometry of the space becomes transparent.
