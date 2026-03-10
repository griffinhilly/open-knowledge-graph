---
id: gradient-vector
title: The Gradient Vector
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: partial-derivatives
  type: hard
- id: vectors-in-rn
  type: hard
builds-toward:
- directional-derivatives
- critical-points-multivariable
- lagrange-multipliers
- conservative-fields
tags:
- gradient
- nabla
- steepest-ascent
- level-curves
stage: formal-systems
status: draft
---

# The Gradient Vector

## Core Idea
The gradient of f is the vector ∇f = ⟨∂f/∂x, ∂f/∂y⟩ (in ℝ²) or ⟨∂f/∂x, ∂f/∂y, ∂f/∂z⟩ (in ℝ³) that collects all partial derivatives. The gradient points in the direction of steepest increase of f and is always perpendicular to the level curves (or level surfaces) of f. The magnitude |∇f| gives the rate of change in the steepest direction. These two properties — direction and orthogonality to level sets — make the gradient the central object of multivariable calculus.

## How It's Best Learned
Draw level curves and overlay the gradient field. Students should see geometrically that ∇f is perpendicular to level curves before they see any algebraic proof. The steepest-ascent interpretation connects directly to gradient descent in optimization and machine learning contexts, which provides strong motivation.

## Common Misconceptions
- The gradient is a vector, not a scalar; confusing ∇f with |∇f| is common.
- The gradient points in the direction of steepest increase, not steepest decrease.
- ∇f is perpendicular to level curves in the domain (xy-plane), not to the surface z = f(x,y) in ℝ³.
