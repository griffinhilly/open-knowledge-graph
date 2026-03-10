---
id: passive-filter-design
title: Passive Filter Design
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: frequency-response-and-bode-plots
  type: hard
- id: impedance-analysis
  type: hard
- id: resonance-circuits
  type: soft
builds-toward:
- op-amp-circuit-applications
tags:
- filters
- low-pass
- high-pass
- band-pass
- band-stop
- notch
- RC-filter
- RLC-filter
- cutoff-frequency
stage: formal-systems
status: draft
---

# Passive Filter Design

## Core Idea
Passive filters use R, L, and C elements to pass signals in desired frequency bands and attenuate others. A first-order RC low-pass filter has transfer function H(jω) = 1/(1 + jωRC) with cutoff ωc = 1/RC; swapping R and C gives a high-pass filter. Combining low-pass and high-pass stages creates band-pass and band-stop (notch) responses. Adding inductors allows second-order filters with sharper roll-off (−40 dB/decade) and the resonant peaking characteristic of RLC networks. Filter order n determines the asymptotic roll-off rate of −20n dB/decade beyond the cutoff.

## How It's Best Learned
Design filters by specifying the cutoff frequency first, then choosing component values. Use the voltage divider approach with impedances to derive the transfer function algebraically. Compare first-order and second-order responses side by side to see how order affects roll-off sharpness and in-band flatness.

## Common Misconceptions
- Treating the cutoff frequency as an absolute boundary — real filters have gradual roll-offs into the stopband.
- Ignoring loading effects: attaching a load resistance modifies the frequency response unless the load impedance is much larger than the filter's output impedance.
- Assuming passive filters can provide signal gain — passive components can only attenuate; active filters using op-amps are required for gain.
