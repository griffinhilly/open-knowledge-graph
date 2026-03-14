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
