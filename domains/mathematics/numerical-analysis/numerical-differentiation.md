---
id: numerical-differentiation
title: Numerical Differentiation
domain: mathematics
course: numerical-analysis
prerequisites:
- id: taylor-series
  type: hard
- id: rounding-errors
  type: hard
builds-toward:
- richardson-extrapolation
tags:
- differentiation
- finite-difference
- numerical
stage: abstract-reasoning
status: draft
---

# Numerical Differentiation

## Core Idea
Numerical differentiation approximates f'(x) using finite differences: forward (f(x+h)-f(x))/h, backward (f(x)-f(x-h))/h, or centered (f(x+h)-f(x-h))/(2h). Taylor analysis shows centered differences have O(h²) truncation error but are sensitive to rounding errors for very small h. Choosing h requires balancing truncation and rounding error—typically h ≈ √(machine epsilon).
