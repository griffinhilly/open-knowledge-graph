---
id: integrating-factor-method
title: Integrating Factor Method for First-Order Linear ODEs
domain: mathematics
course: differential-equations
prerequisites:
- id: separable-differential-equations
  type: hard
- id: partial-derivatives
  type: soft
builds-toward:
- exact-differential-equations
- first-order-linear-odes
tags:
- integrating-factor
- first-order
- linear
stage: formal-systems
status: draft
---

# Integrating Factor Method for First-Order Linear ODEs

## Core Idea
For a first-order linear ODE of the form dy/dx + P(x)y = Q(x), an integrating factor μ(x) = e^(∫P(x)dx) transforms the left side into the derivative of a product: d/dx[μ(x)y] = μ(x)Q(x). This makes the equation directly integrable, converting a challenging linear equation into a solvable form. The integrating factor is one of the most powerful techniques in differential equations.
