---
id: davisson-germer-crystal-diffraction
title: 'Davisson-Germer Experiment: Crystal Diffraction of Electrons'
domain: physics
course: modern-physics
prerequisites:
- id: electron-diffraction-matter-wavelength
  type: hard
tags:
- wave-particle-duality
- electron-diffraction
- experimental
stage: advanced
status: validated
---

# Davisson-Germer Experiment: Crystal Diffraction of Electrons

## Core Idea
The Davisson-Germer experiment (1927) scattered low-energy electrons from a nickel crystal and observed strong diffraction peaks that followed Bragg's law nλ = 2d sinθ. The observed wavelengths exactly matched de Broglie's prediction λ = h/p, providing the first direct confirmation of matter waves and a landmark proof of wave-particle duality.

## How It's Best Learned
Study the original experimental setup and data. Calculate expected wavelengths for the electron energies used and verify Bragg's law. Understand why the diffraction pattern requires the electron to have wave-like properties.

## Common Misconceptions
The Davisson-Germer result is not explained by assuming electrons are classical particles scattering randomly (the sharp diffraction peaks rule this out). The experiment requires electron momentum to be de Broglie wavelength.

## Questions

```yaml
- question: "In the Davisson-Germer experiment, why does electron intensity peak sharply at specific scattering angles rather than spreading diffusely in all directions?"
  type: multiple-choice
  options:
    - "Electrons are repelled by the nickel crystal lattice except at specific angles where the crystal surface is smooth"
    - "The electron beam is narrow and focused, so it only reaches the detector at specific angles"
    - "Constructive interference occurs only when the path length difference between waves scattered from successive crystal planes equals a whole number of wavelengths (Bragg's law)"
    - "The detector is only sensitive to electrons traveling in certain directions due to its geometry"
  answer: 2
  explanation: "The sharp peaks are the direct signature of wave interference. Electrons scatter from multiple parallel planes of the nickel crystal; the waves scattered from successive planes are only in phase (constructively interfering) when the path length difference between them satisfies Bragg's law: nλ = 2d sinθ. At all other angles, partial or complete destructive interference suppresses the signal. This peak-and-trough angular pattern is physically identical to what happens with X-rays or light waves in a diffraction grating — it requires a wave description and is impossible in classical particle physics."

- question: "If electrons were purely classical particles with no wave properties, what would the Davisson-Germer experiment show?"
  type: multiple-choice
  options:
    - "No electrons would scatter at all, since classical particles cannot penetrate a crystal"
    - "Electrons would scatter with sharp peaks at angles predicted by Snell's law for refraction"
    - "Electrons would scatter diffusely in all directions with no sharp angular dependence — a broad, smooth distribution"
    - "Electrons would show diffraction peaks, but at different angles than de Broglie predicts"
  answer: 2
  explanation: "Classical particles bouncing off a crystal surface would scatter based on individual atomic collisions, producing a broad distribution that falls off gradually with angle — similar to billiard balls bouncing off a rough surface. There would be no reason for intensity to peak sharply at specific angles and drop to near-zero in between. The existence of dark regions (destructive interference) between sharp bright peaks is the unambiguous fingerprint of wave behavior. You cannot get a dark region from classical particles — they would simply scatter in that direction with some probability."

- question: "The wavelengths measured from the Davisson-Germer diffraction patterns agreed quantitatively with de Broglie's prediction λ = h/p calculated from the electron's momentum."
  type: true-false
  answer: true
  explanation: "The agreement was not merely qualitative. For electrons accelerated through 54 V, the momentum is p = √(2mₑeV) ≈ 4.0 × 10⁻²⁴ kg·m/s, giving λ = h/p ≈ 0.166 nm. The observed diffraction peak at about 50° from the nickel crystal (lattice spacing d ≈ 0.215 nm) is quantitatively consistent with this wavelength via Bragg's law. The match was at the percent level — not an order-of-magnitude agreement but a precise quantitative confirmation that de Broglie's formula was correct."

- question: "The Davisson-Germer experiment showed that electrons sometimes behave as waves and sometimes as particles, depending on whether they are being measured."
  type: true-false
  answer: false
  explanation: "This is a common misstatement of wave-particle duality. The Davisson-Germer experiment did not show context-dependent behavior — it showed that in this specific experimental context (diffraction from a crystal), electrons exhibit wave behavior. The experiment is a demonstration that matter waves are real, not a demonstration of observer-dependent collapse or context switching. The 'sometimes wave, sometimes particle' framing conflates the philosophical interpretation of quantum mechanics with the experimental result. The result is simply: electrons produce diffraction patterns consistent with λ = h/p, which requires a wave description."

- question: "Why do sharp diffraction peaks rule out a classical (particle-only) explanation for the Davisson-Germer results?"
  type: short-answer
  answer: "Sharp peaks at specific angles separated by regions of near-zero intensity are the hallmark of wave interference. Constructive interference (peaks) occurs only when waves from successive crystal planes are in phase, satisfying Bragg's law. Between these angles, destructive interference suppresses intensity. Classical particles have no mechanism for cancellation — two particles traveling in the same direction don't cancel each other out. A classical particle model predicts diffuse, angle-independent scattering from atomic collisions, not sharp peaks and dark troughs. The existence of the dark troughs (near-zero intensity between peaks) is the decisive evidence that electrons must behave as waves."
  explanation: "This reasoning is more powerful than just 'the peak positions match de Broglie' — it is the pattern of peaks AND troughs together that requires a wave description. X-rays, water waves, and light all produce the same pattern when scattered from periodic structures, and in each case the dark regions are the conclusive signature of wave cancellation. Davisson-Germer placed electrons unambiguously in this category."
```

## Explainer

From your study of electron diffraction and the de Broglie hypothesis, you know that matter has a wavelength λ = h/p. This was a bold theoretical prediction in 1924, but the question physicists urgently needed answered was: is this real? Does matter actually exhibit wave interference, or is the wavelength just a mathematical convenience with no observable consequences? The Davisson-Germer experiment answered this question with a resounding yes, and did so in a way that left no room for classical alternatives.

The experimental setup was straightforward: a beam of low-energy electrons (accelerated through a few tens of volts) was aimed at a nickel crystal, and a movable detector measured the number of electrons scattered into each angle. The crystal was not chosen arbitrarily — its regularly spaced atomic planes act as a **diffraction grating** for anything with the right wavelength. Bragg's law, nλ = 2d sinθ, describes the constructive interference condition: waves reflect from successive atomic planes and reinforce only when the path length difference between them is a whole number of wavelengths. The nickel crystal's lattice spacing d was already known from X-ray crystallography.

The result was unambiguous: the scattered electron intensity peaked sharply at specific angles exactly matching Bragg's law. When Davisson and Germer computed the wavelength that would produce peaks at those angles, they got λ ≈ h/p for electrons of the measured energy — precisely de Broglie's prediction. At 54 eV, the electron momentum is p = √(2mE) ≈ 4.0 × 10⁻²⁴ kg·m/s, giving λ = h/p ≈ 0.166 nm. The nickel crystal spacing is about 0.215 nm, and the observed diffraction peak at 50° is consistent with this wavelength and spacing via Bragg's law. The match was not approximate — it was quantitative agreement at the percent level.

What rules out a classical explanation? Classical particles bouncing off a crystal surface would scatter in a broad, diffuse pattern — some atoms would scatter more, others less, but there would be no sharp constructive interference peaks. The existence of peaks at specific angles, with dark regions in between, is the hallmark of wave interference. Just as two water waves cancel where trough meets crest and reinforce where crest meets crest, the electron "waves" scattered from successive crystal planes cancel at most angles and reinforce only where the Bragg condition is satisfied. This is the same phenomenon that makes soap bubbles iridescent and explains why X-rays diffract from crystals. Davisson-Germer placed electrons in the same category: real waves, not a mathematical fiction. This result, alongside G.P. Thomson's independent electron diffraction experiment using thin metal foils, established wave-particle duality as an experimental fact about matter itself.
