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
- id: complex-numbers-intro
  type: soft
- id: differential-equations-intro
  type: hard
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
status: validated
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

## Explainer

From your study of RC and RL circuits, you know that each alone shows only exponential decay: a capacitor discharges through a resistor with time constant τ = RC; an inductor's current decays through a resistor with τ = L/R. When you combine a capacitor and an inductor without resistance, something qualitatively different happens. Instead of settling toward zero, energy bounces back and forth between the two elements indefinitely. This is **electromagnetic oscillation**, and it is the electrical counterpart of the mechanical oscillation you studied in simple harmonic motion.

The analogy is exact and worth internalizing: the capacitor plays the role of a spring (storing potential energy, proportional to charge²), and the inductor plays the role of a mass (storing kinetic energy, proportional to current²). When the capacitor is fully charged, the current is zero — analogous to a spring at maximum displacement with the mass momentarily stopped. As the capacitor discharges, current builds up in the inductor; this is like the spring releasing and the mass accelerating. When the capacitor is fully discharged, current is at its peak — analogous to the mass at the equilibrium point with maximum velocity. The inductor then forces the charge to continue flowing, recharging the capacitor in the opposite polarity, and the cycle repeats. The governing differential equation is L(d²Q/dt²) + Q/C = 0, which is mathematically identical to the harmonic oscillator equation with ω₀ = 1/√(LC).

Adding resistance creates an **RLC circuit** and introduces damping, just as friction damps a mechanical oscillator. The full equation L(d²Q/dt²) + R(dQ/dt) + Q/C = 0 has three regimes depending on the **damping ratio** ζ = R/(2√(L/C)): underdamped (ζ < 1, oscillations that decay exponentially), critically damped (ζ = 1, fastest approach to equilibrium without oscillating), and overdamped (ζ > 1, slow exponential decay). In practice, most resonant circuits are designed to be underdamped. The **quality factor** Q_factor = ω₀L/R quantifies how sharp the resonance is — a high Q circuit rings many times before its energy dissipates, while a low Q circuit loses energy quickly.

Resonance occurs when an external driving source is applied at exactly ω₀. At resonance, the capacitive and inductive **reactances** cancel (X_L = ω₀L and X_C = 1/(ω₀C) are equal), so the circuit looks like a pure resistance. This is why radio tuning works: by adjusting L or C, you shift ω₀ until it matches the broadcast frequency, at which point that station's signal drives the circuit at resonance, producing maximum current. All other frequencies drive the circuit off-resonance and produce much smaller currents. The sharper the resonance (higher Q), the better the frequency selectivity.
