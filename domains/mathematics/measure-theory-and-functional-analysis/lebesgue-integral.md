---
id: lebesgue-integral
title: Lebesgue Integral (Full Construction)
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: simple-functions-approximation
  type: hard
builds-toward:
- riemann-lebesgue-comparison
- product-measures-fubini-theorem
tags:
- integration
stage: expert
status: draft
---

# Lebesgue Integral (Full Construction)

## Core Idea
The Lebesgue integral is defined for simple functions as ∫s dμ = Σ aᵢμ(Eᵢ), extended to non-negative measurable functions by monotone supremum, then to general functions via positive and negative parts. This construction unifies and extends Riemann integration.

## Questions

```yaml
- question: "How does the Lebesgue integral fundamentally differ from the Riemann integral in its approach to computing the area under a curve?"
  type: multiple-choice
  options:
    - "The Lebesgue integral uses narrower x-axis subintervals, giving greater precision than Riemann sums"
    - "The Lebesgue integral partitions the range of the function and measures the preimage of each value band, rather than partitioning the domain into subintervals"
    - "The Lebesgue integral requires the function to be continuous, while Riemann works for any bounded function"
    - "The Lebesgue integral sums left endpoints of x-axis intervals while Riemann uses right endpoints or midpoints"
  answer: 1
  explanation: "The key structural inversion: Riemann partitions the *domain* (x-axis) into subintervals and approximates the function height on each. Lebesgue partitions the *range* (y-axis) into value bands and measures the *preimage* (the set of x-values where f takes that value) using measure μ. This inversion is why Lebesgue handles discontinuous functions: what matters is the measure of the set of discontinuities, not their structural complexity. A function discontinuous on a dense set (like the Dirichlet function) can still have a preimage with well-defined measure."

- question: "To integrate a general measurable function f that takes both positive and negative values, the Lebesgue construction proceeds by:"
  type: multiple-choice
  options:
    - "Integrating |f| first, then adjusting sign based on where f is negative"
    - "Splitting f into f⁺ = max(f, 0) and f⁻ = max(−f, 0), integrating each separately as non-negative functions, then computing ∫f⁺ dμ − ∫f⁻ dμ"
    - "Approximating f directly by a sequence of simple functions that can take both positive and negative values"
    - "Restricting the construction to the domain where f > 0 and separately to where f < 0, then summing the results"
  answer: 1
  explanation: "The f⁺ − f⁻ splitting is the canonical third stage of the Lebesgue construction. Both f⁺ and f⁻ are non-negative measurable functions, so they can be integrated by the monotone-supremum construction for non-negative functions. Subtracting gives ∫f dμ = ∫f⁺ dμ − ∫f⁻ dμ, defined when at least one of the terms is finite. When both are finite, f is called Lebesgue integrable (f ∈ L¹). Option A (integrating |f|) gives the L¹ norm, not the integral itself — the sign information is lost."

- question: "There exist functions that are Lebesgue integrable but not Riemann integrable — the Lebesgue integral strictly extends the class of integrable functions."
  type: true-false
  answer: true
  explanation: "The Dirichlet function — equal to 1 on rationals, 0 on irrationals — is the standard example. Its Riemann integral does not exist (upper and lower Riemann sums always differ by 1). But its Lebesgue integral is 0: the preimage of the value 1 is the rationals, which have measure zero; the preimage of 0 is the irrationals, which have measure 1. So ∫f dμ = 1·μ(ℚ∩[0,1]) + 0·μ(irrationals) = 1·0 + 0·1 = 0. Every Riemann integrable function is also Lebesgue integrable with the same value, but not vice versa."

- question: "The Lebesgue integral of a simple function is computed by partitioning the x-axis into subintervals and summing height times width on each interval, just as in Riemann integration."
  type: true-false
  answer: false
  explanation: "This is the Riemann approach, not the Lebesgue approach. The Lebesgue integral of a simple function s = Σ aᵢ · 𝟙_{Eᵢ} is ∫s dμ = Σ aᵢ · μ(Eᵢ), where the Eᵢ are the level sets of s — the sets where s takes the value aᵢ. These sets can be any measurable sets, not just intervals. On the real line with Lebesgue measure, if Eᵢ happens to be an interval [c,d], then μ(Eᵢ) = d − c and you recover the Riemann formula — but the Lebesgue definition works for Eᵢ being a Cantor set, a union of scattered points, or any other measurable set."

- question: "Why can the Lebesgue integral handle highly discontinuous functions (like the Dirichlet function) that the Riemann integral cannot? Explain in terms of how each construction approximates the function."
  type: short-answer
  answer: "Riemann integration approximates by partitioning the domain into intervals and summing height × width. Highly discontinuous functions cause the upper and lower Riemann sums to disagree no matter how fine the partition — because any interval contains both large and small values of f. Lebesgue integration partitions the *range* and measures the *preimage* of each value band. For the Dirichlet function, the preimage of {1} is ℚ (measure zero) and the preimage of {0} is the irrationals (measure 1). These preimage sets have well-defined measure even though they are structurally complex. The key shift: the measure of the set of discontinuities matters, not the discontinuities' positions relative to intervals."
  explanation: "This is the philosophical heart of measure theory: the right way to measure 'size' of a set of bad points is not by covering them with intervals (which fails for dense sets like ℚ) but by assigning them a measure via σ-algebras. Once you have a good notion of measure, integration follows by measuring preimage sets rather than domain intervals. The Lebesgue construction thus decouples the geometric structure of the domain from the notion of 'how much of the domain' a set of function values covers — and that decoupling is what gives Lebesgue integration its power."
```

## Explainer

From your work with simple functions, you know that a **simple function** takes only finitely many values: s(x) = a₁ on set E₁, a₂ on E₂, ..., aₙ on Eₙ, where these sets partition the domain. You can think of a simple function as a step function where the steps need not be intervals — they can be any measurable sets. The Lebesgue integral of such a function is defined by the obvious formula: ∫s dμ = Σ aᵢ · μ(Eᵢ). Each term is the height of a step times the measure (size) of the set where that step occurs. This is the entire foundation — everything else is a careful limit process built on this base.

To integrate a **non-negative measurable function** f, you approximate it from below by simple functions. The key idea: for any such f, there is an increasing sequence of simple functions sₙ with sₙ(x) ↑ f(x) pointwise. The integral of f is defined as the supremum of the integrals of all such approximating simple functions: ∫f dμ = sup{∫s dμ : s simple, 0 ≤ s ≤ f}. Because the approximating functions increase to f, and their integrals are already defined, this supremum captures the "total area" under f — even if f is unbounded or has complicated discontinuities. The Monotone Convergence Theorem then guarantees that this limit behaves as expected.

For a **general measurable function** f (which may be positive, negative, or both), write f = f⁺ - f⁻ where f⁺(x) = max(f(x), 0) is the positive part and f⁻(x) = max(-f(x), 0) is the negative part. Both f⁺ and f⁻ are non-negative, so they are already integrable by the construction above. Then ∫f dμ = ∫f⁺ dμ - ∫f⁻ dμ, provided at least one of these is finite. If both are finite, f is called **Lebesgue integrable**, and we write f ∈ L¹(μ).

The power of this construction becomes clear when you compare it to Riemann integration. The Riemann integral partitions the *domain* into subintervals and sums widths times heights. The Lebesgue integral partitions the *range* into value bands and sums values times the measure of the preimage. This inversion is why Lebesgue handles badly-discontinuous functions that Riemann cannot: the measure of a set of discontinuities matters, not the structure of those discontinuities as a subset of the x-axis. The construction through simple functions, monotone limits, and positive/negative splitting is the full, rigorous answer to the question: what does it mean to integrate a general measurable function?
