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

## Questions

```yaml
- question: "Evaluate ∫₁⁴ 3x² dx using FTC Part 2. What is the correct answer?"
  type: multiple-choice
  options:
    - "192 — computed as F(1) - F(4) where F(x) = x³"
    - "63 — computed as F(4) - F(1) where F(x) = x³"
    - "63 + C — the constant of integration must be retained"
    - "−63 — computed as F(1) - F(4)"
  answer: 1
  explanation: "The antiderivative of 3x² is x³. FTC Part 2 gives [x³]₁⁴ = 4³ - 1³ = 64 - 1 = 63. Option C incorrectly includes +C — in definite integrals, the constant cancels: (F(b) + C) - (F(a) + C) = F(b) - F(a). Options A and D reverse the order to F(a) - F(b), giving a negative result. Order matters: it is always F(b) - F(a), upper limit minus lower limit."

- question: "A student evaluates ∫₀² x³ dx and gets −4, reasoning that F(0) - F(2) = 0 - 4 = -4 where F(x) = x⁴/4. What went wrong?"
  type: multiple-choice
  options:
    - "The antiderivative is wrong — the correct antiderivative of x³ is 3x²"
    - "The order of subtraction is reversed — FTC Part 2 requires F(b) - F(a), not F(a) - F(b)"
    - "The student should have used a Riemann sum to verify the result"
    - "The student forgot to include +C before evaluating at the endpoints"
  answer: 1
  explanation: "The antiderivative F(x) = x⁴/4 is correct, but FTC Part 2 requires F(b) - F(a): F(2) - F(0) = 16/4 - 0 = 4. The student computed F(a) - F(b) = F(0) - F(2) = -4. Reversing the limits changes the sign of the definite integral. This is one of the most common computational errors in applying FTC Part 2 — the direction of integration (lower limit to upper limit) is encoded in the subtraction order."

- question: "When applying FTC Part 2, you is expected to use the specific antiderivative that satisfies F(a) = 0; otherwise the formula gives an incorrect answer."
  type: true-false
  answer: false
  explanation: "Any antiderivative works. If F and G are both antiderivatives of f, they differ by a constant: G(x) = F(x) + C. Then G(b) - G(a) = [F(b) + C] - [F(a) + C] = F(b) - F(a). The constant C cancels regardless of its value. This is why you don't write '+C' in definite integral evaluations and why choosing the simplest antiderivative (C = 0) is always valid."

- question: "FTC Part 2 is a computational shortcut that approximates the definite integral; using Riemann sums would give a more exact result."
  type: true-false
  answer: false
  explanation: "FTC Part 2 gives the exact value of the definite integral — not an approximation. Riemann sums are approximations that approach the exact integral only in the limit as the number of rectangles approaches infinity. FTC Part 2 is the theorem that establishes the exact equality between the definite integral and the antiderivative evaluation — it doesn't shortcut around precision, it provides it."

- question: "Why does the constant of integration (+C) disappear when applying FTC Part 2 to evaluate a definite integral?"
  type: short-answer
  answer: "Because it cancels algebraically. Any antiderivative F of f differs from any other by a constant C. When you compute F(b) - F(a), you get [G(b) + C] - [G(a) + C] = G(b) - G(a), and C vanishes. Every valid antiderivative therefore produces the same value for the definite integral, which is why you can freely choose the most convenient one and omit +C from definite integral calculations."
  explanation: "This cancellation reflects a deep property of the definite integral: it measures a net quantity (area, displacement, accumulated change) that is independent of where you set the 'zero point' of the antiderivative. Shifting the antiderivative up or down by C shifts both F(b) and F(a) by the same amount, so the difference is unchanged. Recognizing this makes the formula intuitive — the constant represents where you started counting, and starting from a different point doesn't change how much accumulates between a and b."
```

## Explainer

From FTC Part 1, you learned that the accumulation function A(x) = ∫_a^x f(t) dt is an antiderivative of f — differentiating the integral recovers the integrand. FTC Part 2 is the payoff: it gives you a practical method to *evaluate* that integral. If F is any antiderivative of f on [a, b] — meaning F'(x) = f(x) — then ∫_a^b f(x) dx = F(b) − F(a). The definite integral, which was defined as a limit of Riemann sums (a painful computation), reduces to two function evaluations and a subtraction.

To see why this works, recall from Part 1 that A(x) = ∫_a^x f(t) dt is one antiderivative of f. Any other antiderivative F of f differs from A by a constant: F(x) = A(x) + C for some C. Now compute F(b) − F(a): you get [A(b) + C] − [A(a) + C] = A(b) − A(a). Since A(a) = ∫_a^a f(t) dt = 0, this simplifies to A(b) = ∫_a^b f(t) dt. The constant C cancels regardless of which antiderivative you choose — this is why you do not write "+C" when evaluating definite integrals, and why any correct antiderivative gives the same answer.

In practice, the standard notation is [F(x)]_a^b = F(b) − F(a), evaluated after finding F. For example, ∫_0^3 x² dx = [x³/3]_0^3 = 27/3 − 0 = 9. No limits, no rectangles — just one antiderivative and two evaluations. This efficiency is what makes the theorem so powerful. Every rule you know for finding antiderivatives (power rule, trig integrals, exponentials) becomes a tool for evaluating definite integrals. The upcoming techniques of u-substitution and integration by parts will further extend your antiderivative toolkit, and FTC Part 2 converts each new technique directly into a method for computing areas, accumulated quantities, and net change.

One subtlety: the theorem requires f to be continuous (or nearly so) on [a, b]. If f has a jump discontinuity inside the interval, the antiderivative F may not be differentiable at that point, and the simple subtraction formula can give a wrong answer. When you encounter piecewise or discontinuous integrands, split the integral at the discontinuity and apply FTC Part 2 to each piece separately.
