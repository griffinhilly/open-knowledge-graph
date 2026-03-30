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
stage: advanced
status: validated
---

# Numerical Differentiation

## Core Idea
Numerical differentiation approximates f'(x) using finite differences: forward (f(x+h)-f(x))/h, backward (f(x)-f(x-h))/h, or centered (f(x+h)-f(x-h))/(2h). Taylor analysis shows centered differences have O(h²) truncation error but are sensitive to rounding errors for very small h. Choosing h requires balancing truncation and rounding error—typically h ≈ √(machine epsilon).

## Questions

```yaml
- question: "A programmer wants the most accurate numerical estimate of f'(x) and chooses h = 10⁻¹⁵, reasoning that smaller h means closer to the limit definition. What actually happens?"
  type: multiple-choice
  options:
    - "The estimate improves dramatically because h is nearly zero"
    - "The estimate degrades because catastrophic cancellation in f(x+h) − f(x) amplifies rounding error, overwhelming any gain from smaller truncation error"
    - "The estimate is unchanged because floating-point arithmetic handles small differences correctly"
    - "The truncation error increases when h drops below the optimal value"
  answer: 1
  explanation: "For double precision (ε_machine ≈ 10⁻¹⁶), the rounding error in the derivative grows as ε_machine/h. At h = 10⁻¹⁵, rounding error ≈ 10⁻¹⁶/10⁻¹⁵ = 0.1 — catastrophically large. The numerator f(x+h) − f(x) involves subtracting two nearly equal floating-point numbers, a process that destroys significant digits. Making h smaller than the optimal h_opt ≈ √(ε_machine) ≈ 10⁻⁸ makes things worse, not better."

- question: "Why does the centered difference formula (f(x+h) − f(x−h))/(2h) have O(h²) truncation error while the forward difference (f(x+h) − f(x))/h has only O(h)?"
  type: multiple-choice
  options:
    - "The centered formula uses twice as many function evaluations, which averages out errors"
    - "The symmetric form causes the O(h) terms in the Taylor expansions to cancel, leaving only O(h²) terms"
    - "The factor of 2h in the denominator reduces truncation error by a factor of 2"
    - "The centered formula avoids catastrophic cancellation entirely"
  answer: 1
  explanation: "Taylor-expanding f(x+h) gives f(x) + hf'(x) + (h²/2)f''(x) + (h³/6)f'''(x) + ⋯, and f(x−h) gives f(x) − hf'(x) + (h²/2)f''(x) − (h³/6)f'''(x) + ⋯. Subtracting: f(x+h) − f(x−h) = 2hf'(x) + (2h³/6)f'''(x) + ⋯. Dividing by 2h: f'(x) + (h²/6)f'''(x) + ⋯. The h² terms from each expansion cancelled exactly because the formula is symmetric. This is 'symmetry buys accuracy for free.'"

- question: "For numerical differentiation, using a step size h smaller than the optimal value increases total error rather than decreasing it."
  type: true-false
  answer: true
  explanation: "Total error = truncation error + rounding error. Truncation error decreases as h → 0 (proportional to h for forward differences), but rounding error increases as h → 0 (proportional to ε_machine/h). The sum has a minimum at the optimal h. Below this optimal value, rounding error dominates and the total error rises. This is the fundamental tradeoff of numerical differentiation."

- question: "Making the step size h as small as possible generally produces the most accurate numerical derivative."
  type: true-false
  answer: false
  explanation: "This is the central misconception. Very small h causes catastrophic cancellation: f(x+h) and f(x) become nearly equal floating-point numbers, and their difference loses significant digits. The rounding error in the derivative then grows as ε_machine/h, increasing without bound as h → 0. The optimal h balances truncation error against rounding error, giving h_opt ≈ √(ε_machine) ≈ 10⁻⁸ for forward differences."

- question: "Explain the two competing sources of error in numerical differentiation and why they create an optimal step size h."
  type: short-answer
  answer: "Truncation error arises because the finite-difference formula approximates the derivative using only finitely many terms of a Taylor expansion — the omitted higher-order terms contribute error proportional to h (for forward differences) or h² (for centered). Rounding error arises from floating-point arithmetic: as h shrinks, f(x+h) and f(x) become nearly equal, and their subtraction destroys significant digits through catastrophic cancellation, producing error proportional to ε_machine/h. Truncation error decreases as h → 0 while rounding error increases, so their sum has a minimum at an optimal h that balances both."
  explanation: "The optimal h_opt ≈ √(ε_machine) for forward differences and ≈ ε_machine^(1/3) for centered differences. Below this value, rounding dominates; above it, truncation dominates. This is a fundamental computational limit — you cannot beat it without more sophisticated methods like Richardson extrapolation."
```

## Explainer

The derivative f'(x) is defined as the limit of difference quotients as h → 0. In numerical work, h cannot actually reach zero — you can only evaluate f at specific points. **Numerical differentiation** is the art of choosing h small enough to get a good approximation, but not so small that floating-point errors dominate. Your two prerequisites — Taylor series and rounding errors — are precisely the tools needed to analyze this tension.

The **forward difference** (f(x+h) − f(x))/h is the simplest approximation. Taylor-expanding f(x+h) = f(x) + h f'(x) + h²/2 f''(x) + ⋯ and rearranging shows the error is (h/2) f''(x) + O(h²) — this is the **truncation error**, which shrinks as h → 0. But as h decreases, the numerator f(x+h) − f(x) becomes the difference of two nearly equal numbers. From your study of rounding errors, you know this **catastrophic cancellation** amplifies relative errors: if f(x) and f(x+h) agree to k decimal digits, their difference has k fewer correct digits. The result is that rounding error in the derivative grows like ε_machine / h as h → 0.

The total error is the sum of two opposing forces: truncation error (∝ h) decreasing as h → 0, and rounding error (∝ ε_machine / h) increasing as h → 0. The optimal h minimizes their sum, giving h_opt ≈ √(ε_machine) ≈ 10⁻⁸ for double precision, with a minimum total error of about √(ε_machine) ≈ 10⁻⁸. This is a fundamental limit — you cannot do better with simple forward differences.

The **centered difference** (f(x+h) − f(x−h))/(2h) uses a Taylor argument to show the error is −h²/6 f'''(x) + O(h⁴) — the O(h) term cancels because the formula is symmetric. This gives O(h²) truncation error (much better than O(h) for the forward difference), with optimal h ≈ ε_machine^{1/3} ≈ 10⁻⁵ and minimum error ≈ ε_machine^{2/3} ≈ 10⁻¹¹. The lesson is that **symmetry buys a full order of accuracy for free** — the key insight behind Richardson extrapolation, which pushes even further by combining evaluations at multiple step sizes. For second derivatives, a centered formula gives (f(x+h) − 2f(x) + f(x−h))/h², again derived directly from Taylor series, but with a worse rounding error floor because it subtracts three terms.
