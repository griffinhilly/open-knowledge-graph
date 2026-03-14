---
id: common-collector-amplifier
title: Common-Collector Amplifier
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: bjt-amplifier-configurations
  type: hard
- id: bjt-transistor-fundamentals
  type: hard
builds-toward:
- multi-stage-amplifiers
tags:
- emitter-follower
- unity-gain
- buffer
- impedance-matching
- high-input-impedance
- low-output-impedance
stage: formal-systems
status: draft
---

# Common-Collector Amplifier

## Core Idea
The common-collector (CC) amplifier, also called the emitter follower, has its collector terminal common to both input and output (connected directly to V_CC). The output is taken from the emitter, which follows the base voltage with a gain slightly less than unity (A_v approximately equal to 1). The defining strength of this topology is impedance transformation: it presents very high input impedance (approximately beta times R_E) and very low output impedance (approximately r_e + R_source/beta). This makes it an ideal buffer stage placed between a high-impedance source and a low-impedance load, preventing the load from attenuating the signal. There is no phase inversion between input and output. Current gain remains high (approximately beta), so while voltage gain is near unity, power gain is substantial.

## How It's Best Learned
Derive input and output impedance by replacing the BJT with the hybrid-pi model and applying KCL. Focus on understanding the impedance reflection rule: looking into the base, impedances in the emitter circuit are multiplied by beta; looking into the emitter, impedances in the base circuit are divided by beta. Connect a CC stage between a high-impedance sensor and a low-impedance speaker to physically experience the buffering effect.

## Common Misconceptions
- Dismissing the emitter follower as useless because its voltage gain is less than 1 — its value lies in impedance transformation and current gain, not voltage amplification.
- Forgetting that the output voltage is offset from the input by one V_BE drop (approximately 0.7 V), which matters in DC-coupled applications.
- Assuming infinite input impedance — the bias resistor network at the base is in parallel with the transistor's reflected impedance, significantly reducing the actual input impedance seen by the source.
