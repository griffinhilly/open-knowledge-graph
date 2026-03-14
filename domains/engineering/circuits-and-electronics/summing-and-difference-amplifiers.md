---
id: summing-and-difference-amplifiers
title: Summing and Difference Amplifiers
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: op-amp-circuit-applications
  type: hard
- id: operational-amplifier-fundamentals
  type: hard
builds-toward:
- adc-dac-fundamentals
tags:
- summing-amplifier
- weighted-summer
- difference-amplifier
- instrumentation-amplifier
- differential-input
- cmrr
stage: formal-systems
status: draft
---

# Summing and Difference Amplifiers

## Core Idea
The summing amplifier extends the inverting amplifier by connecting multiple input signals through individual resistors to the inverting node. Since the inverting input is at virtual ground, each input contributes a current V_n / R_n independently, and V_out = -R_f * (V_1/R_1 + V_2/R_2 + ... + V_n/R_n). Equal input resistors produce a simple sum; unequal resistors produce a weighted sum — the foundation of digital-to-analog conversion. The difference amplifier uses both op-amp inputs to compute V_out = (R_f/R_1)(V_2 - V_1) when resistor ratios are matched, rejecting common-mode signals. However, its CMRR depends critically on resistor matching: even 1% mismatch can reduce CMRR to 40 dB. The instrumentation amplifier solves this by adding two non-inverting buffer stages before the difference amplifier, providing high and equal input impedance on both inputs, adjustable differential gain set by a single resistor, and excellent CMRR independent of source impedance matching.

## How It's Best Learned
Derive the summing amplifier output by applying KCL at the virtual ground node with multiple input currents. For the difference amplifier, use superposition — find the output due to each input alone, then add them — and show that common-mode rejection requires R_2/R_1 = R_f/R_g exactly. Build a difference amplifier with 1% and 0.1% resistors and measure CMRR to see the dramatic effect of matching tolerance.

## Common Misconceptions
- Assuming the difference amplifier has inherently high CMRR — its common-mode rejection is entirely limited by resistor matching precision, not by the op-amp itself.
- Forgetting that the difference amplifier has different input impedances on its two inputs — the inverting input sees R_1 while the non-inverting input sees R_2 + R_g, creating asymmetric loading that degrades CMRR when source impedances differ.
- Treating the instrumentation amplifier as merely a more expensive difference amplifier — its buffered inputs, single-resistor gain adjustment, and source-impedance-independent CMRR make it qualitatively different for sensor interfacing applications.
