---
id: chain-rule-multivariable-function
title: Chain Rule for Multivariable Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: chain-rule-multivariable
  type: hard
builds-toward:
- implicit-differentiation-multivariable
tags:
- chain-rule
- composition
- derivatives
stage: formal-systems
status: draft
---

# Chain Rule for Multivariable Functions

## Core Idea
For z = f(x, y) where x = x(t) and y = y(t), the chain rule gives dz/dt = (∂f/∂x)(dx/dt) + (∂f/∂y)(dy/dt). For z = f(x, y) where x = x(s, t), the general case involves partial derivatives: ∂z/∂s and ∂z/∂t.

## Explainer

In single-variable calculus, the chain rule says: if z = f(x) and x = g(t), then dz/dt = (dz/dx)(dx/dt). You can think of this as "the rate at which z changes with t equals the rate z changes with x, times the rate x changes with t" — a chain of rates multiplied together. The multivariable chain rule generalizes this, but with one crucial twist: when z depends on *multiple* intermediate variables, each one contributes its own chain, and you sum all the contributions.

Consider z = f(x, y) where both x and y depend on a parameter t — perhaps t is time and (x(t), y(t)) is the position of a moving particle. As t changes, both x and y change simultaneously, and both changes feed into z. The total rate of change is dz/dt = (∂f/∂x)(dx/dt) + (∂f/∂y)(dy/dt). The two terms are independent contributions: the first captures how much z changes due to x's movement, the second captures how much z changes due to y's movement. Because x and y change simultaneously, you *add* the contributions rather than multiply. This additive structure is the hallmark of the multivariable chain rule.

A useful visual aid is the **dependency diagram**: draw z at the top, with branches down to x and y (intermediate variables), and further branches from x and y down to t (the ultimate variable). Each path from z to t contributes one term: multiply the derivatives along that path, then sum across all paths. For ∂z/∂s when x = x(s,t) and y = y(s,t), there are two paths — through x and through y — giving ∂z/∂s = (∂f/∂x)(∂x/∂s) + (∂f/∂y)(∂y/∂s). Adding more intermediate or final variables just adds more branches to the diagram.

This formula is not just a computational trick — it captures how disturbances propagate through functional dependencies. In physics, if the temperature T(x, y, z) of a fluid depends on position, and a particle moves along a path (x(t), y(t), z(t)), then dT/dt = ∂T/∂x · ẋ + ∂T/∂y · ẏ + ∂T/∂z · ż — the material derivative. In optimization and machine learning, the chain rule (extended to vector form as the Jacobian product rule) is the foundation of backpropagation. Mastering the dependency-diagram approach now lets you handle compositions of any complexity by mechanically reading off the paths.
