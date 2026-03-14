---
id: separable-differential-equations
title: Separable Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: differential-equations-intro
  type: hard
- id: u-substitution
  type: hard
builds-toward:
- first-order-linear-odes
- exact-differential-equations
- autonomous-equations
tags:
- first-order
- method
- integration
stage: advanced
status: draft
---

# Separable Differential Equations

## Core Idea
A separable differential equation can be written as dy/dx = f(x)g(y), where the variables can be separated onto different sides: dy/g(y) = f(x)dx. The solution is found by integrating both sides independently, making this one of the most straightforward methods for solving ODEs.

## How It's Best Learned
Practice identifying when an equation is separable versus when it isn't. Work through examples where implicit solutions are obtained, then verify solutions by implicit differentiation.

## Common Misconceptions
- Forgetting the constant of integration on one side (it should appear on one side only, absorbed into a single ±C). - Not recognizing when equations can be rearranged into separable form. - Confusing separable equations with linear equations.
