---
id: taylor-series
title: Taylor Series
domain: mathematics
course: calculus-2
prerequisites:
- id: taylor-polynomials
  type: hard
- id: power-series
  type: hard
- id: radius-and-interval-of-convergence
  type: hard
- id: lhopitals-rule
  type: soft
builds-toward:
- maclaurin-series
- taylor-series-common-functions
tags:
- series
- Taylor
- representation
stage: formal-systems
status: validated
---
# Taylor Series

## Core Idea
The Taylor series of f centered at a is the infinite power series sum from n=0 to infinity of f^(n)(a)/n! * (x - a)^n. If this series converges to f(x), then f has a power series representation. The Taylor series extends the Taylor polynomial to infinite degree, providing an exact representation (not just an approximation) within the radius of convergence. Not all functions equal their Taylor series (the remainder must go to zero).

## How It's Best Learned
Derive Taylor series for e^x, sin(x), cos(x), and 1/(1 - x) from the definition. Verify convergence using the ratio test. Show that the remainder term goes to zero (at least for the standard functions). Practice manipulating known Taylor series (substitution, differentiation, integration) to find new ones.

## Common Misconceptions
- Assuming every infinitely differentiable function equals its Taylor series (counterexample: e^(-1/x^2) at 0).
- Confusing the Taylor series (infinite, representation) with Taylor polynomial (finite, approximation).
- Not checking that the remainder goes to zero, which is required for the series to equal the function.

## Questions

```yaml
- question: "Which condition is required for a function f(x) to actually equal its Taylor series on an interval, not just be approximated by it?"
  type: multiple-choice
  options:
    - "f must be continuous on the interval"
    - "f must be infinitely differentiable on the interval"
    - "The remainder term R_n(x) must approach zero as n → ∞"
    - "The series must converge for all real numbers, not just on a finite interval"
  answer: 2
  explanation: "Infinite differentiability is necessary but not sufficient. The Taylor series of f always converges to *some* value, but that value may not equal f(x) unless the remainder Rn(x) = f(x) - (partial sum of n terms) → 0 as n → ∞. The classic counterexample is f(x) = e^(-1/x²) at x = 0: all derivatives equal 0 there, so the Taylor series is identically 0, which does not equal f(x) for x ≠ 0."

- question: "A Taylor polynomial and a Taylor series for the same function centered at the same point are two names for the same mathematical object."
  type: true-false
  answer: false
  explanation: "A Taylor polynomial is a finite sum of n+1 terms — it approximates f(x) near the center point. A Taylor series is an infinite sum. Within the radius of convergence, the Taylor series (when it equals f) gives exact values; the polynomial always retains error. The distinction matters: polynomials are used for computation and estimates; the series is used when exact representation is needed."

- question: "The Taylor series for e^x is 1 + x + x²/2! + x³/3! + ···, and it converges for all real x. What does it mean to say this series 'converges to e^x'?"
  type: short-answer
  answer: "It means that as you add more and more terms of the series, the partial sums get arbitrarily close to the exact value of e^x — and in the limit, the infinite sum equals e^x exactly, not just approximately."
  explanation: "Convergence means the sequence of partial sums S_n = 1 + x + x²/2! + ··· + xⁿ/n! approaches e^x as n → ∞. This is stronger than mere approximation: for any desired level of accuracy, you can find an n large enough that S_n is within that accuracy of e^x. For e^x this holds for every real number x."
```

## Explainer

You have already worked with Taylor polynomials, which approximate a smooth function near a point by matching the function's value and derivatives up to some finite degree. A degree-3 Taylor polynomial for sin(x) near 0 gives x − x³/6, which is excellent near x = 0 but drifts away from sin(x) as x grows. The natural question is: what if we never stop adding terms? The **Taylor series** is the answer — it extends the Taylor polynomial to an infinite sum, and when it converges to the function, it gives an *exact* representation rather than an approximation.

The Taylor series of f centered at a is the infinite sum: f(a) + f'(a)(x−a) + f''(a)(x−a)²/2! + f'''(a)(x−a)³/3! + ··· You write this compactly as Σ (f⁽ⁿ⁾(a)/n!) (x−a)ⁿ from n = 0 to ∞. You have already computed these coefficients for Taylor polynomials; the Taylor series just keeps going. The coefficients are determined entirely by the derivatives of f at the single point a — the remarkable claim is that, for well-behaved functions, all the information about f near a is encoded in those derivatives.

But here is the critical caveat: not every infinitely differentiable function equals its Taylor series. The series always converges to *something*, but that something may not equal f(x). To confirm that f(x) equals its Taylor series on an interval, you must show that the **remainder term** Rₙ(x) — the error between f and the nth partial sum — goes to zero as n → ∞. For e^x, sin(x), cos(x), and 1/(1−x) this can be verified directly, which is why these are the standard examples. A pathological function like e^(−1/x²), however, has all zero derivatives at x = 0, so its Taylor series is identically 0 — clearly not equal to the function for x ≠ 0.

The **radius of convergence** from your power series work remains central here. The Taylor series for 1/(1−x) = 1 + x + x² + ··· converges only for |x| < 1, even though the function itself is defined for all x ≠ 1. Within the radius, the series equals the function; outside it, the series diverges. For e^x the radius is infinite — the series converges everywhere. Understanding where equality holds is as important as knowing the series itself.

In practice, the most powerful technique is often *not* recomputing from the definition but instead **manipulating known series**. If you know the series for e^x, you can substitute −x² to get the series for e^(−x²) without computing a single new derivative. You can differentiate or integrate term-by-term inside the radius of convergence. This toolkit — derive the four or five standard series once, then transform them — is what makes Taylor series genuinely useful in applied mathematics, physics, and numerical analysis.
