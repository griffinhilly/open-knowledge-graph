---
id: evanescent-waves-total-reflection
title: Evanescent Waves and Total Internal Reflection
domain: physics
course: electrodynamics
prerequisites:
- id: group-velocity-and-dispersion
  type: hard
- id: electromagnetic-waves-in-media
  type: hard
tags:
- evanescent-waves
- total-reflection
- surface-waves
- tunneling
stage: advanced
status: draft
---

# Evanescent Waves and Total Internal Reflection

## Core Idea
When the wave vector becomes imaginary (above the cutoff frequency for the medium), waves decay exponentially rather than propagate. At interfaces beyond the critical angle, evanescent waves extend into the second medium and can tunnel through thin barriers.

## Explainer

You know from studying electromagnetic waves in media that the wave vector k = n·ω/c, where n is the refractive index of the medium. The refractive index can depend on frequency (dispersion), and in some situations — below a plasma cutoff frequency, inside a waveguide below its cutoff, or beyond the critical angle at an interface — the requirement that k² = (n·ω/c)² forces k² to be negative. A negative k² means k itself is imaginary: k = iκ where κ is real and positive. Substituting this into the plane-wave factor e^(ikx) gives e^(−κx): not oscillation, but **exponential decay**. This is an **evanescent wave**.

The most vivid physical setting is **total internal reflection** (TIR). When a wave travels from a denser medium (refractive index n₁) to a rarer one (n₂ < n₁) and strikes the interface at an angle θᵢ greater than the critical angle θ_c = arcsin(n₂/n₁), Snell's law would require sin θₜ = (n₁/n₂)sin θᵢ > 1 — which has no real solution for the transmitted angle. The wave in medium 2 must still satisfy Maxwell's boundary conditions, but it does so with an evanescent field that decays exponentially away from the interface in the transverse direction while appearing to travel parallel to it. The time-averaged Poynting vector into medium 2 is zero — no net power is transmitted — yet the fields are not zero. They exist in a thin skin extending a wavelength or so beyond the interface.

This non-zero but non-propagating field makes TIR more subtle than it first appears, and it has a measurable consequence: **frustrated total internal reflection**. If you bring a second piece of glass close to the first (within a fraction of a wavelength), the evanescent field from the first glass can couple into the propagating modes of the second. Power flows across the gap even though there is no traveling wave in the air between them. This is the optical analogue of quantum-mechanical tunneling — a particle wave decays exponentially through a classically forbidden barrier but re-emerges as a propagating wave on the other side. The two phenomena obey mathematically identical equations.

Evanescent waves are not just a curiosity: they underpin **near-field optics**, allowing imaging beyond the diffraction limit by collecting the high-spatial-frequency evanescent components that a conventional lens discards. They also explain the operation of optical fiber couplers (where bending creates a geometry where the evanescent tail of one fiber overlaps the second) and attenuated total reflectance spectroscopy, where a sample placed near the reflecting surface absorbs from the evanescent field to reveal its absorption spectrum. Any time you see decaying rather than propagating fields — near an antenna below resonance, in a cutoff waveguide section, at a TIR interface — you are dealing with the same mathematics: imaginary wave vector, exponential envelope, zero net power transport.
