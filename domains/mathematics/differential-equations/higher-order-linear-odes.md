---
id: higher-order-linear-odes
title: Higher-Order Linear Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: variation-of-parameters
  type: hard
- id: characteristic-equation-method
  type: hard
builds-toward:
- systems-of-first-order-linear-odes
- power-series-solutions-to-odes
tags:
- higher-order
- linear
- general-theory
stage: advanced
status: draft
---

# Higher-Order Linear Differential Equations

## Core Idea
An nth-order linear ODE a_n(x)y^{(n)} + ... + a₁(x)y' + a₀(x)y = g(x) is solved by finding n linearly independent solutions to the homogeneous equation and adding a particular solution. The characteristic equation method extends directly: for constant coefficients, solve r^n + ... + a₁r + a₀ = 0.
