---
id: series-resonance-characteristics
title: Series Resonance Characteristics
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: impedance-admittance-networks
  type: hard
- id: circuit-resonance-concepts
  type: hard
builds-toward:
- quality-factor-bandwidth-tradeoff
- frequency-response-analysis-bode
tags:
- resonance
- series-circuits
- frequency-response
stage: advanced
status: validated
---

# Series Resonance Characteristics

## Core Idea
In a series RLC circuit, resonance occurs at ω₀ = 1/√(LC) where inductive and capacitive reactances cancel, leaving only resistance. At resonance, impedance is minimum (Z = R), current is maximum, voltage across the coil and capacitor are equal in magnitude but 180° out of phase, and voltage and current are in phase. Series resonance is exploited in bandpass filters, tuned amplifiers, and impedance matching.

## Questions

```yaml
- question: "In a series RLC circuit with Q = 50 driven by a 1V source at its resonant frequency, what is the approximate voltage across the capacitor?"
  type: multiple-choice
  options:
    - "0V — the capacitive and inductive reactances cancel, so no voltage develops across either element"
    - "1V — the source voltage appears entirely across the capacitor at resonance"
    - "50V — the voltage across each reactive element is Q times the source voltage at resonance"
    - "0.5V — the source voltage is split equally between the inductor and capacitor"
  answer: 2
  explanation: "At resonance, the current is maximum: I = V_s/R. The voltage across the capacitor is V_C = I · X_C = (V_s/R) · (1/ω₀C) = V_s · Q. With Q = 50 and V_s = 1V, V_C ≈ 50V. This is the voltage amplification property of resonance. The same magnitude appears across the inductor — both are Q times the source — but they are 180° out of phase and cancel in series, which is why the net impedance is only R. Students who think 'the reactances cancel so there's no voltage' confuse net voltage with individual element voltages."

- question: "A radio designer wants to sharpen the frequency selectivity of a series RLC tuner — accepting only a very narrow band of frequencies near the station frequency and rejecting everything else. Which change accomplishes this?"
  type: multiple-choice
  options:
    - "Increase the resistance R to raise the quality factor Q"
    - "Decrease the resistance R to raise the quality factor Q and narrow the bandwidth"
    - "Decrease the inductance L, which shifts the resonant frequency and sharpens the peak"
    - "Increase the capacitance C, which reduces the bandwidth BW = R/L"
  answer: 1
  explanation: "Bandwidth BW = R/L = ω₀/Q. To narrow the bandwidth (higher selectivity), you need higher Q, and Q = ω₀L/R. For fixed L and resonant frequency, reducing R increases Q and decreases bandwidth. Increasing R does the opposite — it broadens the response and reduces selectivity. This is why low-loss components (high-Q coils with low resistance) are valued in tuned circuits: they give sharp, selective frequency responses."

- question: "At the resonant frequency of a series RLC circuit, the voltage across the inductor and the voltage across the capacitor are equal in magnitude but 180° out of phase."
  type: true-false
  answer: true
  explanation: "At resonance ω₀ = 1/√(LC), so X_L = ω₀L and X_C = 1/(ω₀C) are equal in magnitude (X_L = X_C). Both are driven by the same current I, so V_L = I·X_L and V_C = I·X_C are also equal in magnitude. However, V_L leads the current by 90° while V_C lags the current by 90° — making them 180° apart in phase. They cancel in series (their phasor sum is zero), so the total reactive voltage is zero and all source voltage appears across R. This is why impedance at resonance equals R."

- question: "At resonance in a series RLC circuit, the voltages across the inductor and capacitor are both zero because the reactive elements are effectively 'short-circuited' by their cancellation."
  type: true-false
  answer: false
  explanation: "The reactive elements do not become short circuits at resonance — they still carry the full current I = V_s/R and each develops a voltage of magnitude Q·V_s across them individually. What cancels is the *net* series voltage across the L-C combination (V_L + V_C = 0 as phasors), because they are equal and opposite. Each element individually has a large voltage — up to Q times the source — which is precisely the voltage amplification that makes resonance useful. Thinking 'cancellation means zero voltage' confuses series voltage addition with individual element voltages."

- question: "Explain why the voltage across the capacitor in a series RLC circuit can be much larger than the source voltage at resonance, and what circuit parameter determines by how much."
  type: short-answer
  answer: "At resonance, the series impedance is minimized to Z = R, so current is at its maximum: I = V_s/R. The voltage across the capacitor is V_C = I · X_C = (V_s/R) · (1/ω₀C). This equals V_s · (1/(ω₀RC)) = V_s · Q, where Q = 1/(ω₀RC) = ω₀L/R is the quality factor. So V_C = Q · V_s. For a high-Q circuit (small R relative to the reactive impedances), Q can be large, and the capacitor voltage greatly exceeds the source. The same factor applies to the inductor. They don't violate energy conservation because they are 180° out of phase and cancel in series — energy sloshes between L and C with only R absorbing power from the source."
  explanation: "This Q-fold voltage amplification is why resonance is useful in practice: radio receivers use high-Q resonant circuits to amplify the tiny voltages of desired signals while rejecting interference. It also explains why high-voltage components must be specified carefully in resonant circuits — the capacitor and inductor must withstand Q times the source voltage, which can exceed component ratings even when the source is modest. The quality factor Q = ω₀L/R = 1/(ω₀CR) is the single most important characteristic of a resonant circuit, encoding both its selectivity (narrow vs. broad bandwidth) and its voltage amplification."
```

## Explainer

From your study of impedance and admittance, you know that inductors and capacitors both oppose current flow, but in opposite ways that depend on frequency. An inductor's reactance X_L = ωL grows with frequency; a capacitor's reactance X_C = 1/(ωC) shrinks with frequency. Connect them in series and you have two frequency-dependent opponents. At one special frequency they cancel exactly — that is **resonance**, and the circuit's behavior at that frequency is dramatically different from any other.

At the **resonant frequency** ω₀ = 1/√(LC), the total reactance is X_L − X_C = ω₀L − 1/(ω₀C) = 0. The series impedance reduces to Z = R — purely resistive, as if the inductor and capacitor weren't there. Since Z is at its minimum, the current amplitude I = V_s/R is at its maximum. All of the source voltage appears across the resistor; none is "wasted" fighting reactive elements. This maximum-current condition is why resonance is so useful: you can extract maximum power transfer from a source at one specific tunable frequency.

The voltages across the inductor and capacitor at resonance are not zero — they can actually be *much larger* than the source voltage. At ω₀, V_L = I·X_L = (V_s/R)·ω₀L, which exceeds V_s whenever ω₀L > R. This **voltage amplification factor** is the **quality factor** Q = ω₀L/R = 1/(ω₀CR). A high-Q circuit (large L/R or small R) has sharp resonance: voltage across L and C can be many times the input voltage, and the circuit responds strongly only to a narrow band of frequencies near ω₀. A low-Q circuit has broad, weak resonance. The voltage across C and L are equal in magnitude at ω₀ but exactly 180° out of phase, so they cancel in series while each independently reaches Q times the source voltage.

This behavior defines the **bandpass** character of a series RLC filter. Near ω₀, low impedance allows large current and large output across R. Far from ω₀ — either very low frequencies where the capacitor dominates and blocks current, or very high frequencies where the inductor dominates and chokes current — the impedance rises and the current falls. The bandwidth of the passband is BW = R/L = ω₀/Q: narrow for high-Q circuits, wide for low-Q. Practical applications include radio tuners (selecting one station's frequency while rejecting others), antenna impedance matching, and intermediate-frequency (IF) amplifier stages in radio receivers — all of which exploit the frequency selectivity that resonance provides.
