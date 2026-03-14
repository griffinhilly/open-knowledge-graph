---
id: repeated-roots-reduction-of-order
title: Repeated Roots and Reduction of Order
domain: mathematics
course: differential-equations
prerequisites:
- id: characteristic-equation-method
  type: hard
- id: second-order-linear-homogeneous-odes
  type: hard
builds-toward:
- variation-of-parameters
tags:
- second-order
- special-case
- method
stage: advanced
status: draft
---

# Repeated Roots and Reduction of Order

## Core Idea
When the characteristic equation has a repeated root r, one solution is y₁ = e^{rx}, but a second linearly independent solution is y₂ = xe^{rx}. Reduction of order is a general technique for finding a second solution when one solution is already known.

## How It's Best Learned
Verify that y₂ = xe^{rx} satisfies the ODE when r is a repeated root. Learn reduction of order as a general method: assume y₂ = u(x)·y₁ and solve for u(x).

## Common Misconceptions
- Thinking y₂ must be e^{r'x} for some other root r'; the factor x is crucial. - Not recognizing repeated roots in the characteristic equation (discriminant = 0). - Confusing the repeated root case with the distinct roots case in terms of the form of solutions.
