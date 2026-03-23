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
stage: expert
status: draft
---

# Bandwidth and Frequency Domain Specifications

## Core Idea
Bandwidth is the frequency range over which a system responds adequately (typically -3dB point where power is half maximum). Bandwidth directly relates to rise time (bandwidth inversely proportional to rise time) and determines the maximum rate of reference tracking. Frequency specifications complement time-domain specs: wider bandwidth enables faster tracking but increases noise sensitivity.

## Questions

```yaml
- question: "A control engineer needs to reduce the rise time of a servo system from 100 ms to 50 ms. What must happen to the closed-loop bandwidth?"
  type: multiple-choice
  options:
    - "The bandwidth must be doubled, since rise time is approximately inversely proportional to bandwidth"
    - "The bandwidth must be halved, since a faster rise means fewer high-frequency components are needed"
    - "The bandwidth must increase by exactly √2, matching the change in damping ratio"
    - "Rise time and bandwidth are independent design parameters that can be adjusted separately"
  answer: 0
  explanation: "For a second-order system, tr ≈ 1.8/BW, so halving the rise time (100 ms → 50 ms) requires doubling the bandwidth. This is a fundamental physical constraint: a faster step response requires the system to pass higher-frequency content, which is exactly what wider bandwidth means. Option 3 is the key misconception to avoid — rise time and bandwidth are tightly coupled by the physics of frequency response. You cannot make a system respond faster without giving it higher-frequency tracking capability."

- question: "A position control system uses an encoder with significant high-frequency electrical noise. An engineer considers increasing the closed-loop bandwidth from 5 Hz to 50 Hz to improve tracking speed. What is the most likely consequence?"
  type: multiple-choice
  options:
    - "Improved tracking with no adverse effects, since encoder noise averages out over time"
    - "High-frequency encoder noise will be amplified and appear as actuator chatter and position error"
    - "The system will become unconditionally unstable because no practical system can operate above 50 Hz"
    - "The motor will run more smoothly because wider bandwidth averages over more frequencies simultaneously"
  answer: 1
  explanation: "A higher-bandwidth controller faithfully responds to all frequencies within its passband — including noise. Encoder electrical noise at high frequencies, previously attenuated by the narrow-bandwidth design, now passes through the control loop and commands the actuator to follow the noise. The result is increased actuator activity (chatter, wear, high current), not better performance. This is the core bandwidth-noise tradeoff: every frequency added to the passband adds both useful signal tracking and noise sensitivity. Option 0 is wrong — noise does not average away in a closed-loop system; it drives actuator commands."

- question: "The -3 dB bandwidth is the frequency at which the closed-loop output power falls to half its DC value, corresponding to the magnitude ratio dropping to approximately 0.707."
  type: true-false
  answer: true
  explanation: "Power is proportional to the square of amplitude. When amplitude drops to 1/√2 ≈ 0.707, power becomes (1/√2)² = 0.5 — exactly half. In decibels: 20·log₁₀(0.707) ≈ -3 dB (amplitude), or equivalently 10·log₁₀(0.5) = -3 dB (power). This is the standard -3 dB point definition used consistently in signals and systems, control theory, and RF engineering. Signals below this frequency pass with minimal attenuation; above it, they are progressively suppressed."

- question: "Increasing the bandwidth of a closed-loop control system always improves its performance, since higher bandwidth means the system can respond to a wider range of input frequencies."
  type: true-false
  answer: false
  explanation: "More bandwidth means more noise sensitivity — the system responds faithfully to sensor noise, quantization errors, and high-frequency disturbances in addition to the desired input. In physical systems, this manifests as actuator chatter, mechanical wear, and excessive energy consumption. Additionally, increasing loop gain to widen bandwidth reduces phase margin, pushing the system toward instability. The engineering goal is the *minimum* bandwidth that satisfies tracking and disturbance rejection specifications, not the maximum achievable. The noise-bandwidth tradeoff is fundamental and cannot be avoided."

- question: "Explain the fundamental tradeoff between bandwidth and noise sensitivity, and why an engineer cannot simply maximize bandwidth to achieve the fastest possible tracking."
  type: short-answer
  answer: "Bandwidth determines which input frequencies the closed-loop system responds to. All sensors have noise, so the control signal always contains both useful tracking error and noise at every frequency. Below the bandwidth, the controller attempts to correct both genuine tracking error and noise-driven deviations. Maximizing bandwidth therefore maximizes noise amplification: the actuator is commanded to correct for every noise fluctuation, not just real errors. In practice this causes chattering, actuator wear, and possibly instability near the phase crossover frequency. The engineer selects the minimum bandwidth that tracks desired reference trajectories within spec while keeping noise-induced actuator activity within acceptable bounds — a tradeoff requiring knowledge of both the reference spectrum and the sensor noise spectrum."
  explanation: "This tradeoff is why practical control design involves both frequency-domain specifications (bandwidth, gain/phase margins) and noise characterization. A motor control system for a precision robot needs to track smooth position commands but not encoder count noise; a sensor filtering bandwidth below encoder noise frequencies achieves acceptable tracking without chattering. The same principle applies in electrical circuit design (op-amp bandwidth limits), communication receivers (noise-bandwidth tradeoffs), and signal processing."
```

## Explainer

From your study of frequency response magnitude and phase, you know how to interpret a system's Bode plot — the magnitude tells you how much the system amplifies or attenuates signals at each frequency. **Bandwidth** gives a single-number summary of that plot: it is the frequency at which the closed-loop magnitude first drops to -3 dB (0.707 of its DC value, equivalently the half-power point). Signals at frequencies below the bandwidth pass through essentially unchanged; signals above it are increasingly attenuated. The bandwidth is therefore the natural measure of how fast a system can respond to changing inputs.

The connection to time-domain behavior is intuitive. A signal that changes rapidly has high-frequency content — it contains Fourier components at high frequencies. If those frequencies exceed the system's bandwidth, the system will not track them. The approximate relationship for a second-order system is BW ≈ ωn·√(1 − 2ζ² + √(4ζ⁴ − 4ζ² + 2)), which for moderate damping (ζ ≈ 0.5–0.7) simplifies to roughly BW ≈ ωn. Since rise time tr ≈ 1.8/ωn, we get the rule of thumb tr ≈ 1.8/BW. **Doubling the bandwidth halves the rise time.** Faster response always requires higher bandwidth.

The cost of wider bandwidth is **noise sensitivity**. Real systems have sensor noise, quantization errors, and disturbances injected at many frequencies. A high-bandwidth controller faithfully tracks all of these, amplifying noise that was supposed to be ignored. In a motor control system, wide bandwidth means the motor responds to every voltage spike and sensor glitch, causing chattering and wear. The engineer's job is to choose a bandwidth that is fast enough to track the desired reference trajectory but not so wide that noise becomes a significant fraction of the control signal — a judgment call informed by knowledge of the noise spectrum.

**Frequency-domain specifications** complement time-domain specs rather than replacing them. Rise time and settling time tell you directly about step responses; bandwidth tells you about the response to a *spectrum* of inputs including sinusoids and disturbances. A well-designed control system specifies both: e.g., "rise time under 50 ms, settling time under 200 ms, bandwidth 10 Hz." When you move to compensator design (lead/lag networks, PID tuning), these frequency specifications become the design targets — you shape the open-loop Bode plot to achieve the desired closed-loop bandwidth while maintaining adequate phase margin for stability.
