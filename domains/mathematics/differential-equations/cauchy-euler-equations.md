---
id: cauchy-euler-equations
title: Cauchy-Euler Equations
domain: mathematics
course: differential-equations
prerequisites:
  - id: characteristic-equation-method
    type: hard
  - id: repeated-roots-reduction-of-order
    type: soft
  - id: complex-roots-oscillatory-solutions
    type: soft
builds-toward:
  - frobenius-method
tags: [differential-equations, second-order, variable-coefficients, euler-equation, indicial-equation]
stage: formal-systems
status: validated
---

# Cauchy-Euler Equations

## Core Idea
A Cauchy-Euler (or equidimensional) equation has the form ax²y'' + bxy' + cy = 0, where each derivative is multiplied by the matching power of x. It has variable coefficients, yet it can be solved exactly. The trial solution y = xʳ turns it into the indicial equation ar(r - 1) + br + c = 0. The roots give the solutions, with three cases parallel to constant-coefficient equations: distinct real roots, a repeated root (which brings in ln x), and complex roots (which bring in cos(β ln x) and sin(β ln x)).

## How It's Best Learned
Have students substitute y = xʳ and watch every term become a multiple of xʳ, which explains why powers of x are the right guess. Then show that the change of variable x = eᵗ converts the equation into one with constant coefficients, which explains the ln x terms. Work one example of each root case and check each answer by substitution.

## Common Misconceptions
- The characteristic equation is ar² + br + c = 0, as for constant coefficients. (The indicial equation is ar(r - 1) + br + c = 0; the extra -ar term comes from differentiating xʳ twice.)
- A repeated root r gives solutions xʳ and x·xʳ. (The second solution is xʳ ln x, since x = eᵗ turns the constant-coefficient pattern teʳᵗ into xʳ ln x.)
- The solutions are valid for all real x. (The equation is singular at x = 0, and the formulas are written for x > 0; for x < 0 replace x by |x|.)

## Questions

```yaml
- question: "What is the general solution of x²y'' - 2xy' + 2y = 0 for x > 0?"
  type: multiple-choice
  options: ["y = c₁eˣ + c₂e²ˣ", "y = c₁x + c₂x²", "y = c₁x + c₂x ln x", "y = c₁x⁻¹ + c₂x⁻²"]
  answer: 1
  explanation: "Substituting y = xʳ gives r(r - 1) - 2r + 2 = r² - 3r + 2 = 0, so r = 1 and r = 2. The general solution is y = c₁x + c₂x². The exponential answer comes from wrongly treating the equation as constant-coefficient."

- question: "For x²y'' + 3xy' + y = 0, the indicial equation has a repeated root. Find the general solution for x > 0."
  type: short-answer
  answer: "y = (c₁ + c₂ ln x)/x"
  explanation: "The indicial equation is r(r - 1) + 3r + 1 = r² + 2r + 1 = (r + 1)² = 0, so r = -1 is repeated. The solutions are x⁻¹ and x⁻¹ ln x."

- question: "The equation x²y'' + xy' + y = 0 has solutions cos(ln x) and sin(ln x) for x > 0."
  type: true-false
  answer: true
  explanation: "The indicial equation is r(r - 1) + r + 1 = r² + 1 = 0, so r = ±i. Complex roots α ± βi give x^α cos(β ln x) and x^α sin(β ln x); here α = 0 and β = 1."

- question: "Why does the substitution x = eᵗ turn a Cauchy-Euler equation into a constant-coefficient equation?"
  type: short-answer
  answer: "With x = eᵗ, x·dy/dx = dy/dt and x²·d²y/dx² = d²y/dt² - dy/dt, so every term loses its power of x and the coefficients become constants."
  explanation: "The new equation is a·y'' + (b - a)y' + cy = 0 in t, whose characteristic equation ar² + (b - a)r + c = 0 is the same as the indicial equation. The solution eʳᵗ becomes xʳ and teʳᵗ becomes xʳ ln x."
```

## Explainer

Most second-order linear equations with variable coefficients cannot be solved with elementary functions. The Cauchy-Euler equation

ax²y'' + bxy' + cy = 0

is an important exception. Each derivative is multiplied by the power of x that matches its order. That pattern suggests a trial solution. If y = xʳ, then xy' = r xʳ and x²y'' = r(r - 1) xʳ. Every term is a multiple of xʳ. Substituting and dividing by xʳ (for x > 0) gives the indicial equation

ar(r - 1) + br + c = 0.

The solutions depend on the roots, in three cases that mirror constant-coefficient equations.

Distinct real roots r₁ and r₂ give y = c₁x^r₁ + c₂x^r₂. For x²y'' - 2xy' + 2y = 0, the indicial equation is r² - 3r + 2 = 0, with roots 1 and 2, so y = c₁x + c₂x².

A repeated root r gives only one power solution, xʳ. The second solution is xʳ ln x, found by reduction of order. For x²y'' + 3xy' + y = 0, the indicial equation is (r + 1)² = 0, so y = (c₁ + c₂ ln x)x⁻¹.

Complex roots α ± βi give x^(α + βi) = x^α e^(iβ ln x). Taking real and imaginary parts yields y = x^α(c₁ cos(β ln x) + c₂ sin(β ln x)). For x²y'' + xy' + y = 0, the roots are ±i and y = c₁ cos(ln x) + c₂ sin(ln x). These solutions oscillate, with the oscillations spreading out as x grows, because ln x grows slowly.

Why do logarithms appear? Substitute x = eᵗ, so t = ln x. The chain rule gives x dy/dx = dy/dt and x² d²y/dx² = d²y/dt² - dy/dt. The equation becomes ay'' + (b - a)y' + cy = 0 in the variable t, which has constant coefficients. Its characteristic equation is the indicial equation. The familiar solutions eʳᵗ and teʳᵗ translate back to xʳ and xʳ ln x.

The coefficient x² vanishes at x = 0, so x = 0 is a singular point. The formulas above hold for x > 0, and replacing x by |x| covers x < 0.

Cauchy-Euler equations are the model case for the method of Frobenius. Near a regular singular point, a general equation behaves like a Cauchy-Euler equation, and its indicial equation is found the same way.
