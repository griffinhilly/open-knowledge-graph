---
id: integral-test
title: Integral Test
domain: mathematics
course: calculus-2
prerequisites:
  - id: improper-integrals-convergence
    type: hard
  - id: divergence-test
    type: hard
builds-toward:
  - comparison-test
  - p-series
tags: [series, convergence-tests, integral-test]
stage: formal-systems
status: validated
---

# Integral Test

## Core Idea
The Integral Test states that if f(x) is positive, continuous, and decreasing for x >= 1, and a_n = f(n), then the series sum of a_n and the improper integral of f(x) from 1 to infinity either both converge or both diverge. The test does not give the sum, only the convergence behavior. It is used to prove the p-series convergence criterion and to estimate series sums via integral bounds.

## How It's Best Learned
Visualize the connection: the series is a left Riemann sum for the integral (or vice versa). Apply to prove p-series convergence/divergence. Practice checking the three conditions (positive, continuous, decreasing). Use the integral remainder estimate to bound the error of partial sums.

## Common Misconceptions
- Applying the integral test when f is not eventually decreasing.
- Believing the integral gives the exact sum of the series (it only matches convergence/divergence behavior).
- Confusing the integral test with evaluating the series by integration.

## Questions

```yaml
- question: "You apply the integral test and find that ∫₁^∞ f(x)dx = 7. What can you conclude about the series Σ f(n)?"
  type: multiple-choice
  options:
    - "The series converges and its sum equals 7"
    - "The series converges, but its sum is not necessarily 7"
    - "The series diverges because the integral value must match the series sum exactly"
    - "Nothing — the integral test only applies when the integral diverges"
  answer: 1
  explanation: "The integral test tells you only whether the series converges or diverges — it does not give the series' sum. If the improper integral converges (finite value), the series also converges; if the integral diverges, so does the series. But the integral's value (7) is not the series' sum — they differ by a finite amount bounded by f(1). For example, ∫₁^∞ 1/x² dx = 1 but Σ 1/n² = π²/6 ≈ 1.645. The most common mistake is treating the integral test as computing the series value."

- question: "Which series does the integral test most directly establish as convergent?"
  type: multiple-choice
  options:
    - "Σ (-1)ⁿ/n — alternating terms, not always positive"
    - "Σ 1/n² — positive, continuous, decreasing; ∫₁^∞ 1/x² dx converges"
    - "Σ n·sin(n) — oscillating, not eventually monotone decreasing"
    - "Σ 1/n — the harmonic series, whose integral also diverges"
  answer: 1
  explanation: "For Σ 1/n², set f(x) = 1/x². This function is positive, continuous, and decreasing on [1, ∞). The integral ∫₁^∞ 1/x² dx = [-1/x]₁^∞ = 1, which converges, so the series converges. Σ (-1)ⁿ/n fails the positivity condition (the integral test requires non-negative terms). Σ n·sin(n) is not monotone decreasing. Σ 1/n satisfies the conditions but has a divergent integral (∫₁^∞ 1/x dx diverges), making it an example of divergence, not convergence."

- question: "If ∫₁^∞ f(x)dx converges to a finite value L, then Σ f(n) also converges to L."
  type: true-false
  answer: false
  explanation: "The integral test establishes only that the series and integral share the same convergence behavior — both converge or both diverge. Their numerical values are almost never equal. The rectangle picture makes this clear: the series terms aₙ = f(n) are rectangle areas that differ from the integral by a finite amount (bounded above by f(1) in typical estimates). For example, ∫₁^∞ 1/x² dx = 1 while Σ 1/n² = π²/6 ≈ 1.645. Confusing the integral's value with the series' sum is the single most common misapplication of this test."

- question: "The integral test can be applied to determine convergence of Σ sin(n)/n² because f(x) = sin(x)/x² is eventually decreasing."
  type: true-false
  answer: false
  explanation: "The integral test requires f to be positive (as well as continuous and decreasing). The function sin(x)/x² takes negative values whenever sin(x) < 0, so the positivity condition fails. Without positivity, the rectangle-to-curve comparison breaks down: rectangles below the x-axis would subtract from the sum rather than add, and the geometric argument for convergence equivalence no longer holds. For series with sign changes, the alternating series test or absolute convergence approach is more appropriate."

- question: "Explain geometrically why a series Σ f(n) and the improper integral ∫₁^∞ f(x)dx share the same convergence behavior when f is positive, continuous, and decreasing."
  type: short-answer
  answer: "Draw the graph of f and place rectangles of width 1 over each integer n, with height f(n). Because f is decreasing, each rectangle on [n, n+1] with height f(n) lies above the curve, making the series an overestimate of the integral: ∫₁^∞ f(x)dx ≤ Σ_{n=1}^∞ f(n). Using heights f(n+1) instead gives rectangles below the curve: Σ_{n=2}^∞ f(n) ≤ ∫₁^∞ f(x)dx. These two inequalities sandwich the integral between two shifted versions of the series, showing they differ by at most a finite amount (f(1)). Therefore, if one diverges to infinity, the other must too; if one is bounded, the other is as well."
  explanation: "The decreasing condition is essential: it ensures the rectangle at n lies consistently above (or below) the curve on [n, n+1], giving a one-sided bound. Without monotone decrease, the rectangle could cross the curve, and you could no longer bound the series from one side by the integral. This is why 'eventually decreasing' is sufficient — behavior at finitely many early terms contributes only a finite amount and cannot affect convergence."
```

## Explainer

You already know two things this test connects: improper integrals (summing continuous area to infinity) and infinite series (summing discrete terms). The integral test says these two summation processes share the same fate — either both converge or both diverge — when the terms come from a function that is positive, continuous, and decreasing.

The geometric picture makes this clear. Suppose f is a decreasing positive function and aₙ = f(n). Draw the graph of f and superimpose rectangles of width 1 centered at each integer. The rectangle at n has height f(n) = aₙ, so its area equals the n-th term of the series. Now compare the rectangles to the area under the curve. Because f is decreasing, each rectangle between n and n+1 lies either above or below the curve, depending on which edge you use. If the rectangle height is f(n), the rectangle is above the curve on [n, n+1], so the series is an **overestimate** of the integral. If you use f(n+1) instead, it is an underestimate. Sandwiching the integral between two shifted versions of the series shows that the integral and the series differ by at most a finite amount — so they share the same convergence behavior.

The three conditions matter. If f is not **positive**, the comparison to area breaks down. If f is not **continuous**, the Riemann sum interpretation fails. If f is not **decreasing**, the rectangle-to-curve comparison can reverse, and the integral no longer bounds the series in a useful way. In practice, "eventually decreasing" is enough — behavior at finitely many early terms does not affect convergence.

The integral test's most important application is the **p-series**: the series Σ 1/nᵖ converges if and only if p > 1. Using f(x) = 1/xᵖ, the improper integral ∫₁^∞ 1/xᵖ dx equals 1/(p−1) when p > 1 (converges) and diverges when p ≤ 1. The integral test carries this result directly to the series. The p-series criterion then becomes a benchmark for the comparison tests you will study next — when you encounter a new series, asking "does it behave like 1/nᵖ for some p?" is often the first diagnostic step.
