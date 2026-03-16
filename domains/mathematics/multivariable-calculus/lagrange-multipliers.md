---
id: lagrange-multipliers
title: Lagrange Multipliers
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: implicit-differentiation-multivariable
  type: hard
builds-toward:
- constrained-optimization
tags:
- lagrange
- constraints
stage: formal-systems
status: draft
---

# Lagrange Multipliers

## Core Idea
To optimize f(x, y) subject to g(x, y) = 0, solve ∇f = λ∇g along with the constraint. The Lagrange multiplier λ represents the sensitivity of the optimum to relaxing the constraint.

## Questions

```yaml
- question: "You want to maximize f(x, y) = xy subject to the constraint x + y = 10. The Lagrange conditions give ∇f = λ∇g. Which system of equations should you solve?"
  type: multiple-choice
  options: ["y = λ, x = λ, x + y = 10", "2x = λ, 2y = λ, x + y = 10", "y = 2λ, x = 2λ, x + y = 10", "x = λy, y = λx, x + y = 10"]
  answer: 0
  explanation: "Here f(x,y) = xy so ∇f = (y, x). The constraint is g(x,y) = x + y - 10 = 0 so ∇g = (1, 1). Setting ∇f = λ∇g gives y = λ·1 and x = λ·1, plus the constraint x + y = 10. This yields x = y = 5 and λ = 5."

- question: "The method of Lagrange multipliers finds the global maximum or minimum of f over all of ℝ², provided the gradient condition ∇f = λ∇g is satisfied somewhere."
  type: true-false
  answer: false
  explanation: "Lagrange multipliers only find candidates for optima *on the constraint curve* g(x,y) = 0, not over all of ℝ². Without the constraint, f might be unbounded or have a different global optimum. The method locates critical points of f restricted to the constraint; you still need to determine which candidates are maxima, minima, or neither."

- question: "Geometrically, why must ∇f be parallel to ∇g at a constrained optimum?"
  type: short-answer
  answer: "At a constrained optimum, the level curve of f must be tangent to the constraint curve g = 0. If the level curves of f crossed the constraint rather than touching it, you could move along the constraint and increase f further — so the point could not be a maximum. Tangency means the two gradients (which are perpendicular to their respective level/constraint curves) must point in the same or opposite directions, i.e., ∇f = λ∇g."
  explanation: "This geometric picture — level curves tangent to the constraint — is the core intuition behind the method. The scalar λ adjusts for the fact that the two gradients may have different magnitudes even when they are parallel."
```

## Explainer

Recall from single-variable calculus that finding the maximum of a function on a closed interval requires checking critical points (where f′ = 0) and boundary points separately. In multivariable calculus, optimizing f(x, y) subject to a constraint g(x, y) = 0 is the analog of that boundary problem: you want the best value of f, but only among points that satisfy the constraint curve.

The key geometric insight is this: at a constrained optimum, the constraint curve g = 0 must be tangent to a level curve of f. If the two curves crossed instead of touching, you could slide along the constraint to reach a higher (or lower) value of f — contradicting optimality. Because gradient vectors are always perpendicular to their level curves, tangency of the curves means the gradients must be parallel. Parallel vectors are scalar multiples of each other, so there exists some λ such that ∇f = λ∇g. That scalar λ is the Lagrange multiplier.

In practice, you solve the system: ∂f/∂x = λ·∂g/∂x, ∂f/∂y = λ·∂g/∂y, and g(x, y) = 0. That is three equations in three unknowns (x, y, λ). The solutions are constrained critical point candidates. You then evaluate f at each candidate to determine which is the maximum and which is the minimum (or compare to boundary behavior if the constraint is bounded).

The Lagrange multiplier λ has an important economic interpretation: it measures the rate of change of the optimal value of f with respect to a small relaxation of the constraint. If you are maximizing profit subject to a budget constraint, λ tells you how much additional profit you would gain per additional dollar of budget. This is why λ is often called the "shadow price" in optimization and economics.

One common error is forgetting to also solve the constraint equation g(x, y) = 0. The condition ∇f = λ∇g alone is not enough — it identifies the direction of the optimum but not where on the constraint it lies. All three equations must be solved simultaneously. Another pitfall: the method finds critical points, not guaranteed optima; always check whether you have found a maximum, a minimum, or a saddle point relative to the constraint.
