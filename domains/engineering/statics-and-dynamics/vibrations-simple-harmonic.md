---
id: vibrations-simple-harmonic
title: Simple Harmonic Motion and Natural Frequency
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: energy-conservation-methods
  type: hard
- id: rotation-fixed-axis-dynamics
  type: soft
- id: simple-harmonic-motion
  type: hard
builds-toward:
- vibrations-damped-forced
tags:
- simple-harmonic
- shm
- natural-frequency
- oscillation
stage: formal-systems
status: draft
---

# Simple Harmonic Motion and Natural Frequency

## Core Idea
Simple harmonic motion occurs when a restoring force is proportional to displacement: F = -kx or τ = -kθ. The resulting motion is sinusoidal with period T = 2π/ω_n, where ω_n = √(k/m) for translation or ω_n = √(k/I) for rotation. Energy oscillates between kinetic and potential forms while total energy remains constant. The natural frequency defines the system's tendency to oscillate at a particular rate.

## Explainer

The defining feature of simple harmonic motion is the **linear restoring force**: a force (or torque) that always points back toward equilibrium and whose magnitude is exactly proportional to how far you've displaced the system. A spring satisfies this: stretch it by x, and it pulls back with force F = −kx. The minus sign is the whole story — the force opposes the displacement. If you displace a mass on a spring and release it, Newton's second law gives mẍ = −kx, which is a second-order linear ODE whose solution is x(t) = A cos(ω_n t + φ). The motion is exactly sinusoidal, oscillating forever with constant amplitude. You already know from energy conservation that a closed system conserves total mechanical energy; SHM is simply the case where all that energy alternates between the spring's potential energy (½kx²) and the mass's kinetic energy (½mv²), with the total sum remaining constant at every instant.

The **natural frequency** ω_n = √(k/m) tells you how fast the system oscillates. Notice its structure: k appears in the numerator and m in the denominator. A stiffer spring (larger k) increases the restoring force at every displacement, causing faster oscillations. A heavier mass (larger m) has more inertia and overshoots equilibrium more slowly. The natural frequency is entirely set by the system's physical parameters — it is not something you impose from outside. Every spring-mass system has exactly one natural frequency, and it will oscillate at that frequency if given any initial displacement or velocity, regardless of amplitude (for small oscillations). This amplitude-independence is a special and important property of SHM that does not hold for nonlinear restoring forces.

For rotational systems, the same logic applies with moment of inertia I replacing mass m and torsional stiffness k replacing linear stiffness: ω_n = √(k/I). A simple pendulum, for small angles, approximates SHM with an effective stiffness k_eff = mg/L, giving ω_n = √(g/L). Notice that the pendulum's natural frequency depends only on its length and gravity — not on the mass of the bob or the amplitude (again, for small angles). This is why pendulum clocks keep reliable time: the period T = 2π/ω_n is stable.

The energy method for finding ω_n bypasses Newton's laws entirely and connects directly to your prerequisite on energy conservation. For a conservative system, total energy E = KE + PE = constant. Setting dE/dt = 0 and comparing the resulting equation to the standard form ẍ + ω_n²x = 0 directly reveals ω_n. This method is often algebraically cleaner than the force method for complex geometries (pendulums, springs on pulleys, compound rotors). The skill to develop is identifying the appropriate kinetic and potential energy expressions, differentiating total energy, and reading off ω_n — a pattern that extends naturally to damped and forced vibration analysis in the next course topic.
