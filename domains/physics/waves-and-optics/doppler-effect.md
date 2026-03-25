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
- id: graphing-sine-and-cosine
  type: soft
tags:
- Doppler
- frequency shift
- moving source
- moving observer
- redshift
stage: advanced
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

## Questions

```yaml
- question: "An ambulance moving toward you at 30 m/s sounds its horn. The speed of sound is 340 m/s. Compared to the emitted frequency, the sound you hear is:"
  type: multiple-choice
  options:
    - "Higher frequency, because the sound waves travel faster toward you when the source moves"
    - "Higher frequency, because the wavefronts pile up — each successive crest is emitted closer to you, shortening the wavelength you receive"
    - "The same frequency — only the amplitude increases as the ambulance approaches"
    - "Lower frequency, because the ambulance 'chases' the waves and cancels some of them out"
  answer: 1
  explanation: "The Doppler effect arises from wavefront compression, not from any change in wave speed. As the ambulance advances toward you, each successive crest is emitted from a position slightly closer to you than the previous one. This shortens the effective wavelength in the forward direction, so you receive crests more frequently than they are emitted — higher observed frequency. The wave speed through the medium (air) is unchanged; it depends on the medium's properties, not the source's motion. Option A describes a common misconception: the speed of sound is determined by the air, not by the source."

- question: "A source moves toward a stationary observer at speed v_s. A stationary source faces an observer moving toward it at the same speed v_s. Are the observed frequency shifts identical?"
  type: multiple-choice
  options:
    - "Yes — relative motion is all that matters, so the frequency shifts are identical"
    - "No — a moving source compresses wavefronts in the medium, while a moving observer intercepts existing wavefronts at a higher rate; these are geometrically different effects and produce slightly different shifts"
    - "No — the moving observer effect always produces a larger shift than the moving source"
    - "Yes — the Doppler formula is symmetric in v_s and v_obs by construction"
  answer: 1
  explanation: "This is the key subtlety of the classical (non-relativistic) Doppler effect: the asymmetry between a moving source and a moving observer. A moving source physically compresses the wavefronts in the medium, changing the wavelength. A moving observer intercepts the existing wavefronts at a higher rate but the wavelength in the medium is unchanged. These are different mechanisms that happen to produce similar (but not identical) results at the same relative speed. Using the formula f_obs = f_s(v ± v_obs)/(v ∓ v_s): if v_s = v_obs = u, the two cases give f_obs = f_s(v + u)/v vs. f_s · v/(v − u), which are different values. Note: for light, the relativistic Doppler formula does depend only on relative velocity."

- question: "When a moving sound source approaches an observer, the speed of sound increases because the source's motion adds to the wave's velocity."
  type: true-false
  answer: false
  explanation: "False — this is one of the most common misconceptions about the Doppler effect. The speed of sound is a property of the medium (air), determined by air pressure, density, and temperature. It is completely unaffected by the motion of the source. What the source's motion does change is the spacing between wavefronts — wavefronts pile up ahead of the moving source and spread out behind it. This changes the wavelength and therefore the frequency observed, but never the wave speed. This is what distinguishes the Doppler effect from, say, a supersonic shock wave, where the source exceeds the wave speed entirely."

- question: "The Doppler effect produces a change in observed frequency, not a change in the speed of the waves through the medium."
  type: true-false
  answer: true
  explanation: "True. Wave speed through a medium depends on the medium's physical properties, not on source or observer motion. The Doppler effect works by changing the geometry of wavefront arrival: a moving source compresses or stretches the spacing between wavefronts (changing wavelength), and a moving observer intercepts those wavefronts at a higher or lower rate (changing observed frequency). In both cases, the wave speed in the medium remains constant at v = fλ, where f and λ adjust together to preserve this relationship."

- question: "Explain conceptually why a source moving toward a stationary observer produces a different frequency shift than an observer moving toward a stationary source at the same speed, even though the relative velocities are equal."
  type: short-answer
  answer: "When the source moves, it physically alters the wavefront pattern in the medium: each successive crest is emitted from a position closer to the observer, so the wavelength in the air between source and observer is compressed. The observer then receives this compressed wavelength at the fixed wave speed v, resulting in higher frequency. When the observer moves toward the source, the wavelength in the medium is unchanged — the source is stationary, so it emits crests at normal spacing. What changes is only how quickly the observer intercepts those crests, because moving toward the source reduces the time between encounters. The formula reflects this: in one case the denominator changes (v − v_s), in the other the numerator changes (v + v_obs). At the same numerical speed, these produce different ratios and thus different observed frequencies."
  explanation: "This asymmetry is a feature of the classical wave Doppler effect, not a flaw. It disappears in special relativity for light (where only relative velocity matters), which is actually a deeper clue that the classical Doppler's asymmetry arises from the existence of a privileged medium (air) for the wave to propagate in."
```

## Explainer

You already know that sound travels as a longitudinal wave with a fixed speed through a medium. When a source is stationary, it sends out wavefronts at equal spacing in all directions, and every observer hears the same frequency. The **Doppler effect** is what happens when that symmetry breaks — when source or observer is moving relative to the medium. The key insight is that motion compresses or stretches the spacing between wavefronts, and observed frequency depends entirely on that spacing.

Picture an ambulance driving toward you, horn blaring. As the ambulance advances, each successive wavefront is emitted from a position slightly closer to you than the previous one. The wavefronts pile up — the distance between them shrinks — and you receive them more frequently than they were emitted. Pitch goes up. Behind the ambulance, wavefronts are stretched apart, and you receive them less frequently. Pitch falls. When the ambulance passes, you hear that characteristic pitch drop — not because the source frequency changes, but because the geometry of wavefront compression reverses in an instant.

The formula f_obs = f_s × (v ± v_obs) / (v ∓ v_s) captures this precisely. The signs are the trickiest part. For the numerator: if the **observer moves toward** the source, wavefronts arrive faster, so add v_obs (use +). For the denominator: if the **source moves toward** the observer, wavefronts are compressed into a shorter wavelength, so subtract v_s (use −), which makes the fraction larger. A reliable mnemonic: motion that brings source and observer closer together increases frequency; motion that separates them decreases it. Apply this physical logic first, then let the sign follow. Note that the effect is not symmetric — a moving source and a moving observer at the same relative speed produce slightly different frequency shifts, because compressing wavefronts (moving source) is geometrically different from intercepting them faster (moving observer).

The Doppler effect applies to all waves, not just sound. Light undergoes Doppler shifting too, though the relativistic formula replaces the classical one at high speeds. When distant galaxies recede from Earth, their light is **redshifted** — frequencies shift toward the lower end of the spectrum — providing the observational cornerstone of cosmic expansion. The same principle powers police radar guns, weather Doppler radar, and medical ultrasound imaging of blood flow. Grasping the conceptual core — motion compresses or stretches wavefronts — gives you immediate access to all of these applications without memorizing each separately.
