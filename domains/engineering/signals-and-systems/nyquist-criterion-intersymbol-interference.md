---
id: nyquist-criterion-intersymbol-interference
title: Nyquist Criterion for Zero Intersymbol Interference
domain: engineering
course: signals-and-systems
prerequisites:
- id: sampling-theorem-nyquist-rate
  type: hard
- id: matched-filter-signal-detection
  type: soft
builds-toward:
- raised-cosine-pulse-shaping
tags:
- nyquist-criterion
- isi
- pulse-shaping
- communication
stage: advanced
status: draft
---

# Nyquist Criterion for Zero Intersymbol Interference

## Core Idea
The Nyquist criterion specifies conditions on pulse response p(t) for zero intersymbol interference (ISI) at sampling times: p(nTs) = 1 for n=0 and p(nTs) = 0 for n≠0. In frequency domain: Σ P(f + k/Ts) = Ts. This ensures adjacent symbols do not interfere, enabling reliable symbol recovery from noisy channels.
