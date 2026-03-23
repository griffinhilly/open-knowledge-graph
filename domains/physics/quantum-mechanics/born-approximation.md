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
stage: advanced
status: validated
---

# The Born Approximation in Scattering

## Core Idea
Born approximation: f(θ) ≈ −(m/2πℏ²) ∫ e^{iq·r'} V(r') d³r' with momentum transfer q. Valid for weak scattering or high energy. Predicts Rutherford scattering.

## Questions

```yaml
- question: "According to the Born approximation, if a scattering potential V(r) is sharply peaked and localized in a tiny region of space, what angular distribution of scattered particles is predicted?"
  type: multiple-choice
  options:
    - "Nearly all scattering occurs at small forward angles, because the potential is weak"
    - "No scattering occurs, because a very small potential has negligible effect"
    - "Scattering is relatively isotropic, because a sharply localized potential has significant Fourier components at large momentum transfer q"
    - "Scattering is concentrated at exactly 90°, by symmetry of the spherical potential"
  answer: 2
  explanation: "The Born approximation gives f(θ) ∝ ∫ e^{iq·r'} V(r') d³r' — the Fourier transform of V evaluated at momentum transfer q = k_f − k_i, with magnitude q = 2k sin(θ/2). A sharply localized potential (like a delta function) has a flat Fourier transform — all spatial frequencies (all q values) are equally present. Large q corresponds to large scattering angles, so a sharply peaked potential scatters in all directions roughly equally. Contrast this with the Coulomb potential, which is long-range and has a Fourier transform concentrated at small q, producing predominantly forward scattering."

- question: "The Born approximation formula f(θ) ≈ −(m/2πℏ²) ∫ e^{iq·r'} V(r') d³r' reveals a deep structural connection between scattering and another mathematical operation. What is it?"
  type: multiple-choice
  options:
    - "The scattering amplitude is the Laplace transform of the potential, evaluated at the imaginary frequency corresponding to energy"
    - "The scattering amplitude is proportional to the Fourier transform of the potential, evaluated at the momentum transfer vector q = k_f − k_i"
    - "The scattering amplitude is the convolution of the potential with the incoming plane wave"
    - "The scattering amplitude equals the matrix element of V in the energy eigenbasis"
  answer: 1
  explanation: "The integral ∫ e^{iq·r'} V(r') d³r' is exactly the three-dimensional Fourier transform of V(r) evaluated at wavevector q. This is the defining structure of the Born approximation and has deep physical content: the scattering pattern encodes the 'spatial frequency content' of the potential. Long-range potentials have Fourier transforms peaked at small q (small scattering angles); short-range potentials have significant components at large q (wide-angle scattering). The same Fourier connection appears in optical diffraction, where the far-field pattern is the Fourier transform of the aperture — scattering and diffraction are mathematically the same phenomenon."

- question: "The Born approximation is most accurate when the scattering potential is strong and the incident particle energy is low."
  type: true-false
  answer: false
  explanation: "The Born approximation is a first-order perturbation theory in the potential V: it treats the scattered wave as a small correction to the incident plane wave. This is valid when the perturbation is small — either because |V| is intrinsically weak relative to the kinetic energy, or because the incident energy ℏ²k²/2m is large (making the kinetic energy dominate over the potential). Strong potentials or low energies lead to multiple scattering events, where the particle bounces off the potential many times. These higher-order contributions are neglected in Born, causing the approximation to fail. The criterion is roughly |V_typical| ≪ ℏ²k²/2m."

- question: "For the Coulomb potential V(r) = Ze²/r, the Born approximation gives the same differential cross section as Rutherford's classical calculation."
  type: true-false
  answer: true
  explanation: "The Fourier transform of the Coulomb potential V(r) = Ze²/r is proportional to 1/q², and with q = 2k sin(θ/2), this gives the differential cross section dσ/dΩ ∝ 1/sin⁴(θ/2) — exactly Rutherford's formula. This agreement between a first-order quantum calculation and the classical result (for the exact same potential) is not accidental: for the pure Coulomb potential, all higher-order Born terms vanish due to the special properties of 1/r. The Rutherford formula's experimental success in 1911 was one of the first triumphs of quantum scattering theory — even though Rutherford derived it classically."

- question: "Why does the Born approximation have the mathematical form of a Fourier transform, and what physical insight does this provide about the relationship between a potential's spatial structure and its scattering pattern?"
  type: short-answer
  answer: "In the Born approximation, the incoming particle travels as a plane wave e^{ik_i·r} and barely deviates. At each point r' in the potential, the interaction re-radiates a small spherical wave weighted by V(r'). Each re-radiated contribution carries a phase factor e^{iq·r'} recording the path-length difference between the incoming wave and the outgoing wave in direction k_f, where q = k_f − k_i is the momentum transfer. The total scattered amplitude is the coherent sum of all these contributions — an integral of the form ∫ e^{iq·r'} V(r') d³r', which is exactly the Fourier transform of V evaluated at q. The physical insight: the scattering pattern is a 'Fourier portrait' of the potential. Long-range potentials have Fourier transforms concentrated at small q (scatter mainly forward); sharply localized potentials have flat Fourier transforms (scatter isotropically). This is the quantum analog of optical Fraunhofer diffraction."
```

## Explainer

From your study of scattering theory, you know that the key quantity is the scattering amplitude f(θ,φ) — the complex function whose squared magnitude gives the differential cross section. The challenge is that computing f exactly requires solving the full Schrödinger equation with the scattering boundary conditions, which is analytically tractable only for a handful of potentials. The **Born approximation** provides an elegant first-principles shortcut: treat the potential V(r) as a weak perturbation and compute the scattered wave to first order in V.

The physical picture is transparent. The incoming particle travels as a plane wave e^{ik·r} and barely deviates. At each point r′ in the potential, the interaction "re-radiates" a small spherical wave weighted by the local potential strength V(r′). The scattered amplitude at angle θ is the coherent sum — the integral — of all these re-radiated waves, each carrying a phase factor e^{iq·r′} that accounts for the path-length difference between the incoming and outgoing waves. The vector **q = k_f − k_i** is the **momentum transfer**, with magnitude q = 2k sin(θ/2) for elastic scattering. The resulting formula, f(θ) ≈ −(m/2πℏ²) ∫ e^{iq·r′} V(r′) d³r′, shows that the scattering amplitude is proportional to the **Fourier transform of the potential** evaluated at the momentum transfer q.

This Fourier-transform structure has deep physical content. A slowly-varying, long-range potential (like the Coulomb potential) has a large Fourier transform at small q — meaning it scatters predominantly at small angles. A sharply peaked, short-range potential has significant Fourier components at large q — scattering out to large angles. This is the quantum analog of optical diffraction: the far-field diffraction pattern of an aperture is the Fourier transform of its transmission function. In both cases, the scatterer and the scattering pattern are related by a Fourier transform. The connection to time-independent perturbation theory is also direct: the Born approximation is equivalent to first-order perturbation theory applied to scattering states.

The Born approximation is valid when the potential is weak compared to the particle's kinetic energy — either because |V| is intrinsically small, or because the incident energy ℏ²k²/2m is large. For the Coulomb potential V(r) = Ze²/r, the Fourier transform gives f(θ) ∝ 1/sin²(θ/2), producing the **Rutherford cross section** dσ/dΩ ∝ 1/sin⁴(θ/2). Remarkably, this is the same result Rutherford derived classically, and it was one of the first triumphs of quantum scattering theory. The approximation fails at low energies or for strong potentials, where higher-order terms (multiple scattering events) become significant, but it remains the essential first tool for connecting potential shapes to scattering patterns.
