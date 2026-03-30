---
id: levi-civita-connection
title: Levi-Civita Connection
domain: mathematics
course: differential-geometry
prerequisites:
  - id: connections-and-covariant-derivative
    type: hard
  - id: riemannian-metrics
    type: hard
  - id: lie-brackets
    type: soft
tags:
  - levi-civita-connection
  - metric-compatibility
  - torsion-free
  - christoffel-symbols
stage: expert
status: validated
---

# Levi-Civita Connection

## Core Idea
The Levi-Civita connection is the unique connection on a Riemannian manifold that is both torsion-free (∇_X Y - ∇_Y X = [X,Y]) and metric-compatible (∇g = 0, meaning parallel transport preserves inner products). Its existence and uniqueness — the Fundamental Theorem of Riemannian Geometry — means the Riemannian metric alone determines all of Riemannian geometry: connections, geodesics, curvature, and parallel transport.

## Questions

```yaml
- question: "The Christoffel symbols of the Levi-Civita connection can be computed from the metric alone using the formula Γᵏᵢⱼ = ½gᵏˡ(∂ᵢgⱼₗ + ∂ⱼgᵢₗ - ∂ₗgᵢⱼ). What two properties force this specific formula?"
  type: multiple-choice
  options:
    - "Symmetry in i,j (torsion-free) and positive-definiteness of g"
    - "Torsion-free (Γᵏᵢⱼ = Γᵏⱼᵢ) and metric compatibility (∂ₖgᵢⱼ = Γˡₖᵢgₗⱼ + Γˡₖⱼgᵢₗ)"
    - "Antisymmetry in i,j and the Bianchi identity"
    - "Metric compatibility and the Jacobi identity"
  answer: 1
  explanation: "The two defining properties are torsion-free (which makes Christoffel symbols symmetric: Γᵏᵢⱼ = Γᵏⱼᵢ) and metric compatibility (which says ∇g = 0, expressed in coordinates as ∂ₖgᵢⱼ = Γˡₖᵢgₗⱼ + Γˡₖⱼgᵢₗ). Writing the metric-compatibility equation three times with cyclically permuted indices and using symmetry of the Christoffel symbols, you can solve uniquely for Γ — this derivation is called the Koszul trick."

- question: "Metric compatibility (∇g = 0) has the geometric meaning that parallel transport preserves lengths and angles."
  type: true-false
  answer: true
  explanation: "If V and W are parallel along a curve γ (∇_{γ'} V = 0 and ∇_{γ'} W = 0), then d/dt g(V,W) = g(∇_{γ'} V, W) + g(V, ∇_{γ'} W) = 0. So the inner product is constant along the curve. Since length |V| = √g(V,V) and angle cos θ = g(V,W)/(|V||W|), both are preserved. This is physically natural: moving a ruler along a path should not change the ruler's length. Non-metric connections exist but lack this property."

- question: "Why is the torsion-free condition (rather than allowing torsion) the natural choice for Riemannian geometry?"
  type: short-answer
  answer: "The torsion-free condition means ∇_X Y - ∇_Y X = [X,Y], so the antisymmetric part of the connection carries no independent information beyond the Lie bracket. This ensures that geodesics depend only on the metric (not on extra torsion data), that the Christoffel symbols are symmetric, and that the connection is fully determined by the metric. Allowing torsion would introduce additional geometric degrees of freedom that the metric alone does not control. The uniqueness of the Levi-Civita connection — that the metric determines the connection — is only possible with the torsion-free condition."
  explanation: "In physics, torsion appears in Einstein-Cartan theory (where spinning matter sources torsion) and in string theory. But in pure Riemannian geometry, the torsion-free condition is universally adopted because it gives the most economical theory: one piece of input data (the metric) determines everything. If you allowed torsion, you would need to specify the metric AND the torsion tensor independently."

- question: "In normal coordinates centered at a point p, the Christoffel symbols of the Levi-Civita connection vanish at p: Γᵏᵢⱼ(p) = 0."
  type: true-false
  answer: true
  explanation: "Normal coordinates (or geodesic coordinates) at p are constructed using the exponential map: geodesics through p become straight lines in these coordinates. The Christoffel symbols vanish at p (the center) because the geodesic equation d²xᵏ/dt² + Γᵏᵢⱼ dxⁱ/dt dxʲ/dt = 0 must be satisfied by all straight lines through the origin, which forces Γᵏᵢⱼ(0) = 0. However, the derivatives of the Christoffel symbols at p are generally nonzero — they encode the curvature. Normal coordinates make the connection look flat to first order but reveal curvature at second order."
```

## Explainer

A smooth manifold admits many connections — they form an affine space (the difference of two connections is a tensor). On a Riemannian manifold, two natural conditions single out a unique connection. **Metric compatibility** (∇g = 0) says the connection "respects the metric": parallel transport preserves inner products, so lengths, angles, and volumes are unchanged by transport. **Torsion-free** (T(X,Y) = ∇_X Y - ∇_Y X - [X,Y] = 0) says the connection has no "twisting" beyond what the vector fields' flows naturally produce.

The **Fundamental Theorem of Riemannian Geometry** states: given a Riemannian metric g, there exists a unique connection ∇ that is both metric-compatible and torsion-free. This is the **Levi-Civita connection**. The proof is constructive — the Koszul formula gives ∇ explicitly: 2g(∇_X Y, Z) = X(g(Y,Z)) + Y(g(X,Z)) - Z(g(X,Y)) + g([X,Y],Z) - g([X,Z],Y) - g([Y,Z],X). In coordinates, this yields the Christoffel symbol formula Γᵏᵢⱼ = ½gᵏˡ(∂ᵢgⱼₗ + ∂ⱼgᵢₗ - ∂ₗgᵢⱼ). The metric alone determines everything.

The significance of this theorem cannot be overstated. It means that specifying a Riemannian metric on a manifold automatically gives you: a connection (hence covariant derivatives), parallel transport, geodesics, and curvature. All of Riemannian geometry flows from a single datum — the metric tensor gᵢⱼ. In general relativity, the spacetime metric encodes the gravitational field, and the Levi-Civita connection determines the freefall trajectories (geodesics) and tidal forces (curvature). Einstein's equations relate the curvature derived from g to the matter content of spacetime.

**Normal coordinates** provide a powerful computational tool. At any point p, you can choose coordinates in which gᵢⱼ(p) = δᵢⱼ (the identity matrix) and Γᵏᵢⱼ(p) = 0. In these coordinates, the connection looks flat at the point p, and curvature appears only in the second-order terms of the Taylor expansion of gᵢⱼ. Specifically, gᵢⱼ(x) = δᵢⱼ - ⅓Rᵢₖⱼₗ(p) xᵏxˡ + O(|x|³). This shows that the Riemann curvature tensor is the leading obstruction to flatness — the first correction to the Euclidean metric in a Taylor expansion. Normal coordinates simplify many local computations and make the geometric content of formulas transparent.
