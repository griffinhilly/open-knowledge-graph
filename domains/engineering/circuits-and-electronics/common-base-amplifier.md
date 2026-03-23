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

## Questions

```yaml
- question: "An RF engineer needs to amplify a 500 MHz signal coming from a 50-ohm coaxial transmission line. She considers both common-emitter (CE) and common-base (CB) topologies using the same BJT. Which should she choose, and what is the primary reason?"
  type: multiple-choice
  options:
    - "CE, because its high current gain β provides more overall signal amplification at RF frequencies"
    - "CE, because grounding the emitter provides better RF shielding and noise immunity than grounding the base"
    - "CB, because its low input impedance (~r_e ≈ 50 Ω) matches the transmission line and eliminates the Miller effect bandwidth penalty"
    - "CB, because its voltage gain A_v = g_m × R_C is higher than the CE configuration for the same transistor"
  answer: 2
  explanation: "Two properties make the CB ideal here. First, its input impedance is approximately r_e = V_T/I_C — on the order of 25–50 Ω at typical bias currents — matching the 50-ohm transmission line and maximizing power transfer while preventing reflections. A CE amplifier's input impedance (β × r_e ≈ a few kΩ) would severely mismatch the line. Second, the CB has no Miller effect: the collector-base capacitance connects to AC ground at the base rather than feeding back across the amplifying stage, so bandwidth is not degraded by capacitance multiplication. Both reasons independently justify the CB choice for high-frequency, low-impedance applications."

- question: "A student sees that a common-base amplifier has current gain α ≈ 0.99 and concludes it is nearly useless compared to a common-emitter stage with β ≈ 100. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The student is correct — a current gain near unity means both voltage gain and power gain are also near unity"
    - "The CB's current gain is irrelevant because it uses feedback to achieve power gain through a different mechanism"
    - "Despite α ≈ 0.99, the CB provides voltage gain A_v = g_m × R_C — equal in magnitude to the CE — because nearly all emitter current reaches the collector and produces voltage across the load"
    - "Alpha of 0.99 is actually much larger than beta in some biasing regimes, making the comparison misleading"
  answer: 2
  explanation: "Voltage gain depends on transconductance g_m and load resistance R_C, not on current gain configuration. Because α ≈ 0.99, nearly all of the emitter (input) current reaches the collector and flows through R_C to produce output voltage: A_v = g_m × R_C. This is the same expression as the CE voltage gain in magnitude — the CB sacrifices current gain but not voltage gain or power gain. The practical advantage of the CB is its high-frequency performance (no Miller effect), not any difference in voltage amplification."

- question: "The common-base amplifier achieves wider bandwidth than the common-emitter amplifier because the base-grounded configuration uses a transistor with physically smaller parasitic capacitances."
  type: true-false
  answer: false
  explanation: "Both configurations use the same transistor with identical parasitic capacitances. The bandwidth difference is purely topological. In the CE configuration, the collector-base capacitance C_bc bridges input and output. Because the stage is inverting with gain |A_v|, the Miller effect multiplies C_bc by (1 + |A_v|) when reflected to the input, creating a large effective input capacitance that limits bandwidth. In the CB configuration, the base is AC-grounded. C_bc connects from the output to AC ground — a simple shunt at the output with no feedback path and no multiplication. The transistor is identical; the topology eliminates the Miller effect."

- question: "The Miller effect limits common-emitter amplifier bandwidth by multiplying the collector-base junction capacitance by (1 + |A_v|) when reflected to the input, creating a large effective input capacitance that rolls off gain at high frequencies."
  type: true-false
  answer: true
  explanation: "The Miller theorem states that an impedance Z connecting input and output of an inverting amplifier with gain −A_v appears at the input as Z/(1 + A_v). For C_bc, this means the effective input capacitance is C_bc × (1 + |A_v|). If A_v = 100 and C_bc = 1 pF, the effective input capacitance is 101 pF — a 100-fold increase. This large capacitance, combined with any source resistance, forms a low-pass RC filter that dramatically limits bandwidth. The CB stage eliminates this by grounding the base: C_bc no longer bridges input and output, so there is no feedback path and no multiplication."

- question: "Explain why AC-grounding the base (rather than the emitter) eliminates the Miller effect, and how this changes the circuit role of the collector-base capacitance C_bc."
  type: short-answer
  answer: "In the CE configuration, C_bc connects from the output (collector) back to the input (base), creating a feedback path. Because the amplifier is inverting, C_bc acts as a negative-impedance feedback element. The Miller theorem shows this appears at the input as a capacitance (1 + |A_v|) times larger, severely limiting high-frequency response. In the CB configuration, the base is AC-grounded — held at zero AC voltage. C_bc now connects from the collector to a fixed AC ground, so it is simply a shunt capacitance at the output node. There is no voltage swing at the base, no feedback to the input, no Miller multiplication, and no bandwidth penalty."
  explanation: "The Miller effect requires a capacitance bridging input and output with an inverting gain that makes the voltage across that capacitance larger than the input alone. The CB satisfies neither condition for C_bc: the base (one terminal of C_bc) is grounded, so the voltage across C_bc is just the collector voltage — there is no input-referred feedback. The result is that the CB's bandwidth is limited primarily by the output pole (C_bc shunting R_C) rather than a magnified input pole, yielding much wider bandwidth for the same transistor and load."
```

## Explainer

You already understand the common-emitter (CE) amplifier from your BJT configurations prerequisite: the emitter is AC-grounded, signal enters the base, output is taken from the collector, and you get high voltage gain with phase inversion. The **common-base (CB)** configuration is best understood by contrast. Instead of AC-grounding the emitter, you AC-ground the *base* (via a large bypass capacitor to AC ground). The signal now enters at the emitter and exits at the collector. Everything changes — except the transistor.

The most immediately striking difference is the input impedance. In the CE amplifier, the input impedance looking into the base is β × r_e, typically a few kilohms. In the CB amplifier, the input is at the emitter, where the impedance is simply r_e = V_T / I_C — on the order of 25 Ω at 1 mA. This is not a bug; it is the feature. Transmission lines (coaxial cables used in RF work) have characteristic impedances of 50 or 75 ohms. Photodetectors and other sensors often behave as current sources driving low impedances. A CE amplifier would create a severe impedance mismatch in these systems, wasting signal power and causing reflections. The CB amplifier is impedance-matched to these sources by design.

The current gain situation is equally counterintuitive. The CB amplifier's current gain is α = I_C / I_E ≈ 0.99 — slightly less than unity. Compare this to the CE's current gain β ≈ 100. You might expect this to make the CB amplifier weak, but voltage gain tells a different story. Since nearly all the emitter current flows to the collector (I_C ≈ I_E), and the output is taken across a load resistor R_C, the voltage gain is A_v = g_m × R_C — numerically identical in magnitude to the CE amplifier. The CB stage sacrifices current gain to get low input impedance; it does not sacrifice voltage gain.

The most important advantage of the CB over the CE is **bandwidth**. Recall that in the CE amplifier, the collector-base junction capacitance C_bc appears across the high-gain amplifying path. By the **Miller effect**, this capacitance is multiplied by (1 + |A_v|) when reflected to the input, creating a large effective input capacitance that limits bandwidth. In the CB amplifier, the base is grounded. The collector-base capacitance C_bc is now connected from the output to AC ground — it forms a simple shunt at the output, not an amplified feedback path. There is no Miller multiplication. The bandwidth of a CB stage can be ten or more times greater than a CE stage with the same transistor and bias current. This is why the CB configuration dominates in RF amplifiers, optical receivers, and the high-frequency input stage of the **cascode** — the CE-plus-CB cascade that combines the current gain of a CE with the bandwidth of a CB.
