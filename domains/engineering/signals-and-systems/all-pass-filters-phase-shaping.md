---
id: all-pass-filters-phase-shaping
title: All-Pass Filters for Phase Shaping
domain: engineering
course: signals-and-systems
prerequisites:
- id: group-delay-phase-characterization
  type: hard
- id: transfer-function-poles-zeros
  type: hard
builds-toward:
- minimum-phase-systems-analysis
tags:
- all-pass-filters
- phase-shaping
- transfer-function
stage: advanced
status: draft
---

# All-Pass Filters for Phase Shaping

## Core Idea
All-pass filters have unity magnitude |H(ω)| = 1 but nonlinear phase response. Poles and zeros are reciprocal (z_k = 1/p_k* for stable filters), canceling magnitude while enabling phase adjustment. All-pass filters compensate for phase distortion and are essential in designing minimum-phase systems with prescribed magnitude response.
