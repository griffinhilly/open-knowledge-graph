---
id: frobenius-method
title: The Frobenius Method for Singular Points
domain: mathematics
course: differential-equations
prerequisites:
- id: ordinary-and-singular-points
  type: hard
- id: power-series-solutions-to-odes
  type: hard
builds-toward:
- bessel-functions
- legendre-polynomials-and-equations
tags:
- series
- singular-point
- method
stage: advanced
status: draft
---

# The Frobenius Method for Singular Points

## Core Idea
At a regular singular point x₀, the Frobenius method assumes y = (x - x₀)^r·Σ(a_n·(x - x₀)^n). Substituting yields an indicial equation determining r and a recurrence for a_n. This method generalizes power series solutions to include logarithmic terms when needed.

## How It's Best Learned
Apply the method to Bessel's equation y'' + (1/x)y' + (1 - n²/x²)y = 0, deriving the indicial equation r² - n² = 0 and recurrence relations for Bessel function coefficients.
