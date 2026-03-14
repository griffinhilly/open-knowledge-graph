---
id: interchange-limit-integral
title: Interchange of Limit and Integral
domain: mathematics
course: real-analysis
prerequisites:
- id: uniform-convergence
  type: hard
- id: riemann-integrability-criteria
  type: hard
tags:
- interchange
- limit
- integral
- convergence
stage: abstract-reasoning
status: draft
---

# Interchange of Limit and Integral

## Core Idea
If (fₙ) converges uniformly to f on [a, b], then lim_{n→∞} ∫_a^b fₙ = ∫_a^b f. That is, ∫_a^b (lim fₙ) = lim (∫_a^b fₙ). This is one of the most useful theorems in analysis, allowing integration of limit functions. Pointwise convergence is not sufficient; uniform convergence is required.
