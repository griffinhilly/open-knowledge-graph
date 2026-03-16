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
status: draft
---

# Separable Differential Equations

## Core Idea
A separable differential equation has the form dy/dx = f(x)g(y), allowing you to separate variables into (1/g(y))dy = f(x)dx and integrate both sides. This is the most straightforward solution technique, converting a differential equation into two integration problems. Separable equations are common in applications and serve as a foundation for more complex methods.

## Explainer

A differential equation involves an unknown function and its derivatives. You already encountered separable equations in your introductory differential equations work, but this course deepens the technique by pairing it with integration-by-parts and u-substitution — tools you now have. The central idea is algebraic: a separable equation dy/dx = f(x)g(y) has its right-hand side factored into a pure function of x times a pure function of y. This factored structure is the key, because it means you can **separate** all y-related expressions to one side and all x-related expressions to the other.

The formal manipulation is: divide both sides by g(y) to get (1/g(y)) dy/dx = f(x), then treat dy/dx as a fraction and "multiply both sides by dx" to get (1/g(y)) dy = f(x) dx. This step is technically heuristic — you are treating the Leibniz notation as algebraic — but it is rigorously justified by the chain rule and substitution, and it produces the correct result. Now both sides can be integrated independently: ∫(1/g(y)) dy = ∫f(x) dx. Each side is a standard integration problem. You add a single constant of integration C (on one side is sufficient) to get the **general solution**.

The integrals you face after separating often require exactly your prerequisite techniques. If 1/g(y) is a product like y·eʸ, integration by parts handles it. If f(x) involves a composition like x·sin(x²), u-substitution applies. The separation step converts the ODE into two ordinary integrals, and your job is to evaluate each one. After integrating, you typically have an implicit equation relating y and x; sometimes you can solve explicitly for y, sometimes not. Either form is a valid solution.

An **initial condition** y(x₀) = y₀ pins down the constant C and selects a **particular solution** from the family of curves. Geometrically, the general solution is a family of curves filling the xy-plane, and the initial condition picks the one passing through the point (x₀, y₀). This is the standard workflow for every physical application: write the separable ODE from the model, integrate to find the general solution, apply initial conditions to find C. Population growth (dy/dt = ky), Newton's law of cooling (dT/dt = k(T − Tₐ)), and radioactive decay (dN/dt = −λN) are all separable equations solved by exactly this procedure — they produce exponential solutions because ∫ dy/y = ln|y|, and exponentiating both sides gives y = Ce^(kx).
