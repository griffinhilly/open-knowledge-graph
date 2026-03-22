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

## Questions

```yaml
- question: "The equation dy/dx + 3y = 6 is solved using an integrating factor. As x → ∞, what determines the long-run behavior of the solution?"
  type: multiple-choice
  options:
    - "The constant of integration C, which scales the entire solution"
    - "The homogeneous solution Ce^(−3x), which stabilizes to a nonzero value"
    - "The particular solution y = 2, which the system settles toward as the transient decays"
    - "The forcing term Q(x) = 6, which continues to drive the system indefinitely"
  answer: 2
  explanation: "The general solution is y = 2 + Ce^(−3x). As x → ∞, the homogeneous part Ce^(−3x) → 0 (the transient dies away), leaving only y = 2 — the particular solution and the system's steady state. The forcing term Q(x) = 6 is what *creates* the steady state, but the steady state itself is the particular solution y_p = 2, not the forcing term directly."

- question: "Which property of the equation dy/dx + P(x)y = Q(x) is what makes the integrating factor method work and guarantees the solution has a homogeneous-plus-particular structure?"
  type: multiple-choice
  options:
    - "Q(x) must be a continuous function"
    - "P(x) must be a positive constant"
    - "Both y and dy/dx appear only to the first power — the equation is linear in y"
    - "The equation must have a unique solution for every initial condition"
  answer: 2
  explanation: "Linearity — y and dy/dx appearing only to the first power, with no y², sin(y), or (dy/dx)³ terms — is the structural property that makes the integrating factor trick work. It guarantees that the solution space has the additive structure that allows homogeneous and particular solutions to be combined. Nonlinear first-order ODEs do not generally admit this clean decomposition and cannot be solved by integrating factors."

- question: "For the equation dy/dx + P(x)y = Q(x) with P(x) > 0, the homogeneous solution always decays to zero as x → ∞."
  type: true-false
  answer: true
  explanation: "The homogeneous solution is y_h = Ce^(−∫P(x)dx). When P(x) > 0, the integral ∫P(x)dx grows without bound as x → ∞, so e^(−∫P(x)dx) → 0. This is why the homogeneous part is called a 'transient' in applied contexts — it represents the system's natural response to initial conditions, which eventually dies away, leaving only the particular solution (the forced steady state)."

- question: "In the general solution y = y_h + y_p of a first-order linear ODE, y_h captures the steady-state behavior the system approaches, while y_p represents the transient that dies away over time."
  type: true-false
  answer: false
  explanation: "This is reversed. The homogeneous solution y_h is the transient — it decays to zero (when P(x) > 0) and represents what the system does when left to its own natural dynamics from initial conditions. The particular solution y_p is the steady state — the system's persistent response to the forcing term Q(x). In the example dy/dx + 2y = 4, the solution y = 2 + Ce^(−2x) has transient Ce^(−2x) (homogeneous) and steady state y = 2 (particular)."

- question: "Explain why the solution to a first-order linear ODE dy/dx + P(x)y = Q(x) splits into a homogeneous part and a particular solution. What does each part represent physically or dynamically?"
  type: short-answer
  answer: "The homogeneous part y_h solves the equation with Q(x) = 0 — it describes the system's natural behavior driven purely by initial conditions, with no external forcing. The particular solution y_p represents the system's response to the forcing term Q(x). The full solution combines both: y_h captures how the initial state evolves (usually decaying), while y_p captures where the system is being driven toward. Linearity of the equation is what guarantees these two parts simply add together."
  explanation: "This structure — natural response plus forced response — appears throughout applied mathematics because linear systems obey superposition. In physical terms: the transient (y_h) is what the system 'wants' to do based on where it started; the steady state (y_p) is what the external driver is pushing it toward. As time passes, the transient fades and the forced behavior dominates. This is why circuits eventually charge to supply voltage, why temperatures equilibrate, and why chemical concentrations approach equilibrium."
```

## Explainer

You've already seen the integrating factor method as a technique. Now let's build intuition for what the equation dy/dx + P(x)y = Q(x) actually says and why the solution has the structure it does. The equation is called **linear** because y and dy/dx appear only to the first power — no y², no sin(y), no (dy/dx)³. This linearity is what makes the integrating factor trick work and is what guarantees the solution has a clean homogeneous-plus-particular form.

The term P(x)y is a **feedback term**: the rate of change of y depends on y itself, scaled by P(x). Consider the simplified case Q(x) = 0: the equation becomes dy/dx = −P(x)y, meaning "the rate of change of y is proportional to y." This is exponential behavior. When P(x) = k (constant), the solution is y = Ce^(−kx): exponential growth if k < 0, exponential decay if k > 0. This is the mathematics of radioactive decay (k > 0), population growth (k < 0), and Newton's law of cooling — the temperature difference decays exponentially toward zero.

The full equation with Q(x) ≠ 0 adds a **forcing term**: something external is driving the system. The general solution splits into two parts. The **homogeneous solution** y_h = Ce^(−∫P(x)dx) solves the equation with Q = 0 and captures the natural behavior of the system — what it does when left alone. The **particular solution** y_p captures the system's response to the forcing. The general solution y = y_h + y_p combines both, with the constant C determined by an initial condition. This structure — natural response plus forced response — reappears in every linear ODE and PDE, making it one of the most important patterns in applied mathematics.

A concrete example: dy/dx + 2y = 4. Here P(x) = 2, Q(x) = 4, so the integrating factor is e^(∫2 dx) = e^(2x). Multiply both sides: d/dx[e^(2x)y] = 4e^(2x). Integrate: e^(2x)y = 2e^(2x) + C. Divide: y = 2 + Ce^(−2x). The term Ce^(−2x) is the homogeneous solution (a transient that decays to zero), and y = 2 is the particular solution (the **steady state** the system settles toward as x → ∞). This pattern — a decaying transient plus a persistent steady state — describes circuits charging toward supply voltage, chemical concentrations approaching equilibrium, and temperatures equilibrating. The integrating factor method is the algorithm that computes this structure reliably for any P(x) and Q(x).
