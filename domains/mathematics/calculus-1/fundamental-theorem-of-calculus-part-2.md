---
id: fundamental-theorem-of-calculus-part-2
title: Fundamental Theorem of Calculus Part 2
domain: mathematics
course: calculus-1
prerequisites:
- id: fundamental-theorem-of-calculus-part-1
  type: hard
- id: antiderivatives
  type: hard
- id: indefinite-integrals
  type: soft
builds-toward:
- u-substitution
- area-between-curves
tags:
- integration
- FTC
- evaluation
stage: formal-systems
status: validated
---
# Fundamental Theorem of Calculus Part 2

## Core Idea
FTC Part 2 (the Evaluation Theorem) states that if F is any antiderivative of f on [a, b], then the integral from a to b of f(x) dx = F(b) - F(a). This transforms the problem of computing a definite integral from a limit of Riemann sums (hard) into finding an antiderivative and evaluating at the endpoints (often easy). This is the most computationally powerful theorem in introductory calculus.

## How It's Best Learned
Evaluate definite integrals using the notation F(x) evaluated from a to b = F(b) - F(a). Practice with polynomial, trigonometric, and exponential integrands. Compare with Riemann sum approximations to verify. Emphasize that the +C cancels out in definite integrals.

## Common Misconceptions
- Computing F(a) - F(b) instead of F(b) - F(a) (order matters for the sign).
- Including +C in definite integral evaluations (it cancels).
- Assuming FTC Part 2 applies even when f has discontinuities on [a, b] (it requires continuity or at worst finitely many removable discontinuities).
