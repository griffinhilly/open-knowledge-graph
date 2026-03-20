---
id: circuit-resonance-concepts
title: Circuit Resonance Concepts
domain: engineering
course: circuits-and-electronics
prerequisites:
- id: rlc-circuit-transient-analysis-overview
  type: hard
- id: AC-power-calculation-and-factor
  type: soft
builds-toward:
- series-RLC-resonance-characteristics
- parallel-RLC-resonance-characteristics
tags:
- resonance
- natural-frequency
- bandwidth
- Q-factor
stage: advanced
status: draft
---

# Circuit Resonance Concepts

## Core Idea
Resonance occurs when inductive and capacitive reactances cancel, making impedance purely resistive. The resonant frequency ω₀ = 1/√(LC) is independent of resistance. At resonance, impedance is minimum (series) or maximum (parallel), and power transfer is maximum. The quality factor Q determines how sharp the resonance peak is and the bandwidth.

## Explainer

From your work on RLC transient analysis, you know that inductors and capacitors store energy in magnetic and electric fields respectively, and that their impedances are frequency-dependent: Z_L = jωL rises with frequency, while Z_C = 1/jωC falls with frequency. Resonance is what happens when these two frequency-dependent effects exactly cancel each other, leaving only the resistive component standing.

At the **resonant frequency** ω₀ = 1/√(LC), the inductive reactance jω₀L equals the capacitive reactance 1/jω₀C in magnitude (they are opposite in sign, so they cancel). This result is purely determined by L and C — resistance plays no role in setting ω₀. In a series RLC circuit, at resonance the total impedance collapses to just R, so current is maximized for a given voltage. In a parallel RLC circuit, at resonance the impedance is maximized (the tank circuit looks like an open circuit to the source), so voltage across the circuit is maximized. These opposite behaviors — series resonance minimizes impedance, parallel resonance maximizes it — both arise from the same cancellation mechanism but manifest differently because of the circuit topology.

The **quality factor Q** captures how sharply peaked the resonance response is, and it relates two competing aspects of the circuit: energy storage versus energy loss. Q = ω₀L/R = 1/(ω₀CR) for a series circuit — it is the ratio of reactive impedance to resistance at resonance. A high-Q circuit stores a lot of energy relative to what it dissipates per cycle: energy sloshes between the inductor and capacitor with little leaking out through the resistor. Physically, high Q means the resonance peak is tall and narrow. A low-Q circuit dissipates energy quickly, giving a broad, flat peak. The **bandwidth** BW = ω₀/Q is the range of frequencies within 3 dB of the peak — a high-Q circuit selects a narrow band of frequencies (useful in filters and tuners), while a low-Q circuit responds to a wide band.

The practical significance is that Q links the time domain to the frequency domain. In the transient analysis you already studied, a high-Q RLC circuit produces many oscillations before dying out (underdamped with slow decay); a low-Q circuit barely oscillates before settling (overdamped or lightly underdamped). In the frequency domain, that same high-Q circuit acts as a sharp bandpass filter. Both descriptions are two views of the same physical reality: energy stored relative to energy lost per cycle. This connection between Q, bandwidth, and transient behavior is the reason resonance appears across all of electronics — in filters, oscillators, amplifiers, and antenna systems.
