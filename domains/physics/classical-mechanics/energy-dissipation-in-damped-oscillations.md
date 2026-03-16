---
id: energy-dissipation-in-damped-oscillations
title: Energy Dissipation in Damped Oscillations
domain: physics
course: classical-mechanics
prerequisites:
- id: damped-harmonic-oscillator
  type: hard
- id: power-and-work-rate
  type: soft
tags:
- damping
- energy
- dissipation
- oscillations
stage: formal-systems
status: draft
---

# Energy Dissipation in Damped Oscillations

## Core Idea
The damping force dissipates mechanical energy at a rate P_damp = b v² (always positive). Over time, total mechanical energy decays exponentially: E(t) = E₀ exp(−t/τ), where τ = m/b is the characteristic decay time. In driven-damped oscillations, the external force continuously supplies energy, which the damping continuously dissipates; at steady state, input and dissipation balance.

## Explainer

From your study of the damped harmonic oscillator, you know that the equation of motion includes a damping force proportional to velocity: F_damp = −bv. You know the solutions — underdamped oscillations with shrinking amplitude, critical damping, and overdamping — and you have a qualitative picture of how energy gradually leaves the system. This topic makes that energy picture quantitative by asking: at what rate does the damping force remove energy, and how does the total mechanical energy evolve over time?

The key connection comes from the power concept you have studied. **Power** is the rate at which a force does work: P = F · v. For the damping force F_damp = −bv, the instantaneous power delivered by this force to the oscillator is P_damp = F_damp · v = (−bv)(v) = −bv². The negative sign confirms that the damping force always removes energy from the system — it is dissipative by construction, regardless of whether the oscillator is moving forward or backward. The magnitude bv² is always positive, and it is largest when the oscillator moves fastest (near the equilibrium position, where kinetic energy is maximum).

Now consider how total mechanical energy E = ½mv² + ½kx² evolves. Differentiating with respect to time and using the equation of motion gives dE/dt = −bv², which matches exactly the power dissipated by damping. This is not a coincidence: it is conservation of energy in differential form. The rate of change of mechanical energy equals the rate at which the damping force does (negative) work. Since v² is always non-negative, dE/dt ≤ 0 — energy can only decrease or stay constant, never increase spontaneously.

For the underdamped case, v²(t) oscillates while its envelope decays. Averaging over a complete cycle (so the oscillating part averages out), one finds that energy decays exponentially with a time constant **τ = m/b**. The result is E(t) = E₀ e^(−t/τ), where τ measures how quickly energy bleeds away. A large mass or small damping coefficient gives a long decay time; a large damping coefficient gives rapid dissipation. This exponential envelope is the energy analogue of the amplitude decay e^(−bt/2m) you already know — the energy decays at twice the rate of amplitude, which makes sense because energy scales as amplitude squared.

In **driven-damped oscillations**, a periodic external force replenishes the energy that damping removes. At steady state (transients gone), the system oscillates at the driving frequency with constant amplitude — meaning energy input from the driver exactly balances energy lost to damping. At resonance, the system absorbs maximum power from the driver because the velocity is exactly in phase with the driving force. The **quality factor** Q = ω₀/γ (where γ = b/m is the damping rate) quantifies this balance: a high-Q oscillator loses energy slowly, has sharp resonance, and rings for many cycles; a low-Q oscillator damps out quickly and has a broad, flat resonance curve. This energy perspective unifies the dynamics — amplitude, phase, and steady-state behavior all follow from the same underlying energy budget between driving power and dissipation.
