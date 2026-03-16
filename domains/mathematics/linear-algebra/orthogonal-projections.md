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

## Explainer

The orthogonal projection of b onto a subspace W is the unique vector in W that is closest to b. This idea connects directly to your knowledge of inner product spaces: the inner product measures "how much" one vector aligns with another, so the projection formula extracts the W-component of b by taking inner products with basis vectors of W.

To understand why the formula works, start with the 1D case. If W is spanned by a single unit vector u, then proj_W(b) = ⟨b, u⟩u. The inner product ⟨b, u⟩ is a scalar saying how far b extends in the u-direction; multiplying by u converts that scalar back into a vector. The formula for projecting onto a higher-dimensional subspace with orthonormal basis u₁, ..., uₖ just repeats this independently for each basis vector and sums: proj_W(b) = ⟨b, u₁⟩u₁ + ... + ⟨b, uₖ⟩uₖ.

The key geometric insight is that b decomposes into exactly two orthogonal pieces: the projection proj_W(b) lying in W, and the **error vector** b - proj_W(b) lying in W⊥ (the orthogonal complement). These two pieces are perpendicular by construction. The fact that the error lives in W⊥ is precisely why proj_W(b) is the *closest* point in W to b: any other w ∈ W would require adding some W-component to the error, which by the Pythagorean theorem only increases the distance.

This decomposition drives two major applications. In **least-squares approximation**, Ax = b has no exact solution when b is not in the column space of A, so you project b onto the column space and solve the projected system — producing the best possible approximation. In **Gram-Schmidt**, you iteratively subtract projections onto previously found directions: each new vector has all prior directions projected out, leaving only the genuinely new component. Both applications rely on the same geometric core — decomposing a vector into the part that lives in a subspace and the part that is orthogonal to it.
