---
id: logarithmic-plots-and-frequency-scales
title: Logarithmic Plots and Frequency Scales
domain: engineering
course: control-systems
prerequisites:
- id: sinusoidal-response-magnitude-phase-angle
  type: hard
- id: bode-plot-construction
  type: soft
builds-toward:
- control-loop-design-via-bode-plots
tags:
- bode-plot
- decibel
- logarithmic-frequency
- asymptotic-approximation
stage: advanced
status: draft
---

# Logarithmic Plots and Frequency Scales

## Core Idea
Logarithmic frequency and magnitude scales compress wide dynamic ranges into manageable plots. Magnitude in decibels is 20 log₁₀|G(jω)| dB; logarithmic frequency enables asymptotic approximations of Bode plots where poles and zeros contribute straight-line segments with slopes of ±20 dB/decade.

## Explainer

From your work with sinusoidal frequency response, you know that a system's behavior changes as frequency sweeps from near zero to very high values — filters pass some frequencies and attenuate others, and the gain can vary by factors of thousands. Plotting this on linear axes is nearly useless: a gain of 1000 at low frequency and 0.001 at high frequency would compress all the interesting detail into an unreadable spike at one end. Logarithmic scales solve this by displaying the ratio between values rather than their absolute difference.

The **decibel** (dB) is the standard unit for log-scale magnitude: magnitude in dB = 20 log₁₀|G(jω)|. The factor of 20 comes from the convention for power ratios (10 log₁₀ for power, 20 log₁₀ for amplitude). Key reference points: 0 dB means unity gain (output = input), +20 dB means a factor of 10 gain, −20 dB means a factor of 10 attenuation, +6 dB ≈ factor of 2, −6 dB ≈ factor of ½. These are worth memorizing because they let you read Bode plots at a glance: a gain that drops from 40 dB to 0 dB spans a factor of 100 in amplitude.

The logarithmic frequency axis creates the key simplification: the gain of a first-order pole or zero — a factor like (1 + jω/ωc) — becomes piecewise linear in dB when plotted against log ω. Below the **corner frequency** ωc, the term ≈ 1 (0 dB contribution). Above ωc, the term grows like ω/ωc, contributing 20 log₁₀(ω/ωc) dB — a straight line with slope +20 dB/decade (or −20 dB/decade for a pole). These **asymptotic approximations** let you sketch the entire Bode magnitude plot by hand: start at the DC gain, then add a slope change of ±20 dB/decade at each corner frequency, with the sign determined by whether it is a zero (+) or pole (−). Higher-order poles or zeros contribute multiples: a double pole contributes −40 dB/decade. The approximation is exact at frequencies far from the corner; the maximum error is 3 dB right at the corner frequency itself.

The phase plot does not become piecewise linear in the same clean way, but it does have a useful approximation. Each pole contributes −45° at its corner frequency, transitioning from 0° to −90° over roughly a decade on either side. The full transition spans about two decades (from 0.1ωc to 10ωc). The combination of magnitude and phase asymptotes lets you sketch the complete Bode plot for a transfer function in minutes without numerical computation — which is why Bode plots were developed in the first place, before computers, as a rapid tool for frequency-domain design.
