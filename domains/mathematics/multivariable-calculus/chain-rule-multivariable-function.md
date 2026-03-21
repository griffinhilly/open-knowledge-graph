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

## Questions

```yaml
- question: "A particle moves along a circle: x(t) = cos(t), y(t) = sin(t). The temperature field is T(x, y) = x² + y². What is dT/dt?"
  type: multiple-choice
  options:
    - "0 — the particle moves along the level set x² + y² = 1, so T is constant"
    - "−4xy sin(t)cos(t) — multiply the two chain contributions together"
    - "−2cos(t)sin(t) — only the x-contribution matters"
    - "2(cos t − sin t) — differentiate x and y and add them without partial derivatives"
  answer: 0
  explanation: "By the multivariable chain rule: dT/dt = (∂T/∂x)(dx/dt) + (∂T/∂y)(dy/dt) = (2x)(−sin t) + (2y)(cos t) = −2cos(t)sin(t) + 2sin(t)cos(t) = 0. The answer is zero because T = x² + y² = 1 everywhere on the unit circle — T is constant along this path. Option B is the critical misconception: the two chain contributions are added, not multiplied. Each intermediate variable contributes an independent additive term."

- question: "For z = f(x, y) where x = x(s, t) and y = y(s, t), what is ∂z/∂s according to the multivariable chain rule?"
  type: multiple-choice
  options:
    - "(∂f/∂x)(∂x/∂s) + (∂f/∂y)(∂y/∂s)"
    - "(∂f/∂x)(∂x/∂s) · (∂f/∂y)(∂y/∂s)"
    - "∂f/∂x + ∂f/∂y"
    - "(∂f/∂x + ∂f/∂y)(∂x/∂s + ∂y/∂s)"
  answer: 0
  explanation: "The dependency diagram shows two paths from z to s: one through x and one through y. Each path contributes one term — multiply the derivatives along that path — and the two terms are added. This gives (∂f/∂x)(∂x/∂s) + (∂f/∂y)(∂y/∂s). Option B multiplies the two contributions, which would only be correct if the effects were compounding rather than simultaneous. Options C and D incorrectly separate the partial derivatives."

- question: "When z depends on two intermediate variables x and y, each of which depends on t, the number of terms in dz/dt equals the number of intermediate variables (two)."
  type: true-false
  answer: true
  explanation: "True. The multivariable chain rule produces one term per path from z to the final variable t. With two intermediate variables, there are exactly two paths (z→x→t and z→y→t), giving two terms: (∂f/∂x)(dx/dt) + (∂f/∂y)(dy/dt). This pattern generalizes: three intermediate variables give three terms, and so on. The dependency diagram makes this explicit — count the paths, and you have the number of terms."

- question: "For z = f(x, y) with x = g(t) and y = h(t), the chain rule gives dz/dt = (∂f/∂x)(dx/dt) · (∂f/∂y)(dy/dt)."
  type: true-false
  answer: false
  explanation: "False. The correct formula is dz/dt = (∂f/∂x)(dx/dt) + (∂f/∂y)(dy/dt) — the contributions are added, not multiplied. Multiplication would apply if one effect depended on the other, but x and y change simultaneously and independently. Each is a separate channel through which changes in t reach z, so their contributions to z's total rate of change are summed."

- question: "Explain why the multivariable chain rule adds contributions from each intermediate variable rather than multiplying them."
  type: short-answer
  answer: "Each intermediate variable is a separate, simultaneous channel through which a small change in t affects z. As t changes by Δt, x changes by (dx/dt)Δt and y changes by (dy/dt)Δt, and each of these changes independently nudges z. The x-channel contributes approximately (∂f/∂x)(dx/dt)Δt to z, and the y-channel contributes (∂f/∂y)(dy/dt)Δt. Since both effects happen at the same time through independent pathways, the total change in z is the sum. Multiplication would imply one effect depends on the other."
  explanation: "This is the key structural difference from the single-variable chain rule, which has only one intermediate variable and thus one term. The additive structure reflects the linearity of the first-order approximation (total differential): dz ≈ (∂f/∂x)dx + (∂f/∂y)dy. The chain rule is just this differential formula divided by dt."
```

## Explainer

In single-variable calculus, the chain rule says: if z = f(x) and x = g(t), then dz/dt = (dz/dx)(dx/dt). You can think of this as "the rate at which z changes with t equals the rate z changes with x, times the rate x changes with t" — a chain of rates multiplied together. The multivariable chain rule generalizes this, but with one crucial twist: when z depends on *multiple* intermediate variables, each one contributes its own chain, and you sum all the contributions.

Consider z = f(x, y) where both x and y depend on a parameter t — perhaps t is time and (x(t), y(t)) is the position of a moving particle. As t changes, both x and y change simultaneously, and both changes feed into z. The total rate of change is dz/dt = (∂f/∂x)(dx/dt) + (∂f/∂y)(dy/dt). The two terms are independent contributions: the first captures how much z changes due to x's movement, the second captures how much z changes due to y's movement. Because x and y change simultaneously, you *add* the contributions rather than multiply. This additive structure is the hallmark of the multivariable chain rule.

A useful visual aid is the **dependency diagram**: draw z at the top, with branches down to x and y (intermediate variables), and further branches from x and y down to t (the ultimate variable). Each path from z to t contributes one term: multiply the derivatives along that path, then sum across all paths. For ∂z/∂s when x = x(s,t) and y = y(s,t), there are two paths — through x and through y — giving ∂z/∂s = (∂f/∂x)(∂x/∂s) + (∂f/∂y)(∂y/∂s). Adding more intermediate or final variables just adds more branches to the diagram.

This formula is not just a computational trick — it captures how disturbances propagate through functional dependencies. In physics, if the temperature T(x, y, z) of a fluid depends on position, and a particle moves along a path (x(t), y(t), z(t)), then dT/dt = ∂T/∂x · ẋ + ∂T/∂y · ẏ + ∂T/∂z · ż — the material derivative. In optimization and machine learning, the chain rule (extended to vector form as the Jacobian product rule) is the foundation of backpropagation. Mastering the dependency-diagram approach now lets you handle compositions of any complexity by mechanically reading off the paths.
