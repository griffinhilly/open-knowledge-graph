---
id: electric-dipole-radiation
title: Electric Dipole Radiation and Radiation Patterns
domain: physics
course: electrodynamics
prerequisites:
- id: multipole-expansion-radiation
  type: hard
- id: larmor-formula
  type: soft
builds-toward:
- radiation-reaction-force
tags:
- dipole-radiation
- antenna
- patterns
stage: abstract-reasoning
status: draft
---

# Electric Dipole Radiation and Radiation Patterns

## Core Idea
Electric dipole radiation from time-varying dipole moment p(t) dominates for non-relativistic sources. Radiated power and angular distribution depend on dipole acceleration magnitude and direction. Maximum radiation perpendicular to acceleration; zero along it. Dipole antennas exploit this pattern.

## Explainer

In your study of multipole expansions and the Larmor formula, you found that accelerating charges radiate electromagnetic energy, and that the leading-order term in the multipole expansion of the radiation field comes from the **electric dipole moment** p⃗(t) of the source. For any localized charge distribution oscillating at frequency ω with size much smaller than the radiation wavelength (the non-relativistic, long-wavelength limit), the dipole term dominates all higher multipole contributions by factors of (kd) ≪ 1, where d is the source size. This is why dipole radiation is the first and most important radiation mechanism to master.

The **electric dipole moment** p⃗ = Σ qᵢrᵢ captures the overall charge separation in the source. For a sinusoidally oscillating dipole p(t) = p₀ cos(ωt), the second time derivative p̈ = −ω²p₀ cos(ωt) enters the radiation fields. The radiated power follows from the Larmor formula generalized to dipoles: P = p̈²/(6πε₀c³) (in SI). The key insight is that **it is the acceleration of the dipole moment, not just its existence, that produces radiation**. A static dipole radiates nothing; a uniformly moving dipole radiates nothing; only a changing p̈ (equivalently, changing current distribution) produces radiation.

The **angular radiation pattern** is one of the most beautiful results in classical electrodynamics. The power radiated per unit solid angle varies as dP/dΩ ∝ sin²θ, where θ is the angle measured from the direction of p̈. This means: maximum radiation is emitted perpendicular to the oscillation direction (θ = 90°, a band around the "equator" of the dipole), and zero radiation is emitted along the dipole axis (θ = 0°, the "poles"). Visualize a toroidal or donut-shaped pattern, with the hole aligned along the dipole. The radiation is also polarized: the electric field in the far zone lies in the plane containing the observation direction and the dipole axis.

This pattern directly explains antenna design. A **half-wave dipole antenna** is a conducting rod driven to oscillate current back and forth along its length. The pattern broadcasts strongest broadside (perpendicular to the rod) and nothing off the ends — exactly the sin²θ shape. Engineers orient antennas accordingly. The same physics governs how atoms radiate light: an excited atom's oscillating electron distribution can be approximated as an oscillating dipole, and dipole selection rules (which transitions are allowed) govern which spectral lines appear bright. The sin²θ pattern, the ω⁴ power dependence on frequency, and the dominance of perpendicular emission are features you will encounter repeatedly in radiation physics, optics, and antenna engineering.
