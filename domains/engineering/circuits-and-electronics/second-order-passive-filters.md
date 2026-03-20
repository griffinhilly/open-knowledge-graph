---
id: second-order-passive-filters
title: Second-Order Passive Filters
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: passive-filter-transfer-function-analysis
  type: hard
- id: rlc-circuit-transient-analysis-overview
  type: hard
builds-toward:
- bandpass-and-bandstop-filter-design
tags:
- RLC-filters
- damping
- resonance
- steeper-rolloff
stage: advanced
status: draft
---

# Second-Order Passive Filters

## Core Idea
Second-order filters built from RLC circuits provide -40 dB/decade rolloff and can exhibit resonance peaks or dips depending on damping. The quality factor Q controls the sharpness; low Q gives smooth response while high Q causes peaking. Series and parallel RLC configurations yield different filter characteristics (e.g., series RLC is notch, parallel RLC is peaking).

## Explainer

From your work with first-order RC and RL filters, you know that a single reactive element produces a -20 dB/decade rolloff above (or below) the cutoff frequency. A second-order filter adds a second reactive element — making it an RLC circuit — and something qualitatively new happens. The rolloff steepens to **-40 dB/decade**, meaning the filter cuts twice as sharply. But the bigger change is that the circuit now has a natural resonance frequency where energy can oscillate between the inductor and capacitor, producing behavior impossible with a single reactive element.

The transfer function of a second-order filter contains a quadratic in the denominator: H(s) = ω₀² / (s² + (ω₀/Q)s + ω₀²) for a low-pass prototype. The two key parameters are the **natural frequency** ω₀ = 1/√(LC), which sets where the rolloff begins, and the **quality factor** Q = ω₀ / (R/L) (for a series RLC), which controls the shape of the response near resonance. Q captures the ratio of energy stored to energy dissipated per cycle — a high-Q circuit stores energy efficiently relative to its losses, and so it can sustain oscillations. In filter terms: low Q produces a smooth, overdamped response; high Q produces a peaked response that amplifies signals near ω₀ before sharply attenuating them.

The Q factor is intimately related to the **damping ratio** ζ = 1/(2Q) from your RLC transient analysis. When ζ > 1 (Q < 0.5), the system is overdamped — no peaking in the frequency response, just a gradual rolloff. When ζ = 1/√2 (Q = 1/√2 ≈ 0.707), you get the **Butterworth** condition — the maximally flat response where there is no peaking and the -3 dB point is exactly at ω₀. When ζ < 1/√2 (Q > 0.707), the magnitude response peaks above 0 dB before rolling off, which can be useful for certain equalizer designs but undesirable for most anti-aliasing filters.

The physical configuration determines what kind of filter you get. In a **series RLC** driven from a voltage source, taking the output across the resistor yields a bandpass response (passes signals near ω₀); taking it across the capacitor yields low-pass; taking it across the inductor yields high-pass. Taking the output across the series LC combination (inductor + capacitor in series) gives a **notch** (band-reject) filter, because at resonance the series LC is a short circuit and no voltage appears across it. A **parallel RLC** tank circuit behaves dually — at resonance the parallel LC presents infinite impedance, so all the source current flows through the resistor, producing a bandpass output. These configurations let you sculpt frequency responses that no single-pole RC filter could approach.
