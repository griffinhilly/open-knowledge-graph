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
stage: expert
status: draft
---

# Product Measures and Fubini's Theorem

## Core Idea
The product of two σ-finite measure spaces has a natural product measure. Fubini's theorem guarantees that integrable functions on product spaces can be iterated: ∫∫f dμ dν = ∫(∫f(x,y) dν(y)) dμ(x).

## Questions

```yaml
- question: "A function f on [0,1] × [0,1] has one iterated integral equal to +π/4 and the other equal to −π/4. What does this tell you about f?"
  type: multiple-choice
  options:
    - "f is discontinuous, so the Riemann integral cannot be applied"
    - "f is not Lebesgue integrable — its absolute value has infinite integral, so Fubini's theorem does not apply"
    - "The σ-algebras on the two copies of [0,1] are incompatible"
    - "A computational error was made — Fubini's theorem guarantees both iterated integrals are equal for any measurable f"
  answer: 1
  explanation: "This is the classic counterexample: f(x,y) = (x²−y²)/(x²+y²)² on [0,1]×[0,1]. The two iterated integrals give +π/4 and −π/4 because f is not Lebesgue integrable — ∫|f| d(μ×ν) = ∞. Fubini's theorem only guarantees equality of iterated integrals when the function is integrable. Option D is the most dangerous misconception: Fubini does NOT apply to all measurable functions, only to integrable ones."

- question: "You want to compute ∫∫f(x,y) dμ dν but are unsure whether f is integrable. What is the correct strategy?"
  type: multiple-choice
  options:
    - "Apply Fubini's theorem directly — it works for all σ-finite measure spaces"
    - "Average the two iterated integrals to obtain the correct value"
    - "Apply Tonelli's theorem to ∫∫|f| first: since |f| ≥ 0, Tonelli guarantees the iterated integrals of |f| are equal, allowing you to check whether ∫|f| d(μ×ν) < ∞ before invoking Fubini"
    - "Differentiate under the integral sign to simplify the integrand"
  answer: 2
  explanation: "Tonelli's theorem is the safety check that unlocks Fubini. For non-negative functions, Tonelli guarantees the two iterated integrals always agree (possibly being ∞), so you can compute ∫(∫|f(x,y)|dν)dμ in whichever order is convenient. If this equals a finite number, f is integrable and Fubini applies to f itself — you can switch orders freely. If it equals ∞, Fubini is inapplicable and switching orders may give different answers. Tonelli → Fubini is the standard workflow."

- question: "Fubini's theorem guarantees that for any measurable function f on a product of σ-finite measure spaces, the two iterated integrals are equal."
  type: true-false
  answer: false
  explanation: "Fubini requires not just measurability but integrability: ∫|f| d(μ×ν) < ∞. Without this condition, switching integration order can yield different values — as demonstrated by f(x,y) = (x²−y²)/(x²+y²)² on [0,1]². The σ-finiteness condition is needed for the product measure construction, but it alone does not save you from the ordering problem. The integrability condition is the binding constraint for safe order-switching."

- question: "Lebesgue measure on ℝ² is the product of two copies of Lebesgue measure on ℝ, in the sense that the measure of a rectangle A × B equals the product of the measures of A and B."
  type: true-false
  answer: true
  explanation: "This is exactly how the product measure construction works: (μ × ν)(A × B) = μ(A) · ν(B) on measurable rectangles, then extended via Carathéodory to the full product σ-algebra. Lebesgue measure on ℝ² is precisely this product — the measure of a rectangle is width times height, consistent with the geometric notion of area. This concrete case motivates the abstract construction."

- question: "Why can switching the order of integration change the result for some functions, and what condition prevents this from happening?"
  type: short-answer
  answer: "When a function f has both large positive and large negative regions, the 'cancellation' between them can depend on which variable is integrated first — the partial integrals along one variable may diverge or accumulate differently. The condition that prevents this is absolute integrability: ∫|f| d(μ×ν) < ∞. When the integral of |f| is finite, the positive and negative parts of f each have finite integrals independently, so their contributions are unambiguous regardless of integration order."
  explanation: "This is the reason Fubini has a hypothesis rather than being a universal rule. In calculus courses, students switch integration order freely because the functions involved are typically continuous on bounded domains — integrability is implicit. In measure theory, the condition must be stated explicitly. The standard proof of Fubini proceeds by decomposing f = f⁺ − f⁻ into positive and negative parts, then applying Tonelli to each (both are non-negative). Integrability of f guarantees both f⁺ and f⁻ have finite integrals, making the decomposition valid and order-independent."
```

## Explainer

When you computed double integrals in calculus, you likely switched freely between ∫∫f(x,y) dy dx and ∫∫f(x,y) dx dy without much worry. Fubini's theorem is the rigorous justification for this exchange — and it reveals precisely when that exchange is *not* valid.

Start with the **product measure** construction. If (X, μ) and (Y, ν) are two measure spaces, their product space X × Y carries a natural measure μ × ν defined on "rectangles" A × B by (μ × ν)(A × B) = μ(A) · ν(B). This extends to a full σ-algebra on the product space using the standard Carathéodory extension from your measure theory prerequisites. Lebesgue measure on ℝ² is exactly the product of two copies of Lebesgue measure on ℝ: the measure of a rectangle is its width times its height.

**Fubini's theorem** then says: if f is integrable on the product space (meaning ∫|f| d(μ × ν) < ∞), then for μ-almost every x, the function y ↦ f(x, y) is ν-integrable; the function x ↦ ∫f(x,y) dν(y) is μ-integrable; and the iterated integrals equal the double integral. Moreover, the two orders of iteration give the same answer: ∫(∫f(x,y) dν(y)) dμ(x) = ∫(∫f(x,y) dμ(x)) dν(y). This is the "switch the order of integration" theorem from multivariable calculus, now on firm footing.

The **σ-finiteness condition** and the **integrability condition** are not just technicalities. Without integrability, iteration order can change the answer. The classic counterexample is f(x,y) = (x² − y²)/(x² + y²)² on [0,1] × [0,1]: one iterated integral gives +π/4 and the other gives −π/4. Fubini's theorem excludes this because f is not integrable (the absolute value has infinite integral). The theorem tells you: if ∫|f| d(μ × ν) < ∞, you're safe. If you're unsure, apply **Tonelli's theorem** first: for non-negative f, the iterated integrals always equal each other (possibly being ∞), so you can use Tonelli to check integrability before invoking Fubini for the sign-sensitive version.
