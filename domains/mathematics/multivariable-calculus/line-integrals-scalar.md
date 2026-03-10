---
id: line-integrals-scalar
title: Line Integrals of Scalar Functions
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: vector-valued-functions
  type: hard
- id: definite-integral-definition
  type: hard
- id: arc-length-parametric
  type: hard
builds-toward:
- line-integrals-vector-fields
tags:
- line-integral
- curve
- scalar
- arc-length
- mass
stage: formal-systems
status: draft
---

# Line Integrals of Scalar Functions

## Core Idea
The line integral ∫_C f ds integrates a scalar function f along a curve C, where ds = |r′(t)| dt is the arc length element. It computes the total accumulated value of f along the curve, weighted by arc length — for instance, the mass of a wire with linear density f(x, y). The integral is evaluated by parametrizing C as r(t), a ≤ t ≤ b, and computing ∫_a^b f(r(t)) |r′(t)| dt. The value is independent of the parametrization (as long as orientation is preserved).

## How It's Best Learned
The mass-of-a-wire interpretation is the clearest motivation. Work several examples where C is a line segment or a circular arc and f is a simple function. Emphasize that ds = |r′(t)| dt automatically handles the arc length weight — students should not try to separately compute arc length.

## Common Misconceptions
- The line integral ∫_C f ds is not the same as ∫_a^b f(t) dt; the integrand includes the speed factor |r′(t)|.
- The result does not depend on the parametrization (as long as the curve is traversed once in the same direction).
- Unlike line integrals of vector fields, scalar line integrals are independent of orientation — reversing the direction of C does not change the sign.
