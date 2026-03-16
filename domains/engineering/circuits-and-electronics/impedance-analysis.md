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

## Explainer

From your work with phasors, you know that sinusoidal voltages and currents in steady state can be represented as complex amplitudes — phasors — that encode both magnitude and phase. The power of this representation is that differentiation and integration in the time domain become simple multiplication and division in the phasor domain. **Impedance** is the concept that completes this picture: it is the ratio Z = V/I of the voltage phasor to the current phasor, generalizing resistance to any linear element at any frequency.

For a resistor, Z_R = R — real and frequency-independent, just as you know from DC analysis. For a capacitor, the voltage-current relationship i = C(dv/dt) transforms into I = jωC·V in phasor form, giving Z_C = 1/(jωC). This is purely imaginary and decreases as frequency ω rises: at high frequency, the capacitor barely opposes changing signals. For an inductor, v = L(di/dt) transforms into V = jωL·I, giving Z_L = jωL — also purely imaginary but increasing with frequency: the inductor increasingly resists rapid changes. The imaginary part of impedance is the **reactance** X: positive (inductive) when the element stores energy in a magnetic field, negative (capacitive) when it stores energy in an electric field.

The pivotal insight is that impedances combine by exactly the same rules as resistances: series impedances add, parallel impedances combine as reciprocals. This means every circuit analysis technique you learned for DC — Kirchhoff's laws, voltage dividers, Norton and Thévenin equivalents, node voltage, mesh current — applies unchanged to AC circuits, as long as you replace resistance with impedance and work in the phasor domain with complex arithmetic. A voltage divider with two impedances gives V_out/V_in = Z_2/(Z_1 + Z_2), and because Z depends on ω, this ratio changes with frequency. That frequency dependence is the foundation of all filter design.

**Admittance** Y = 1/Z is the parallel dual of impedance: it is convenient when elements are in parallel, since parallel admittances add. The real part of admittance is **conductance** G, and the imaginary part is **susceptance** B. The relationship G = 1/R holds only for a purely resistive element — in general, G ≠ 1/Re(Z) because the real part of 1/Z is not the reciprocal of the real part of Z. This asymmetry is a common source of error when working with mixed RLC networks. The clean workflow is always to express Z in rectangular form, apply complex arithmetic correctly, and convert to Y only when a parallel calculation demands it.
