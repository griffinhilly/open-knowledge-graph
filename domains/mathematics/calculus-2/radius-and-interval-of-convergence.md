---
id: radius-and-interval-of-convergence
title: Radius and Interval of Convergence
domain: mathematics
course: calculus-2
prerequisites:
  - id: power-series
    type: hard
  - id: ratio-test
    type: hard
  - id: root-test
    type: soft
builds-toward:
  - taylor-series
tags: [series, power-series, convergence, radius]
stage: formal-systems
status: validated
---

# Radius and Interval of Convergence

## Core Idea
Every power series sum of c_n * (x - a)^n has a radius of convergence R such that the series converges absolutely for |x - a| < R and diverges for |x - a| > R. The interval of convergence is (a - R, a + R) with the endpoints requiring separate testing. R is found using the ratio test or root test applied to the general term. R can be 0 (converges only at a), infinity (converges everywhere), or any positive number.

## How It's Best Learned
Apply the ratio test to |c_n (x - a)^n| and solve for the values of x where the resulting limit is less than 1. This gives R. Then test each endpoint individually using known series tests (p-series, alternating series, etc.). Practice until the three-step process (find R, determine interval, test endpoints) is systematic.

## Common Misconceptions
- Forgetting to test the endpoints (the ratio/root test is inconclusive at |x - a| = R).
- Believing the radius of convergence determines the interval completely (endpoints must be checked separately).
- Confusing radius of convergence with interval of convergence (R is a number, the interval is a set).

## Explainer

A **power series** Σ cₙ(x − a)ⁿ is not a fixed number — it is a function of x, and whether the series converges depends on which x you plug in. You already know the ratio test: it determines convergence for a fixed series by looking at the ratio of successive terms. Apply the ratio test to a power series, and something remarkable happens — the test produces a condition on x itself, carving the real line into a region where the series converges and a region where it diverges. The threshold between those regions is the **radius of convergence** R.

To find R, form the ratio |cₙ₊₁(x − a)ⁿ⁺¹ / cₙ(x − a)ⁿ| = |cₙ₊₁/cₙ| · |x − a|. For the series to converge, you need this ratio to be less than 1 as n → ∞. If |cₙ₊₁/cₙ| → L as n → ∞, then the condition becomes L · |x − a| < 1, or |x − a| < 1/L. So R = 1/L. The series converges absolutely for all x within distance R of the center a, and diverges for all x farther than R from a. Three special cases: if L = 0, then R = ∞ (converges everywhere); if L = ∞, then R = 0 (converges only at x = a itself); otherwise R is a positive finite number.

Here is the critical subtlety: at the boundary points x = a + R and x = a − R, the ratio test gives exactly 1 — which is **inconclusive**. You must test each endpoint separately using whatever series test fits the resulting series. At x = a + R, the series becomes Σ cₙ Rⁿ, a fixed numerical series. At x = a − R, it becomes Σ cₙ (−R)ⁿ, which has alternating signs if R > 0. One endpoint might give a convergent alternating series; the other might give a divergent p-series. Each endpoint is an independent question. The **interval of convergence** is the full set of x-values where the series converges — it is always an interval centered at a, but its endpoints may be included, excluded, or one of each.

A useful mental picture: the power series is "centered" at a and extends equally in both directions. The radius R tells you how far you can travel from the center before the series breaks down. Think of it like a circle on the real line: inside the circle, convergence is guaranteed; outside, divergence is guaranteed; on the boundary, anything is possible and you must check. This picture also previews what happens in complex analysis — power series in the complex plane literally converge inside a disk of radius R centered at a in the complex plane, which is where the term "radius" comes from. The boundary behavior is richer and more subtle in that setting, but the core structure — a convergence region, a divergence region, and a boundary requiring case-by-case analysis — carries over exactly.
