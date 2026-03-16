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
status: draft
---

# Series and Parallel Inductor Networks

## Core Idea
Inductors in series sum directly: L_eq = L₁ + L₂ + ... Inductors in parallel sum reciprocals: 1/L_eq = 1/L₁ + 1/L₂ + ... These relationships mirror resistor behavior. Series inductors share total applied voltage and all carry the same current; parallel inductors share voltage and distribute current inversely to inductance. Inductor networks are critical in power supply design and tuned circuits.

## Explainer

From your study of energy storage elements, you know that an inductor obeys v = L·(di/dt): the voltage across an inductor is proportional to the rate of change of the current through it. The inductance L is the constant of proportionality and is set by the physical geometry — the number of turns, the core material, and the cross-sectional area. When you connect multiple inductors together, the combination behaves as a single **equivalent inductance** L_eq, and the rules for finding it follow directly from applying v = L·di/dt together with Kirchhoff's laws — exactly the same reasoning you used to derive series and parallel resistor formulas.

For **inductors in series**, the same current flows through every inductor in the chain (there is no branch point). Applying KVL around the loop: the total voltage is the sum of the individual voltages. Since each inductor sees the same di/dt, v_total = L₁·(di/dt) + L₂·(di/dt) + ... = (L₁ + L₂ + ...)·(di/dt). Comparing with v = L_eq·(di/dt) gives L_eq = L₁ + L₂ + ... Series inductors add directly, just like series resistors. Each inductor contributes its own opposition to current change, and the series combination is collectively harder to drive.

For **inductors in parallel**, all inductors share the same voltage across their terminals. The total current is the sum of the individual currents, so di_total/dt = v/L₁ + v/L₂ + ... = v·(1/L₁ + 1/L₂ + ...). Comparing with di/dt = v/L_eq gives 1/L_eq = 1/L₁ + 1/L₂ + ... — the parallel combination law, again mirroring resistors. Parallel inductors share the burden of handling current changes, and the combination is easier to drive than any single element alone. For two inductors in parallel, L_eq = (L₁·L₂)/(L₁ + L₂) — the "product over sum" shortcut.

The analogy with resistors is deep but has an important flip: resistors dissipate energy, while inductors store it in a magnetic field and return it. This means the value of combining inductors matters not just for steady-state current but for transient behavior and energy storage. In power converter design, inductors are often placed in series to increase effective inductance (slowing current changes, smoothing ripple), or in parallel to distribute current and reduce the current handled by any single component. In tuned LC circuits, the equivalent inductance directly sets the resonant frequency ω₀ = 1/√(L_eq·C), so combining inductors is a practical tool for tuning a filter to a desired frequency without rewinding a custom coil.
