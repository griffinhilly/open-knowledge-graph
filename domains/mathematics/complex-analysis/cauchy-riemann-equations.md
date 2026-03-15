---
id: cauchy-riemann-equations
title: Cauchy-Riemann Equations
domain: mathematics
course: complex-analysis
prerequisites:
- id: holomorphic-functions
  type: hard
- id: partial-derivatives
  type: hard
builds-toward:
- harmonic-functions-complex-analysis
- harmonic-conjugates
tags:
- cauchy-riemann
- partial-derivatives
- holomorphic
stage: advanced
status: draft
---

# Cauchy-Riemann Equations

## Core Idea
If f(z) = u(x,y) + i v(x,y) is holomorphic, then ∂u/∂x = ∂v/∂y and ∂u/∂y = -∂v/∂x. These equations are necessary and sufficient (with continuity of partial derivatives) for f to be analytic. They reveal that the real and imaginary parts are not independent: once one is specified on a simply connected domain, the other is determined up to a constant.
