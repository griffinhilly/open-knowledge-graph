---
id: series-resonance-characteristics
title: Series Resonance Characteristics
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: impedance-admittance-networks
  type: hard
builds-toward:
- quality-factor-bandwidth-tradeoff
- frequency-response-analysis-bode
tags:
- resonance
- series-circuits
- frequency-response
stage: advanced
status: draft
---

# Series Resonance Characteristics

## Core Idea
In a series RLC circuit, resonance occurs at ω₀ = 1/√(LC) where inductive and capacitive reactances cancel, leaving only resistance. At resonance, impedance is minimum (Z = R), current is maximum, voltage across the coil and capacitor are equal in magnitude but 180° out of phase, and voltage and current are in phase. Series resonance is exploited in bandpass filters, tuned amplifiers, and impedance matching.

## Explainer

From your study of impedance and admittance, you know that inductors and capacitors both oppose current flow, but in opposite ways that depend on frequency. An inductor's reactance X_L = ωL grows with frequency; a capacitor's reactance X_C = 1/(ωC) shrinks with frequency. Connect them in series and you have two frequency-dependent opponents. At one special frequency they cancel exactly — that is **resonance**, and the circuit's behavior at that frequency is dramatically different from any other.

At the **resonant frequency** ω₀ = 1/√(LC), the total reactance is X_L − X_C = ω₀L − 1/(ω₀C) = 0. The series impedance reduces to Z = R — purely resistive, as if the inductor and capacitor weren't there. Since Z is at its minimum, the current amplitude I = V_s/R is at its maximum. All of the source voltage appears across the resistor; none is "wasted" fighting reactive elements. This maximum-current condition is why resonance is so useful: you can extract maximum power transfer from a source at one specific tunable frequency.

The voltages across the inductor and capacitor at resonance are not zero — they can actually be *much larger* than the source voltage. At ω₀, V_L = I·X_L = (V_s/R)·ω₀L, which exceeds V_s whenever ω₀L > R. This **voltage amplification factor** is the **quality factor** Q = ω₀L/R = 1/(ω₀CR). A high-Q circuit (large L/R or small R) has sharp resonance: voltage across L and C can be many times the input voltage, and the circuit responds strongly only to a narrow band of frequencies near ω₀. A low-Q circuit has broad, weak resonance. The voltage across C and L are equal in magnitude at ω₀ but exactly 180° out of phase, so they cancel in series while each independently reaches Q times the source voltage.

This behavior defines the **bandpass** character of a series RLC filter. Near ω₀, low impedance allows large current and large output across R. Far from ω₀ — either very low frequencies where the capacitor dominates and blocks current, or very high frequencies where the inductor dominates and chokes current — the impedance rises and the current falls. The bandwidth of the passband is BW = R/L = ω₀/Q: narrow for high-Q circuits, wide for low-Q. Practical applications include radio tuners (selecting one station's frequency while rejecting others), antenna impedance matching, and intermediate-frequency (IF) amplifier stages in radio receivers — all of which exploit the frequency selectivity that resonance provides.
