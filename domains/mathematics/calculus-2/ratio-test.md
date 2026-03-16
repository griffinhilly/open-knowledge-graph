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

## Explainer

The ratio test is built on a single insight: if a series eventually behaves like a geometric series, its convergence is determined by the common ratio. You already know from geometric series that Σ rⁿ converges when |r| < 1 and diverges when |r| > 1. The ratio test asks whether the ratio of consecutive terms settles toward some limiting value L as n grows — and if it does, the series converges or diverges exactly like the geometric series with ratio L.

The mechanics: compute the ratio |a_{n+1}/a_n| and take the limit as n → ∞. If L < 1, terms eventually shrink faster than a convergent geometric series, so the series converges absolutely. If L > 1, terms grow, so the series diverges. If L = 1, the test gives no information — terms shrink, but not fast enough to guarantee convergence (p-series like Σ 1/n all give L = 1 despite having different convergence behaviors).

The test shines when **factorials or exponentials** appear in the terms, because the ratio of consecutive terms simplifies beautifully. For Σ n!/nⁿ, computing (n+1)!/(n+1)^(n+1) divided by n!/nⁿ gives (n+1)·n! / ((n+1)·(n+1)ⁿ) · nⁿ/n! = (n/(n+1))ⁿ → 1/e < 1, so the series converges. The key algebraic fact to drill: **(n+1)! = (n+1)·n!**, which lets you cancel the n! cleanly. Similarly, for series involving both exponentials and factorials like Σ 2ⁿ/n!, the ratio is 2^(n+1)/(n+1)! · n!/2ⁿ = 2/(n+1) → 0 < 1, confirming convergence.

The ratio test becomes inconclusive — giving L = 1 — for power-law series like Σ 1/nᵖ or Σ 1/(n ln n). For these, use the integral test or comparison test instead. A useful mental rule: **reach for the ratio test when you see n! or aⁿ; reach for the integral test when you see rational functions of n**. The ratio test's other major application is finding the **radius of convergence** of a power series Σ cₙxⁿ — there, you apply it to the absolute value of the terms, treating x as a parameter, and solve for the values of x where L < 1.
