---
id: series-RLC-resonance-characteristics
title: Series RLC Resonance Characteristics
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: circuit-resonance-concepts
  type: hard
builds-toward:
- passive-filter-transfer-function-analysis
tags:
- series-resonance
- current-magnification
- voltage-magnification
stage: advanced
status: draft
---

# Series RLC Resonance Characteristics

## Core Idea
In a series RLC circuit at resonance, impedance equals R (minimum), current is maximum, and voltage across the capacitor or inductor can exceed the source voltage by a factor Q (voltage magnification). The bandwidth BW = ω₀/Q determines the frequency range of strong response. Series resonance is used in filters and impedance matching.

## Explainer

From your study of resonance concepts, you know that L and C are reactive elements with opposite characters: inductors oppose changes in current and present impedance that grows with frequency (Z_L = jωL), while capacitors oppose changes in voltage and present impedance that shrinks with frequency (Z_C = 1/jωC). In a series RLC circuit, these two reactive impedances are in direct opposition, and at one special frequency they cancel exactly. That cancellation is resonance, and the circuit behavior at that frequency is striking enough to power entire families of practical applications.

The **resonant frequency** is found by setting the total reactive impedance to zero: jωL + 1/jωC = 0, which gives ω₀ = 1/√(LC). At this frequency, the inductor's positive reactance and the capacitor's negative reactance are equal in magnitude and opposite in sign. They cancel, leaving only R in the series loop. Current is therefore maximized — I = V_s/R — because the circuit offers the least opposition to the source. This is the intuition behind **series resonance as a current maximizer**: all the voltage source's driving capability goes into R, with the reactive elements neutralizing each other.

Now the surprising part: **voltage magnification**. Even though the net reactive voltage is zero, the individual voltages across L and C are not zero — they are large, equal, and opposite. The voltage across the inductor at resonance is V_L = I × ωL = (V_s/R) × ω₀L. The ratio V_L/V_s = ω₀L/R is defined as **Q**, the quality factor. If Q = 50 (not unusual for an LC resonator), the voltage across L (and across C, which is equal and opposite) is 50 times the source voltage. This is not a violation of KVL — the two large voltages cancel each other around the loop — but it means that components must be rated for voltages far exceeding the source. In radio tuning circuits, this Q-fold voltage magnification is exploited to selectively amplify signals at the resonant frequency; in power electronics, it can destroy components if not carefully designed for.

**Bandwidth** is the practical measure of frequency selectivity: BW = ω₀/Q = R/L. A high-Q circuit (small R relative to √(L/C)) has a narrow bandwidth — it responds strongly only to frequencies very close to ω₀ and sharply rejects others. A low-Q circuit (large R) has a wide bandwidth — it responds to a broad range of frequencies but with less peak selectivity. This tradeoff is everywhere in filter design: a sharp bandpass filter for picking one radio station out of thousands needs high Q (low loss), while a wideband amplifier intentionally uses low Q to pass a wide frequency range. The quantity √(L/C) is called the **characteristic impedance** of the resonator, and R/√(L/C) = 1/Q is the damping ratio — the same concept you may encounter in mechanical vibrations, where it controls whether a spring-mass-damper system rings out slowly (low damping) or returns to rest quickly (high damping).
