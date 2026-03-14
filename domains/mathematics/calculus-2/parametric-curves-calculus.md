---
id: parametric-curves-calculus
title: Calculus of Parametric Curves
domain: mathematics
course: calculus-2
prerequisites:
  - id: parametric-equations-intro
    type: hard
  - id: chain-rule
    type: hard
builds-toward:
  - arc-length-parametric
tags: [parametric, derivatives, calculus]
stage: formal-systems
status: validated
---

# Calculus of Parametric Curves

## Core Idea
For parametric curves x = f(t), y = g(t), the slope of the tangent line is dy/dx = (dy/dt)/(dx/dt), applying the chain rule. The second derivative d^2y/dx^2 = (d/dt[dy/dx])/(dx/dt). These formulas let you find tangent lines, identify horizontal and vertical tangents, determine concavity, and locate extrema for parametrically defined curves without eliminating the parameter.

## How It's Best Learned
Derive dy/dx from the chain rule. Practice finding tangent lines to parametric curves (e.g., the cycloid). Identify horizontal tangents (dy/dt = 0) and vertical tangents (dx/dt = 0). Compute the second derivative for concavity analysis.

## Common Misconceptions
- Computing dy/dx as g(t)/f(t) instead of g'(t)/f'(t).
- Confusing horizontal tangent (dy/dt = 0) with vertical tangent (dx/dt = 0).
- Incorrectly computing the second derivative (it is not d^2y/dt^2 divided by d^2x/dt^2).
