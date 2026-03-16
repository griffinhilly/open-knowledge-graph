---
id: series-parallel-capacitor-networks
title: Series and Parallel Capacitor Networks
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: capacitor-inductor-energy-storage
  type: hard
- id: series-parallel-resistor-analysis
  type: soft
builds-toward:
- transient-response-rc-circuits
- impedance-admittance-networks
tags:
- capacitors
- reactive-circuits
- energy-storage
stage: formal-systems
status: draft
---

# Series and Parallel Capacitor Networks

## Core Idea
Capacitors in series sum reciprocals: 1/C_eq = 1/C₁ + 1/C₂ + ... Capacitors in parallel sum directly: C_eq = C₁ + C₂ + ... These relationships are opposite to resistor combinations. Series capacitors share total applied voltage and store equal charge; parallel capacitors share the same voltage and distribute total charge. Understanding capacitor networks is essential for filter design and timing circuits.

## Explainer

You know how resistors combine from series-parallel analysis — series resistors add directly, parallel resistors add reciprocals. Capacitors do the opposite at every step, and understanding *why* builds deeper intuition than memorizing the formulas.

Recall that capacitance is defined as C = Q/V: it measures how much charge is stored per volt of applied voltage. A large capacitor stores more charge at a given voltage; a small one stores less. For **parallel capacitors**, both devices are connected between the same two nodes — they share the same voltage V. Each stores its own charge: Q₁ = C₁V and Q₂ = C₂V. The total charge drawn from the source is Q_total = Q₁ + Q₂ = (C₁ + C₂)V. Since C_eq = Q_total/V, the parallel equivalent is C_eq = C₁ + C₂ — capacitances add directly. Physically, parallel capacitors act as one larger capacitor with combined plate area, which is why adding plates increases capacitance.

For **series capacitors**, the same current flows through all elements in sequence. This enforces equal charge on each capacitor: the charge that flows onto one plate of C₁ must equal the charge flowing off the adjacent plate of C₂ (those plates form an isolated conductor — charge cannot appear or disappear within it). So Q₁ = Q₂ = Q. But voltage distributes across each element: V_total = V₁ + V₂ = Q/C₁ + Q/C₂ = Q(1/C₁ + 1/C₂). Since V_total = Q/C_eq, we get 1/C_eq = 1/C₁ + 1/C₂ — the reciprocal rule. Physically, series capacitors act as one capacitor with the combined thickness of both dielectrics; more separation between opposite charges means less capacitance.

The inversion relative to resistors is not arbitrary — it follows directly from duality. Resistors in series share the same current, so resistance (voltage per unit current) adds. Capacitors in series share the same charge, so the quantity Q/V inverted — that is, 1/C — adds. This is the pattern: when a circuit variable is shared, the corresponding impedance-like quantity adds. In AC analysis, capacitive reactance X_C = 1/(ωC) behaves exactly like resistance: series reactances add and parallel reactances combine reciprocally, now consistent with resistors. The apparent inversion at DC is really the same rule applied to the underlying physical variable — charge instead of current — that capacitors share in series.
