---
id: characteristic-equation-method
title: Characteristic Equation Method for Linear ODEs
domain: mathematics
course: differential-equations
prerequisites:
- id: second-order-linear-homogeneous-odes
  type: hard
- id: quadratic-formula
  type: hard
builds-toward:
- complex-roots-oscillatory-solutions
- repeated-roots-reduction-of-order
tags:
- characteristic-equation
- constant-coefficients
- solution-method
stage: formal-systems
status: draft
---

# Characteristic Equation Method for Linear ODEs

## Core Idea
For constant-coefficient linear ODEs, assume a solution y = e^(rx) and substitute to obtain a characteristic equation. For y'' + py' + qy = 0, the characteristic equation is r² + pr + q = 0. The roots r determine the solution form: distinct real roots give y = c₁e^(r₁x) + c₂e^(r₂x); complex roots give oscillatory solutions; repeated roots require x factors. This algebraic approach elegantly solves a wide class of equations.

## Explainer

You know from second-order linear ODEs that the general solution to y″ + py′ + qy = 0 is a linear combination of two independent solutions. The characteristic equation method is the systematic algorithm for finding those two solutions when p and q are constants. The key insight is an inspired guess, or **ansatz**: if we try y = e^(rx), then y′ = re^(rx) and y″ = r²e^(rx). Substituting into the equation gives r²e^(rx) + pre^(rx) + qe^(rx) = 0. Factor out e^(rx) — which is never zero — and you get r² + pr + q = 0. The differential equation has become a quadratic.

This quadratic, called the **characteristic equation**, is solved with the quadratic formula you already know. The roots r₁ and r₂ determine the solution form, and there are three cases based on the discriminant p² − 4q:

- **Two distinct real roots** (p² − 4q > 0): The two independent solutions are e^(r₁x) and e^(r₂x), giving y = c₁e^(r₁x) + c₂e^(r₂x). Each root contributes its own exponential.
- **Complex conjugate roots** r = α ± βi (p² − 4q < 0): The complex exponentials e^((α+βi)x) and e^((α−βi)x) are valid, but we can use Euler's formula to rewrite them in real form: y = e^(αx)(c₁cos(βx) + c₂sin(βx)). This is the oscillatory case — the solution is a sinusoid with exponentially growing or decaying amplitude.
- **Repeated root** r₁ = r₂ = r (p² − 4q = 0): Two copies of e^(rx) are not independent, so e^(rx) alone cannot span the solution space. The second independent solution is xe^(rx), giving y = (c₁ + c₂x)e^(rx).

The elegance of this method is that it converts a calculus problem into a purely algebraic one. The structure of the ODE's solutions — exponential growth or decay, oscillation, polynomial growth — is entirely encoded in the location of the characteristic roots in the complex plane. Roots with large negative real parts decay fast; purely imaginary roots oscillate without damping; roots with positive real parts grow without bound. This geometric picture of roots predicting behavior is the foundation for understanding stability in differential equations and control systems.
