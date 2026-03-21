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

## Questions

```yaml
- question: "To find the Maclaurin series for sin(x²), a student should..."
  type: multiple-choice
  options:
    - "Substitute x² for x in the known Maclaurin series for sin(x)"
    - "Differentiate the known Maclaurin series for cos(x) term by term"
    - "Integrate the known Maclaurin series for sin(x) term by term"
    - "Compute all derivatives of sin(x²) at x = 0 from scratch using the chain rule"
  answer: 0
  explanation: "The most efficient approach is substitution: since sin(x) = x − x³/3! + x⁵/5! − ⋯, replacing every x with x² gives sin(x²) = x² − x⁶/3! + x¹⁰/5! − ⋯. This takes seconds and avoids the escalating complexity of computing higher derivatives of sin(x²) via repeated chain and product rules. Option D represents the common but inefficient approach — the whole point of memorizing the standard series is to avoid re-deriving from scratch every time."

- question: "A classmate claims: 'The Maclaurin series is a generalization of the Taylor series — it works at more points.' What is wrong with this statement?"
  type: multiple-choice
  options:
    - "It reverses the relationship: a Maclaurin series is a special case of a Taylor series, specifically the one centered at a = 0"
    - "Nothing — Maclaurin series do converge for a wider range of x than Taylor series in general"
    - "The Maclaurin series only works for trigonometric functions, not for general functions"
    - "Taylor series centered at a ≠ 0 are undefined; all Taylor series are centered at 0"
  answer: 0
  explanation: "A Maclaurin series is simply a Taylor series with the center set to a = 0. It is more restricted, not more general — you sacrifice the ability to center the expansion near other points. The Taylor series formula Σ f⁽ⁿ⁾(a)/n! · (x−a)ⁿ becomes Σ f⁽ⁿ⁾(0)/n! · xⁿ when a = 0. The Maclaurin series is used frequently because centering at 0 simplifies the algebra for many common functions, not because it has broader applicability."

- question: "Differentiating the Maclaurin series for sin(x) term by term yields the Maclaurin series for cos(x)."
  type: true-false
  answer: true
  explanation: "Yes. sin(x) = x − x³/3! + x⁵/5! − x⁷/7! + ⋯. Differentiating term by term: 1 − 3x²/3! + 5x⁴/5! − 7x⁶/7! + ⋯ = 1 − x²/2! + x⁴/4! − x⁶/6! + ⋯, which is exactly the Maclaurin series for cos(x). This works because within the radius of convergence, power series can be differentiated term by term — and this is actually how the cos(x) series can be derived from sin(x) rather than by computing cos's derivatives independently."

- question: "Every Maclaurin series converges for all real numbers x."
  type: true-false
  answer: false
  explanation: "This is false. Some Maclaurin series have limited radii of convergence. The series for e^x, sin(x), and cos(x) do converge for all x, but 1/(1−x) = 1 + x + x² + ⋯ only converges for |x| < 1, and ln(1+x) only converges for −1 < x ≤ 1. When you manipulate a known series (by substitution, differentiation, or integration), you must track what happens to the radius of convergence — it can shrink but never grow."

- question: "Why is it generally more efficient to find the Maclaurin series for e^(−x²) by substituting into the known series for e^x rather than computing derivatives of e^(−x²) directly?"
  type: short-answer
  answer: "Substituting −x² for x in the known series e^x = 1 + x + x²/2! + x³/3! + ⋯ gives 1 − x² + x⁴/2! − x⁶/3! + ⋯ in one step. Computing derivatives of e^(−x²) directly requires repeatedly applying the chain and product rules — the n-th derivative at x = 0 grows rapidly in complexity. Both methods yield the same result, but substitution leverages already-known information and avoids computational errors."
  explanation: "The point of memorizing the standard Maclaurin series is precisely to make this substitution strategy available. The key insight is that the Maclaurin series for a function is uniquely determined by its derivatives at 0 — so if you can algebraically transform a known series into the target function, you have the correct series without any differentiation. Substitution, differentiation, and integration of series are the core manipulation toolkit."
```

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
