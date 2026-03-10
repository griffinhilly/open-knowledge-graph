---
id: lc-and-rlc-circuits
title: LC and RLC Circuits
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: rl-circuits
  type: hard
- id: rc-circuits
  type: hard
- id: simple-harmonic-motion
  type: soft
builds-toward:
- ac-circuits-fundamentals
- ac-power-and-resonance
tags:
- LC-circuit
- RLC-circuit
- oscillation
- resonance
- damping
stage: formal-systems
status: draft
---

# LC and RLC Circuits

## Core Idea
An ideal LC circuit oscillates indefinitely, with charge on the capacitor and current in the inductor exchanging energy at angular frequency ω₀ = 1/√(LC) — the natural resonance frequency. This is directly analogous to a spring-mass oscillator (C ↔ m, L ↔ 1/k, Q ↔ x). Adding resistance gives an RLC circuit with damped oscillations; the quality factor Q = ω₀L/R describes how many oscillations occur before energy dissipates. When driven at ω₀, the circuit resonates.

## How It's Best Learned
Exploit the mechanical analogy: L ↔ mass (inertia), C ↔ compliance (inverse spring constant), R ↔ damping. Write the differential equation for Q(t) and recognize it as the damped harmonic oscillator equation. Solve for underdamped, critically damped, and overdamped cases.

## Common Misconceptions
- The resonance frequency ω₀ = 1/√(LC) is a property of the circuit, not the driving source.
- In an ideal LC circuit, energy oscillates between electric (capacitor) and magnetic (inductor) forms — total energy is conserved.
- The quality factor Q in circuits is different from charge Q — context determines meaning.
