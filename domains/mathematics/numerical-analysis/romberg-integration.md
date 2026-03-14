---
id: romberg-integration
title: Romberg Integration
domain: mathematics
course: numerical-analysis
prerequisites:
- id: richardson-extrapolation
  type: hard
- id: composite-quadrature
  type: hard
tags:
- romberg
- integration
- extrapolation
stage: abstract-reasoning
status: draft
---

# Romberg Integration

## Core Idea
Romberg integration systematically applies composite trapezoidal rules with successive halvings of step size, then uses Richardson extrapolation to accelerate convergence. The method builds a triangular array where each new entry combines results from halved step size with previous entries to cancel error terms. Romberg achieves high accuracy efficiently and provides adaptive error estimation.
