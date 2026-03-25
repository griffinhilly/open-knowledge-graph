---
id: series-RLC-resonance-characteristics
title: Series RLC Resonance Characteristics
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: circuit-resonance-concepts
  type: hard
- id: parallel-RLC-resonance-characteristics
  type: soft
builds-toward:
- passive-filter-transfer-function-analysis
tags:
- series-resonance
- current-magnification
- voltage-magnification
stage: formal-systems
status: validated
---
# Series RLC Resonance Characteristics

## Core Idea
In a series RLC circuit at resonance, impedance equals R (minimum), current is maximum, and voltage across the capacitor or inductor can exceed the source voltage by a factor Q (voltage magnification). The bandwidth BW = ω₀/Q determines the frequency range of strong response. Series resonance is used in filters and impedance matching.

## Questions

```yaml
- question: "A series RLC circuit is at resonance with a quality factor Q = 40 and a source voltage of 5V. What is the approximate voltage across the capacitor at resonance?"
  type: multiple-choice
  options:
    - "5V — equal to the source voltage, since the reactive voltages cancel at resonance"
    - "0V — the capacitor's reactance disappears at the resonant frequency"
    - "200V — the capacitor voltage equals Q times the source voltage at resonance"
    - "5V/√2 — the half-power voltage at the resonant frequency"
  answer: 2
  explanation: "At resonance, the current is maximized at I = V_s/R. The voltage across the capacitor is V_C = I × X_C = (V_s/R)(1/ω₀C) = Q × V_s. With Q = 40 and V_s = 5V, V_C = 200V. This voltage magnification by factor Q is the key phenomenon: individual component voltages far exceed the source voltage. V_L is also 200V but exactly opposite in phase, so they cancel (KVL is satisfied), but the capacitor must be rated to handle 200V. Option A is the most tempting wrong answer — students assume resonance makes everything equal to the source voltage."

- question: "Two series RLC circuits have the same resonant frequency ω₀. Circuit A has Q = 80 and circuit B has Q = 4. Which statement correctly describes the difference in their frequency responses?"
  type: multiple-choice
  options:
    - "Circuit A has a wider bandwidth and responds to a broader range of frequencies near ω₀"
    - "Circuit A has a narrower bandwidth, responding selectively to a tight frequency band, making it better for isolating a single signal"
    - "Both circuits respond identically since they share the same resonant frequency"
    - "Circuit B has higher impedance at resonance, delivering more voltage to the load"
  answer: 1
  explanation: "Bandwidth = ω₀/Q, so higher Q means narrower bandwidth. Circuit A (Q = 80) has bandwidth ω₀/80 — it responds strongly only to frequencies extremely close to ω₀, sharply rejecting everything else. Circuit B (Q = 4) has bandwidth ω₀/4 — a much wider pass-band. For selecting one radio station from thousands, high Q is essential. For a wideband amplifier, low Q is desirable. The two circuits differ not at ω₀ itself but in how their response falls off away from ω₀."

- question: "At series resonance, the total impedance of the circuit is zero because the inductive and capacitive reactances cancel each other completely."
  type: true-false
  answer: false
  explanation: "False. The reactive impedances cancel — X_L and X_C are equal and opposite — but the resistive impedance R remains. Total impedance at resonance equals R, which is the minimum possible value, not zero. Only in the hypothetical case of a lossless circuit (R = 0) would impedance reach zero. In practice, R is always present (wire resistance, inductor resistance, etc.), and the circuit at resonance behaves as a pure resistance. This is why current is maximized (not infinite) at resonance: I = V_s/R."

- question: "A higher Q factor in a series RLC resonant circuit corresponds to a narrower bandwidth, meaning the circuit is more frequency-selective."
  type: true-false
  answer: true
  explanation: "True. Q = ω₀/BW, equivalently BW = ω₀/Q = R/L. A higher Q (achieved by reducing resistance relative to the reactance √(L/C)) gives narrower bandwidth. High-Q resonators are used wherever frequency selectivity matters: radio tuners discriminating between adjacent stations, crystal oscillators maintaining precise frequency, bandpass filters in signal processing. The Q factor is the single most important figure of merit for resonant circuits because it captures both the sharpness of the frequency response and the voltage magnification at resonance."

- question: "In a series RLC circuit at resonance, KVL requires that voltages sum to the source voltage. Yet the voltage across the capacitor alone can exceed the source voltage by a factor of Q. Explain how this is possible without violating KVL."
  type: short-answer
  answer: "At resonance, V_L and V_C are both equal in magnitude to Q × V_s, but they are exactly 180° out of phase with each other. In the phasor domain: V_L = +jQV_s and V_C = −jQV_s. Their sum is zero. KVL around the loop: V_R + V_L + V_C = V_s + jQV_s − jQV_s = V_s. The large reactive voltages cancel each other perfectly, leaving only V_R = V_s to satisfy KVL. The capacitor and inductor trade energy back and forth (reactive power circulating between them) while the source only supplies the real power dissipated in R. The key insight is that 'large voltage across a component' does not mean that voltage adds to the loop sum — phasor addition accounts for phase, not just magnitude."
  explanation: "This is the voltage magnification paradox resolved by phasor arithmetic. Students familiar only with scalar addition expect large component voltages to exceed the source — but phasors at 180° cancel. The practical implication: components in a high-Q resonant circuit must be rated for voltages Q times larger than the source, even though the net loop voltage is only the source voltage. Failing to account for this in design causes catastrophic component failure."
```

## Explainer

From your study of resonance concepts, you know that L and C are reactive elements with opposite characters: inductors oppose changes in current and present impedance that grows with frequency (Z_L = jωL), while capacitors oppose changes in voltage and present impedance that shrinks with frequency (Z_C = 1/jωC). In a series RLC circuit, these two reactive impedances are in direct opposition, and at one special frequency they cancel exactly. That cancellation is resonance, and the circuit behavior at that frequency is striking enough to power entire families of practical applications.

The **resonant frequency** is found by setting the total reactive impedance to zero: jωL + 1/jωC = 0, which gives ω₀ = 1/√(LC). At this frequency, the inductor's positive reactance and the capacitor's negative reactance are equal in magnitude and opposite in sign. They cancel, leaving only R in the series loop. Current is therefore maximized — I = V_s/R — because the circuit offers the least opposition to the source. This is the intuition behind **series resonance as a current maximizer**: all the voltage source's driving capability goes into R, with the reactive elements neutralizing each other.

Now the surprising part: **voltage magnification**. Even though the net reactive voltage is zero, the individual voltages across L and C are not zero — they are large, equal, and opposite. The voltage across the inductor at resonance is V_L = I × ωL = (V_s/R) × ω₀L. The ratio V_L/V_s = ω₀L/R is defined as **Q**, the quality factor. If Q = 50 (not unusual for an LC resonator), the voltage across L (and across C, which is equal and opposite) is 50 times the source voltage. This is not a violation of KVL — the two large voltages cancel each other around the loop — but it means that components must be rated for voltages far exceeding the source. In radio tuning circuits, this Q-fold voltage magnification is exploited to selectively amplify signals at the resonant frequency; in power electronics, it can destroy components if not carefully designed for.

**Bandwidth** is the practical measure of frequency selectivity: BW = ω₀/Q = R/L. A high-Q circuit (small R relative to √(L/C)) has a narrow bandwidth — it responds strongly only to frequencies very close to ω₀ and sharply rejects others. A low-Q circuit (large R) has a wide bandwidth — it responds to a broad range of frequencies but with less peak selectivity. This tradeoff is everywhere in filter design: a sharp bandpass filter for picking one radio station out of thousands needs high Q (low loss), while a wideband amplifier intentionally uses low Q to pass a wide frequency range. The quantity √(L/C) is called the **characteristic impedance** of the resonator, and R/√(L/C) = 1/Q is the damping ratio — the same concept you may encounter in mechanical vibrations, where it controls whether a spring-mass-damper system rings out slowly (low damping) or returns to rest quickly (high damping).
