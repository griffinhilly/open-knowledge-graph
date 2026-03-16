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

## Explainer

From FTC Part 1, you learned that the accumulation function A(x) = ∫_a^x f(t) dt is an antiderivative of f — differentiating the integral recovers the integrand. FTC Part 2 is the payoff: it gives you a practical method to *evaluate* that integral. If F is any antiderivative of f on [a, b] — meaning F'(x) = f(x) — then ∫_a^b f(x) dx = F(b) − F(a). The definite integral, which was defined as a limit of Riemann sums (a painful computation), reduces to two function evaluations and a subtraction.

To see why this works, recall from Part 1 that A(x) = ∫_a^x f(t) dt is one antiderivative of f. Any other antiderivative F of f differs from A by a constant: F(x) = A(x) + C for some C. Now compute F(b) − F(a): you get [A(b) + C] − [A(a) + C] = A(b) − A(a). Since A(a) = ∫_a^a f(t) dt = 0, this simplifies to A(b) = ∫_a^b f(t) dt. The constant C cancels regardless of which antiderivative you choose — this is why you do not write "+C" when evaluating definite integrals, and why any correct antiderivative gives the same answer.

In practice, the standard notation is [F(x)]_a^b = F(b) − F(a), evaluated after finding F. For example, ∫_0^3 x² dx = [x³/3]_0^3 = 27/3 − 0 = 9. No limits, no rectangles — just one antiderivative and two evaluations. This efficiency is what makes the theorem so powerful. Every rule you know for finding antiderivatives (power rule, trig integrals, exponentials) becomes a tool for evaluating definite integrals. The upcoming techniques of u-substitution and integration by parts will further extend your antiderivative toolkit, and FTC Part 2 converts each new technique directly into a method for computing areas, accumulated quantities, and net change.

One subtlety: the theorem requires f to be continuous (or nearly so) on [a, b]. If f has a jump discontinuity inside the interval, the antiderivative F may not be differentiable at that point, and the simple subtraction formula can give a wrong answer. When you encounter piecewise or discontinuous integrands, split the integral at the discontinuity and apply FTC Part 2 to each piece separately.
