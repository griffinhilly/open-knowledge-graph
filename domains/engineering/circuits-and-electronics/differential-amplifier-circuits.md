---
id: differential-amplifier-circuits
title: Differential Amplifier Circuits
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: operational-amplifier-fundamentals
  type: hard
- id: bjt-transistor-fundamentals
  type: hard
builds-toward:
- adc-dac-fundamentals
tags:
- differential-pair
- cmrr
- common-mode-rejection
- current-mirror
- differential-mode
- common-mode
- long-tailed-pair
stage: formal-systems
status: draft
---

# Differential Amplifier Circuits

## Core Idea
The differential amplifier (long-tailed pair) consists of two matched transistors with their emitters connected to a shared tail current source I_EE. It amplifies the difference between two input signals (differential mode, v_d = v_1 - v_2) while rejecting signals common to both inputs (common mode, v_cm = (v_1 + v_2)/2). Differential-mode gain is A_d = g_m * R_C, while common-mode gain A_cm is ideally zero (limited by the finite output impedance of the tail current source and transistor mismatches). The common-mode rejection ratio CMRR = |A_d / A_cm| quantifies this rejection capability and is maximized by using a high-impedance current mirror as the tail current source instead of a simple resistor. The differential pair is the input stage of virtually every operational amplifier, making it the foundational building block of analog IC design. When driven by a large differential signal, the pair acts as a current switch — all of I_EE steers to one transistor — which forms the basis of ECL digital logic.

## How It's Best Learned
Analyze the circuit by decomposing any pair of input signals into differential and common-mode components, solving each mode independently using half-circuit analysis. For differential mode, a virtual ground appears at the emitter node; for common mode, the tail impedance appears unbypassed in each half-circuit. Calculate CMRR for a resistor tail versus a current-mirror tail to see the dramatic improvement.

## Common Misconceptions
- Assuming perfect common-mode rejection — real circuits have transistor mismatches (V_BE offsets, beta differences) and finite tail current source impedance that limit CMRR to practical values (60-120 dB).
- Confusing differential gain with single-ended gain — taking the output from one collector gives half the differential gain and includes a common-mode component; true differential output requires both collectors.
- Treating the tail current source as a simple resistor in analysis — while a resistor works for basic understanding, it provides poor CMRR and the distinction between resistor and active current source is critical for real designs.
