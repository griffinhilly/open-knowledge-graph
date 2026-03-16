---
id: geometric-series
title: Geometric Series
domain: mathematics
course: calculus-2
prerequisites:
- id: series-definition-and-partial-sums
  type: hard
- id: sequences-and-series-review
  type: hard
- id: geometric-sequences
  type: soft
builds-toward:
- power-series
- radius-and-interval-of-convergence
tags:
- series
- geometric
- convergence
stage: formal-systems
status: validated
---
# Geometric Series

## Core Idea
A geometric series has the form sum from n=0 to infinity of a*r^n = a/(1 - r), converging if and only if |r| < 1. It is the most important series because it has a known closed-form sum, serves as a benchmark for comparison tests, and is the basis for power series and Taylor series. The partial sum formula S_N = a(1 - r^N)/(1 - r) shows exactly how the series converges.

## How It's Best Learned
Derive the partial sum formula by multiplying S_N by r and subtracting. Take the limit as N -> infinity to get the infinite sum. Practice identifying geometric series in various forms (e.g., sum of (2/3)^n, sum of (-1)^n / 4^n). Apply to repeating decimals and real-world scenarios.

## Common Misconceptions
- Applying the formula when |r| >= 1 (the series diverges in this case).
- Off-by-one errors on the starting index (the formula changes if the series starts at n = 1 vs. n = 0).
- Not recognizing a geometric series when it is written in a non-standard form.

## Questions

```yaml
- question: "What is the sum of the geometric series sum_{n=1}^∞ (1/3)^n?"
  type: multiple-choice
  options: ["3/2", "1", "1/2", "3"]
  answer: 2
  explanation: "Starting at n=1 means the first term is (1/3)^1 = 1/3, not 1. So a = 1/3 and r = 1/3, giving sum = (1/3)/(1 - 1/3) = (1/3)/(2/3) = 1/2. A very common error is to use a = 1 (the n=0 term), which gives 3/2 — this is the off-by-one index mistake."

- question: "A geometric series with ratio r = -0.5 converges because |-0.5| < 1."
  type: true-false
  answer: true
  explanation: "The convergence condition is |r| < 1, which applies to negative ratios as well. Here |-0.5| = 0.5 < 1, so the series converges to a/(1-r) = a/1.5. Negative ratios produce alternating series that still converge as long as the terms shrink to zero."

- question: "Use the geometric series formula to express the repeating decimal 0.777... as a fraction."
  type: short-answer
  answer: "7/9. Write 0.777... = 7/10 + 7/100 + 7/1000 + ... This is a geometric series with a = 7/10 and r = 1/10, so the sum is (7/10)/(1 - 1/10) = (7/10)/(9/10) = 7/9."
  explanation: "Every repeating decimal is a geometric series in disguise. Identifying a and r and checking |r| < 1 converts the infinite decimal to a ratio of integers. This is one of the clearest real-world applications of the convergence formula."
```

## Explainer

A geometric series is one where each term is obtained by multiplying the previous one by a fixed ratio r. You already know geometric sequences from earlier work; a geometric series is simply the sum of such a sequence. The central question is: when you add infinitely many terms, can the total be finite?

The answer depends entirely on |r|. To see why, consider the partial sum S_N = a + ar + ar² + ... + ar^N. Multiply both sides by r: rS_N = ar + ar² + ... + ar^(N+1). Subtract the second equation from the first and almost everything cancels, leaving S_N(1 - r) = a(1 - r^N), so S_N = a(1 - r^N)/(1 - r). As N → ∞, the term r^N → 0 only when |r| < 1 — when r is a fraction between -1 and 1. In that case the infinite sum collapses to the clean formula a/(1 - r). If |r| ≥ 1, the terms don't shrink and the sum grows without bound.

The starting index matters more than students expect. The formula a/(1 - r) uses the first term actually in the sum as a. If your series starts at n = 0, the first term is a·r⁰ = a. If it starts at n = 1, the first term is a·r¹. Plugging in the wrong first term is the most frequent source of errors, so always identify a by evaluating the term at the lowest index before applying the formula.

Geometric series are foundational to the rest of Calculus 2 because power series — and ultimately Taylor series — are geometric series with r replaced by a variable expression. The radius of convergence of a power series is precisely the set of x-values for which the underlying geometric series converges. Every Taylor series you will encounter is, in a structural sense, built on the geometric series formula. Getting comfortable recognizing and summing geometric series now will pay dividends through the end of the course.
