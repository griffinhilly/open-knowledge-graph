---
id: constrained-optimization
title: Constrained Optimization Applications
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: lagrange-multipliers
  type: hard
- id: optimization-multivariable-basics
  type: soft
tags:
- constraints
- applications
stage: formal-systems
status: validated
---

# Constrained Optimization Applications

## Core Idea
Constrained optimization models engineering problems: maximizing profit subject to resource constraints, minimizing surface area for fixed volume, finding shortest paths on surfaces. Lagrange multipliers solve these systematically.

## Questions

```yaml
- question: "To minimize f(x, y) subject to the constraint g(x, y) = 0, the Lagrange condition requires:"
  type: multiple-choice
  options: ["∇f = 0 at the solution", "∇f = λ∇g for some scalar λ", "∇g = 0 at the solution", "f(x, y) = g(x, y) at the solution"]
  answer: 1
  explanation: "The Lagrange condition is ∇f = λ∇g: the gradient of the objective must be parallel to the gradient of the constraint at any constrained optimum. The gradient of f is not zero in general (that would be an unconstrained critical point), and the constraint gradient ∇g points normal to the constraint surface."

- question: "At a constrained optimum, the gradient of the objective function f should equal the zero vector."
  type: true-false
  answer: false
  explanation: "At a free (unconstrained) optimum, ∇f = 0. But at a constrained optimum, ∇f is typically nonzero — it is parallel to ∇g (the constraint normal). The condition ∇f = λ∇g says the objective 'wants' to move in the same direction the constraint prevents it from moving. Setting ∇f = 0 would mean the unconstrained optimum already satisfies the constraint, which is a coincidence, not the general case."

- question: "A factory maximizes output f(x, y) subject to a budget constraint g(x, y) = 5000. The Lagrange multiplier λ = 12. What does this value mean practically?"
  type: short-answer
  answer: "Each additional unit of budget (e.g., one extra dollar) would allow approximately 12 more units of output. λ is the marginal value of the constraint."
  explanation: "The Lagrange multiplier measures the sensitivity of the optimal objective value to the constraint bound. If the budget increased from 5000 to 5001, the maximum output would increase by approximately λ = 12. In economics this is called the shadow price of the constraint — how much you would be willing to pay for one more unit of the scarce resource."
```

## Explainer

You learned Lagrange multipliers as a method for finding critical points of a function on a constraint surface. Constrained optimization applications ask: once you have that method, what real problems does it solve, and how do you set them up correctly?

The setup always has the same structure. There is an objective function f(x₁, …, xₙ) you want to maximize or minimize, and one or more constraint equations g(x₁, …, xₙ) = c that restrict which points are feasible. Classic examples: maximize the volume of a box (objective) with fixed total surface area (constraint); minimize the cost of a cylindrical can (objective) with fixed volume (constraint); find the point on a plane closest to the origin (objective) subject to the plane equation (constraint). The Lagrange condition ∇f = λ∇g is the same in every case — only the algebra changes.

The geometric intuition is worth carrying into applications: at a constrained optimum, the level sets of f are tangent to the constraint curve or surface. If they were not tangent — if they crossed — you could slide along the constraint and improve f, so you would not yet be at an optimum. Tangency means the two gradients point in the same direction, which is exactly ∇f = λ∇g.

The Lagrange multiplier λ itself carries important information that is easy to overlook. Mathematically, λ = df*/dc, where f* is the optimal value and c is the constraint bound. In words: λ tells you how much the optimal objective value changes per unit relaxation of the constraint. In the box problem, λ would tell you how much extra volume you gain per additional unit of surface area. In an economics problem, λ is the shadow price — the maximum you would be willing to pay for one more unit of the constrained resource. When you report a constrained optimization solution, reporting λ alongside the optimal point often provides the most actionable information.
