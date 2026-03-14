---
id: secant-method-root-finding
title: Secant Method
domain: mathematics
course: numerical-analysis
prerequisites:
- id: taylor-series
  type: soft
builds-toward:
- order-of-convergence
tags:
- secant-method
- root-finding
- derivative-free
stage: advanced
status: draft
---

# Secant Method

## Core Idea
The secant method approximates Newton's method by replacing the derivative with a finite difference quotient: x_{n+1} = x_n - f(x_n)(x_n - x_{n-1})/(f(x_n) - f(x_{n-1})). This avoids derivative computation but requires two initial points and achieves superlinear convergence (order ≈ 1.618), between linear and quadratic convergence.
