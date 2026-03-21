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

## Questions

```yaml
- question: "A spring-mass system is oscillating with amplitude A. If you increase the initial displacement to 2A without changing the spring or mass, what happens to the natural frequency?"
  type: multiple-choice
  options:
    - "It doubles — the system now oscillates with twice the energy, so it moves faster"
    - "It increases by a factor of √2 — energy is proportional to A², so frequency scales accordingly"
    - "It decreases — the larger displacement means the mass takes more time to travel the full cycle"
    - "It remains unchanged — natural frequency depends only on k and m, not on amplitude"
  answer: 3
  explanation: "Natural frequency ω_n = √(k/m) is a property of the system's physical parameters alone — it is completely independent of amplitude. Doubling the amplitude doubles the maximum velocity and quadruples the total energy, but both changes cancel: the mass travels twice as far at twice the speed, so the period is unchanged. This amplitude-independence is a unique and important feature of systems with linear restoring forces."

- question: "An engineer uses the energy method to find the natural frequency of a compound pendulum. She writes E = ½Iθ̇² + ½k_eff θ², differentiates with respect to time, and sets dE/dt = 0. What equation does she arrive at?"
  type: multiple-choice
  options:
    - "Iθ̈ + k_eff θ = 0, revealing ω_n = √(k_eff/I)"
    - "Iθ̈ = k_eff θ, which requires numerical solution for ω_n"
    - "θ̈ = 0, indicating no oscillation occurs"
    - "dE/dt = 0 only holds at equilibrium and gives no information about frequency"
  answer: 0
  explanation: "Differentiating E = ½Iθ̇² + ½k_eff θ² gives dE/dt = Iθ̇θ̈ + k_eff θθ̇ = 0. Dividing through by θ̇ (nonzero except at turning points) yields Iθ̈ + k_eff θ = 0 — the standard SHM equation. Comparing to the form θ̈ + ω_n²θ = 0 directly gives ω_n = √(k_eff/I). This energy method bypasses drawing free body diagrams and applying Newton's second law directly, often simplifying the algebra for complex geometries."

- question: "The natural frequency of a spring-mass system is independent of the amplitude of oscillation."
  type: true-false
  answer: true
  explanation: "ω_n = √(k/m) contains no amplitude term. This holds for any system with a truly linear restoring force (F = −kx), and is the defining characteristic that makes SHM exactly sinusoidal with a constant period. Amplitude determines the energy stored (E = ½kA²) and the maximum speed (v_max = Aω_n), but not how fast the cycle repeats. This property breaks down for large displacements where Hooke's law no longer applies — hence the small-angle approximation for pendulums."

- question: "Attaching a heavier mass to a spring increases the natural frequency because more mass stores more kinetic energy and therefore oscillates faster."
  type: true-false
  answer: false
  explanation: "A heavier mass decreases the natural frequency: ω_n = √(k/m) — mass m is in the denominator. Greater mass means greater inertia, so the restoring force accelerates it more slowly and the oscillation is slower. The misconception confuses energy storage with oscillation rate. While more mass does carry more kinetic energy at peak velocity, it also moves more sluggishly — the net effect is a lower natural frequency and a longer period."

- question: "Explain why the energy method (setting dE/dt = 0 for a conservative system) yields the natural frequency, and why it is sometimes preferred over Newton's second law for this purpose."
  type: short-answer
  answer: "For a conservative system, total mechanical energy E = KE + PE is constant, so dE/dt = 0. Differentiating and collecting terms produces an equation of the form ẍ + ω_n²x = 0, where ω_n² is the coefficient of x (or θ for rotational systems). Reading off this coefficient directly gives ω_n without requiring explicit identification of all forces. The energy method is preferred when the system has complex geometry — pulleys, compound pendulums, systems with multiple moving parts — because energy is scalar and easier to write down correctly than all the force and moment equations."
  explanation: "Newton's second law requires drawing free body diagrams and resolving forces, which can be algebraically messy for complex systems. Energy methods bypass this by working with scalar quantities (kinetic and potential energy), which are often easier to express for complicated geometries. Both methods must give the same ω_n — they are mathematically equivalent for linear, conservative systems. The energy method is especially powerful when the system's kinetic energy involves multiple velocity components or when constraint forces do no work and can simply be ignored."
```

## Explainer

The defining feature of simple harmonic motion is the **linear restoring force**: a force (or torque) that always points back toward equilibrium and whose magnitude is exactly proportional to how far you've displaced the system. A spring satisfies this: stretch it by x, and it pulls back with force F = −kx. The minus sign is the whole story — the force opposes the displacement. If you displace a mass on a spring and release it, Newton's second law gives mẍ = −kx, which is a second-order linear ODE whose solution is x(t) = A cos(ω_n t + φ). The motion is exactly sinusoidal, oscillating forever with constant amplitude. You already know from energy conservation that a closed system conserves total mechanical energy; SHM is simply the case where all that energy alternates between the spring's potential energy (½kx²) and the mass's kinetic energy (½mv²), with the total sum remaining constant at every instant.

The **natural frequency** ω_n = √(k/m) tells you how fast the system oscillates. Notice its structure: k appears in the numerator and m in the denominator. A stiffer spring (larger k) increases the restoring force at every displacement, causing faster oscillations. A heavier mass (larger m) has more inertia and overshoots equilibrium more slowly. The natural frequency is entirely set by the system's physical parameters — it is not something you impose from outside. Every spring-mass system has exactly one natural frequency, and it will oscillate at that frequency if given any initial displacement or velocity, regardless of amplitude (for small oscillations). This amplitude-independence is a special and important property of SHM that does not hold for nonlinear restoring forces.

For rotational systems, the same logic applies with moment of inertia I replacing mass m and torsional stiffness k replacing linear stiffness: ω_n = √(k/I). A simple pendulum, for small angles, approximates SHM with an effective stiffness k_eff = mg/L, giving ω_n = √(g/L). Notice that the pendulum's natural frequency depends only on its length and gravity — not on the mass of the bob or the amplitude (again, for small angles). This is why pendulum clocks keep reliable time: the period T = 2π/ω_n is stable.

The energy method for finding ω_n bypasses Newton's laws entirely and connects directly to your prerequisite on energy conservation. For a conservative system, total energy E = KE + PE = constant. Setting dE/dt = 0 and comparing the resulting equation to the standard form ẍ + ω_n²x = 0 directly reveals ω_n. This method is often algebraically cleaner than the force method for complex geometries (pendulums, springs on pulleys, compound rotors). The skill to develop is identifying the appropriate kinetic and potential energy expressions, differentiating total energy, and reading off ω_n — a pattern that extends naturally to damped and forced vibration analysis in the next course topic.
