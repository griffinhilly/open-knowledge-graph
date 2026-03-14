---
id: directional-derivatives
title: Directional Derivatives
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: gradient-vector
  type: hard
- id: dot-product
  type: hard
builds-toward:
- conservative-fields
tags:
- directional-derivative
- gradient
- unit-vector
- rate-of-change
stage: formal-systems
status: validated
---

# Directional Derivatives

## Core Idea
The directional derivative D_u f gives the rate of change of f in an arbitrary direction specified by a unit vector u. It is computed as D_u f = ∇f · u — the dot product of the gradient with the unit direction vector. This unifies partial derivatives (which are directional derivatives along coordinate axes) with the gradient (which is the direction of maximum directional derivative). The maximum value of D_u f over all unit vectors u is |∇f|, achieved when u = ∇f/|∇f|.

## How It's Best Learned
Present directional derivatives as answering the question: 'How fast does f change if I walk in direction u?' Then show that the formula D_u f = ∇f · u follows naturally. Have students compute directional derivatives for several directions at a single point and verify that the maximum occurs in the gradient direction.

## Common Misconceptions
- The direction vector u must be a unit vector; using a non-unit vector gives a scaled result.
- D_u f = ∇f · u, not |∇f| · |u|; the dot product formula includes the angle between ∇f and u.
- Directional derivatives can be negative (when moving in a direction that decreases f).
