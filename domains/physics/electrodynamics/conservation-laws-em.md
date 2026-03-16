---
id: conservation-laws-em
title: Conservation Laws in Electromagnetism
domain: physics
course: electrodynamics
prerequisites:
- id: maxwells-equations-differential-form
  type: hard
- id: multivariable-calculus
  type: hard
builds-toward:
- poynting-vector-and-energy-flux
tags:
- conservation
- charge
- energy-momentum
stage: abstract-reasoning
status: draft
---

# Conservation Laws in Electromagnetism

## Core Idea
The continuity equation ∂ρ/∂t + ∇·J = 0 expresses charge conservation. Energy conservation emerges from the Poynting theorem. Momentum conservation relates to the Maxwell stress tensor. These conservation laws are implicit in Maxwell's equations and reflect fundamental symmetries.

## Explainer

From your work with Maxwell's equations in differential form, you know that ∇·E = ρ/ε₀ and ∇×B = μ₀J + μ₀ε₀∂E/∂t. Taking the divergence of the Ampère-Maxwell equation and using ∇·(∇×B) = 0, you get 0 = μ₀∇·J + μ₀ε₀∂(∇·E)/∂t = μ₀(∇·J + ∂ρ/∂t). This gives the **continuity equation** ∂ρ/∂t + ∇·J = 0 — not a separate postulate, but a theorem derived directly from Maxwell's equations. Physically, it says charge cannot be created or destroyed locally: any decrease in charge density at a point must be accompanied by a current flowing outward. Integrating over a volume and applying the divergence theorem yields dQ_enclosed/dt = −∮J·dA: the rate of change of enclosed charge equals the net current flowing out through the boundary.

The energy account starts by asking how fast the fields do work on charges. The power delivered to currents is P = ∫J·E dV. Using Maxwell's equations to rewrite J·E, you can show P = −∂u/∂t − ∇·S, where u = ½(ε₀E² + B²/μ₀) is the **electromagnetic energy density** and S = (1/μ₀)(E × B) is the **Poynting vector**. This is the Poynting theorem: the power delivered to matter comes from decreasing field energy and convergence of the energy flux S. The Poynting vector points in the direction electromagnetic energy is flowing, with units of W/m². From your multivariable calculus, you recognize this as a continuity equation for energy: the divergence theorem converts ∇·S into surface integrals, giving a total energy accounting statement for any volume.

Electromagnetic momentum is less intuitive but equally real. The fields themselves carry momentum density g = μ₀ε₀S = S/c². The **Maxwell stress tensor** T_ij encodes the flux of this momentum and the electromagnetic forces transmitted across surfaces. The momentum conservation law ∂g/∂t = ∇·T − f (where f is the force density on charges) parallels the charge and energy conservation statements exactly. Together, these three conservation laws — charge, energy, and momentum — are not additional assumptions layered onto Maxwell's equations. They are consequences embedded in the structure of the equations themselves, reflecting the deep symmetries of electromagnetism first identified by Noether's theorem: charge conservation follows from global phase symmetry, energy from time-translation symmetry, and momentum from spatial-translation symmetry.
