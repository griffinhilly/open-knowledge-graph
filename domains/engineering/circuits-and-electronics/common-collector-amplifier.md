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

## Explainer

You've already studied the common-emitter (CE) configuration, which inverts the signal and provides substantial voltage gain. The **common-collector (CC) amplifier** — universally called the **emitter follower** — is the CE's complementary circuit, designed for an entirely different purpose. Understanding why it exists requires thinking about what problem it solves before examining how it works.

Imagine connecting a high-impedance microphone (10 kΩ output impedance) directly to a low-impedance speaker (8 Ω). The connection forms a voltage divider between the source and load impedances. Virtually all the signal voltage drops across the source impedance, and almost none appears across the speaker. The result is catastrophic signal loss. What you need is a **buffer**: a circuit with high input impedance (so it doesn't load the source) and low output impedance (so it can drive the load) — voltage gain is secondary, even unimportant.

The CC topology achieves impedance transformation through the **impedance reflection rule** from the hybrid-π model. The collector is tied to V_CC (AC ground). Input is at the base; output is taken from the emitter. When you look into the base terminal, impedances in the emitter circuit appear multiplied by β (typically 100–300). A 100 Ω emitter resistor looks like ~10 kΩ from the base — a massive impedance step-up that prevents the stage from loading its source. Conversely, looking into the emitter, impedances in the base circuit appear divided by β. A 10 kΩ source driving the base looks like roughly 33 Ω from the emitter — a massive impedance step-down that allows the stage to drive heavy loads.

The voltage gain is A_v = R_E/(R_E + r_e), slightly less than 1, where r_e = 26 mV/I_C is the intrinsic emitter resistance from the small-signal model. This is why the emitter "follows" the base — the output tracks the input with near-unity gain and no phase inversion. The DC offset is exactly one V_BE drop (~0.7 V): the emitter sits 0.7 V below the base at all times, which must be accounted for in DC-coupled multi-stage designs. Despite near-unity voltage gain, current gain is approximately β, giving substantial power amplification.

In practice, the emitter follower is placed between stages in a multi-stage amplifier wherever impedance mismatch would degrade signal transfer. Without it, a low-impedance second stage reflects back and reduces the gain of the preceding common-emitter stage. With it, each stage sees only the emitter follower's high input impedance, and the signal chain remains clean. The bias resistor network at the base appears in parallel with β × R_E, limiting the practical input impedance — a detail that matters when the source impedance is comparable to the bias resistors.
