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
stage: advanced
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

## Explainer

From your study of BJT fundamentals, you know that a transistor's collector current is controlled by its base-emitter voltage: I_C = I_S · exp(V_BE / V_T). The differential pair exploits this exponential relationship with two matched transistors sharing a common emitter node connected to a **tail current source** I_EE. Whatever current the tail source demands, that current splits between the two transistors according to the difference in their base voltages. When both bases are at the same potential, each transistor carries I_EE/2. When one base is slightly higher, more of I_EE steers toward that transistor and less toward the other — the circuit converts a voltage difference into a current imbalance, which collector resistors then convert back into a voltage difference at the outputs.

The key analytical tool is **half-circuit analysis**, which decomposes any pair of inputs into differential and common-mode components. Any two input voltages v₁ and v₂ can be written as v₁ = v_cm + v_d/2 and v₂ = v_cm − v_d/2, where v_cm = (v₁ + v₂)/2 is the common-mode component and v_d = v₁ − v₂ is the differential component. For the differential mode, the shared emitter node does not move (it is a **virtual ground** by symmetry — equal and opposite currents from both halves cancel), so each half-circuit sees a grounded emitter and has gain A_d = g_m · R_C. For the common-mode, both transistors receive the same signal, both emitter currents increase together, and the tail current source resists this change. The effective emitter impedance is 2·R_EE (or 2·r_o for a current mirror), which suppresses the common-mode gain dramatically. Common-mode rejection ratio **CMRR = |A_d / A_cm|** quantifies how well the circuit ignores the shared signal.

The quality of the tail current source is decisive for CMRR. A simple resistor R_EE has finite impedance: at signal frequencies, common-mode signals see 2R_EE as an emitter degeneration resistance, giving a common-mode gain of approximately −R_C / (2R_EE). A **current mirror** as the tail source presents very high output impedance (r_o of the mirror transistor), making A_cm extremely small and CMRR potentially 80–120 dB. This is why every practical op-amp input stage uses an active current source: the difference in CMRR between a resistor tail and a current mirror can be 40–60 dB (100× to 1000× in ratio). When you look inside a 741 or LM358, the first thing you see is a differential pair with a current mirror tail — the architecture you are now equipped to analyze from first principles.

The large-signal behavior completes the picture. As v_d grows large (several V_T ≈ 26 mV), the differential pair saturates: all of I_EE steers into one transistor and none into the other. This hard switching behavior — where the circuit snaps between two states — is the basis of **emitter-coupled logic (ECL)**, the fastest digital logic family. The same circuit that amplifies millivolt signals with exquisite linearity in analog mode becomes a high-speed digital switch when driven with large differential signals. This dual personality makes the differential pair arguably the single most important circuit topology in electronics, appearing as the input stage of every op-amp and as the switching core of high-speed digital ICs.
