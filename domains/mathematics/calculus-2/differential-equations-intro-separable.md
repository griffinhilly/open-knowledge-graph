---
id: differential-equations-intro-separable
title: Introduction to Differential Equations - Separable Equations
domain: mathematics
course: calculus-2
prerequisites:
  - id: u-substitution
    type: hard
  - id: derivatives-of-exponential-functions
    type: hard
builds-toward: []
tags: [differential-equations, separable, applications]
stage: formal-systems
status: draft
---

# Introduction to Differential Equations - Separable Equations

## Core Idea
A differential equation is an equation involving a function and its derivatives. A separable equation has the form dy/dx = f(x)g(y), which can be solved by separating variables: (1/g(y)) dy = f(x) dx, then integrating both sides. This technique solves many fundamental models: exponential growth/decay (dy/dx = ky), Newton's cooling law, logistic growth, and mixing problems. It is the first and most natural solution technique.

## How It's Best Learned
Start with exponential growth dy/dx = ky (solution: y = Ce^(kx)) as the motivating example. Practice the separation procedure: rearrange, integrate both sides, solve for y, apply initial conditions to find C. Work through applications: population growth, radioactive decay, cooling.

## Common Misconceptions
- Forgetting the constant of integration (or absolute value signs from integrating 1/y).
- Not checking that division by g(y) is valid (g(y) = 0 may give equilibrium solutions).
- Treating dy/dx as a fraction without understanding that separation of variables is justified by the chain rule.
