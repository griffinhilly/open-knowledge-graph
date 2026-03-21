---
id: capacitor-circuits-series-parallel
title: Capacitors in Series and Parallel
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: parallel-plate-capacitor-formula
  type: hard
builds-toward:
- energy-density-electric-field
- dielectric-materials-polarization
tags:
- circuit
- combination
- equivalent
stage: formal-systems
status: draft
---

# Capacitors in Series and Parallel

## Core Idea
Capacitors in parallel have same voltage; equivalent capacitance is C_eq = ΣC_i. In series, charge is same; 1/C_eq = Σ(1/C_i). Series capacitors divide voltage; parallel capacitors sum capacitances.

## How It's Best Learned
Draw circuits with parallel and series configurations, identify equivalent capacitances step-by-step, then verify with limiting cases.

## Questions

```yaml
- question: "Two capacitors, C₁ = 4 μF and C₂ = 12 μF, are connected in series. What is the equivalent capacitance?"
  type: multiple-choice
  options:
    - "16 μF — they add directly"
    - "3 μF — from the reciprocal sum formula"
    - "48 μF — from the product of capacitances"
    - "8 μF — their average"
  answer: 1
  explanation: "For series capacitors: 1/C_eq = 1/C₁ + 1/C₂ = 1/4 + 1/12 = 3/12 + 1/12 = 4/12, so C_eq = 3 μF. Series combination always produces an equivalent capacitance smaller than either individual capacitor. The answer 16 μF (direct addition) is the parallel rule — the most common error is applying parallel addition to a series circuit. Always identify configuration before choosing the formula."

- question: "C₁ = 6 μF and C₂ = 3 μF are connected in series to a 9V battery. What is the charge on each capacitor?"
  type: multiple-choice
  options:
    - "C₁ has charge 54 μC; C₂ has charge 27 μC — proportional to capacitance"
    - "C₁ has charge 18 μC; C₂ has charge 18 μC — they share the same charge"
    - "C₁ has charge 6 μC; C₂ has charge 3 μC — equal to capacitance value"
    - "C₁ has charge 9 μC; C₂ has charge 9 μC — equal shares of battery voltage"
  answer: 1
  explanation: "In series, all capacitors carry the same charge: C_eq = 1/(1/6 + 1/3) = 2 μF; Q = C_eq × V = 2 × 9 = 18 μC. Both C₁ and C₂ have Q = 18 μC. Their voltages differ: V₁ = Q/C₁ = 18/6 = 3V and V₂ = Q/C₂ = 18/3 = 6V (summing to 9V ✓). The larger capacitor drops less voltage — an important and often counterintuitive result. Equal charge, not equal voltage, is the defining feature of series capacitors."

- question: "Connecting capacitors in parallel increases the equivalent capacitance because you are effectively adding plate area that can store charge at the same voltage."
  type: true-false
  answer: true
  explanation: "Parallel capacitors share the same two nodes and thus the same voltage V. Each accumulates charge independently: Q_i = C_i × V. Total charge = (C₁ + C₂ + ...)V, giving C_eq = C₁ + C₂ + .... Physically, parallel connection is equivalent to one large capacitor whose total plate area is the sum of all individual plate areas — and larger plates store more charge at the same voltage. This is why parallel always increases capacitance."

- question: "The combination rules for capacitors follow the same pattern as resistors: capacitors in series add, just as resistors in series add."
  type: true-false
  answer: false
  explanation: "The rules are algebraically mirrored between capacitors and resistors. For resistors: series = add (R_eq = R₁ + R₂), parallel = reciprocal sum (1/R_eq = 1/R₁ + 1/R₂). For capacitors it is exactly reversed: parallel = add (C_eq = C₁ + C₂), series = reciprocal sum (1/C_eq = 1/C₁ + 1/C₂). This swap occurs because capacitors and resistors respond to the same circuit constraints (voltage and charge/current) but in opposite roles. Confusing the two is the most common error in capacitor circuit problems."

- question: "Why do capacitors in series all carry the same charge, even if they have different capacitances? Explain the physical mechanism."
  type: short-answer
  answer: "The conductor between adjacent series capacitors is electrically isolated — no charge can flow onto or off it from the external circuit. When charge +Q builds up on the outer plate of the first capacitor, it repels an equal +Q off the adjacent inner plate, which flows to the next capacitor. This induction propagates through the chain so every capacitor accumulates exactly Q, regardless of its capacitance. Their different capacitances then determine how the total voltage is divided: V = Q/C, so smaller capacitance receives a larger voltage share."
  explanation: "This charge-conservation argument is the physical basis of the series rule. The isolated middle conductor acts as a charge relay, ensuring equal charge everywhere in the chain. The voltage division is a consequence: series capacitors act like a single capacitor with larger effective gap between outer plates, which reduces total capacitance — consistent with 1/C_eq = Σ(1/C_i)."
```

## Explainer

You already know that a parallel-plate capacitor stores charge according to C = Q/V — the capacitance tells you how much charge accumulates per volt of applied voltage. When you combine capacitors in a circuit, the combination rules follow directly from this definition plus two inescapable constraints: voltage is single-valued around any loop, and charge cannot appear from nowhere on isolated conductors.

**Parallel capacitors** share the same two nodes, so they sit across the same voltage V. Each one independently accumulates charge: Q₁ = C₁V, Q₂ = C₂V, and so on. The total charge drawn from the source is Q_total = Q₁ + Q₂ + ... = (C₁ + C₂ + ...)V. Comparing with Q_total = C_eq × V gives C_eq = C₁ + C₂ + ... — capacitances add in parallel. Physically, you are increasing the total plate area that can store charge at the same voltage, so of course the combined device stores more.

**Series capacitors** present a subtler constraint. Consider two capacitors connected end-to-end with no other connections. The segment of conductor between them is electrically isolated — no charge can flow onto or off it from the external circuit. When a charge +Q builds up on the left plate of C₁, it repels an equal +Q off the right plate of C₁, which flows onto the left plate of C₂. By induction the isolated middle conductor redistributes so that each capacitor ends up with exactly the same charge Q. Their voltages differ — V₁ = Q/C₁ and V₂ = Q/C₂ — and the total voltage across the series combination is V = V₁ + V₂ = Q(1/C₁ + 1/C₂). Dividing both sides by Q: 1/C_eq = 1/C₁ + 1/C₂. Series combination reduces capacitance because you are effectively increasing the gap between the "outer" plates while the charge remains fixed.

A useful sanity check: two identical capacitors C in parallel give 2C; the same two in series give C/2. Parallel always increases equivalent capacitance; series always decreases it. For mixed networks, reduce step by step — identify series and parallel sub-groups, replace each with its equivalent, and repeat until one capacitor remains. The rules for capacitors are the algebraic mirror of resistors: the parallel rule for capacitors (add them) is the same form as the series rule for resistors, and vice versa. This swap happens because capacitors and resistors respond to the same circuit constraints (V and I/Q) but in opposite roles.
