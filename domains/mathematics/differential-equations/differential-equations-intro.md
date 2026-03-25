---
id: differential-equations-intro
title: Introduction to Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: integration-by-parts
  type: hard
- id: rlc-circuits
  type: soft
builds-toward:
- separable-differential-equations
- first-order-linear-odes
- direction-fields-and-solution-curves
tags:
- ode
- foundational
- modeling
stage: formal-systems
status: validated
---
# Introduction to Differential Equations

## Core Idea
A differential equation is an equation involving a function and its derivatives. Differential equations model how systems change over time and are fundamental to physics, engineering, and natural sciences. The goal is to find the function (or functions) that satisfy the equation.

## Questions

```yaml
- question: "What is the general solution to the differential equation dy/dx = y?"
  type: multiple-choice
  options: ["y = x + C", "y = Ce^x", "y = x²/2 + C", "y = ln(x) + C"]
  answer: 1
  explanation: "We need a function whose derivative equals itself. The exponential function y = e^x has this property. Scaling by any constant C still satisfies the equation: d(Ce^x)/dx = Ce^x = y. The general solution is y = Ce^x, where C is determined by an initial condition. The other options do not satisfy dy/dx = y."

- question: "The solution to a differential equation is always a single specific number."
  type: true-false
  answer: false
  explanation: "Solutions to differential equations are functions, not numbers. The general solution is typically a family of functions parameterized by one or more constants (e.g., y = Ce^x). A particular solution is one member of that family, selected by applying an initial or boundary condition. The constants arise because integration — the reverse of differentiation — always introduces an arbitrary constant."

- question: "What is the difference between a general solution and a particular solution of a differential equation?"
  type: short-answer
  answer: "A general solution represents the full family of functions satisfying the equation, containing arbitrary constants. A particular solution fixes those constants using initial or boundary conditions to give one specific function."
  explanation: "When you integrate to solve a differential equation, each integration step introduces one arbitrary constant. The general solution preserves these constants. To find a particular solution, you apply given conditions (e.g., y(0) = 3) to determine the constant values, selecting the single function from the family that satisfies both the equation and the conditions."
```

## Explainer

Every calculus course teaches you to compute derivatives — given a function f(x), find f′(x). A differential equation flips that task: you are given a relationship involving f′(x) (or higher derivatives), and you must recover f(x) itself. For example, if you know that a quantity grows at a rate proportional to its current size, you can write this as dy/dt = ky, and the question becomes: which function y(t) satisfies this equation? The answer — y = Ce^(kt) — is the exponential growth model that describes populations, radioactive decay, compound interest, and more.

The key conceptual shift is that *solutions are functions, not numbers*. In algebra, solving x² = 9 gives x = ±3 — specific values. Solving dy/dx = y gives y = Ce^x — an entire family of functions, one for each value of the constant C. The constant arises because solving a differential equation involves integration, and integration always introduces an arbitrary constant. To pin down a specific solution, you need an *initial condition*: a known value of the function at a specific point, like y(0) = 5. With that, C = 5 and the particular solution is y = 5e^x.

Differential equations are classified by two key attributes: *order* and *linearity*. The order is the highest derivative that appears — dy/dx = y is first-order, d²y/dx² + y = 0 is second-order. Linearity means that y and all its derivatives appear to the first power without multiplication by each other. These classifications matter because they determine which solution techniques apply. Most courses start with first-order equations and progress to second-order linear equations, which have rich solution theory.

Your prerequisite of integration by parts is already a direct solving technique: some first-order equations can be solved by separating variables and integrating both sides. Later in the course, partial derivatives and matrix operations become relevant — partial derivatives open the door to *partial* differential equations (PDEs), and matrices are used to solve systems of ODEs. But the introductory material requires only single-variable calculus. This course focuses on *ordinary* differential equations (ODEs), where the unknown function has only one independent variable.

Almost everything in physics, engineering, and the natural sciences is ultimately described by differential equations. Newton's second law (F = ma) is a second-order ODE when force depends on position. Circuit equations, population models, fluid dynamics — all express "how fast something changes" in terms of "what it currently is." Learning to read, classify, and solve differential equations is learning the language that the physical world is written in.
