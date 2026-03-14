---
id: exact-differential-equations
title: Exact Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: separable-differential-equations
  type: hard
- id: partial-derivatives
  type: hard
builds-toward:
- integrating-factor-method
- partial-fraction-decomposition-integration
tags:
- first-order
- test
- method
stage: advanced
status: draft
---

# Exact Differential Equations

## Core Idea
An equation M(x,y)dx + N(x,y)dy = 0 is exact if ∂M/∂y = ∂N/∂x, meaning it represents the total differential of some function F(x,y). For exact equations, the solution is F(x,y) = C, found by integrating M or N appropriately.

## How It's Best Learned
Start by checking the exactness condition ∂M/∂y = ∂N/∂x for several examples. Then practice finding F by integrating M with respect to x, then adjusting for the y-dependent part.

## Common Misconceptions
- Confusing exactness with separability; an exact equation is not necessarily separable. - Computing partial derivatives incorrectly. - Not handling the constant of integration properly when finding F(x,y) from M or N.
