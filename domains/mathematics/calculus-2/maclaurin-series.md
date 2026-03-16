---
id: maclaurin-series
title: Maclaurin Series
domain: mathematics
course: calculus-2
prerequisites:
  - id: taylor-series
    type: hard
builds-toward:
  - taylor-series-common-functions
tags: [series, Maclaurin, Taylor, special-case]
stage: formal-systems
status: validated
---

# Maclaurin Series

## Core Idea
A Maclaurin series is a Taylor series centered at a = 0: sum from n=0 to infinity of f^(n)(0)/n! * x^n. It is not a separate concept from Taylor series but a special case that is used so frequently it has its own name. The most important Maclaurin series (e^x, sin(x), cos(x), 1/(1-x), ln(1+x), arctan(x)) should be memorized because they are used to derive many other series.

## How It's Best Learned
Derive the standard Maclaurin series from the definition. Memorize the key ones. Practice using them to find series for related functions: e^(-x^2) from e^x, sin(x^2) from sin(x), etc. Show how known series can be added, multiplied, substituted, differentiated, and integrated.

## Common Misconceptions
- Believing Maclaurin series and Taylor series are fundamentally different concepts (Maclaurin is just Taylor at 0).
- Not memorizing the standard series and rederiving from scratch every time (inefficient).
- Forgetting the radius of convergence of the manipulated series.

## Explainer

You already know Taylor series: a way to represent a function f(x) as a power series centered at a point a, using the formula Σ f^(n)(a)/n! · (x − a)^n. A **Maclaurin series** is not a new idea — it is simply the Taylor series with a = 0, so every (x − a) becomes just x. The formula reduces to Σ f^(n)(0)/n! · x^n. This special case appears constantly because many of the most important functions in mathematics are most naturally described near the origin, and the algebra simplifies considerably when the center is zero.

The five series you must internalize are:
- **e^x** = 1 + x + x²/2! + x³/3! + ⋯ = Σ x^n/n! (converges for all x)
- **sin(x)** = x − x³/3! + x⁵/5! − ⋯ = Σ (−1)^n x^(2n+1)/(2n+1)! (converges for all x)
- **cos(x)** = 1 − x²/2! + x⁴/4! − ⋯ = Σ (−1)^n x^(2n)/(2n)! (converges for all x)
- **1/(1−x)** = 1 + x + x² + x³ + ⋯ = Σ x^n (converges for |x| < 1)
- **ln(1+x)** = x − x²/2 + x³/3 − ⋯ = Σ (−1)^(n+1) x^n/n (converges for −1 < x ≤ 1)

These five are not arbitrary memorization targets — they are the atomic building blocks from which hundreds of other series are built through algebraic manipulation. If you need the series for e^(−x²), substitute −x² for x in the e^x series: 1 − x² + x⁴/2! − x⁶/3! + ⋯. If you need sin(3x), substitute 3x for x in the sin(x) series. This substitution strategy is faster and less error-prone than re-deriving from the definition every time.

Beyond substitution, you can also **differentiate** or **integrate** a known series term by term within its radius of convergence. The series for cos(x) can be derived by differentiating the series for sin(x) term by term. The series for ln(1+x) can be derived by integrating the geometric series 1/(1+x) = 1 − x + x² − ⋯. This interconnectedness means that memorizing a few series unlocks many others. The key discipline is tracking what happens to the radius of convergence: it can only shrink or stay the same through these operations — it never grows.
