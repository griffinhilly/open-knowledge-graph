---
id: riemann-integral-darboux-sums
title: Riemann Integral via Darboux Sums
domain: mathematics
course: real-analysis
prerequisites:
- id: riemann-sums
  type: hard
- id: epsilon-delta-continuity
  type: soft
builds-toward:
- riemann-integrability-criteria
- properties-riemann-integral
tags:
- riemann-integral
- darboux-sums
- integrability
stage: abstract-reasoning
status: draft
---

# Riemann Integral via Darboux Sums

## Core Idea
For a bounded function f on [a, b], the upper Darboux sum U(P) sums the maximum values on each subinterval, and the lower Darboux sum L(P) sums the minimum values. If sup L(P) = inf U(P) over all partitions P, this common value is the Riemann integral. The Darboux approach is equivalent to Riemann's definition and often easier to work with rigorously.
