---
id: sound-waves-longitudinal
title: Sound Waves and Longitudinal Propagation
domain: physics
course: waves-and-optics
prerequisites:
- id: transverse-and-longitudinal-waves
  type: hard
- id: wavelength-frequency-speed-relationship
  type: hard
builds-toward:
- doppler-shift-observer-motion
- acoustic-resonance-pipes
tags:
- sound
- longitudinal
- compression
stage: formal-systems
status: draft
---

# Sound Waves and Longitudinal Propagation

## Core Idea
Sound travels as longitudinal pressure waves, with particles oscillating parallel to the direction of wave propagation. Sound speed depends on the medium's properties (density and elasticity), not on frequency or amplitude. In air at 20°C, sound travels at ~343 m/s; in water it's ~1480 m/s due to higher elasticity.

## Questions

```yaml
- question: "A bass note (low frequency, 80 Hz) and a treble note (high frequency, 4000 Hz) are played simultaneously from a speaker 100 meters away. Which arrives first?"
  type: multiple-choice
  options:
    - "The treble note — higher frequency waves travel faster through air"
    - "The bass note — lower frequency waves travel faster through air"
    - "They arrive at the same time — sound speed in air depends on the medium, not frequency"
    - "The treble note — shorter wavelength means the wave completes its journey in fewer cycles"
  answer: 2
  explanation: "Sound speed in air (~343 m/s at 20°C) is a property of the medium — its density and bulk modulus — not of the source's frequency. Both notes travel at the same speed and arrive simultaneously. Option D reflects a common confusion: shorter wavelength at the same speed means more oscillations per second (higher frequency), not faster travel. The relationship v = fλ shows that if v is fixed and f increases, λ decreases proportionally — the speed itself doesn't change."

- question: "Sound travels about four times faster in water (~1480 m/s) than in air (~343 m/s), even though water is much denser. What explains this?"
  type: multiple-choice
  options:
    - "Water molecules are more tightly packed, allowing direct physical contact transmission"
    - "Water's bulk modulus (resistance to compression) is far higher than air's, and this effect dominates over its greater density"
    - "Sound travels as a transverse wave in water, which propagates faster than the longitudinal mode in air"
    - "Water's higher temperature at depth accelerates sound, raising the average speed"
  answer: 1
  explanation: "Sound speed v = √(B/ρ) depends on bulk modulus B (stiffness) and density ρ. Water has higher density than air (which would slow sound), but its bulk modulus is vastly higher — water resists compression far more strongly. The stiffness effect dominates: sound is transmitted so much more efficiently through water's strong intermolecular bonds that it travels ~4× faster despite the density penalty. Option C is wrong: sound is longitudinal in both water and air."

- question: "A louder sound (greater amplitude) travels faster through the same medium than a quiet sound at the same frequency."
  type: true-false
  answer: false
  explanation: "Amplitude measures the intensity of the pressure variation — how far above and below atmospheric pressure the compressions and rarefactions are. It determines loudness but has no effect on propagation speed. Speed depends only on medium properties (bulk modulus and density). A whisper and a shout in the same room travel at the same ~343 m/s. Students often assume a 'bigger' wave must move faster, but the restoring force and inertia of the medium are unchanged by amplitude."

- question: "Sound waves require a medium to propagate because they depend on the physical displacement of particles in that medium."
  type: true-false
  answer: true
  explanation: "Sound propagates by alternating compression and rarefaction of medium particles — each particle pushes its neighbor. Without particles, there is nothing to compress and rarefy. This is why sound cannot travel through a vacuum (light, an electromagnetic wave, can). The classic demonstration: a ringing bell inside an evacuated jar becomes inaudible as air is removed, even though the bell still vibrates. The mechanism is purely mechanical — particle displacement is the wave itself."

- question: "Why does sound travel faster in warm air than in cold air, even though neither frequency nor amplitude has changed?"
  type: short-answer
  answer: "Temperature increases the bulk modulus of air: warmer air has more energetically moving molecules that resist compression more elastically, effectively increasing the medium's stiffness. Since v = √(B/ρ) and bulk modulus increases with temperature while density slightly decreases (warmer air expands), both effects raise speed. In practice, sound speed in air increases by about 0.6 m/s per 1°C rise. Frequency and amplitude are properties of the source, not the medium — changing them doesn't change propagation speed."
  explanation: "This illustrates the key principle: sound speed is a property of the medium, not the source. Warm the medium and speed changes; change only the source (louder, higher pitch) and speed stays the same. The same principle explains why you hear thunder after seeing lightning: light arrives nearly instantly, but sound travels at a fixed medium-dependent speed, so the delay directly measures distance."
```

## Explainer

From your study of wave types, you know the key distinction: in a **transverse** wave, the medium oscillates perpendicular to the wave's travel direction (like a rope wave), while in a **longitudinal** wave, the medium oscillates parallel to the travel direction. Sound is longitudinal. A vibrating speaker cone pushes on the air molecules directly in front of it, creating a region of slightly higher pressure — a **compression**. Those molecules then push on their neighbors, which push on their neighbors, and so on. Behind the initial compression, molecules spread apart into a **rarefaction** (lower pressure). The result is a pressure disturbance that propagates outward even though no individual air molecule travels the full distance — each one just oscillates back and forth around its equilibrium position.

You also know from the wave equation v = fλ that wave speed, frequency, and wavelength are linked. For sound, this relationship holds, but the speed v is set entirely by the **medium** — not by the frequency or amplitude of the source. Sound speed depends on two competing properties: the **bulk modulus** (how strongly the medium resists compression — a higher modulus means faster transmission) and the **density** (how much mass must be accelerated — higher density slows transmission). Mathematically, v = √(B/ρ), where B is the bulk modulus and ρ is density. Water has both higher bulk modulus and higher density than air, but the modulus effect dominates, which is why sound travels about four times faster in water (~1480 m/s) than in air (~343 m/s).

Temperature affects sound speed because it affects the bulk modulus of a gas. Warmer air has faster-moving molecules and resists compression more elastically, so sound travels faster: in air, roughly +0.6 m/s per degree Celsius rise. This explains a familiar experience: you see a lightning bolt essentially instantaneously (light arrives in microseconds), but you hear the thunder about 3 seconds later per kilometer of distance. The delay is pure sound travel time, and knowing the speed of sound lets you estimate how far away the storm is. Frequency and amplitude change what you hear (pitch and loudness), but they don't change the propagation speed — that is entirely a property of the medium.

