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
stage: formal-systems
status: draft
---

# Doppler Effect: Complete Analysis for Moving Source and Observer

## Core Idea
The observed frequency when source and observer move is f' = f(v ± vₒ)/(v ∓ vₛ), where v is wave speed, vₒ observer velocity, vₛ source velocity, and signs depend on relative motion directions. This general formula unifies all Doppler shift scenarios including astrophysical and medical applications.

## Explainer

You've already encountered the Doppler effect in simpler cases — a moving source compresses wavefronts ahead of it and stretches them behind. Now you need the full formula that handles both a moving source and a moving observer simultaneously: f′ = f(v ± vₒ)/(v ∓ vₛ). Let's build up to it from physical reasoning rather than just memorizing the signs.

Start with a stationary source and a moving observer. If you run toward a sound source, you intercept wavefronts more frequently than if you stood still — you're covering the distance between wavefronts faster. If the wave speed in the medium is v and the observer moves toward the source at vₒ, the effective approach speed is v + vₒ, so the observed frequency is f′ = f(v + vₒ)/v. Moving away gives f′ = f(v − vₒ)/v. The observer speed changes the **numerator**. Now flip it: stationary observer, moving source. A source moving toward you at vₛ compresses each successive wavefront because it has caught up slightly since the last one. The wavelength ahead is shortened to λ′ = (v − vₛ)/f, so the observed frequency is f′ = v/λ′ = fv/(v − vₛ). Moving away stretches the wavelength: f′ = fv/(v + vₛ). The source speed changes the **denominator**.

Combining both effects gives the general formula. The sign convention is the tricky part, and it's worth anchoring with a physical rule: choose signs so that motion bringing source and observer closer together produces a higher observed frequency (blueshift), and motion increasing the gap produces a lower frequency (redshift). Toward each other: f′ = f(v + vₒ)/(v − vₛ). Away from each other: f′ = f(v − vₒ)/(v + vₛ). Mixed cases (one toward, one away) combine the appropriate signs in numerator and denominator. The asymmetry between numerator and denominator is real — it reflects the asymmetry between moving the source (which physically changes the wavelength) and moving the observer (which changes only the rate of wavefront encounters, not the wavelength).

The applications of this formula span astronomy to medicine. **Redshift** in astronomy: light from distant galaxies is shifted toward longer wavelengths, revealing that the universe is expanding. Hubble's law came from measuring these Doppler-like shifts. **Radar and Doppler weather imaging**: a transmitted radio wave reflects off a moving target (a raindrop, a car), and the returned frequency reveals the target's velocity. **Medical ultrasound**: ultrasound bounces off moving blood cells, and the frequency shift reveals blood flow speed and direction — a non-invasive way to detect blocked arteries. In each case, the same formula applies: measure the shift, calculate the velocity.

One important boundary condition: the formula breaks down when vₛ approaches v, the wave speed in the medium. The denominator approaches zero, meaning the wavefronts pile up into a **shock wave** — the sonic boom created by supersonic aircraft or the bow wave of a fast boat. That regime requires different analysis. But for all sub-sonic relative motions, the Doppler formula gives precise, testable predictions that connect wave physics directly to real-world measurement.
