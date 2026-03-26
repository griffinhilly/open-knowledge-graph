---
id: ratio-test
title: Ratio Test
domain: mathematics
course: calculus-2
prerequisites:
  - id: geometric-series
    type: hard
  - id: sequences-convergence
    type: hard
builds-toward:
  - radius-and-interval-of-convergence
  - absolute-vs-conditional-convergence
tags: [series, convergence-tests, ratio-test]
stage: formal-systems
status: validated
---

# Ratio Test

## Core Idea
The Ratio Test examines L = lim(n->infinity) |a_(n+1)/a_n|. If L < 1, the series converges absolutely. If L > 1, the series diverges. If L = 1, the test is inconclusive. The ratio test is particularly effective for series involving factorials (n!) and exponentials (r^n), where the ratio of consecutive terms simplifies nicely. It is also the key tool for finding the radius of convergence of power series.

## How It's Best Learned
Apply to series with factorials and exponentials where the ratio simplifies. Compare with the geometric series (the ratio test essentially checks whether terms decrease geometrically in the limit). Practice recognizing when the test is inconclusive (p-series, for example) and switching to another test.

## Common Misconceptions
- Concluding convergence or divergence when L = 1 (the test is inconclusive).
- Computing the ratio incorrectly, especially with factorials ((n+1)! = (n+1)*n!).
- Applying the ratio test to series where it is inconclusive when a simpler test would work.

## Questions

```yaml
- question: "You apply the ratio test to a series and find L = lim(n→∞) |a_{n+1}/a_n| = 1. What can you conclude?"
  type: multiple-choice
  options:
    - "The series converges, since L is not greater than 1"
    - "The series diverges, since L equals 1 and terms do not shrink"
    - "The test is inconclusive — the series may converge or diverge"
    - "The series converges absolutely"
  answer: 2
  explanation: "L = 1 is the inconclusive case. The ratio test cannot distinguish between convergence and divergence when L = 1. For example, both Σ 1/n (diverges) and Σ 1/n² (converges) give L = 1. This is the most important exception to memorize: L < 1 → absolute convergence; L > 1 → divergence; L = 1 → no information."

- question: "For which series would the ratio test be the most natural and effective choice?"
  type: multiple-choice
  options:
    - "Σ 1/n² — a p-series where terms decay as a power function"
    - "Σ 2ⁿ/n! — a series involving both an exponential and a factorial"
    - "Σ 1/(n ln n) — a series needing the integral test"
    - "Σ (-1)ⁿ/n — a series best handled by the alternating series test"
  answer: 1
  explanation: "The ratio test excels when terms involve factorials (n!) or exponentials (aⁿ), because the ratio a_{n+1}/a_n simplifies beautifully. For Σ 2ⁿ/n!, the ratio is 2^(n+1)/(n+1)! ÷ 2ⁿ/n! = 2/(n+1) → 0 < 1, so it converges. P-series and logarithmic series give L = 1 (inconclusive), and the alternating series test is more direct for alternating signs."

- question: "The ratio test works by checking whether a series eventually behaves like a convergent or divergent geometric series."
  type: true-false
  answer: true
  explanation: "This is the underlying logic. The ratio test computes L = lim |a_{n+1}/a_n|. If L < 1, terms eventually decrease faster than a geometric series with ratio L (which converges). If L > 1, terms eventually grow like a geometric series with ratio L > 1 (which diverges). The test is literally asking: 'What geometric series does this series asymptotically resemble?'"

- question: "If the ratio test gives L = 1 for a series, that series is expected to converge slowly but steadily."
  type: true-false
  answer: false
  explanation: "L = 1 is inconclusive — the series may converge or diverge. Σ 1/n gives L = 1 and diverges; Σ 1/n² gives L = 1 and converges; Σ 1/(n ln n) gives L = 1 and diverges. L = 1 provides no information. Interpreting L = 1 as 'borderline convergence' is a fundamental misunderstanding of the test's scope."

- question: "When applying the ratio test to a series involving n!, what algebraic identity is essential, and why does it make the factorial term tractable?"
  type: short-answer
  answer: "(n+1)! = (n+1) · n!. This allows the (n+1)! in the numerator of the ratio to cancel with n! in the denominator, leaving only the factor (n+1). Without this identity, the factorial in the ratio would not simplify cleanly."
  explanation: "For example, in Σ n!/nⁿ, the ratio is [(n+1)!/(n+1)^(n+1)] / [n!/nⁿ]. Applying (n+1)! = (n+1)·n! lets you write this as (n+1)·n! / ((n+1)·(n+1)ⁿ) · nⁿ/n! = (n/(n+1))ⁿ → 1/e < 1. The ability to cancel the factorial is the entire reason the ratio test is the right tool for factorial-containing series."
```

## Explainer

The ratio test is built on a single insight: if a series eventually behaves like a geometric series, its convergence is determined by the common ratio. You already know from geometric series that Σ rⁿ converges when |r| < 1 and diverges when |r| > 1. The ratio test asks whether the ratio of consecutive terms settles toward some limiting value L as n grows — and if it does, the series converges or diverges exactly like the geometric series with ratio L.

The mechanics: compute the ratio |a_{n+1}/a_n| and take the limit as n → ∞. If L < 1, terms eventually shrink faster than a convergent geometric series, so the series converges absolutely. If L > 1, terms grow, so the series diverges. If L = 1, the test gives no information — terms shrink, but not fast enough to guarantee convergence (p-series like Σ 1/n all give L = 1 despite having different convergence behaviors).

The test shines when **factorials or exponentials** appear in the terms, because the ratio of consecutive terms simplifies beautifully. For Σ n!/nⁿ, computing (n+1)!/(n+1)^(n+1) divided by n!/nⁿ gives (n+1)·n! / ((n+1)·(n+1)ⁿ) · nⁿ/n! = (n/(n+1))ⁿ → 1/e < 1, so the series converges. The key algebraic fact to drill: **(n+1)! = (n+1)·n!**, which lets you cancel the n! cleanly. Similarly, for series involving both exponentials and factorials like Σ 2ⁿ/n!, the ratio is 2^(n+1)/(n+1)! · n!/2ⁿ = 2/(n+1) → 0 < 1, confirming convergence.

The ratio test becomes inconclusive — giving L = 1 — for power-law series like Σ 1/nᵖ or Σ 1/(n ln n). For these, use the integral test or comparison test instead. A useful mental rule: **reach for the ratio test when you see n! or aⁿ; reach for the integral test when you see rational functions of n**. The ratio test's other major application is finding the **radius of convergence** of a power series Σ cₙxⁿ — there, you apply it to the absolute value of the terms, treating x as a parameter, and solve for the values of x where L < 1.
