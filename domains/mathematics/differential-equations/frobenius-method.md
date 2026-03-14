---
id: frobenius-method
title: Frobenius Method and Equations with Singular Points
domain: mathematics
course: differential-equations
prerequisites:
- id: power-series-solutions
  type: hard
- id: continuity-definition
  type: soft
builds-toward:
- bessel-functions
- legendre-equations
tags:
- frobenius-method
- singular-points
- series-solution
stage: advanced
status: draft
---

# Frobenius Method and Equations with Singular Points

## Core Idea
For regular singular points where (x-x₀)p and (x-x₀)²q are analytic in y'' + p(x)y' + q(x)y = 0, the Frobenius method seeks y = (x-x₀)^r Σ aₙ(x-x₀)^n. Substituting yields an indicial equation for r and a recurrence relation for coefficients. Two independent solutions typically arise from different indicial roots. This method extends power series to a broader class of important equations.
