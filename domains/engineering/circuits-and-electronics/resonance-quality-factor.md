---
id: resonance-quality-factor
title: Resonance and Quality Factor in RLC Circuits
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: phasor-notation-and-complex-algebra
  type: hard
- id: energy-storage-elements-l-and-c
  type: hard
- id: transient-response-rlc-circuits
  type: soft
tags:
- resonance
- bandwidth
- quality-factor
- selectivity
- damping
stage: formal-systems
status: validated
---
# Resonance and Quality Factor in RLC Circuits

## Core Idea
Resonance occurs when inductive and capacitive reactances cancel at frequency ω₀ = 1/√(LC), minimizing impedance in series circuits and maximizing impedance in parallel circuits. Quality factor Q = ω₀L/R = 1/(ω₀RC) characterizes resonance sharpness and bandwidth, relating energy storage to dissipation. High-Q resonant circuits are essential for filtering, oscillation, and signal selection applications.

## Questions

```yaml
- question: "A series RLC circuit is driven by an AC voltage source. As the frequency is swept from DC to very high frequencies, at what frequency does the current through the circuit reach its maximum value?"
  type: multiple-choice
  options:
    - "At the lowest frequency, because capacitive reactance is highest and forces more current"
    - "At the resonant frequency ω₀ = 1/√(LC), because the reactive elements cancel and only R remains"
    - "At the highest frequency, because inductive reactance rises with frequency and boosts current"
    - "At resonance, the current is zero because inductive and capacitive reactances cancel"
  answer: 1
  explanation: "In a series RLC circuit, total impedance is Z = R + j(ωL − 1/ωC). At resonance, the imaginary parts cancel: ωL = 1/ωC, leaving Z = R (purely resistive minimum). By Ohm's law, I = V/Z, so minimum impedance means maximum current. At low frequencies, the capacitor's large reactance 1/ωC dominates and impedes current. At high frequencies, the inductor's large reactance ωL dominates. The resonant frequency is the sweet spot where both reactive elements cancel each other, and only the resistive loss remains. Option D reverses the series/parallel distinction: zero impedance at resonance is for parallel circuits, not series."

- question: "A radio receiver uses a resonant circuit to select a station at 98.1 MHz while rejecting adjacent stations at 97.9 and 98.3 MHz (a separation of 200 kHz). Which Q factor better achieves this selectivity?"
  type: multiple-choice
  options:
    - "Q = 5, because lower Q produces a broader response that captures more signal energy"
    - "Q = 500, because higher Q produces a narrower bandwidth, rejecting adjacent frequencies"
    - "Q = 1, because at Q = 1 the circuit is critically damped and most selective"
    - "Q doesn't affect bandwidth — it only affects how high the resonance peak rises"
  answer: 1
  explanation: "Bandwidth BW = ω₀/Q. A higher Q means smaller bandwidth — the circuit passes a narrower range of frequencies around ω₀. To separate stations 200 kHz apart at 98.1 MHz, the bandwidth must be less than 200 kHz, requiring Q > 98.1 MHz / 200 kHz ≈ 490. Q = 500 achieves this; Q = 5 would produce a bandwidth of ~20 MHz, completely failing to distinguish adjacent stations. Option D is wrong: Q directly determines bandwidth through BW = ω₀/Q, and the bandwidth is the primary practical consequence of Q in filter applications."

- question: "At resonance, a series RLC circuit exhibits maximum impedance because the inductive and capacitive reactances cancel and reinforce each other."
  type: true-false
  answer: false
  explanation: "This confuses series and parallel resonance. In a *series* RLC circuit, resonance produces *minimum* impedance — the reactive parts cancel (they are equal and opposite in sign: +jωL and −j/ωC), leaving only the resistance R. Minimum impedance → maximum current for a fixed voltage source. In a *parallel* RLC circuit, resonance produces *maximum* impedance because the inductive and capacitive branch currents cancel, so the parallel combination draws minimum current from the source. The statement is true for parallel circuits but false for series circuits. The polarity flip between series and parallel resonance is the most common confusion in this topic."

- question: "Doubling the quality factor Q of a resonant circuit (while holding ω₀ constant) halves the circuit's 3dB bandwidth."
  type: true-false
  answer: true
  explanation: "This follows directly from the relationship BW = ω₀/Q. If Q doubles with ω₀ fixed, the denominator doubles, so BW halves. This is a precise inverse proportionality. Physically, higher Q means the circuit stores energy more efficiently relative to how fast resistance dissipates it — energy recirculates between L and C many more times before fading, creating a sharper, narrower resonance peak. Halving the bandwidth means the circuit becomes twice as selective: it passes a narrower range of frequencies around ω₀ and more aggressively attenuates frequencies even slightly off resonance."

- question: "Explain physically why a high-Q resonant circuit has a narrower bandwidth than a low-Q circuit, using the concept of energy storage and dissipation."
  type: short-answer
  answer: "Q measures the ratio of energy stored in the reactive elements (L and C) to energy dissipated in resistance per cycle. A high-Q circuit stores much more energy than it loses each cycle, so energy sloshes back and forth between the inductor's magnetic field and the capacitor's electric field many times before resistance dissipates it. This means the circuit responds strongly to frequencies near ω₀ (where it stores energy efficiently) and very weakly to nearby frequencies (where the storage-to-loss ratio drops off sharply). A low-Q circuit dissipates energy quickly relative to what it stores, so the resonance peak is broad and flat — it responds to a wider range of frequencies without strong discrimination."
  explanation: "The energy perspective makes the bandwidth formula BW = ω₀/Q intuitive. 'Bandwidth' is the frequency range where the circuit still responds with at least half its peak power. A high-Q circuit has sharp discrimination precisely because its stored energy per cycle is large relative to loss — slight departures from ω₀ immediately tip the balance toward net loss, collapsing the response. A crystal resonator with Q in the millions has almost no bandwidth at all: only frequencies within a few hertz of ω₀ couple efficiently to the crystal's mechanical resonance."
```

## Explainer

Using phasors, you know that inductive reactance X_L = ωL grows with frequency while capacitive reactance X_C = 1/(ωC) shrinks with frequency. At low frequencies, the capacitor dominates and blocks the signal; at high frequencies, the inductor dominates. At exactly one frequency, they are equal in magnitude: ωL = 1/(ωC), which gives the **resonant frequency** ω₀ = 1/√(LC). At this frequency, the reactive parts cancel — the inductor's impedance +jω₀L and the capacitor's impedance −j/(ω₀C) sum to zero, leaving only resistance.

In a **series RLC circuit**, this cancellation makes total impedance a minimum equal to just R. For a fixed source voltage, maximum current flows at resonance. In a **parallel RLC circuit**, the situation inverts: the inductive and capacitive currents cancel in the parallel branches, so the circuit draws minimum current from the source — the parallel combination presents maximum impedance at ω₀. Both cases represent a sharp peak in the circuit's frequency response: near resonance, behavior changes dramatically; far from resonance, either the capacitor (below ω₀) or inductor (above ω₀) dominates and attenuates the response.

The **quality factor** Q = ω₀L/R characterizes how sharp this peak is. The physical definition — Q = 2π × (energy stored / energy dissipated per cycle) = ω₀ / bandwidth — reveals what Q actually measures: the ratio of reactive energy circulation to resistive loss. A high-Q circuit passes energy back and forth between the inductor's magnetic field and the capacitor's electric field many times per cycle before resistance dissipates it. This manifests as a narrow, tall resonance peak and a small **bandwidth** BW = ω₀/Q. A low-Q circuit dissipates energy quickly, producing a broad, flat response.

The practical importance of Q is widespread. A radio receiver must select one station's frequency (say, 98.1 MHz) while rejecting adjacent stations at 97.9 and 98.3 MHz — this requires high Q to achieve narrow bandwidth. A crystal oscillator in a clock uses quartz with Q in the millions, producing an extremely stable frequency because the resonance is so sharp that small perturbations barely shift ω₀. Conversely, the tone controls in audio equipment use moderate-Q circuits to smoothly boost or cut frequency bands without creating narrow spikes or notches. In all these cases, Q is the single number that captures how "focused" the resonant response is — the ratio of energy storage to loss.
