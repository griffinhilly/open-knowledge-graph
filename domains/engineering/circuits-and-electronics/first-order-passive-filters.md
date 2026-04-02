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
stage: advanced
status: validated
---

# First-Order Passive Filters

## Core Idea
First-order RC and RL filters have a single pole at the corner frequency ω_c = 1/τ. Low-pass filters (RC or RL) have -20 dB/decade rolloff above the corner; high-pass filters have +20 dB/decade rolloff below the corner. Phase shift varies from 0° to ±90° around the corner frequency. These simple filters are building blocks for complex filter designs.

## Questions

```yaml
- question: "A first-order low-pass RC filter has R = 1 kΩ and C = 1 μF. Approximately what is the gain in dB at a frequency ten times the corner frequency?"
  type: multiple-choice
  options:
    - "Approximately 0 dB — the signal passes without attenuation"
    - "Approximately −3 dB — the corner frequency marks only a slight rolloff"
    - "Approximately −20 dB — one decade above the corner produces −20 dB of attenuation"
    - "Approximately −40 dB — the rolloff doubles past the corner frequency"
  answer: 2
  explanation: "The corner frequency is ω_c = 1/RC = 1/(1000 × 10⁻⁶) = 1000 rad/s. At ten times the corner frequency (10ω_c), the Bode approximation gives −20 dB/decade × 1 decade = −20 dB of attenuation. The −20 dB/decade rolloff is the signature of a single-pole (first-order) filter: every factor-of-10 increase in frequency above the corner attenuates by another 20 dB. The −40 dB/decade rolloff belongs to a two-pole (second-order) filter."

- question: "Why does a first-order filter produce exactly −20 dB/decade rolloff rather than −10 or −40 dB/decade?"
  type: multiple-choice
  options:
    - "−20 dB/decade is set by the IEC standard for passive filter design"
    - "The transfer function magnitude falls as 1/ω for large ω; each decade of frequency multiplies ω by 10, and 20·log₁₀(10) = 20 dB"
    - "Energy stored in the capacitor decreases exponentially with frequency"
    - "−20 dB/decade is the rolloff of any passive filter regardless of order"
  answer: 1
  explanation: "For a first-order low-pass filter, |H(jω)| ≈ ω_c/ω for ω >> ω_c. When frequency increases by a decade (factor of 10), magnitude decreases by a factor of 10, which is 20·log₁₀(10) = 20 dB. Each additional pole adds another factor of 1/ω to the magnitude rolloff, adding another 20 dB/decade — so a second-order filter gives −40 dB/decade, third-order −60 dB/decade, and so on."

- question: "In a first-order RC circuit, which element you take the output voltage across determines whether you get a low-pass or high-pass response."
  type: true-false
  answer: true
  explanation: "The capacitor's impedance Z_C = 1/(jωC) is large at low frequencies and small at high frequencies. Taking V_out across the capacitor: at low frequencies the capacitor has high impedance and captures most of the voltage (low-pass). Taking V_out across the resistor: at high frequencies the capacitor has low impedance, leaving most of the voltage drop on the resistor (high-pass). Same circuit, different measurement point — different filter type."

- question: "At the corner frequency of a first-order low-pass RC filter, the output voltage is exactly half the input voltage."
  type: true-false
  answer: false
  explanation: "At the corner frequency, the gain is 1/√2 ≈ 0.707 (not 0.5), corresponding to −3 dB. The factor of 1/√2 comes from |H(jω_c)| = 1/√(1 + (ω_c/ω_c)²) = 1/√2. A gain of 0.5 would be −6 dB. The phase shift at the corner frequency is −45° for a low-pass filter. Both the −3 dB magnitude and −45° phase are signatures that uniquely identify the corner frequency."

- question: "Why is the −3 dB corner frequency also called the 'half-power frequency,' and what is its relationship to the time-domain time constant τ?"
  type: short-answer
  answer: "Power is proportional to voltage squared. At the corner frequency the voltage gain is 1/√2, so delivered power is (1/√2)² = 1/2 of the passband power — hence 'half-power frequency.' The corner frequency is ω_c = 1/τ, where τ = RC (or L/R for RL filters). A larger time constant means the capacitor charges and discharges more slowly in the time domain, so it cannot follow rapid (high-frequency) changes — equivalently, the corner frequency is lower and the passband is narrower. Smaller τ means faster transient response and higher corner frequency (wider bandwidth). Time constant and bandwidth are reciprocals."
  explanation: "This relationship is not coincidental — it is the same physics in two domains. A capacitor with large τ acts as a better integrator (averages fast fluctuations), which corresponds directly to more aggressive high-frequency attenuation. Understanding both perspectives simultaneously is essential for filter design: the time-domain spec (settling time) and the frequency-domain spec (bandwidth) are linked by τ = 1/ω_c."
```

## Explainer

You know from transfer function analysis that a filter's frequency response describes how it scales and phase-shifts sinusoids at each frequency. First-order RC and RL filters make this concrete with the simplest possible case: one reactive element, one resistor, and a transfer function with a single **pole**. Understanding these filters deeply gives you the foundation to analyze any filter as a combination of simpler building blocks.

The **corner frequency** (or cutoff frequency) ω_c = 1/τ — where τ = RC for RC circuits and τ = L/R for RL circuits — is the pivot point of the filter's behavior. At frequencies well below ω_c, the filter passes signals nearly unchanged (gain ≈ 1, phase ≈ 0°). At frequencies well above ω_c, the filter substantially attenuates the signal. For a **low-pass RC filter** (output taken across the capacitor), the Bode magnitude plot is flat at 0 dB below the corner, then falls at −20 dB per decade above it — meaning every tenfold increase in frequency beyond the corner halves the output amplitude in a logarithmic sense. The −20 dB/decade rolloff is the signature of a single pole, and it's why first-order filters are sometimes called "single-pole" filters.

A **high-pass filter** inverts the behavior: signals are attenuated at low frequencies and passed at high frequencies. In an RC high-pass (output taken across the resistor), the magnitude rises at +20 dB/decade below the corner and levels off above it. The physical intuition follows directly from impedance: a capacitor has impedance 1/(jωC), which is very large at low frequencies (blocking DC and slow signals) and small at high frequencies (passing fast signals). If you take the output across the capacitor, you get a low-pass response; across the resistor, a high-pass response. Swapping which element you measure determines the filter type.

Phase shift is the other half of the filter's character and should not be treated as an afterthought. At the corner frequency, both low-pass and high-pass first-order filters introduce exactly ±45° of phase shift. The low-pass filter produces −45° (output lags input by 45°) and approaches −90° as frequency increases far above the corner. This phase shift matters for control systems — it contributes to the total phase lag in a feedback loop that determines stability. The **−3 dB point**, where the gain drops to 1/√2 ≈ 0.707 of its passband value, coincides precisely with the corner frequency, directly linking the time-domain time constant τ to the frequency-domain bandwidth. Smaller τ means higher corner frequency and wider passband; larger τ means narrower bandwidth and slower transient response.
