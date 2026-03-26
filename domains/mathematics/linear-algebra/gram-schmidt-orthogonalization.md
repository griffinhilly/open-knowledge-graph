---
id: gram-schmidt-orthogonalization
title: Gram-Schmidt Process and QR Decomposition
domain: mathematics
course: linear-algebra
prerequisites:
- id: orthogonal-vectors-orthonormal-bases
  type: hard
builds-toward:
- orthogonal-projections-least-squares
- least-squares-approximation
tags:
- gram-schmidt
- orthogonalization
- qr-decomposition
stage: formal-systems
status: validated
---

# Gram-Schmidt Process and QR Decomposition

## Core Idea
The Gram-Schmidt process converts a linearly independent set {v₁, ..., vₖ} into an orthonormal set by iteratively projecting out previously computed directions. It produces vectors u₁, u₂, ... where uᵢ is perpendicular to all u₁, ..., uᵢ₋₁. QR decomposition writes A = QR where Q has orthonormal columns and R is upper triangular, computed via Gram-Schmidt. This is numerically superior to solving normal equations.

## Questions

```yaml
- question: "After applying Gram-Schmidt to {v₁, v₂, v₃} to produce {u₁, u₂, u₃}, which statements are guaranteed to be true?"
  type: multiple-choice
  options:
    - "span{u₁} = span{v₁, v₂, v₃} — the first output vector spans the full original space"
    - "span{u₁, u₂} = span{v₁, v₂} — the process preserves the subspace structure at each prefix"
    - "u₁ = v₁ — the first output is always identical to the first input"
    - "u₃ is the projection of v₃ onto the plane spanned by u₁ and u₂"
  answer: 1
  explanation: "The key structural guarantee of Gram-Schmidt is that span{u₁, …, uᵢ} = span{v₁, …, vᵢ} at every step — the orthonormal prefix spans the same subspace as the original prefix. This is more than just saying the full sets span the same space; the agreement holds at every intermediate level. Option A is wrong: u₁ spans only the line through v₁, not the full space. Option C is wrong: u₁ = v₁/‖v₁‖ (normalized, not identical, unless v₁ already has unit length). Option D has the direction inverted — u₃ is the *residual* of v₃ after projecting out u₁ and u₂ directions, then normalized."

- question: "A numerical analyst must solve a least-squares problem Ax = b where the columns of A are nearly linearly dependent. She must choose between forming AᵀA and solving the normal equations, or computing A = QR and solving via back-substitution. Which is numerically safer and why?"
  type: multiple-choice
  options:
    - "Normal equations — they reduce the problem from a rectangular to a square system, which is simpler"
    - "QR decomposition — it avoids squaring the condition number of A, preventing amplification of floating-point errors"
    - "Both methods produce identical numerical results because they solve the same mathematical problem"
    - "Normal equations — AᵀA is always symmetric positive definite, which guarantees stability"
  answer: 1
  explanation: "When the columns of A are nearly linearly dependent, A has a large condition number κ. Forming AᵀA squares the condition number to κ², dramatically amplifying rounding errors. This can make the normal equations numerically useless even when the true solution is well-defined. QR decomposition avoids this: solving via the orthonormal Q and triangular R never squares the condition number. Option C is mathematically true but practically false — identical in exact arithmetic, but hugely different under floating-point. Option D is also true but misses the point: symmetric positive definite is not sufficient for stability when the condition number is enormous."

- question: "The Gram-Schmidt process can be applied to any set of vectors, linearly independent or not, and generally produces an orthonormal set of the same size as the input."
  type: true-false
  answer: false
  explanation: "When a vector is linearly dependent on the preceding ones, its residual after subtracting all projections is the zero vector — which cannot be normalized (division by zero). The process breaks down at that vector. In practice, a linearly dependent vector is discarded, and the output set is smaller than the input. Gram-Schmidt produces an orthonormal basis for the *span* of the input vectors; if the inputs are linearly dependent, the span has dimension less than the number of input vectors."

- question: "In QR decomposition A = QR, the matrix R is upper triangular because each new orthonormal vector is built by subtracting projections only onto previously computed basis vectors, not future ones."
  type: true-false
  answer: true
  explanation: "The entry Rᵢⱼ records the projection coefficient of vⱼ onto uᵢ. When processing vⱼ during Gram-Schmidt, you subtract projections onto u₁, …, uⱼ₋₁ (vectors already built). Vectors uⱼ, uⱼ₊₁, …, uₖ have not yet been constructed, so there are no projection terms involving them. Consequently Rᵢⱼ = 0 whenever i > j — upper triangular. The triangular structure is not an imposed constraint; it is a direct consequence of the sequential, forward-only structure of the Gram-Schmidt algorithm."

- question: "Why does Gram-Schmidt subtract projections onto ALL previously computed orthonormal vectors at each step, rather than just the most recent one?"
  type: short-answer
  answer: "Because each new vector uᵢ must be perpendicular to the entire set {u₁, …, uᵢ₋₁}, not just the previous vector uᵢ₋₁. If you only subtracted the projection onto uᵢ₋₁, the residual might still have components along u₁, …, uᵢ₋₂ from earlier steps. By subtracting the projection onto every previously established direction simultaneously, you remove all those components and guarantee the residual is orthogonal to the full set built so far. Each projection subtraction eliminates one direction; you need as many subtractions as there are previously established directions."
  explanation: "This is why the algorithm is iterative rather than pairwise. The orthogonality requirement is cumulative — each new vector must be orthogonal not just to its neighbor but to everything that came before. Classical Gram-Schmidt does all these subtractions simultaneously, while modified Gram-Schmidt applies them sequentially to improve numerical stability, but both achieve the same mathematical result."
```

## Explainer

From your prerequisite on orthogonality, you know that an **orthonormal set** of vectors is one where every vector has unit length and every pair of distinct vectors is perpendicular. Working in an orthonormal basis is computationally ideal: projections become dot products, and coordinates are computed without solving any systems. The Gram-Schmidt process answers the question: given any linearly independent set of vectors, how do you replace them with an orthonormal set that spans the same space?

The core idea is **iterative projection and subtraction**. Start with v₁: normalize it to get u₁ = v₁/‖v₁‖. Now take v₂: it has some component in the direction of u₁ and some component perpendicular to u₁. The component in the u₁ direction is (v₂ · u₁)u₁ — the projection of v₂ onto u₁. Subtract this out: v₂ − (v₂ · u₁)u₁ is the part of v₂ that is perpendicular to u₁. Normalize this residual to get u₂. Now u₁ and u₂ are orthonormal and span the same plane as v₁ and v₂. For v₃, subtract its projections onto both u₁ and u₂, leaving the component perpendicular to both, then normalize. Each step "peels off" the contributions of previously computed directions, leaving a new direction orthogonal to all of them. The order matters — you process the original vectors in sequence, and each new orthonormal vector is built from the residual after removing all earlier influences.

The process produces a set {u₁, ..., uₖ} where span{u₁, ..., uᵢ} = span{v₁, ..., vᵢ} at every step — the orthonormal basis agrees with the original basis at each prefix. This is the key structural property: you're not just finding any orthonormal basis for the whole space; you're finding one that progressively refines through the same subspaces as the original vectors. This structure is exactly what **QR decomposition** captures. If A is a matrix whose columns are v₁, ..., vₖ, then Gram-Schmidt produces Q (columns are u₁, ..., uₖ — orthonormal) and R (upper triangular — encodes how each vᵢ decomposes in terms of the u₁, ..., uᵢ directions). The entry Rᵢⱼ records the projection coefficient of vⱼ onto uᵢ, which is why R is upper triangular: when processing vⱼ, you only subtract projections onto u₁, ..., uⱼ₋₁.

QR decomposition is numerically preferred over the **normal equations** approach to least squares (Aᵀ A x = Aᵀ b) because forming Aᵀ A squares the condition number of A — it amplifies numerical errors. Solving via QR avoids squaring the condition number and is more stable when columns of A are nearly linearly dependent. This is why most numerical libraries (NumPy, LAPACK) use QR-based algorithms rather than normal equations for least-squares problems. The Gram-Schmidt process is the conceptual foundation, but in practice **modified Gram-Schmidt** or **Householder reflections** are used instead, because they maintain orthogonality more reliably under floating-point arithmetic — small rounding errors in classical Gram-Schmidt accumulate and make the resulting vectors gradually lose their perpendicularity.
