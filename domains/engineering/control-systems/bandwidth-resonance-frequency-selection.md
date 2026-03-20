---
id: bandwidth-resonance-frequency-selection
title: Bandwidth and Resonant Frequency Selection
domain: engineering
course: control-systems
prerequisites:
- id: frequency-response-magnitude-phase-plots
  type: hard
- id: frequency-response-magnitude-phase-basics
  type: soft
builds-toward:
- control-loop-design-via-bode-plots
tags:
- bandwidth
- resonance
- peak
- magnitude-response
- frequency-domain-performance
stage: advanced
status: draft
---
# Bandwidth and Resonant Frequency Selection

## Core Idea
Bandwidth is the frequency at which magnitude drops to −3 dB (0.707 times the DC value). It indicates how fast a system can respond to changing reference inputs. Resonant peaks indicate underdamped modes; peak height increases as damping decreases.

## Explainer

From your study of frequency response and Bode plots, you know how to compute and plot a system's gain and phase as a function of frequency — the magnitude plot showing |G(jω)| and the phase plot showing ∠G(jω). Bandwidth and resonance are the two most important features to read off those plots when assessing how a system will perform in closed-loop operation.

**Bandwidth** (ω_BW) is the frequency at which the closed-loop magnitude response drops to −3 dB, which corresponds to a gain of 0.707 (or 1/√2) relative to the DC value. The −3 dB criterion is not arbitrary: it is the frequency at which output power has dropped to half of its DC value (since power is proportional to amplitude squared). Below the bandwidth, the system tracks reference inputs faithfully — a sinusoidal command at frequency ω < ω_BW produces a nearly full-amplitude output. Above the bandwidth, the system cannot keep up: output amplitude shrinks and phase lag increases, meaning fast reference changes are partially or fully filtered out. Bandwidth is therefore a direct measure of **speed**: a wider bandwidth means the system can track faster-changing references. Practically, doubling the bandwidth roughly halves the rise time of the step response.

**Resonant peaks** in the frequency response appear when the system has **underdamped poles** — complex conjugate poles whose real part is small relative to their imaginary part. A second-order system with natural frequency ω_n and damping ratio ζ has a closed-loop frequency response that peaks near ω_n when ζ < 1/√2 ≈ 0.707. The peak magnitude is **M_p = 1/(2ζ√(1−ζ²))**, which grows without bound as ζ → 0. A resonant peak in the frequency response translates directly into overshoot in the step response: a system whose magnitude peaks at +6 dB will produce roughly 30% overshoot on a step input. This is the critical link between the frequency domain (where controller design happens) and the time domain (where performance specifications are written).

The **tradeoff between bandwidth and resonance** is central to control design. Increasing controller gain generally pushes the closed-loop bandwidth higher — faster tracking — but also brings the closed-loop poles closer to the imaginary axis, increasing the resonant peak and overshoot. Aggressive bandwidth comes at the cost of oscillatory transient behavior, noise sensitivity (high-frequency disturbances are amplified near the resonant peak), and eventually instability. The practical design goal is to achieve the bandwidth required by the speed specification while keeping M_p below about 3–6 dB (corresponding to ζ ≥ 0.35–0.5), ensuring acceptable damping. Resonant peaks at or above 0 dB — meaning the magnitude response exceeds DC gain at some frequency — indicate very underdamped behavior and often signal that the design is approaching instability margins.
