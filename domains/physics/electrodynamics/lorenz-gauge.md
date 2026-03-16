---
id: lorenz-gauge
title: Lorenz Gauge
domain: physics
course: electrodynamics
prerequisites:
- id: gauge-transformations
  type: hard
- id: scalar-vector-potentials
  type: hard
builds-toward:
- retarded-potentials
- electromagnetic-field-tensor
tags:
- lorenz-gauge
- covariant
- relativistic
stage: advanced
status: draft
---

# Lorenz Gauge

## Core Idea
The Lorenz gauge (∂φ/∂t + c²∇·A = 0) is manifestly covariant under Lorentz transformations, treating the scalar and vector potentials symmetrically. Both φ and A satisfy decoupled wave equations in this gauge, making it ideal for relativistic problems and for quantizing the electromagnetic field. The gauge condition elegantly encodes causality and charge conservation.

## Explainer

From gauge transformations, you know that the physically observable fields E and B are unchanged when you shift the scalar potential φ → φ − ∂χ/∂t and the vector potential A → A + ∇χ for any smooth function χ. This freedom means there are infinitely many (φ, A) pairs that describe the same physical fields — the gauge is unspecified until you impose a constraint. Different choices of gauge constraint are mathematically equivalent in terms of physics, but certain choices drastically simplify the equations for certain problems. The **Lorenz gauge** is the choice that makes the potentials satisfy the most elegant wave equations.

The Lorenz condition is ∇·A + (1/c²)∂φ/∂t = 0. (Note: this gauge is named after Ludvig Lorenz, the Danish physicist, not Hendrik Lorentz of the Lorentz transformation — a historically persistent confusion.) What makes this condition special is its **Lorentz covariance**: in four-vector notation, the Lorenz condition is simply ∂_μ A^μ = 0, the four-divergence of the four-potential vanishes. This is a single covariant equation, symmetric in space and time, that transforms properly under Lorentz boosts. Both φ/c and A together form a four-vector A^μ = (φ/c, **A**), and the Lorenz condition treats all four components on equal footing.

When you substitute the Lorenz gauge condition into Maxwell's equations, the scalar and vector potentials **decouple**. Each satisfies its own wave equation driven by the appropriate source: □²φ = −ρ/ε₀ and □²**A** = −μ₀**J**, where □² = ∂²/∂t² /c² − ∇² is the d'Alembertian wave operator. This is a massive simplification — in other gauges (such as the Coulomb gauge ∇·**A** = 0), the equations for φ and **A** are coupled together and φ satisfies an instantaneous Poisson equation that appears to violate relativity (the instantaneous action is an artifact, not a real signal). In the Lorenz gauge, both equations are manifestly wave equations that propagate at c, encoding causality directly into the structure of the equations.

The solutions to these wave equations are the **retarded potentials** — φ and **A** at a field point at time t depend on sources at the retarded time t − r/c, where r is the distance from source to field point. The signal travels at the speed of light; cause precedes effect by exactly the light-travel time. This retardation is where the Lorenz gauge's encoding of causality becomes visible. In the Coulomb gauge, the same physical causality is present but hidden — the instantaneous φ is canceled by compensating terms in **A** to give retarded E and B. The Lorenz gauge makes the causal structure transparent, which is why it is the natural starting point for quantizing the electromagnetic field in quantum electrodynamics.
