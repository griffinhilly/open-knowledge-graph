---
id: curvature-tensor
title: Curvature Tensor
domain: mathematics
course: differential-geometry
prerequisites:
  - id: connections-and-covariant-derivative
    type: hard
  - id: parallel-transport
    type: hard
  - id: lie-brackets
    type: soft
tags:
  - curvature
  - riemann-curvature-tensor
  - curvature-tensor
  - tidal-forces
stage: expert
status: validated
---

# Curvature Tensor

## Core Idea
The Riemann curvature tensor R(X,Y)Z measures the failure of covariant differentiation to commute: R(X,Y)Z = ∇_X ∇_Y Z - ∇_Y ∇_X Z - ∇_{[X,Y]} Z. Equivalently, it measures the rotation a vector undergoes when parallel-transported around an infinitesimal loop. The curvature tensor is the fundamental invariant of a connection — it vanishes if and only if the manifold is locally flat (isometric to Euclidean space). All other curvature quantities (Ricci, scalar, sectional) are derived from it.

## Questions

```yaml
- question: "The Riemann curvature tensor R(X,Y)Z is defined as ∇_X ∇_Y Z - ∇_Y ∇_X Z - ∇_{[X,Y]} Z. Why is the [X,Y] term necessary?"
  type: multiple-choice
  options:
    - "To make R vanish in flat space — without it, R would be nonzero even on ℝⁿ with the standard connection"
    - "To make R a tensor — without the [X,Y] term, the expression would not be C∞(M)-linear in X and Y"
    - "To account for the torsion of the connection"
    - "Both A and B are correct"
  answer: 3
  explanation: "Both reasons are correct and related. On flat ℝⁿ with the standard connection, ∇_X ∇_Y Z - ∇_Y ∇_X Z = [X,Y](Z) (because partial derivatives commute), so subtracting ∇_{[X,Y]}Z gives zero — as it should, since flat space has no curvature. Without the [X,Y] term, the expression would be nonzero in flat space when X and Y have a nonzero bracket. Moreover, the [X,Y] term is exactly what is needed to make R C∞(M)-linear in X and Y (i.e., tensorial), which is necessary for R to define a pointwise multilinear map."

- question: "The Riemann curvature tensor of an n-dimensional Riemannian manifold has n⁴ components Rⁱⱼₖₗ, but the symmetries of the tensor greatly reduce the number of independent components. For n = 4 (spacetime), how many independent components does the Riemann tensor have?"
  type: multiple-choice
  options:
    - "256 (no reduction)"
    - "20"
    - "10"
    - "6"
  answer: 1
  explanation: "The Riemann tensor has symmetries: Rᵢⱼₖₗ = -Rⱼᵢₖₗ = -Rᵢⱼₗₖ (antisymmetric in first and second pairs), Rᵢⱼₖₗ = Rₖₗᵢⱼ (pair symmetry), and the first Bianchi identity Rᵢⱼₖₗ + Rᵢₖₗⱼ + Rᵢₗⱼₖ = 0. Together these reduce the n⁴ = 256 components to n²(n²-1)/12 = 20 independent components for n = 4. For n = 2, there is only 1 independent component (the Gaussian curvature). For n = 3, there are 6."

- question: "A Riemannian manifold has vanishing curvature tensor (R = 0) if and only if it is locally isometric to Euclidean space."
  type: true-false
  answer: true
  explanation: "R = 0 means parallel transport is path-independent (in simply connected neighborhoods), which means you can define globally consistent 'constant' vector fields. These constant fields serve as a coordinate frame in which the metric has constant components gij = δij — so the manifold is locally flat. Conversely, Euclidean space has R = 0 because the standard connection has zero Christoffel symbols and partial derivatives commute. Note 'locally isometric' — a flat torus has R = 0 everywhere but is not globally isometric to ℝ² (it is a quotient of ℝ²)."

- question: "How does the curvature tensor relate to tidal forces in general relativity?"
  type: short-answer
  answer: "In general relativity, spacetime is a 4-dimensional Lorentzian manifold and the curvature tensor encodes the tidal gravitational field. Two freely falling particles (following geodesics) that start nearby will accelerate relative to each other due to curvature — this relative acceleration is given by the geodesic deviation equation d²Jᵏ/dt² = -Rᵏₗₘₙ γ'ˡ Jᵐ γ'ⁿ, where J is the separation vector. Curvature stretches and squeezes nearby geodesics, which is exactly what tidal forces do."
  explanation: "The geodesic deviation equation (or Jacobi equation) is the precise connection: the Riemann tensor acting on the velocity and separation vectors gives the tidal acceleration. In Newtonian gravity, tidal forces are the second derivatives of the gravitational potential; in GR, the Riemann tensor replaces and generalizes these second derivatives. This is why gravity in GR is curvature — not because massive objects 'bend space,' but because the curvature tensor encodes the physical tidal effects that are the observable content of gravity."
```

## Explainer

In Euclidean space, the order of partial differentiation does not matter: ∂²f/∂x∂y = ∂²f/∂y∂x. When you replace partial derivatives with covariant derivatives on a manifold, this commutativity generally fails. The **Riemann curvature tensor** R precisely measures this failure: for vector fields X, Y, Z, the expression R(X,Y)Z = ∇_X ∇_Y Z - ∇_Y ∇_X Z - ∇_{[X,Y]} Z measures how much "differentiating Z first in the Y then X direction" differs from "first in X then Y." The [X,Y] term corrects for the non-commutativity of X and Y as differential operators, isolating the contribution of the geometry.

The curvature tensor R is a (1,3)-tensor: it takes three vector inputs and returns a vector. In coordinates, R(∂ᵢ, ∂ⱼ)∂ₖ = Rˡₖᵢⱼ ∂ₗ, where Rˡₖᵢⱼ = ∂ᵢΓˡⱼₖ - ∂ⱼΓˡᵢₖ + ΓˡᵢₘΓᵐⱼₖ - ΓˡⱼₘΓᵐᵢₖ. Despite the complicated formula, the key message is: R is built algebraically from the Christoffel symbols and their first derivatives, and it transforms as a tensor. It has extensive symmetries: antisymmetry in the first pair and second pair of lowered indices, pair symmetry Rᵢⱼₖₗ = Rₖₗᵢⱼ, and the first Bianchi identity. These reduce the independent components from n⁴ to n²(n²-1)/12.

Geometrically, R(X,Y)v is the rotation that a vector v acquires when parallel transported around an infinitesimal parallelogram spanned by X and Y. If R = 0, parallel transport is path-independent (locally), and the manifold is flat — isometric to Euclidean space in a neighborhood of each point. If R ≠ 0, different paths between the same endpoints produce different parallel transport maps, and the manifold is genuinely curved. The holonomy group (the group of all parallel transport maps around loops at a point) is generated by the curvature.

The Riemann tensor is the master curvature invariant from which all others derive. Contracting one pair of indices gives the **Ricci tensor** Rᵢⱼ = Rᵏᵢₖⱼ, which encodes how volumes change along geodesics. Contracting again gives the **scalar curvature** R = gⁱʲRᵢⱼ, a single number at each point. The **sectional curvature** K(σ) measures curvature in a 2-plane σ ⊂ TpM. In two dimensions, all these reduce to a single function — the Gaussian curvature. In higher dimensions, they carry progressively more refined information about the geometry.
