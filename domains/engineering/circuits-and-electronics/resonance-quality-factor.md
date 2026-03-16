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
tags:
- resonance
- bandwidth
- quality-factor
- selectivity
- damping
stage: formal-systems
status: draft
---

# Resonance and Quality Factor in RLC Circuits

## Core Idea
Resonance occurs when inductive and capacitive reactances cancel at frequency ω₀ = 1/√(LC), minimizing impedance in series circuits and maximizing impedance in parallel circuits. Quality factor Q = ω₀L/R = 1/(ω₀RC) characterizes resonance sharpness and bandwidth, relating energy storage to dissipation. High-Q resonant circuits are essential for filtering, oscillation, and signal selection applications.

## Explainer

Using phasors, you know that inductive reactance X_L = ωL grows with frequency while capacitive reactance X_C = 1/(ωC) shrinks with frequency. At low frequencies, the capacitor dominates and blocks the signal; at high frequencies, the inductor dominates. At exactly one frequency, they are equal in magnitude: ωL = 1/(ωC), which gives the **resonant frequency** ω₀ = 1/√(LC). At this frequency, the reactive parts cancel — the inductor's impedance +jω₀L and the capacitor's impedance −j/(ω₀C) sum to zero, leaving only resistance.

In a **series RLC circuit**, this cancellation makes total impedance a minimum equal to just R. For a fixed source voltage, maximum current flows at resonance. In a **parallel RLC circuit**, the situation inverts: the inductive and capacitive currents cancel in the parallel branches, so the circuit draws minimum current from the source — the parallel combination presents maximum impedance at ω₀. Both cases represent a sharp peak in the circuit's frequency response: near resonance, behavior changes dramatically; far from resonance, either the capacitor (below ω₀) or inductor (above ω₀) dominates and attenuates the response.

The **quality factor** Q = ω₀L/R characterizes how sharp this peak is. The physical definition — Q = 2π × (energy stored / energy dissipated per cycle) = ω₀ / bandwidth — reveals what Q actually measures: the ratio of reactive energy circulation to resistive loss. A high-Q circuit passes energy back and forth between the inductor's magnetic field and the capacitor's electric field many times per cycle before resistance dissipates it. This manifests as a narrow, tall resonance peak and a small **bandwidth** BW = ω₀/Q. A low-Q circuit dissipates energy quickly, producing a broad, flat response.

The practical importance of Q is widespread. A radio receiver must select one station's frequency (say, 98.1 MHz) while rejecting adjacent stations at 97.9 and 98.3 MHz — this requires high Q to achieve narrow bandwidth. A crystal oscillator in a clock uses quartz with Q in the millions, producing an extremely stable frequency because the resonance is so sharp that small perturbations barely shift ω₀. Conversely, the tone controls in audio equipment use moderate-Q circuits to smoothly boost or cut frequency bands without creating narrow spikes or notches. In all these cases, Q is the single number that captures how "focused" the resonant response is — the ratio of energy storage to loss.
