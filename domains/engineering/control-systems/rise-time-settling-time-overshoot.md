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
stage: advanced
status: draft
---

# Rise Time, Settling Time, and Overshoot Specifications

## Core Idea
Rise time, settling time, and overshoot are time-domain performance metrics. Rise time measures how fast the output reaches the desired value; settling time measures how long transients persist; overshoot measures how much the response exceeds its target. Trade-offs exist: reducing overshoot slows response.

## Explainer

From your analysis of second-order systems, you know that the step response of a standard second-order system is governed by two parameters: the **natural frequency** ωn (which sets the overall speed) and the **damping ratio** ζ (which controls how oscillatory the response is). Rise time, settling time, and percent overshoot are essentially three different ways of reading the same underlying response — each capturing a different aspect of quality that matters in practice.

**Rise time** tr measures how quickly the output first reaches the target. The standard definition is the time to go from 10% to 90% of the final value (avoiding the slow initial transient). For an underdamped second-order system, tr ≈ (π − arccos ζ)/(ωn·√(1−ζ²)). The key insight: rise time is primarily controlled by ωn. A higher natural frequency → faster rise. Increasing ζ slightly slows the rise (the arccos term grows), but the dominant handle is ωn. Think of it as: ωn determines the system's "gear ratio," and ζ determines how smoothly it shifts.

**Percent overshoot** (%OS) is determined entirely by ζ: %OS = 100·exp(−πζ/√(1−ζ²)). At ζ = 1 (critically damped), overshoot is exactly 0. At ζ = 0.707, overshoot is about 4.3%. At ζ = 0.5, it reaches 16.3%. At ζ = 0.2, it exceeds 50%. The formula shows overshoot is a function of ζ alone — changing ωn does not affect it. This means you can choose ζ to meet an overshoot specification, then choose ωn independently to meet a speed specification. The two parameters are (approximately) independent handles on two different aspects of transient response.

**Settling time** ts measures how long the response takes to stay within a tolerance band (usually 2% or 5%) of the final value. The 2% criterion gives ts ≈ 4/(ζ·ωn). This depends on both parameters: increasing ζ reduces settling time (less ringing), and increasing ωn also reduces settling time (faster decay). Note the interaction: if you increase ωn to speed up the rise time but hold ζ fixed, settling time also improves. If you increase ζ to reduce overshoot while holding ωn fixed, settling time also improves. This makes settling time a less independent specification than rise time and overshoot — it tends to be satisfied once the other two are met, unless the system has a near-unstable behavior.

The practical tradeoff is between **speed and smoothness**. A low-ζ system rises quickly but oscillates; a high-ζ system settles cleanly but responds sluggishly. Most engineering specifications express this as a requirement: "rise time under X ms and overshoot under Y%." You translate this directly: the overshoot bound maps to a minimum ζ, and the rise time bound maps to a minimum ωn. The region of acceptable (ζ, ωn) pairs defines your design space — your job as a control engineer is to find a compensator that places the closed-loop poles inside that region.
