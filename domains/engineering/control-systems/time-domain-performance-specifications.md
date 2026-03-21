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

## Questions

```yaml
- question: "Two second-order systems A and B both have damping ratio ζ = 0.5, but system A has ωₙ = 10 rad/s while system B has ωₙ = 20 rad/s. How do their step responses compare?"
  type: multiple-choice
  options:
    - "System B has lower percentage overshoot because it responds faster"
    - "System A has lower percentage overshoot because it responds more slowly and has more time to damp"
    - "Both systems have the same percentage overshoot, but system B settles in approximately half the time"
    - "The responses are identical since both systems have the same damping ratio and natural frequency determines only the amplitude"
  answer: 2
  explanation: "Percentage overshoot depends only on ζ — the formula %OS = exp(−πζ/√(1−ζ²)) × 100 contains no ωₙ term. With identical ζ = 0.5, both systems have the same overshoot (~16%). But settling time ≈ 4/(ζωₙ): system A settles in 4/(0.5×10) = 0.8 s while system B settles in 4/(0.5×20) = 0.4 s — half the time. Overshoot and response speed are controlled by different parameters and can be adjusted independently (within limits)."

- question: "A control engineer must design a system with both fast rise time and very low overshoot. The current design has unacceptably high overshoot. Increasing the damping ratio ζ will:"
  type: multiple-choice
  options:
    - "Reduce overshoot and also reduce rise time, improving both specifications simultaneously"
    - "Reduce overshoot but tend to increase rise time, creating a fundamental design tradeoff"
    - "Have no effect on rise time since rise time depends only on ωₙ"
    - "Reduce overshoot only at the cost of permanently increased steady-state error"
  answer: 1
  explanation: "Increasing ζ reduces overshoot directly (the %OS formula decreases with increasing ζ). However, higher ζ moves poles toward the real axis — reducing the imaginary component — which slows the oscillatory response and increases rise time. To satisfy both a fast rise time AND low overshoot, the engineer must also increase ωₙ (moving poles further left), not just increase ζ alone. This is the central design tension in second-order system specification."

- question: "Doubling the natural frequency ωₙ of a second-order system while keeping ζ constant will approximately double the percentage overshoot."
  type: true-false
  answer: false
  explanation: "Percentage overshoot depends only on ζ, not on ωₙ. The formula %OS = exp(−πζ/√(1−ζ²)) × 100 has no ωₙ term. Doubling ωₙ makes the system respond twice as fast (halves rise time and settling time) but leaves overshoot completely unchanged. A common misconception is that faster systems overshoot more — speed and overshoot are controlled by independent parameters."

- question: "Moving a closed-loop pole further to the left in the s-plane (increasing the magnitude of its real part) reduces both rise time and settling time."
  type: true-false
  answer: true
  explanation: "The real part of the pole is −ζωₙ. Moving poles leftward increases |Re(s)| = ζωₙ, which decreases the time constant τ = 1/(ζωₙ) of the decaying envelope. Settling time ≈ 4τ = 4/(ζωₙ) decreases, and rise time ≈ 1.8/ωₙ also decreases with higher ωₙ. Poles on the far left of the s-plane correspond to rapidly decaying, fast-response systems."

- question: "A control system has too much overshoot (30%) and too slow a rise time. An engineer proposes increasing ζ to fix the overshoot. What trade-off will they encounter, and what additional design change could address both specifications simultaneously?"
  type: short-answer
  answer: "Increasing ζ reduces overshoot (since %OS decreases as ζ rises) but also slows rise time because poles move toward the real axis, reducing the oscillatory speed. To satisfy both a lower overshoot and a faster rise time, the engineer must also increase ωₙ — moving the poles both further left (faster) and at a steeper angle (higher ζ, less overshoot). In the s-plane, the target is a pole location with larger |Re(s)| and a steeper angle from the negative real axis, corresponding to simultaneously higher ωₙ and higher ζ."
  explanation: "This is why controller design begins with converting performance specs into desired pole locations in the s-plane. A 5% overshoot requirement maps to ζ ≈ 0.69; a 50 ms settling time maps to ζωₙ ≥ 4/0.05 = 80. These two requirements together specify a region in the s-plane (left of −80, at an angle corresponding to ζ = 0.69) where the poles must lie. Root locus and lead-lag design are then tools for placing poles in this target region."
```

## Explainer

When you studied second-order systems, you learned that the step response is shaped by two parameters: **natural frequency** ωₙ (how fast the system would oscillate with zero damping) and **damping ratio** ζ (how quickly those oscillations decay). Time-domain performance specifications translate those abstract parameters into engineering requirements a customer can actually state: "the actuator must reach position within 50 ms" or "it must not overshoot by more than 5%." These four metrics — rise time, settling time, peak overshoot, and steady-state error — are the bridge between mathematical pole locations and physical design requirements.

**Peak overshoot** (%OS) is directly tied to ζ alone: %OS = exp(−πζ/√(1−ζ²)) × 100. For ζ = 0.7 (a common design target), overshoot is about 4.3%. For ζ = 0.5, it jumps to roughly 16%. The critical insight: overshoot depends only on damping ratio, not on how fast the system is. Two systems with the same ζ but different ωₙ will exhibit the same percentage overshoot — just at different time scales. **Settling time** (to within ±2%) approximates to 4/(ζωₙ) for underdamped systems — four time constants of the decaying exponential envelope. **Rise time** is roughly 1.8/ωₙ for lightly damped systems. Both rise time and settling time scale inversely with ωₙ: doubling the natural frequency halves both.

The s-plane interpretation makes these relationships visual. Poles have the form s = −ζωₙ ± jωₙ√(1−ζ²). Moving poles leftward (increasing |Re(s)| = ζωₙ) speeds up the transient response — shorter rise time and settling time. Moving poles further from the real axis (increasing |Im(s)|) increases the oscillation frequency and overshoot. A pole at s = −3 ± j4 decays with time constant 1/3 and oscillates at 4 rad/s. The same pole moved to s = −6 ± j4 decays twice as fast with the same oscillation — lower overshoot because ζ increased. Moving it to s = −3 ± j8 oscillates faster with much more overshoot. The tradeoff lives in the geometry of where poles sit.

The fundamental tension is this: you cannot simultaneously minimize all four metrics. Reducing overshoot means increasing ζ, which typically slows rise time. Speeding up rise time pushes poles leftward and upward, which may increase oscillations. **Steady-state error** is controlled independently by the number of integrators in the forward loop (system type) and is largely decoupled from transient behavior. These four metrics form the complete performance specification framework that all subsequent controller design — root locus, lead-lag compensation — uses as its target. In practice, before designing any controller, convert the written customer requirements into these four numbers; then use pole placement to meet them.
