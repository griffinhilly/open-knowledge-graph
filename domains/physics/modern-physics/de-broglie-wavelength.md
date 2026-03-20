---
id: de-broglie-wavelength
title: de Broglie Wavelength
domain: physics
course: modern-physics
prerequisites:
- id: wave-particle-duality
  type: hard
- id: momentum-and-impulse
  type: hard
- id: photon-model
  type: hard
builds-toward:
- heisenberg-uncertainty-principle
- schrodinger-equation-intro
tags:
- quantum
- matter-waves
- de-broglie
- wavelength
stage: advanced
status: validated
---

# de Broglie Wavelength

## Core Idea
de Broglie (1924) proposed that all matter has an associated wavelength λ = h/p = h/(mv) for a non-relativistic particle with momentum p. This matter wave is not a physical wave in a medium but a probability wave. For a macroscopic object the wavelength is immeasurably small, which is why classical mechanics works; for electrons the wavelength is comparable to atomic spacings, producing observable diffraction. The de Broglie relation gives a physical basis for Bohr's angular momentum quantization: standing matter waves fit on integer orbits.

## How It's Best Learned
Calculate de Broglie wavelengths for electrons, protons, and a baseball to get a sense of scale. Rederive Bohr quantization by requiring an integer number of matter wave wavelengths to fit the orbit circumference.

## Common Misconceptions
- The de Broglie wavelength applies only to electrons — it applies to all matter; it is just negligible for large masses.
- A slower particle has a shorter wavelength — a slower particle has less momentum, so λ = h/p is larger, not smaller.

## Explainer

From your prerequisite on wave-particle duality, you know that light behaves both as a wave (diffraction, interference) and as a particle (the photon, with energy E = hf). From the photon model, you know that a photon carries momentum p = E/c = hf/c = h/λ. de Broglie's 1924 insight was audaciously simple: if light (which we thought was a wave) turned out to have particle properties, why shouldn't matter (which we thought was particles) have wave properties? He proposed that any particle with momentum p has an associated wavelength **λ = h/p**, where h is Planck's constant.

The formula connects your two prerequisites directly. From momentum-and-impulse, you know p = mv for a non-relativistic particle. So λ = h/(mv): a heavier or faster particle has a shorter wavelength. Planck's constant h ≈ 6.63 × 10⁻³⁴ J·s is extraordinarily small. For a baseball (0.15 kg) at 40 m/s: λ = 6.63 × 10⁻³⁴ / (0.15 × 40) ≈ 10⁻³⁴ m — far smaller than an atomic nucleus. No experiment can detect wave behavior at that scale, which is why classical mechanics works perfectly for everyday objects. For an electron accelerated through 100 V: its kinetic energy is 100 eV, its momentum p = √(2mE) ≈ 5.4 × 10⁻²⁴ kg·m/s, and λ ≈ 1.2 × 10⁻¹⁰ m = 1.2 Å — exactly the spacing between atoms in a crystal. This is why electron diffraction is a real, observable phenomenon used to determine crystal structures.

The **matter wave** described by λ = h/p is not a physical oscillation of a medium — it is a **probability wave**. The squared magnitude of the wave function at a location gives the probability of finding the particle there. This reinterpretation has no classical analog, but the mathematical consequences are immediate and testable. When electron beams scatter off a crystal lattice, they produce diffraction patterns (Davisson-Germer experiment, 1927) that match the prediction from λ = h/p exactly, confirming de Broglie's hypothesis.

The most elegant connection is the derivation of Bohr's quantization rule. Bohr had postulated, without justification, that angular momentum must be quantized in units of ħ = h/(2π). de Broglie's hypothesis explains this: for a stable electron orbit of radius r, you require an **integer number of wavelengths to fit the circumference** — a standing wave condition. This gives 2πr = nλ = nh/p = nh/(mv), so mvr = nħ, which is exactly Bohr's quantization condition. The formerly arbitrary postulate becomes a resonance condition: only orbits that support standing matter waves are stable. This insight — that quantization arises from wave interference — is the conceptual foundation on which Schrödinger would later build his full wave equation.
