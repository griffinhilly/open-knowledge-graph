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
stage: formal-systems
status: draft
---

# Inductance and Transient Response in RL Circuits

## Core Idea
Self-inductance L relates induced EMF to changing current: ε = −L dI/dt. RL circuit: I(t) = (ε/R)(1 − e^(−t/τ)) for charging, τ = L/R. Energy stored in inductor: U = ½LI². Inductance arises from magnetic flux linkage.

## Explainer

From Lenz's law — your prerequisite — you know that a changing magnetic flux through a loop induces an EMF that opposes the change. **Self-inductance** is what happens when a coil's own changing current creates the changing flux through itself. As current in a coil increases, its magnetic field strengthens, flux through the coil increases, and by Faraday's law this generates an EMF that opposes the current's increase. The coil is literally fighting its own change. The **self-inductance** L quantifies how strongly a device does this: ε = −L dI/dt. A larger L means a larger back-EMF for the same rate of current change.

To understand transient behavior in an RL circuit, think about what happens the instant you connect a battery through a resistor and an inductor in series. At t = 0, no current flows, so there's no voltage drop across R, and the full battery EMF appears across L. But ε = −L dI/dt means a large back-EMF corresponds to a large dI/dt — the current starts rising quickly. As current rises, the resistor claims more voltage (V = IR), leaving less voltage to drive further change in current. The rise slows. Eventually, when current reaches its steady-state value ε/R, dI/dt = 0 and the inductor contributes nothing. The result is the characteristic exponential: I(t) = (ε/R)(1 − e^(−t/τ)), with **time constant** τ = L/R. After one time constant, current has reached about 63% of its final value.

The time constant has an intuitive physical interpretation: it is the ratio of the inductor's resistance to change (L) to the circuit's ability to dissipate energy (R). A larger L means more inertia — the circuit takes longer to ramp up. A larger R means more friction — but also a smaller final current, so there is less total ramping to do, and the time constant is shorter. Think of the current like a mass (L) being pushed by a force (ε) while experiencing drag (R).

Energy storage closes the picture. Just as a capacitor stores energy in its electric field (U = ½CV²), an inductor stores energy in its magnetic field: U = ½LI². This energy cannot vanish instantaneously — current through an inductor cannot jump discontinuously, just as voltage across a capacitor cannot jump. This continuity constraint is fundamental in circuit analysis: when a switch opens abruptly in an RL circuit, the inductor forces current to continue flowing, often producing a large voltage spike. Understanding these transient behaviors is essential for designing circuits with inductive loads like motors, solenoids, and transformers.
