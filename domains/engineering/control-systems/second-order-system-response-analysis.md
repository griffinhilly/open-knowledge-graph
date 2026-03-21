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

## Questions

```yaml
- question: "A control engineer needs to reduce settling time in a second-order system by increasing the natural frequency ωₙ while keeping the damping ratio ζ fixed. What happens to the percent overshoot?"
  type: multiple-choice
  options:
    - "Overshoot increases because faster systems oscillate more"
    - "Overshoot decreases because higher ωₙ adds effective damping"
    - "Overshoot is unchanged because percent overshoot depends only on ζ"
    - "Overshoot doubles along with the reduction in settling time"
  answer: 2
  explanation: "Percent overshoot is OS% = exp(−πζ/√(1−ζ²)) × 100, which depends exclusively on ζ. Increasing ωₙ compresses all time scales — settling time (ts ≈ 4/(ζωₙ)) and peak time (tp = π/ωd) both decrease — but does not change the shape of the response. ωₙ is a speed dial; ζ is a shape dial. This independence is what makes the two-parameter framework so powerful: you can design for speed and shape independently by placing poles at a chosen (ζ, ωₙ) combination."

- question: "A second-order system has damping ratio ζ = 0.1. Compared to a system with ζ = 0.7, what is the expected step response behavior?"
  type: multiple-choice
  options:
    - "Faster settling with no overshoot, because light damping means little energy loss"
    - "Slower response with a single smooth rise to the setpoint"
    - "Large percent overshoot and many oscillations before settling"
    - "The same settling time but with a sharper initial rise"
  answer: 2
  explanation: "ζ = 0.1 is highly underdamped — much less than the critical value of 1. The poles are complex with a small real part (−ζωₙ is small), meaning oscillations decay very slowly. OS% ≈ exp(−π·0.1/√0.99) × 100 ≈ 73% — nearly three-quarters of the final value as overshoot. ζ = 0.7 gives about 4.6% overshoot and settles quickly. A common misconception is that 'lighter damping = faster' — it oscillates longer, so settling time is actually worse despite the faster initial rise."

- question: "For a second-order system, the percent overshoot depends only on the damping ratio ζ and is independent of the natural frequency ωₙ."
  type: true-false
  answer: true
  explanation: "The formula OS% = exp(−πζ/√(1−ζ²)) × 100 contains only ζ — ωₙ does not appear. This means two systems with the same ζ but very different natural frequencies (one fast, one slow) will have identical percent overshoot; they simply reach that overshoot at different times. ωₙ scales the time axis, stretching or compressing the step response without changing its shape. This is why pole placement typically targets a specific (ζ, ωₙ) pair: ζ sets overshoot, ωₙ sets speed."

- question: "A critically damped system (ζ = 1) oscillates once and then settles, making it faster to reach steady state than an underdamped system."
  type: true-false
  answer: false
  explanation: "Critical damping (ζ = 1) produces NO oscillation. The two poles merge at s = −ωₙ on the real axis, giving a monotonically increasing step response that approaches the final value without overshoot. It is the *fastest possible non-oscillatory response*. An underdamped system (ζ < 1) initially rises faster and overshoots, but then oscillates around the setpoint — it may cross the final value sooner, but 'settling' (staying within a tolerance band) takes longer. Critical damping is not 'oscillates once'; it is the boundary condition below which oscillation begins."

- question: "A system is overdamped (ζ > 1). It has no overshoot — so why is this not always the preferred design choice? What is the tradeoff compared to critical damping?"
  type: short-answer
  answer: "Overdamped systems have two distinct real poles; the slower pole (closer to the origin) dominates, making the response sluggish. The system approaches its final value more slowly than a critically damped system with the same ωₙ. Critical damping (ζ = 1) achieves the fastest possible response without any overshoot — it is the optimal balance point. Increasing ζ beyond 1 trades speed for no benefit (overshoot is already zero at ζ = 1). The practical tradeoff: overdamping avoids overshoot but at the cost of slower response, which may be unacceptable in applications requiring fast setpoint tracking."
  explanation: "In control design, the choice depends on what penalty the application places on overshoot vs. speed. Safety-critical systems (e.g., positioning mechanisms near physical stops) may demand overdamping to guarantee no overshoot at the cost of speed. High-performance systems (robotics, hard disk drive heads) tolerate small overshoot (ζ ≈ 0.7, OS ≈ 4.6%) in exchange for much faster settling. ζ = 0.7 is a common engineering target because it gives low overshoot and settling time roughly equal to the critically damped case — a sweet spot between the extremes."
```

## Explainer

The transfer function maps input signals to output signals in the Laplace domain. A **second-order system** has a transfer function whose denominator is a quadratic in s — meaning two poles, which together determine everything about the transient behavior. The standard form is H(s) = ωₙ²/(s² + 2ζωₙs + ωₙ²). Just two parameters — **natural frequency** ωₙ and **damping ratio** ζ — completely characterize how the system responds to any input.

The poles sit at s = −ζωₙ ± jωₙ√(1 − ζ²). When ζ < 1 (underdamped), the poles are complex conjugates in the left half-plane. The real part −ζωₙ controls how fast oscillations decay; the imaginary part ωd = ωₙ√(1 − ζ²) is the damped oscillation frequency. Think of a mass-spring-damper: ωₙ is the frequency the system would oscillate at with no damping, and ζ measures how much friction suppresses that oscillation. Low ζ (light damping) gives many visible oscillations before settling; ζ approaching 1 gives a faster, smoother approach to steady state.

When ζ = 1, the two poles merge at s = −ωₙ on the real axis — **critical damping**, the boundary between oscillatory and non-oscillatory response. The step response reaches its final value as fast as possible without overshoot. For ζ > 1, the poles split along the negative real axis; the slower pole (closer to the origin) dominates, and the response decays exponentially without oscillating — but more sluggishly than the critically damped case.

Key transient specifications connect directly to ζ and ωₙ through closed-form formulas. **Percent overshoot** OS% = exp(−πζ/√(1−ζ²)) × 100 depends only on ζ. **Peak time** tp = π/ωd depends on the damped frequency. **Settling time** ts ≈ 4/(ζωₙ) depends on the real part of the poles. This means ωₙ scales the speed of everything — higher ωₙ compresses all time scales — while ζ controls the shape: how much the response overshoots and how quickly it settles relative to the oscillation. Given a specification like "less than 10% overshoot and settling within 2 seconds," you solve backward for the required ζ and ωₙ, then design a system whose poles land at those values. This design-by-specification approach is the central skill these formulas enable.
