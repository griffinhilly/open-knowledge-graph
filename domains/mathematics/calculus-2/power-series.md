---
id: power-series
title: Power Series
domain: mathematics
course: calculus-2
prerequisites:
- id: geometric-series
  type: hard
- id: absolute-vs-conditional-convergence
  type: hard
- id: binomial-theorem-expansion
  type: soft
- id: convergence-test-strategy
  type: soft
builds-toward:
- radius-and-interval-of-convergence
- taylor-polynomials
tags:
- series
- power-series
- functions
stage: formal-systems
status: validated
---
# Power Series

## Core Idea
A power series centered at a is sum from n=0 to infinity of c_n * (x - a)^n, where c_n are the coefficients and x is the variable. It is a "polynomial of infinite degree" that defines a function of x on whatever interval it converges. Within its interval of convergence, a power series can be differentiated and integrated term by term. Power series are the bridge between series and functions, culminating in Taylor series representations.

## How It's Best Learned
Start with the geometric series 1/(1 - x) = sum of x^n for |x| < 1 as the prototype power series. Manipulate it (substitute, differentiate, integrate) to generate new power series. Introduce the concept of radius of convergence. Emphasize that the power series defines a function whose domain is determined by convergence.

## Common Misconceptions
- Treating a power series as valid for all x (it converges only within its radius of convergence).
- Forgetting that term-by-term differentiation and integration are only valid inside the interval of convergence.
- Confusing the coefficients c_n with the partial sums.

## Questions

```yaml
- question: "The series Σ(x/3)^n (from n=0 to ∞) is a geometric power series. For which values of x does it converge?"
  type: multiple-choice
  options:
    - "All real x"
    - "|x| < 1"
    - "|x| < 3"
    - "x = 0 only"
  answer: 2
  explanation: "This is a geometric series with ratio r = x/3. It converges when |r| < 1, i.e., |x/3| < 1, i.e., |x| < 3. The radius of convergence is 3, not 1. A common error is confusing the series with the standard Σx^n and concluding |x| < 1, ignoring that the ratio is x/3."

- question: "A power series that converges for all x in (-5, 5) can be differentiated term by term, and the resulting power series also converges for all x in (-5, 5)."
  type: true-false
  answer: true
  explanation: "Term-by-term differentiation of a power series is valid inside its interval of convergence, and the resulting series has the same radius of convergence. Endpoint behavior may change, but the open interval (-5, 5) is preserved. This is one of the powerful properties that makes power series so useful — they behave like polynomials inside their interval of convergence."

- question: "Starting from the geometric series 1/(1-x) = Σx^n for |x| < 1, how would you find a power series for 1/(1-x²)?"
  type: short-answer
  answer: "Substitute x² for x: 1/(1-x²) = Σ(x²)^n = Σx^(2n) for |x²| < 1, i.e., |x| < 1."
  explanation: "Substituting x² into the geometric series is valid as long as the new ratio |x²| < 1, which gives |x| < 1. The resulting series Σx^(2n) = 1 + x² + x⁴ + x⁶ + ... converges on the same interval. This technique — deriving new series by substituting into known ones — is far faster than computing coefficients directly."
```

## Explainer

A power series is best understood as a polynomial that never stops: Σ c_n (x - a)^n = c₀ + c₁(x-a) + c₂(x-a)² + .... Like a polynomial, it defines a function of x. Unlike a polynomial, it may only converge for certain values of x — specifically, within a radius R of the center a. Outside that radius, the series diverges and the formula gives no meaningful value.

The prototype power series is the geometric series: 1/(1-x) = 1 + x + x² + x³ + ... for |x| < 1. You've already seen this; now recognize it as the simplest power series, centered at 0 with radius of convergence 1. Every concept about power series can be illustrated with this example first. Substituting -x for x gives 1/(1+x) = Σ(-1)^n x^n; substituting x² gives 1/(1-x²) = Σx^(2n). Manipulation is almost always faster than computing coefficients from scratch.

Within its interval of convergence, a power series is extraordinarily well-behaved — it can be differentiated and integrated term by term, just like a finite polynomial. The resulting series has the same radius of convergence. This is the bridge to Taylor series: if f(x) has a power series representation, you can recover the coefficients by differentiating. The connection between functions and series — allowing you to compute things like sin(0.1) to arbitrary precision, or integrate functions with no closed-form antiderivative — rests entirely on this property.

The key discipline is always respecting the interval of convergence. Outside it, the series is meaningless, and manipulations like term-by-term differentiation are not valid. Endpoint behavior (at x = a ± R) requires separate analysis and is one of the subtler aspects of series theory. As you move toward Taylor series and applications like solving differential equations, keeping the interval of convergence in mind will prevent errors that look algebraically reasonable but are analytically invalid.
