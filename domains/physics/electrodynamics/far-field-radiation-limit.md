---
id: far-field-radiation-limit
title: Far-Field Limit and Radiation Zone
domain: physics
course: electrodynamics
prerequisites:
- id: retarded-potentials
  type: hard
- id: radiation-from-accelerated-charges
  type: hard
builds-toward:
- radiation-directivity-and-pattern
- radiation-angular-distribution-em
tags:
- far-field
- radiation-zone
- multipole-expansion
stage: advanced
status: draft
---

# Far-Field Limit and Radiation Zone

## Core Idea
In the radiation zone (kr >> 1), retarded potentials simplify to pure radiation fields with E ∝ ∇ × a_ret and B = (k̂ × E)/c. The electric field near a small source becomes (1/4πε₀c²r)[k̂ × (k̂ × p̈)], proportional to acceleration, decaying as 1/r.

## Explainer

From your work with **retarded potentials**, you know that the fields of a moving charge are not instantaneous: they reflect the charge's position and velocity at the retarded time t_ret = t − r/c, the moment when the "news" of the charge's motion was emitted. The full fields of an accelerating charge (the Liénard-Wiechert fields) contain two terms: one that decays as 1/r² and one that decays as 1/r. At close range, the 1/r² term dominates and looks like a modified Coulomb field that is dragged along with the charge. At large distances, the 1/r² term becomes negligible and only the 1/r term survives.

This 1/r term is the **radiation field**, and its survival at large distances is what makes radiation important. Energy flux (the Poynting vector S = E × B / μ₀) scales as E² ∝ 1/r². Multiply by the surface area of a sphere (4πr²), and the total power flowing outward through any sphere is independent of r — radiation carries energy to infinity. The 1/r² Coulomb-like term contributes a Poynting vector that falls as 1/r⁴, so the power through a sphere goes as 1/r² and vanishes at infinity. Only the 1/r radiation field represents genuine energy loss from the source.

In the **radiation zone** (r >> λ, equivalently kr >> 1), you can simplify the retarded potential calculation drastically. For a small source (size a << λ), the radiation field from an oscillating dipole moment p(t) takes the clean form E = (1/4πε₀c²r)[k̂ × (k̂ × p̈)], where k̂ is the unit vector pointing from source to field point and p̈ is the second time derivative of the dipole moment (the acceleration of the charge distribution). The double cross product k̂ × (k̂ × p̈) extracts the component of p̈ transverse to the direction of observation — fields in the radiation zone are always **transverse waves**, with E and B perpendicular to k̂ and to each other, with |B| = |E|/c.

The 1/r dependence and transverse polarization together define what it means for radiation to be "far field." In addition to distance, far field also means that you are far compared to the source size, so all parts of the source contribute nearly the same retardation delay. This approximation — retaining only the dominant 1/r term — is what makes antenna theory and radiation pattern analysis tractable. The angular distribution of power (dP/dΩ ∝ sin²θ for a linear dipole oscillating along ẑ) reveals the **radiation pattern**: maximum emission perpendicular to the oscillation axis, zero emission along it. These patterns, derived from the far-field limit, are exactly what antenna engineers optimize when designing directional transmitters.
