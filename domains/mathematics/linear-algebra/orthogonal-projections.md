---
id: orthogonal-projections
title: Orthogonal Projections
domain: mathematics
course: linear-algebra
prerequisites:
- id: inner-product-spaces
  type: hard
builds-toward:
- gram-schmidt-process
- least-squares-approximation
tags:
- orthogonal-projection
- projection
- nearest-point
stage: formal-systems
status: draft
---

# Orthogonal Projections

## Core Idea
The orthogonal projection of vector b onto a subspace W is the unique point proj_W(b) ∈ W closest to b. For a subspace spanned by orthonormal vectors u₁, ..., uₖ, proj_W(b) = (⟨b,u₁⟩u₁ + ... + ⟨b,uₖ⟩uₖ). Projections are fundamental to least-squares and Gram–Schmidt.

## Questions

```yaml
- question: "Vector b is projected onto subspace W, giving proj_W(b). Why is proj_W(b) the closest point in W to b, rather than some other vector in W?"
  type: multiple-choice
  options:
    - "Because the projection formula minimizes the number of basis vectors used"
    - "Because the error vector b − proj_W(b) is orthogonal to W, so any other choice increases distance by the Pythagorean theorem"
    - "Because the inner products ⟨b, uᵢ⟩ are always non-negative, ensuring minimum distance"
    - "Because proj_W(b) lies in W, and all vectors in W are equidistant from b"
  answer: 1
  explanation: "The error vector e = b − proj_W(b) is perpendicular to W by construction. For any other w ∈ W, write b − w = e + (proj_W(b) − w). Since e ⊥ W and (proj_W(b) − w) ∈ W, these are orthogonal, and by the Pythagorean theorem: ‖b − w‖² = ‖e‖² + ‖proj_W(b) − w‖² ≥ ‖e‖². So any other w is at least as far from b as the projection."

- question: "If {u₁, u₂} is an orthonormal basis for W and proj_W(b) = ⟨b,u₁⟩u₁ + ⟨b,u₂⟩u₂, what can we say about the vector b − proj_W(b)?"
  type: multiple-choice
  options:
    - "It lies in W, because it is a linear combination of u₁ and u₂"
    - "It is zero, because the projection formula accounts for all components of b"
    - "It lies in W⊥, perpendicular to every vector in W"
    - "Its magnitude equals ‖b‖, because the projection preserves length"
  answer: 2
  explanation: "The error vector b − proj_W(b) is the part of b that the projection 'left behind.' For any basis vector uᵢ: ⟨b − proj_W(b), uᵢ⟩ = ⟨b, uᵢ⟩ − ⟨b, uᵢ⟩ = 0. Since the error is orthogonal to every basis vector of W, it is orthogonal to every vector in W — it lies in W⊥."

- question: "The formula proj_W(b) = ⟨b,u₁⟩u₁ + ⟨b,u₂⟩u₂ gives the correct orthogonal projection for any basis {u₁, u₂} of W."
  type: true-false
  answer: false
  explanation: "False. This formula works only when {u₁, u₂} is an orthonormal basis — each vector has unit length and they are mutually orthogonal. For a general (non-orthonormal) basis, the formula overcounts or undercounts contributions because the basis vectors are not independent in the inner-product sense. The correct formula for a non-orthonormal basis requires the Gram matrix (AᵀA)⁻¹Aᵀ — precisely the least-squares normal equation. This is why Gram-Schmidt, which converts any basis to an orthonormal one, is so useful."

- question: "The orthogonal projection of b onto W always lies strictly between b and the origin."
  type: true-false
  answer: false
  explanation: "False. The projection can be anywhere in W — including at the origin (if b ⊥ W, the projection is 0) or at b itself (if b ∈ W, the projection is b). The projection minimizes distance from b to W, but that doesn't constrain where in W the projected point falls. For example, if b is perpendicular to the line W, proj_W(b) = 0."

- question: "Why does the error vector b − proj_W(b) lie in W⊥? Explain using the projection formula."
  type: short-answer
  answer: "For each orthonormal basis vector uᵢ of W: ⟨b − proj_W(b), uᵢ⟩ = ⟨b, uᵢ⟩ − ⟨proj_W(b), uᵢ⟩ = ⟨b, uᵢ⟩ − ⟨b, uᵢ⟩ = 0. Since the error is orthogonal to every basis vector of W, it is orthogonal to every vector in W, so it lies in W⊥."
  explanation: "The projection formula is constructed to extract the W-component of b. What remains after subtracting this component must be orthogonal to W. This decomposition b = proj_W(b) + (b − proj_W(b)) into a W-part and a W⊥-part is the fundamental theorem of orthogonal projections, and it is why the projection is the closest point in W to b."
```

## Explainer

The orthogonal projection of b onto a subspace W is the unique vector in W that is closest to b. This idea connects directly to your knowledge of inner product spaces: the inner product measures "how much" one vector aligns with another, so the projection formula extracts the W-component of b by taking inner products with basis vectors of W.

To understand why the formula works, start with the 1D case. If W is spanned by a single unit vector u, then proj_W(b) = ⟨b, u⟩u. The inner product ⟨b, u⟩ is a scalar saying how far b extends in the u-direction; multiplying by u converts that scalar back into a vector. The formula for projecting onto a higher-dimensional subspace with orthonormal basis u₁, ..., uₖ just repeats this independently for each basis vector and sums: proj_W(b) = ⟨b, u₁⟩u₁ + ... + ⟨b, uₖ⟩uₖ.

The key geometric insight is that b decomposes into exactly two orthogonal pieces: the projection proj_W(b) lying in W, and the **error vector** b - proj_W(b) lying in W⊥ (the orthogonal complement). These two pieces are perpendicular by construction. The fact that the error lives in W⊥ is precisely why proj_W(b) is the *closest* point in W to b: any other w ∈ W would require adding some W-component to the error, which by the Pythagorean theorem only increases the distance.

This decomposition drives two major applications. In **least-squares approximation**, Ax = b has no exact solution when b is not in the column space of A, so you project b onto the column space and solve the projected system — producing the best possible approximation. In **Gram-Schmidt**, you iteratively subtract projections onto previously found directions: each new vector has all prior directions projected out, leaving only the genuinely new component. Both applications rely on the same geometric core — decomposing a vector into the part that lives in a subspace and the part that is orthogonal to it.
