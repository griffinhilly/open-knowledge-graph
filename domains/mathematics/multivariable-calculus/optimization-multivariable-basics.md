---
id: optimization-multivariable-basics
title: Optimization in Multiple Variables
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: critical-points-extrema
  type: hard
- id: second-partials-test-hessian
  type: hard
- id: unconstrained-optimization
  type: soft
- id: differentiability-multivariable
  type: soft
builds-toward:
- lagrange-multipliers
- constrained-optimization
tags:
- optimization
- extrema
stage: formal-systems
status: validated
---
# Optimization in Multiple Variables

## Core Idea
To optimize f(x, y) on a region: find critical points, classify them, evaluate f at critical points and on the boundary, then compare. Global extrema on closed bounded sets are guaranteed to exist.

## Questions

```yaml
- question: "You are maximizing a continuous function f(x, y) on a closed bounded region D. You find two interior critical points and also optimize f along the boundary. Where must the global maximum occur?"
  type: multiple-choice
  options: ["At one of the interior critical points where ∇f = 0", "On the boundary of D", "At either a critical point or on the boundary — you must compare all candidates", "At the critical point where the Hessian is negative definite"]
  answer: 2
  explanation: "The Extreme Value Theorem guarantees a global max exists on a closed bounded set, but it can occur at an interior critical point OR on the boundary. You must evaluate f at all critical points and all boundary candidates, then compare every value. Stopping after finding interior critical points, or assuming the negative-definite Hessian point is the global max, is the most common error on multivariable optimization problems."

- question: "If a differentiable function f(x, y) has exactly one critical point in its domain and the Hessian at that point is positive definite (confirming a local minimum), then that point should be the global minimum of f."
  type: true-false
  answer: false
  explanation: "This is only guaranteed if the domain is closed and bounded (by the Extreme Value Theorem) and you have also checked the boundary. On an unbounded domain — or even on a closed bounded region where the boundary has not been checked — f could attain smaller values outside the interior. A local minimum is only a global minimum if no other point (including boundary points) yields a smaller value."

- question: "Describe the complete procedure for finding the global maximum and minimum of a continuous function f(x, y) on a closed bounded region D."
  type: short-answer
  answer: "Step 1: Find all interior critical points by solving ∇f = 0 and evaluate f at each. Step 2: Parameterize each piece of the boundary and optimize f restricted to that piece (a single-variable problem). Step 3: Collect all candidate values from steps 1 and 2. Step 4: The global max is the largest value; the global min is the smallest."
  explanation: "The Extreme Value Theorem guarantees both extrema exist on a closed bounded set, so this exhaustive comparison always terminates with valid answers. Steps 1 and 2 together cover all possible locations: the interior (where ∇f = 0 at any interior extremum) and the boundary (where the extremum need not satisfy ∇f = 0). Stopping after step 1 is a very common mistake — the global extremum often lies on the boundary."
```

## Explainer

From single-variable calculus, you know the procedure for finding extrema on a closed interval: set the derivative to zero, find interior critical points, evaluate at the endpoints, and compare all values. Multivariable optimization follows exactly the same logic — it just has more geometry. The "interior" is now the open region inside D, the "endpoints" become the boundary curve (or surface) of D, and "derivative = 0" becomes ∇f = 0.

The gradient ∇f = (∂f/∂x, ∂f/∂y) must vanish at any interior local extremum. This gives a system of two equations in two unknowns — typically nonlinear and potentially with multiple solutions. From second-partials-test-hessian you can classify each critical point by computing the Hessian matrix H and its determinant D = f_xx f_yy − (f_xy)². If D > 0 and f_xx > 0, the point is a local min; if D > 0 and f_xx < 0, a local max; if D < 0, a saddle point. Saddle points are the distinctly multivariable phenomenon — f increases in some directions and decreases in others, so the point is neither a local max nor a local min. They have no single-variable analogue (inflection points with f' = 0 are different).

The critical insight for global optimization is the Extreme Value Theorem: a continuous function on a closed bounded region D always attains a global maximum and minimum, and these must occur either at interior critical points or on the boundary of D. The boundary of a 2D region is typically made up of curves — line segments, circular arcs, or other parameterizable pieces. Optimizing f on each boundary piece reduces to a single-variable problem: parameterize the curve (e.g., x = cos t, y = sin t for the unit circle), substitute into f, and use single-variable calculus to find the extrema of the resulting function of t.

After collecting all candidates — values of f at interior critical points plus values at boundary extrema — you simply compare them. The largest is the global max; the smallest is the global min. There is no shortcut: a negative-definite Hessian at an interior point tells you only that it is a local max, not the global max. The boundary can easily produce higher values. This exhaustive comparison is the entire algorithm, and it always works on closed bounded domains.

This framework is the foundation for Lagrange multipliers, which handle equality-constrained optimization more elegantly. Instead of parameterizing the constraint curve and substituting, Lagrange multipliers directly find the points where ∇f is proportional to ∇g (the constraint gradient). The geometric meaning is the same: at a constrained optimum, f cannot increase in any direction tangent to the constraint, which is precisely the condition ∇f = λ∇g. Lagrange multipliers are the multivariable analogue of the endpoint condition in single-variable calculus.
