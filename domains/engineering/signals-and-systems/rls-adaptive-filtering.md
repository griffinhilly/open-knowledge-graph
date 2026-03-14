---
id: rls-adaptive-filtering
title: Recursive Least-Squares Adaptive Filtering
domain: engineering
course: signals-and-systems
prerequisites:
- id: adaptive-filtering-lms
  type: hard
tags:
- adaptive-filters
- rls
- least-squares
- convergence
stage: advanced
status: draft
---

# Recursive Least-Squares Adaptive Filtering

## Core Idea
Recursive Least-Squares (RLS) adapts filter coefficients to minimize weighted sum of squared errors using matrix inversion lemma for efficient recursive updates. Convergence is typically faster than LMS and can track time-varying systems with exponential weighting. The O(N²) complexity per update is higher than LMS but suitable for ill-conditioned channels.
