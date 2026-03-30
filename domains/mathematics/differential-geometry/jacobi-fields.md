---
id: jacobi-fields
title: Jacobi Fields
domain: mathematics
course: differential-geometry
prerequisites:
  - id: geodesics
    type: hard
  - id: curvature-tensor
    type: hard
  - id: exponential-map
    type: soft
tags:
  - jacobi-fields
  - geodesic-deviation
  - conjugate-points
  - second-variation
stage: expert
status: validated
---

# Jacobi Fields

## Core Idea
A Jacobi field is a vector field along a geodesic that describes how nearby geodesics deviate from it — it satisfies the Jacobi equation J'' + R(J, γ')γ' = 0, a second-order linear ODE where the curvature tensor acts as a "spring constant." Positive curvature causes geodesics to converge (Jacobi fields oscillate), negative curvature causes divergence (Jacobi fields grow exponentially), and zero curvature gives linear behavior. Conjugate points — where Jacobi fields vanish — mark where geodesics refocus and lose minimality.

## Questions

```yaml
- question: "On a sphere of radius 1 (constant curvature K = 1), the Jacobi equation along a geodesic becomes J'' + J = 0. The solutions are J(t) = A sin(t) + B cos(t). This means Jacobi fields vanish (have conjugate points) at t = π. What does this imply geometrically?"
  type: multiple-choice
  options:
    - "Geodesics on the sphere are undefined past t = π"
    - "All geodesics from a point refocus at the antipodal point (distance π), and geodesics beyond that distance are no longer minimizing"
    - "The curvature changes sign at t = π"
    - "The exponential map becomes complex-valued at t = π"
  answer: 1
  explanation: "The Jacobi field J(t) = sin(t) vanishes at t = 0 and t = π. Geometrically, this means a one-parameter family of geodesics from a point p (say, lines of longitude from the north pole) all meet again at the antipodal point (south pole), which is the conjugate point at distance π. Beyond the conjugate point, the geodesic is no longer minimizing — there are shorter paths going 'the other way.' This is why great-circle arcs longer than half the circumference are not shortest paths."

- question: "In a Riemannian manifold with non-positive sectional curvature (K ≤ 0), there are no conjugate points along any geodesic."
  type: true-false
  answer: true
  explanation: "The Jacobi equation J'' + R(J,γ')γ' = 0 has the curvature acting as a 'restoring force.' When K ≤ 0, the force pushes Jacobi fields AWAY from zero (the term R(J,γ')γ' has the 'wrong sign' for oscillation). A Jacobi field that starts at zero grows monotonically and never returns to zero — so there are no conjugate points. By the Cartan-Hadamard theorem, this implies the exponential map is a covering map, and the universal cover of M is diffeomorphic to ℝⁿ."

- question: "Why are Jacobi fields important for understanding the second variation of arc length?"
  type: short-answer
  answer: "The second variation of the energy/length functional of a geodesic involves the Jacobi operator (the linear differential operator J ↦ J'' + R(J,γ')γ'). A geodesic is a local minimum of length if and only if the second variation is non-negative, which happens if and only if there are no conjugate points along the geodesic. Jacobi fields that vanish at both endpoints (conjugate points) are the 'zero modes' of the second variation — they represent directions in which the geodesic can be varied without changing the length to first order but where the second-order change is zero or negative."
  explanation: "This is the Riemannian analogue of the second-derivative test in calculus. A geodesic is a critical point of the length functional (first variation = 0). The Jacobi fields determine whether it is a local minimum (no conjugate points), saddle point (conjugate points exist), or degenerate critical point. The Morse index theorem counts the number of conjugate points (with multiplicity) along a geodesic segment, which equals the number of negative eigenvalues of the second variation."
```

## Explainer

Consider a one-parameter family of geodesics γ_s(t) emanating from a point p. The **variation field** J(t) = ∂γ_s/∂s|_{s=0} measures how fast the geodesics spread apart at time t. Differentiating the geodesic equation ∇_{γ'_s} γ'_s = 0 with respect to s and using the definition of the curvature tensor yields the **Jacobi equation**: ∇²_{γ'} J + R(J, γ')γ' = 0, often written J'' + R(J, γ')γ' = 0. This is a second-order linear ODE along the geodesic, with the curvature tensor playing the role of a position-dependent "spring constant."

The character of solutions depends on curvature. On a space of **positive curvature** (like a sphere), the Jacobi equation is like a harmonic oscillator: J'' + KJ = 0 with K > 0 has sinusoidal solutions sin(√K t), meaning Jacobi fields oscillate and periodically return to zero. Geometrically, geodesics converge, refocusing at **conjugate points**. On a space of **negative curvature** (like hyperbolic space), the equation is J'' - |K|J = 0, with exponentially growing solutions sinh(√|K| t). Geodesics diverge exponentially, and there are no conjugate points. On **flat space**, J'' = 0 gives linear solutions J = at + b — geodesics separate at constant rate.

**Conjugate points** are points where a nonzero Jacobi field (vanishing at the initial point) vanishes again. They mark where the exponential map fails to be a local diffeomorphism, where geodesics lose their minimizing property, and where the second variation of arc length has a zero eigenvalue. The **Morse index** of a geodesic segment counts conjugate points with multiplicity — it equals the number of independent directions in which the geodesic can be shortened by a small variation.

The **Rauch comparison theorem** is the quantitative version: if the sectional curvature of M is bounded above/below by a constant κ, then Jacobi fields on M are bounded below/above by Jacobi fields on the model space of constant curvature κ. This translates curvature bounds into metric bounds: distances between geodesics on M are controlled by the corresponding distances in the model space. Rauch comparison is the engine behind most of the global theorems in Riemannian geometry — the sphere theorem, the Bonnet-Myers theorem, the volume comparison theorem, and the Toponogov theorem all follow from Jacobi field estimates.
