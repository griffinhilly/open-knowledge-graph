---
id: natural-frequency-damping-second-order
title: Natural Frequency and Damping Ratio
domain: engineering
course: control-systems
prerequisites:
- id: characteristic-equation-and-stability
  type: hard
- id: second-order-system-response-analysis
  type: hard
builds-toward:
- time-domain-performance-specifications
- root-locus-pole-placement
tags:
- natural-frequency
- damping
- second-order
- parameters
stage: advanced
status: draft
---

# Natural Frequency and Damping Ratio

## Core Idea
A second-order system is completely characterized by natural frequency ωₙ (undamped oscillation rate) and damping ratio ζ (energy dissipation). Standard form H(s) = ωₙ²/(s² + 2ζωₙs + ωₙ²) yields poles at -ζωₙ ± jωₙ√(1-ζ²). These parameters directly relate to time-domain metrics: overshoot depends on ζ, rise time on ωₙ, and settling time on ζωₙ.
