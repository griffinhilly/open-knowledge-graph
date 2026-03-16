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

## Explainer

In single-variable calculus, you learned to differentiate y implicitly by treating y as a function of x and applying the chain rule. For example, differentiating x² + y² = 1 with respect to x gives 2x + 2y(dy/dx) = 0, so dy/dx = −x/y. The multivariable version makes this procedure precise and general by reframing it in terms of partial derivatives. If F(x, y) = 0 defines y as a function of x near a point, then differentiating F(x, y(x)) = 0 with respect to x using the **chain rule** gives ∂F/∂x + (∂F/∂y)(dy/dx) = 0. Solving for dy/dx yields dy/dx = −(∂F/∂x)/(∂F/∂y), provided ∂F/∂y ≠ 0.

Your prerequisite on the multivariable chain rule is doing all the work here. F depends on x both directly and through y(x), so the total derivative of F with respect to x picks up both contributions: the direct partial ∂F/∂x, plus the indirect contribution through y, which is (∂F/∂y)(dy/dx). Setting the total to zero (because F = 0 is a constant) isolates dy/dx. The formula dy/dx = −Fₓ/F_y is not magic; it is the chain rule applied to a constant-valued composition.

The same idea extends to more variables. If F(x, y, z) = 0 defines z as a function of x and y, then ∂z/∂x = −(∂F/∂x)/(∂F/∂z) and ∂z/∂y = −(∂F/∂y)/(∂F/∂z). This lets you compute partial derivatives of implicitly defined functions without ever solving explicitly for z. For instance, if F(x, y, z) = x³ + y³ + z³ − xyz = 0 defines a surface, you can find the slope of the surface in the x-direction at any point without ever isolating z.

The technique also extends to systems of equations defining multiple variables implicitly. If you have two equations F(x, y, u, v) = 0 and G(x, y, u, v) = 0 defining u and v as functions of x and y, you differentiate both equations with respect to x (using the chain rule for each), which gives a 2 × 2 linear system in ∂u/∂x and ∂v/∂x. Solving that system — using Cramer's rule or substitution — gives the implicit partial derivatives. This is the beginning of the **implicit function theorem**, which formalizes exactly when a system of equations can be solved implicitly and provides the derivative formula as a consequence. The condition ∂F/∂y ≠ 0 (in the one-equation case) becomes the condition that the relevant Jacobian determinant is nonzero — the precise criterion for the local existence of the implicit function.
