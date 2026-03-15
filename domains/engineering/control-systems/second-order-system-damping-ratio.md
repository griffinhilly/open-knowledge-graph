---
id: second-order-system-damping-ratio
title: 'Second-Order System Response: Damping Ratio and Natural Frequency'
domain: engineering
course: control-systems
prerequisites:
- id: first-order-system-transient-response
  type: hard
- id: second-order-systems-resonance
  type: soft
builds-toward:
- compensation-design-tradeoffs-cascadefeedback
tags:
- second-order
- damping-ratio
- natural-frequency
- underdamped
- overdamped
stage: formal-systems
status: draft
---

# Second-Order System Response: Damping Ratio and Natural Frequency

## Core Idea
Second-order systems are characterized by natural frequency ωₙ and damping ratio ζ. Overdamped (ζ>1): slow, no overshoot; critically damped (ζ=1): fastest without overshoot; underdamped (ζ<1): fast but with overshoot and oscillation. Overshoot M_p ≈ e^(-πζ/√(1-ζ²)); settling time T_s ≈ 4/(ζωₙ).
