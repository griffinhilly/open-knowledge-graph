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

## Questions

```yaml
- question: "A function f(z) = u(x,y) + iv(x,y) has continuous partial derivatives at z₀ and satisfies ∂u/∂x = ∂v/∂y and ∂u/∂y = −∂v/∂x there. Which conclusion follows?"
  type: multiple-choice
  options:
    - "f is real-differentiable at z₀ as a map from ℝ² to ℝ², but not necessarily complex-differentiable"
    - "f is holomorphic (complex-differentiable) at z₀"
    - "u and v are each harmonic on all of ℂ"
    - "f can be extended to a real-analytic function on a neighborhood of z₀"
  answer: 1
  explanation: "The Cauchy-Riemann equations together with continuity of partial derivatives are necessary and sufficient for complex differentiability at a point. Option A is wrong: satisfying the CR equations with continuous partials implies complex differentiability, which is stronger than (and implies) real differentiability, not the other way around. Option C overstates scope — harmonicity holds locally at the point, not necessarily on all of ℂ."

- question: "What is the geometric meaning of the Cauchy-Riemann equations, distinguishing holomorphic maps from arbitrary real-differentiable maps?"
  type: multiple-choice
  options:
    - "They force u and v to be polynomials, restricting holomorphic functions to algebraic expressions"
    - "They require f to map circles to circles, ruling out functions with varying scale"
    - "They restrict the local linear approximation to rotation and uniform scaling, ruling out shear or differential stretching"
    - "They require the Jacobian matrix of f to have positive determinant, ensuring orientation preservation"
  answer: 2
  explanation: "A real-differentiable map from ℝ² to ℝ² can have any 2×2 Jacobian. The CR equations restrict the Jacobian to matrices of the form [[a, −b],[b, a]], corresponding precisely to multiplication by the complex number a + ib — a rotation and uniform scaling. This eliminates shear, differential stretching, and orientation-reversing maps. Option D is weaker: positive determinant only ensures orientation preservation, whereas CR equations impose the much stronger condition of conformality."

- question: "If f(z) = u(x,y) + iv(x,y) is holomorphic on a simply connected domain, the harmonic conjugate of u is determined uniquely."
  type: true-false
  answer: false
  explanation: "Given a harmonic function u on a simply connected domain, the CR equations can be integrated to find v such that f = u + iv is holomorphic. But v is determined only up to an additive real constant: if v₀ is one harmonic conjugate, then v₀ + c for any real constant c also satisfies the CR equations with u. This mirrors how antiderivatives in single-variable calculus are defined only up to a constant."

- question: "Complex differentiability is strictly stronger than real differentiability: there exist functions that are real-differentiable everywhere but nowhere holomorphic."
  type: true-false
  answer: true
  explanation: "A real-differentiable function f: ℝ² → ℝ² only requires the linear approximation to exist; it can have any 2×2 Jacobian. Complex differentiability additionally requires that Jacobian to satisfy the CR equations. The function f(z) = z̄ (complex conjugate) is real-differentiable everywhere — its Jacobian is the constant matrix [[1, 0],[0, −1]] — but nowhere holomorphic because it reverses orientation and violates the CR equations (∂u/∂x = 1 but ∂v/∂y = −1)."

- question: "Derive the Cauchy-Riemann equations from the definition of complex differentiability by computing the limit of [f(z₀+Δz)−f(z₀)]/Δz along two different paths."
  type: short-answer
  answer: "Write f(z) = u(x,y) + iv(x,y). Along the real axis (Δz = Δx): the limit is ∂u/∂x + i∂v/∂x. Along the imaginary axis (Δz = iΔy): the limit is (1/i)∂u/∂y + ∂v/∂y = ∂v/∂y − i∂u/∂y. Setting the two limits equal — real parts equal and imaginary parts equal — gives ∂u/∂x = ∂v/∂y and ∂u/∂y = −∂v/∂x."
  explanation: "The derivation reveals why complex differentiability is so restrictive: the limit must be path-independent. Even requiring agreement along just two axis directions forces a coupling between all four partial derivatives. When partial derivatives are also continuous, this two-direction agreement is enough to guarantee the limit is the same from every direction — a non-trivial fact that makes holomorphic functions far more special than real-differentiable ones."
```

## Explainer

You know from holomorphic functions that complex differentiability is a much stronger condition than real differentiability, and you know how to compute partial derivatives of real two-variable functions. The **Cauchy-Riemann equations** are the precise bridge: they translate the complex-analytic condition (f is holomorphic at z₀) into a pair of real PDE conditions on the component functions u and v.

Write f(z) = u(x, y) + i·v(x, y) with z = x + iy. For f to be complex-differentiable at z₀, the limit [f(z₀ + Δz) − f(z₀)]/Δz must be the same no matter how Δz approaches 0. Approach along the real axis (Δz = Δx real): the limit is ∂u/∂x + i·∂v/∂x. Approach along the imaginary axis (Δz = i·Δy): the limit is (1/i)·∂u/∂y + ∂v/∂y = ∂v/∂y − i·∂u/∂y. Setting these equal — real parts equal and imaginary parts equal — gives exactly: **∂u/∂x = ∂v/∂y** and **∂u/∂y = −∂v/∂x**. These are the Cauchy-Riemann equations, and they must hold at every point where f is holomorphic.

The geometric meaning is that a holomorphic function acts locally like a rotation and uniform scaling — it cannot stretch x-directions differently from y-directions. A real-differentiable map from ℝ² to ℝ² can apply any linear transformation (any 2×2 matrix); a complex-differentiable map is restricted to those linear transformations corresponding to multiplication by a complex number (rotation + scaling). The Cauchy-Riemann equations enforce this restriction by coupling the partial derivatives of u and v.

An immediate consequence is that both u and v are **harmonic**: they satisfy Laplace's equation ∇²u = 0 and ∇²v = 0. To see why, differentiate the first C-R equation with respect to x and the second with respect to y, then add: ∂²u/∂x² + ∂²u/∂y² = 0. Given u, the Cauchy-Riemann equations become a system of first-order PDEs you can integrate (on a simply connected domain) to recover v uniquely up to a constant — this v is called the **harmonic conjugate** of u. This construction is the foundation for using complex analysis to solve physical problems involving fluid flow, heat distribution, and electrostatics.
