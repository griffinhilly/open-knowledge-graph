---
id: power-series-solutions
title: Power Series Solutions to Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: power-series
  type: hard
- id: taylor-series
  type: hard
- id: higher-order-linear-odes
  type: hard
builds-toward:
- frobenius-method
tags:
- power-series
- analytic-solutions
- series-method
stage: formal-systems
status: draft
---

# Power Series Solutions to Differential Equations

## Core Idea
When an ODE cannot be solved by standard methods, assume a power series solution y = Σ aₙx^n, substitute into the equation, and match coefficients to find aₙ. This approach works when the equation has an analytic solution around a point. Recurrence relations for the coefficients determine the solution, usually yielding two linearly independent series from different initial conditions.
