---
id: time-domain-performance-specifications
title: Time-Domain Performance Metrics and Specifications
domain: engineering
course: control-systems
prerequisites:
- id: natural-frequency-damping-second-order
  type: hard
- id: first-order-system-response-analysis
  type: soft
builds-toward:
- root-locus-pole-placement
- lead-lag-compensation-design
tags:
- performance
- time-domain
- specifications
- metrics
stage: advanced
status: draft
---

# Time-Domain Performance Metrics and Specifications

## Core Idea
Control system performance is specified by time-domain metrics: rise time (time to reach 90% of final value), settling time (time to stay within ±2% of final value), peak overshoot (maximum deviation above final value), and steady-state error. These metrics tie directly to pole locations: left-shift increases speed (reduces rise and settling time), increased damping reduces overshoot. Trade-offs exist between these metrics—decreasing overshoot typically increases rise time.

## Explainer

When you studied second-order systems, you learned that the step response is shaped by two parameters: **natural frequency** ωₙ (how fast the system would oscillate with zero damping) and **damping ratio** ζ (how quickly those oscillations decay). Time-domain performance specifications translate those abstract parameters into engineering requirements a customer can actually state: "the actuator must reach position within 50 ms" or "it must not overshoot by more than 5%." These four metrics — rise time, settling time, peak overshoot, and steady-state error — are the bridge between mathematical pole locations and physical design requirements.

**Peak overshoot** (%OS) is directly tied to ζ alone: %OS = exp(−πζ/√(1−ζ²)) × 100. For ζ = 0.7 (a common design target), overshoot is about 4.3%. For ζ = 0.5, it jumps to roughly 16%. The critical insight: overshoot depends only on damping ratio, not on how fast the system is. Two systems with the same ζ but different ωₙ will exhibit the same percentage overshoot — just at different time scales. **Settling time** (to within ±2%) approximates to 4/(ζωₙ) for underdamped systems — four time constants of the decaying exponential envelope. **Rise time** is roughly 1.8/ωₙ for lightly damped systems. Both rise time and settling time scale inversely with ωₙ: doubling the natural frequency halves both.

The s-plane interpretation makes these relationships visual. Poles have the form s = −ζωₙ ± jωₙ√(1−ζ²). Moving poles leftward (increasing |Re(s)| = ζωₙ) speeds up the transient response — shorter rise time and settling time. Moving poles further from the real axis (increasing |Im(s)|) increases the oscillation frequency and overshoot. A pole at s = −3 ± j4 decays with time constant 1/3 and oscillates at 4 rad/s. The same pole moved to s = −6 ± j4 decays twice as fast with the same oscillation — lower overshoot because ζ increased. Moving it to s = −3 ± j8 oscillates faster with much more overshoot. The tradeoff lives in the geometry of where poles sit.

The fundamental tension is this: you cannot simultaneously minimize all four metrics. Reducing overshoot means increasing ζ, which typically slows rise time. Speeding up rise time pushes poles leftward and upward, which may increase oscillations. **Steady-state error** is controlled independently by the number of integrators in the forward loop (system type) and is largely decoupled from transient behavior. These four metrics form the complete performance specification framework that all subsequent controller design — root locus, lead-lag compensation — uses as its target. In practice, before designing any controller, convert the written customer requirements into these four numbers; then use pole placement to meet them.
