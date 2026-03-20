---
id: frequency-response-analysis-bode
title: Frequency Response and Bode Plot Analysis
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: impedance-admittance-networks
  type: hard
builds-toward:
- filter-design-specifications
- feedback-control-fundamentals
tags:
- frequency-response
- bode-plots
stage: advanced
status: draft
---

# Frequency Response and Bode Plot Analysis

## Core Idea
Bode plots display magnitude (in dB) and phase (in degrees) of transfer functions versus frequency on logarithmic scales. For a transfer function H(jω), magnitude is 20·log₁₀|H(jω)| dB. Asymptotic Bode plots use slopes of ±20 dB/decade for poles/zeros and ±90°/decade for phase. Bode plots simplify design and analysis of frequency-dependent circuits by linearizing the logarithmic response.

## Explainer

From your study of impedance and admittance networks, you know that capacitors and inductors present reactances that depend on frequency: X_C = 1/(ωC), X_L = ωL. When a circuit contains these elements, its transfer function — the ratio of output to input as a function of frequency — varies across the spectrum. A **Bode plot** is a systematic way to visualize this dependence across many decades of frequency simultaneously. Rather than plotting the magnitude |H(jω)| directly, Bode plots use the **decibel** scale: 20 log₁₀|H|. This transforms multiplicative gains into additive dB values and compresses a dynamic range of millions into a readable scale. Separately, the phase angle of H(jω) is plotted in degrees versus log frequency.

The real power of Bode plots comes from how poles and zeros of H(jω) appear. A **pole** at angular frequency ω_p contributes a factor 1/(1 + jω/ω_p) to the transfer function. Below ω_p, this factor's magnitude is approximately 1 (0 dB). Above ω_p, the magnitude decreases as ω_p/ω — a straight line with slope −20 dB per decade on the log-log plot. The **asymptotic Bode approximation** replaces the actual smooth curve with two straight line segments meeting at the **corner frequency** ω_p; the true response deviates by at most 3 dB at the corner itself. A **zero** at ω_z contributes the mirror image: the factor (1 + jω/ω_z) adds +20 dB/decade above its corner frequency. For complex conjugate pole pairs (underdamped second-order systems), there is a resonant peak near the natural frequency, with height and width determined by the damping ratio.

The phase Bode plot follows parallel asymptotic logic. A real pole at ω_p contributes 0° phase well below the corner, −90° well above it, and a transition spanning roughly a decade on each side of ω_p. The complete circuit's phase response is the sum of contributions from all poles and zeros, readable directly from the Bode diagram by adding asymptotic segments. This additivity — a direct consequence of the logarithm converting products into sums — is what makes Bode analysis powerful for cascaded circuits: the overall Bode plot of a cascade is simply the sum of the individual plots in dB and degrees.

Putting it together: to sketch the Bode magnitude plot for a transfer function, identify the DC gain (value as ω → 0), locate each pole and zero on the frequency axis, and draw asymptotic magnitude starting from the DC gain, bending down by 20 dB/decade at each pole and up by 20 dB/decade at each zero. For a simple RC low-pass filter H(jω) = 1/(1 + jωRC), the single pole is at ω_p = 1/RC. Below 1/RC, the gain is 0 dB; above 1/RC, it rolls off at −20 dB/decade — this corner frequency defines the **−3 dB bandwidth** of the filter, the frequency at which the output power is halved.

Bode plots are the foundational tool for filter design and feedback control analysis, both of which you'll study next. In filter design, you specify the desired frequency response (pass-band gain, stop-band attenuation, transition bandwidth) and work backward to the pole-zero configuration that achieves it. In feedback control, Bode plots reveal **gain margin** and **phase margin** — how much gain increase or phase lag the loop can tolerate before becoming unstable. The Bode framework makes these analyses tractable by exposing the loop's frequency-dependent behavior in a form where design targets can be read directly off the graph.
