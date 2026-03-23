---
id: holders-inequality
title: Hölder's Inequality
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lp-norm-metric
  type: hard
builds-toward:
- minkowski-inequality-lp
tags:
- lp-spaces
- inequalities
stage: expert
status: draft
---

# Hölder's Inequality

## Core Idea
For 1 < p < ∞ with 1/p + 1/q = 1, Hölder's inequality states ∫|fg| ≤ ‖f‖_p ‖g‖_q. This is the key inequality enabling duality in L^p theory. When p = q = 2, it reduces to Cauchy–Schwarz.

## Questions

```yaml
- question: "A student wants to bound ∫|fg| dμ for functions f ∈ L³ and g ∈ L². She attempts to apply Hölder's inequality with p = 3 and q = 2. What is wrong with this approach?"
  type: multiple-choice
  options:
    - "Hölder's inequality only applies when f and g are in the same Lᵖ space"
    - "Hölder's inequality requires conjugate exponents satisfying 1/p + 1/q = 1; since 1/3 + 1/2 = 5/6 ≠ 1, the pair (3, 2) is not conjugate and the standard Hölder bound does not apply"
    - "The bound ‖f‖₃ ‖g‖₂ is valid whenever both exponents exceed 1"
    - "Hölder's inequality only applies to functions on probability spaces where the total measure is 1"
  answer: 1
  explanation: "The conjugate exponent condition 1/p + 1/q = 1 is not a technicality — it is precisely what makes the bound tight and what emerges from the proof via Young's inequality. For p = 3, the conjugate is q = 3/2 (since 1/3 + 2/3 = 1), not q = 2. The pair (3, 2) gives 1/3 + 1/2 = 5/6 < 1, and applying Hölder directly would be invalid. If g ∈ L² but not L^(3/2), a direct Hölder bound is not available; one would need to use a different inequality or interpolation."

- question: "When p = q = 2, Hölder's inequality reduces to a well-known classical inequality. Which one?"
  type: multiple-choice
  options:
    - "The triangle inequality for L² norms (Minkowski's inequality)"
    - "The Cauchy–Schwarz inequality: ∫|fg| ≤ ‖f‖₂ ‖g‖₂"
    - "Young's inequality for products: ab ≤ a²/2 + b²/2"
    - "Jensen's inequality for convex functions"
  answer: 1
  explanation: "When p = q = 2, the conjugate condition 1/2 + 1/2 = 1 is satisfied, and Hölder's inequality becomes ∫|fg| ≤ ‖f‖₂ ‖g‖₂ — precisely the Cauchy–Schwarz inequality in L². This reveals Cauchy–Schwarz as a special case of a more general phenomenon. Hölder's inequality generalizes it to all conjugate pairs (p, q) with 1/p + 1/q = 1 and p, q ∈ (1, ∞), showing that the bounding of ∫|fg| by separate norms is a feature of the conjugate structure, not special to L²."

- question: "The conjugate condition 1/p + 1/q = 1 in Hölder's inequality is an arbitrary technical restriction; with additional work, the inequality could be extended to non-conjugate pairs."
  type: true-false
  answer: false
  explanation: "The conjugate condition is not arbitrary — it is precisely what emerges from the proof. The standard argument normalizes f and g to have unit Lᵖ and Lq norms, then applies Young's inequality pointwise: |f(x)g(x)| ≤ |f(x)|ᵖ/p + |g(x)|^q/q. Integrating both sides gives ∫|fg| ≤ 1/p + 1/q. For this to equal 1 (recovering the desired bound of ‖f‖_p ‖g‖_q after un-normalizing), we need exactly 1/p + 1/q = 1. The conjugate condition is what makes the proof work, not an afterthought."

- question: "Hölder's inequality is essential to Lᵖ duality theory because it provides the bound showing that integration against a function in Lq defines a bounded linear functional on Lᵖ — a fact central to the Riesz representation theorem."
  type: true-false
  answer: true
  explanation: "This is the deep significance of Hölder's inequality beyond computation. Every bounded linear functional on Lᵖ can be represented as Λ(f) = ∫fg dμ for some g ∈ Lq (where 1/p + 1/q = 1). Hölder's inequality is what makes this functional bounded: |Λ(f)| = |∫fg| ≤ ‖f‖_p ‖g‖_q. Without this bound, the correspondence (Lᵖ)* ≅ Lq would not be well-defined as a bounded isomorphism. Hölder is also used directly in proving Minkowski's inequality (the triangle inequality for Lᵖ norms), so it is load-bearing for the entire structure of Lᵖ space theory."

- question: "Explain the role of Hölder's inequality in establishing the duality between Lᵖ and Lq spaces, and why the conjugate exponent condition is essential to this duality."
  type: short-answer
  answer: "The Riesz representation theorem for Lᵖ spaces states that every bounded linear functional Λ on Lᵖ(μ) can be represented as Λ(f) = ∫fg dμ for a unique g ∈ Lq, where 1/p + 1/q = 1. Hölder's inequality provides the bound |∫fg| ≤ ‖f‖_p ‖g‖_q that proves this functional is bounded with norm at most ‖g‖_q. The conjugate condition is essential because it is precisely the condition under which Hölder holds — pairing Lᵖ with any other space does not yield a controlled bound. The duality (Lᵖ)* ≅ Lq is therefore built directly on the structure of Hölder's inequality: conjugate exponents are not just a technical convenience but the algebraic expression of the duality itself."
  explanation: "The conjugate condition 1/p + 1/q = 1 can be read as the statement that p and q are 'complementary' in a specific sense: their reciprocals sum to 1. This is precisely the algebraic condition that makes the Lᵖ-Lq pairing work, and Hölder's inequality is the analytic theorem that realizes that algebraic structure."
```

## Explainer

You already know the **Lᵖ norm** ‖f‖_p = (∫|f|ᵖ)^(1/p), which measures the "size" of a function in a way that weights extreme values more heavily as p grows. Hölder's inequality answers the question: how large can the integral of the product |fg| be, given that you know ‖f‖_p and ‖g‖_q? The answer is the elegant bound ∫|fg| ≤ ‖f‖_p ‖g‖_q — and the condition 1/p + 1/q = 1 is precisely what makes this tight.

The pair (p, q) satisfying 1/p + 1/q = 1 are called **conjugate exponents**. When p = 2, we get q = 2 as well, and Hölder's inequality becomes the Cauchy–Schwarz inequality ∫|fg| ≤ ‖f‖₂ ‖g‖₂ — a fact you may recognize from inner product spaces. Hölder generalizes this: for p = 3 and q = 3/2, Hölder's inequality handles situations where f has L³ integrability but g is only in L^(3/2). The conjugate condition is not arbitrary; it emerges from the proof via **Young's inequality** (ab ≤ aᵖ/p + bq/q for a, b ≥ 0), which in turn follows from the convexity of the exponential function.

The proof strategy is instructive: normalize by replacing f with f/‖f‖_p and g with g/‖g‖_q, reducing to the case where both norms are 1 and you need to show ∫|fg| ≤ 1. Then apply Young's inequality pointwise to get |f(x)g(x)| ≤ |f(x)|ᵖ/p + |g(x)|^q/q, and integrate both sides. The right-hand side integrates to 1/p + 1/q = 1. This argument reveals why the conjugate condition is necessary: it is exactly what makes Young's inequality integrate to 1.

The deepest significance of Hölder's inequality is its role in **Lᵖ duality**. Every bounded linear functional on Lᵖ can be represented as integration against some function in Lq — written symbolically as (Lᵖ)* ≅ Lq. This duality underpins the Riesz representation theorem and is central to functional analysis. Hölder's inequality is what makes this identification *bounded*: without it, you couldn't control ∫fg by separate norms. It also immediately implies the Minkowski inequality (triangle inequality for Lᵖ norms), which is the next step in the theory.
