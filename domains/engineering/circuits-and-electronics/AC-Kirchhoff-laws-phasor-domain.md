---
id: AC-Kirchhoff-laws-phasor-domain
title: AC Kirchhoff's Laws in the Phasor Domain
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: phasor-conversion-and-representation
  type: hard
- id: complex-impedance-networks-ac
  type: hard
- id: complex-exponential-form
  type: soft
builds-toward:
- AC-power-calculation-and-factor
- passive-filter-transfer-function-analysis
tags:
- Kirchhoff-laws
- phasor-domain
- AC-analysis
stage: advanced
status: draft
---

# AC Kirchhoff's Laws in the Phasor Domain

## Core Idea
Kirchhoff's voltage and current laws apply directly to phasors: ΣV̅ = 0 around a loop and ΣI̅ = 0 at a node. Nodal and mesh analysis, superposition, and Thévenin/Norton equivalents all work in the phasor domain. This unified approach eliminates the need to solve differential equations for AC steady state.

## Explainer

You've already seen that phasors convert sinusoidal voltages and currents into complex numbers, and that impedance Z = R + jX generalizes resistance to inductors and capacitors. The payoff for all that setup arrives now: **Kirchhoff's laws work on phasors exactly as they work on DC values**, except you use complex arithmetic instead of real arithmetic. KVL says the sum of phasor voltages around any closed loop is zero; KCL says the sum of phasor currents into any node is zero. The fundamental conservation principles don't change — only the numbers become complex.

The practical power of this is enormous. Every DC analysis technique you've learned — nodal analysis, mesh analysis, superposition, voltage dividers, Thévenin equivalents — transfers directly to AC circuits with one substitution: replace resistance R with complex impedance Z. A voltage divider with two resistors becomes a voltage divider with two impedances, and the output phasor is simply Z₂/(Z₁ + Z₂) times the input phasor. The algebra looks identical; the result is a complex number encoding both amplitude and phase. This is far easier than solving the differential equations that describe inductor and capacitor behavior in the time domain.

For nodal analysis in the phasor domain, assign node voltage phasors as unknowns, write KCL at each node using V̅/Z for each branch current, and solve the resulting system of linear equations — now over the complex numbers. The node voltages you find are phasors: their magnitudes are the AC amplitudes at that node, and their angles are the phase shifts relative to your reference. Thévenin equivalents work the same way: find the open-circuit phasor voltage V̅_th and the Thévenin impedance Z_th by deactivating independent sources (short voltage sources, open current sources), then replace the circuit with V̅_th in series with Z_th.

The key conceptual move here is recognizing that the phasor domain doesn't just make calculation easier — it reveals the structure of AC circuits. A circuit's response at a given frequency is completely described by complex numbers (phasors and impedances). As you extend this to analyze filters and power, you'll be asking how the ratio V̅_out/V̅_in depends on frequency ω. That ratio — the **transfer function** — is the bridge from phasor-domain analysis to frequency-response analysis, and it is built directly from the KVL and KCL equations you write here.
