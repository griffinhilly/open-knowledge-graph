---
id: gauss-bonnet-theorem
title: Gauss-Bonnet Theorem
domain: mathematics
course: differential-geometry
prerequisites:
  - id: curvature-tensor
    type: hard
  - id: integration-on-manifolds
    type: hard
  - id: orientation
    type: hard
  - id: stokes-theorem-on-manifolds
    type: soft
tags:
  - gauss-bonnet
  - euler-characteristic
  - total-curvature
  - topology-geometry-bridge
stage: expert
status: validated
---

# Gauss-Bonnet Theorem

## Core Idea
The Gauss-Bonnet theorem states that the total Gaussian curvature of a compact oriented surface equals 2π times its Euler characteristic: ∫_S K dA = 2πχ(S). This is the first and most beautiful theorem connecting local geometry (curvature) to global topology (Euler characteristic). It implies that the total curvature is a topological invariant — unchanged by any deformation of the metric — and generalizes to higher dimensions via the Chern-Gauss-Bonnet theorem.

## Questions

```yaml
- question: "A closed orientable surface S has Euler characteristic χ(S) = 2 - 2g, where g is the genus (number of handles). By Gauss-Bonnet, ∫_S K dA = 2π(2 - 2g). For the torus (g = 1), this gives..."
  type: multiple-choice
  options:
    - "∫ K dA = 4π, so the torus must have everywhere positive curvature"
    - "∫ K dA = 0, so any metric on the torus must have regions of both positive and negative curvature (unless K = 0 everywhere)"
    - "∫ K dA = -4π, so the torus must have everywhere negative curvature"
    - "∫ K dA = 2π, so the torus has exactly half the total curvature of a sphere"
  answer: 1
  explanation: "For g = 1: ∫ K dA = 2π(2-2) = 0. The total curvature vanishes. If K is not identically zero, it must be positive somewhere and negative somewhere (by the intermediate value theorem on a connected manifold, if K is continuous and integrates to zero but is not identically zero, it must change sign). The flat torus (K = 0 everywhere) is the special case where the curvature vanishes pointwise. The embedded torus in ℝ³ (doughnut shape) has positive curvature on the outside and negative curvature on the inside, integrating to zero."

- question: "The Gauss-Bonnet theorem implies that the total curvature ∫_S K dA is unchanged if you smoothly deform the metric on S."
  type: true-false
  answer: true
  explanation: "The Euler characteristic χ(S) is a topological invariant — it depends only on the homeomorphism type of S, not on the metric. Since ∫_S K dA = 2πχ(S), the total curvature is also a topological invariant. You can bend, stretch, and deform the surface in any smooth way, and the integral of curvature will not change. This is remarkable because K and dA separately depend on the metric — only their product integrates to a topological constant."

- question: "Apply the Gauss-Bonnet theorem to the sphere S² with any Riemannian metric. What can you conclude about the Gaussian curvature?"
  type: short-answer
  answer: "The sphere has χ(S²) = 2, so ∫_{S²} K dA = 4π for any metric on S². This means the total Gaussian curvature is always 4π, regardless of how you deform the sphere. In particular, K must be positive somewhere — a sphere cannot carry a metric with everywhere non-positive curvature. For the round sphere of radius r, K = 1/r² and Area = 4πr², giving ∫ K dA = (1/r²)(4πr²) = 4π, confirming the theorem."
  explanation: "More generally, Gauss-Bonnet constrains which curvature conditions are compatible with a given topology. A surface of genus g ≥ 2 has χ < 0, so it must have negative curvature somewhere (and cannot have a metric of everywhere non-negative curvature). These topological obstructions to curvature conditions are a central theme in Riemannian geometry."

- question: "The Gauss-Bonnet theorem has a version for surfaces with boundary: ∫_S K dA + ∫_{∂S} κg ds = 2πχ(S), where κg is the geodesic curvature of the boundary."
  type: true-false
  answer: true
  explanation: "When the surface has boundary, the boundary's geodesic curvature contributes a correction term. For a geodesic triangle (boundary consists of three geodesic segments, κg = 0 on each), the formula gives ∫_T K dA + (sum of exterior angles) = 2π, which is equivalent to the angle excess formula: (sum of interior angles) - π = ∫_T K dA. On a sphere, the angles of a geodesic triangle sum to more than π, with the excess equal to the enclosed area times the curvature."
```

## Explainer

The Gauss-Bonnet theorem is the prototypical result in differential geometry — the first theorem to bridge local curvature and global topology. On a compact oriented surface S without boundary, it states: **∫_S K dA = 2πχ(S)**, where K is the Gaussian curvature, dA is the area element, and χ(S) is the Euler characteristic. For closed orientable surfaces, χ = 2 - 2g where g is the genus, so the total curvature is 2π(2 - 2g): it equals 4π for a sphere, 0 for a torus, -4π for a genus-2 surface, and so on.

The theorem has immediate consequences. No metric on a torus can have everywhere positive Gaussian curvature (the total curvature must be zero). No metric on a sphere can have everywhere non-positive curvature (the total must be 4π). A surface of genus ≥ 2 must have negative curvature somewhere. These are **topological obstructions** to curvature conditions — the topology of the surface constrains what curvature is possible. Conversely, the theorem implies that the total curvature is a topological invariant: you can deform the metric however you like (stretch, squish, bend), and ∫ K dA does not change.

The version with boundary adds a geodesic-curvature term: ∫_S K dA + ∫_{∂S} κg ds + Σ αᵢ = 2πχ(S), where κg is the geodesic curvature of the boundary and αᵢ are the exterior angles at corners. Applied to a geodesic triangle on a surface of constant curvature K, this gives (angle sum) = π + K·(area), the famous angle-excess formula. On a sphere (K > 0), angles sum to more than π; on a hyperbolic surface (K < 0), less than π. The amount of excess or deficit is proportional to the area, with proportionality constant K.

The **Chern-Gauss-Bonnet theorem** extends this to higher even dimensions: on a compact oriented 2n-manifold M, ∫_M Pf(Ω) = (2π)ⁿ χ(M), where Pf(Ω) is the Pfaffian of the curvature form. The integrand is a polynomial in the Riemann curvature tensor, and the integral equals the Euler characteristic. In dimension 4, the integrand involves the square of the curvature tensor, and the theorem constrains the topology of 4-manifolds from curvature data. The Gauss-Bonnet theorem is the genesis of the theory of **characteristic classes**, which are topological invariants of vector bundles computed from curvature — one of the deepest threads connecting differential geometry, algebraic topology, and mathematical physics.
