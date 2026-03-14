---
id: resonance-circuits
title: Resonance in RLC Circuits
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: impedance-analysis
  type: hard
- id: second-order-transient-circuits
  type: soft
- id: ac-power-analysis-circuits
  type: soft
builds-toward:
- frequency-response-and-bode-plots
- passive-filter-design
tags:
- resonance
- quality-factor
- bandwidth
- series-resonance
- parallel-resonance
- selectivity
stage: formal-systems
status: validated
---

# Resonance in RLC Circuits

## Core Idea
Resonance occurs at ω₀ = 1/√(LC) where inductive and capacitive reactances are equal in magnitude and cancel. In a series RLC circuit at resonance, impedance is purely resistive (minimum), and current is maximum. In a parallel RLC circuit, admittance is minimum (impedance maximum), and the circuit draws minimum current from the source. The quality factor Q = ω₀L/R (series) measures sharpness of the resonance peak; the −3 dB bandwidth BW = ω₀/Q. High-Q circuits exhibit strong frequency selectivity and are used in filters, oscillators, and impedance matching networks.

## How It's Best Learned
Plot impedance magnitude versus frequency for series and parallel RLC circuits on the same graph. Compute ω₀, Q, and bandwidth from component values and locate the half-power frequencies on the plot. Explore how varying R changes Q and bandwidth while keeping ω₀ fixed.

## Common Misconceptions
- Using the same Q formula for series and parallel circuits — Q = ω₀L/R for series but Q = R/(ω₀L) = Rω₀C for parallel.
- Expecting voltages across individual reactive elements to equal the source voltage at resonance — in a high-Q series circuit, they can greatly exceed the source voltage by a factor of Q.
- Confusing bandwidth (frequency interval between half-power points) with the resonant frequency itself.
