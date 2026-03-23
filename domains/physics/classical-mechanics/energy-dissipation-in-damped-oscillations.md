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
status: validated
---

# Energy Dissipation in Damped Oscillations

## Core Idea
The damping force dissipates mechanical energy at a rate P_damp = b v² (always positive). Over time, total mechanical energy decays exponentially: E(t) = E₀ exp(−t/τ), where τ = m/b is the characteristic decay time. In driven-damped oscillations, the external force continuously supplies energy, which the damping continuously dissipates; at steady state, input and dissipation balance.

## Questions

```yaml
- question: "An underdamped oscillator is losing energy to friction. At which point in its oscillation is energy being dissipated most rapidly?"
  type: multiple-choice
  options:
    - "At maximum displacement (the turning points), because that is where stored energy is greatest"
    - "At the equilibrium position, because that is where the oscillator moves fastest"
    - "At equal rates throughout the cycle, since energy decays exponentially in time"
    - "Only when the direction of motion reverses, since that is when the damping force changes sign"
  answer: 1
  explanation: "The rate of energy dissipation is P = bv², which is maximum when velocity is maximum. For a harmonic oscillator, velocity is maximum at the equilibrium position (x = 0), not at the turning points where v = 0. At the turning points, the oscillator is momentarily at rest, so the damping force does zero work and dissipation is zero. Option A is the classic misconception: confusing the amplitude (maximum displacement) with the velocity. Energy is highest at the turning points, but the rate of energy loss is lowest there."

- question: "If the amplitude of a damped oscillator decays as e^(−bt/2m), how does its total mechanical energy decay?"
  type: multiple-choice
  options:
    - "At the same rate: E(t) ∝ e^(−bt/2m)"
    - "At half the rate: E(t) ∝ e^(−bt/4m)"
    - "At twice the rate: E(t) ∝ e^(−bt/m)"
    - "Linearly in time, since power dissipation is approximately constant"
  answer: 2
  explanation: "Mechanical energy is proportional to amplitude squared: E ∝ A². If A decays as e^(−bt/2m), then E ∝ A² ∝ (e^(−bt/2m))² = e^(−bt/m). The energy decays at twice the rate of the amplitude. This follows directly from the power law: if dE/dt = −bv², and v scales as amplitude, then v² scales as amplitude squared, and energy (also scaling as amplitude squared) decays twice as fast in the exponent. This factor of 2 is a direct consequence of energy being a quadratic quantity."

- question: "The damping force dissipates energy at a rate proportional to v², so energy dissipation is greatest when the oscillator passes through the equilibrium position."
  type: true-false
  answer: true
  explanation: "The instantaneous power dissipated by the damping force F_damp = −bv is P = F_damp · v = −bv². The magnitude bv² is maximum when v is maximum. In a harmonic oscillator, maximum velocity occurs at equilibrium (x = 0), where all energy is kinetic and potential energy is zero. So the oscillator dissipates energy most rapidly at equilibrium and most slowly near the turning points, where it momentarily stops."

- question: "In driven-damped oscillations at steady state, the total mechanical energy of the oscillator continues to decrease over time."
  type: true-false
  answer: false
  explanation: "At steady state, the transients have died out and the oscillator vibrates at constant amplitude at the driving frequency. This constant amplitude means constant total energy — the energy neither grows nor decays. The external driver continuously supplies energy at exactly the rate the damping dissipates it; input and dissipation balance. Before steady state is reached, the energy may be growing (if driving is building up amplitude) or decaying (if the system is settling down), but at steady state the net change is zero on average."

- question: "Why does the mechanical energy of an underdamped oscillator decay at twice the rate of its amplitude? What does this reveal about the relationship between energy and amplitude?"
  type: short-answer
  answer: "Energy is proportional to amplitude squared (E ∝ ½kA²). If amplitude decays as e^(−γt) with γ = b/2m, then E ∝ A² ∝ e^(−2γt) — the energy decays at twice the exponent rate. This reveals that energy is a quadratic function of amplitude: doubling amplitude quadruples energy, and halving amplitude reduces energy to one-quarter. The rate of energy loss is therefore always twice the rate of amplitude loss."
  explanation: "This quadratic relationship is a universal feature of simple harmonic motion, not specific to damped systems. In any SHO, E = ½kA² = ½mω²A². So all the energy information is in the amplitude, and changes in amplitude produce proportionally larger changes in energy. The practical consequence is that a lightly damped oscillator (large τ) loses amplitude slowly but loses energy at twice that rate — which matters for engineering applications like resonators, clocks, and acoustic instruments where energy retention determines performance."
```

## Explainer

From your study of the damped harmonic oscillator, you know that the equation of motion includes a damping force proportional to velocity: F_damp = −bv. You know the solutions — underdamped oscillations with shrinking amplitude, critical damping, and overdamping — and you have a qualitative picture of how energy gradually leaves the system. This topic makes that energy picture quantitative by asking: at what rate does the damping force remove energy, and how does the total mechanical energy evolve over time?

The key connection comes from the power concept you have studied. **Power** is the rate at which a force does work: P = F · v. For the damping force F_damp = −bv, the instantaneous power delivered by this force to the oscillator is P_damp = F_damp · v = (−bv)(v) = −bv². The negative sign confirms that the damping force always removes energy from the system — it is dissipative by construction, regardless of whether the oscillator is moving forward or backward. The magnitude bv² is always positive, and it is largest when the oscillator moves fastest (near the equilibrium position, where kinetic energy is maximum).

Now consider how total mechanical energy E = ½mv² + ½kx² evolves. Differentiating with respect to time and using the equation of motion gives dE/dt = −bv², which matches exactly the power dissipated by damping. This is not a coincidence: it is conservation of energy in differential form. The rate of change of mechanical energy equals the rate at which the damping force does (negative) work. Since v² is always non-negative, dE/dt ≤ 0 — energy can only decrease or stay constant, never increase spontaneously.

For the underdamped case, v²(t) oscillates while its envelope decays. Averaging over a complete cycle (so the oscillating part averages out), one finds that energy decays exponentially with a time constant **τ = m/b**. The result is E(t) = E₀ e^(−t/τ), where τ measures how quickly energy bleeds away. A large mass or small damping coefficient gives a long decay time; a large damping coefficient gives rapid dissipation. This exponential envelope is the energy analogue of the amplitude decay e^(−bt/2m) you already know — the energy decays at twice the rate of amplitude, which makes sense because energy scales as amplitude squared.

In **driven-damped oscillations**, a periodic external force replenishes the energy that damping removes. At steady state (transients gone), the system oscillates at the driving frequency with constant amplitude — meaning energy input from the driver exactly balances energy lost to damping. At resonance, the system absorbs maximum power from the driver because the velocity is exactly in phase with the driving force. The **quality factor** Q = ω₀/γ (where γ = b/m is the damping rate) quantifies this balance: a high-Q oscillator loses energy slowly, has sharp resonance, and rings for many cycles; a low-Q oscillator damps out quickly and has a broad, flat resonance curve. This energy perspective unifies the dynamics — amplitude, phase, and steady-state behavior all follow from the same underlying energy budget between driving power and dissipation.
