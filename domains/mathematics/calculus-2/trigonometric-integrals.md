---
id: trigonometric-integrals
title: Trigonometric Integrals
domain: mathematics
course: calculus-2
prerequisites:
  - id: trigonometric-identities-pythagorean
    type: hard
  - id: double-angle-identities
    type: hard
  - id: u-substitution
    type: hard
builds-toward:
  - trigonometric-substitution
tags: [integration, techniques, trigonometric]
stage: formal-systems
status: draft
---

# Trigonometric Integrals

## Core Idea
Trigonometric integrals involve products and powers of trig functions: sin^m(x) cos^n(x), tan^m(x) sec^n(x), etc. The strategy depends on the exponents: if one exponent is odd, save one factor for du and convert the rest using Pythagorean identities. If both are even, use half-angle (power-reduction) identities. For tangent-secant integrals, similar strategies apply with tan^2 = sec^2 - 1.

## How It's Best Learned
Organize by case: sin^m cos^n with one odd exponent, both even, and the analogous tan-sec cases. Master each case's strategy, then practice mixed problems where you identify the case first. Connect to the identities from precalculus.

## Common Misconceptions
- Applying the wrong strategy (e.g., using power-reduction when an odd exponent allows a simpler substitution).
- Making errors in the Pythagorean identity substitution (sin^2 = 1 - cos^2 vs. cos^2 = 1 - sin^2).
- Forgetting the reduction formulas for higher powers of secant.
