---
id: partial-wave-analysis
title: Partial Wave Analysis in Scattering
domain: physics
course: quantum-mechanics
prerequisites:
- id: scattering-theory-intro
  type: hard
- id: orbital-angular-momentum-quantum
  type: hard
builds-toward:
- cross-sections-scattering
tags:
- partial-waves
- angular-momentum
stage: advanced
status: validated
---

# Partial Wave Analysis in Scattering

## Core Idea
Scattering amplitude expands in angular momentum: f(θ) = Σ_l (2l+1) f_l P_l(cos θ) / 2ik. Low energies dominated by s-wave (l=0). Phase shift δ_l encodes each partial wave's phase change.

## Questions

```yaml
- question: "For a spherically symmetric scattering potential, why does the potential affect each partial wave independently rather than mixing different angular momentum values?"
  type: multiple-choice
  options:
    - "The potential is too weak at large distances to couple different angular momentum channels"
    - "Angular momentum l is conserved under central potentials, so each l-channel evolves independently and the potential can only shift the phase within each channel"
    - "The Legendre polynomials P_l are orthogonal, which prevents numerical mixing during computation"
    - "The scattering amplitude f(θ) is defined only for real angles, which restricts any coupling to single l values"
  answer: 1
  explanation: "This follows directly from your study of orbital angular momentum: a spherically symmetric (central) potential commutes with the angular momentum operators L² and Lz, so l is a good quantum number. States of different l cannot mix under a central force. This is what makes partial wave analysis so powerful: the scattering problem decouples into independent channels, each described by a single real number δ_l — the phase shift."

- question: "A scattering experiment at low energy (kR ≪ 1) yields an angular distribution that is completely isotropic — the same differential cross section in every direction. What does this immediately tell you about the partial wave expansion?"
  type: multiple-choice
  options:
    - "The potential has no angular dependence, so the scattering amplitude vanishes entirely"
    - "Only the s-wave (l = 0) contributes significantly; P₀(cosθ) = 1 gives isotropic scattering, and higher l partial waves are negligible"
    - "The total cross section is zero because partial waves from different l values cancel"
    - "The phase shift δ₀ must equal zero, meaning the s-wave scatters as if there is no potential"
  answer: 1
  explanation: "The angular dependence of each partial wave is given by P_l(cosθ). Since P₀ = 1 (constant), s-wave scattering is isotropic by construction. Higher partial waves (l ≥ 1) produce angular structure: P₁ ~ cosθ (dipole pattern), P₂ ~ (3cos²θ − 1)/2, etc. Isotropic scattering therefore signals that only l = 0 contributes. This makes physical sense: at low energy, a particle with momentum ℏk only reaches partial waves with l ≲ kR, so when kR ≪ 1 only l = 0 is accessible."

- question: "The scattering length a = −lim_{k→0} tan(δ₀)/k captures all of the low-energy scattering physics regardless of the detailed shape of the potential."
  type: true-false
  answer: true
  explanation: "At low energies, only the s-wave contributes, and the entire s-wave contribution is encoded in the single phase shift δ₀. As k → 0, the phase shift goes to zero and tan(δ₀)/k approaches a finite limit defining the scattering length a. Different potentials with the same scattering length are indistinguishable at low energies, regardless of how they differ at short range. This is why nuclear and atomic physicists can characterize very different potential shapes with a single parameter — the details of the potential are 'integrated out' into just a."

- question: "A resonance in partial wave l (a sharp peak in δ_l near π/2) indicates that the potential is too weak to cause significant scattering at that energy."
  type: true-false
  answer: false
  explanation: "This is exactly backwards. A resonance at δ_l = π/2 corresponds to the maximum possible scattering contribution from partial wave l. The partial wave cross section goes as sin²(δ_l), which equals 1 when δ_l = π/2 — the unitarity limit for that l-channel. Physically, a resonance signals a quasi-bound state: the particle lingers near the target (the attractive potential almost supports a bound state), producing a dramatic enhancement of scattering. The name 'resonance' reflects this: like a driven oscillator at resonance frequency, the scattering amplitude peaks dramatically."

- question: "Explain why partial wave analysis is especially powerful at low energies, and what information suffices to characterize scattering in that regime."
  type: short-answer
  answer: "At low energies (kR ≪ 1), a particle with momentum ℏk has angular momentum ℏl ≈ ℏkb for impact parameter b. Only partial waves with l ≲ kR have impact parameters small enough to 'feel' the potential of range R. When kR ≪ 1, only l = 0 (the s-wave) satisfies this, so the sum over partial waves reduces to a single term. Since P₀(cosθ) = 1, the scattering is isotropic. The entire interaction is encoded in the single phase shift δ₀, or equivalently the scattering length a. Any potential — regardless of its detailed shape — produces the same low-energy scattering if it has the same scattering length. This is a powerful universality: complex short-range physics is summarized by one number."
  explanation: "This universality is exploited throughout nuclear and atomic physics. The scattering length of two ultracold atoms can be tuned experimentally using a Feshbach resonance (an external magnetic field), allowing control of inter-particle interactions without changing the underlying potential's shape."
```

## Explainer

From scattering theory you already know the basic setup: an incident plane wave e^{ikz} interacts with a target potential and produces an outgoing spherical wave, with everything encoded in the **scattering amplitude** f(θ). Partial wave analysis is a systematic way to decompose this amplitude by angular momentum — essentially, by how far the incoming particle misses the center of the target.

The key insight is that a plane wave can be expanded in spherical waves of definite angular momentum: e^{ikz} = Σ_l i^l (2l+1) j_l(kr) P_l(cos θ). Each term in this sum is a **partial wave** corresponding to orbital angular momentum quantum number l. Far from the target, each radial function j_l(kr) looks like a combination of incoming and outgoing spherical waves. The potential can only change the *relative phase* between incoming and outgoing parts of each partial wave — it cannot mix different l values for a spherically symmetric potential, because you already know from orbital angular momentum theory that l is conserved under central potentials. The effect of the potential on partial wave l is therefore completely captured by a single real number, the **phase shift** δ_l: the outgoing wave is delayed (or advanced) in phase relative to the free case by 2δ_l.

This leads directly to the scattering amplitude: f(θ) = (1/k) Σ_l (2l+1) e^{iδ_l} sin(δ_l) P_l(cos θ), where the Legendre polynomials P_l(cos θ) carry the angular dependence. The total cross section is the integral |f(θ)|² over all angles, giving the **optical theorem**: σ_total = (4π/k) Im[f(0)]. Each partial wave contributes independently, and its maximum possible contribution to the cross section is 4π(2l+1)/k² — achieved when sin²(δ_l) = 1, i.e., δ_l = π/2.

The practical power comes from truncating the sum. A particle with linear momentum ℏk and impact parameter b has angular momentum ℏl ≈ ℏkb, so significant scattering only occurs for partial waves with l ≲ kR, where R is the range of the potential. At low energies (kR ≪ 1), only the **s-wave** (l = 0) contributes — scattering is isotropic (since P₀ = 1) and the entire interaction is encoded in the single number δ₀. This is why nuclear and atomic physicists can often characterize a low-energy scattering potential with just the **scattering length** a = −lim_{k→0} tan(δ₀)/k: one parameter captures all the low-energy physics regardless of the potential's detailed shape. As energy increases, higher partial waves turn on sequentially, and resonances — sharp peaks in a particular δ_l — signal quasi-bound states where the particle lingers near the target.
