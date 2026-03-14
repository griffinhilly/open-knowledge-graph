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
