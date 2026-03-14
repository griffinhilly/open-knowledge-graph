---
id: poles-zeros-stability-analysis
title: Poles, Zeros, and System Stability
domain: engineering
course: control-systems
prerequisites:
- id: transfer-functions-control
  type: hard
- id: transfer-function-poles-zeros
  type: hard
builds-toward:
- characteristic-equation-and-stability
- root-locus-pole-placement
- frequency-stability-from-bode-and-nyquist
tags:
- poles
- zeros
- stability
- dynamics
stage: advanced
status: draft
---

# Poles, Zeros, and System Stability

## Core Idea
System poles in the s-plane directly determine stability: poles in the left half-plane produce bounded responses (stable), poles on the imaginary axis produce sustained oscillation (marginally stable), and poles in the right half-plane cause exponential divergence (unstable). Zeros affect the shape of transient response and can create undershoot or non-minimum-phase behavior. Pole-zero locations comprehensively characterize system dynamics without requiring time-domain solution.
