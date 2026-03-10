---
id: orthogonal-projections
title: Orthogonal Projections
domain: mathematics
course: linear-algebra
prerequisites:
- id: gram-schmidt-process
  type: hard
- id: subspaces
  type: hard
- id: inner-product-spaces
  type: soft
builds-toward:
- least-squares-approximation
tags:
- projection
- orthogonal projection
- projection matrix
- best approximation
- decomposition
stage: formal-systems
status: draft
---

# Orthogonal Projections

## Core Idea
The orthogonal projection of a vector b onto a subspace W is the vector p in W closest to b, characterized by the condition that b − p is orthogonal to every vector in W (the 'hat theorem'). If {u₁, …, uₖ} is an orthonormal basis for W, then p = ⟨b,u₁⟩u₁ + … + ⟨b,uₖ⟩uₖ. The projection matrix P = QQᵀ (where Q has orthonormal columns spanning W) satisfies P² = P and Pᵀ = P — the defining properties of an orthogonal projector. Orthogonal projection is the theoretical foundation for least squares and the best-approximation theorem.

## How It's Best Learned
Compute projections onto lines and planes in R³ both with and without an orthonormal basis. Verify the best-approximation property by confirming ‖b − p‖ < ‖b − w‖ for any w in W with w ≠ p.

## Common Misconceptions
- The projection p lies IN the subspace W; the residual b − p is ORTHOGONAL to W; these are different objects.
- Projecting b onto W twice gives the same result as once: P(Pb) = Pb, because p is already in W.
- Students sometimes project onto a vector instead of a subspace — these are the same when the subspace is a line, but differ in general.
