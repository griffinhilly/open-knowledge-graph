---
id: first-order-passive-filters
title: First-Order Passive Filters
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: passive-filter-transfer-function-analysis
  type: hard
- id: rc-circuit-charging-and-discharging
  type: soft
builds-toward:
- bandpass-and-bandstop-filter-design
tags:
- RC-filters
- RL-filters
- rolloff
- corner-frequency
stage: formal-systems
status: draft
---

# First-Order Passive Filters

## Core Idea
First-order RC and RL filters have a single pole at the corner frequency ω_c = 1/τ. Low-pass filters (RC or RL) have -20 dB/decade rolloff above the corner; high-pass filters have +20 dB/decade rolloff below the corner. Phase shift varies from 0° to ±90° around the corner frequency. These simple filters are building blocks for complex filter designs.

## Explainer

You know from transfer function analysis that a filter's frequency response describes how it scales and phase-shifts sinusoids at each frequency. First-order RC and RL filters make this concrete with the simplest possible case: one reactive element, one resistor, and a transfer function with a single **pole**. Understanding these filters deeply gives you the foundation to analyze any filter as a combination of simpler building blocks.

The **corner frequency** (or cutoff frequency) ω_c = 1/τ — where τ = RC for RC circuits and τ = L/R for RL circuits — is the pivot point of the filter's behavior. At frequencies well below ω_c, the filter passes signals nearly unchanged (gain ≈ 1, phase ≈ 0°). At frequencies well above ω_c, the filter substantially attenuates the signal. For a **low-pass RC filter** (output taken across the capacitor), the Bode magnitude plot is flat at 0 dB below the corner, then falls at −20 dB per decade above it — meaning every tenfold increase in frequency beyond the corner halves the output amplitude in a logarithmic sense. The −20 dB/decade rolloff is the signature of a single pole, and it's why first-order filters are sometimes called "single-pole" filters.

A **high-pass filter** inverts the behavior: signals are attenuated at low frequencies and passed at high frequencies. In an RC high-pass (output taken across the resistor), the magnitude rises at +20 dB/decade below the corner and levels off above it. The physical intuition follows directly from impedance: a capacitor has impedance 1/(jωC), which is very large at low frequencies (blocking DC and slow signals) and small at high frequencies (passing fast signals). If you take the output across the capacitor, you get a low-pass response; across the resistor, a high-pass response. Swapping which element you measure determines the filter type.

Phase shift is the other half of the filter's character and should not be treated as an afterthought. At the corner frequency, both low-pass and high-pass first-order filters introduce exactly ±45° of phase shift. The low-pass filter produces −45° (output lags input by 45°) and approaches −90° as frequency increases far above the corner. This phase shift matters for control systems — it contributes to the total phase lag in a feedback loop that determines stability. The **−3 dB point**, where the gain drops to 1/√2 ≈ 0.707 of its passband value, coincides precisely with the corner frequency, directly linking the time-domain time constant τ to the frequency-domain bandwidth. Smaller τ means higher corner frequency and wider passband; larger τ means narrower bandwidth and slower transient response.
