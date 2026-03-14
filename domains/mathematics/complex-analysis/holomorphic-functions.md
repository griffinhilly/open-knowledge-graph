---
id: holomorphic-functions
title: Holomorphic Functions
domain: mathematics
course: complex-analysis
prerequisites:
- id: complex-differentiability
  type: hard
builds-toward:
- cauchy-riemann-equations
- complex-line-integrals
- taylor-series-complex
tags:
- holomorphic
- analytic
- differentiable
stage: abstract-reasoning
status: draft
---

# Holomorphic Functions

## Core Idea
A function f is holomorphic (analytic) on a domain D if it is differentiable at every point in D. Holomorphic functions are infinitely differentiable and equal their Taylor series. They are the central objects of complex analysis because they satisfy rigid properties: their real and imaginary parts satisfy the Cauchy-Riemann equations, they satisfy integral theorems, and isolated zeros force local injectivity.

## How It's Best Learned
Study the function f(z) = e^z and verify it is holomorphic everywhere; compute its derivatives and Taylor series. Compare to a merely continuous function like f(z) = |z| to see the difference in rigidity.

## Common Misconceptions
Thinking holomorphic functions form a large class; they are extremely special and rigid. Assuming holomorphic functions are only polynomials and exponentials; there are many more (trig, logarithm, etc.).
