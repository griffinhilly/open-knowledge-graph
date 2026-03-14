---
id: secant-method
title: Secant Method
domain: mathematics
course: numerical-analysis
prerequisites:
- id: newton-method-convergence
  type: hard
builds-toward:
- order-of-convergence
tags:
- secant-method
- root-finding
- finite-difference
stage: abstract-reasoning
status: draft
---

# Secant Method

## Core Idea
The secant method approximates Newton's method by replacing f'(x_n) with a finite difference: x_{n+1} = x_n - f(x_n)[x_n - x_{n-1}]/[f(x_n) - f(x_{n-1})]. It avoids computing derivatives, requiring only function values at two initial points. The secant method converges superlinearly (faster than linear, slower than quadratic) with order ≈ 1.618.
