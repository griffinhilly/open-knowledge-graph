---
id: electric-field-continuous-distributions
title: Electric Field from Continuous Charge Distributions
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-field-point-charges
  type: hard
- id: integration-applications
  type: hard
builds-toward:
- gauss-law-integral-form
- electric-flux-and-divergence
tags:
- field
- integration
- distributions
stage: formal-systems
status: draft
---

# Electric Field from Continuous Charge Distributions

## Core Idea
For continuous charge distributions, divide the region into infinitesimal elements dq and integrate: E = ∫(k dq/r²) r̂. Charge density (linear λ, surface σ, or volume ρ) parameterizes the distribution.

## Explainer

You already know the electric field from a single point charge: E = kq/r² in the radial direction. Continuous distributions extend this with a single conceptual move — replace the point charge with a sum over infinitely many infinitesimal charges dq, and replace the sum with an integral. The formula E = ∫(k dq/r²) r̂ is Coulomb's law applied element by element, with r̂ pointing from each dq to the field point. Every technique you learned for evaluating point-charge superpositions carries over; integration just makes the sum continuous.

The first challenge is expressing dq in terms of geometry. You have three types of **charge density**: **linear charge density** λ (charge per unit length, units C/m) for wires and rods, so dq = λ dl; **surface charge density** σ (charge per unit area, C/m²) for sheets and shells, so dq = σ dA; and **volume charge density** ρ (charge per unit volume, C/m³) for solid objects, so dq = ρ dV. Choosing the right density and parameterizing the geometry is the setup step — the rest is calculus.

The second challenge is that E is a vector, so you must integrate its components separately. This is where symmetry becomes indispensable. For a uniformly charged rod on the x-axis, you set up dEx and dEy integrals. By symmetry arguments — or by direct calculation — components that point in opposite directions from symmetric pairs of elements cancel. For an infinite line charge, the perpendicular components cancel and only the radial component survives, giving E = 2kλ/r (equivalently, λ/(2πε₀r)). For an infinite sheet, a similar argument leaves only the component normal to the sheet. Before integrating, always ask: what components must cancel by symmetry? Setting those to zero upfront turns a multi-component integral into a one-component calculation.

The most important examples to work through are: (1) the uniformly charged rod of finite length, which teaches you how to set up the general geometry; (2) the infinite line charge, the result of taking that rod to infinite length; (3) the uniformly charged ring, where the on-axis field simplifies because perpendicular components cancel in azimuthal pairs; and (4) the uniformly charged disk, obtained by integrating the ring result over radius, which in the limit of infinite radius gives the infinite-sheet result E = σ/(2ε₀). Each is a building block for Gauss's law problems you will encounter next.
