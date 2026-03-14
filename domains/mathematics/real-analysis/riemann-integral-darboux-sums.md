---
id: riemann-integral-darboux-sums
title: Riemann Integral via Darboux Sums
domain: mathematics
course: real-analysis
prerequisites:
- id: rigorous-derivative-definition
  type: hard
- id: supremum-and-infimum
  type: hard
builds-toward:
- riemann-integrability-criteria
- riemann-integral-properties
tags:
- riemann-integral
- darboux-sums
- integrability
stage: abstract-reasoning
status: draft
---

# Riemann Integral via Darboux Sums

## Core Idea
The Riemann integral is defined via Darboux sums: partition [a,b] into subintervals, compute upper (U) and lower (L) sums using suprema and infima of f on each subinterval. The integral exists if inf U = sup L. This definition is equivalent to Riemann sums and clarifies when functions are integrable: discontinuities on a set of measure zero are allowed.
