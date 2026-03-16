---
id: lebesgue-integral-general-definition
title: 'Lebesgue Integral: General Definition'
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lebesgue-integral-non-negative
  type: hard
builds-toward:
- lebesgue-integral-properties
- riemann-vs-lebesgue-integrals
- dominated-convergence-theorem
tags:
- integration
- lebesgue-integral
stage: abstract-reasoning
status: draft
---

# Lebesgue Integral: General Definition

## Core Idea
For general measurable f, decompose f = f⁺ - f⁻ (positive and negative parts). If at least one of ∫f⁺ or ∫f⁻ is finite, define ∫f dμ = ∫f⁺ - ∫f⁻. Functions with ∫|f| < ∞ are integrable. This preserves linearity for signed functions.

## Explainer

You've already built the Lebesgue integral for non-negative measurable functions, starting with simple functions and taking monotone limits. That construction worked cleanly because all integrals were either finite non-negative numbers or +∞ — no cancellation issues. The challenge with a general function f is that it takes both positive and negative values, and subtracting two infinite quantities leads to the undefined expression ∞ − ∞.

The solution is a clean decomposition: define **f⁺(x) = max(f(x), 0)** (the positive part) and **f⁻(x) = max(−f(x), 0)** (the negative part, always non-negative). Then f = f⁺ − f⁻ everywhere, and |f| = f⁺ + f⁻. Both f⁺ and f⁻ are non-negative measurable functions, so the Lebesgue integral you already defined applies to each of them. The integral of f is then ∫f dμ = ∫f⁺ dμ − ∫f⁻ dμ, provided this subtraction is not ∞ − ∞.

The condition "at least one of ∫f⁺ or ∫f⁻ is finite" is exactly what prevents the ∞ − ∞ problem. If both are infinite, the integral is undefined — not zero, not infinite, but genuinely undefined, because the positive and negative contributions overwhelm each other with no well-defined net result. A function is called **integrable** (or in L¹) when the stronger condition ∫|f| dμ = ∫f⁺ dμ + ∫f⁻ dμ < ∞ holds, meaning both parts are individually finite. Integrability ensures well-defined, finite integrals with all the nice properties — linearity, dominated convergence — you'll use going forward.

This decomposition also reveals why linearity holds for signed functions. If f = f⁺ − f⁻ and g = g⁺ − g⁻, then (f + g) can be decomposed similarly, and the integral of the sum equals the sum of the integrals. The same argument fails to work cleanly with a direct Riemann-style definition for functions with complicated sign-change structure, which is one reason the Lebesgue theory is essential for handling functions that oscillate wildly or are defined on irregular domains.
