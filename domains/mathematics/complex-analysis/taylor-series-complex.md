---
id: taylor-series-complex
title: Taylor Series for Complex Functions
domain: mathematics
course: complex-analysis
prerequisites:
- id: cauchys-integral-formula-derivatives
  type: hard
- id: taylor-series
  type: hard
builds-toward:
- power-series-complex-plane
- laurent-series
tags:
- taylor-series
- power-series
- analytic
stage: abstract-reasoning
status: draft
---

# Taylor Series for Complex Functions

## Core Idea
Every holomorphic function f on a disk |z - z₀| < R is equal to its Taylor series f(z) = Σ f^(n)(z₀)/n! (z - z₀)^n, which converges for |z - z₀| < R. The radius of convergence R is the distance to the nearest singularity. This makes complex analytic functions completely rigid: the Taylor coefficients encode all information.

## How It's Best Learned
Compute the Taylor series of f(z) = 1/(1-z) around z = 0 and verify the radius of convergence is 1. Understand why: the function has a singularity at z = 1, which is distance 1 from the center.

## Common Misconceptions
Assuming every power series converges everywhere or nowhere; the radius of convergence is finite for holomorphic functions with singularities. Confusing the radius of convergence with the domain of the function.
