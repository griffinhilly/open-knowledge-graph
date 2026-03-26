---
id: damped-harmonic-oscillator
title: Damped Harmonic Oscillator
domain: physics
course: classical-mechanics
prerequisites:
- id: simple-harmonic-motion
  type: hard
- id: friction-forces
  type: soft
- id: higher-order-linear-odes
  type: hard
- id: second-order-linear-homogeneous-odes
  type: hard
- id: characteristic-equation-method
  type: hard
- id: differential-equations-intro
  type: hard
- id: exponential-functions-and-graphs
  type: soft
- id: complex-roots-oscillatory-solutions
  type: hard
- id: complex-numbers-intro
  type: soft
builds-toward:
- driven-harmonic-oscillator
tags:
- oscillations
- damping
- friction
- differential-equations
stage: formal-systems
status: validated
---

# Damped Harmonic Oscillator

## Core Idea
A damped oscillator experiences a restoring force (−kx) and velocity-dependent friction (−bv). The equation m d²x/dt² + b dx/dt + kx = 0 exhibits three regimes: underdamped (oscillates while decaying), critically damped (no oscillation, fastest return to equilibrium), and overdamped (slow decay without oscillation). Damping reduces the oscillation frequency compared to the undamped case.

## Questions

```yaml
- question: "A door closer is engineered so that the door swings shut as quickly as possible without bouncing or oscillating. Which damping regime describes this behavior?"
  type: multiple-choice
  options: ["Underdamped", "Critically damped", "Overdamped", "Undamped"]
  answer: 1
  explanation: "Critical damping produces the fastest return to equilibrium without any oscillation. Underdamped systems oscillate (the door would bounce). Overdamped systems return without oscillating but more slowly than critically damped. Door closers and galvanometers are engineered to be critically damped for exactly this reason."

- question: "Increasing the damping coefficient of an oscillator generally makes it return to equilibrium faster."
  type: true-false
  answer: false
  explanation: "Critical damping is the optimal point — it produces the fastest return without oscillation. Adding damping beyond the critical value produces an overdamped system, which returns to equilibrium more slowly. So increasing damping helps only up to the critical threshold; beyond that, it makes the system sluggish."

- question: "How does the presence of damping affect the oscillation frequency of an underdamped oscillator compared to the undamped natural frequency ω₀?"
  type: short-answer
  answer: "Damping reduces the oscillation frequency. The damped frequency ω_d = √(ω₀² − (b/2m)²) is always less than the undamped natural frequency ω₀."
  explanation: "This follows from solving the characteristic equation of the damped oscillator ODE. The complex roots have an imaginary part ω_d that is smaller than ω₀ by an amount depending on the damping coefficient b. Physically, the system is losing energy on every cycle, which effectively slows the oscillation compared to the frictionless case."
```

## Explainer

Simple harmonic motion describes an ideal oscillator with no energy loss — a spring-mass system that oscillates forever. Real oscillators always lose energy to their environment through friction, air resistance, or internal dissipation. The damped harmonic oscillator adds a velocity-dependent drag force F_drag = −bv, where b is the damping coefficient. The governing equation becomes m d²x/dt² + b dx/dt + kx = 0.

To solve this, you apply the characteristic equation method from your ODE work. Substituting x = e^(rt) yields mr² + br + k = 0, with roots r = (−b ± √(b² − 4mk)) / (2m). The behavior of the system is entirely determined by the discriminant b² − 4mk, which gives rise to three distinct regimes. When b² − 4mk < 0 (underdamped), the roots are complex: r = −γ ± iω_d, where γ = b/(2m) is the decay rate and ω_d = √(ω₀² − γ²) is the damped frequency. The solution is x(t) = A e^(−γt) cos(ω_d t + φ) — an oscillation with an exponentially decaying amplitude envelope. Notice that ω_d < ω₀: the system oscillates more slowly than the undamped case.

When b² − 4mk = 0 (critically damped), both roots equal −b/(2m). The solution decays without oscillating and reaches equilibrium as fast as any non-oscillating solution can. When b² − 4mk > 0 (overdamped), both roots are real and negative; the system decays without oscillating but more slowly than the critically damped case. The counterintuitive result is that adding *more* damping beyond the critical point slows the return to equilibrium — at critical damping the system is perfectly balanced, and extra friction just adds resistance without eliminating oscillation (since there is already none).

The exponential envelope e^(−γt) is a signature of damped oscillators everywhere in physics. The same mathematical structure appears in LRC circuits (where charge oscillates and decays), quantum mechanical decay of excited states, and acoustic reverberation. The three-regime classification — underdamped, critically damped, overdamped — recurs throughout physics and engineering. Recognizing which regime a system is in from its parameters (or its behavior) is a core skill for analyzing any dissipative oscillating system.
