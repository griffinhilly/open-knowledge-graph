---
id: uniform-convergence-power-series
title: Uniform Convergence of Power Series
domain: mathematics
course: real-analysis
prerequisites:
- id: weierstrass-m-test
  type: hard
- id: power-series
  type: soft
- id: interchange-limit-derivative
  type: soft
- id: rigorous-series-convergence
  type: hard
tags:
- power-series
- uniform-convergence
- analytic
stage: advanced
status: validated
---

# Uniform Convergence of Power Series

## Core Idea
A power series ∑aₙ(x - c)ⁿ converges uniformly on any closed interval inside its interval of convergence. This justifies term-by-term differentiation and integration of power series, making them the foundation of analytic functions. The uniform convergence follows from the Weierstrass M-Test applied to majorizing geometric series.

## How It's Best Learned
Work everything on the geometric series ∑xⁿ = 1/(1 − x), with R = 1. On [−1/2, 1/2], take Mₙ = (1/2)ⁿ, which sums to 2. On (−1, 1), the tail after the xⁿ term is xⁿ⁺¹/(1 − x), which is unbounded as x → 1⁻, so convergence there is not uniform. Then integrate from 0 to x term by term to get −ln(1 − x) = ∑xⁿ⁺¹/(n+1).

## Common Misconceptions
- A power series converges uniformly on its whole open interval of convergence. (∑xⁿ converges at every point of (−1, 1), but its tail xⁿ⁺¹/(1 − x) has no bound near x = 1, so the convergence there is not uniform.)
- Differentiating term by term keeps the interval of convergence exactly the same. (The radius stays the same, but endpoint behavior can change. ∑xⁿ/n² converges at x = 1, while its derivative series ∑xⁿ⁻¹/n is the harmonic series there and diverges.)
- Because uniform convergence holds only on closed subintervals [−r, r], the sum is known to be continuous only on those subintervals. (Continuity is local. Each x in (−R, R) lies inside some [−r, r] with |x| < r < R, so the sum is continuous on all of (−R, R).)
- Term-by-term differentiation is justified because the original series converges uniformly. (Uniform convergence of a series does not by itself allow this. It is justified because the differentiated series has the same radius, so it too converges uniformly on each closed subinterval [c − r, c + r] with r < R.)

## Questions

```yaml
- question: "A power series has radius of convergence R = 3. On which domain is term-by-term integration rigorously justified by the uniform convergence theorem?"
  type: multiple-choice
  options:
    - "The open interval (−3, 3), since the series converges at every point there"
    - "The closed interval [−3, 3], which is the full interval of convergence"
    - "Any closed interval [−r, r] with r < 3, where uniform convergence is guaranteed by the Weierstrass M-test"
    - "Only at the center x = 0, where all terms are trivially bounded"
  answer: 2
  explanation: "Uniform convergence (and the resulting validity of term-by-term operations) holds on any closed interval strictly inside the radius of convergence. On a closed [−r, r] with r < R, each term |aₙ(x−c)ⁿ| ≤ |aₙ|rⁿ = Mₙ, and ΣMₙ converges. On the full open interval (option A), the bound breaks down near the boundary. On [−R, R] (option B), convergence at the endpoints may be conditional, and uniform convergence can fail there."

- question: "In applying the Weierstrass M-test to show ∑aₙxⁿ converges uniformly on [−r, r] (with r < R), what is the bounding sequence Mₙ, and why must r be strictly less than R?"
  type: multiple-choice
  options:
    - "Mₙ = |aₙ| — the coefficients alone bound the terms"
    - "Mₙ = |aₙ|Rⁿ — using the full radius ensures the tightest possible bound"
    - "Mₙ = |aₙ|rⁿ — this dominates all terms on [−r, r] and ΣMₙ converges because r < R"
    - "Mₙ = n|aₙ|rⁿ⁻¹ — the derivative series provides the correct bound"
  answer: 2
  explanation: "For any x in [−r, r], |aₙxⁿ| ≤ |aₙ|rⁿ = Mₙ. The M-test requires ΣMₙ < ∞. Since r < R, the series ∑|aₙ|rⁿ converges (this is what having a radius of convergence means). If we tried r = R (option B), ∑|aₙ|Rⁿ might diverge, and the M-test would fail. Using just |aₙ| (option A) ignores the x-dependence entirely and doesn't give a valid bound for all n."

- question: "A power series that converges pointwise at most point of (−R, R) necessarily converges uniformly on that entire open interval."
  type: true-false
  answer: false
  explanation: "Pointwise convergence on an open interval does not imply uniform convergence on that same interval. The theorem guarantees uniform convergence only on closed sub-intervals [−r, r] with r strictly less than R. Near the endpoints, the partial sums may converge more and more slowly, preventing uniformity on the full open interval. This is precisely why the Weierstrass M-test is applied to a compact sub-interval: the bound Mₙ = |aₙ|rⁿ is only summable because r < R."

- question: "Term-by-term differentiation of a power series ∑aₙ(x − c)ⁿ produces a new power series with the same radius of convergence as the original."
  type: true-false
  answer: true
  explanation: "The differentiated series is ∑naₙ(x − c)ⁿ⁻¹. The radius of convergence is determined by lim sup |aₙ|^(1/n) via the root test, and the factor of n does not affect this limit since n^(1/n) → 1. So the radius of convergence is unchanged. Similarly for integration. This means a power series can be differentiated and integrated infinitely many times within its disk of convergence — making analytic functions the most well-behaved class in analysis."

- question: "Why must you restrict to a closed sub-interval strictly inside the interval of convergence to establish uniform convergence via the Weierstrass M-test? What goes wrong at the boundary of the interval of convergence?"
  type: short-answer
  answer: "The M-test requires finding Mₙ such that |aₙ(x−c)ⁿ| ≤ Mₙ for all x in the interval and ΣMₙ < ∞. On [−r, r] with r < R, the bound Mₙ = |aₙ|rⁿ works because ∑|aₙ|rⁿ converges (by definition of R). At the boundary x = R, the bound would need Mₙ = |aₙ|Rⁿ, but ∑|aₙ|Rⁿ may diverge — the series might only converge conditionally there, not absolutely. Without an absolutely convergent dominating series, the M-test cannot be applied."
  explanation: "The boundary behavior of a power series is delicate: it can converge absolutely, converge conditionally, or diverge at x = ±R, depending on the specific series. Uniform convergence on an open interval would require controlling the supremum over all points, including those approaching R — and near R the partial sums may converge arbitrarily slowly. The compactness of [−r, r] with r < R is what lets the geometric bound close."
```

## Explainer

A power series ∑aₙ(x − c)ⁿ looks like an infinite polynomial, and you want to treat it like one: differentiate term by term, integrate term by term, substitute x into the series and get a meaningful value. But an infinite sum of functions is a limit — a limit of partial sums Sₙ(x) = ∑ₖ₌₀ⁿ aₖ(x−c)ᵏ — and you know that limits and operations like differentiation don't automatically commute. The question is: when can you treat a power series exactly like a polynomial for purposes of integration and differentiation?

The answer comes from the **Weierstrass M-Test**, which you already know. On any closed interval [c−r, c+r] strictly inside the interval of convergence, you can bound each term: |aₙ(x−c)ⁿ| ≤ |aₙ|rⁿ for all x in the interval. Call Mₙ = |aₙ|rⁿ. Since r is strictly less than the radius of convergence, the series ∑Mₙ = ∑|aₙ|rⁿ converges — it is dominated by a convergent geometric-like series. The Weierstrass M-Test then guarantees that ∑aₙ(x−c)ⁿ converges uniformly on [c−r, c+r]. The key word is "closed interval strictly inside" — uniformity can fail at the boundary, which is why you must stay strictly interior.

Once you have uniform convergence on compact subintervals, you can integrate term by term: ∫∑aₙ(x−c)ⁿ dx = ∑∫aₙ(x−c)ⁿ dx = ∑aₙ(x−c)ⁿ⁺¹/(n+1). Differentiation needs one more step, because uniform convergence of a series alone does not allow term-by-term differentiation. The differentiated series ∑naₙ(x−c)ⁿ⁻¹ is again a power series with the same radius of convergence, so it also converges uniformly on compact subintervals, and that is what justifies d/dx ∑aₙ(x−c)ⁿ = ∑naₙ(x−c)ⁿ⁻¹. Both operations produce a new power series with the same radius of convergence. This means that on the interior of its disk of convergence, a power series can be differentiated infinitely many times, and each derivative is again a power series. Functions representable by power series are called **analytic functions** — the most well-behaved class in analysis.

This result is the gateway to understanding functions like sin(x), cos(x), and eˣ as infinite polynomials that you can manipulate term by term. When you learned that sin(x) = x − x³/6 + x⁵/120 − ···, you were implicitly using this theorem: the series converges uniformly on any bounded interval, so you can integrate it to get the series for −cos(x), differentiate it to get the series for cos(x), and multiply two such series to get new identities. Every formula involving Taylor series manipulation rests on this foundation.
