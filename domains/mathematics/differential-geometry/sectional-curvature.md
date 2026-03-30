---
id: sectional-curvature
title: Sectional Curvature
domain: mathematics
course: differential-geometry
prerequisites:
  - id: curvature-tensor
    type: hard
  - id: riemannian-metrics
    type: hard
tags:
  - sectional-curvature
  - constant-curvature
  - space-forms
  - gaussian-curvature
stage: expert
status: validated
---

# Sectional Curvature

## Core Idea
The sectional curvature K(σ) of a 2-plane σ ⊂ TpM is the Gaussian curvature of the surface formed by geodesics tangent to σ. It is the finest pointwise curvature invariant and determines the full Riemann tensor. Spaces of constant sectional curvature — Euclidean space (K=0), spheres (K>0), and hyperbolic space (K<0) — are the model geometries of Riemannian geometry. Comparison theorems use sectional curvature bounds to control geodesic behavior, volume growth, and topology.

## Questions

```yaml
- question: "The sectional curvature K(σ) of a 2-plane σ = span{X, Y} ⊂ TpM is defined as K(σ) = g(R(X,Y)Y, X) / (g(X,X)g(Y,Y) - g(X,Y)²). The denominator is the squared area of the parallelogram spanned by X and Y. Why is this normalization needed?"
  type: multiple-choice
  options:
    - "To make K(σ) independent of the choice of basis {X, Y} for σ"
    - "To ensure K(σ) is always positive"
    - "To make K(σ) equal to the scalar curvature"
    - "To cancel the metric dependence so K(σ) is a topological invariant"
  answer: 0
  explanation: "The numerator g(R(X,Y)Y, X) depends on the specific vectors X, Y chosen to span σ — rescaling X by λ rescales the numerator by λ². Dividing by the squared area of the parallelogram (which scales the same way) makes the quotient depend only on the 2-plane σ, not on the basis. K(σ) is NOT always positive (hyperbolic space has K < 0), NOT equal to scalar curvature (that is a different contraction), and NOT a topological invariant (it depends on the metric)."

- question: "If a Riemannian manifold has constant sectional curvature K at every point and for every 2-plane, then it is locally isometric to one of three model spaces: Euclidean space (K=0), a sphere of radius 1/√K (K>0), or hyperbolic space of curvature K (K<0)."
  type: true-false
  answer: true
  explanation: "This is a fundamental classification theorem. Constant sectional curvature completely determines the local geometry — the Riemann tensor takes the form Rᵢⱼₖₗ = K(gᵢₖgⱼₗ - gᵢₗgⱼₖ), and the metric is locally that of the unique model space with that curvature. Complete, simply connected manifolds of constant curvature are exactly the three space forms: ℝⁿ, Sⁿ, Hⁿ. Non-simply-connected space forms are quotients of these by discrete isometry groups (e.g., ℝPⁿ = Sⁿ/ℤ₂, flat torus = ℝⁿ/ℤⁿ)."

- question: "In dimension 2, the sectional curvature at a point is the same as the Gaussian curvature. In higher dimensions, the sectional curvature contains strictly more information than the Ricci or scalar curvature. Why?"
  type: short-answer
  answer: "In dimension 2, there is only one 2-plane at each point (the entire tangent plane), so sectional curvature is a single number — which equals the Gaussian curvature. In higher dimensions, there are infinitely many 2-planes at each point, and the sectional curvature varies over them. The Ricci curvature in a direction v averages sectional curvatures of planes containing v, and the scalar curvature averages further. These averages lose information: manifolds with the same Ricci curvature can have different sectional curvatures. The sectional curvature function determines the full Riemann tensor, while Ricci and scalar curvature do not (in dimension ≥ 4)."
  explanation: "The fact that sectional curvature determines the full Riemann tensor is a consequence of the symmetries of R: knowing g(R(X,Y)Y,X) for all X,Y determines R by polarization. This is analogous to how a symmetric bilinear form is determined by its associated quadratic form."
```

## Explainer

The Riemann curvature tensor is a complicated object — it takes four vector inputs. **Sectional curvature** distills this to a function on 2-planes, which is both more geometric and more tractable. Given a 2-plane σ ⊂ TpM, consider the surface Σ traced out by geodesics starting at p with initial velocities in σ. The sectional curvature K(σ) is the Gaussian curvature of this surface at p. It measures how fast geodesics in the plane σ converge or diverge: K > 0 means geodesics converge (like on a sphere), K < 0 means they diverge (like in hyperbolic space), and K = 0 means they stay parallel (like in flat space).

The three **space forms** — Euclidean space ℝⁿ, the sphere Sⁿ, and hyperbolic space Hⁿ — are the complete, simply connected Riemannian manifolds of constant sectional curvature K = 0, K > 0, and K < 0 respectively. These are the "maximally symmetric" geometries: each admits an isometry group of dimension n(n+1)/2, the maximum possible. The classification theorem says these are the only possibilities for constant curvature. Every complete manifold of constant curvature is a quotient of one of these by a discrete group of isometries — the flat torus is ℝ²/ℤ², the real projective space is Sⁿ/ℤ₂, and hyperbolic surfaces are H²/Γ for various Fuchsian groups Γ.

**Comparison geometry** uses sectional curvature bounds to control the behavior of geodesics and volumes. If K ≤ κ (curvature bounded above), then geodesic triangles are "thinner" than in the model space of constant curvature κ — geodesics spread apart at least as fast. If K ≥ κ (curvature bounded below), geodesic triangles are "fatter." The **Rauch comparison theorem** makes this precise for Jacobi fields, and the **Toponogov triangle comparison theorem** extends it to global distance comparisons. These tools yield deep topological results: the sphere theorem (manifolds with ¼ < K ≤ 1 are homeomorphic to spheres), the Cartan-Hadamard theorem (complete manifolds with K ≤ 0 have contractible universal cover), and the soul theorem for non-negative curvature.

The relationship between sectional, Ricci, and scalar curvature forms a hierarchy of information. Constant sectional curvature is the strongest condition (the space form classification). Positive sectional curvature implies positive Ricci, which implies positive scalar curvature — but the converses are false. Each level of the hierarchy gives progressively weaker geometric and topological constraints. Understanding this hierarchy and finding optimal conditions for geometric conclusions is one of the driving programs in Riemannian geometry.
