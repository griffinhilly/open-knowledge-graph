---
id: rise-time-settling-time-overshoot
title: Rise Time, Settling Time, and Overshoot Specifications
domain: engineering
course: control-systems
prerequisites:
- id: second-order-system-response-analysis
  type: hard
builds-toward:
- control-loop-design-via-bode-plots
tags:
- performance-specs
- time-domain
- transient-metrics
- design-constraints
stage: expert
status: draft
---

# Rise Time, Settling Time, and Overshoot Specifications

## Core Idea
Rise time, settling time, and overshoot are time-domain performance metrics. Rise time measures how fast the output reaches the desired value; settling time measures how long transients persist; overshoot measures how much the response exceeds its target. Trade-offs exist: reducing overshoot slows response.

## Questions

```yaml
- question: "A control engineer needs to reduce percent overshoot from 25% to 5% without significantly slowing the rise time. Which parameter adjustment achieves this?"
  type: multiple-choice
  options:
    - "Increase ωn while holding ζ constant — higher natural frequency reduces overshoot"
    - "Increase ζ while holding ωn approximately constant — damping ratio is the primary handle for overshoot"
    - "Decrease both ζ and ωn proportionally — the ratio determines overshoot"
    - "Decrease ωn while holding ζ constant — lower natural frequency reduces oscillations"
  answer: 1
  explanation: "Percent overshoot is determined solely by ζ via %OS = 100·exp(−πζ/√(1−ζ²)). Changing ωn does not affect overshoot at all. To go from 25% overshoot (ζ ≈ 0.4) to 5% overshoot (ζ ≈ 0.69), increase ζ. Rise time is primarily controlled by ωn, so if ωn is held roughly constant, rise time is preserved. The independence of these two parameters is the key design insight."

- question: "For a second-order underdamped system, what is the percent overshoot when the damping ratio ζ = 0.707?"
  type: multiple-choice
  options:
    - "Exactly 0% — ζ = 0.707 is the critically damped condition with no overshoot"
    - "Approximately 4.3% — ζ = 0.707 gives modest overshoot with fast response, a common design target"
    - "Approximately 16.3% — ζ = 0.707 is the half-damping threshold"
    - "Approximately 50% — ζ = 0.707 corresponds to low damping and large overshoot"
  answer: 1
  explanation: "Using %OS = 100·exp(−πζ/√(1−ζ²)) with ζ = 0.707: exp(−π·0.707/√(1−0.5)) = exp(−π·0.707/0.707) = exp(−π) ≈ exp(−3.14) ≈ 4.3%. This is why ζ = 0.707 (often called the 'Butterworth damping') is a common design target — it gives fast response with barely perceptible overshoot. Critical damping (zero overshoot) requires ζ = 1, which is noticeably slower."

- question: "For an underdamped second-order system, increasing ωn while holding ζ constant will reduce rise time without changing percent overshoot."
  type: true-false
  answer: true
  explanation: "Percent overshoot depends only on ζ (via the formula %OS = 100·exp(−πζ/√(1−ζ²))), so changing ωn while holding ζ constant does not affect overshoot at all. Rise time tr ≈ (π − arccos ζ)/(ωn·√(1−ζ²)) is inversely proportional to ωn — doubling ωn halves the rise time. This approximate independence of the two parameters (overshoot controlled by ζ, speed controlled by ωn) is the core insight for second-order system design."

- question: "A critically damped system (ζ = 1) responds more slowly than an overdamped system (ζ > 1) because higher damping always slows the response."
  type: true-false
  answer: false
  explanation: "Counterintuitively, critical damping (ζ = 1) is actually the fastest non-overshooting response — it is faster than any overdamped system (ζ > 1). An overdamped system has two distinct real poles; as ζ increases beyond 1, one pole moves very close to the origin, creating a slow mode that drags out the response. Critical damping balances the two poles at the same location, giving the fastest approach to steady state without overshoot. This is why 'critically damped' is the design target when overshoot is forbidden."

- question: "A specification requires rise time under 50 ms and overshoot under 5%. Explain how you translate these requirements into constraints on the second-order system parameters ζ and ωn."
  type: short-answer
  answer: "The overshoot constraint maps to a minimum ζ. Using %OS = 100·exp(−πζ/√(1−ζ²)) ≤ 5%, solving for ζ gives ζ ≥ approximately 0.69. The rise time constraint maps to a minimum ωn. Using tr ≈ (π − arccos ζ)/(ωn·√(1−ζ²)) ≤ 0.05 s, with ζ at its minimum value of 0.69, you can solve for the required ωn. The two constraints together define a region in (ζ, ωn) parameter space: the system's closed-loop poles must satisfy both bounds simultaneously."
  explanation: "The key is recognizing that the two specifications target different parameters: overshoot → minimum ζ, rise time → minimum ωn. Because these parameters are approximately independent (ωn sets speed; ζ sets oscillation level), you can design them separately. Find the minimum ζ from the overshoot bound, then find the minimum ωn from the rise time bound at that ζ. Any (ζ, ωn) pair satisfying both constraints is an acceptable design."
```

## Explainer

From your analysis of second-order systems, you know that the step response of a standard second-order system is governed by two parameters: the **natural frequency** ωn (which sets the overall speed) and the **damping ratio** ζ (which controls how oscillatory the response is). Rise time, settling time, and percent overshoot are essentially three different ways of reading the same underlying response — each capturing a different aspect of quality that matters in practice.

**Rise time** tr measures how quickly the output first reaches the target. The standard definition is the time to go from 10% to 90% of the final value (avoiding the slow initial transient). For an underdamped second-order system, tr ≈ (π − arccos ζ)/(ωn·√(1−ζ²)). The key insight: rise time is primarily controlled by ωn. A higher natural frequency → faster rise. Increasing ζ slightly slows the rise (the arccos term grows), but the dominant handle is ωn. Think of it as: ωn determines the system's "gear ratio," and ζ determines how smoothly it shifts.

**Percent overshoot** (%OS) is determined entirely by ζ: %OS = 100·exp(−πζ/√(1−ζ²)). At ζ = 1 (critically damped), overshoot is exactly 0. At ζ = 0.707, overshoot is about 4.3%. At ζ = 0.5, it reaches 16.3%. At ζ = 0.2, it exceeds 50%. The formula shows overshoot is a function of ζ alone — changing ωn does not affect it. This means you can choose ζ to meet an overshoot specification, then choose ωn independently to meet a speed specification. The two parameters are (approximately) independent handles on two different aspects of transient response.

**Settling time** ts measures how long the response takes to stay within a tolerance band (usually 2% or 5%) of the final value. The 2% criterion gives ts ≈ 4/(ζ·ωn). This depends on both parameters: increasing ζ reduces settling time (less ringing), and increasing ωn also reduces settling time (faster decay). Note the interaction: if you increase ωn to speed up the rise time but hold ζ fixed, settling time also improves. If you increase ζ to reduce overshoot while holding ωn fixed, settling time also improves. This makes settling time a less independent specification than rise time and overshoot — it tends to be satisfied once the other two are met, unless the system has a near-unstable behavior.

The practical tradeoff is between **speed and smoothness**. A low-ζ system rises quickly but oscillates; a high-ζ system settles cleanly but responds sluggishly. Most engineering specifications express this as a requirement: "rise time under X ms and overshoot under Y%." You translate this directly: the overshoot bound maps to a minimum ζ, and the rise time bound maps to a minimum ωn. The region of acceptable (ζ, ωn) pairs defines your design space — your job as a control engineer is to find a compensator that places the closed-loop poles inside that region.
