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
stage: advanced
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

## Explainer

From your study of op-amp fundamentals, you know the two golden rules: the differential input voltage is driven to zero (virtual short), and no current enters the input terminals. The **summing amplifier** extends the standard inverting amplifier by connecting multiple input signals through individual resistors to the inverting node. Because the inverting input is held at virtual ground (0V), each input independently contributes a current V_n / R_n—the inputs do not interact with each other at all. KCL at the inverting node forces all those currents through the feedback resistor R_f, giving V_out = −R_f(V_1/R_1 + V_2/R_2 + ... + V_n/R_n). With equal input resistors, this is a simple scaled sum. With different input resistors, it is a **weighted sum**—the mathematical foundation of a digital-to-analog converter, where each binary bit contributes with a weight proportional to its binary significance.

The **difference amplifier** uses both op-amp inputs to compute the difference between two signals while rejecting anything they share in common. The signal at the inverting input is amplified by −R_f/R_1 (as in a standard inverting amplifier). The signal at the non-inverting input passes through a voltage divider and is then amplified by the non-inverting gain factor. When the resistor ratios are matched (R_f/R_1 = R_g/R_2), these combine to yield V_out = (R_f/R_1)(V_2 − V_1)—pure differential gain. Any signal that appears identically on both inputs (**common-mode signal**) cancels out. This **common-mode rejection** is invaluable when measuring small signals in noisy environments: the useful signal (differential) is preserved while noise picked up equally by both wires (common-mode) is eliminated.

The weakness of the basic difference amplifier is that its **CMRR**—common-mode rejection ratio—depends entirely on resistor matching precision. Even a 1% tolerance mismatch reduces CMRR to roughly 40 dB, meaning common-mode noise is attenuated by only a factor of 100. The solution is the **instrumentation amplifier (INA)**: two non-inverting buffer stages amplify the differential signal in the first stage (with gain set by a single external resistor R_G), feeding a conventional difference amplifier at the output. The buffers ensure both inputs see high, equal impedance regardless of source impedance—eliminating the asymmetric loading problem—and the internal resistors are laser-trimmed on a single chip, achieving 80–120 dB CMRR in practice.

Recognizing which architecture to use is a design skill. If you are mixing two audio tracks at equal levels, a simple summing amplifier suffices. If you are reading a strain gauge producing millivolt signals in the presence of motor noise, the instrumentation amplifier's CMRR and high input impedance are non-negotiable. The same underlying op-amp principles—virtual short, KCL at the summing node, superposition—apply to all three circuits, but understanding how resistor matching and input impedance affect performance is what separates correct application from costly mistakes.
