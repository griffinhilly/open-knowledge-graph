---
id: curved-spacetime-metric-tensor
title: Curved Spacetime and the Metric Tensor
domain: physics
course: general-relativity
prerequisites:
- id: equivalence-principle
  type: hard
- id: special-relativity
  type: hard
- id: riemannian-metrics
  type: hard
- id: spacetime-diagrams-minkowski
  type: soft
tags:
- metric-tensor
- spacetime
- line-element
- lorentzian-geometry
- interval
stage: expert
status: validated
---

# Curved Spacetime and the Metric Tensor

## Core Idea
In general relativity, spacetime is a four-dimensional pseudo-Riemannian manifold whose geometry is encoded in the metric tensor g_μν. The metric generalizes the flat Minkowski metric η_μν of special relativity to allow curvature: the infinitesimal spacetime interval ds² = g_μν dx^μ dx^ν determines proper time along timelike paths, proper distance along spacelike separations, and the causal structure (timelike, null, spacelike) at every event. The metric is the fundamental dynamical variable of GR — it is determined by the distribution of matter and energy through Einstein's field equations, and it in turn dictates how matter and light move through spacetime.

## Questions

```yaml
- question: "In flat Minkowski spacetime the interval is ds² = -c²dt² + dx² + dy² + dz². In a curved spacetime, which of the following correctly describes how this changes?"
  type: multiple-choice
  options:
    - "The signs of the temporal and spatial terms swap, so ds² = c²dt² - dx² - dy² - dz²"
    - "The constant coefficients (-c², +1, +1, +1) are replaced by functions g_μν(x) that vary from point to point and may include off-diagonal cross terms"
    - "Additional spatial dimensions are added, extending the interval to five or more terms"
    - "The speed of light c is replaced by a position-dependent function c(x) while the metric remains diagonal"
  answer: 1
  explanation: "The metric tensor g_μν generalizes the Minkowski metric by replacing constant coefficients with position-dependent functions and allowing off-diagonal terms (cross terms like g_{tr} dr dt). This is what encodes curvature. The signature (-,+,+,+) is preserved, the dimensionality remains four, and c remains a universal constant — its apparent variation in some coordinate systems (like Schwarzschild coordinates) is a coordinate artifact, not a physical change."

- question: "The metric tensor in general relativity plays the same role as the gravitational potential in Newtonian gravity."
  type: true-false
  answer: true
  explanation: "In the Newtonian limit, the g_{00} component of the metric reduces to approximately -(1 + 2Φ/c²), where Φ is the Newtonian gravitational potential. More broadly, the metric tensor encodes all gravitational information: it determines how clocks tick, how rulers measure, how objects fall, and how light propagates. Just as Φ is the single function that specifies Newtonian gravity, g_μν (with its ten independent components in four dimensions) specifies the full gravitational field in GR."

- question: "Why does the metric tensor have ten independent components in four-dimensional spacetime rather than sixteen?"
  type: short-answer
  answer: "The metric tensor is symmetric: g_μν = g_νμ. In four dimensions, a general 4×4 matrix has 16 components, but symmetry means g_μν = g_νμ for all μ,ν, reducing the independent components to 4×5/2 = 10. This symmetry follows from the definition of the metric as the inner product on the tangent space, which is inherently symmetric: ds² = g_μν dx^μ dx^ν = g_νμ dx^ν dx^μ."
  explanation: "The ten independent components of g_μν are the dynamical degrees of freedom of the gravitational field, though not all ten are physical — four can be removed by coordinate (gauge) freedom, and four more are constrained by the Bianchi identities, leaving two true propagating degrees of freedom (the two polarizations of gravitational waves)."

- question: "Explain the physical distinction between a timelike interval (ds² < 0), a spacelike interval (ds² > 0), and a null interval (ds² = 0) in the (-,+,+,+) signature convention."
  type: short-answer
  answer: "A timelike interval (ds² < 0) connects two events that can be visited by a massive particle traveling slower than light; the square root of -ds²/c² gives the proper time elapsed on a clock following that path. A spacelike interval (ds² > 0) separates events that cannot be causally connected — no signal can travel between them. A null interval (ds² = 0) is the path followed by light (or any massless particle) — the proper time along a null path is zero. The metric's signature ensures that at every event in spacetime, the light cone separating these three regions is well-defined."
  explanation: "The causal classification of intervals is one of the metric's most fundamental roles. It defines the light cone structure, which in turn determines causality: causes must precede effects along timelike or null paths. Curvature changes the shapes of light cones from point to point but never changes the local causal structure."
```

## Explainer

In special relativity, spacetime is flat and described by the Minkowski metric η_μν = diag(-1, +1, +1, +1) (in units where c = 1). The interval ds² = η_μν dx^μ dx^ν = -dt² + dx² + dy² + dz² is the same for all inertial observers — it is the invariant quantity that encodes both the geometry and the causal structure of flat spacetime. Timelike intervals measure proper time; null intervals trace the paths of light; spacelike intervals measure proper distance between simultaneous events.

General relativity promotes this to curved spacetime. The Minkowski metric is replaced by a general symmetric tensor field g_μν(x) that varies from point to point: ds² = g_μν(x) dx^μ dx^ν. The metric now has ten independent components (owing to symmetry g_μν = g_νμ), and they are functions of the spacetime coordinates. In the presence of matter and energy, the geometry is no longer flat — the metric components encode gravitational effects. Near a massive body, g_00 deviates from -1 in a way that produces gravitational time dilation; the spatial components deviate from the flat values in ways that curve spatial geometry. The Schwarzschild metric, for example, describes the spacetime outside a spherically symmetric mass and is fully specified by the ten functions g_μν evaluated in a particular coordinate system.

The metric does far more than measure distances. It defines the inner product on the tangent space at each point, which in turn defines angles, orthogonality, and volume elements. It determines the connection (Christoffel symbols), which specifies how vectors are parallel-transported and how geodesics curve. It determines the curvature tensors (Riemann, Ricci, scalar), which encode tidal forces. And it determines the causal structure: the light cones tilt and deform as g_μν varies, dictating which events can influence which others. All of gravitational physics is contained in g_μν.

A crucial property of the metric is its signature. In four-dimensional spacetime, the metric has one negative and three positive eigenvalues (or the reverse, depending on convention) everywhere — this (-,+,+,+) or (+,-,-,-) signature is what makes the geometry pseudo-Riemannian rather than Riemannian. The negative sign is what creates the distinction between time and space, and it is what produces light cones. Without it, there would be no causal structure and no distinction between past and future. Physically, the signature is inherited from special relativity: in any sufficiently small region, the equivalence principle guarantees that coordinates can be chosen so that g_μν reduces to η_μν, confirming the Lorentzian signature.

Finally, the metric is the dynamical variable of general relativity in the same sense that the electromagnetic four-potential A_μ is the dynamical variable of electrodynamics. Einstein's field equations G_μν = 8πG T_μν are second-order partial differential equations for g_μν, with the stress-energy tensor T_μν as the source. Solving for the metric given a matter distribution is the central computational task of GR. The ten components of g_μν minus four coordinate degrees of freedom and four constraint equations from the Bianchi identities leave two physical degrees of freedom — precisely the two polarizations of gravitational waves, the dynamical excitations of spacetime geometry itself.
