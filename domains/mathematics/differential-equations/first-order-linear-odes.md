---
id: first-order-linear-odes
title: First-Order Linear Ordinary Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: integrating-factor-method
  type: hard
- id: antiderivatives
  type: hard
builds-toward:
- higher-order-linear-odes
- systems-first-order-linear-odes
tags:
- first-order
- linear
- fundamental
stage: formal-systems
status: draft
---

# First-Order Linear Ordinary Differential Equations

## Core Idea
A first-order linear ODE has the form dy/dx + P(x)y = Q(x). The general solution is y = c·e^(-∫P(x)dx) + e^(-∫P(x)dx)∫Q(x)e^(∫P(x)dx)dx, consisting of a homogeneous part and a particular solution. These equations are fundamental throughout applied mathematics and physics, modeling everything from radioactive decay to chemical reactions.

## Explainer

You've already seen the integrating factor method as a technique. Now let's build intuition for what the equation dy/dx + P(x)y = Q(x) actually says and why the solution has the structure it does. The equation is called **linear** because y and dy/dx appear only to the first power — no y², no sin(y), no (dy/dx)³. This linearity is what makes the integrating factor trick work and is what guarantees the solution has a clean homogeneous-plus-particular form.

The term P(x)y is a **feedback term**: the rate of change of y depends on y itself, scaled by P(x). Consider the simplified case Q(x) = 0: the equation becomes dy/dx = −P(x)y, meaning "the rate of change of y is proportional to y." This is exponential behavior. When P(x) = k (constant), the solution is y = Ce^(−kx): exponential growth if k < 0, exponential decay if k > 0. This is the mathematics of radioactive decay (k > 0), population growth (k < 0), and Newton's law of cooling — the temperature difference decays exponentially toward zero.

The full equation with Q(x) ≠ 0 adds a **forcing term**: something external is driving the system. The general solution splits into two parts. The **homogeneous solution** y_h = Ce^(−∫P(x)dx) solves the equation with Q = 0 and captures the natural behavior of the system — what it does when left alone. The **particular solution** y_p captures the system's response to the forcing. The general solution y = y_h + y_p combines both, with the constant C determined by an initial condition. This structure — natural response plus forced response — reappears in every linear ODE and PDE, making it one of the most important patterns in applied mathematics.

A concrete example: dy/dx + 2y = 4. Here P(x) = 2, Q(x) = 4, so the integrating factor is e^(∫2 dx) = e^(2x). Multiply both sides: d/dx[e^(2x)y] = 4e^(2x). Integrate: e^(2x)y = 2e^(2x) + C. Divide: y = 2 + Ce^(−2x). The term Ce^(−2x) is the homogeneous solution (a transient that decays to zero), and y = 2 is the particular solution (the **steady state** the system settles toward as x → ∞). This pattern — a decaying transient plus a persistent steady state — describes circuits charging toward supply voltage, chemical concentrations approaching equilibrium, and temperatures equilibrating. The integrating factor method is the algorithm that computes this structure reliably for any P(x) and Q(x).
