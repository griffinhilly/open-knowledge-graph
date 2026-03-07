---
id: definite-integral-definition
title: Definite Integral Definition
domain: mathematics
course: calculus-1
prerequisites:
  - id: riemann-sums
    type: hard
  - id: limit-definition-intuitive
    type: hard
builds-toward:
  - fundamental-theorem-of-calculus-part-1
  - fundamental-theorem-of-calculus-part-2
tags: [integration, definite-integral, area]
stage: formal-systems
status: draft
---

# Definite Integral Definition

## Core Idea
The definite integral of f from a to b, written as the integral from a to b of f(x) dx, is defined as the limit of Riemann sums as the number of subintervals approaches infinity. When f(x) >= 0, the definite integral equals the area under the curve. When f takes negative values, it computes signed area (negative below the x-axis). The definite integral is a number, not a function, and it has properties: linearity, additivity over intervals, and comparison properties.

## How It's Best Learned
Connect to Riemann sums by computing limits of sums for simple functions (polynomials). State and apply properties of definite integrals. Emphasize that the definite integral is defined independently of antiderivatives (the FTC connects them, but they are conceptually separate).

## Common Misconceptions
- Believing the definite integral always represents area (it represents signed area; area requires taking absolute values).
- Confusing definite integrals (numbers with bounds) and indefinite integrals (functions with +C).
- Forgetting that the integral from a to a of f(x) dx = 0 and the integral from b to a equals the negative of the integral from a to b.
