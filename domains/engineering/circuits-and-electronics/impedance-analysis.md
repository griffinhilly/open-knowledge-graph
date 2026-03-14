---
id: impedance-analysis
title: Impedance and Admittance in AC Circuits
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: phasor-representation
  type: hard
- id: impedance-and-reactance
  type: soft
- id: operations-with-complex-numbers
  type: hard
builds-toward:
- ac-circuit-analysis-methods
- resonance-circuits
- passive-filter-design
tags:
- impedance
- admittance
- reactance
- susceptance
- frequency-dependent
stage: formal-systems
status: validated
---

# Impedance and Admittance in AC Circuits

## Core Idea
Impedance Z = V/I (phasors) generalizes resistance to AC circuits: Z_R = R (real, frequency-independent), Z_C = 1/(jωC) (imaginary, decreases with frequency), and Z_L = jωL (imaginary, increases with frequency). Admittance Y = 1/Z is the parallel dual. Impedances combine in series and parallel using the same rules as resistances, making all DC analysis techniques directly applicable in the phasor domain. The real part of impedance is resistance R; the imaginary part is reactance X; the real part of admittance is conductance G and imaginary part is susceptance B.

## How It's Best Learned
Derive capacitor and inductor impedances from their phasor i-v relationships rather than memorizing them. Practice computing equivalent impedances at several frequencies and observe how the circuit's character shifts from capacitive to inductive across the impedance spectrum.

## Common Misconceptions
- Forgetting impedance is frequency-dependent — the same RLC circuit behaves differently at different frequencies.
- Adding complex impedances by adding only their magnitudes rather than using complex arithmetic.
- Confusing admittance Y = 1/Z with conductance G = 1/R — conductance is only the real part of admittance.
