---
id: electromotive-force-batteries
title: Electromotive Force (EMF) and Batteries
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: potential-energy-systems
  type: hard
- id: ohms-law-circuits
  type: hard
builds-toward:
- kirchhoff-circuit-laws-rules
tags:
- emf
- battery
- energy-source
stage: formal-systems
status: validated
---

# Electromotive Force (EMF) and Batteries

## Core Idea
Electromotive force (EMF) ε is the work per unit charge a battery (or other source) does; EMF creates and maintains potential difference. Real batteries have internal resistance r; terminal voltage V = ε − Ir decreases with current.

## Questions

```yaml
- question: "A battery with EMF ε = 9 V and internal resistance r = 1 Ω is connected to an external resistor R = 8 Ω. What is the terminal voltage across the battery's terminals?"
  type: multiple-choice
  options:
    - "9 V — the terminal voltage always equals the EMF"
    - "8 V — the terminal voltage equals the voltage across the external resistor only"
    - "1 V — the terminal voltage equals the voltage drop across the internal resistance"
    - "8 V — calculated as V = ε − Ir = 9 − (1)(1) = 8 V"
  answer: 3
  explanation: "The current in the circuit is I = ε/(R + r) = 9/(8+1) = 1 A. The terminal voltage is V = ε − Ir = 9 − (1)(1) = 8 V. This equals the voltage across the external load, as expected: V = IR = (1)(8) = 8 V. Note that options B and D state the same number (8 V) but option B gives the wrong reasoning — the terminal voltage happens to equal the load voltage here, but the reason is V = ε − Ir, not a definition. Option A is the ideal-battery misconception; real batteries always have V < ε when current flows."

- question: "A nearly discharged battery reads 12 V on a voltmeter when nothing is connected, but drops to 8 V when connected to a motor. What best explains this?"
  type: multiple-choice
  options:
    - "The voltmeter drained the battery during measurement"
    - "The motor reversed the current through the battery, reducing its voltage"
    - "The battery's internal resistance increased as it discharged; the large current drawn by the motor creates a significant Ir voltage drop inside the battery"
    - "The motor's back-EMF opposes the battery, reducing the effective voltage"
  answer: 2
  explanation: "The open-circuit voltage (12 V) approximates the EMF ε because no current flows and thus Ir ≈ 0. When the motor draws large current I, the internal resistance r (which increases as the battery discharges) causes a voltage drop Ir inside the battery, leaving V = ε − Ir = 8 V at the terminals. This is exactly why 'dead' batteries often read fine on a voltmeter but fail under load — their internal resistance has risen so much that any real current draw collapses the terminal voltage."

- question: "Electromotive force is a force that pushes charges through the circuit."
  type: true-false
  answer: false
  explanation: "Despite its name, EMF is not a force — it is energy per unit charge, measured in volts (joules per coulomb). It represents the work done by the source (chemical reactions, mechanical motion, etc.) per coulomb of charge moved through it. The naming is a historical accident; 'electromotive force' was coined before the modern distinction between force and energy was fully established. Treating EMF as a literal force leads to confusion when applying energy conservation (Kirchhoff's voltage law) to circuits."

- question: "The terminal voltage of a real battery under load is always less than its EMF."
  type: true-false
  answer: true
  explanation: "The terminal voltage is V = ε − Ir. Since I > 0 when current flows and r > 0 for any real battery, the product Ir > 0, so V < ε always. The terminal voltage equals the EMF only in the ideal limiting case r = 0 (no internal resistance) or I = 0 (open circuit). In real batteries, internal resistance is always positive, so current draw always causes a voltage sag at the terminals. This is why the measured voltage of a battery under load is the relevant quantity for circuit calculations, not the open-circuit EMF."

- question: "Why does the terminal voltage of a battery decrease when it must supply a larger current? Explain using the internal resistance model."
  type: short-answer
  answer: "Every real battery has internal resistance r. When current I flows, this internal resistance causes a voltage drop Ir inside the battery itself. The terminal voltage — the voltage available to the external circuit — is what remains after that internal drop: V = ε − Ir. The larger the current drawn, the larger the Ir drop, and the lower the terminal voltage. The EMF ε is fixed by the battery's chemistry; it is the internal drop that eats into the usable voltage."
  explanation: "This model explains many practical observations: why headlights dim when you start a car (starter draws huge current, Ir increases, lights get less voltage); why a 'dead' battery reads fine on a voltmeter but fails under load (high internal resistance makes Ir large even for moderate I); and why short-circuiting a battery is dangerous (R → 0, I = ε/r can be enormous). The internal resistance model connects the abstract EMF concept to observable circuit behavior."
```

## Explainer

From your study of potential energy, you know that moving charges uphill in a potential field requires work. In a circuit, current flows from high to low potential through the external load, dissipating energy. But something must continuously pump charge back from low to high potential to sustain the current — that something is the **electromotive force**. Despite the name, EMF is not a force; it is energy per unit charge (measured in volts), representing the work done by the source (chemical, mechanical, thermal) per coulomb moved through it. A 12 V car battery does 12 joules of work for every coulomb it drives around the circuit.

The idealized battery maintains a fixed potential difference ε across its terminals regardless of the current drawn. Real batteries do not behave this way. Every real battery has **internal resistance** r — resistance inside the battery itself due to the ionic solution and electrodes. When current I flows, there is a voltage drop Ir within the battery, so the actual terminal voltage is V = ε − Ir. Draw more current and the terminal voltage sags. This is why a nearly dead battery reads 12 V when disconnected but might only sustain 9 V when trying to start a car engine. The EMF is still 12 V; the internal resistance has increased, causing a larger voltage drop at the high current demanded.

You already know from Ohm's law that V = IR for a resistor. Combining that with the battery model gives you the complete single-loop circuit: ε = I(R + r). The total driving EMF equals the total resistive voltage drop across both the external load R and the internal resistance r. Rearranging, I = ε/(R + r). Notice the limiting cases: if r → 0 (ideal battery), I = ε/R as you would naively expect; if R → 0 (short circuit), I = ε/r, which can be dangerously large since r is small.

The power perspective ties it together. The battery delivers power P = εI. Of this, P_load = I²R goes to the external load doing useful work, and P_lost = I²r is wasted as heat inside the battery. Maximum power is delivered to the load when R = r — a result called the maximum power transfer theorem that will reappear in circuit analysis. The EMF concept is the bridge between the energy-source view (chemistry pumping charge) and the circuit-analysis view (voltage sources driving currents through resistances); mastering it is essential before you move to multi-loop circuits with Kirchhoff's laws.
