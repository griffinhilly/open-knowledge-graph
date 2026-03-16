---
id: bjt-amplifier-configurations
title: BJT Amplifier Configurations
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: bjt-transistor-fundamentals
  type: hard
- id: thevenin-norton-equivalents
  type: hard
- id: ac-circuit-analysis-methods
  type: soft
builds-toward:
- operational-amplifier-fundamentals
tags:
- common-emitter
- common-base
- common-collector
- emitter-follower
- small-signal
- hybrid-pi-model
- voltage-gain
- input-impedance
stage: formal-systems
status: validated
---

# BJT Amplifier Configurations

## Core Idea
BJTs are configured in three amplifier topologies defined by which terminal is common between input and output. The common-emitter amplifier provides high voltage and current gain with 180° phase inversion and is the most widely used. The common-collector (emitter-follower) has near-unity voltage gain but provides current gain and low output impedance, useful for driving loads. The common-base amplifier offers high voltage gain at high frequencies with no phase inversion. Small-signal analysis replaces the BJT with the hybrid-π model (voltage-controlled current source g_m·v_be, input resistance r_π = β/g_m, output resistance r_o) to compute gain and impedances for small sinusoidal signals around the Q-point.

## How It's Best Learned
Master the hybrid-π small-signal model. For each configuration, systematically set all DC sources to zero, short large bypass capacitors, replace the BJT with the small-signal model, and then apply KCL/KVL to find voltage gain, input impedance, and output impedance.

## Common Misconceptions
- Mixing large-signal DC quantities with small-signal AC quantities in the same equation.
- Forgetting to short bypass capacitors during small-signal analysis — an un-bypassed emitter resistor dramatically reduces voltage gain.
- Dismissing the emitter follower as useless because its voltage gain is less than 1 — its low output impedance is essential for impedance matching and current delivery.

## Explainer

From your study of BJT fundamentals, you know that a bipolar transistor is a current-controlled device: a small base current i_B controls a much larger collector current i_C = β·i_B, with β typically between 50 and 300. You also know from Thévenin/Norton equivalents how to reduce complex networks to simple equivalent circuits. Small-signal amplifier analysis combines these two ideas: replace the transistor with a linear equivalent model (valid for small AC signals around the DC operating point), then use standard circuit analysis to find gain and impedances.

The **hybrid-π small-signal model** is the key analytical tool. It represents the BJT as a voltage-controlled current source: a signal v_be at the input produces a current g_m·v_be at the output, where **g_m** (transconductance, units A/V) is the gain parameter and equals I_C/V_T (collector DC bias current divided by thermal voltage ≈ 26 mV at room temperature). The input resistance r_π = β/g_m appears between base and emitter. An output resistance r_o accounts for the finite slope of i_C vs. v_CE curves. To do small-signal analysis: set all DC voltage sources to zero (short them), replace DC current sources with open circuits, short large bypass capacitors, then substitute the hybrid-π model for each transistor, and apply KCL/KVL.

The three amplifier configurations differ in which BJT terminal is connected to AC ground (the "common" terminal). In the **common-emitter** configuration, the emitter is the reference node. The input signal goes to the base; the amplified output appears at the collector. This topology offers large voltage gain A_v = −g_m·R_C (the negative sign indicates 180° phase inversion) and moderate input and output impedances. The voltage gain can be enormous — hundreds or thousands — making common-emitter the workhorse configuration for voltage amplification.

The **common-collector** (also called the **emitter follower**) takes input at the base and produces output at the emitter, with the collector at AC ground. Its voltage gain is slightly less than 1 (A_v ≈ 1), which sounds useless until you examine its impedances: input impedance is high (β+1 times the emitter load) and output impedance is very low (roughly 1/g_m, typically tens of ohms). This makes the emitter follower ideal as a **buffer**: it drives a low-impedance load (like a speaker or long cable) without loading the high-impedance source stage. Think of it as a power translator — voltage is passed through unchanged, but current gain and impedance transformation do the real work. The **common-base** configuration connects the base to AC ground, takes input at the emitter, and delivers output at the collector. It has no phase inversion, very low input impedance, and high output impedance. Its main advantage is excellent high-frequency performance because it eliminates the Miller effect — the feedback capacitance between input and output that limits bandwidth in the common-emitter stage. These three configurations are building blocks: real amplifier stages often combine them (for example, a common-emitter driving an emitter-follower output stage) to simultaneously achieve high gain, high input impedance, and low output impedance.
