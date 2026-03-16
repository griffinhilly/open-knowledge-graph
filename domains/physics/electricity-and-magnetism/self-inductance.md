---
id: self-inductance
title: Self-Inductance and Magnetic Energy
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: motional-emf
  type: soft
- id: faraday-induced-emf
  type: hard
builds-toward:
- rl-transient-response
tags:
- self-inductance
- energy
- induction
stage: formal-systems
status: draft
---

# Self-Inductance and Magnetic Energy

## Core Idea
Self-inductance L is defined by Φ = LI. When current changes, induced EMF is ε = −L dI/dt, opposing the change (Lenz's law). Energy stored in the magnetic field is U = (1/2)LI². For a solenoid: L = μ₀N²A/ℓ. Inductance depends on geometry but not on current. Inductors resist current changes and are essential in AC circuits and transient analysis.

## Explainer

From Faraday's law you learned that changing magnetic flux induces an EMF. A coil of wire carrying current creates its own magnetic field, and that field produces magnetic flux through the coil itself. When the current changes, the flux changes — and by Faraday's law, this changing flux induces an EMF *in the very coil that created it*. This is **self-inductance**: a circuit element's tendency to oppose changes in its own current by inducing a back-EMF. The **inductance** L is the constant of proportionality between flux and current: Φ_total = LI, where Φ_total counts all turns (Φ_total = NΦ for an N-turn coil).

Taking the time derivative, ε = −dΦ_total/dt = −L dI/dt. This back-EMF acts like inertia for current: just as a massive object resists changes in velocity, an inductor resists changes in current. Trying to increase current quickly requires you to "push against" this back-EMF; trying to interrupt current quickly generates a large back-EMF that can arc across switches. (This is why opening an inductive circuit causes sparks — the inductor "insists" on continuing the current and drives whatever voltage it takes.) The negative sign, again, is Lenz's law: the induced EMF opposes the cause.

The **energy stored in an inductor** U = (1/2)LI² is the magnetic analog of the capacitor's (1/2)CV² for electric energy. Both are quadratic in their respective quantities — charge for capacitors, current for inductors. This energy is stored in the magnetic field itself, distributed throughout space, with energy density u = B²/(2μ₀). For a solenoid with N turns, area A, and length ℓ, the geometry gives L = μ₀N²A/ℓ. Notice that L scales as N² — doubling the number of turns quadruples the inductance, because each turn both creates more flux and "sees" more flux.

Inductors are one of the three fundamental passive circuit elements (alongside resistors and capacitors), and each plays a distinct temporal role. Resistors respond instantaneously to voltage. Capacitors resist voltage changes (current "charges" them). Inductors resist current changes. In the RL transient circuit you will study next, these properties combine to produce exponential decays in current with time constant τ = L/R. In AC circuits, inductors cause current to lag behind voltage — the dual of capacitors, where current leads. Together, inductors and capacitors form LC resonators that store and release energy alternately between magnetic and electric fields, the basis of filters, oscillators, and tuned circuits.
