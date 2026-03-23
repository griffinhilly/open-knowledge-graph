---
id: parallel-RLC-resonance-characteristics
title: Parallel RLC Resonance Characteristics
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: circuit-resonance-concepts
  type: hard
builds-toward:
- passive-filter-transfer-function-analysis
tags:
- parallel-resonance
- current-magnification
- impedance-maximum
stage: formal-systems
status: validated
---

# Parallel RLC Resonance Characteristics

## Core Idea
In a parallel RLC circuit at resonance, impedance is maximum (approximately L/CR for high Q), current through R is maximum, and circulating currents in L and C can exceed the source current by a factor Q (current magnification). Parallel resonance appears in tuning circuits and reactive load compensation.

## Questions

```yaml
- question: "In a high-Q parallel RLC circuit at resonance, you measure 1 mA flowing from the source into the parallel combination. What do you expect when you measure the current flowing through the inductor alone?"
  type: multiple-choice
  options:
    - "Approximately 1 mA — the inductor carries the same current as the source"
    - "Approximately Q × 1 mA — the circulating tank current is much larger than the source current"
    - "Approximately zero — at resonance, the inductor blocks current"
    - "Approximately 1 mA / Q — the inductor carries only a fraction of the source current"
  answer: 1
  explanation: "This is current magnification, the defining feature of parallel resonance. At resonance, the L and C currents are equal in magnitude and opposite in phase, so they cancel from the source's perspective — the source only needs to supply the (small) resistive branch current. But the reactive currents circulating in the tank (between L and C) can be Q times the source current. This is the direct dual of voltage magnification in series resonance. A student who confuses series and parallel resonance will expect the inductor current to equal the source current."

- question: "A parallel RLC tank circuit is used in a radio receiver to select one station from many. At the resonant frequency, it presents high impedance to the antenna signal. Why is high impedance desirable here?"
  type: multiple-choice
  options:
    - "High impedance draws more current at the resonant frequency, amplifying the signal"
    - "High impedance means a larger voltage appears across the tank at the resonant frequency, selecting that station while other frequencies see low impedance"
    - "High impedance prevents the circuit from resonating at unwanted harmonics"
    - "High impedance reduces the bandwidth, making the circuit more selective by increasing energy dissipation"
  answer: 1
  explanation: "In a parallel tuned circuit, the voltage across the tank equals the source current times the impedance. At resonance, impedance is maximum — so the voltage developed at the tuned frequency is maximum. All other frequencies see low impedance, meaning their current is shunted through L and C to ground without developing significant voltage. The selected station 'stands out' as a large voltage; all others are suppressed. This is the fundamental mechanism of radio tuning, exploiting the impedance peak at resonance rather than a current peak."

- question: "In a parallel RLC circuit at resonance, the currents flowing through the inductor and capacitor individually are much larger than the current supplied by the source."
  type: true-false
  answer: true
  explanation: "This is current magnification — the defining characteristic of parallel resonance. At resonance, the inductor current lags the voltage by 90° and the capacitor current leads by 90°; they are exactly opposite in phase and cancel each other when summed at the source terminal. The source sees only the resistive branch and supplies a small current. But the L and C currents themselves are independently Q times larger, circulating in the tank as energy continuously transfers between the magnetic field of the inductor and the electric field of the capacitor."

- question: "Parallel resonance and series resonance behave identically at their respective resonant frequencies: both circuits draw maximum current from the source and present minimum impedance."
  type: true-false
  answer: false
  explanation: "Parallel and series resonance are duals — they behave oppositely at resonance. Series resonance: minimum impedance, maximum source current, maximum voltage across L and C (voltage magnification). Parallel resonance: maximum impedance, minimum source current, maximum voltage across the parallel combination, with circulating currents Q times larger than the source current (current magnification). Confusing these two is a common error when first studying resonant circuits."

- question: "Explain how the quality factor Q determines the selectivity (bandwidth) of a parallel RLC tank circuit, and why a high-Q circuit is preferred in radio tuning applications."
  type: short-answer
  answer: "Q = ω₀/BW = ω₀RC, so a higher Q means a narrower bandwidth (BW = 1/RC). A high-Q circuit presents high impedance over a very narrow frequency range centered on ω₀, dropping to low impedance just slightly above or below resonance. In radio tuning, this means the circuit responds strongly to one station's carrier frequency while rejecting nearby stations with frequencies only slightly different. A low-Q circuit has a wide bandwidth and would pass multiple stations simultaneously, preventing clean signal selection."
  explanation: "The tradeoff is that higher Q requires larger L/C values or lower R (losses). In practice, coil resistance is the main source of loss, so inductor quality determines tank Q. Very high-Q circuits are also more sensitive to component tolerances and temperature drift — a tiny shift in L or C shifts the resonant frequency noticeably in a narrow-band circuit. This is why variable capacitors were used in old radio tuners: small adjustments to C shift ω₀ across the broadcast band while maintaining high Q."
```

## Explainer

You've already studied resonance concepts, including the series RLC circuit where resonance means minimum impedance and maximum current from the source. Parallel RLC resonance is the dual of that story — and understanding the duality is the cleanest path to intuition here.

In a **parallel RLC circuit**, the three components share the same voltage across their terminals. The source drives a current into the parallel combination, and that current splits among R, L, and C. Recall that the inductor's current lags the voltage by 90° while the capacitor's current leads the voltage by 90° — they are exactly out of phase with each other. At the **resonant frequency** ω₀ = 1/√(LC), the currents through L and C are equal in magnitude and opposite in phase, so they cancel each other when viewed from the source terminals. From the source's perspective, the L and C currents sum to zero, leaving only the resistive current. Since the source only has to supply the resistive branch, the total current drawn from the source is minimized — equivalently, the impedance of the parallel combination is **maximized**.

This maximum impedance at resonance is the defining characteristic that inverts the series case. For a high-Q parallel circuit, the impedance at resonance is approximately R (if R is large) or more precisely L/CR for a practical circuit with losses in the inductor. The key phenomenon is **current magnification**: although the source supplies only a modest current, the circulating current sloshing back and forth between the inductor and capacitor can be Q times larger. Energy is continuously trading between the magnetic field of the inductor and the electric field of the capacitor — the reactive currents in the loop are Q times the source current while the tank "resonates." This is analogous to a pendulum swinging with large amplitude from a small periodic push.

The practical consequence is that a high-Q parallel resonant circuit — often called a **tank circuit** — presents a very high impedance at one frequency and low impedance at all others. This makes it ideal for **frequency selection**: in a radio receiver, a tank circuit connected across the input can be tuned to resonate at a desired station's frequency, presenting high impedance (large voltage) at that frequency while shunting all other frequencies to ground through the low impedance off resonance. The **bandwidth** of the parallel resonance is BW = ω₀/Q = 1/(RC), so a high-Q circuit is narrowband and selective, while a low-Q circuit is broadband but less discriminating. Understanding whether you need narrow selectivity or broad response determines whether you want a high-Q or low-Q design — a tradeoff that appears constantly in RF and signal-processing circuits.


