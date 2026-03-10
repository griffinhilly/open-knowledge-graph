---
id: partial-derivatives
title: Partial Derivatives
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: multivariable-limits
  type: hard
- id: derivative-notation
  type: hard
- id: functions-of-several-variables
  type: hard
builds-toward:
- higher-order-partial-derivatives
- gradient-vector
- tangent-planes
- chain-rule-multivariable
- critical-points-multivariable
tags:
- partial-derivatives
- differentiation
- multivariable
stage: formal-systems
status: draft
---

# Partial Derivatives

## Core Idea
The partial derivative ∂f/∂x measures the rate of change of f with respect to x while all other variables are held constant. It is computed exactly like an ordinary derivative, treating all other variables as constants. Geometrically, ∂f/∂x at a point gives the slope of the curve obtained by slicing the surface z = f(x, y) with a plane y = constant. Partial derivatives quantify sensitivity to each input variable independently.

## How It's Best Learned
Students who know single-variable differentiation can compute partial derivatives immediately — just hold other variables fixed. The challenge is not computation but interpretation. Emphasize the 'hold other variables fixed' rule and have students verify partial derivatives by drawing the corresponding cross-sectional slice of the surface.

## Common Misconceptions
- ∂f/∂x is not the same as df/dx; the partial derivative is only the rate of change in the x-direction.
- Existence of both partial derivatives at a point does not imply differentiability or even continuity.
- ∂²f/∂x∂y usually equals ∂²f/∂y∂x (Clairaut's theorem), but not always for pathological functions.
