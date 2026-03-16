---
id: p-series
title: P-Series
domain: mathematics
course: calculus-2
prerequisites:
- id: series-definition-and-partial-sums
  type: hard
- id: improper-integrals-convergence
  type: hard
- id: integral-test
  type: soft
builds-toward:
- comparison-test
- limit-comparison-test
tags:
- series
- p-series
- convergence
- benchmark
stage: formal-systems
status: validated
---
# P-Series

## Core Idea
A p-series is sum from n=1 to infinity of 1/n^p. It converges if p > 1 and diverges if p <= 1. The case p = 1 is the harmonic series, the most famous divergent series. The convergence boundary at p = 1 matches the p-integral test and serves as the primary benchmark for comparison tests. Knowing p-series convergence is essential for all subsequent convergence tests.

## How It's Best Learned
Prove convergence/divergence using the integral test (integral of 1/x^p). Study the harmonic series carefully to understand why terms going to zero is not sufficient for convergence. Use p-series as comparison benchmarks for other series.

## Common Misconceptions
- Believing the harmonic series converges because 1/n -> 0 (this is the classic trap).
- Confusing p-series with geometric series (p-series has n in the base, geometric has n in the exponent).
- Not remembering whether p > 1 converges or diverges (think: the integral of 1/x^2 from 1 to infinity converges).

## Explainer

From your work with series, you know that convergence asks whether the infinite sum of a sequence of terms adds up to a finite number. From improper integrals, you know that ∫₁^∞ 1/x^p dx converges when p > 1 and diverges when p ≤ 1 — this is a boundary you calculated explicitly. The **p-series** ∑ 1/n^p mirrors this exactly, and that's not a coincidence: it's because the integral test directly connects the two. The integral test says that ∑f(n) and ∫f(x) dx converge or diverge together for positive, decreasing f. Since f(x) = 1/x^p is exactly that kind of function, the series and integral share the same fate at the same boundary: **p-series converges if and only if p > 1**.

The most important special case is p = 1, the **harmonic series**: 1 + 1/2 + 1/3 + 1/4 + .... This diverges, and it is the canonical example that demolishes the intuition "if the terms go to zero, the series converges." The terms 1/n do go to zero, yet the sum grows without bound. The divergence is very slow — the partial sums only grow like ln(n) — but they do grow forever. The standard proof groups the terms: the 2nd term is ≥ 1/2, the 3rd and 4th terms together are ≥ 1/4 + 1/4 = 1/2, the next four terms are ≥ 1/2, and so on. Each doubling block contributes at least 1/2, so the sum is unbounded. Knowing this failure of a seemingly reasonable test is essential for understanding why the full arsenal of convergence tests is necessary.

When p > 1, the series converges, and the convergence improves as p increases. The series ∑ 1/n² converges (its sum is π²/6, a famous result), ∑ 1/n³ converges to a smaller value, and so on. When p ≤ 0, the terms don't even go to zero, so divergence is immediate by the divergence test. The boundary is precisely p = 1: just below it (like p = 0.99), the terms go to zero but too slowly to converge; just above it (like p = 1.01), the terms go to zero fast enough that the partial sums have a finite limit.

The practical reason to master p-series is that they serve as **benchmark comparisons** for the comparison tests you'll use next. When you encounter a series like ∑ 1/(n² + 3n), you compare it to ∑ 1/n² (which converges, p = 2) or ∑ 1/√n (which diverges, p = 1/2). If your series is eventually smaller than a convergent p-series, it converges; if it's eventually larger than a divergent one, it diverges. P-series are the reference standards of the comparison test world — knowing their behavior by heart transforms every subsequent convergence analysis into a pattern-matching exercise.
