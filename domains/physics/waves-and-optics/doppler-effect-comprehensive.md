---
id: doppler-effect-comprehensive
title: 'Doppler Effect: Complete Analysis for Moving Source and Observer'
domain: physics
course: waves-and-optics
prerequisites:
- id: doppler-effect
  type: soft
- id: doppler-shift-source-motion
  type: soft
builds-toward:
- doppler-applications-astronomy
tags:
- doppler-effect
- frequency-shift
- relative-motion
stage: advanced
status: validated
---

# Doppler Effect: Complete Analysis for Moving Source and Observer

## Core Idea
The observed frequency when source and observer move is f' = f(v ± vₒ)/(v ∓ vₛ), where v is wave speed, vₒ observer velocity, vₛ source velocity, and signs depend on relative motion directions. This general formula unifies all Doppler shift scenarios including astrophysical and medical applications.

## Questions

```yaml
- question: "A train (source) moves toward you at 30 m/s and sounds its horn at 400 Hz. You walk toward the train at 2 m/s. Using v = 340 m/s, what is the observed frequency?"
  type: multiple-choice
  options:
    - "f' = 400 × (340 − 2)/(340 − 30) ≈ 437 Hz (observer away subtracts; source toward subtracts)"
    - "f' = 400 × (340 + 2)/(340 + 30) ≈ 369 Hz (student treats both motions as additive in the same direction)"
    - "f' = 400 × (340 + 2)/(340 − 30) ≈ 441 Hz (observer toward adds in numerator; source toward subtracts in denominator)"
    - "f' = 400 × (340)/(340 − 30) ≈ 439 Hz (only source motion enters the formula)"
  answer: 2
  explanation: "Observer moving toward source adds to the numerator (v + vₒ = 342); source moving toward observer subtracts from the denominator (v − vₛ = 310). Result: 400 × 342/310 ≈ 441 Hz. The common errors are option B (treating both as simple additions, ignoring the numerator/denominator asymmetry) and option D (forgetting that observer motion also enters the formula). The key is knowing which quantity each velocity affects."

- question: "A source moves toward you at speed vₛ. You move toward the source at the same speed vₛ. Are the contributions of these two motions to the observed frequency equal?"
  type: multiple-choice
  options:
    - "Yes — since both motions bring source and observer closer at the same rate, the Doppler shifts are equal and can be added symmetrically"
    - "No — source motion physically shortens the wavelength in the medium (denominator effect), while observer motion only increases the rate of wavefront encounters without changing the wavelength (numerator effect); they produce different frequency shifts even for equal speeds"
    - "Yes, but only when both speeds are much smaller than the wave speed v"
    - "No — observer motion has no effect on observed frequency; only source motion matters"
  answer: 1
  explanation: "The asymmetry is real and physical. A moving source compresses wavefronts ahead of it — the wavelength in the medium changes. A moving observer just intercepts those existing wavefronts faster, without altering the wavelength. For a source moving at vₛ: f' = fv/(v − vₛ). For an observer moving at the same speed vₒ = vₛ: f' = f(v + vₒ)/v = f(v + vₛ)/v. These are different numbers. Equal approach speeds do not produce equal frequency shifts."

- question: "Source velocity appears in the Dopinator of the Doppler formula because a moving source physically changes the wavelength of waves in the medium."
  type: true-false
  answer: true
  explanation: "As the source moves toward the observer, each successive wavefront is emitted from a position slightly closer to the observer than the last, compressing the wavelength to λ' = (v − vₛ)/f. This physically altered wavelength is what the observer detects. The denominator v − vₛ in f' = fv/(v − vₛ) encodes this compressed wavelength. Observer motion, by contrast, changes how fast the observer sweeps through the unaltered wavefronts — a numerator effect."

- question: "The classical Doppler formula f' = f(v ± vₒ)/(v ∓ vₛ) applies equally well to light (electromagnetic waves) from distant galaxies as to sound waves."
  type: true-false
  answer: false
  explanation: "The classical Doppler formula is derived for waves that require a medium (like sound). It depends on the velocities of source and observer relative to that medium. Light in vacuum has no medium, and velocities must be treated relativistically. The relativistic Doppler formula for light depends only on the relative velocity between source and observer, not on each velocity relative to a medium. For sound at everyday speeds the classical formula is accurate; for light or for sources moving at a significant fraction of c, the relativistic formula is required."

- question: "Explain in physical terms why a moving source and a moving observer produce asymmetric contributions to the observed Doppler shift — specifically, why source velocity appears in the denominator and observer velocity in the numerator."
  type: short-answer
  answer: "A moving source changes the physical wavelength in the medium: because the source moves between emitting successive wavefronts, each wavefront is laid down at a different position, compressing (or stretching) the spacing between them. The observer then detects this modified wavelength. A moving observer does not change the wavelength — the wavefronts are still spaced as laid down by the source — but the observer intercepts them at a higher (or lower) rate depending on relative motion. Source motion affects the denominator because wavelength λ = (v ± vₛ)/f and f' = v/λ'. Observer motion affects the numerator because f' = (v ± vₒ)/λ."
  explanation: "A useful way to remember: source motion → medium is disturbed, wavelength changes → denominator. Observer motion → medium is undisturbed, encounter rate changes → numerator. This asymmetry is a key conceptual point that distinguishes the Doppler effect from a situation of pure relative motion (which would be symmetric), and it foreshadows why the relativistic Doppler formula for light — where there is no medium — takes a different form."
```

## Explainer

You've already encountered the Doppler effect in simpler cases — a moving source compresses wavefronts ahead of it and stretches them behind. Now you need the full formula that handles both a moving source and a moving observer simultaneously: f′ = f(v ± vₒ)/(v ∓ vₛ). Let's build up to it from physical reasoning rather than just memorizing the signs.

Start with a stationary source and a moving observer. If you run toward a sound source, you intercept wavefronts more frequently than if you stood still — you're covering the distance between wavefronts faster. If the wave speed in the medium is v and the observer moves toward the source at vₒ, the effective approach speed is v + vₒ, so the observed frequency is f′ = f(v + vₒ)/v. Moving away gives f′ = f(v − vₒ)/v. The observer speed changes the **numerator**. Now flip it: stationary observer, moving source. A source moving toward you at vₛ compresses each successive wavefront because it has caught up slightly since the last one. The wavelength ahead is shortened to λ′ = (v − vₛ)/f, so the observed frequency is f′ = v/λ′ = fv/(v − vₛ). Moving away stretches the wavelength: f′ = fv/(v + vₛ). The source speed changes the **denominator**.

Combining both effects gives the general formula. The sign convention is the tricky part, and it's worth anchoring with a physical rule: choose signs so that motion bringing source and observer closer together produces a higher observed frequency (blueshift), and motion increasing the gap produces a lower frequency (redshift). Toward each other: f′ = f(v + vₒ)/(v − vₛ). Away from each other: f′ = f(v − vₒ)/(v + vₛ). Mixed cases (one toward, one away) combine the appropriate signs in numerator and denominator. The asymmetry between numerator and denominator is real — it reflects the asymmetry between moving the source (which physically changes the wavelength) and moving the observer (which changes only the rate of wavefront encounters, not the wavelength).

The applications of this formula span astronomy to medicine. **Redshift** in astronomy: light from distant galaxies is shifted toward longer wavelengths, revealing that the universe is expanding. Hubble's law came from measuring these Doppler-like shifts. **Radar and Doppler weather imaging**: a transmitted radio wave reflects off a moving target (a raindrop, a car), and the returned frequency reveals the target's velocity. **Medical ultrasound**: ultrasound bounces off moving blood cells, and the frequency shift reveals blood flow speed and direction — a non-invasive way to detect blocked arteries. In each case, the same formula applies: measure the shift, calculate the velocity.

One important boundary condition: the formula breaks down when vₛ approaches v, the wave speed in the medium. The denominator approaches zero, meaning the wavefronts pile up into a **shock wave** — the sonic boom created by supersonic aircraft or the bow wave of a fast boat. That regime requires different analysis. But for all sub-sonic relative motions, the Doppler formula gives precise, testable predictions that connect wave physics directly to real-world measurement.
