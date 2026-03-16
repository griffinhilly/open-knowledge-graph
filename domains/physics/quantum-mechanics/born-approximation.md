---
id: born-approximation
title: The Born Approximation in Scattering
domain: physics
course: quantum-mechanics
prerequisites:
- id: scattering-theory-intro
  type: hard
- id: time-independent-perturbation-theory
  type: soft
tags:
- born-approximation
- scattering
stage: formal-systems
status: draft
---

# The Born Approximation in Scattering

## Core Idea
Born approximation: f(θ) ≈ −(m/2πℏ²) ∫ e^{iq·r'} V(r') d³r' with momentum transfer q. Valid for weak scattering or high energy. Predicts Rutherford scattering.

## Explainer

From your study of scattering theory, you know that the key quantity is the scattering amplitude f(θ,φ) — the complex function whose squared magnitude gives the differential cross section. The challenge is that computing f exactly requires solving the full Schrödinger equation with the scattering boundary conditions, which is analytically tractable only for a handful of potentials. The **Born approximation** provides an elegant first-principles shortcut: treat the potential V(r) as a weak perturbation and compute the scattered wave to first order in V.

The physical picture is transparent. The incoming particle travels as a plane wave e^{ik·r} and barely deviates. At each point r′ in the potential, the interaction "re-radiates" a small spherical wave weighted by the local potential strength V(r′). The scattered amplitude at angle θ is the coherent sum — the integral — of all these re-radiated waves, each carrying a phase factor e^{iq·r′} that accounts for the path-length difference between the incoming and outgoing waves. The vector **q = k_f − k_i** is the **momentum transfer**, with magnitude q = 2k sin(θ/2) for elastic scattering. The resulting formula, f(θ) ≈ −(m/2πℏ²) ∫ e^{iq·r′} V(r′) d³r′, shows that the scattering amplitude is proportional to the **Fourier transform of the potential** evaluated at the momentum transfer q.

This Fourier-transform structure has deep physical content. A slowly-varying, long-range potential (like the Coulomb potential) has a large Fourier transform at small q — meaning it scatters predominantly at small angles. A sharply peaked, short-range potential has significant Fourier components at large q — scattering out to large angles. This is the quantum analog of optical diffraction: the far-field diffraction pattern of an aperture is the Fourier transform of its transmission function. In both cases, the scatterer and the scattering pattern are related by a Fourier transform. The connection to time-independent perturbation theory is also direct: the Born approximation is equivalent to first-order perturbation theory applied to scattering states.

The Born approximation is valid when the potential is weak compared to the particle's kinetic energy — either because |V| is intrinsically small, or because the incident energy ℏ²k²/2m is large. For the Coulomb potential V(r) = Ze²/r, the Fourier transform gives f(θ) ∝ 1/sin²(θ/2), producing the **Rutherford cross section** dσ/dΩ ∝ 1/sin⁴(θ/2). Remarkably, this is the same result Rutherford derived classically, and it was one of the first triumphs of quantum scattering theory. The approximation fails at low energies or for strong potentials, where higher-order terms (multiple scattering events) become significant, but it remains the essential first tool for connecting potential shapes to scattering patterns.
