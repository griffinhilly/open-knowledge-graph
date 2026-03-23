---
id: longitudinal-wave-characteristics
title: Longitudinal Wave Characteristics and Properties
domain: physics
course: waves-and-optics
prerequisites:
- id: wave-motion-definition
  type: hard
builds-toward:
- sound-waves-intro
- acoustic-pressure-and-amplitude
tags:
- longitudinal-waves
- sound
- compression
stage: formal-systems
status: validated
---

# Longitudinal Wave Characteristics and Properties

## Core Idea
In longitudinal waves, particles oscillate parallel to the direction of energy propagation, creating regions of compression and rarefaction. Sound waves are the primary example, and unlike transverse waves, longitudinal waves cannot be polarized.

## Questions

```yaml
- question: "A student claims that sound waves could be polarized using a material with specially aligned structures, similar to how polarizing filters work for light. This claim is:"
  type: multiple-choice
  options:
    - "Correct — sound, like light, has oscillations that can be restricted to one plane"
    - "Incorrect — sound is longitudinal, so particle motion is already parallel to propagation with no perpendicular component to restrict"
    - "Incorrect, but only because sound moves too slowly for polarization to be practical"
    - "Correct, but only for ultrasound frequencies above 20 kHz"
  answer: 1
  explanation: "Polarization filters work by blocking one direction of transverse oscillation while passing another. But in a longitudinal wave, particle motion is already confined to the axis of propagation — there is no perpendicular oscillation to select or block. This is a fundamental geometric constraint, not a practical limitation. You cannot polarize something that has no transverse component."

- question: "In a longitudinal wave traveling horizontally to the right through air, what are the air molecules doing?"
  type: multiple-choice
  options:
    - "Moving up and down, perpendicular to the wave's travel direction"
    - "Moving left and right, parallel to the wave's travel direction"
    - "Staying stationary while pressure changes pass through"
    - "Rotating in circles around their equilibrium positions"
  answer: 1
  explanation: "The defining characteristic of a longitudinal wave is that particle displacement is parallel (not perpendicular) to the direction of energy propagation. In a sound wave in air, molecules are pushed back and forth along the same axis the wave travels — creating alternating compressions (crowded together) and rarefactions (spread apart). Option A describes transverse waves like waves on a string or light."

- question: "In a longitudinal wave, the wavelength is the distance from one compression to the next adjacent compression."
  type: true-false
  answer: true
  explanation: "The wavelength of any wave is the distance over one complete cycle. In a longitudinal wave, one complete cycle goes from one compression to the next compression (or equivalently, from one rarefaction to the next). This is exactly analogous to measuring peak-to-peak distance in a transverse wave — the same wave property, just expressed through pressure regions rather than displacement peaks."

- question: "A longitudinal wave and a transverse wave traveling through the same medium at the same frequency differ only in their propagation speed."
  type: true-false
  answer: false
  explanation: "The fundamental difference is the direction of particle oscillation relative to energy propagation, not their speeds. Transverse waves have particles oscillating perpendicular to travel; longitudinal waves have particles oscillating parallel to travel. This geometric difference leads to distinct physical properties — including the fact that transverse waves can be polarized while longitudinal waves cannot — regardless of their speeds."

- question: "Why can longitudinal waves not be polarized, while transverse waves can? What does this reveal about the fundamental difference in particle motion between the two wave types?"
  type: short-answer
  answer: "Polarization restricts particle oscillation to one specific direction within the plane perpendicular to propagation. In a transverse wave, particles oscillate perpendicular to travel, so there are multiple possible oscillation directions to choose from. In a longitudinal wave, particles oscillate parallel to the direction of travel — there is only one possible direction, already fixed by the wave's geometry. With no perpendicular dimension to restrict, the concept of polarization simply does not apply."
  explanation: "This distinction is practically important: optical polarizers exploit the two-dimensional freedom of transverse oscillation (light). No analogous device can exist for sound. It also illustrates that polarization is not a general wave property but one specific to the transverse geometry."
```

## Explainer

From your study of wave motion, you know that a wave is a disturbance that transfers energy through a medium without transporting matter. What distinguishes longitudinal waves from transverse ones is the geometry of the disturbance. In a transverse wave — like a wave on a string — particles move perpendicular to the direction of energy flow. In a **longitudinal wave**, particles move back and forth along the same direction the wave is traveling. Picture a Slinky toy stretched horizontally: if you push and pull one end back and forth horizontally, you create a longitudinal wave traveling down the Slinky's length, with the coils bunching and spreading in the same axis as wave travel.

This back-and-forth motion produces two alternating regions. A **compression** is where particles are crowded together — local pressure is higher than the equilibrium pressure. A **rarefaction** is where particles are spread apart — local pressure is lower than equilibrium. These regions travel through the medium at the wave speed, carrying energy forward. The wavelength of a longitudinal wave is the distance from one compression to the next (or one rarefaction to the next), and the amplitude is the maximum displacement of a particle from its rest position. All the standard wave properties — frequency, period, wavelength, wave speed — apply to longitudinal waves exactly as they do to transverse waves.

Sound is the most important longitudinal wave. When a speaker vibrates, it alternately compresses and rarifies the air in front of it, and those pressure fluctuations travel outward in all directions as longitudinal waves. This is why sound can travel through gases, liquids, and solids — all of which can be compressed and expanded — but cannot travel through a vacuum (there are no particles to push). The speed of sound depends on the medium's elasticity (how readily it restores equilibrium) and density: denser media are harder to set in motion, while more elastic media spring back faster. Sound travels about 343 m/s in air, about 1480 m/s in water, and much faster in steel.

The inability of longitudinal waves to be polarized follows directly from their geometry. **Polarization** restricts the direction of particle oscillation — but for a longitudinal wave, particle motion is already locked to a single direction (along the wave travel). There is no perpendicular dimension to restrict. This distinguishes sound fundamentally from light: you can polarize light (select one plane of the transverse vibration), but no such operation exists for a longitudinal wave. This property has practical implications: optical polarizers and polarized sunglasses have no acoustic equivalent, and techniques like polarimetry that exploit transverse wave geometry do not apply to sound.
