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

## Questions

```yaml
- question: "A power series centered at a = 2 is found to have radius of convergence R = 3. A student concludes the interval of convergence is (−1, 5). What is wrong with this conclusion?"
  type: multiple-choice
  options:
    - "Nothing is wrong — (−1, 5) is the correct interval of convergence"
    - "The center and radius were applied incorrectly; the interval should be (−1, 5) is wrong and it should be (2−3, 2+3)"
    - "The endpoints x = −1 and x = 5 require separate testing before including or excluding them"
    - "A radius of 3 means the interval has length 3, not 6, so the answer should be (2, 5)"
  answer: 2
  explanation: "The ratio or root test is inconclusive exactly at the boundary points |x − a| = R. At x = −1 and x = 5, the test gives limit = 1, which tells you nothing. Each endpoint produces a fixed numerical series that must be tested independently using other tests (alternating series, p-series, etc.). One endpoint might converge, one might diverge, or both might do either. The interval (−1, 5) is the open interior guaranteed by the ratio test, but the full interval of convergence could be (−1, 5), [−1, 5), (−1, 5], or [−1, 5]."

- question: "Applying the ratio test to the power series Σ xⁿ / n gives lim |aₙ₊₁/aₙ| = |x|. Which of the following correctly describes the interval of convergence?"
  type: multiple-choice
  options:
    - "[−1, 1], because the series converges for all |x| ≤ 1"
    - "(−1, 1), because the ratio test shows convergence for |x| < 1 and the endpoints are not worth checking"
    - "[−1, 1), because x = −1 gives a convergent alternating series and x = 1 gives the divergent harmonic series"
    - "(−1, 1], because x = 1 gives a convergent p-series and x = −1 gives a divergent series"
  answer: 2
  explanation: "The ratio test gives R = 1, guaranteeing convergence for |x| < 1 and divergence for |x| > 1. At x = 1, the series becomes Σ 1/n (harmonic series), which diverges. At x = −1, the series becomes Σ (−1)ⁿ/n (alternating harmonic series), which converges by the alternating series test. So the interval is [−1, 1) — left endpoint included, right excluded. This illustrates that each endpoint is an independent question."

- question: "If the radius of convergence of a power series is R = 5, then the series converges for all x in the closed interval [a − 5, a + 5]."
  type: true-false
  answer: false
  explanation: "The radius of convergence guarantees convergence only in the open interval (a − 5, a + 5). The endpoints a − 5 and a + 5 lie exactly at the boundary where the ratio/root test is inconclusive (limit = 1). Each endpoint must be tested separately and may converge or diverge independently. The interval of convergence could be open, half-open, or closed at either end."

- question: "The radius of convergence R and the interval of convergence are two distinct concepts: R is a non-negative number (or ∞), while the interval of convergence is a set of real numbers."
  type: true-false
  answer: true
  explanation: "This is a crucial distinction students frequently blur. R = 5 tells you the half-length of the convergence interval, but it does not specify the interval — you still need to determine whether each endpoint is included. For the same R, the interval could be (a−5, a+5), [a−5, a+5), (a−5, a+5], or [a−5, a+5]. R is a scalar; the interval is a subset of ℝ."

- question: "Why must the endpoints of the interval of convergence be tested separately, rather than being determined by the radius of convergence alone?"
  type: short-answer
  answer: "At the endpoints x = a ± R, the ratio (or root) test yields a limit exactly equal to 1, which is the test's inconclusive case. The test only guarantees convergence when the limit is strictly less than 1 and divergence when strictly greater than 1. At the boundary, anything is possible: the series may converge or diverge at each endpoint independently. Each endpoint produces a fixed numerical series (with x replaced by a + R or a − R), which must be analyzed using other tests such as the alternating series test or p-series comparison."
  explanation: "The ratio test is derived from comparison with a geometric series: if the ratio of successive terms is eventually less than some r < 1, the series converges like a geometric series. At the boundary, the ratio approaches exactly 1, which means the comparison with a geometric series breaks down — successive terms are not shrinking fast enough to guarantee convergence, but they aren't growing either. The resulting boundary series may be anything from a p-series (which converges for p > 1, diverges for p ≤ 1) to an alternating series or something else entirely."
```

## Explainer

A **power series** Σ cₙ(x − a)ⁿ is not a fixed number — it is a function of x, and whether the series converges depends on which x you plug in. You already know the ratio test: it determines convergence for a fixed series by looking at the ratio of successive terms. Apply the ratio test to a power series, and something remarkable happens — the test produces a condition on x itself, carving the real line into a region where the series converges and a region where it diverges. The threshold between those regions is the **radius of convergence** R.

To find R, form the ratio |cₙ₊₁(x − a)ⁿ⁺¹ / cₙ(x − a)ⁿ| = |cₙ₊₁/cₙ| · |x − a|. For the series to converge, you need this ratio to be less than 1 as n → ∞. If |cₙ₊₁/cₙ| → L as n → ∞, then the condition becomes L · |x − a| < 1, or |x − a| < 1/L. So R = 1/L. The series converges absolutely for all x within distance R of the center a, and diverges for all x farther than R from a. Three special cases: if L = 0, then R = ∞ (converges everywhere); if L = ∞, then R = 0 (converges only at x = a itself); otherwise R is a positive finite number.

Here is the critical subtlety: at the boundary points x = a + R and x = a − R, the ratio test gives exactly 1 — which is **inconclusive**. You must test each endpoint separately using whatever series test fits the resulting series. At x = a + R, the series becomes Σ cₙ Rⁿ, a fixed numerical series. At x = a − R, it becomes Σ cₙ (−R)ⁿ, which has alternating signs if R > 0. One endpoint might give a convergent alternating series; the other might give a divergent p-series. Each endpoint is an independent question. The **interval of convergence** is the full set of x-values where the series converges — it is always an interval centered at a, but its endpoints may be included, excluded, or one of each.

A useful mental picture: the power series is "centered" at a and extends equally in both directions. The radius R tells you how far you can travel from the center before the series breaks down. Think of it like a circle on the real line: inside the circle, convergence is guaranteed; outside, divergence is guaranteed; on the boundary, anything is possible and you must check. This picture also previews what happens in complex analysis — power series in the complex plane literally converge inside a disk of radius R centered at a in the complex plane, which is where the term "radius" comes from. The boundary behavior is richer and more subtle in that setting, but the core structure — a convergence region, a divergence region, and a boundary requiring case-by-case analysis — carries over exactly.
