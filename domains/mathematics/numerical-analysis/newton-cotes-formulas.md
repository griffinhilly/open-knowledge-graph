---
id: newton-cotes-formulas
title: Newton-Cotes Quadrature Formulas
domain: mathematics
course: numerical-analysis
prerequisites:
- id: taylor-series
  type: hard
- id: lagrange-polynomial-interpolation
  type: hard
builds-toward:
- composite-quadrature
- gaussian-quadrature
tags:
- quadrature
- newton-cotes
- integration
stage: abstract-reasoning
status: draft
---

# Newton-Cotes Quadrature Formulas

## Core Idea
Newton-Cotes formulas approximate ∫f(x)dx using weighted sums of f evaluated at equally-spaced points. Examples include the trapezoidal rule (2-point, O(h³) error) and Simpson's rule (3-point, O(h⁵) error), derived by integrating the Lagrange polynomial through sample points. Open formulas omit endpoints and are useful when f is singular or undefined at boundaries.
