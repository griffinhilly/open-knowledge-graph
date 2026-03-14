---
id: convergence-fourier-series
title: Convergence of Fourier Series
domain: mathematics
course: differential-equations
prerequisites:
- id: fourier-series-definition
  type: hard
- id: sequences-convergence
  type: hard
builds-toward:
- even-odd-extensions-fourier
tags:
- convergence
- dirichlet-conditions
- pointwise
stage: advanced
status: draft
---

# Convergence of Fourier Series

## Core Idea
If f is piecewise smooth and periodic, its Fourier series converges pointwise to f at continuity points and to the average of left and right limits at jump discontinuities. The Dirichlet conditions (finitely many jumps and extrema per period) guarantee this convergence. The Gibbs phenomenon causes overshoot at discontinuities, a key practical consideration.
