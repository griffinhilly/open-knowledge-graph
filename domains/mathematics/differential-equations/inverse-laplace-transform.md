---
id: inverse-laplace-transform
title: Inverse Laplace Transform and Partial Fractions
domain: mathematics
course: differential-equations
prerequisites:
- id: common-laplace-transforms
  type: hard
- id: partial-fractions
  type: hard
builds-toward:
- laplace-transform-of-derivatives
tags:
- inverse-transform
- partial-fractions
- recovery
stage: formal-systems
status: validated
---

# Inverse Laplace Transform and Partial Fractions

## Core Idea
To recover f(t) from F(s), decompose F(s) = P(s)/Q(s) using partial fractions, then apply the inverse Laplace transform to each term via tables. This converts a challenging inversion problem into algebra and table lookup. The partial fraction decomposition handles poles (roots of the denominator), with simple poles giving exponential terms and complex conjugate poles giving oscillatory terms.

## Questions

```yaml
- question: "You are given F(s) = 5 / ((s + 2)(s + 7)). What is the correct approach to find f(t)?"
  type: multiple-choice
  options:
    - "Apply the inverse Laplace transform directly to the entire fraction — there is a single table entry for products of linear factors"
    - "Decompose into partial fractions A/(s + 2) + B/(s + 7), then invert each term separately using the table entry L⁻¹{1/(s − a)} = e^{at}"
    - "Differentiate F(s) with respect to s to simplify it, then invert"
    - "Take the limit of F(s) as s → 0 to recover the initial value, then integrate"
  answer: 1
  explanation: "The strategy is always: partial fractions first, then table lookup. The product of two linear factors does not match any single standard table entry, but each individual term A/(s + 2) and B/(s + 7) matches the entry L⁻¹{1/(s − a)} = e^{at} directly (with a = −2 and a = −7 respectively). The linearity of the inverse Laplace transform means you can invert each term separately and sum the results. Options C and D describe valid Laplace transform properties but are not the approach for this type of problem."

- question: "F(s) = (3s + 1) / ((s + 2)(s² + 9)). After partial fraction decomposition, what types of terms will appear in f(t)?"
  type: multiple-choice
  options:
    - "Only exponential terms of the form Ce^{at}"
    - "A decaying exponential e^{−2t} and oscillatory terms involving cos(3t) and/or sin(3t)"
    - "Only sinusoidal terms, since the complex conjugate poles dominate the response"
    - "Polynomial terms in t, since the denominator has degree 3"
  answer: 1
  explanation: "The denominator has two types of roots: a real root at s = −2 (from the factor s + 2) and complex conjugate roots at s = ±3i (from s² + 9 = 0). The real root contributes A/(s + 2), which inverts to Ae^{−2t}. The complex conjugate roots contribute (Bs + C)/(s² + 9), which inverts to a linear combination of cos(3t) and sin(3t) (since these roots have zero real part, α = 0, giving pure oscillation rather than exponentially modulated oscillation). Both types are present. Option C is wrong because real poles also contribute to the response."

- question: "Complex conjugate poles in F(s) always produce purely sinusoidal terms in f(t) with no exponential envelope."
  type: true-false
  answer: false
  explanation: "Complex conjugate poles at s = α ± βi produce terms of the form e^{αt}cos(βt) and e^{αt}sin(βt) in f(t). If α = 0 (the poles are purely imaginary, on the imaginary axis), the result is pure oscillation with no growth or decay. But if α ≠ 0 — the poles have a nonzero real part — the oscillation is modulated by an exponential envelope: decaying if α < 0, growing if α > 0. For example, poles at s = −1 ± 2i give e^{−t}cos(2t) and e^{−t}sin(2t) — damped oscillations, not pure sinusoids."

- question: "The inverse Laplace transform is a linear operation, so the inverse transform of a sum of partial fraction terms equals the sum of the inverse transforms of each individual term."
  type: true-false
  answer: true
  explanation: "Linearity is the property that makes the entire partial-fractions strategy work. L⁻¹{F₁(s) + F₂(s)} = L⁻¹{F₁(s)} + L⁻¹{F₂(s)}, and L⁻¹{cF(s)} = c · L⁻¹{F(s)} for any constant c. This means once you decompose F(s) into a sum of simple terms that each match a table entry, you can invert each independently and sum the results. Without linearity, partial fractions would not yield the complete solution — you would have to invert the entire combined expression at once, which is the hard problem you are trying to avoid."

- question: "Describe the complete pipeline for solving an initial value problem using Laplace transforms. Where does the inverse Laplace transform fit, and why are partial fractions necessary at that step?"
  type: short-answer
  answer: "The pipeline has four steps: (1) Apply the Laplace transform to both sides of the ODE, converting the differential equation into an algebraic equation in F(s). (2) Solve algebraically for F(s), using the derivative-transform properties to handle the initial conditions. (3) Decompose F(s) using partial fractions — because the algebraic solution typically produces a rational function P(s)/Q(s) whose form does not directly match any table entry. (4) Apply the inverse Laplace transform term by term to recover f(t). Partial fractions are necessary at step 3 because the denominator Q(s) usually has multiple roots, and only after decomposing into simple terms — one per root — does each term match a standard table entry that can be inverted by inspection."
  explanation: "The pipeline's power is that it converts an ODE (hard: requires integration or series methods) into algebra (easy: multiply, divide, simplify), and then converts the s-domain algebraic answer back into a time-domain function through pattern-matching. The inverse transform and partial fractions together are the 'return path' — the step that converts the convenient s-domain answer into the actual solution f(t) that the problem asked for."
```

## Explainer

You've built a table of Laplace transform pairs — functions f(t) and their transforms F(s) — and you've practiced decomposing rational functions into simpler fractions using partial fractions. The **inverse Laplace transform** closes the loop: given F(s) in the s-domain, recover f(t) in the time domain. The challenge is that F(s) is rarely in a form that directly matches any table entry. It arrives as a rational function P(s)/Q(s) whose denominator has multiple roots, none of which look like simple table entries on their own.

The strategy is partial fractions first, then table lookup. Partial fractions rewrites F(s) as a sum of simpler terms, each of which *does* match a table entry. The structure of the denominator determines which terms appear. A simple real root at s = a contributes a term A/(s − a), whose inverse transform is Ae^{at}. A repeated root at s = a of order k contributes A₁/(s − a) + A₂/(s − a)² + ··· + Aₖ/(s − a)ᵏ, whose inverses involve tʲe^{at}. Complex conjugate roots s = α ± βi combine into terms of the form (As + B)/((s − α)² + β²), whose inverses give e^{αt}cos(βt) and e^{αt}sin(βt) — exponentially-modulated oscillations.

Work through a simple example: F(s) = 1/(s² + 4s + 3). Factor the denominator: s² + 4s + 3 = (s + 1)(s + 3). Decompose: 1/((s+1)(s+3)) = A/(s+1) + B/(s+3). Clear denominators: 1 = A(s+3) + B(s+1). Setting s = −1 gives A = 1/2; setting s = −3 gives B = −1/2. So F(s) = (1/2)/(s+1) − (1/2)/(s+3). From the table, L⁻¹{1/(s − a)} = e^{at}, so f(t) = (1/2)e^{−t} − (1/2)e^{−3t}. This is a sum of two decaying exponentials — exactly what you'd expect from a system with two real, negative poles.

This technique is the final step in the Laplace transform method for solving differential equations. The complete pipeline: (1) transform the ODE into an algebraic equation for F(s), using the derivative properties from your table; (2) solve algebraically for F(s); (3) decompose F(s) by partial fractions; (4) invert term by term to recover f(t). Each step reduces complexity — an ODE becomes an algebra problem, and the algebra is solved by pattern-matching to known transforms. The inverse transform is what converts the s-domain answer back into the actual time-domain solution you need.
