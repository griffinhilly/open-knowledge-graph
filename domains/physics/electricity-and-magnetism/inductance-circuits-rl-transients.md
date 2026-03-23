---
id: inductance-circuits-rl-transients
title: Inductance and Transient Response in RL Circuits
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: lenz-law-induced-currents
  type: hard
- id: magnetic-torque-dipole
  type: soft
builds-toward:
- lorentz-force-complete-em
tags:
- inductance
- rl-circuit
- transient
stage: advanced
status: validated
---

# Inductance and Transient Response in RL Circuits

## Core Idea
Self-inductance L relates induced EMF to changing current: ε = −L dI/dt. RL circuit: I(t) = (ε/R)(1 − e^(−t/τ)) for charging, τ = L/R. Energy stored in inductor: U = ½LI². Inductance arises from magnetic flux linkage.

## Questions

```yaml
- question: "A switch is opened abruptly in a circuit where an inductor has been carrying a steady current of 2 A. What happens immediately after the switch opens?"
  type: multiple-choice
  options:
    - "Current drops immediately to zero as the circuit is broken"
    - "Current reverses direction through the inductor"
    - "Current continues to flow momentarily, and a large voltage spike may appear across the switch"
    - "The inductor discharges instantly by converting its stored energy to heat"
  answer: 2
  explanation: "An inductor stores energy in its magnetic field (U = ½LI²), and this energy cannot vanish instantaneously. When the switch opens, the inductor opposes the sudden change in current by inducing a large EMF — forcing current to continue flowing across the now-open switch gap (often as an arc). This voltage spike can damage circuit components; it is why protective circuitry (flyback diodes, snubbers) is needed in inductive loads like motors and solenoids. The key misconception is that 'breaking the circuit' instantly stops the current — for inductors, it does not."

- question: "An RL series circuit has R = 100 Ω, L = 0.2 H, and a battery with EMF = 12 V. After one time constant has elapsed, what is the approximate current?"
  type: multiple-choice
  options:
    - "120 mA (the full steady-state value)"
    - "76 mA (approximately 63% of steady-state)"
    - "44 mA (approximately 37% of steady-state)"
    - "12 mA (10% of steady-state)"
  answer: 1
  explanation: "The time constant is τ = L/R = 0.2/100 = 0.002 s. The steady-state current is ε/R = 12/100 = 120 mA. After one time constant, I(τ) = (ε/R)(1 − e⁻¹) ≈ 120 × 0.632 ≈ 76 mA. After one τ, any RL circuit has reached approximately 63% of its final value — a universal result. Option C (37% ≈ e⁻¹) represents the current still to be gained, not the current already achieved — a common confusion between e⁻¹ and 1 − e⁻¹."

- question: "The current through an inductor cannot change instantaneously because an instantaneous change would require the inductor to produce an infinite voltage."
  type: true-false
  answer: true
  explanation: "The defining equation is ε = −L(dI/dt). An instantaneous change in current means dI/dt → ∞, which would require ε → ∞. Real circuits cannot sustain infinite voltage, so instantaneous current jumps through an inductor are physically impossible. This is directly analogous to the constraint on capacitors (voltage cannot jump instantaneously because that would require infinite current, since I = C dV/dt). These continuity constraints are the key initial conditions in transient circuit analysis."

- question: "Increasing the resistance in an RL circuit always increases the time it takes for the current to reach its final steady-state value."
  type: true-false
  answer: false
  explanation: "The time constant is τ = L/R, so increasing R *decreases* τ — the circuit reaches steady state faster in absolute time. This seems counterintuitive: more resistance means more 'friction,' yet the circuit charges faster? The resolution is that the final current (ε/R) is also smaller when R is larger. The inductor has less total change to accomplish, and despite unchanged inductance, arrives at the smaller target more quickly. Think of the mechanical analogy: a mass under constant force with high drag has a low terminal velocity that it reaches quickly."

- question: "Describe the physical analogy between an RL circuit and a mass experiencing linear drag, identifying what plays the role of mass, applied force, friction, and terminal velocity."
  type: short-answer
  answer: "In the RL circuit: inductance L corresponds to mass (inertia — resistance to change in current/velocity); EMF ε corresponds to the applied force; resistance R corresponds to the drag coefficient (friction); and the final steady-state current ε/R corresponds to terminal velocity. The exponential approach to steady state — I(t) = (ε/R)(1 − e^(−Rt/L)) — mirrors the velocity equation for a mass under constant force with linear drag: v(t) = (F/b)(1 − e^(−bt/m)), where b is drag. In both cases, the system asymptotically approaches a fixed final state with time constant set by inertia divided by friction."
  explanation: "The analogy is mathematically exact — both systems are governed by first-order linear ODEs of the same form. It clarifies why τ = L/R: large inductance (mass) means more inertia and a slower approach, while large resistance (friction) means a lower final current (terminal velocity) and a shorter τ because there is less total change to accomplish. Energy storage closes the analogy: kinetic energy ½mv² corresponds to magnetic field energy ½LI², and both are the reason the system cannot stop (or start) instantaneously."
```

## Explainer

From Lenz's law — your prerequisite — you know that a changing magnetic flux through a loop induces an EMF that opposes the change. **Self-inductance** is what happens when a coil's own changing current creates the changing flux through itself. As current in a coil increases, its magnetic field strengthens, flux through the coil increases, and by Faraday's law this generates an EMF that opposes the current's increase. The coil is literally fighting its own change. The **self-inductance** L quantifies how strongly a device does this: ε = −L dI/dt. A larger L means a larger back-EMF for the same rate of current change.

To understand transient behavior in an RL circuit, think about what happens the instant you connect a battery through a resistor and an inductor in series. At t = 0, no current flows, so there's no voltage drop across R, and the full battery EMF appears across L. But ε = −L dI/dt means a large back-EMF corresponds to a large dI/dt — the current starts rising quickly. As current rises, the resistor claims more voltage (V = IR), leaving less voltage to drive further change in current. The rise slows. Eventually, when current reaches its steady-state value ε/R, dI/dt = 0 and the inductor contributes nothing. The result is the characteristic exponential: I(t) = (ε/R)(1 − e^(−t/τ)), with **time constant** τ = L/R. After one time constant, current has reached about 63% of its final value.

The time constant has an intuitive physical interpretation: it is the ratio of the inductor's resistance to change (L) to the circuit's ability to dissipate energy (R). A larger L means more inertia — the circuit takes longer to ramp up. A larger R means more friction — but also a smaller final current, so there is less total ramping to do, and the time constant is shorter. Think of the current like a mass (L) being pushed by a force (ε) while experiencing drag (R).

Energy storage closes the picture. Just as a capacitor stores energy in its electric field (U = ½CV²), an inductor stores energy in its magnetic field: U = ½LI². This energy cannot vanish instantaneously — current through an inductor cannot jump discontinuously, just as voltage across a capacitor cannot jump. This continuity constraint is fundamental in circuit analysis: when a switch opens abruptly in an RL circuit, the inductor forces current to continue flowing, often producing a large voltage spike. Understanding these transient behaviors is essential for designing circuits with inductive loads like motors, solenoids, and transformers.
