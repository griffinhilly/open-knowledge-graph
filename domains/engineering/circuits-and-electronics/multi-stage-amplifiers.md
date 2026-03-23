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
stage: formal-systems
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

## Questions

```yaml
- question: "A two-stage amplifier has Stage 1 with an unloaded voltage gain of 50 and an output impedance of 8 kΩ, and Stage 2 with an input impedance of 2 kΩ. What is the actual overall voltage gain of the cascaded amplifier (ignoring Stage 2's own gain for simplicity)?"
  type: multiple-choice
  options:
    - "50 — the stages multiply directly because coupling capacitors isolate them"
    - "10 — the inter-stage voltage divider passes only 2/(8+2) = 20% of Stage 1's output to Stage 2"
    - "100 — the two impedances add to increase the effective gain"
    - "25 — you average the unloaded and loaded gains"
  answer: 1
  explanation: "Stage 2's input impedance loads Stage 1's output, forming a voltage divider: V_delivered = V_oc × [R_in2 / (R_out1 + R_in2)] = 50 × [2/(8+2)] = 50 × 0.2 = 10. This is the classic loading effect: the actual gain is far below the unloaded product because the stages interact through their impedances. Coupling capacitors block DC bias but do not isolate the AC signal path — impedances still interact at signal frequencies."

- question: "Why is a common-collector (emitter follower) stage typically placed after a common-emitter gain stage rather than a second common-emitter stage?"
  type: multiple-choice
  options:
    - "The CC stage adds additional voltage gain that compensates for the loading loss"
    - "The CC stage's very low output impedance prevents the load from forming a damaging voltage divider with the CE output"
    - "Two CE stages would cancel each other's phase inversions, reducing net gain"
    - "The CC stage increases bandwidth more than a second CE stage would"
  answer: 1
  explanation: "The CE stage's output impedance (~R_C, often several kilohms) forms an unfavorable voltage divider with the external load resistance, wasting the gain achieved. The CC stage (emitter follower) has very low output impedance (typically tens of ohms) and near-unity voltage gain — it buffers the CE output so the load barely matters. Meanwhile, the CC stage's high input impedance doesn't significantly load the CE stage. This impedance matching is the core reason for the CE-CC configuration: CE provides gain, CC preserves it all the way to the load."

- question: "Cascading three identical amplifier stages with individual −3 dB bandwidth of 1 MHz produces an overall −3 dB bandwidth narrower than 1 MHz."
  type: true-false
  answer: true
  explanation: "Each stage's gain rolls off independently. At the individual stage's −3 dB frequency, each stage has already dropped by 3 dB, so three cascaded stages have dropped 9 dB total at that frequency — well past the combined −3 dB point. The combined bandwidth must be at a lower frequency, roughly 510 kHz for three identical stages (using the formula involving √(2^(1/n) − 1)). More stages always means narrower combined bandwidth — the gain-bandwidth tradeoff is inescapable."

- question: "The overall voltage gain of a multi-stage amplifier equals the product of the individual stages' unloaded voltage gains."
  type: true-false
  answer: false
  explanation: "This is the central misconception of multi-stage amplifier analysis. Each stage's output impedance loads the next stage's input impedance, forming a voltage divider at every interface. The correct formula is A_total = A1_loaded × A2_loaded × ..., where each stage's gain is computed with the subsequent stage's input impedance as the load. The unloaded gain product can be dramatically higher than the actual gain — in the extreme case where output impedance equals input impedance, each interface passes only half the signal, and the product of unloaded gains overstates actual gain by 2^(n-1) for n stages."

- question: "Why does adding more stages to an amplifier inevitably narrow its overall bandwidth, and what design principle does this reflect?"
  type: short-answer
  answer: "Each amplifier stage has its own frequency-dependent gain that rolls off above its −3 dB bandwidth. When stages are cascaded, their roll-offs compound: at any frequency where each stage contributes some gain reduction, the total reduction multiplies. The combined −3 dB point therefore falls at a lower frequency than any individual stage's bandwidth. For n identical stages, the bandwidth shrinks by a factor of √(2^(1/n) − 1). This reflects the fundamental gain-bandwidth product limitation: amplifier technology offers a fixed product of gain and bandwidth, so trading one for the other is unavoidable — more stages buy more gain but always at the cost of bandwidth."
  explanation: "The gain-bandwidth product is a device-level constraint rooted in transistor physics, but the compounding effect is a system-level consequence of the math of cascaded roll-offs. Engineers working around this use techniques like shunt-peaked loads or feedback to extend bandwidth per stage, but they cannot escape the underlying constraint — they can only shift where the tradeoff lands."
```

## Explainer

You know how a single common-emitter (CE) stage works: it inverts the signal, provides voltage gain set roughly by -R_C/r_e, and has a moderately high output impedance. The common-collector (CC) stage doesn't amplify voltage but buffers it — it has near-unity voltage gain, very high input impedance, and very low output impedance. Cascading these stages lets you combine their strengths, but connecting real stages introduces a complication that the single-stage analysis hides: **loading effects**.

When you connect the output of Stage 1 to the input of Stage 2, the two stages interact. Stage 1's Thevenin equivalent output circuit (its output impedance R_out1 in series with the open-circuit output voltage) drives Stage 2's input impedance R_in2 as a load. The signal that reaches Stage 2's input is not the full open-circuit output of Stage 1 — it's reduced by a **voltage divider**: V_in2 = V_out1_oc × [R_in2 / (R_out1 + R_in2)]. If Stage 1 has output impedance 10 kΩ and Stage 2 has input impedance 2 kΩ, only 2/12 = 17% of Stage 1's open-circuit output reaches Stage 2. This inter-stage loading factor multiplies at every interface. The correct formula for overall gain is: A_total = A1_loaded × A2_loaded × ... where each stage gain is computed with the next stage's input impedance as the load — not the unloaded gain.

The classic **CE + CC cascade** exploits the complementary impedance profiles: the CE stage provides the voltage gain you need, and the CC (emitter follower) output stage presents very low output impedance (typically tens of ohms) to the external load. Without the CC stage, the CE output impedance (~R_C) forms an unfavorable voltage divider with any resistive load, killing the gain you worked to build. With the CC buffer inserted between CE and load, the load barely matters. Meanwhile, the CC stage's high input impedance (β × r_e at the input) doesn't significantly load the CE output — the inter-stage voltage divider ratio is close to 1. This is the engineering intuition behind impedance matching: you want the driving impedance much lower than the driven impedance at every interface.

**Bandwidth** is the other major cost of cascading. Each amplifier stage has its own -3 dB bandwidth, determined by where its gain rolls off. When you cascade two identical stages, the overall gain is the square of the individual gain — but the frequency where the total gain has dropped by 3 dB is *lower* than either individual stage's bandwidth. This is because both stages' roll-offs compound: if each stage drops by 3 dB at frequency f₀, the combined response has already dropped by 6 dB there, and you must look at a lower frequency for the 3 dB combined point. For n identical stages, the combined -3 dB bandwidth shrinks by a factor of √(2^(1/n) - 1). Three stages with individual bandwidth of 1 MHz yield a combined bandwidth of roughly 510 kHz. More gain from cascading always comes at the cost of narrower bandwidth — a fundamental engineering tradeoff captured by the **gain-bandwidth product** of each amplifier technology.
