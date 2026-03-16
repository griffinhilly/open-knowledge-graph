---
id: geometric-sequences-and-series
title: Geometric Sequences and Series
domain: mathematics
course: algebra-2
prerequisites:
- id: arithmetic-sequences-and-series
  type: soft
- id: exponential-functions-and-graphs
  type: hard
builds-toward:
- sigma-notation
- binomial-theorem
- series-definition-and-partial-sums
tags:
- sequences
- series
- geometric
- common-ratio
stage: abstract-reasoning
status: validated
---
# Geometric Sequences and Series

## Core Idea
A geometric sequence has a constant ratio r between consecutive terms: a_n = a_1 * r^(n-1). The sum of the first n terms (geometric series) is S_n = a_1 * (1 - r^n)/(1 - r) for r != 1. If |r| < 1, the infinite geometric series converges to S = a_1/(1 - r). Geometric sequences model exponential growth and decay. The infinite series formula is foundational for calculus and finance.

## How It's Best Learned
Identify common ratios in sequences. Derive the finite sum formula by multiplying S_n by r and subtracting. Explore the infinite series by examining what happens as n grows when |r| < 1. Apply to compound interest, bouncing balls, and repeating decimals as infinite geometric series.

## Common Misconceptions
- Confusing common difference (arithmetic) with common ratio (geometric).
- Using the sum formula when r = 1 (division by zero; the sum is simply n*a_1).
- Applying the infinite series formula when |r| >= 1 (the series diverges).
- Sign errors in the sum formula when r is negative.

## Explainer

You already understand exponential functions: y = a · r^x, where a is the starting value and r is the growth (or decay) factor applied repeatedly. A **geometric sequence** is the discrete version of exactly this idea. Instead of a continuous curve, you have a list: a₁, a₁r, a₁r², a₁r³, …. Each term is r times the previous one. The number r is the **common ratio** — the defining characteristic that makes a sequence geometric. To check whether a sequence is geometric, divide any term by the one before it: if you always get the same number, it is geometric.

The nth term formula a_n = a₁ · r^(n−1) follows directly from the exponential structure. Starting at a₁ (when n = 1, r⁰ = 1), each successive step multiplies by r. This connects to every exponential model you have seen: compound interest starts with a principal and multiplies by (1 + rate) each period; radioactive decay multiplies by a fraction each half-life; a bouncing ball reaches r times the previous height on each bounce. All of these are geometric sequences. Whether |r| > 1 (growth), 0 < |r| < 1 (decay), or r < 0 (alternating sign) determines the sequence's long-run behavior.

The **finite sum formula** S_n = a₁(1 − r^n)/(1 − r) is derived by an elegant algebraic trick. Write S_n = a₁ + a₁r + a₁r² + … + a₁r^(n−1). Multiply both sides by r: rS_n = a₁r + a₁r² + … + a₁r^n. Subtract: S_n − rS_n = a₁ − a₁r^n, so S_n(1 − r) = a₁(1 − r^n), giving the formula. This "multiply and subtract" technique is a foundational algebraic strategy that reappears in many contexts, including proving limits and summing other special series.

The **infinite series formula** S = a₁/(1 − r) for |r| < 1 emerges from taking the limit as n → ∞. When |r| < 1, the term r^n shrinks toward zero, so the factor (1 − r^n) in the numerator approaches 1, leaving a₁/(1 − r). The series converges because each additional term contributes a shrinking fraction of the last, and the cumulative total is bounded. A striking application: the repeating decimal 0.333… = 3/10 + 3/100 + 3/1000 + … is an infinite geometric series with a₁ = 3/10 and r = 1/10. The formula gives S = (3/10)/(1 − 1/10) = (3/10)/(9/10) = 1/3 exactly — confirming that 0.333… and 1/3 are the same number.
