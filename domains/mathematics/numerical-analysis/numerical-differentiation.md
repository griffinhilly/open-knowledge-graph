---
id: numerical-differentiation
title: Numerical Differentiation
domain: mathematics
course: numerical-analysis
prerequisites:
- id: taylor-series
  type: hard
- id: rounding-errors
  type: hard
builds-toward:
- richardson-extrapolation
tags:
- differentiation
- finite-difference
- numerical
stage: formal-systems
status: draft
---

# Numerical Differentiation

## Core Idea
Numerical differentiation approximates f'(x) using finite differences: forward (f(x+h)-f(x))/h, backward (f(x)-f(x-h))/h, or centered (f(x+h)-f(x-h))/(2h). Taylor analysis shows centered differences have O(h²) truncation error but are sensitive to rounding errors for very small h. Choosing h requires balancing truncation and rounding error—typically h ≈ √(machine epsilon).

## Explainer

The derivative f'(x) is defined as the limit of difference quotients as h → 0. In numerical work, h cannot actually reach zero — you can only evaluate f at specific points. **Numerical differentiation** is the art of choosing h small enough to get a good approximation, but not so small that floating-point errors dominate. Your two prerequisites — Taylor series and rounding errors — are precisely the tools needed to analyze this tension.

The **forward difference** (f(x+h) − f(x))/h is the simplest approximation. Taylor-expanding f(x+h) = f(x) + h f'(x) + h²/2 f''(x) + ⋯ and rearranging shows the error is (h/2) f''(x) + O(h²) — this is the **truncation error**, which shrinks as h → 0. But as h decreases, the numerator f(x+h) − f(x) becomes the difference of two nearly equal numbers. From your study of rounding errors, you know this **catastrophic cancellation** amplifies relative errors: if f(x) and f(x+h) agree to k decimal digits, their difference has k fewer correct digits. The result is that rounding error in the derivative grows like ε_machine / h as h → 0.

The total error is the sum of two opposing forces: truncation error (∝ h) decreasing as h → 0, and rounding error (∝ ε_machine / h) increasing as h → 0. The optimal h minimizes their sum, giving h_opt ≈ √(ε_machine) ≈ 10⁻⁸ for double precision, with a minimum total error of about √(ε_machine) ≈ 10⁻⁸. This is a fundamental limit — you cannot do better with simple forward differences.

The **centered difference** (f(x+h) − f(x−h))/(2h) uses a Taylor argument to show the error is −h²/6 f'''(x) + O(h⁴) — the O(h) term cancels because the formula is symmetric. This gives O(h²) truncation error (much better than O(h) for the forward difference), with optimal h ≈ ε_machine^{1/3} ≈ 10⁻⁵ and minimum error ≈ ε_machine^{2/3} ≈ 10⁻¹¹. The lesson is that **symmetry buys a full order of accuracy for free** — the key insight behind Richardson extrapolation, which pushes even further by combining evaluations at multiple step sizes. For second derivatives, a centered formula gives (f(x+h) − 2f(x) + f(x−h))/h², again derived directly from Taylor series, but with a worse rounding error floor because it subtracts three terms.
