---
id: common-emitter-amplifier
title: Common-Emitter Amplifier
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: bjt-amplifier-configurations
  type: hard
- id: bjt-transistor-fundamentals
  type: hard
builds-toward:
- amplifier-biasing-stability
- multi-stage-amplifiers
- differential-amplifier-circuits
tags:
- common-emitter
- voltage-gain
- bypass-capacitor
- biasing
- small-signal
- hybrid-pi-model
- phase-inversion
stage: formal-systems
status: validated
---

# Common-Emitter Amplifier

## Core Idea
The common-emitter (CE) amplifier is the most widely used BJT amplifier topology, providing substantial voltage gain with 180-degree phase inversion between input and output. The transistor's emitter terminal is common to both the input and output circuits (grounded through a bypass capacitor at signal frequencies). Voltage gain is determined by the ratio of collector resistance to the small-signal emitter resistance: A_v = -g_m * R_C (or equivalently -R_C / r_e for the simplified T-model), where the negative sign reflects phase inversion. A voltage divider network at the base establishes a stable DC operating point (Q-point), while coupling capacitors isolate the amplifier's DC bias from signal source and load. An emitter resistor R_E provides DC stability against beta variation, but an emitter bypass capacitor must short R_E at signal frequencies to preserve full voltage gain.

## How It's Best Learned
Start by establishing the DC bias point using Thevenin equivalent analysis at the base, then replace the BJT with the hybrid-pi small-signal model. Systematically short all DC sources and large capacitors, apply KCL at the collector node, and derive gain and impedance expressions. Compare measured gain with and without the emitter bypass capacitor to see how the un-bypassed emitter resistor trades gain for linearity and bandwidth.

## Common Misconceptions
- Assuming the bypass capacitor is optional — without it, the emitter resistance R_E appears in the gain expression and reduces voltage gain dramatically (A_v = -R_C / (r_e + R_E)).
- Confusing the DC bias resistors with the small-signal input impedance — the bias network loads the input in parallel with the transistor's r_pi, so the amplifier's input impedance is lower than r_pi alone.
- Expecting the CE amplifier to have constant gain across all frequencies — coupling and bypass capacitors create low-frequency roll-off, while parasitic capacitances and the transistor's f_T limit high-frequency response.

## Questions

```yaml
- question: "A common-emitter amplifier has R_C = 2 kΩ and an emitter resistor R_E = 500 Ω with a bypass capacitor. When the bypass capacitor is removed, the voltage gain magnitude drops dramatically. What is the primary reason?"
  type: multiple-choice
  options:
    - "The transistor's transconductance g_m decreases when the bypass capacitor is removed"
    - "R_E appears in series with r_e in the gain denominator, reducing gain to R_C/(r_e + R_E)"
    - "The coupling capacitors can no longer pass the AC signal effectively"
    - "The DC operating point shifts when the bypass capacitor is removed"
  answer: 1
  explanation: "With the bypass capacitor, R_E is shorted at signal frequencies and gain is −g_m·R_C = −R_C/r_e. Without it, R_E is in series with r_e, giving gain −R_C/(r_e + R_E) — much smaller when R_E >> r_e. The Q-point, g_m, and coupling capacitors are unaffected by the bypass capacitor."

- question: "In a common-emitter amplifier, the input voltage rises (becomes more positive). What happens to the collector voltage, and why?"
  type: multiple-choice
  options:
    - "It rises, because the transistor acts as a voltage follower"
    - "It falls, because increased base-emitter voltage increases collector current, increasing the voltage drop across R_C"
    - "It remains constant, because the voltage divider bias stabilizes it"
    - "It rises, because the emitter bypass capacitor inverts the signal back"
  answer: 1
  explanation: "A rising input increases v_be, which increases the controlled current g_m·v_be flowing through R_C. Greater current means greater voltage drop across R_C, so the collector voltage (V_CC − I_C·R_C) falls. This 180-degree phase inversion is fundamental to the CE configuration — it is why the gain expression A_v = −g_m·R_C carries a negative sign."

- question: "The emitter bypass capacitor in a common-emitter amplifier is optional and primarily affects the DC bias point."
  type: true-false
  answer: false
  explanation: "The bypass capacitor has no effect on the DC bias — it is an open circuit at DC. Its critical role is at signal frequencies, where it shorts R_E, preventing the emitter resistance from appearing in the gain expression. Without it, gain drops from −g_m·R_C to −R_C/(r_e + R_E). Far from optional, it is responsible for most of the amplifier's voltage gain."

- question: "Removing the emitter bypass capacitor from a common-emitter amplifier reduces voltage gain but improves linearity, input impedance, and bandwidth."
  type: true-false
  answer: true
  explanation: "When R_E is un-bypassed, it introduces series-series feedback. This reduces gain but stabilizes the operating point against signal swings (improving linearity), increases the input impedance seen by the source, and extends bandwidth. This is the classic gain-stability tradeoff: the same resistor that fights AC gain is responsible for DC stability and improved small-signal linearity."

- question: "Why does the common-emitter amplifier produce a 180-degree phase inversion between input and output? Explain using the transistor's action and the role of R_C."
  type: short-answer
  answer: "When the input rises, it increases the base-emitter voltage, which increases the collector current. Greater collector current causes a larger voltage drop across R_C, which lowers the collector voltage. The output therefore moves opposite to the input — 180-degree inversion."
  explanation: "The key is V_out = V_CC − I_C·R_C. Since I_C increases when v_in increases, V_out decreases. The small-signal model captures this as v_out = −g_m·v_be·R_C, where the negative sign encodes the inversion caused by the resistive load at the collector."
```

## Explainer

From your study of BJT fundamentals, you know that a small base current controls a much larger collector current — that is the transistor's essential action. The **common-emitter amplifier** exploits this by routing a small AC signal into the base and extracting an amplified version at the collector. The name "common emitter" means the emitter is the terminal shared by both the input loop (base–emitter) and the output loop (collector–emitter) — it is the reference node at signal frequencies, held to AC ground by a **bypass capacitor** across the emitter resistor.

Before you can analyze the amplifier's gain, you must set its **DC operating point (Q-point)**. Two resistors, R₁ and R₂, form a voltage divider that fixes the base voltage. This divider is designed so that its Thevenin resistance is small compared to the transistor's input resistance, making the base voltage largely independent of transistor beta — a form of negative feedback that stabilizes the Q-point against part-to-part variation. The emitter resistor R_E further stabilizes the collector current: if temperature causes I_C to drift upward, the voltage across R_E increases, reducing the base-emitter voltage and pulling I_C back down. This DC stability is why the emitter resistor exists, even though it fights against AC gain.

To find the **voltage gain**, you replace the transistor with its **hybrid-pi small-signal model** — a controlled current source g_m·v_be in parallel with the output resistance r_o, and an input resistance r_π from base to emitter. At signal frequencies, the bypass capacitor shorts R_E (so it no longer appears in the gain), and the coupling capacitors are also short circuits. The output voltage develops across R_C (or R_C || R_L if a load is connected). Applying KVL around the input loop: v_be = v_in. Applying KCL at the collector node: v_out = −g_m·v_be·R_C. Dividing gives A_v = −g_m·R_C — the negative sign is crucial and reflects **phase inversion**: the output swings opposite to the input. When the input rises (forward biasing the junction more), collector current increases, the voltage drop across R_C increases, and the collector voltage falls.

The bypass capacitor is the key to understanding the gain-stability tradeoff. With the bypass capacitor in place, R_E is shorted at signal frequencies and the full gain −g_m·R_C is achieved. Without it, R_E appears in series with r_e = 1/g_m, and gain drops to −R_C/(r_e + R_E) — often much smaller. This un-bypassed configuration is actually useful: the emitter resistor provides **series-series feedback** that linearizes the amplifier, increases input impedance, and extends bandwidth. The designer's choice — bypass or not — depends on whether gain or linearity matters more. This tradeoff between gain and stability through feedback is a theme you will encounter repeatedly as you study multi-stage and differential amplifiers.
