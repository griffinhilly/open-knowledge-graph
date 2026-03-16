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

## Explainer

From simple harmonic motion, you know what happens to a single mass on a spring: it oscillates back and forth around equilibrium, with position described by a sinusoidal function of time. A wave is what happens when you connect many such oscillators together — each one coupled to its neighbors. When you disturb one particle, it pulls on the next, which pulls on the next, and the disturbance travels through the medium as a wave. The crucial insight is that each individual particle stays near its home position; it is the *pattern* of displacement — the disturbance — that moves. A leaf on a pond bobs up and down as a water wave passes beneath it, but it does not travel with the wave across the pond. **Energy propagates; matter does not.**

The two main classifications follow from asking which direction the particles oscillate relative to the direction the wave travels. In a **transverse wave**, particles move perpendicular to the direction of propagation — shake a rope sideways and the disturbance travels along the rope while each bit of rope moves up and down. Light is a transverse electromagnetic wave. In a **longitudinal wave**, particles oscillate parallel to the direction of propagation — a compression travels through air as alternating regions of high pressure (compressions) and low pressure (rarefactions), with air molecules moving back and forth along the direction the sound is heading. Sound is a longitudinal wave. Some waves, like waves on the surface of water, have both components simultaneously.

The mathematical description builds directly on what you know from periodic functions. A sinusoidal wave traveling in the positive x-direction can be written y(x,t) = A sin(kx − ωt), where A is the **amplitude**, k = 2π/λ is the **wave number** (spatial frequency), and ω = 2πf is the **angular frequency**. These parameters are connected by the wave speed: v = ω/k = fλ. The wave speed depends on the medium (tension and density for a string; bulk modulus and density for sound), not on the frequency or amplitude of the wave. This independence of speed from frequency is what makes wave communication possible — different frequencies travel together without dispersing (in non-dispersive media).

Understanding wave motion as coupled oscillators also explains why superposition works so naturally: if the medium responds linearly (each particle's restoring force is proportional to its displacement), then two independent disturbances simply add without affecting each other. This connects directly to the interference and diffraction phenomena you will study next, which all depend on waves being able to occupy the same space and have their displacements combine algebraically.
