---
id: compton-wavelength-shift
title: Compton Scattering and Wavelength Shift
domain: physics
course: modern-physics
prerequisites:
- id: photon-concept-quanta
  type: hard
- id: conservation-of-momentum
  type: hard
builds-toward:
- matter-wave-de-broglie-momentum
tags:
- quantum
- scattering
- photons
stage: advanced
status: draft
---

# Compton Scattering and Wavelength Shift

## Core Idea
When a photon scatters off a free electron, the photon loses energy and its wavelength increases (redshifts). The wavelength shift is Δλ = λ' − λ = (h/mₑc)(1 − cos θ), independent of incident wavelength and depending only on scattering angle. This effect demonstrates that photons carry momentum and act like particles in collisions, not like classical waves.

## Explainer

From the photon concept, you know that light comes in discrete quanta with energy E = hf = hc/λ and — crucially — momentum p = h/λ = E/c. From conservation of momentum, you know how to analyze collisions using both components of momentum and energy. Compton scattering is simply a collision problem where the projectile is a photon and the target is an electron at rest, treated with the tools you already have.

Before 1923, wave theory predicted that when X-rays scatter off electrons, the scattered X-rays should have the same wavelength as the incident ones — the electron should just oscillate and re-radiate at the driving frequency. This is **Thomson scattering**, the classical prediction. What Compton found experimentally was that the scattered X-rays were consistently longer in wavelength than the incident ones, with the shift depending on the angle. Classical wave theory had no explanation. The photon model did.

Apply conservation of energy and conservation of both components of momentum to a photon-electron collision, treating the photon as carrying energy E = hc/λ and momentum p = h/λ. The electron recoils and picks up both energy and momentum. Working through the algebra (using the relativistic energy-momentum relation for the recoiling electron, E² = (pc)² + (mₑc²)²), you arrive at the **Compton formula**: Δλ = λ' − λ = (h/mₑc)(1 − cos θ), where θ is the angle between the incident and scattered photon directions. The quantity λ_C = h/mₑc ≈ 2.43 × 10⁻¹² m is the **Compton wavelength** of the electron — the natural length scale of the interaction.

Notice two key features. First, Δλ depends only on scattering angle, not on the incident wavelength. At θ = 0° (forward scatter), Δλ = 0 — no energy is transferred. At θ = 90°, Δλ = λ_C. At θ = 180° (backscatter), Δλ = 2λ_C — maximum energy transfer. Second, the shift Δλ = 2.43 pm is tiny compared to visible light wavelengths (∼500 nm) but significant for hard X-rays (∼10–100 pm) — which is why Compton used X-rays in his experiments. The Compton effect was decisive evidence that photons are real particles that exchange definite momentum with electrons, not merely waves — a cornerstone result in establishing the quantum mechanical picture of light.
