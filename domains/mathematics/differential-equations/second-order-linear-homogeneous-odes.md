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
tags:
- second-order
- homogeneous
- linear
stage: formal-systems
status: draft
---

# Second-Order Linear Homogeneous Differential Equations

## Core Idea
A second-order linear homogeneous ODE has the form y'' + p(x)y' + q(x)y = 0. The general solution is a linear combination of two linearly independent solutions: y = c₁y₁ + c₂y₂. For constant coefficients, solutions have exponential or trigonometric form determined by a characteristic equation. These equations model vibrations, electrical circuits, and countless physical phenomena.

## Questions

```yaml
- question: "The characteristic equation for y'' − 5y' + 6y = 0 has roots r = 2 and r = 3. What is the general solution?"
  type: multiple-choice
  options: ["y = e^(5x)", "y = c₁e^(2x) + c₂e^(3x)", "y = c₁cos(2x) + c₂sin(3x)", "y = (c₁ + c₂x)e^(5x)"]
  answer: 1
  explanation: "For two distinct real roots r₁ and r₂, the general solution is y = c₁e^(r₁x) + c₂e^(r₂x). With r₁ = 2 and r₂ = 3, this gives c₁e^(2x) + c₂e^(3x). The sinusoidal option applies only when roots are complex conjugates; the repeated-root option (c₁ + c₂x)eʳˣ applies only when r₁ = r₂."

- question: "A second-order linear homogeneous ODE can have three or more linearly independent solutions."
  type: true-false
  answer: false
  explanation: "The solution space of a second-order linear homogeneous ODE is exactly two-dimensional — it always has a basis of exactly two linearly independent solutions. Any solution is a linear combination c₁y₁ + c₂y₂ of those two. This mirrors how a second-order equation requires two initial conditions to determine a unique solution."

- question: "For a constant-coefficient second-order ODE, why do we try y = eʳˣ as the solution form?"
  type: short-answer
  answer: "Because differentiation of eʳˣ reproduces the same exponential: (eʳˣ)' = r·eʳˣ and (eʳˣ)'' = r²·eʳˣ. Substituting y = eʳˣ into the ODE therefore converts it into the algebraic equation r² + pr + q = 0 (the characteristic equation), which can be solved directly for r."
  explanation: "The exponential eʳˣ is an eigenfunction of the differentiation operator — differentiating it just multiplies by r. This property is what makes the substitution work. No other elementary function has this property in general, which is why the guess y = eʳˣ is so productive for constant-coefficient equations."
```

## Explainer

You already know how to solve first-order linear ODEs, which have a one-parameter family of solutions y = Ce^(∫−p dx). Second-order equations are one level harder: y'' + p(x)y' + q(x)y = 0 involves two derivatives, and the general solution has two free constants c₁ and c₂. Two constants are needed because specifying a unique solution requires two initial conditions — typically the value of y and the value of y' at a single point.

The structure of the general solution is y = c₁y₁ + c₂y₂, where y₁ and y₂ are any two linearly independent solutions. "Linearly independent" means neither is a constant multiple of the other — they represent genuinely different behaviors of the system. Any solution you could possibly find is a linear combination of these two, so once you have y₁ and y₂, you have everything. This is why the prerequisite on linear independence matters: it gives you the language to confirm you have a complete solution set.

For constant-coefficient equations y'' + py' + qy = 0, the key insight is the trial solution y = eʳˣ. Since (eʳˣ)'' = r²eʳˣ and (eʳˣ)' = reʳˣ, substituting into the ODE gives (r² + pr + q)eʳˣ = 0. Since eʳˣ ≠ 0, this reduces to the characteristic equation r² + pr + q = 0 — a plain quadratic. Its roots determine the solution form:
- Two distinct real roots r₁, r₂: y = c₁e^(r₁x) + c₂e^(r₂x)
- Repeated root r: y = (c₁ + c₂x)eʳˣ
- Complex conjugate roots α ± βi: y = eᵅˣ(c₁cos(βx) + c₂sin(βx))

The complex-root case explains why these equations model oscillation. A simple spring-mass system satisfies y'' + ky = 0 (no damping term), whose characteristic roots are ±i√k — pure imaginary. The solution is c₁cos(√k · x) + c₂sin(√k · x), perpetual sinusoidal motion. Adding a damping term y' shifts the roots into the left complex half-plane, introducing a decaying exponential factor eᵅˣ with α < 0: the system oscillates but with amplitude that shrinks over time. The characteristic equation encodes all of this physics in two numbers.
