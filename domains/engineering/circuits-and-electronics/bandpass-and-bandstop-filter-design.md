---
id: bandpass-and-bandstop-filter-design
title: Bandpass and Bandstop Filter Design
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: first-order-passive-filters
  type: hard
- id: second-order-passive-filters
  type: hard
builds-toward:
- filter-selection-and-practical-applications
tags:
- bandpass
- bandstop
- notch
- cascade-filters
stage: advanced
status: draft
---

# Bandpass and Bandstop Filter Design

## Core Idea
Bandpass filters allow frequencies within a passband while rejecting others; the passband width and center frequency are set by component values. Bandstop (notch) filters do the opposite. Practical designs cascade first-order and second-order stages to achieve the desired attenuation slope and selectivity. The resonance characteristics of RLC circuits are exploited to create sharp transitions.

## Explainer

You already know that a **low-pass filter** passes low frequencies and blocks high ones, while a **high-pass filter** does the opposite. A **bandpass filter** targets a specific frequency range — passing everything in between and rejecting both low and high extremes. The most intuitive way to build one is to cascade a low-pass and a high-pass filter in series: the low-pass sets the upper edge of the passband, the high-pass sets the lower edge, and only frequencies satisfying both conditions get through. For this to work, the low-pass cutoff must be above the high-pass cutoff; otherwise the regions overlap and nothing passes.

The **center frequency** ω₀ and **bandwidth** BW are the key design parameters. For an RLC bandpass filter, ω₀ = 1/√(LC) — the resonant frequency at which the reactive components cancel, leaving only the resistive impedance. At resonance, the circuit passes signals with minimal attenuation. As you move away from ω₀ in either direction, the impedance imbalance grows and the output falls. The bandwidth is set by the resistance: lower R → higher Q → narrower bandwidth around ω₀. This is why you need your knowledge of second-order filter behavior: the sharpness of the bandpass response is entirely determined by the Q factor of the resonant circuit.

A **bandstop** (or **notch**) filter is the complement: it rejects a specific frequency range and passes everything else. The easiest conceptual construction is to place a low-pass and high-pass filter in *parallel* rather than series — signals that are low enough to pass the low-pass stage, or high enough to pass the high-pass stage, combine at the output, while the target band falls through the gap. RLC circuits can also be configured directly as notch filters, exploiting the same resonance that creates a bandpass peak but routing the resonant impedance to ground instead of the load.

In practice, real designs stack multiple first- and second-order stages to achieve steeper roll-off slopes. Each additional pole adds 20 dB/decade of attenuation beyond the cutoff. A **Butterworth** design maximizes flatness in the passband at the cost of gradual roll-off; a **Chebyshev** design allows ripple in the passband to achieve a sharper transition; an **elliptic** design permits ripple in both passband and stopband for the sharpest possible transition. Selecting among these is an engineering tradeoff: audio applications tolerate Butterworth's gradual roll-off, while interference rejection in communications often demands elliptic steepness.
