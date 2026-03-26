---
id: constrained-optimization-lagrange
title: Constrained Optimization and Lagrange Multipliers
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: gradient-vector
  type: hard
- id: lagrange-multipliers
  type: hard
builds-toward:
- applications-multivariable
tags:
- lagrange-multipliers
- constraints
- optimization
stage: formal-systems
status: validated
---

# Constrained Optimization and Lagrange Multipliers

## Core Idea
To optimize f(x, y) subject to constraint g(x, y) = 0, solve ∇f = λ∇g at extrema. The multiplier λ indicates the rate of change of the optimum with respect to the constraint. Check boundary and critical points for absolute extrema on constrained regions.

## Questions

```yaml
- question: "To maximize f(x, y) = xy subject to x + y = 10, you set up ∇f = λ∇g with g(x, y) = x + y - 10. What are the correct gradient components ∇f and ∇g?"
  type: multiple-choice
  options: ["∇f = (y, x) and ∇g = (1, 1)", "∇f = (x, y) and ∇g = (1, 1)", "∇f = (y, x) and ∇g = (x, y)", "∇f = (1, 1) and ∇g = (y, x)"]
  answer: 0
  explanation: "The gradient of f(x, y) = xy is (∂f/∂x, ∂f/∂y) = (y, x). The gradient of g(x, y) = x + y - 10 is (∂g/∂x, ∂g/∂y) = (1, 1). Setting ∇f = λ∇g gives the system y = λ and x = λ, meaning x = y. Combined with the constraint x + y = 10, you get x = y = 5 and a maximum of f = 25."

- question: "If ∇f = λ∇g yields a unique solution point, that point is guaranteed to be the global maximum of f subject to g(x, y) = 0."
  type: true-false
  answer: false
  explanation: "Lagrange's condition ∇f = λ∇g identifies candidates for extrema — points where the constraint curve is tangent to a level curve of f. A unique solution could be a maximum, a minimum, or (in degenerate cases) neither. To determine which, you must evaluate f at all candidate points and compare values, or use second-order conditions. On a compact (closed and bounded) constraint, the maximum and minimum both exist, so the highest and lowest values among candidates are indeed the extrema — but you cannot know which is which without comparing."

- question: "Give the geometric interpretation of why ∇f and ∇g must be parallel at a constrained optimum."
  type: short-answer
  answer: "At a constrained optimum, the constraint curve g = 0 must be tangent to a level curve of f. If they crossed instead, you could move along the constraint to reach a higher (or lower) level curve of f, contradicting the assumption that we are at an optimum. Since the gradient of a function is always perpendicular to its level curves, both ∇f and ∇g are perpendicular to the same tangent direction — meaning they must be parallel to each other."
  explanation: "This geometric reasoning is the heart of the Lagrange method. The condition ∇f = λ∇g is not an arbitrary algebraic trick; it captures exactly the geometric situation where you cannot improve f by moving along the constraint. The scalar λ tells you how fast the optimal value of f changes if you relax the constraint — making it a powerful economic and physical interpretive tool (e.g., in resource allocation, λ is the 'shadow price' of the constraint)."
```

## Explainer

When you optimize a function without constraints, you look for points where the gradient is zero — flat spots where no direction of movement improves f. But many real problems impose restrictions: maximize profit given a fixed budget, minimize surface area of a container given a fixed volume, find the point on a curve closest to the origin. The Lagrange method is a systematic way to handle these constraints without eliminating variables by substitution.

The geometric insight is this: suppose you want to maximize f(x, y) subject to staying on the curve g(x, y) = 0. As you slide along the constraint curve, f changes. You have reached an optimum when moving along the constraint neither increases nor decreases f — in other words, the constraint curve is *tangent* to a level curve of f at that point. From your study of gradients, you know that ∇f is always perpendicular to the level curves of f, and similarly ∇g is always perpendicular to the constraint curve. When the two curves are tangent, they share the same tangent line and therefore have parallel normal vectors. This means ∇f and ∇g must point in the same (or opposite) direction — that is, ∇f = λ∇g for some scalar λ.

The scalar λ is the Lagrange multiplier. It is not merely an algebraic artifact; it has a concrete meaning. If you were to relax the constraint — for example, increasing the budget by one dollar — the optimal value of f would change by approximately λ. This interpretation makes λ valuable in economics (as the "shadow price" of a constraint) and in physics (as a generalized force associated with a constraint).

In practice, the method produces a system of equations: ∂f/∂x = λ(∂g/∂x), ∂f/∂y = λ(∂g/∂y), and g(x, y) = 0. For two variables and one constraint, this is three equations in three unknowns (x, y, λ). Solve for all candidates, evaluate f at each, and compare values to identify the maximum or minimum. A common error is assuming a unique solution must be a maximum — it could be a minimum, or the constraint might be unbounded, in which case no maximum exists at all.

For problems over a closed bounded region (not just a curve), you must also check *interior* critical points where ∇f = 0 and *boundary* behavior separately. The Lagrange method handles the constraint boundary, but the global optimum might occur in the interior. Always think about whether the feasible region is compact, because compactness (closed and bounded) guarantees that extrema exist and can be found by comparing all candidates.
