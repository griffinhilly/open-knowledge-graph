---
id: bandwidth-and-cutoff-frequencies
title: Bandwidth and Frequency Domain Specifications
domain: engineering
course: control-systems
prerequisites:
- id: frequency-response-magnitude-and-phase
  type: hard
builds-toward:
- gain-phase-margins-stability-robustness
- resonance-and-peaking-response
tags:
- bandwidth
- cutoff-frequency
- frequency-domain
- specifications
stage: advanced
status: draft
---

# Bandwidth and Frequency Domain Specifications

## Core Idea
Bandwidth is the frequency range over which a system responds adequately (typically -3dB point where power is half maximum). Bandwidth directly relates to rise time (bandwidth inversely proportional to rise time) and determines the maximum rate of reference tracking. Frequency specifications complement time-domain specs: wider bandwidth enables faster tracking but increases noise sensitivity.

## Explainer

From your study of frequency response magnitude and phase, you know how to interpret a system's Bode plot — the magnitude tells you how much the system amplifies or attenuates signals at each frequency. **Bandwidth** gives a single-number summary of that plot: it is the frequency at which the closed-loop magnitude first drops to -3 dB (0.707 of its DC value, equivalently the half-power point). Signals at frequencies below the bandwidth pass through essentially unchanged; signals above it are increasingly attenuated. The bandwidth is therefore the natural measure of how fast a system can respond to changing inputs.

The connection to time-domain behavior is intuitive. A signal that changes rapidly has high-frequency content — it contains Fourier components at high frequencies. If those frequencies exceed the system's bandwidth, the system will not track them. The approximate relationship for a second-order system is BW ≈ ωn·√(1 − 2ζ² + √(4ζ⁴ − 4ζ² + 2)), which for moderate damping (ζ ≈ 0.5–0.7) simplifies to roughly BW ≈ ωn. Since rise time tr ≈ 1.8/ωn, we get the rule of thumb tr ≈ 1.8/BW. **Doubling the bandwidth halves the rise time.** Faster response always requires higher bandwidth.

The cost of wider bandwidth is **noise sensitivity**. Real systems have sensor noise, quantization errors, and disturbances injected at many frequencies. A high-bandwidth controller faithfully tracks all of these, amplifying noise that was supposed to be ignored. In a motor control system, wide bandwidth means the motor responds to every voltage spike and sensor glitch, causing chattering and wear. The engineer's job is to choose a bandwidth that is fast enough to track the desired reference trajectory but not so wide that noise becomes a significant fraction of the control signal — a judgment call informed by knowledge of the noise spectrum.

**Frequency-domain specifications** complement time-domain specs rather than replacing them. Rise time and settling time tell you directly about step responses; bandwidth tells you about the response to a *spectrum* of inputs including sinusoids and disturbances. A well-designed control system specifies both: e.g., "rise time under 50 ms, settling time under 200 ms, bandwidth 10 Hz." When you move to compensator design (lead/lag networks, PID tuning), these frequency specifications become the design targets — you shape the open-loop Bode plot to achieve the desired closed-loop bandwidth while maintaining adequate phase margin for stability.
