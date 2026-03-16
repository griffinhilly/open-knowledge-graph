---
id: resonance-and-peaking-response
title: Resonance, Peaking, and Bandwidth Relationships
domain: engineering
course: control-systems
prerequisites:
- id: bandwidth-and-cutoff-frequencies
  type: hard
- id: natural-frequency-damping-second-order
  type: soft
builds-toward:
- lead-lag-compensation-design
tags:
- resonance
- peaking
- bandwidth
- frequency-response
stage: advanced
status: draft
---

# Resonance, Peaking, and Bandwidth Relationships

## Core Idea
Resonance occurs when system natural frequency aligns with input frequency, causing amplitude amplification above DC gain. Peak resonance magnitude (Mr, resonance peak) and resonant frequency (ωr) depend on damping: lower damping yields higher peaks and sharpened resonance. The relationship between Mr, bandwidth, and damping provides design insight: reducing damping increases bandwidth but increases peaking and overshoot—a fundamental design trade-off.

## Explainer

You know from bandwidth and cutoff frequency analysis that a system's frequency response has a characteristic shape — flat at low frequencies, then rolling off. You also know from second-order system theory that the **natural frequency ω_n** and **damping ratio ζ** together define how a system responds. Resonance is the phenomenon that connects these: when the driving frequency is close to ω_n, the system amplifies the input rather than attenuating it — the output is *larger* than the input, not smaller.

The physical mechanism is energy exchange. An underdamped second-order system stores energy in two forms (think of a spring-mass system: kinetic and potential, or an LC circuit: magnetic and electric). Near the natural frequency, energy sloshes back and forth between the two storage elements in synchrony with the driving signal. If damping is low, little energy escapes each cycle, and the oscillation grows large. At exactly the resonant frequency ω_r = ω_n √(1 − 2ζ²), the magnitude of the frequency response reaches its peak **M_r** = 1 / (2ζ√(1 − ζ²)). Notice that as ζ → 0, M_r → ∞ — an undamped system driven at resonance grows without bound.

The damping ratio governs a direct trade-off between three related quantities: **peaking**, **bandwidth**, and **time-domain overshoot**. Reducing ζ (less damping) increases M_r (more peaking in frequency domain), increases bandwidth (the −3 dB frequency rises), and increases percent overshoot in the step response. These are not independent consequences you can pick among — they are manifestations of the same underlying system pole locations moving closer to the imaginary axis. A system with ζ = 0.707 ("critically flat" or Butterworth response) has M_r ≈ 1 (no peaking) and about 4% step overshoot — often a good starting point for design. A system with ζ = 0.5 has M_r ≈ 1.15 and about 16% overshoot.

For control design, this trade-off is a central constraint. You can make a system respond faster (wider bandwidth, lower ζ), but you pay with peaking and overshoot — the system overshoots its target and may oscillate before settling. You can make a system well-damped (high ζ, low overshoot), but it becomes sluggish and slow to reject disturbances. Real specifications typically constrain both: a step response must settle within X% of final value in time T, *and* peak no more than Y% above — translating directly into constraints on ζ and ω_n. Understanding the resonance-damping-bandwidth relationship is what lets you read those specs and immediately reason about whether they are achievable and at what cost.
