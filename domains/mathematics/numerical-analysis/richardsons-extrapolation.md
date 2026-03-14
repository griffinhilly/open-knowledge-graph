---
id: richardsons-extrapolation
title: Richardson's Extrapolation
domain: mathematics
course: numerical-analysis
prerequisites:
- id: taylor-series
  type: hard
builds-toward:
- romberg-integration
tags:
- richardson-extrapolation
- acceleration
- deferred-correction
stage: advanced
status: draft
---

# Richardson's Extrapolation

## Core Idea
Richardson's extrapolation accelerates convergence by combining approximations at different step sizes to cancel leading error terms. If an approximation has error A(h) = a₀ + a₁h^p + a₂h^{2p} + ..., linear combinations of A(h) and A(h/2) eliminate the a₁h^p term, increasing convergence order. This technique amplifies accuracy without more function evaluations.
