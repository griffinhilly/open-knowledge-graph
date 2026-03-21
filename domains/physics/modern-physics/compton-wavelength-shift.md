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

## Questions

```yaml
- question: "Classical wave theory (Thomson scattering) predicted that X-rays scattered off electrons would have the same wavelength as the incident X-rays. What did Compton actually observe, and why was it decisive evidence for the photon model?"
  type: multiple-choice
  options:
    - "Scattered X-rays were shorter in wavelength, proving electrons absorb photon energy and re-emit it at higher frequencies"
    - "Scattered X-rays had the same wavelength as predicted, confirming the classical wave model"
    - "Scattered X-rays were longer in wavelength, and the shift depended on scattering angle — consistent with photons losing momentum and energy in a particle collision"
    - "The wavelength shift depended on the incident wavelength, consistent with wave interference patterns"
  answer: 2
  explanation: "Compton observed wavelength *increase* (redshift) in scattered X-rays, with the shift depending on scattering angle — exactly as predicted by treating the photon as a particle carrying momentum p = h/λ and applying conservation of energy and momentum. Classical wave theory predicted zero wavelength shift (the electron oscillates at the driving frequency and re-radiates at the same frequency). The fact that the shift was independent of incident wavelength but depended only on scattering angle was unmistakable evidence for particle-like photon behavior."

- question: "What is the wavelength shift Δλ when X-rays undergo Compton scattering at θ = 90°?"
  type: multiple-choice
  options:
    - "Zero — no energy is transferred in perpendicular scattering"
    - "λ_C = h/mₑc ≈ 2.43 × 10⁻¹² m (the Compton wavelength)"
    - "2λ_C ≈ 4.86 pm — twice the Compton wavelength"
    - "It depends on the incident wavelength"
  answer: 1
  explanation: "The Compton formula is Δλ = (h/mₑc)(1 − cos θ). At θ = 90°, cos 90° = 0, so Δλ = h/mₑc = λ_C ≈ 2.43 pm. The maximum shift occurs at θ = 180° (backscatter): Δλ = 2λ_C. At θ = 0° (forward scatter), Δλ = 0 — no energy transfer. A critical feature: Δλ depends only on θ, not on the incident wavelength. This angle-only dependence is a characteristic fingerprint of particle collisions and has no natural explanation in classical wave theory."

- question: "The Compton wavelength shift Δλ is larger for shorter-wavelength (higher-energy) incident photons than for longer-wavelength ones, at the same scattering angle."
  type: true-false
  answer: false
  explanation: "This is the most tempting misconception. The formula Δλ = (h/mₑc)(1 − cos θ) contains no dependence on the incident wavelength λ — only on the scattering angle θ and fundamental constants. At a given angle, the absolute wavelength shift is always the same (≈ 2.43 pm at θ = 90°) regardless of whether the incident photon is a hard X-ray or a soft one. The *fractional* shift Δλ/λ is larger for short-wavelength photons, which is why the effect is measurable with X-rays but negligible for visible light."

- question: "Compton scattering provides experimental evidence that photons carry momentum, not just energy."
  type: true-false
  answer: true
  explanation: "The Compton formula is derived by applying conservation of *both* energy and momentum to the photon-electron collision, assigning the photon momentum p = h/λ. If photons carried no momentum, there would be no recoil of the electron, no energy transfer, and no wavelength shift — the classical Thomson scattering result. The fact that the observed wavelength shift matches exactly the prediction from momentum conservation confirms that photons carry momentum h/λ and exchange it with electrons in a collision. This was a cornerstone result in establishing the quantum picture of light."

- question: "Why did Compton use X-rays rather than visible light in his experiment, and why does deriving the Compton formula require relativistic mechanics?"
  type: short-answer
  answer: "Compton used X-rays because the wavelength shift Δλ = λ_C(1 − cos θ) is a fixed value (at most ~4.86 pm). For visible light (λ ~ 500 nm), this shift is less than 0.001% of the wavelength — far too small to measure. For X-rays (λ ~ 10–100 pm), the shift is a significant fraction of the wavelength and measurable. Relativistic mechanics is required because the recoiling electron can gain kinetic energy comparable to its rest mass energy (mₑc² ≈ 0.511 MeV) for energetic photons, and the relativistic energy-momentum relation E² = (pc)² + (mₑc²)² must be used for the electron. Non-relativistic treatment gives incorrect results."
  explanation: "The choice of X-rays was not arbitrary — it was dictated by the scale of the effect. The Compton wavelength λ_C = h/mₑc ≈ 2.43 pm sets the natural scale; the effect is only measurable when the incident wavelength is comparable to λ_C. The relativistic requirement is a deeper point: it shows that even 'low-energy' photon scattering can impart relativistic recoil velocities to electrons, making Compton scattering one of the earliest phenomena demanding special relativity for its explanation."
```

## Explainer

From the photon concept, you know that light comes in discrete quanta with energy E = hf = hc/λ and — crucially — momentum p = h/λ = E/c. From conservation of momentum, you know how to analyze collisions using both components of momentum and energy. Compton scattering is simply a collision problem where the projectile is a photon and the target is an electron at rest, treated with the tools you already have.

Before 1923, wave theory predicted that when X-rays scatter off electrons, the scattered X-rays should have the same wavelength as the incident ones — the electron should just oscillate and re-radiate at the driving frequency. This is **Thomson scattering**, the classical prediction. What Compton found experimentally was that the scattered X-rays were consistently longer in wavelength than the incident ones, with the shift depending on the angle. Classical wave theory had no explanation. The photon model did.

Apply conservation of energy and conservation of both components of momentum to a photon-electron collision, treating the photon as carrying energy E = hc/λ and momentum p = h/λ. The electron recoils and picks up both energy and momentum. Working through the algebra (using the relativistic energy-momentum relation for the recoiling electron, E² = (pc)² + (mₑc²)²), you arrive at the **Compton formula**: Δλ = λ' − λ = (h/mₑc)(1 − cos θ), where θ is the angle between the incident and scattered photon directions. The quantity λ_C = h/mₑc ≈ 2.43 × 10⁻¹² m is the **Compton wavelength** of the electron — the natural length scale of the interaction.

Notice two key features. First, Δλ depends only on scattering angle, not on the incident wavelength. At θ = 0° (forward scatter), Δλ = 0 — no energy is transferred. At θ = 90°, Δλ = λ_C. At θ = 180° (backscatter), Δλ = 2λ_C — maximum energy transfer. Second, the shift Δλ = 2.43 pm is tiny compared to visible light wavelengths (∼500 nm) but significant for hard X-rays (∼10–100 pm) — which is why Compton used X-rays in his experiments. The Compton effect was decisive evidence that photons are real particles that exchange definite momentum with electrons, not merely waves — a cornerstone result in establishing the quantum mechanical picture of light.
