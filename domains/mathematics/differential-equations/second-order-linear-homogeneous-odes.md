---
id: second-order-linear-homogeneous-odes
title: Second-Order Linear Homogeneous Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: first-order-linear-odes
  type: hard
- id: linear-independence
  type: hard
builds-toward:
- characteristic-equation-method
- wronskian-linear-independence
- undetermined-coefficients
tags:
- second-order
- linear
- homogeneous
stage: advanced
status: draft
---

# Second-Order Linear Homogeneous Differential Equations

## Core Idea
A second-order linear homogeneous ODE has the form y'' + p(x)y' + q(x)y = 0, where the right side is zero. If y₁ and y₂ are linearly independent solutions, the general solution is y = c₁y₁ + c₂y₂, following the superposition principle unique to linear equations.

## How It's Best Learned
Learn the general solution structure first, then master the characteristic equation method for constant coefficients. Verify linear independence using the Wronskian.

## Common Misconceptions
- Thinking the two solutions must have different functional forms; e^{rx} and xe^{rx} are both valid even though they have the same base form. - Confusing linearly independent solutions with distinct solutions. - Not recognizing that the superposition principle applies only to homogeneous equations.
