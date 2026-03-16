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

## Explainer

You know from holomorphic functions that complex differentiability is a much stronger condition than real differentiability, and you know how to compute partial derivatives of real two-variable functions. The **Cauchy-Riemann equations** are the precise bridge: they translate the complex-analytic condition (f is holomorphic at z₀) into a pair of real PDE conditions on the component functions u and v.

Write f(z) = u(x, y) + i·v(x, y) with z = x + iy. For f to be complex-differentiable at z₀, the limit [f(z₀ + Δz) − f(z₀)]/Δz must be the same no matter how Δz approaches 0. Approach along the real axis (Δz = Δx real): the limit is ∂u/∂x + i·∂v/∂x. Approach along the imaginary axis (Δz = i·Δy): the limit is (1/i)·∂u/∂y + ∂v/∂y = ∂v/∂y − i·∂u/∂y. Setting these equal — real parts equal and imaginary parts equal — gives exactly: **∂u/∂x = ∂v/∂y** and **∂u/∂y = −∂v/∂x**. These are the Cauchy-Riemann equations, and they must hold at every point where f is holomorphic.

The geometric meaning is that a holomorphic function acts locally like a rotation and uniform scaling — it cannot stretch x-directions differently from y-directions. A real-differentiable map from ℝ² to ℝ² can apply any linear transformation (any 2×2 matrix); a complex-differentiable map is restricted to those linear transformations corresponding to multiplication by a complex number (rotation + scaling). The Cauchy-Riemann equations enforce this restriction by coupling the partial derivatives of u and v.

An immediate consequence is that both u and v are **harmonic**: they satisfy Laplace's equation ∇²u = 0 and ∇²v = 0. To see why, differentiate the first C-R equation with respect to x and the second with respect to y, then add: ∂²u/∂x² + ∂²u/∂y² = 0. Given u, the Cauchy-Riemann equations become a system of first-order PDEs you can integrate (on a simply connected domain) to recover v uniquely up to a constant — this v is called the **harmonic conjugate** of u. This construction is the foundation for using complex analysis to solve physical problems involving fluid flow, heat distribution, and electrostatics.
