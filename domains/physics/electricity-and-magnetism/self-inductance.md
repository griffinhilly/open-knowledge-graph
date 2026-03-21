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

## Questions

```yaml
- question: "An inductor carries a steady 2 A current. What is the back-EMF induced across it?"
  type: multiple-choice
  options:
    - "LI — the inductance multiplied by the current"
    - "Zero, because the current is not changing"
    - "½LI², converted to a voltage"
    - "μ₀N²A/ℓ multiplied by the current"
  answer: 1
  explanation: "The back-EMF is ε = −L(dI/dt). If the current is steady, dI/dt = 0, so ε = 0. An inductor does not oppose current itself — it opposes changes in current. A common misconception is that LI gives the back-EMF (it gives the total flux linkage), but voltage depends on the rate of change. Options A and C both confuse the energy/flux relationship with the EMF relationship."

- question: "If you double the number of turns N in a solenoid while keeping length, cross-sectional area, and current constant, what happens to the inductance?"
  type: multiple-choice
  options:
    - "It doubles, since inductance is proportional to N"
    - "It triples"
    - "It quadruples, since inductance is proportional to N²"
    - "It remains unchanged, because inductance depends only on the physical geometry, not turn count"
  answer: 2
  explanation: "From L = μ₀N²A/ℓ, inductance scales as N². Doubling N gives L → μ₀(2N)²A/ℓ = 4μ₀N²A/ℓ — four times the original inductance. The N² dependence arises because each turn both produces more flux and links more of that flux: doubling turns doubles the flux and doubles how many turns 'see' it, giving a factor of 4. The misconception in option D is partly correct (geometry matters) but wrong to exclude turn count — N is part of the coil geometry."

- question: "An inductor opposes the flow of current through it, similar to how a resistor limits current."
  type: true-false
  answer: false
  explanation: "An inductor opposes changes in current (rate of change dI/dt), not current itself. An ideal inductor with a steady current flowing through it presents zero voltage drop — it behaves like a wire in DC steady state. A resistor, by contrast, always drops voltage proportional to the instantaneous current. The distinction matters: after a long time in a DC circuit, an inductor is a short circuit; a resistor never is."

- question: "The energy stored in an inductor is proportional to the square of the current flowing through it."
  type: true-false
  answer: true
  explanation: "The energy stored in an inductor is U = ½LI², which is quadratic in current I. This is analogous to the energy stored in a capacitor (U = ½CV²), which is quadratic in voltage. The energy is stored in the magnetic field distributed throughout the coil — not in the wire itself."

- question: "When a switch in a highly inductive circuit is suddenly opened, the current is interrupted abruptly. Why does this produce a large voltage spike, and what physically causes it?"
  type: short-answer
  answer: "Opening the switch forces the current to drop to zero nearly instantaneously, making dI/dt extremely large in magnitude. Since ε = −L(dI/dt), a large |dI/dt| produces a large back-EMF. The inductor 'insists' on maintaining its current and drives whatever voltage is necessary — potentially thousands of volts — across the switch gap, causing an arc."
  explanation: "This is Lenz's law in action: the induced EMF opposes the change (here, the decrease in current). The energy stored as ½LI² must go somewhere — it drives the arc discharge. This phenomenon explains why inductive loads (motors, solenoids, relay coils) require flyback diodes or snubber circuits to protect switching electronics from voltage spikes."
```

## Explainer

From Faraday's law you learned that changing magnetic flux induces an EMF. A coil of wire carrying current creates its own magnetic field, and that field produces magnetic flux through the coil itself. When the current changes, the flux changes — and by Faraday's law, this changing flux induces an EMF *in the very coil that created it*. This is **self-inductance**: a circuit element's tendency to oppose changes in its own current by inducing a back-EMF. The **inductance** L is the constant of proportionality between flux and current: Φ_total = LI, where Φ_total counts all turns (Φ_total = NΦ for an N-turn coil).

Taking the time derivative, ε = −dΦ_total/dt = −L dI/dt. This back-EMF acts like inertia for current: just as a massive object resists changes in velocity, an inductor resists changes in current. Trying to increase current quickly requires you to "push against" this back-EMF; trying to interrupt current quickly generates a large back-EMF that can arc across switches. (This is why opening an inductive circuit causes sparks — the inductor "insists" on continuing the current and drives whatever voltage it takes.) The negative sign, again, is Lenz's law: the induced EMF opposes the cause.

The **energy stored in an inductor** U = (1/2)LI² is the magnetic analog of the capacitor's (1/2)CV² for electric energy. Both are quadratic in their respective quantities — charge for capacitors, current for inductors. This energy is stored in the magnetic field itself, distributed throughout space, with energy density u = B²/(2μ₀). For a solenoid with N turns, area A, and length ℓ, the geometry gives L = μ₀N²A/ℓ. Notice that L scales as N² — doubling the number of turns quadruples the inductance, because each turn both creates more flux and "sees" more flux.

Inductors are one of the three fundamental passive circuit elements (alongside resistors and capacitors), and each plays a distinct temporal role. Resistors respond instantaneously to voltage. Capacitors resist voltage changes (current "charges" them). Inductors resist current changes. In the RL transient circuit you will study next, these properties combine to produce exponential decays in current with time constant τ = L/R. In AC circuits, inductors cause current to lag behind voltage — the dual of capacitors, where current leads. Together, inductors and capacitors form LC resonators that store and release energy alternately between magnetic and electric fields, the basis of filters, oscillators, and tuned circuits.
