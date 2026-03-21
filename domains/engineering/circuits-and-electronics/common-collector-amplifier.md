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
stage: advanced
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

## Questions

```yaml
- question: "A common-collector (emitter follower) stage is inserted between a sensor with 50 kΩ source impedance and a speaker with 8 Ω impedance. What is the primary purpose of this stage?"
  type: multiple-choice
  options:
    - "To amplify the voltage from the sensor before it reaches the speaker"
    - "To invert the signal phase so the speaker receives the correct polarity"
    - "To prevent the low-impedance speaker from loading the high-impedance sensor and causing catastrophic signal loss"
    - "To convert the analog signal to a digital signal compatible with the speaker driver"
  answer: 2
  explanation: "Without the emitter follower, connecting a 50 kΩ source to an 8 Ω load creates a massive voltage divider: virtually all signal voltage drops across the 50 kΩ source resistance, and almost none appears across the 8 Ω speaker. The emitter follower solves this by presenting a high input impedance (so it doesn't load the sensor) and a low output impedance (so it can drive the speaker). Voltage gain near unity is irrelevant — the circuit's value is impedance transformation, not voltage amplification. The emitter follower does not invert phase."

- question: "An emitter follower with β = 150 and an emitter resistor R_E = 200 Ω is driven by a source with 30 kΩ internal resistance. Approximately what output impedance does the stage present to a load at the emitter?"
  type: multiple-choice
  options:
    - "30 kΩ — the output impedance equals the source resistance"
    - "200 Ω — the output impedance equals R_E"
    - "~200 Ω in parallel with approximately 200 Ω, giving ~100 Ω"
    - "Approximately 200 Ω from the emitter resistance appearing in the denominator of the impedance reflection formula"
  answer: 2
  explanation: "The output impedance looking into the emitter is approximately r_e + R_source/β, where r_e is the small-signal emitter resistance (~26mV/I_C) and R_source is the Thevenin source impedance at the base. Here R_source/β = 30,000/150 = 200 Ω, plus a small r_e. This is much less than the 30 kΩ source impedance — the emitter follower has divided it by β. This dramatic reduction in output impedance (from 30 kΩ to ~200 Ω) is what allows the stage to drive low-impedance loads without signal loss."

- question: "The emitter follower has near-unity voltage gain and no phase inversion between input and output."
  type: true-false
  answer: true
  explanation: "Both statements are correct. The voltage gain A_v = R_E/(R_E + r_e) is slightly less than 1 because the signal at the emitter tracks the base signal minus the small voltage drop across r_e (the intrinsic emitter resistance). There is no phase inversion because the emitter voltage rises and falls in step with the base voltage — the transistor is not inverting the signal as it would in a common-emitter configuration where the output is taken from the collector. The output is offset by a fixed V_BE (~0.7 V), but this DC offset does not affect the AC signal's phase."

- question: "An emitter follower is a poor design choice when voltage gain matters because its gain is less than 1, and it should be replaced by a common-emitter stage in most applications."
  type: true-false
  answer: false
  explanation: "This is the primary misconception the emitter follower is designed to dispel. The emitter follower is not chosen for voltage gain — it is chosen for impedance transformation. Its near-unity voltage gain is a feature, not a bug: it transfers nearly all the signal voltage to the output while transforming impedances by a factor of β. Current gain remains approximately β, providing substantial power gain. In multi-stage amplifiers, emitter followers are inserted wherever impedance mismatch would degrade performance, protecting each stage from the loading effects of subsequent stages."

- question: "Explain how the impedance reflection rule produces both very high input impedance and very low output impedance in the emitter follower, using the same underlying mechanism."
  type: short-answer
  answer: "The impedance reflection rule says that impedances in the emitter circuit, when viewed from the base, appear multiplied by (β + 1) ≈ β. Conversely, impedances in the base circuit, when viewed from the emitter, appear divided by β. For input impedance: looking into the base terminal, R_E (in the emitter circuit) appears as β × R_E — a massive increase. For output impedance: looking into the emitter terminal, the source resistance R_source (in the base circuit) appears as R_source/β — a massive decrease. The same reflection factor β operates in opposite directions depending on which terminal you're looking into."
  explanation: "The underlying physics is the transistor's current amplification: β milliamps of emitter current result from 1 milliamp of base current. This means a small base current change causes a large emitter current change, so a large impedance at the emitter presents a small effective load to the base — and the reverse. Understanding this bidirectional reflection is the key to analyzing any BJT circuit from the base or emitter perspective."
```

## Explainer

You've already studied the common-emitter (CE) configuration, which inverts the signal and provides substantial voltage gain. The **common-collector (CC) amplifier** — universally called the **emitter follower** — is the CE's complementary circuit, designed for an entirely different purpose. Understanding why it exists requires thinking about what problem it solves before examining how it works.

Imagine connecting a high-impedance microphone (10 kΩ output impedance) directly to a low-impedance speaker (8 Ω). The connection forms a voltage divider between the source and load impedances. Virtually all the signal voltage drops across the source impedance, and almost none appears across the speaker. The result is catastrophic signal loss. What you need is a **buffer**: a circuit with high input impedance (so it doesn't load the source) and low output impedance (so it can drive the load) — voltage gain is secondary, even unimportant.

The CC topology achieves impedance transformation through the **impedance reflection rule** from the hybrid-π model. The collector is tied to V_CC (AC ground). Input is at the base; output is taken from the emitter. When you look into the base terminal, impedances in the emitter circuit appear multiplied by β (typically 100–300). A 100 Ω emitter resistor looks like ~10 kΩ from the base — a massive impedance step-up that prevents the stage from loading its source. Conversely, looking into the emitter, impedances in the base circuit appear divided by β. A 10 kΩ source driving the base looks like roughly 33 Ω from the emitter — a massive impedance step-down that allows the stage to drive heavy loads.

The voltage gain is A_v = R_E/(R_E + r_e), slightly less than 1, where r_e = 26 mV/I_C is the intrinsic emitter resistance from the small-signal model. This is why the emitter "follows" the base — the output tracks the input with near-unity gain and no phase inversion. The DC offset is exactly one V_BE drop (~0.7 V): the emitter sits 0.7 V below the base at all times, which must be accounted for in DC-coupled multi-stage designs. Despite near-unity voltage gain, current gain is approximately β, giving substantial power amplification.

In practice, the emitter follower is placed between stages in a multi-stage amplifier wherever impedance mismatch would degrade signal transfer. Without it, a low-impedance second stage reflects back and reduces the gain of the preceding common-emitter stage. With it, each stage sees only the emitter follower's high input impedance, and the signal chain remains clean. The bias resistor network at the base appears in parallel with β × R_E, limiting the practical input impedance — a detail that matters when the source impedance is comparable to the bias resistors.
