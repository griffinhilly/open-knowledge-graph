---
id: second-order-system-response-analysis
title: Second-Order System Response Analysis
domain: engineering
course: control-systems
prerequisites:
- id: transfer-functions-control
  type: hard
builds-toward:
- transient-response-damping-oscillation
- bandwidth-resonance-frequency-selection
tags:
- natural-frequency
- damping-ratio
- poles
- characteristic-equation
stage: advanced
status: draft
---

# Second-Order System Response Analysis

## Core Idea
Second-order systems have two poles determined by natural frequency ωₙ and damping ratio ζ. For ζ < 1 (underdamped), response oscillates; ζ = 1 (critically damped) is the fastest non-oscillatory response; ζ > 1 (overdamped) is slower and non-oscillatory.

## Explainer

The transfer function maps input signals to output signals in the Laplace domain. A **second-order system** has a transfer function whose denominator is a quadratic in s — meaning two poles, which together determine everything about the transient behavior. The standard form is H(s) = ωₙ²/(s² + 2ζωₙs + ωₙ²). Just two parameters — **natural frequency** ωₙ and **damping ratio** ζ — completely characterize how the system responds to any input.

The poles sit at s = −ζωₙ ± jωₙ√(1 − ζ²). When ζ < 1 (underdamped), the poles are complex conjugates in the left half-plane. The real part −ζωₙ controls how fast oscillations decay; the imaginary part ωd = ωₙ√(1 − ζ²) is the damped oscillation frequency. Think of a mass-spring-damper: ωₙ is the frequency the system would oscillate at with no damping, and ζ measures how much friction suppresses that oscillation. Low ζ (light damping) gives many visible oscillations before settling; ζ approaching 1 gives a faster, smoother approach to steady state.

When ζ = 1, the two poles merge at s = −ωₙ on the real axis — **critical damping**, the boundary between oscillatory and non-oscillatory response. The step response reaches its final value as fast as possible without overshoot. For ζ > 1, the poles split along the negative real axis; the slower pole (closer to the origin) dominates, and the response decays exponentially without oscillating — but more sluggishly than the critically damped case.

Key transient specifications connect directly to ζ and ωₙ through closed-form formulas. **Percent overshoot** OS% = exp(−πζ/√(1−ζ²)) × 100 depends only on ζ. **Peak time** tp = π/ωd depends on the damped frequency. **Settling time** ts ≈ 4/(ζωₙ) depends on the real part of the poles. This means ωₙ scales the speed of everything — higher ωₙ compresses all time scales — while ζ controls the shape: how much the response overshoots and how quickly it settles relative to the oscillation. Given a specification like "less than 10% overshoot and settling within 2 seconds," you solve backward for the required ζ and ωₙ, then design a system whose poles land at those values. This design-by-specification approach is the central skill these formulas enable.
