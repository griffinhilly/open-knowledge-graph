---
id: passive-filter-transfer-function-analysis
title: Passive Filter Transfer Function Analysis
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: AC-Kirchhoff-laws-phasor-domain
  type: hard
- id: series-RLC-resonance-characteristics
  type: soft
builds-toward:
- first-order-passive-filters
- second-order-passive-filters
tags:
- filters
- transfer-function
- magnitude-response
- phase-response
stage: formal-systems
status: draft
---

# Passive Filter Transfer Function Analysis

## Core Idea
A filter's transfer function H(jω) = V_out/V_in is a ratio of phasors that characterizes frequency response. The magnitude |H(jω)| and phase ∠H(jω) show which frequencies are passed or attenuated. Passive filters (built with R, L, C) have transfer functions that are ratios of polynomials in jω, leading to characteristic rolloff rates.

## Explainer

From your work with phasor-domain KVL, you know how to write voltage divider expressions with complex impedances: V̅_out = V̅_in · Z₂ / (Z₁ + Z₂). The **transfer function** H(jω) = V̅_out / V̅_in is exactly that ratio — but instead of thinking of it as a number for one particular frequency, you treat it as a function of ω and ask how the circuit responds across all frequencies. This is the conceptual shift from phasor analysis (one frequency at a time) to filter analysis (all frequencies simultaneously).

Consider a simple RC low-pass filter: a resistor R in series with the input, a capacitor C to ground, with the output taken across the capacitor. The capacitor's impedance is Z_C = 1/(jωC). Writing the voltage divider: H(jω) = Z_C / (R + Z_C) = 1 / (1 + jωRC). Now compute the magnitude: |H(jω)| = 1 / √(1 + (ωRC)²). At low frequencies (ω → 0), the denominator approaches 1, so |H| ≈ 1 — the signal passes through unchanged. At high frequencies (ω → ∞), the denominator grows without bound, so |H| → 0 — the signal is blocked. The transition happens around the **cutoff frequency** ω_c = 1/RC, where |H| = 1/√2 ≈ 0.707, which corresponds to a −3 dB attenuation. The capacitor acts like an open circuit at low ω (blocks DC... but wait, at DC, Z_C → ∞, so the output equals the input!) and a short circuit at high ω (shunting the signal to ground).

The phase is ∠H(jω) = −arctan(ωRC). At low frequencies the phase shift is near zero; at the cutoff frequency it is −45°; at very high frequencies it approaches −90°. Phase shift matters because it represents a time delay — a sinusoid at the output lags behind the input. For audio applications this is often acceptable; for control systems the accumulated phase shift can cause instability. Understanding both magnitude and phase is essential for using filters in larger systems.

For passive filters, the **rolloff rate** beyond the cutoff frequency is determined by circuit order. A first-order RC or RL filter rolls off at −20 dB/decade (the magnitude halves every time frequency doubles). A second-order RLC filter rolls off at −40 dB/decade and can exhibit resonance: the denominator polynomial has complex roots, causing the magnitude to peak near the resonant frequency ω₀ = 1/√(LC) before falling. By combining filter stages or using higher-order RLC networks, you can build steeper rolloffs. The transfer function's polynomial structure — specifically the locations of its poles and zeros in the complex plane — fully predicts these behaviors, connecting passive filter analysis directly to the poles-and-zeros framework you'll use for more general system analysis.
