---
id: frequency-response-Bode-plot-basics
title: Frequency Response and Bode Plot Basics
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: AC-Kirchhoff-laws-phasor-domain
  type: hard
- id: passive-filter-transfer-function-analysis
  type: soft
- id: logarithms-intro
  type: hard
- id: logarithmic-functions-review
  type: hard
builds-toward:
- filter-selection-and-practical-applications
tags:
- Bode-plots
- magnitude-plot
- phase-plot
- gain
- logarithmic-scale
stage: advanced
status: draft
---

# Frequency Response and Bode Plot Basics

## Core Idea
Bode plots display magnitude (in dB) and phase versus frequency on a logarithmic scale. Magnitude in dB is 20 log₁₀|H(jω)|; phase is ∠H(jω). Bode plots make it easy to visualize filtering action, identify resonances, and understand stability margins. Asymptotic Bode plots can be sketched by hand from the transfer function poles and zeros.

## Explainer

From your AC circuit analysis using phasors, you know that a circuit's behavior at a single frequency ω is captured by its **transfer function** H(jω) = V_out/V_in — a complex number whose magnitude tells you how much the circuit amplifies or attenuates, and whose angle tells you the phase shift. A **frequency response** is simply the collection of all these H(jω) values as ω sweeps from near-zero to very large. The challenge is displaying this information clearly, since frequency can span many orders of magnitude and gain can range from nearly 1 to nearly 0.

The **Bode plot** solves both display problems by using logarithms. The horizontal axis uses log₁₀(ω) so that each factor-of-ten change in frequency occupies equal space — a decade from 100 Hz to 1000 Hz takes the same width as a decade from 1 kHz to 10 kHz. The magnitude is converted to **decibels**: |H|_dB = 20·log₁₀|H(jω)|. This transformation turns multiplicative gain into addition (useful when cascading stages: dB totals add) and compresses large dynamic ranges into a readable scale. A gain of 1/10 becomes -20 dB; a gain of 100 becomes +40 dB. The phase plot shows ∠H(jω) in degrees on a linear vertical scale, also versus log frequency.

The most powerful feature of Bode plots is that they can be **sketched by hand** using asymptotic approximations. Every real pole at s = -p contributes a term 1/(1 + jω/p) to H(jω). At frequencies well below p, this factor contributes 0 dB and 0° phase. At frequencies well above p, the magnitude drops at -20 dB/decade and the phase approaches -90°. The transition happens near ω = p — the **corner frequency** (also called the break frequency or cutoff frequency). You simply draw two straight-line asymptotes meeting at the corner frequency. Each additional pole adds another -20 dB/decade slope break and another -90° of eventual phase lag. Zeros at s = -z work the same way but in reverse: +20 dB/decade slope increase and +90° phase lead.

This asymptotic technique lets you read a transfer function and sketch its Bode plot in minutes, without evaluating complex arithmetic at every frequency. The approximation is exact at the asymptotes and off by at most 3 dB and 6° at the corner frequency itself. The skill is worth practicing carefully because it builds the intuition you will need to understand filter design (why cascading stages multiplies attenuation), resonance (why a complex pole pair produces a peak), and control system stability (why phase lag near the gain crossover frequency is dangerous).
