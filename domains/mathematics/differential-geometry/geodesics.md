---
id: geodesics
title: Geodesics
domain: mathematics
course: differential-geometry
prerequisites:
  - id: connections-and-covariant-derivative
    type: hard
  - id: riemannian-metrics
    type: hard
  - id: parallel-transport
    type: soft
tags:
  - geodesics
  - shortest-paths
  - geodesic-equation
  - energy-functional
stage: expert
status: validated
---

# Geodesics

## Core Idea
Geodesics are curves that parallel-transport their own velocity — formally, ∇_{γ'} γ' = 0. They generalize straight lines to curved spaces: on a Riemannian manifold, geodesics are locally length-minimizing, and they are the critical points of the energy functional. The geodesic equation is a system of second-order ODEs whose solutions are determined by an initial point and initial velocity. Great circles on spheres, straight lines in Euclidean space, and freefall trajectories in general relativity are all geodesics.

## Questions

```yaml
- question: "A geodesic on a Riemannian manifold locally minimizes length. Does a geodesic always globally minimize length between its endpoints?"
  type: multiple-choice
  options:
    - "Yes — geodesics are always the shortest paths"
    - "No — geodesics are only locally length-minimizing; beyond the cut point, shorter paths may exist"
    - "No — geodesics maximize length, not minimize it"
    - "Geodesics minimize length if and only if the manifold has non-negative curvature"
  answer: 1
  explanation: "Geodesics are locally length-minimizing: any sufficiently short segment is the shortest path between its endpoints. But globally, a geodesic may cease to minimize. On the sphere, a great-circle arc shorter than a half-circle is minimizing, but past the antipodal point, there are shorter paths going the other way. The cut point is where a geodesic first fails to minimize. Between a point and its cut point, the geodesic is the unique shortest path. Beyond it, shorter paths exist."

- question: "The geodesic equation in coordinates is d²γᵏ/dt² + Γᵏᵢⱼ (dγⁱ/dt)(dγʲ/dt) = 0. This is a second-order ODE, so geodesics are determined by..."
  type: multiple-choice
  options:
    - "A starting point p only"
    - "A starting point p and initial velocity v ∈ TpM"
    - "Two distinct points p, q on the manifold"
    - "A starting point p, initial velocity v, and the curvature at p"
  answer: 1
  explanation: "As a second-order ODE, the geodesic equation has a unique solution given initial position γ(0) = p and initial velocity γ'(0) = v. This is analogous to Newton's second law: the trajectory of a particle is determined by its initial position and velocity. By contrast, two points do NOT uniquely determine a geodesic — on a sphere, there are infinitely many great circles through two non-antipodal points (well, exactly one great circle, but antipodal points have infinitely many). The curvature enters through the Christoffel symbols, not as separate initial data."

- question: "On a Riemannian manifold, geodesics are both locally length-minimizing curves and curves that parallel-transport their own velocity vector. Why are these two characterizations equivalent?"
  type: short-answer
  answer: "The length-minimizing characterization comes from the calculus of variations: critical points of the length (or energy) functional satisfy the Euler-Lagrange equation, which turns out to be exactly the geodesic equation ∇_{γ'}γ' = 0. The parallel-transport characterization says the velocity is 'constant' along the curve — the curve has zero acceleration. Both descriptions yield the same ODE. The connection is that a curve with constant-speed and zero acceleration is precisely one that cannot be shortened by small perturbations."
  explanation: "Technically, geodesics are critical points of the energy functional E(γ) = ½∫g(γ',γ')dt, not always minima (they could be saddle points). The equivalence between ∇_{γ'}γ' = 0 and the Euler-Lagrange equation for E is a direct computation in local coordinates. The energy functional is preferred over the length functional because it gives a nicer (non-degenerate) second variation and its critical points are automatically constant-speed."

- question: "All geodesics on a compact Riemannian manifold are defined for all time (complete)."
  type: true-false
  answer: true
  explanation: "This is the Hopf-Rinow theorem: a Riemannian manifold is geodesically complete (all geodesics extend to all time) if and only if it is complete as a metric space. Compact manifolds are complete, so they are geodesically complete. On non-compact manifolds, geodesics can fail to be complete — for instance, on the punctured plane ℝ² \ {0}, geodesics aimed at the origin cannot be extended past the missing point."
```

## Explainer

In Euclidean space, straight lines are characterized in three equivalent ways: (1) they minimize distance, (2) they have zero acceleration, and (3) they parallel-transport their own velocity. On a Riemannian manifold, these three properties continue to characterize the same class of curves — **geodesics** — but the equivalence is nontrivial and depends on the connection.

The **geodesic equation** ∇_{γ'} γ' = 0 says that the covariant acceleration of γ vanishes. In coordinates: d²γᵏ/dt² + Γᵏᵢⱼ (dγⁱ/dt)(dγʲ/dt) = 0. The Christoffel symbol term is the "centripetal" correction that accounts for the curving of coordinate lines — on a sphere, great circles satisfy this equation even though their coordinate expressions are curved in (θ, φ) coordinates. Solutions exist and are unique for given initial point p = γ(0) and initial velocity v = γ'(0) ∈ TpM, by the existence and uniqueness theorem for ODEs.

Geodesics are also the critical points of the **energy functional** E(γ) = ½∫₀¹ |γ'(t)|² dt. The Euler-Lagrange equation for this variational problem is exactly the geodesic equation. Using energy rather than length is technically convenient: energy critical points are automatically constant-speed, and the second variation formula is cleaner. A geodesic is a local minimum of energy (and hence of length among constant-speed curves) when the second variation is positive — this fails when the geodesic passes through a **conjugate point**, where nearby geodesics refocus.

The **Hopf-Rinow theorem** connects geodesic completeness to metric completeness: on a complete Riemannian manifold, any two points are connected by a length-minimizing geodesic. This is the manifold analogue of "the shortest path between two points is a straight line." The theorem fails without completeness — on an incomplete manifold (like ℝⁿ with a point removed), geodesics can run into the missing region. The cut locus of a point p — the set of points beyond which geodesics from p cease to minimize — is a fundamental geometric object that encodes the global structure of the metric.
