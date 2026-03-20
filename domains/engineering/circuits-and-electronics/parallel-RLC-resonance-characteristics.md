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
stage: advanced
status: draft
---

# Parallel RLC Resonance Characteristics

## Core Idea
In a parallel RLC circuit at resonance, impedance is maximum (approximately L/CR for high Q), current through R is maximum, and circulating currents in L and C can exceed the source current by a factor Q (current magnification). Parallel resonance appears in tuning circuits and reactive load compensation.

## Explainer

You've already studied resonance concepts, including the series RLC circuit where resonance means minimum impedance and maximum current from the source. Parallel RLC resonance is the dual of that story — and understanding the duality is the cleanest path to intuition here.

In a **parallel RLC circuit**, the three components share the same voltage across their terminals. The source drives a current into the parallel combination, and that current splits among R, L, and C. Recall that the inductor's current lags the voltage by 90° while the capacitor's current leads the voltage by 90° — they are exactly out of phase with each other. At the **resonant frequency** ω₀ = 1/√(LC), the currents through L and C are equal in magnitude and opposite in phase, so they cancel each other when viewed from the source terminals. From the source's perspective, the L and C currents sum to zero, leaving only the resistive current. Since the source only has to supply the resistive branch, the total current drawn from the source is minimized — equivalently, the impedance of the parallel combination is **maximized**.

This maximum impedance at resonance is the defining characteristic that inverts the series case. For a high-Q parallel circuit, the impedance at resonance is approximately R (if R is large) or more precisely L/CR for a practical circuit with losses in the inductor. The key phenomenon is **current magnification**: although the source supplies only a modest current, the circulating current sloshing back and forth between the inductor and capacitor can be Q times larger. Energy is continuously trading between the magnetic field of the inductor and the electric field of the capacitor — the reactive currents in the loop are Q times the source current while the tank "resonates." This is analogous to a pendulum swinging with large amplitude from a small periodic push.

The practical consequence is that a high-Q parallel resonant circuit — often called a **tank circuit** — presents a very high impedance at one frequency and low impedance at all others. This makes it ideal for **frequency selection**: in a radio receiver, a tank circuit connected across the input can be tuned to resonate at a desired station's frequency, presenting high impedance (large voltage) at that frequency while shunting all other frequencies to ground through the low impedance off resonance. The **bandwidth** of the parallel resonance is BW = ω₀/Q = 1/(RC), so a high-Q circuit is narrowband and selective, while a low-Q circuit is broadband but less discriminating. Understanding whether you need narrow selectivity or broad response determines whether you want a high-Q or low-Q design — a tradeoff that appears constantly in RF and signal-processing circuits.


