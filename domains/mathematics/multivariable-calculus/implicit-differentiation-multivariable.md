---
id: implicit-differentiation-multivariable
title: Implicit Differentiation in Several Variables
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: chain-rule-multivariable-function
  type: hard
builds-toward:
- critical-points-multivariable
tags:
- implicit-functions
- differentiation
stage: formal-systems
status: draft
---

# Implicit Differentiation in Several Variables

## Core Idea
For an implicit equation F(x, y) = 0, we can find dy/dx by differentiating with respect to x: (∂F/∂x) + (∂F/∂y)(dy/dx) = 0, so dy/dx = −(∂F/∂x)/(∂F/∂y). This extends to multiple variables and constraints.

## Questions

```yaml
- question: "Given F(x, y) = x² + y³ − 5 = 0, which expression correctly gives dy/dx?"
  type: multiple-choice
  options:
    - "dy/dx = −(2x)/(3y²)"
    - "dy/dx = −(3y²)/(2x)"
    - "dy/dx = (2x)/(3y²)"
    - "dy/dx = (∂F/∂y)/(∂F/∂x)"
  answer: 0
  explanation: "The formula is dy/dx = −(∂F/∂x)/(∂F/∂y). Here ∂F/∂x = 2x and ∂F/∂y = 3y², so dy/dx = −2x/(3y²). Option B reverses numerator and denominator. Option C drops the negative sign. Option D inverts the ratio — a very common error, since the negative partial of x goes in the numerator, not denominator."

- question: "When using the implicit differentiation formula dy/dx = −Fₓ/F_y, a student asks: 'Where does the negative sign come from?' The best answer is:"
  type: multiple-choice
  options:
    - "It is a convention chosen to make the formula agree with known examples like the unit circle"
    - "It arises because differentiating F(x, y(x)) = 0 with respect to x gives Fₓ + F_y(dy/dx) = 0, so dy/dx = −Fₓ/F_y"
    - "It reflects the fact that as x increases, y must decrease to stay on the level set"
    - "It comes from the negative slope of implicit curves, which always decrease"
  answer: 1
  explanation: "The negative sign is not a convention or a geometric observation — it is a direct algebraic consequence of the chain rule. Differentiating the constant F(x, y(x)) = 0 with respect to x produces two terms via the chain rule: the direct dependence ∂F/∂x, and the indirect dependence through y, which is (∂F/∂y)(dy/dx). Setting their sum to zero and solving gives the formula with its negative sign. Option C is geometrically true for some curves but is not the source of the sign."

- question: "The formula dy/dx = −(∂F/∂x)/(∂F/∂y) is an independent rule specific to implicit functions, separate from the chain rule."
  type: true-false
  answer: false
  explanation: "The formula is a direct application of the multivariable chain rule to the identity F(x, y(x)) = 0. It is not an independent rule; the chain rule is doing all the work. Understanding this derivation — rather than memorizing the formula — allows you to extend the technique to more variables, constrained systems, and eventually the implicit function theorem."

- question: "If F(x, y) = 0 and ∂F/∂y = 0 at a point, the implicit differentiation formula dy/dx = −Fₓ/F_y breaks down at that point."
  type: true-false
  answer: true
  explanation: "The condition ∂F/∂y ≠ 0 is essential: dividing by ∂F/∂y is only valid when it is nonzero. Geometrically, ∂F/∂y = 0 means the level set F = 0 has a vertical tangent or a singular point at that location — y may not be well-defined as a function of x near there. This is precisely the condition stated by the implicit function theorem for when the implicit function y(x) locally exists and is differentiable."

- question: "Explain why the implicit differentiation formula dy/dx = −(∂F/∂x)/(∂F/∂y) requires the condition ∂F/∂y ≠ 0, and what its failure signals geometrically."
  type: short-answer
  answer: "The formula is derived by solving Fₓ + F_y(dy/dx) = 0 for dy/dx; dividing by F_y is only valid if F_y ≠ 0. If F_y = 0, the equation Fₓ = 0 either has no solution for dy/dx (if Fₓ ≠ 0) or leaves dy/dx undetermined. Geometrically, F_y = 0 means the level curve F = 0 has a vertical tangent — the curve turns back on itself so y is no longer a single-valued function of x. The implicit function theorem formalizes this: F_y ≠ 0 guarantees that y can be expressed as a smooth function of x near the point."
  explanation: "Students often apply the formula mechanically without checking the condition. At a vertical tangent, the tangent line is dy/dx → ∞, which the formula correctly signals by producing division by zero. At a cusp or self-intersection, F_y = 0 occurs at a singular point where the whole concept of 'the derivative' fails. The condition is not a technicality but a genuine check on whether differentiation makes sense."
```

## Explainer

In single-variable calculus, you learned to differentiate y implicitly by treating y as a function of x and applying the chain rule. For example, differentiating x² + y² = 1 with respect to x gives 2x + 2y(dy/dx) = 0, so dy/dx = −x/y. The multivariable version makes this procedure precise and general by reframing it in terms of partial derivatives. If F(x, y) = 0 defines y as a function of x near a point, then differentiating F(x, y(x)) = 0 with respect to x using the **chain rule** gives ∂F/∂x + (∂F/∂y)(dy/dx) = 0. Solving for dy/dx yields dy/dx = −(∂F/∂x)/(∂F/∂y), provided ∂F/∂y ≠ 0.

Your prerequisite on the multivariable chain rule is doing all the work here. F depends on x both directly and through y(x), so the total derivative of F with respect to x picks up both contributions: the direct partial ∂F/∂x, plus the indirect contribution through y, which is (∂F/∂y)(dy/dx). Setting the total to zero (because F = 0 is a constant) isolates dy/dx. The formula dy/dx = −Fₓ/F_y is not magic; it is the chain rule applied to a constant-valued composition.

The same idea extends to more variables. If F(x, y, z) = 0 defines z as a function of x and y, then ∂z/∂x = −(∂F/∂x)/(∂F/∂z) and ∂z/∂y = −(∂F/∂y)/(∂F/∂z). This lets you compute partial derivatives of implicitly defined functions without ever solving explicitly for z. For instance, if F(x, y, z) = x³ + y³ + z³ − xyz = 0 defines a surface, you can find the slope of the surface in the x-direction at any point without ever isolating z.

The technique also extends to systems of equations defining multiple variables implicitly. If you have two equations F(x, y, u, v) = 0 and G(x, y, u, v) = 0 defining u and v as functions of x and y, you differentiate both equations with respect to x (using the chain rule for each), which gives a 2 × 2 linear system in ∂u/∂x and ∂v/∂x. Solving that system — using Cramer's rule or substitution — gives the implicit partial derivatives. This is the beginning of the **implicit function theorem**, which formalizes exactly when a system of equations can be solved implicitly and provides the derivative formula as a consequence. The condition ∂F/∂y ≠ 0 (in the one-equation case) becomes the condition that the relevant Jacobian determinant is nonzero — the precise criterion for the local existence of the implicit function.
