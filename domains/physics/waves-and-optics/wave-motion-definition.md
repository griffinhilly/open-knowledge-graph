---
id: wave-motion-definition
title: 'Wave Motion: Definition and Classification'
domain: physics
course: waves-and-optics
prerequisites:
- id: simple-harmonic-motion
  type: hard
- id: periodic-functions
  type: soft
builds-toward:
- transverse-wave-characteristics
- longitudinal-wave-characteristics
tags:
- wave-basics
- oscillation
- propagation
stage: formal-systems
status: draft
---

# Wave Motion: Definition and Classification

## Core Idea
A wave is a disturbance that propagates through a medium by transferring energy without permanently displacing the medium itself. Waves are classified by particle motion direction (transverse vs. longitudinal) and by dimensionality, with all waves obeying principles of superposition and interference.

## Questions

```yaml
- question: "A leaf floats on the surface of a still pond. When a wave passes beneath it, what does the leaf do?"
  type: multiple-choice
  options:
    - "It bobs up and down approximately in place — water particles oscillate without traveling in the direction of the wave"
    - "It moves steadily in the direction the wave is traveling, carried by the wave's momentum across the pond"
    - "It moves perpendicular to the wave's direction of travel, swept sideways by particle motion"
    - "It remains completely stationary, since surface waves do not disturb floating objects"
  answer: 0
  explanation: "This is the central insight of wave motion: energy propagates, matter does not. Each water particle at the surface moves in a roughly circular or up-and-down path near its equilibrium position as the wave passes — the particle does not travel with the disturbance. The leaf bobs up and down but ends up roughly where it started. Option B is the most common misconception: students confuse the direction of wave propagation with the direction of particle motion, imagining that matter flows along with the wave."

- question: "Sound is a longitudinal wave traveling through air. What does this classification tell us about how air molecules move?"
  type: multiple-choice
  options:
    - "Air molecules oscillate back and forth parallel to the direction the sound travels, creating alternating compressions and rarefactions"
    - "Air molecules oscillate perpendicular to the direction the sound travels, like a rope shaken sideways"
    - "Air molecules travel from the sound source to the listener, carrying kinetic energy with them"
    - "Air molecules do not move at all — only pressure values change propagate through the medium"
  answer: 0
  explanation: "In a longitudinal wave, particle displacement is parallel to the direction of propagation — the defining characteristic. Air molecules get pushed back and forth along the direction the sound is heading, creating regions of high pressure (compressions) and low pressure (rarefactions). This contrasts with transverse waves (like light or a shaken rope), where particle motion is perpendicular to propagation. Option C is the wave-as-matter-flow misconception: molecules don't travel from source to listener; the disturbance pattern does."

- question: "In a wave, energy is transported through a medium without the medium itself being permanently displaced in the direction of propagation."
  type: true-false
  answer: true
  explanation: "This is the defining property of wave motion. Each particle in the medium oscillates around its equilibrium position as the wave passes, but returns to approximately where it started. The disturbance — the pattern of displacement — moves through the medium, carrying energy with it, while the matter stays put. This is what distinguishes wave propagation from bulk flow (like wind or current), where matter actually moves from one place to another."

- question: "The speed at which a wave travels through a medium depends primarily on the wave's amplitude — larger disturbances travel faster."
  type: true-false
  answer: false
  explanation: "Wave speed depends on properties of the medium, not on the amplitude or frequency of the wave. For a string, wave speed depends on tension and linear density; for sound in air, it depends on bulk modulus and density; for light in a vacuum, it is the constant c. Amplitude affects how much energy the wave carries, not how fast it travels. This independence of speed from amplitude and frequency (in non-dispersive media) is what makes wave communication reliable — a complex signal composed of many frequencies travels intact without the components arriving at different times."

- question: "A cork bobs up and down as ocean waves pass beneath it but does not travel toward shore. What does this tell us about what waves actually transport?"
  type: short-answer
  answer: "The cork's behavior shows that waves transport energy, not matter. The water molecules beneath the cork oscillate around their equilibrium positions as each wave passes, temporarily displacing the cork upward and downward, but they do not travel in the direction of wave propagation. Since the cork (which rides on the water surface) does not move toward shore, the water molecules themselves are not flowing shoreward. What moves is the pattern of displacement — the disturbance — which carries energy from the wave source across the ocean without the water itself making that journey."
  explanation: "This is the key conceptual distinction between wave motion and bulk flow. Ocean currents involve water actually flowing from one place to another; waves do not. A student who pictures waves as 'moving water' will misunderstand most wave phenomena — interference, reflection, the independence of wave speed from amplitude. The cork thought experiment isolates this principle cleanly."
```

## Explainer

From simple harmonic motion, you know what happens to a single mass on a spring: it oscillates back and forth around equilibrium, with position described by a sinusoidal function of time. A wave is what happens when you connect many such oscillators together — each one coupled to its neighbors. When you disturb one particle, it pulls on the next, which pulls on the next, and the disturbance travels through the medium as a wave. The crucial insight is that each individual particle stays near its home position; it is the *pattern* of displacement — the disturbance — that moves. A leaf on a pond bobs up and down as a water wave passes beneath it, but it does not travel with the wave across the pond. **Energy propagates; matter does not.**

The two main classifications follow from asking which direction the particles oscillate relative to the direction the wave travels. In a **transverse wave**, particles move perpendicular to the direction of propagation — shake a rope sideways and the disturbance travels along the rope while each bit of rope moves up and down. Light is a transverse electromagnetic wave. In a **longitudinal wave**, particles oscillate parallel to the direction of propagation — a compression travels through air as alternating regions of high pressure (compressions) and low pressure (rarefactions), with air molecules moving back and forth along the direction the sound is heading. Sound is a longitudinal wave. Some waves, like waves on the surface of water, have both components simultaneously.

The mathematical description builds directly on what you know from periodic functions. A sinusoidal wave traveling in the positive x-direction can be written y(x,t) = A sin(kx − ωt), where A is the **amplitude**, k = 2π/λ is the **wave number** (spatial frequency), and ω = 2πf is the **angular frequency**. These parameters are connected by the wave speed: v = ω/k = fλ. The wave speed depends on the medium (tension and density for a string; bulk modulus and density for sound), not on the frequency or amplitude of the wave. This independence of speed from frequency is what makes wave communication possible — different frequencies travel together without dispersing (in non-dispersive media).

Understanding wave motion as coupled oscillators also explains why superposition works so naturally: if the medium responds linearly (each particle's restoring force is proportional to its displacement), then two independent disturbances simply add without affecting each other. This connects directly to the interference and diffraction phenomena you will study next, which all depend on waves being able to occupy the same space and have their displacements combine algebraically.
