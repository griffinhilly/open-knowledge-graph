---
id: multi-stage-amplifiers
title: Multi-Stage Amplifiers
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: common-emitter-amplifier
  type: hard
- id: common-collector-amplifier
  type: soft
builds-toward:
- differential-amplifier-circuits
tags:
- cascading
- coupling-capacitors
- overall-gain
- loading-effect
- bandwidth
- cascade
- cascode
stage: advanced
status: draft
---

# Multi-Stage Amplifiers

## Core Idea
When a single amplifier stage cannot provide sufficient gain, bandwidth, or impedance characteristics, multiple stages are cascaded in series. The overall voltage gain is the product of individual stage gains, but each stage's output impedance loads the next stage's input impedance, reducing the effective gain below the product of unloaded gains. Coupling capacitors between stages block DC to preserve each stage's independent bias point while passing the AC signal. A common design pattern pairs a high-gain CE first stage with a CC (emitter follower) output stage — the CE provides voltage amplification while the CC provides low output impedance to drive the load without gain degradation. The overall bandwidth of a multi-stage amplifier is narrower than any individual stage because each stage's roll-off compounds, reducing the combined -3 dB bandwidth by a factor that depends on the number of identical stages. Cascode (CE + CB) and Darlington (CE + CC with shared collector) are specialized two-transistor configurations that achieve specific performance targets.

## How It's Best Learned
Analyze a two-stage CE-CC cascade by first solving each stage in isolation, then connecting them and accounting for loading. Compare the overall gain calculated as a simple product of individual gains versus the gain computed with inter-stage loading to see the discrepancy. Measure bandwidth of one, two, and three identical stages to observe the progressive bandwidth shrinkage.

## Common Misconceptions
- Multiplying unloaded stage gains to get overall gain — the output impedance of each stage forms a voltage divider with the input impedance of the next, reducing the effective gain at each interface.
- Assuming coupling capacitors have no effect on performance — they introduce low-frequency poles that raise the overall low-frequency cutoff, and each additional coupling capacitor adds another pole.
- Thinking more stages always improve performance — beyond a point, added stages reduce bandwidth, increase noise, and complicate bias design with diminishing gain returns.

## Explainer

You know how a single common-emitter (CE) stage works: it inverts the signal, provides voltage gain set roughly by -R_C/r_e, and has a moderately high output impedance. The common-collector (CC) stage doesn't amplify voltage but buffers it — it has near-unity voltage gain, very high input impedance, and very low output impedance. Cascading these stages lets you combine their strengths, but connecting real stages introduces a complication that the single-stage analysis hides: **loading effects**.

When you connect the output of Stage 1 to the input of Stage 2, the two stages interact. Stage 1's Thevenin equivalent output circuit (its output impedance R_out1 in series with the open-circuit output voltage) drives Stage 2's input impedance R_in2 as a load. The signal that reaches Stage 2's input is not the full open-circuit output of Stage 1 — it's reduced by a **voltage divider**: V_in2 = V_out1_oc × [R_in2 / (R_out1 + R_in2)]. If Stage 1 has output impedance 10 kΩ and Stage 2 has input impedance 2 kΩ, only 2/12 = 17% of Stage 1's open-circuit output reaches Stage 2. This inter-stage loading factor multiplies at every interface. The correct formula for overall gain is: A_total = A1_loaded × A2_loaded × ... where each stage gain is computed with the next stage's input impedance as the load — not the unloaded gain.

The classic **CE + CC cascade** exploits the complementary impedance profiles: the CE stage provides the voltage gain you need, and the CC (emitter follower) output stage presents very low output impedance (typically tens of ohms) to the external load. Without the CC stage, the CE output impedance (~R_C) forms an unfavorable voltage divider with any resistive load, killing the gain you worked to build. With the CC buffer inserted between CE and load, the load barely matters. Meanwhile, the CC stage's high input impedance (β × r_e at the input) doesn't significantly load the CE output — the inter-stage voltage divider ratio is close to 1. This is the engineering intuition behind impedance matching: you want the driving impedance much lower than the driven impedance at every interface.

**Bandwidth** is the other major cost of cascading. Each amplifier stage has its own -3 dB bandwidth, determined by where its gain rolls off. When you cascade two identical stages, the overall gain is the square of the individual gain — but the frequency where the total gain has dropped by 3 dB is *lower* than either individual stage's bandwidth. This is because both stages' roll-offs compound: if each stage drops by 3 dB at frequency f₀, the combined response has already dropped by 6 dB there, and you must look at a lower frequency for the 3 dB combined point. For n identical stages, the combined -3 dB bandwidth shrinks by a factor of √(2^(1/n) - 1). Three stages with individual bandwidth of 1 MHz yield a combined bandwidth of roughly 510 kHz. More gain from cascading always comes at the cost of narrower bandwidth — a fundamental engineering tradeoff captured by the **gain-bandwidth product** of each amplifier technology.
