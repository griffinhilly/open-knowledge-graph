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
- laplace-transform-derivatives
tags:
- inverse-transform
- partial-fractions
- recovery
stage: formal-systems
status: draft
---

# Inverse Laplace Transform and Partial Fractions

## Core Idea
To recover f(t) from F(s), decompose F(s) = P(s)/Q(s) using partial fractions, then apply the inverse Laplace transform to each term via tables. This converts a challenging inversion problem into algebra and table lookup. The partial fraction decomposition handles poles (roots of the denominator), with simple poles giving exponential terms and complex conjugate poles giving oscillatory terms.

## Explainer

You've built a table of Laplace transform pairs — functions f(t) and their transforms F(s) — and you've practiced decomposing rational functions into simpler fractions using partial fractions. The **inverse Laplace transform** closes the loop: given F(s) in the s-domain, recover f(t) in the time domain. The challenge is that F(s) is rarely in a form that directly matches any table entry. It arrives as a rational function P(s)/Q(s) whose denominator has multiple roots, none of which look like simple table entries on their own.

The strategy is partial fractions first, then table lookup. Partial fractions rewrites F(s) as a sum of simpler terms, each of which *does* match a table entry. The structure of the denominator determines which terms appear. A simple real root at s = a contributes a term A/(s − a), whose inverse transform is Ae^{at}. A repeated root at s = a of order k contributes A₁/(s − a) + A₂/(s − a)² + ··· + Aₖ/(s − a)ᵏ, whose inverses involve tʲe^{at}. Complex conjugate roots s = α ± βi combine into terms of the form (As + B)/((s − α)² + β²), whose inverses give e^{αt}cos(βt) and e^{αt}sin(βt) — exponentially-modulated oscillations.

Work through a simple example: F(s) = 1/(s² + 4s + 3). Factor the denominator: s² + 4s + 3 = (s + 1)(s + 3). Decompose: 1/((s+1)(s+3)) = A/(s+1) + B/(s+3). Clear denominators: 1 = A(s+3) + B(s+1). Setting s = −1 gives A = 1/2; setting s = −3 gives B = −1/2. So F(s) = (1/2)/(s+1) − (1/2)/(s+3). From the table, L⁻¹{1/(s − a)} = e^{at}, so f(t) = (1/2)e^{−t} − (1/2)e^{−3t}. This is a sum of two decaying exponentials — exactly what you'd expect from a system with two real, negative poles.

This technique is the final step in the Laplace transform method for solving differential equations. The complete pipeline: (1) transform the ODE into an algebraic equation for F(s), using the derivative properties from your table; (2) solve algebraically for F(s); (3) decompose F(s) by partial fractions; (4) invert term by term to recover f(t). Each step reduces complexity — an ODE becomes an algebra problem, and the algebra is solved by pattern-matching to known transforms. The inverse transform is what converts the s-domain answer back into the actual time-domain solution you need.
