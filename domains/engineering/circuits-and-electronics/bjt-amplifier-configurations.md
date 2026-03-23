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

## Questions

```yaml
- question: "A high-impedance microphone (~10 kΩ output impedance) needs to drive a low-impedance cable (50 Ω). Directly connecting them would severely load the microphone and attenuate the signal. Which BJT configuration is best suited for this interface?"
  type: multiple-choice
  options:
    - "Common-emitter, because its high voltage gain amplifies the weak microphone signal before it reaches the cable"
    - "Common-collector (emitter follower), because its high input impedance does not load the microphone and its low output impedance can drive the 50 Ω cable efficiently"
    - "Common-base, because its low input impedance matches the microphone's high output impedance"
    - "Common-emitter with a large bypass capacitor to eliminate the impedance mismatch"
  answer: 1
  explanation: "This is the emitter follower's defining use case: impedance transformation without inversion. Its input impedance (~(β+1)×R_E) is very high and does not load the source. Its output impedance (~1/g_m, typically tens of ohms) is very low and can drive a 50 Ω cable with minimal voltage drop. Voltage gain is ≈1, preserving signal amplitude. The common-emitter (option 0) has only moderate input impedance and would still load the microphone; it also inverts phase unnecessarily for this application."

- question: "In a common-emitter amplifier, the emitter resistor R_E is present but not bypassed with a capacitor. Compared to a fully bypassed version, what happens to the voltage gain?"
  type: multiple-choice
  options:
    - "Voltage gain increases because R_E stabilizes the Q-point, allowing larger undistorted signal swings"
    - "Voltage gain decreases dramatically because R_E appears in the AC signal path, reducing gain to approximately −R_C/R_E when g_m·R_E >> 1"
    - "Voltage gain is unaffected because R_E only influences DC bias, not AC signals"
    - "Voltage gain increases because un-bypassed R_E raises input impedance, drawing more signal current into the base"
  answer: 1
  explanation: "When the emitter resistor is un-bypassed, it appears in the small-signal equivalent: A_v ≈ −g_m·R_C / (1 + g_m·R_E) ≈ −R_C/R_E when g_m·R_E >> 1. This can reduce gain from hundreds (bypassed) to single digits (un-bypassed). Option 2 reflects the most common error — R_E sees AC signal current through the emitter, so it absolutely affects AC gain. Shorting R_E with a bypass capacitor removes it from the AC path while preserving its DC biasing role."

- question: "The common-collector amplifier is rarely useful in practice because its voltage gain is less than 1 and it provides no voltage amplification."
  type: true-false
  answer: false
  explanation: "The emitter follower's near-unity voltage gain is paired with current gain and dramatic impedance transformation that make it indispensable. Output impedance is very low (~1/g_m, typically 25–50 Ω) and input impedance is very high — these properties allow it to buffer a high-impedance source and drive a low-impedance load without voltage divider losses. Many multi-stage amplifiers use a common-emitter stage for voltage gain followed by an emitter follower output stage to deliver current to a load. Dismissing it because voltage gain ≈ 1 misses what the configuration actually provides."

- question: "The three BJT amplifier configurations are defined by which terminal is connected to AC ground, not simply by where the input signal is applied."
  type: true-false
  answer: true
  explanation: "The naming convention 'common-X' means terminal X is the shared AC reference between input and output paths — i.e., it is connected to AC ground. In common-emitter, the emitter is grounded (often through a bypass capacitor); in common-collector, the collector is at AC ground; in common-base, the base is at AC ground. The signal input and output points follow from this topology. Understanding the grounding arrangement is more fundamental than memorizing which terminal 'receives the input,' and it directly determines the gain and impedance characteristics."

- question: "Why is small-signal analysis performed separately from DC bias analysis, and what does 'setting DC sources to zero' mean in practice?"
  type: short-answer
  answer: "Small-signal analysis models the BJT's linear behavior for small AC variations around the DC operating point (Q-point). The DC bias circuit sets where the transistor operates; the hybrid-π small-signal model is only valid as a linear approximation near that point. Setting DC sources to zero means shorting all DC voltage sources (replacing V_CC with wire) and opening all DC current sources, because they don't contribute to AC signal variations. Large bypass capacitors are also treated as short circuits since they present negligible impedance at signal frequencies. The remaining circuit is the pure AC equivalent."
  explanation: "Mixing large-signal and small-signal quantities is the most common analysis error. The total collector voltage is V_C = V_CC + v_c — a DC term plus a small AC variation — and they cannot be combined in a single gain equation. Keeping them separate through superposition is the key discipline: first solve for DC bias (transistor operating point), then replace the transistor with its small-signal model and solve for AC gain and impedances."
```

## Explainer

From your study of BJT fundamentals, you know that a bipolar transistor is a current-controlled device: a small base current i_B controls a much larger collector current i_C = β·i_B, with β typically between 50 and 300. You also know from Thévenin/Norton equivalents how to reduce complex networks to simple equivalent circuits. Small-signal amplifier analysis combines these two ideas: replace the transistor with a linear equivalent model (valid for small AC signals around the DC operating point), then use standard circuit analysis to find gain and impedances.

The **hybrid-π small-signal model** is the key analytical tool. It represents the BJT as a voltage-controlled current source: a signal v_be at the input produces a current g_m·v_be at the output, where **g_m** (transconductance, units A/V) is the gain parameter and equals I_C/V_T (collector DC bias current divided by thermal voltage ≈ 26 mV at room temperature). The input resistance r_π = β/g_m appears between base and emitter. An output resistance r_o accounts for the finite slope of i_C vs. v_CE curves. To do small-signal analysis: set all DC voltage sources to zero (short them), replace DC current sources with open circuits, short large bypass capacitors, then substitute the hybrid-π model for each transistor, and apply KCL/KVL.

The three amplifier configurations differ in which BJT terminal is connected to AC ground (the "common" terminal). In the **common-emitter** configuration, the emitter is the reference node. The input signal goes to the base; the amplified output appears at the collector. This topology offers large voltage gain A_v = −g_m·R_C (the negative sign indicates 180° phase inversion) and moderate input and output impedances. The voltage gain can be enormous — hundreds or thousands — making common-emitter the workhorse configuration for voltage amplification.

The **common-collector** (also called the **emitter follower**) takes input at the base and produces output at the emitter, with the collector at AC ground. Its voltage gain is slightly less than 1 (A_v ≈ 1), which sounds useless until you examine its impedances: input impedance is high (β+1 times the emitter load) and output impedance is very low (roughly 1/g_m, typically tens of ohms). This makes the emitter follower ideal as a **buffer**: it drives a low-impedance load (like a speaker or long cable) without loading the high-impedance source stage. Think of it as a power translator — voltage is passed through unchanged, but current gain and impedance transformation do the real work. The **common-base** configuration connects the base to AC ground, takes input at the emitter, and delivers output at the collector. It has no phase inversion, very low input impedance, and high output impedance. Its main advantage is excellent high-frequency performance because it eliminates the Miller effect — the feedback capacitance between input and output that limits bandwidth in the common-emitter stage. These three configurations are building blocks: real amplifier stages often combine them (for example, a common-emitter driving an emitter-follower output stage) to simultaneously achieve high gain, high input impedance, and low output impedance.
