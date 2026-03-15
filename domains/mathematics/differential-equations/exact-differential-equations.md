---
id: exact-differential-equations
title: Exact Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: integrating-factor-method
  type: hard
- id: partial-derivatives
  type: soft
builds-toward:
- existence-uniqueness-ode
tags:
- exact-equations
- first-order
- partial-derivatives
stage: formal-systems
status: draft
---

# Exact Differential Equations

## Core Idea
An exact differential equation M(x,y)dx + N(x,y)dy = 0 satisfies ∂M/∂y = ∂N/∂x, indicating it comes from a potential function F(x,y) where dF = M dx + N dy. The solution is implicitly F(x,y) = C, found by integrating M with respect to x. For non-exact equations, an integrating factor can restore exactness.
