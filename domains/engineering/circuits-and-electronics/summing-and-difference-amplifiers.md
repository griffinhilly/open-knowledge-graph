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
- id: inverting-amplifier-analysis
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
status: validated
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

## Questions

```yaml
- question: "An engineer builds a difference amplifier to measure a 5 mV sensor signal riding on 2 V of common-mode noise. The circuit uses 1% tolerance resistors and measures poor noise rejection. What is the most likely cause?"
  type: multiple-choice
  options:
    - "The op-amp's open-loop gain is too low for differential inputs"
    - "Resistor mismatch from 1% tolerance breaks the equal ratio condition, reducing CMRR dramatically"
    - "The sensor signal is too small for the difference amplifier architecture to handle"
    - "Common-mode rejection requires the inputs to be driven from the same source impedance"
  answer: 1
  explanation: "The CMRR of a difference amplifier depends entirely on the resistor ratio R_f/R_1 = R_g/R_2 being exactly equal on both sides. Even 1% resistor tolerance mismatch can reduce CMRR to roughly 40 dB (factor of 100 rejection), which may be completely insufficient for millivolt-level signals sitting on volt-level common-mode noise. This is the defining weakness of the basic difference amplifier — the CMRR is limited by passive component matching, not the op-amp. Option A is incorrect: op-amp open-loop gain is typically very high and not the limiting factor. Option D is partially related but describes a secondary effect of different input impedances, not the primary CMRR mechanism."

- question: "In a summing amplifier, three input signals V₁, V₂, V₃ are applied through equal resistors R to the inverting input. Why do the three signals not interact with each other or affect each other's contribution to the output?"
  type: multiple-choice
  options:
    - "The op-amp's high input impedance blocks current from flowing between inputs"
    - "The virtual ground at the inverting node forces each input to see 0V regardless of the others, making each current independent"
    - "The resistors are large enough that mutual coupling between them is negligible"
    - "The non-inverting input is grounded, which prevents any signal from propagating backward"
  answer: 1
  explanation: "Virtual ground is the key: the inverting node is held at 0V by the op-amp feedback regardless of what the other inputs are doing. Each input only sees the voltage drop from its own source to 0V across its own resistor, contributing current V_n/R_n. Because each input always sees the same 0V node, changing one input's voltage does not change the voltage seen by any other input's resistor. The inputs are completely decoupled at the summing junction. Option A is incorrect — op-amp input impedance refers to the inputs of the op-amp chip itself, not the summing node. Option D is a distraction; the grounded non-inverting input sets the common-mode reference but doesn't explain input independence."

- question: "In a basic difference amplifier, the CMRR can degrade severely even when the op-amp itself is ideal, if the resistors are not perfectly matched."
  type: true-false
  answer: true
  explanation: "Common-mode rejection in a difference amplifier works by cancellation: the signal that appears identically on both inputs is amplified with equal and opposite gain factors that sum to zero. This cancellation requires R_f/R_1 = R_g/R_2 exactly. Any mismatch — even 1% — breaks the cancellation, allowing some common-mode signal to appear at the output. An ideal op-amp with mismatched resistors will have poor CMRR. This is fundamentally different from the op-amp's own CMRR specification, which describes the chip's ability to reject differential input offset. The circuit-level CMRR and the op-amp CMRR are separate and independently limiting."

- question: "An instrumentation amplifier achieves high CMRR primarily because it uses a more precise op-amp chip than a standard difference amplifier."
  type: true-false
  answer: false
  explanation: "The instrumentation amplifier's CMRR advantage comes from its architecture, not from a better op-amp. The INA adds two non-inverting buffer stages before the difference amplifier output stage. These buffers provide high, equal input impedance on both inputs (eliminating asymmetric loading) and the differential gain is set by a single external resistor R_G, which does not affect CMRR. Critically, the internal resistors in the output difference amplifier stage are laser-trimmed on a single chip to match to very high precision — achieving 80–120 dB CMRR that is independent of source impedance variation. The benefit is architectural and manufacturing precision, not a fundamentally different op-amp technology."

- question: "Why does the instrumentation amplifier solve the two main weaknesses of the basic difference amplifier, and what specific design features accomplish this?"
  type: short-answer
  answer: "The basic difference amplifier has two weaknesses: (1) low and unequal input impedances (the inverting input sees R₁, the non-inverting input sees R₂ + Rg), which causes asymmetric loading from source impedances that degrades CMRR; and (2) CMRR limited by external resistor matching, which is difficult to control in discrete circuits. The instrumentation amplifier solves both. First, two unity-gain non-inverting buffer stages at the inputs provide very high and equal input impedances, eliminating loading asymmetry. Second, all resistors in the output stage are laser-trimmed on a single integrated circuit, achieving precise matching (and thus high CMRR) that is impossible with discrete resistors. The differential gain is set by a single external resistor R_G in the input stage, which controls gain without affecting CMRR."
  explanation: "A complete answer identifies both problems and maps each to the specific design solution. The input buffer stages solve the impedance problem; the laser-trimmed integrated resistors solve the matching problem. Students who only say 'it has buffers for high input impedance' have captured half the insight. The key is that CMRR in the basic difference amp is limited by an external, uncontrolled factor (resistor tolerance), while the INA moves that sensitive component inside the chip where it can be trimmed to high precision."
```

## Explainer

From your study of op-amp fundamentals, you know the two golden rules: the differential input voltage is driven to zero (virtual short), and no current enters the input terminals. The **summing amplifier** extends the standard inverting amplifier by connecting multiple input signals through individual resistors to the inverting node. Because the inverting input is held at virtual ground (0V), each input independently contributes a current V_n / R_n—the inputs do not interact with each other at all. KCL at the inverting node forces all those currents through the feedback resistor R_f, giving V_out = −R_f(V_1/R_1 + V_2/R_2 + ... + V_n/R_n). With equal input resistors, this is a simple scaled sum. With different input resistors, it is a **weighted sum**—the mathematical foundation of a digital-to-analog converter, where each binary bit contributes with a weight proportional to its binary significance.

The **difference amplifier** uses both op-amp inputs to compute the difference between two signals while rejecting anything they share in common. The signal at the inverting input is amplified by −R_f/R_1 (as in a standard inverting amplifier). The signal at the non-inverting input passes through a voltage divider and is then amplified by the non-inverting gain factor. When the resistor ratios are matched (R_f/R_1 = R_g/R_2), these combine to yield V_out = (R_f/R_1)(V_2 − V_1)—pure differential gain. Any signal that appears identically on both inputs (**common-mode signal**) cancels out. This **common-mode rejection** is invaluable when measuring small signals in noisy environments: the useful signal (differential) is preserved while noise picked up equally by both wires (common-mode) is eliminated.

The weakness of the basic difference amplifier is that its **CMRR**—common-mode rejection ratio—depends entirely on resistor matching precision. Even a 1% tolerance mismatch reduces CMRR to roughly 40 dB, meaning common-mode noise is attenuated by only a factor of 100. The solution is the **instrumentation amplifier (INA)**: two non-inverting buffer stages amplify the differential signal in the first stage (with gain set by a single external resistor R_G), feeding a conventional difference amplifier at the output. The buffers ensure both inputs see high, equal impedance regardless of source impedance—eliminating the asymmetric loading problem—and the internal resistors are laser-trimmed on a single chip, achieving 80–120 dB CMRR in practice.

Recognizing which architecture to use is a design skill. If you are mixing two audio tracks at equal levels, a simple summing amplifier suffices. If you are reading a strain gauge producing millivolt signals in the presence of motor noise, the instrumentation amplifier's CMRR and high input impedance are non-negotiable. The same underlying op-amp principles—virtual short, KCL at the summing node, superposition—apply to all three circuits, but understanding how resistor matching and input impedance affect performance is what separates correct application from costly mistakes.
