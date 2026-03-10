---
id: frequency-response-and-bode-plots
title: Frequency Response and Bode Plots
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: ac-circuit-analysis-methods
  type: hard
- id: resonance-circuits
  type: soft
- id: logarithms-intro
  type: soft
- id: ac-power-and-resonance
  type: soft
builds-toward:
- passive-filter-design
tags:
- frequency-response
- transfer-function
- Bode-plot
- gain
- phase
- poles
- zeros
stage: formal-systems
status: draft
---

# Frequency Response and Bode Plots

## Core Idea
The frequency response of a circuit is described by its transfer function H(jω) = output/input phasors as ω varies. Bode plots display the magnitude |H(jω)| in decibels (20·log₁₀|H|) and phase ∠H in degrees, both on a logarithmic frequency axis. Each real pole at ωp contributes a break in the Bode magnitude plot: flat below ωp, then falling at −20 dB/decade above it, with a −45°/decade phase transition centered at ωp. Complex pole pairs (from underdamped second-order factors) produce a resonance peak. Asymptotic straight-line approximations enable rapid sketching from the factored transfer function.

## How It's Best Learned
Start with simple RC (single-pole) and LC (complex pole pair) circuits and derive their transfer functions by voltage divider. Sketch Bode plots from asymptotic approximations, then verify against computed frequency-response tables. Practice identifying poles and zeros from the shape of a given Bode plot.

## Common Misconceptions
- Using 10·log₁₀ instead of 20·log₁₀ for voltage or current ratios — the factor of 10 applies to power ratios only.
- Treating the −3 dB frequency as a perfect brick-wall cutoff — it is the half-power point, and signals above it are attenuated but not eliminated.
- Neglecting phase when designing filters or feedback systems — phase relationships are as important as magnitude for stability and signal fidelity.
