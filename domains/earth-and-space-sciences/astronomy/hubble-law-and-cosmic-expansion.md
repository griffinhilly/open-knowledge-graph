---
id: hubble-law-and-cosmic-expansion
title: Hubble's Law and the Expanding Universe
domain: earth-and-space-sciences
course: astronomy
prerequisites:
- id: doppler-effect
  type: hard
- id: galaxy-morphology-and-classification
  type: hard
- id: stellar-end-states
  type: soft
- id: slope-concept
  type: soft
- id: cosmic-distance-ladder-calibration
  type: hard
builds-toward:
- big-bang-cosmology
- dark-matter-and-dark-energy
tags:
- Hubble-constant
- cosmic-expansion
- cosmological-redshift
- recession-velocity
- distance-ladder
- Cepheid-variables
- standard-candles
stage: advanced
status: validated
---

# Hubble's Law and the Expanding Universe

## Core Idea
Hubble's law states that galaxies recede from us at velocities proportional to their distances: v = H₀d, where H₀ is the Hubble constant (~70 km/s/Mpc). Discovered in 1929, this proportionality implies the universe is uniformly expanding — every galaxy moves away from every other, like raisins in rising bread. The spectral shift of galaxies is a cosmological redshift caused by the stretching of space itself, not by galaxies moving through static space. Measuring H₀ precisely requires the cosmic distance ladder: parallax → Cepheid variable stars → Type Ia supernovae; current precision measurements of H₀ reveal a tension that may signal new physics.

## How It's Best Learned
Plot recession velocity versus distance for a sample of galaxies and fit a line to recover H₀. Use the inverse of the Hubble constant as a rough estimate of the universe's age and compare to other age estimates.

## Common Misconceptions
- Hubble's law does not mean Earth is at the center of the universe — every observer in a uniformly expanding universe sees all other objects receding, with no special center.
- Cosmological redshift is not a Doppler effect; photon wavelengths are stretched by the expansion of space during travel, not by the source's peculiar velocity.

## Questions

```yaml
- question: "An astronomer in a galaxy 500 Mpc away measures the redshifts of neighboring galaxies and finds that they all appear to be receding from her. What does this tell us about the expansion of the universe?"
  type: multiple-choice
  options:
    - "Her galaxy is also at the center of the universe, just like Earth"
    - "Every observer in a uniformly expanding universe sees all other galaxies receding, so no location is special"
    - "The expansion must have originated near her galaxy, since she also observes recession"
    - "Her measurements are in error — only observers on Earth should see recession"
  answer: 1
  explanation: "Hubble's law reflects uniform expansion of space itself — like raisins in rising bread, every raisin moves away from every other. There is no special center. An observer anywhere would find the same proportionality v = H₀d, which is precisely why the expanding universe has no center."

- question: "A galaxy at redshift z = 2 has its light shifted to three times its emitted wavelength. The most accurate interpretation is that this galaxy is:"
  type: multiple-choice
  options:
    - "Moving away from Earth at twice the speed of light through static space"
    - "Located so far away that its Doppler shift has accumulated over time"
    - "Observed from an epoch when the universe was one-third its current scale, with wavelengths stretched by space expanding during transit"
    - "Emitting abnormally red light due to its stellar population"
  answer: 2
  explanation: "Cosmological redshift is not a Doppler effect from motion through space. A redshift of z = 2 means the universe has expanded by a factor of 3 since the photon was emitted — the photon's wavelength stretched along with space during its journey. The galaxy is not 'moving' at superluminal speeds; space between us and it expanded."

- question: "The inverse of the Hubble constant, 1/H₀, gives a rough estimate of the age of the universe."
  type: true-false
  answer: true
  explanation: "If galaxies have been receding at roughly their current rates, then 1/H₀ ≈ 14 billion years gives an order-of-magnitude age estimate. This is the Hubble time. The true age depends on how expansion has accelerated or decelerated over cosmic history, but 1/H₀ is a useful first approximation."

- question: "The cosmological redshift of distant galaxies is fundamentally the same phenomenon as the Doppler redshift of a receding ambulance siren."
  type: true-false
  answer: false
  explanation: "The Doppler effect arises from relative motion through static space. Cosmological redshift arises because space itself expands during the photon's travel, stretching the wavelength. For nearby galaxies the numerical difference is negligible, but for distant objects at high redshift the distinction is physically essential — a galaxy at z = 1 is not moving at the speed of light; space has doubled in scale since the photon was emitted."

- question: "Why does Hubble's law (v = H₀d) not imply that Earth is at the center of the universe?"
  type: short-answer
  answer: "Because in a uniformly expanding universe every observer sees all other objects receding with velocity proportional to distance. The raisin-bread analogy shows that every raisin measures the same v = H₀d relationship with all other raisins — the pattern is the same from any vantage point, so no location is privileged as the center."
  explanation: "The key insight is that uniform expansion produces the Hubble relation from any location, not just from a special center. If space is stretching uniformly, more space between two objects means faster separation — and this holds everywhere simultaneously."
```

## Explainer

From your understanding of the Doppler effect, you know that the wavelength of light shifts when the source and observer are in relative motion — blueshift for approach, redshift for recession. In the 1920s, Edwin Hubble combined Vesto Slipher's measurements of galaxy redshifts with his own distance estimates (using Cepheid variable stars in nearby galaxies) and discovered a striking pattern: the farther a galaxy is, the faster it appears to be receding. This proportionality, **v = H₀d**, is Hubble's law. The constant of proportionality, **H₀** (the Hubble constant), has units of km/s per megaparsec and is currently measured at roughly 70 km/s/Mpc — meaning a galaxy 100 Mpc away recedes at about 7,000 km/s.

The profound implication is that the universe is **expanding**. But the expansion is not galaxies flying apart through static space like shrapnel from an explosion. Instead, the fabric of space itself is stretching, carrying galaxies along with it. The classic analogy is raisins in baking bread: as the dough rises, every raisin moves away from every other raisin, and the farther apart two raisins are, the faster they separate — not because they are moving through the dough, but because more dough is expanding between them. This means there is no center of expansion. Every galaxy sees all others receding, exactly as Hubble's law predicts.

The **cosmological redshift** of distant galaxies reflects this expansion directly. A photon emitted by a distant galaxy travels through space that is stretching during the journey. The photon's wavelength stretches along with it, arriving redder than when it was emitted. This is subtly different from a classical Doppler shift, which arises from relative motion through space. For nearby galaxies the distinction is negligible, but for distant objects the cosmological interpretation is essential — a galaxy at redshift z = 1 is not "moving" at the speed of light; rather, space has doubled in scale since the photon was emitted.

Measuring H₀ precisely requires the **cosmic distance ladder**, a chain of calibrated distance indicators that bootstrap from nearby to cosmological scales. Geometric parallax works for stars within a few kiloparsecs. Cepheid variable stars — whose pulsation periods correlate with luminosity — extend the reach to tens of megaparsecs. Type Ia supernovae, which explode with a standardizable peak luminosity, reach billions of light-years. Each rung calibrates the next. Current measurements from the distance ladder (the SH0ES project) give H₀ ≈ 73 km/s/Mpc, while measurements from the cosmic microwave background (Planck satellite) give H₀ ≈ 67 km/s/Mpc. This **Hubble tension** — a statistically significant disagreement between early-universe and late-universe measurements — is one of the most active problems in modern cosmology and may point to new physics beyond the standard model.
