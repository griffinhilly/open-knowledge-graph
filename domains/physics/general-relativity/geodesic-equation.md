---
id: geodesic-equation
title: The Geodesic Equation
domain: physics
course: general-relativity
prerequisites:
- id: christoffel-symbols
  type: hard
- id: geodesics
  type: hard
- id: lagrangian-mechanics-intro
  type: soft
tags:
- geodesics
- free-fall
- proper-time
- equations-of-motion
- variational-principle
stage: expert
status: validated
---

# The Geodesic Equation

## Core Idea
The geodesic equation d²x^μ/dτ² + Γ^μ_{αβ}(dx^α/dτ)(dx^β/dτ) = 0 describes the motion of a freely falling particle in curved spacetime — the GR generalization of Newton's first law. Geodesics extremize the proper time between two events (for timelike paths) or equivalently extremize the spacetime interval. They are the straightest possible curves in a curved geometry: the four-velocity is parallel-transported along itself. For massive particles the affine parameter is proper time τ; for photons (null geodesics, ds² = 0) a different affine parameter is used. The geodesic equation encodes the complete gravitational dynamics of test particles without reference to forces — gravity is simply the curvature of the spacetime through which particles travel along their natural paths.

## Questions

```yaml
- question: "A massive particle in free fall follows a path that:"
  type: multiple-choice
  options:
    - "Minimizes the spatial distance traveled between two events"
    - "Maximizes the proper time elapsed between two events (among nearby paths)"
    - "Moves along a path of zero proper time"
    - "Follows a straight line in the coordinate system centered on the gravitating body"
  answer: 1
  explanation: "In Lorentzian geometry, timelike geodesics maximize proper time among nearby paths — this is the opposite of the Riemannian case where geodesics minimize distance. A freely falling clock between two events records more elapsed time than any nearby accelerated clock (the relativistic twin effect generalized to curved spacetime). Option C describes null geodesics (light). Option D is generally false in curved spacetime — geodesics appear curved in most coordinate systems."

- question: "In the Newtonian limit (weak gravitational field, slow motion), the geodesic equation reduces to Newton's second law for gravity: d²x^i/dt² = -∂Φ/∂x^i."
  type: true-false
  answer: true
  explanation: "In the weak-field (g_μν ≈ η_μν + h_μν with |h_μν| << 1), slow-motion (v << c) limit, the geodesic equation reduces to d²x^i/dτ² ≈ -(1/2)∂_i g_{00} c². With g_{00} ≈ -(1 + 2Φ/c²), this gives d²x^i/dt² ≈ -∂_i Φ, which is precisely Newton's gravitational acceleration. The Christoffel symbol Γ^i_{00} encodes the Newtonian gravitational force in this limit."

- question: "Why must null geodesics (the paths of light) use an affine parameter other than proper time?"
  type: short-answer
  answer: "Along a null geodesic, ds² = g_μν dx^μ dx^ν = 0 by definition, so the proper time dτ = √(-ds²/c²) is identically zero along the entire path. Proper time therefore cannot serve as a parameter to track progress along the curve. Instead, null geodesics are parameterized by an arbitrary affine parameter λ, defined by the requirement that the geodesic equation retains its standard form: d²x^μ/dλ² + Γ^μ_{αβ}(dx^α/dλ)(dx^β/dλ) = 0. Any reparameterization λ → aλ + b (affine transformation) preserves this form."
  explanation: "The affine parameter for null geodesics has no direct physical interpretation as elapsed time, but it is mathematically essential for writing the equation of motion. In practice, for light moving in a static spacetime, coordinate time t is often used as a convenient (though generally non-affine) parameter."

- question: "Derive the geodesic equation from a variational principle by extremizing the proper time functional τ = ∫√(-g_μν dx^μ dx^ν) along a timelike path."
  type: short-answer
  answer: "Treat the path x^μ(λ) as the dynamical variable and form the action S = ∫√(-g_μν (dx^μ/dλ)(dx^ν/dλ)) dλ. Applying the Euler-Lagrange equations to the integrand L = √(-g_μν ẋ^μ ẋ^ν) yields (d/dλ)(∂L/∂ẋ^μ) - ∂L/∂x^μ = 0. Choosing proper time τ as the parameter (so L = 1) simplifies the Euler-Lagrange equations to d²x^μ/dτ² + Γ^μ_{αβ}(dx^α/dτ)(dx^β/dτ) = 0, with the Christoffel symbols arising from the metric derivatives in the Euler-Lagrange equations. Alternatively, extremizing ∫g_μν ẋ^μ ẋ^ν dλ (which avoids the square root) gives the same geodesic equation directly."
  explanation: "The variational derivation connects geodesics to the Lagrangian mechanics framework. The 'trick' of extremizing the squared integrand instead of the square root is standard in practice — it produces the same geodesic paths (with affine parameterization automatically enforced) and is much easier to compute."
```

## Explainer

Newton's first law says that a free particle — one with no forces acting on it — moves in a straight line at constant speed. In curved spacetime, the concept of "straight line" must be generalized. A geodesic is the closest analog: it is the curve along which the tangent vector is parallel-transported along itself, meaning the direction of motion does not change relative to the local geometry. The geodesic equation d²x^μ/dτ² + Γ^μ_{αβ}(dx^α/dτ)(dx^β/dτ) = 0 makes this precise. The first term is the coordinate acceleration; the second term, involving the Christoffel symbols, corrects for the fact that coordinates themselves may be curved or non-inertial. A freely falling particle has zero covariant acceleration — its four-velocity is covariantly constant along its worldline.

The geodesic equation can be derived from a variational principle: among all timelike paths connecting two events, the geodesic is the one that extremizes the proper time ∫dτ. In Lorentzian geometry, this extremum is a maximum — the freely falling path between two events records more proper time than any nearby accelerated path. This is the general-relativistic version of the twin paradox: the twin who remains in free fall ages more than the twin who accelerates. The Euler-Lagrange equations applied to the proper-time action yield the geodesic equation, with the Christoffel symbols emerging naturally from the derivatives of the metric. In practice, it is often easier to extremize the squared interval ∫g_μν(dx^μ/dλ)(dx^ν/dλ) dλ, which avoids the square root and automatically enforces affine parameterization.

For null geodesics — the paths of massless particles like photons — the proper time along the path is identically zero (ds² = 0), so τ cannot serve as the curve parameter. Instead, an affine parameter λ is used, and the geodesic equation takes the identical form with τ replaced by λ. Null geodesics determine the causal structure of spacetime: they are the boundaries of light cones, and they define which events can communicate with which others. The bending of light by gravity, the formation of black hole shadows, and gravitational lensing are all consequences of null geodesics in curved spacetime.

In the Newtonian limit — weak gravitational field, speeds much less than c — the geodesic equation reduces to Newton's second law for gravity. The dominant Christoffel symbol Γ^i_{00} becomes proportional to the gradient of the Newtonian potential Φ, and the spatial geodesic equation becomes d²x^i/dt² = -∂Φ/∂x^i. Planetary orbits, the trajectory of a thrown ball, and the motion of satellites are all geodesics of the weakly curved spacetime around the Earth or Sun. The geodesic equation thus unifies free-fall motion across all regimes: from everyday gravity to the extreme curvature near black holes, from massive particles to massless photons.
