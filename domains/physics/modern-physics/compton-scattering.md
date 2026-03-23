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
stage: formal-systems
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

## Questions

```yaml
- question: "A physicist repeats Compton's experiment using ultraviolet light (λ ≈ 100 nm) instead of X-rays, measuring the scattered wavelength at θ = 90°. How large is the wavelength shift?"
  type: multiple-choice
  options:
    - "Much larger than for X-rays, because UV photons have higher energy"
    - "Much smaller than for X-rays, because UV photons have lower momentum"
    - "Approximately 2.4 pm — the same as for X-rays at the same angle, because the Compton shift depends only on scattering angle and fundamental constants"
    - "Zero, because UV light is not energetic enough to transfer momentum to an electron"
  answer: 2
  explanation: "The Compton formula Δλ = (h/m_e c)(1 − cos θ) contains no term for the incident wavelength — only the scattering angle θ and fundamental constants (h, m_e, c). At θ = 90°, Δλ = h/m_e c ≈ 2.4 pm regardless of whether you use soft X-rays, hard X-rays, or UV. The fractional shift Δλ/λ is much smaller for UV (λ ≈ 100 nm) than for hard X-rays (λ ≈ 0.1 nm), which is why the effect wasn't first detected with visible or UV light, but the absolute shift is the same."

- question: "How did classical electromagnetic theory (Thomson scattering) predict the outcome of X-ray scattering off electrons, before Compton's experiment?"
  type: multiple-choice
  options:
    - "The scattered X-rays should have a shorter wavelength, as energy is transferred from photon to electron"
    - "The scattered X-rays should have the same wavelength as the incident X-rays — the driven electron re-radiates at the same frequency it was driven at"
    - "The scattered X-rays should show the same wavelength shift as Compton observed"
    - "No scattering should occur because classical electrons are too light to deflect X-rays"
  answer: 1
  explanation: "In Thomson scattering, the oscillating electric field of an X-ray forces the electron to oscillate at the same frequency. The accelerating electron then re-radiates electromagnetic waves at that same frequency — no wavelength change is predicted. This is why Compton's observation of a real, angle-dependent wavelength shift was so striking: it was completely inexplicable by classical wave theory and required treating the photon as a particle with momentum."

- question: "The Compton wavelength shift at a given scattering angle is the same whether the incident photon is a soft X-ray or a hard X-ray."
  type: true-false
  answer: true
  explanation: "The Compton formula Δλ = (h/m_e c)(1 − cos θ) is independent of the incident wavelength. The absolute shift depends only on the scattering angle and fundamental constants. This is one of the formula's most striking features, and it was confirmed by Compton's data across multiple X-ray energies. The fractional shift Δλ/λ does depend on the incident wavelength — which is why the effect is only observable with X-rays (λ ~ 0.1 nm) and not with visible light (λ ~ 500 nm)."

- question: "Compton scattering was primarily significant for confirming that light travels at the speed c in all inertial frames."
  type: true-false
  answer: false
  explanation: "Compton scattering proved that photons carry momentum (p = h/λ) and interact as particles in elastic collisions — not anything about the speed of light. The speed of light was already firmly established. The revolutionary insight from Compton's experiment was photon momentum: Einstein had proposed p = h/λ, but the photoelectric effect couldn't test it (photons were absorbed, not scattered). Compton's experiment — where photons bounced off electrons at measurable angles with predictable momentum transfer — was the decisive test."

- question: "Why couldn't the photoelectric effect alone prove that photons carry momentum, and what made Compton scattering the decisive evidence?"
  type: short-answer
  answer: "In the photoelectric effect, photons are absorbed by electrons — the photon disappears. An absorbed particle transfers its energy, but there is no way to measure the momentum transfer independently of the energy, so the momentum hypothesis p = h/λ couldn't be directly tested. In Compton scattering, the photon bounces off the electron and continues in a new direction — it survives the collision. By measuring both the scattered photon's new wavelength and the electron's recoil angle, Compton could check that both energy and momentum were conserved according to relativistic mechanics, with p_photon = h/λ. The agreement between the formula and data at every angle confirmed photon momentum directly."
  explanation: "The key distinction is absorption vs. scattering. Scattering is a two-body collision with two measurable final states (scattered photon + recoiling electron), allowing independent tests of momentum conservation. This is what made Compton's experiment so compelling — the particle-collision model made specific, quantitative predictions about how the wavelength shift would vary with angle, and those predictions matched data precisely."
```

## Explainer

By 1923, photoelectric effect experiments had established that light delivers energy in discrete quanta E = hf. But a more radical claim was still contested: does light also carry **momentum**? Classical waves carry energy spread continuously through the wave, but no well-defined particle momentum. Einstein had proposed that a photon's momentum should be p = E/c = hf/c = h/λ — a hypothesis that could not be tested by the photoelectric effect alone, which involved photons being absorbed rather than scattered. Compton's experiment was the decisive test.

The classical prediction for X-ray scattering off electrons is called **Thomson scattering**: the oscillating electric field of the X-ray drives the electron to oscillate, and the accelerating electron re-radiates at the same frequency. Classical theory predicts zero wavelength shift — the scattered X-ray should have the same wavelength as the incident one. Compton measured scattered X-rays at various angles and found that the scattered wavelength was always *longer* than the incident wavelength, by an amount that increased with scattering angle. The wavelength shift was real, reproducible, and completely inexplicable by classical wave theory.

Compton's insight was to treat the interaction as a **two-body elastic collision** between a photon and a free electron, applying conservation of both relativistic energy and momentum. Before the collision: photon with energy E = hc/λ and momentum p_photon = h/λ, electron at rest with rest energy m_e c². After the collision: photon departs at angle θ with wavelength λ', electron recoils at angle φ with relativistic energy and momentum. Setting up conservation of energy and x- and y-momentum gives three equations in three unknowns (λ', and the electron's exit angle and speed). Solving this system — which requires eliminating the electron's final state variables — yields the celebrated **Compton formula**: Δλ = λ' − λ = (h/m_e c)(1 − cos θ).

The quantity h/m_e c = 2.426 × 10⁻¹² m ≈ 2.4 pm is called the **Compton wavelength** of the electron. It sets the scale of the wavelength shift. At θ = 0° (forward scattering), Δλ = 0 — the photon passes through undeflected. At θ = 90°, Δλ = h/m_e c ≈ 2.4 pm. At θ = 180° (backscattering), Δλ = 2h/m_e c ≈ 4.8 pm — the maximum shift. Crucially, this shift is independent of the initial wavelength λ. For visible light (λ ≈ 500 nm), the fractional shift Δλ/λ ≈ 10⁻⁵ is unmeasurably small — this is why Compton's effect doesn't matter for everyday light. For hard X-rays (λ ≈ 0.1 nm), the fractional shift becomes several percent, large enough to measure precisely with the crystal spectrometers available in the 1920s. The agreement between Compton's formula and his data, verified immediately by others, established once and for all that photons carry momentum and interact as particles in collisions.
