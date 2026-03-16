---
id: electromagnetic-wave-polarization
title: Polarization of Electromagnetic Waves
domain: physics
course: electrodynamics
prerequisites:
- id: plane-electromagnetic-waves
  type: hard
builds-toward:
- electromagnetic-waves-in-dielectrics
tags:
- polarization
- wave-properties
- em-waves
stage: advanced
status: draft
---

# Polarization of Electromagnetic Waves

## Core Idea
The polarization of an electromagnetic wave describes how the electric field vector varies in direction as the wave propagates. Waves can be linearly polarized (E oscillates along a fixed direction), circularly polarized (E traces a helix), or elliptically polarized. Polarization is determined by the superposition of orthogonal field components and is crucial for understanding light-matter interactions and optical devices.

## Explainer

From your study of plane electromagnetic waves, you know that E⃗ and B⃗ are perpendicular to each other and to the direction of propagation. If the wave travels in the z-direction, E⃗ must lie in the xy-plane. But within that plane, E⃗ can point in any direction — and **polarization** describes exactly how that direction varies as the wave propagates or as time passes. It is a degree of freedom that has no analog in, say, sound waves (which are longitudinal), and it turns out to be physically consequential for reflection, absorption, and how light interacts with anisotropic materials.

The simplest case is **linear polarization**: the electric field oscillates back and forth along a single fixed direction in the xy-plane. For example, E⃗(z,t) = E₀ cos(kz - ωt) x̂. The field is always along x̂, just oscillating in magnitude. Sunlight reflected at a shallow angle off water or glass tends to be predominantly horizontally polarized, which is why polarized sunglasses (which block horizontal polarization) reduce glare. A linear polarizer transmits only the component of E along its transmission axis, so the transmitted intensity follows Malus's law: I = I₀ cos²θ, where θ is the angle between the incoming polarization and the polarizer axis.

Now consider superimposing two orthogonal linearly polarized waves with equal amplitude but a phase difference of 90°: E⃗ = E₀ cos(kz - ωt) x̂ + E₀ sin(kz - ωt) ŷ. At any fixed z, the tip of E⃗ traces a circle as time progresses — this is **circular polarization**. Left and right circular polarization differ only in the sign of the phase difference (±90°). If the two amplitudes are unequal, or if the phase difference is anything other than 90°, the tip traces an ellipse: **elliptical polarization** is the general case, with linear and circular polarization as special limits. This decomposition — any polarization state as a superposition of two orthogonal components — is fundamental, and it has a direct quantum-mechanical analog in photon spin states.

**Unpolarized light**, such as that from the sun or an incandescent bulb, has E⃗ oriented randomly and rapidly in all directions within the plane perpendicular to propagation — the polarization state changes on a timescale faster than any detector can resolve. A single polarizer transmits half of unpolarized light (on average) and fully polarizes it. Two crossed polarizers (with transmission axes at 90°) transmit essentially nothing — but inserting a third polarizer at 45° between them allows some light through again, because each polarizer projects onto its axis and rotates the polarization state. Polarization is not just an abstract property; it underlies LCD screens, optical fiber communication, spectroscopy of chiral molecules, and the operation of wave plates and beam splitters.
