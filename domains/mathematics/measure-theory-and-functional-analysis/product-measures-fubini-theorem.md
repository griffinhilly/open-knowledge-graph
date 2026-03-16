---
id: product-measures-fubini-theorem
title: Product Measures and Fubini's Theorem
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lebesgue-measure-euclidean-space
  type: hard
- id: lebesgue-integral
  type: hard
builds-toward:
- fourier-series-lp-theory
tags:
- product-measures
- integration
stage: advanced
status: draft
---

# Product Measures and Fubini's Theorem

## Core Idea
The product of two σ-finite measure spaces has a natural product measure. Fubini's theorem guarantees that integrable functions on product spaces can be iterated: ∫∫f dμ dν = ∫(∫f(x,y) dν(y)) dμ(x).

## Explainer

When you computed double integrals in calculus, you likely switched freely between ∫∫f(x,y) dy dx and ∫∫f(x,y) dx dy without much worry. Fubini's theorem is the rigorous justification for this exchange — and it reveals precisely when that exchange is *not* valid.

Start with the **product measure** construction. If (X, μ) and (Y, ν) are two measure spaces, their product space X × Y carries a natural measure μ × ν defined on "rectangles" A × B by (μ × ν)(A × B) = μ(A) · ν(B). This extends to a full σ-algebra on the product space using the standard Carathéodory extension from your measure theory prerequisites. Lebesgue measure on ℝ² is exactly the product of two copies of Lebesgue measure on ℝ: the measure of a rectangle is its width times its height.

**Fubini's theorem** then says: if f is integrable on the product space (meaning ∫|f| d(μ × ν) < ∞), then for μ-almost every x, the function y ↦ f(x, y) is ν-integrable; the function x ↦ ∫f(x,y) dν(y) is μ-integrable; and the iterated integrals equal the double integral. Moreover, the two orders of iteration give the same answer: ∫(∫f(x,y) dν(y)) dμ(x) = ∫(∫f(x,y) dμ(x)) dν(y). This is the "switch the order of integration" theorem from multivariable calculus, now on firm footing.

The **σ-finiteness condition** and the **integrability condition** are not just technicalities. Without integrability, iteration order can change the answer. The classic counterexample is f(x,y) = (x² − y²)/(x² + y²)² on [0,1] × [0,1]: one iterated integral gives +π/4 and the other gives −π/4. Fubini's theorem excludes this because f is not integrable (the absolute value has infinite integral). The theorem tells you: if ∫|f| d(μ × ν) < ∞, you're safe. If you're unsure, apply **Tonelli's theorem** first: for non-negative f, the iterated integrals always equal each other (possibly being ∞), so you can use Tonelli to check integrability before invoking Fubini for the sign-sensitive version.
