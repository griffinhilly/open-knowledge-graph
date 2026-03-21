---
id: cosmological-redshift-and-hubble-law
title: Cosmological Redshift and the Hubble Law
domain: earth-and-space-sciences
course: astronomy
prerequisites:
- id: galaxy-rotation-curves-dark-matter
  type: soft
- id: doppler-effect
  type: soft
builds-toward:
- cosmic-microwave-background-observations
tags:
- cosmology
- redshift
- expansion
stage: advanced
status: draft
---

# Cosmological Redshift and the Hubble Law

## Core Idea
The redshift of distant galaxies—the stretching of wavelengths due to expansion of spacetime—is related to distance by the Hubble law: recession velocity is proportional to distance (v = H₀d). This relationship revealed that the universe is expanding uniformly and enabled the first measurements of the cosmic expansion rate (Hubble constant ~70 km/s/Mpc). Cosmological redshift differs fundamentally from Doppler redshift: it results from metric expansion, not motion through space.

## Questions

```yaml
- question: "A galaxy is observed with a recession velocity that appears to exceed the speed of light based on the Hubble law. What is the correct interpretation?"
  type: multiple-choice
  options:
    - "The measurement must be wrong — nothing can recede faster than light"
    - "The galaxy is actually moving through space faster than light, which is possible for massive objects"
    - "The space between us and the galaxy is expanding, and metric expansion is not limited by the speed of light"
    - "The Hubble law has broken down and a different formula must be used instead"
  answer: 2
  explanation: "Cosmological redshift is caused by the expansion of spacetime itself, not by galaxies moving through pre-existing space. The speed-of-light limit applies to objects moving through space; the expansion of the metric has no such restriction. Galaxies at redshift z > 1 have recession velocities exceeding c in the naive Hubble formula, but this is perfectly consistent with general relativity. The key insight is distinguishing motion through space (kinematic, limited by c) from the stretching of space itself (metric expansion, not so limited)."

- question: "A galaxy is observed at redshift z = 2. What does this tell us about the scale of the universe when that light was emitted?"
  type: multiple-choice
  options:
    - "The universe was twice as large as it is today"
    - "The universe was one-third its current size when the light was emitted"
    - "The galaxy was moving at twice the speed of light when it emitted the light"
    - "The observed wavelength is twice the emitted wavelength"
  answer: 1
  explanation: "z = (λ_observed − λ_emitted)/λ_emitted = 2 means λ_observed = 3 × λ_emitted. This tells us the universe has expanded by a factor of 1 + z = 3 since that light was emitted — the universe was one-third its current size. Option A (twice as large) is wrong; option D only captures part of the definition. The redshift parameter directly encodes the ratio of the scale factor at observation to the scale factor at emission: a_observed/a_emitted = 1 + z."

- question: "Cosmological redshift and Doppler redshift are essentially the same phenomenon — both involve the stretching of light wavelengths as source and observer separate."
  type: true-false
  answer: false
  explanation: "They are fundamentally different despite producing similar spectral shifts. Doppler redshift is a kinematic effect: the source moves through space, and the wavefronts are physically stretched by that motion. Cosmological redshift arises from metric expansion: the source and observer are not moving through space; rather, space itself is expanding between them, stretching the photon wavelengths during transit. The distinction has real observational consequences — at large redshifts, the Doppler interpretation gives velocities exceeding c and breaks down, while the metric expansion interpretation remains physically consistent."

- question: "The Hubble constant H₀ encodes the expansion rate of the universe, and inverting it (1/H₀) gives a rough estimate of the age of the universe."
  type: true-false
  answer: true
  explanation: "If the expansion rate has been roughly constant, the time elapsed since all galaxies were at the same location is approximately 1/H₀. With H₀ ≈ 70 km/s/Mpc, this gives 1/H₀ ≈ 14 billion years — close to the more precise value of 13.8 billion years from detailed cosmological modeling. The estimate is only approximate because the expansion rate has not been constant: it was decelerating early (matter-dominated era) and has been accelerating recently (dark energy-dominated). A full treatment requires integrating over the entire expansion history."

- question: "Explain why cosmological redshift differs fundamentally from the Doppler effect, and why the distinction matters for interpreting observations of very distant galaxies."
  type: short-answer
  answer: "Doppler redshift occurs when a source moves through space — the motion compresses or stretches wavefronts relative to a stationary observer. Cosmological redshift occurs when space itself expands: a photon's wavelength is stretched in proportion to the expansion of the universe during the photon's travel time. The distinction matters because the speed-of-light limit applies to objects moving through space, not to the expansion of space. At large redshifts (z > 1), naive application of the Doppler formula implies velocities exceeding c, which would be physically impossible for a kinematic effect but is perfectly valid for metric expansion."
  explanation: "The practical consequence is that the simple Hubble law v = H₀d is only valid for nearby galaxies where z << 1 and the two interpretations converge. At cosmological distances, the full general-relativistic treatment is required, relating redshift to the integral of the scale factor history. Understanding this distinction is also essential for interpreting the cosmic microwave background (z ≈ 1100), where photons have been traveling since the universe was 1/1101 its current size."
```

## Explainer

You are familiar with the Doppler effect: when a source of waves moves away from you, the waves get stretched and their wavelength increases. For light, this stretching shifts the spectrum toward the red end — a **redshift**. In the 1920s, Edwin Hubble observed that nearly all distant galaxies show redshifted spectra, and that the amount of redshift is proportional to the galaxy's distance. This pattern — now called the **Hubble law** — was the first observational evidence that the universe is expanding.

The Hubble law is expressed as v = H₀d, where v is the recession velocity of a galaxy, d is its distance from us, and H₀ is the **Hubble constant**, measured at approximately 70 km/s/Mpc (kilometers per second per megaparsec). This means a galaxy 100 Mpc away recedes at about 7,000 km/s, while one 200 Mpc away recedes at 14,000 km/s. The linear relationship tells us something profound: the universe is expanding uniformly. There is no special center — every point in the universe sees every other point receding, just as dots on a balloon all move apart from each other as the balloon inflates. The Hubble constant sets the rate of this expansion and, inverted, gives a rough estimate of the age of the universe (1/H₀ ≈ 14 billion years, close to the more precise value of 13.8 billion years from detailed cosmological models).

The critical conceptual distinction is between **cosmological redshift** and ordinary Doppler redshift. A Doppler shift occurs when a source moves through space — it is a kinematic effect. Cosmological redshift is fundamentally different: the galaxies are not flying apart through a pre-existing space; rather, the fabric of space itself is expanding, and the light waves traveling through it get stretched along with it. A photon emitted with a certain wavelength when the universe was smaller arrives with a longer wavelength because space has expanded during the photon's journey. The redshift parameter z is defined as the fractional change in wavelength: z = (λ_observed - λ_emitted) / λ_emitted. A galaxy at z = 1 means the universe has doubled in scale since that light was emitted.

This distinction matters because at large distances, the Doppler interpretation breaks down. Galaxies with redshifts z > 1 have recession velocities that formally exceed the speed of light, which would be impossible for motion through space but is perfectly consistent with metric expansion — space itself is not bound by the speed-of-light limit. The Hubble law in its simple form (v = H₀d) is an approximation valid for nearby galaxies; at cosmological distances, the full general-relativistic treatment replaces it with a relationship between redshift and the scale factor of the universe. Measuring the Hubble constant precisely remains one of the central challenges of modern cosmology, with different measurement methods currently yielding slightly discrepant values — the so-called **Hubble tension** — which may point to new physics beyond the standard cosmological model.
