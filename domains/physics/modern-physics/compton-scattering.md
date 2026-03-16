---
id: compton-scattering
title: Compton Scattering
domain: physics
course: modern-physics
prerequisites:
- id: photon-model
  type: hard
- id: momentum-and-impulse
  type: hard
- id: special-relativity-postulates
  type: soft
- id: trigonometric-ratios-review
  type: soft
builds-toward:
- wave-particle-duality
tags:
- quantum
- photon
- scattering
- momentum
- wavelength-shift
stage: advanced
status: validated
---

# Compton Scattering

## Core Idea
When X-rays scatter off electrons, the scattered photons have a longer wavelength than the incident ones — a shift unexplainable by classical wave theory. Compton (1923) showed that treating the photon as a particle with momentum p = h/λ and applying conservation of relativistic energy and momentum gives the Compton shift formula: Δλ = (h/m_e c)(1 − cos θ), where θ is the scattering angle. This was decisive evidence that photons carry momentum and behave as particles in collisions.

## How It's Best Learned
Derive the Compton formula using 2D conservation of energy and momentum, treating the electron relativistically. Compare the wavelength shift predicted at various angles with Compton's original data.

## Common Misconceptions
- The wavelength shift depends on the initial wavelength — it depends only on the scattering angle and fundamental constants, not on the incident wavelength.
- Classical scattering (Thomson) predicts the same shift — classical theory predicts no wavelength change at all, which is why the observed shift was so striking.

## Explainer

By 1923, photoelectric effect experiments had established that light delivers energy in discrete quanta E = hf. But a more radical claim was still contested: does light also carry **momentum**? Classical waves carry energy spread continuously through the wave, but no well-defined particle momentum. Einstein had proposed that a photon's momentum should be p = E/c = hf/c = h/λ — a hypothesis that could not be tested by the photoelectric effect alone, which involved photons being absorbed rather than scattered. Compton's experiment was the decisive test.

The classical prediction for X-ray scattering off electrons is called **Thomson scattering**: the oscillating electric field of the X-ray drives the electron to oscillate, and the accelerating electron re-radiates at the same frequency. Classical theory predicts zero wavelength shift — the scattered X-ray should have the same wavelength as the incident one. Compton measured scattered X-rays at various angles and found that the scattered wavelength was always *longer* than the incident wavelength, by an amount that increased with scattering angle. The wavelength shift was real, reproducible, and completely inexplicable by classical wave theory.

Compton's insight was to treat the interaction as a **two-body elastic collision** between a photon and a free electron, applying conservation of both relativistic energy and momentum. Before the collision: photon with energy E = hc/λ and momentum p_photon = h/λ, electron at rest with rest energy m_e c². After the collision: photon departs at angle θ with wavelength λ', electron recoils at angle φ with relativistic energy and momentum. Setting up conservation of energy and x- and y-momentum gives three equations in three unknowns (λ', and the electron's exit angle and speed). Solving this system — which requires eliminating the electron's final state variables — yields the celebrated **Compton formula**: Δλ = λ' − λ = (h/m_e c)(1 − cos θ).

The quantity h/m_e c = 2.426 × 10⁻¹² m ≈ 2.4 pm is called the **Compton wavelength** of the electron. It sets the scale of the wavelength shift. At θ = 0° (forward scattering), Δλ = 0 — the photon passes through undeflected. At θ = 90°, Δλ = h/m_e c ≈ 2.4 pm. At θ = 180° (backscattering), Δλ = 2h/m_e c ≈ 4.8 pm — the maximum shift. Crucially, this shift is independent of the initial wavelength λ. For visible light (λ ≈ 500 nm), the fractional shift Δλ/λ ≈ 10⁻⁵ is unmeasurably small — this is why Compton's effect doesn't matter for everyday light. For hard X-rays (λ ≈ 0.1 nm), the fractional shift becomes several percent, large enough to measure precisely with the crystal spectrometers available in the 1920s. The agreement between Compton's formula and his data, verified immediately by others, established once and for all that photons carry momentum and interact as particles in collisions.
