---
id: common-base-amplifier
title: Common-Base Amplifier
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: bjt-amplifier-configurations
  type: hard
builds-toward:
- multi-stage-amplifiers
tags:
- common-base
- current-buffer
- high-frequency
- low-input-impedance
- cascode
- no-phase-inversion
stage: formal-systems
status: draft
---

# Common-Base Amplifier

## Core Idea
The common-base (CB) amplifier has its base terminal AC-grounded (via a bypass capacitor), with signal input at the emitter and output taken from the collector. It provides high voltage gain (A_v = g_m * R_C, similar in magnitude to the CE but without phase inversion) and a current gain near unity (alpha, slightly less than 1). Its distinctive feature is very low input impedance (approximately r_e = V_T / I_C, typically tens of ohms), making it suited for interfacing with low-impedance sources like transmission lines or photodetectors. The CB configuration excels at high frequencies because the Miller effect is absent — the collector-base capacitance C_bc does not get multiplied by voltage gain as it does in the CE topology, yielding a much wider bandwidth. The CB stage is frequently combined with a CE stage in the cascode configuration to achieve both high gain and wide bandwidth.

## How It's Best Learned
Compare the CB and CE amplifiers side by side using the hybrid-pi model. Show that the same transistor produces similar voltage gain magnitudes in both topologies but with fundamentally different input impedances, current gains, and frequency responses. Analyze the Miller effect in the CE case to see why it limits bandwidth, then demonstrate its absence in the CB configuration.

## Common Misconceptions
- Assuming current gain near unity means the CB amplifier is weak — it still provides substantial voltage and power gain; its strength is high-frequency performance, not current amplification.
- Confusing the low input impedance as a disadvantage in all cases — for matched-impedance systems (50-ohm RF lines, current-output sensors), it is precisely what is needed.
- Neglecting the base bypass capacitor — if the base is not properly AC-grounded, feedback through the base network degrades gain and bandwidth, defeating the purpose of the CB topology.

## Explainer

You already understand the common-emitter (CE) amplifier from your BJT configurations prerequisite: the emitter is AC-grounded, signal enters the base, output is taken from the collector, and you get high voltage gain with phase inversion. The **common-base (CB)** configuration is best understood by contrast. Instead of AC-grounding the emitter, you AC-ground the *base* (via a large bypass capacitor to AC ground). The signal now enters at the emitter and exits at the collector. Everything changes — except the transistor.

The most immediately striking difference is the input impedance. In the CE amplifier, the input impedance looking into the base is β × r_e, typically a few kilohms. In the CB amplifier, the input is at the emitter, where the impedance is simply r_e = V_T / I_C — on the order of 25 Ω at 1 mA. This is not a bug; it is the feature. Transmission lines (coaxial cables used in RF work) have characteristic impedances of 50 or 75 ohms. Photodetectors and other sensors often behave as current sources driving low impedances. A CE amplifier would create a severe impedance mismatch in these systems, wasting signal power and causing reflections. The CB amplifier is impedance-matched to these sources by design.

The current gain situation is equally counterintuitive. The CB amplifier's current gain is α = I_C / I_E ≈ 0.99 — slightly less than unity. Compare this to the CE's current gain β ≈ 100. You might expect this to make the CB amplifier weak, but voltage gain tells a different story. Since nearly all the emitter current flows to the collector (I_C ≈ I_E), and the output is taken across a load resistor R_C, the voltage gain is A_v = g_m × R_C — numerically identical in magnitude to the CE amplifier. The CB stage sacrifices current gain to get low input impedance; it does not sacrifice voltage gain.

The most important advantage of the CB over the CE is **bandwidth**. Recall that in the CE amplifier, the collector-base junction capacitance C_bc appears across the high-gain amplifying path. By the **Miller effect**, this capacitance is multiplied by (1 + |A_v|) when reflected to the input, creating a large effective input capacitance that limits bandwidth. In the CB amplifier, the base is grounded. The collector-base capacitance C_bc is now connected from the output to AC ground — it forms a simple shunt at the output, not an amplified feedback path. There is no Miller multiplication. The bandwidth of a CB stage can be ten or more times greater than a CE stage with the same transistor and bias current. This is why the CB configuration dominates in RF amplifiers, optical receivers, and the high-frequency input stage of the **cascode** — the CE-plus-CB cascade that combines the current gain of a CE with the bandwidth of a CB.
