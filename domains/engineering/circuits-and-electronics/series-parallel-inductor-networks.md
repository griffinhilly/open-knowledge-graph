---
id: series-parallel-inductor-networks
title: Series and Parallel Inductor Networks
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: capacitor-inductor-energy-storage
  type: hard
- id: series-parallel-resistor-analysis
  type: soft
builds-toward:
- transient-response-rl-circuits
- impedance-admittance-networks
- series-resonance-characteristics
- parallel-resonance-characteristics
tags:
- inductors
- reactive-circuits
- energy-storage
stage: formal-systems
status: validated
---

# Series and Parallel Inductor Networks

## Core Idea
Inductors in series sum directly: L_eq = L₁ + L₂ + ... Inductors in parallel sum reciprocals: 1/L_eq = 1/L₁ + 1/L₂ + ... These relationships mirror resistor behavior. Series inductors share total applied voltage and all carry the same current; parallel inductors share voltage and distribute current inversely to inductance. Inductor networks are critical in power supply design and tuned circuits.

## Questions

```yaml
- question: "A student says: 'Inductors combine just like resistors — series adds, parallel uses product-over-sum — so I can analyze an inductor network exactly the same way I analyze a resistor network.' What important distinction does this overlook?"
  type: multiple-choice
  options:
    - "The formulas are different — series inductors multiply rather than add"
    - "Inductors store energy in a magnetic field and return it to the circuit, while resistors dissipate energy permanently — so while the equivalent inductance formula mirrors resistors, the energy behavior and transient dynamics are fundamentally different"
    - "The parallel combination rule for inductors adds inductances, while resistors use reciprocals"
    - "Inductors and resistors cannot be in the same circuit, making the analogy invalid"
  answer: 1
  explanation: "The combination formulas are identical in form (series: add; parallel: reciprocal sum), but inductors are reactive elements that store energy in a magnetic field during one part of the cycle and return it during another. Resistors convert electrical energy to heat irreversibly. This means inductor networks have time-dependent (transient) behavior — current through an inductor cannot change instantaneously — that has no parallel in resistor networks. The formula analogy is useful for finding L_eq, but the circuit behavior is governed by differential equations, not Ohm's law."

- question: "Two inductors L₁ = 6 H and L₂ = 3 H are connected in parallel. What is the equivalent inductance?"
  type: multiple-choice
  options:
    - "9 H — they add in parallel"
    - "2 H — product over sum: (6 × 3)/(6 + 3)"
    - "18 H — they multiply in parallel"
    - "4.5 H — the average of the two values"
  answer: 1
  explanation: "For two inductors in parallel: L_eq = (L₁ × L₂)/(L₁ + L₂) = (6 × 3)/(6 + 3) = 18/9 = 2 H. The equivalent inductance is always less than either individual value — adding parallel paths makes it easier to change the total current, reducing the effective inductance. This mirrors the parallel resistor formula exactly. Option A (adding) is the series formula applied incorrectly to parallel; option C confuses inductors with some other element."

- question: "Adding a second inductor in parallel with an existing one always decreases the equivalent inductance below either individual inductor's value."
  type: true-false
  answer: true
  explanation: "1/L_eq = 1/L₁ + 1/L₂, so L_eq = (L₁L₂)/(L₁+L₂). Since L₁L₂ < L₁(L₁+L₂) (as L₂ < L₁+L₂), we have L_eq < L₁, and by symmetry L_eq < L₂. The parallel combination is always smaller than the smallest individual element. Physically, adding a parallel inductor provides an additional current path, making the combined element easier to drive — requiring less voltage per unit of di/dt, which is equivalent to a smaller inductance."

- question: "Because inductors store energy rather than dissipate it, the formulas for combining series and parallel inductor networks differ from those used for resistors."
  type: true-false
  answer: false
  explanation: "The combination formulas are mathematically identical: series inductors add (L_eq = L₁ + L₂ + ...) just like series resistors, and parallel inductors use the reciprocal sum (1/L_eq = 1/L₁ + 1/L₂ + ...) just like parallel resistors. The formulas follow from applying KVL/KCL to v = L·(di/dt), which has the same mathematical structure as V = IR with respect to how elements combine. The distinction between energy storage and dissipation changes the circuit's transient behavior but not the combining rules for equivalent inductance."

- question: "Starting from v = L·(di/dt) and Kirchhoff's current law, explain why inductors in parallel combine with the formula 1/L_eq = 1/L₁ + 1/L₂."
  type: short-answer
  answer: "In parallel, both inductors share the same voltage v across their terminals. By KCL, the total current derivative is di_total/dt = di₁/dt + di₂/dt. Since each inductor sees voltage v, its current derivative is di/dt = v/L, giving di_total/dt = v/L₁ + v/L₂ = v·(1/L₁ + 1/L₂). For the equivalent inductance, di_total/dt = v/L_eq, so 1/L_eq = 1/L₁ + 1/L₂. This mirrors the parallel resistor derivation (I_total = V/R₁ + V/R₂) because v = L·di/dt and V = IR have the same algebraic structure with respect to how branch quantities add."
  explanation: "The derivation should make clear that the 'reciprocal sum' rule is not a fact to memorize but a consequence of KCL plus the constitutive relation v = L·di/dt. The same logical structure (shared voltage → additive current derivatives → reciprocal inductances) applies because KCL doesn't care whether elements are resistors or inductors. Understanding the derivation also clarifies the analogy's limits: the formula gives L_eq for DC and AC analysis, but in transient circuits you must still write the differential equation, not just replace the network with L_eq and apply Ohm's law."
```

## Explainer

From your study of energy storage elements, you know that an inductor obeys v = L·(di/dt): the voltage across an inductor is proportional to the rate of change of the current through it. The inductance L is the constant of proportionality and is set by the physical geometry — the number of turns, the core material, and the cross-sectional area. When you connect multiple inductors together, the combination behaves as a single **equivalent inductance** L_eq, and the rules for finding it follow directly from applying v = L·di/dt together with Kirchhoff's laws — exactly the same reasoning you used to derive series and parallel resistor formulas.

For **inductors in series**, the same current flows through every inductor in the chain (there is no branch point). Applying KVL around the loop: the total voltage is the sum of the individual voltages. Since each inductor sees the same di/dt, v_total = L₁·(di/dt) + L₂·(di/dt) + ... = (L₁ + L₂ + ...)·(di/dt). Comparing with v = L_eq·(di/dt) gives L_eq = L₁ + L₂ + ... Series inductors add directly, just like series resistors. Each inductor contributes its own opposition to current change, and the series combination is collectively harder to drive.

For **inductors in parallel**, all inductors share the same voltage across their terminals. The total current is the sum of the individual currents, so di_total/dt = v/L₁ + v/L₂ + ... = v·(1/L₁ + 1/L₂ + ...). Comparing with di/dt = v/L_eq gives 1/L_eq = 1/L₁ + 1/L₂ + ... — the parallel combination law, again mirroring resistors. Parallel inductors share the burden of handling current changes, and the combination is easier to drive than any single element alone. For two inductors in parallel, L_eq = (L₁·L₂)/(L₁ + L₂) — the "product over sum" shortcut.

The analogy with resistors is deep but has an important flip: resistors dissipate energy, while inductors store it in a magnetic field and return it. This means the value of combining inductors matters not just for steady-state current but for transient behavior and energy storage. In power converter design, inductors are often placed in series to increase effective inductance (slowing current changes, smoothing ripple), or in parallel to distribute current and reduce the current handled by any single component. In tuned LC circuits, the equivalent inductance directly sets the resonant frequency ω₀ = 1/√(L_eq·C), so combining inductors is a practical tool for tuning a filter to a desired frequency without rewinding a custom coil.
