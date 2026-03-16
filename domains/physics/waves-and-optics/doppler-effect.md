---
id: doppler-effect
title: The Doppler Effect
domain: physics
course: waves-and-optics
prerequisites:
- id: sound-waves-intro
  type: hard
- id: wave-speed-medium
  type: hard
- id: sound-intensity-and-decibels
  type: soft
- id: trigonometric-functions-and-graphs
  type: soft
tags:
- Doppler
- frequency shift
- moving source
- moving observer
- redshift
stage: abstract-reasoning
status: validated
---
# The Doppler Effect

## Core Idea
When a wave source or observer moves relative to the medium, the observed frequency differs from the emitted frequency. For a source moving toward an observer, wavefronts pile up, increasing observed frequency (higher pitch); motion away decreases it. The general formula is f_obs = f_s × (v ± v_obs)/(v ∓ v_s), where v is wave speed, v_obs the observer speed, and v_s the source speed. This applies to sound, light (as redshift/blueshift), and any wave phenomenon.

## How It's Best Learned
Listen to a passing ambulance siren and describe the pitch change qualitatively, then work through the formula quantitatively for a car horn. Discuss astronomical redshift as the light analog.

## Common Misconceptions
- The Doppler effect changes frequency, not wave speed.
- Sign conventions in the formula are often misapplied; always define the positive direction consistently as 'toward' the other party.

## Explainer

You already know that sound travels as a longitudinal wave with a fixed speed through a medium. When a source is stationary, it sends out wavefronts at equal spacing in all directions, and every observer hears the same frequency. The **Doppler effect** is what happens when that symmetry breaks — when source or observer is moving relative to the medium. The key insight is that motion compresses or stretches the spacing between wavefronts, and observed frequency depends entirely on that spacing.

Picture an ambulance driving toward you, horn blaring. As the ambulance advances, each successive wavefront is emitted from a position slightly closer to you than the previous one. The wavefronts pile up — the distance between them shrinks — and you receive them more frequently than they were emitted. Pitch goes up. Behind the ambulance, wavefronts are stretched apart, and you receive them less frequently. Pitch falls. When the ambulance passes, you hear that characteristic pitch drop — not because the source frequency changes, but because the geometry of wavefront compression reverses in an instant.

The formula f_obs = f_s × (v ± v_obs) / (v ∓ v_s) captures this precisely. The signs are the trickiest part. For the numerator: if the **observer moves toward** the source, wavefronts arrive faster, so add v_obs (use +). For the denominator: if the **source moves toward** the observer, wavefronts are compressed into a shorter wavelength, so subtract v_s (use −), which makes the fraction larger. A reliable mnemonic: motion that brings source and observer closer together increases frequency; motion that separates them decreases it. Apply this physical logic first, then let the sign follow. Note that the effect is not symmetric — a moving source and a moving observer at the same relative speed produce slightly different frequency shifts, because compressing wavefronts (moving source) is geometrically different from intercepting them faster (moving observer).

The Doppler effect applies to all waves, not just sound. Light undergoes Doppler shifting too, though the relativistic formula replaces the classical one at high speeds. When distant galaxies recede from Earth, their light is **redshifted** — frequencies shift toward the lower end of the spectrum — providing the observational cornerstone of cosmic expansion. The same principle powers police radar guns, weather Doppler radar, and medical ultrasound imaging of blood flow. Grasping the conceptual core — motion compresses or stretches wavefronts — gives you immediate access to all of these applications without memorizing each separately.
