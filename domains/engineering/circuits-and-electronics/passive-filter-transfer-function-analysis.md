---
id: passive-filter-transfer-function-analysis
title: Passive Filter Transfer Function Analysis
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: AC-Kirchhoff-laws-phasor-domain
  type: hard
- id: series-resonance-characteristics
  type: soft
builds-toward:
- first-order-passive-filters
- second-order-passive-filters
tags:
- filters
- transfer-function
- magnitude-response
- phase-response
stage: advanced
status: validated
---

# Passive Filter Transfer Function Analysis

## Core Idea
A filter's transfer function H(jω) = V_out/V_in is a ratio of phasors that characterizes frequency response. The magnitude |H(jω)| and phase ∠H(jω) show which frequencies are passed or attenuated. Passive filters (built with R, L, C) have transfer functions that are ratios of polynomials in jω, leading to characteristic rolloff rates.

## Questions

```yaml
- question: "An RC low-pass filter has cutoff frequency ω_c = 1/RC. At exactly ω = ω_c, what is the magnitude of the transfer function |H(jω)|?"
  type: multiple-choice
  options:
    - "1 — the signal passes through at full amplitude at the cutoff"
    - "1/√2 ≈ 0.707, corresponding to −3 dB attenuation"
    - "0 — the signal is completely blocked at the cutoff frequency"
    - "1/2 — the signal amplitude is exactly halved"
  answer: 1
  explanation: "At the cutoff frequency, |H(jω_c)| = 1/√(1 + (ω_c·RC)²) = 1/√(1+1) = 1/√2 ≈ 0.707. This is the standard definition of the cutoff: power is halved (−3 dB), not amplitude. The signal is neither fully passed nor fully blocked — that only happens asymptotically at ω = 0 and ω → ∞. Option D is a common confusion; amplitude of 1/2 would correspond to −6 dB."

- question: "A designer needs a passive filter that rolls off at −40 dB/decade. What determines whether this is achievable and how?"
  type: multiple-choice
  options:
    - "By choosing a small enough RC time constant in a first-order filter"
    - "By using a second-order RLC filter — rolloff rate is set by circuit order, not component values"
    - "By cascading two resistors without any reactive components"
    - "By lowering the supply voltage, which steepens the attenuation slope"
  answer: 1
  explanation: "Rolloff rate is determined by the order of the filter. Each pole in the transfer function contributes −20 dB/decade beyond the cutoff. A first-order RC or RL filter always rolls off at −20 dB/decade regardless of R and C values — changing those shifts the cutoff frequency, not the slope. A −40 dB/decade rolloff requires a second-order filter (e.g., an RLC circuit). Component values set *where* the rolloff begins; circuit order sets *how steeply* it falls."

- question: "For a first-order RC low-pass filter, the phase shift ∠H(jω) approaches −90° as ω → ∞."
  type: true-false
  answer: true
  explanation: "The phase is ∠H(jω) = −arctan(ωRC). As ω → ∞, arctan(ωRC) → π/2, so the phase approaches −90°. At ω = 0 it is 0°; at the cutoff frequency it is −45°. This progressive phase shift represents increasing time delay at higher frequencies — a critical practical concern in control systems, where accumulated phase shift reduces phase margin and can cause instability."

- question: "The transfer function H(jω) should be recalculated for each new input frequency, just as phasor analysis requires knowing the frequency in advance."
  type: true-false
  answer: false
  explanation: "This conflates phasor analysis with transfer function analysis. Phasor analysis computes a single voltage ratio at one chosen frequency. The transfer function H(jω) is an analytic function of ω that characterizes the circuit's response across ALL frequencies simultaneously — you evaluate it at any ω of interest without redoing the circuit analysis. This is the conceptual shift: from reasoning about 'what happens at this frequency' to 'what does this circuit do to every frequency at once.'"

- question: "What is the key conceptual difference between using the transfer function H(jω) to analyze a filter versus performing a single-frequency phasor analysis?"
  type: short-answer
  answer: "Phasor analysis yields a single gain and phase value at one specific frequency. The transfer function treats frequency as a variable, producing an analytic expression that describes the circuit's gain and phase shift at every frequency simultaneously — revealing the passband, stopband, rolloff rate, and cutoff in one expression."
  explanation: "The power of the transfer function is that it turns the question 'what happens at this frequency?' into 'what does this circuit do to the entire spectrum?' The magnitude |H(jω)| gives the gain at each frequency; the phase ∠H(jω) gives the time delay. Both are read directly from the same expression derived once from the voltage divider ratio. This is what allows filter design to specify performance across a bandwidth rather than at a single point."
```

## Explainer

From your work with phasor-domain KVL, you know how to write voltage divider expressions with complex impedances: V̅_out = V̅_in · Z₂ / (Z₁ + Z₂). The **transfer function** H(jω) = V̅_out / V̅_in is exactly that ratio — but instead of thinking of it as a number for one particular frequency, you treat it as a function of ω and ask how the circuit responds across all frequencies. This is the conceptual shift from phasor analysis (one frequency at a time) to filter analysis (all frequencies simultaneously).

Consider a simple RC low-pass filter: a resistor R in series with the input, a capacitor C to ground, with the output taken across the capacitor. The capacitor's impedance is Z_C = 1/(jωC). Writing the voltage divider: H(jω) = Z_C / (R + Z_C) = 1 / (1 + jωRC). Now compute the magnitude: |H(jω)| = 1 / √(1 + (ωRC)²). At low frequencies (ω → 0), the denominator approaches 1, so |H| ≈ 1 — the signal passes through unchanged. At high frequencies (ω → ∞), the denominator grows without bound, so |H| → 0 — the signal is blocked. The transition happens around the **cutoff frequency** ω_c = 1/RC, where |H| = 1/√2 ≈ 0.707, which corresponds to a −3 dB attenuation. The capacitor acts like an open circuit at low ω (blocks DC... but wait, at DC, Z_C → ∞, so the output equals the input!) and a short circuit at high ω (shunting the signal to ground).

The phase is ∠H(jω) = −arctan(ωRC). At low frequencies the phase shift is near zero; at the cutoff frequency it is −45°; at very high frequencies it approaches −90°. Phase shift matters because it represents a time delay — a sinusoid at the output lags behind the input. For audio applications this is often acceptable; for control systems the accumulated phase shift can cause instability. Understanding both magnitude and phase is essential for using filters in larger systems.

For passive filters, the **rolloff rate** beyond the cutoff frequency is determined by circuit order. A first-order RC or RL filter rolls off at −20 dB/decade (the magnitude halves every time frequency doubles). A second-order RLC filter rolls off at −40 dB/decade and can exhibit resonance: the denominator polynomial has complex roots, causing the magnitude to peak near the resonant frequency ω₀ = 1/√(LC) before falling. By combining filter stages or using higher-order RLC networks, you can build steeper rolloffs. The transfer function's polynomial structure — specifically the locations of its poles and zeros in the complex plane — fully predicts these behaviors, connecting passive filter analysis directly to the poles-and-zeros framework you'll use for more general system analysis.
