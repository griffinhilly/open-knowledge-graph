---
id: em-waves-in-conductors
title: Electromagnetic Waves in Conductors and Skin Depth
domain: physics
course: electrodynamics
prerequisites:
- id: electromagnetic-waves-in-media
  type: hard
- id: differential-equations
  type: hard
builds-toward:
- waveguides-transmission-lines
tags:
- conductors
- skin-depth
- attenuation
stage: advanced
status: draft
---

# Electromagnetic Waves in Conductors and Skin Depth

## Core Idea
Electromagnetic waves in conductors exponentially attenuate with characteristic penetration depth (skin depth) δ = 1/√(πfμσ). High-frequency fields penetrate skin-depth; low frequencies penetrate deeper. Perfect conductors (σ → ∞) have δ → 0 and exclude fields. Essential for shielding and cavity resonators.

## Explainer

In a vacuum or insulating medium, electromagnetic waves travel indefinitely — there are no free charges to absorb energy. In a conductor, the situation is fundamentally different: the electric field of the wave drives free electrons, which accelerate, collide with the lattice, and convert field energy into heat. The wave is being drained as it penetrates. The result is exponential attenuation: the field amplitude decays as E ∝ e^(−z/δ), where z is the depth into the conductor and **δ** is the **skin depth**.

The skin depth formula δ = 1/√(πfμσ) encodes three physical dependencies. Higher **conductivity** σ means more free electrons to absorb the wave — so better conductors have smaller skin depths. Higher **frequency** f means the field reverses more rapidly, giving charges less time to respond and penetrate — so high-frequency fields are confined to an even thinner surface layer. Higher **permeability** μ concentrates the magnetic field effects near the surface, reducing penetration further. For copper at 60 Hz, δ ≈ 8.5 mm — the field barely reaches the center of a thick wire. At 1 GHz, δ ≈ 2 μm — essentially all current flows within a few microns of the surface.

This surface confinement has a name — the **skin effect** — and it has major engineering consequences. At high frequencies, only the outer skin of a wire carries current, so the effective resistance of the wire increases with frequency (smaller cross-section in use). Coaxial cables use a thin conducting shell rather than a solid rod because the interior is wasted at high frequencies. Shielding a sensitive circuit with a metal enclosure works because incoming high-frequency waves cannot penetrate more than a few skin depths into the metal; the field is absorbed in the metal itself rather than reaching the interior.

The ideal **perfect conductor** (σ → ∞) represents the limit δ → 0: the field does not penetrate at all, and surface currents flow in an infinitesimally thin layer to cancel any internal field. This perfect-conductor boundary condition — E_tangential = 0 and B_normal = 0 at the surface — is the idealization used in waveguide and cavity analysis. Real conductors behave this way to an excellent approximation when the skin depth is much smaller than all other relevant length scales, which is typically satisfied for good metals at microwave frequencies and above.
