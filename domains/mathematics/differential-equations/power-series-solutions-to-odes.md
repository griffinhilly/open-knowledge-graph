---
id: power-series-solutions-to-odes
title: Power Series Solutions to Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: power-series
  type: hard
- id: second-order-linear-homogeneous-odes
  type: hard
builds-toward:
- ordinary-and-singular-points
- frobenius-method
tags:
- series
- method
- special-functions
stage: advanced
status: draft
---

# Power Series Solutions to Differential Equations

## Core Idea
For ODEs that don't have elementary closed-form solutions, assume a power series solution y = Σ(a_n·x^n) and substitute into the ODE to find a recurrence relation for coefficients a_n. This yields convergent power series solutions valid near x = 0.

## How It's Best Learned
Work through Airy's equation or Bessel's equation. Substitute y = Σ(a_n·x^n) and y' = Σ(n·a_n·x^{n-1}), then collect powers of x and equate coefficients to zero.

## Common Misconceptions
- Confusing power series solutions with Taylor series approximations; they are exact within their radius of convergence. - Not recognizing the radius of convergence limitations. - Making algebra errors when equating coefficients of like powers.
