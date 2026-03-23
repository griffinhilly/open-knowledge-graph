---
id: separable-differential-equations
title: Separable Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: differential-equations-intro-separable
  type: hard
- id: integration-by-parts
  type: hard
- id: u-substitution
  type: hard
builds-toward:
- integrating-factor-method
tags:
- separable
- first-order
- integration
stage: formal-systems
status: validated
---

# Separable Differential Equations

## Core Idea
A separable differential equation has the form dy/dx = f(x)g(y), allowing you to separate variables into (1/g(y))dy = f(x)dx and integrate both sides. This is the most straightforward solution technique, converting a differential equation into two integration problems. Separable equations are common in applications and serve as a foundation for more complex methods.

## Questions

```yaml
- question: "You encounter the equation dy/dx = x + y. Can you solve it by separation of variables?"
  type: multiple-choice
  options:
    - "Yes — move all x terms to the right and all y terms to the left"
    - "No — the right side is a sum (x + y), not a product f(x)·g(y), so the variables cannot be separated"
    - "Yes — integrate both sides directly with respect to x"
    - "No — only first-order equations with constant coefficients can be separated"
  answer: 1
  explanation: "Separation of variables requires the equation to have the form dy/dx = f(x)·g(y) — the right side must factor into a product of a pure function of x and a pure function of y. The sum x + y cannot be factored this way: there is no way to write it as f(x)·g(y). This is the structural test for separability. An equation like dy/dx = xy (a product) is separable; dy/dx = x + y (a sum) is not."

- question: "After separating and integrating the equation dy/dx = 2xy, a student obtains ln|y| = x² + C. What does the constant C represent geometrically?"
  type: multiple-choice
  options:
    - "The domain over which the solution is defined"
    - "The parameter that selects one particular solution from the family of curves, determined by an initial condition"
    - "The type of integration technique used on the left side"
    - "Whether the solution is expressed implicitly or explicitly"
  answer: 1
  explanation: "The general solution ln|y| = x² + C (or equivalently y = Ae^(x²)) is a family of curves filling the xy-plane, one for each value of C. An initial condition y(x₀) = y₀ picks the specific curve passing through the point (x₀, y₀), determining C. Without an initial condition, C remains a free parameter and the solution is the entire family. C is not an artifact of the integration method — it is the essential parameter that distinguishes one particular solution from all the others."

- question: "A separable differential equation can yield a solution expressed as an implicit relation between x and y rather than as an explicit formula y = h(x)."
  type: true-false
  answer: true
  explanation: "After integrating both sides of a separated equation, you typically have an implicit equation like F(y) = G(x) + C. Sometimes this can be solved explicitly for y; sometimes it cannot. Both implicit and explicit forms are valid complete solutions. For example, separating and integrating dy/dx = y/x gives ln|y| = ln|x| + C, which simplifies to y = Ax. But more complex integrals may leave an implicit equation that cannot be inverted."

- question: "The general solution to a separable ODE is a unique curve determined by the equation alone."
  type: true-false
  answer: false
  explanation: "The general solution is a family of curves, parameterized by the constant of integration C. The equation alone does not pick one — it describes the entire collection of solutions consistent with the differential relationship. Only an initial condition (a specified point the solution must pass through) pins down C and selects one particular solution from the family."

- question: "What does it mean for a differential equation to be 'separable,' and why does that structural property allow integration to solve it?"
  type: short-answer
  answer: "A separable equation has the form dy/dx = f(x)·g(y): the right side factors into a pure function of x times a pure function of y. This means you can divide both sides by g(y) and multiply by dx to get (1/g(y)) dy = f(x) dx — all y-expressions on the left, all x-expressions on the right. Each side can now be integrated independently, converting the differential equation into two standard integration problems. The factored structure is the key: if the right side cannot be written as a product of separate functions, the variables cannot be separated and this technique does not apply."
  explanation: "Separability is a structural property of the equation, not a technique. The technique (separate and integrate) only works because the structure exists. Checking separability is always the first step, and recognizing when an equation is NOT separable (e.g., dy/dx = x + y) is as important as solving those that are."
```

## Explainer

A differential equation involves an unknown function and its derivatives. You already encountered separable equations in your introductory differential equations work, but this course deepens the technique by pairing it with integration-by-parts and u-substitution — tools you now have. The central idea is algebraic: a separable equation dy/dx = f(x)g(y) has its right-hand side factored into a pure function of x times a pure function of y. This factored structure is the key, because it means you can **separate** all y-related expressions to one side and all x-related expressions to the other.

The formal manipulation is: divide both sides by g(y) to get (1/g(y)) dy/dx = f(x), then treat dy/dx as a fraction and "multiply both sides by dx" to get (1/g(y)) dy = f(x) dx. This step is technically heuristic — you are treating the Leibniz notation as algebraic — but it is rigorously justified by the chain rule and substitution, and it produces the correct result. Now both sides can be integrated independently: ∫(1/g(y)) dy = ∫f(x) dx. Each side is a standard integration problem. You add a single constant of integration C (on one side is sufficient) to get the **general solution**.

The integrals you face after separating often require exactly your prerequisite techniques. If 1/g(y) is a product like y·eʸ, integration by parts handles it. If f(x) involves a composition like x·sin(x²), u-substitution applies. The separation step converts the ODE into two ordinary integrals, and your job is to evaluate each one. After integrating, you typically have an implicit equation relating y and x; sometimes you can solve explicitly for y, sometimes not. Either form is a valid solution.

An **initial condition** y(x₀) = y₀ pins down the constant C and selects a **particular solution** from the family of curves. Geometrically, the general solution is a family of curves filling the xy-plane, and the initial condition picks the one passing through the point (x₀, y₀). This is the standard workflow for every physical application: write the separable ODE from the model, integrate to find the general solution, apply initial conditions to find C. Population growth (dy/dt = ky), Newton's law of cooling (dT/dt = k(T − Tₐ)), and radioactive decay (dN/dt = −λN) are all separable equations solved by exactly this procedure — they produce exponential solutions because ∫ dy/y = ln|y|, and exponentiating both sides gives y = Ce^(kx).
