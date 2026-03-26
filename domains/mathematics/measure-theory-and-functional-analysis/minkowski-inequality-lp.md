---
id: minkowski-inequality-lp
title: Minkowski's Inequality for L^p Spaces
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lp-norm-metric
  type: hard
- id: holders-inequality
  type: soft
builds-toward:
- lp-space-completeness-riesz-fischer
tags:
- lp-spaces
- triangle-inequality
stage: expert
status: validated
---
# Minkowski's Inequality for L^p Spaces

## Core Idea
Minkowski's inequality asserts ‖f + g‖_p ≤ ‖f‖_p + ‖g‖_p for all f, g ∈ L^p. This is the triangle inequality, establishing that L^p is a normed space. It follows from Hölder's inequality.

## Questions

```yaml
- question: "Why is Minkowski's inequality for L^p spaces considered a foundational result, beyond being a useful estimate?"
  type: multiple-choice
  options:
    - "It provides a computable formula for calculating the L^p norm of a sum of two functions"
    - "It establishes the triangle inequality, thereby certifying that L^p with the p-norm is a normed vector space"
    - "It shows that L^p functions are bounded almost everywhere"
    - "It generalizes the Cauchy-Schwarz inequality to arbitrary exponents p"
  answer: 1
  explanation: "The triangle inequality — ‖f + g‖_p ≤ ‖f‖_p + ‖g‖_p — is the hardest of the three normed space axioms to verify for L^p (positivity and scaling are straightforward). Without it, L^p would have a notion of size but no guarantee that adding functions behaves consistently with that size. Minkowski's inequality supplies this missing axiom, completing the verification that L^p is a normed vector space. Combined with completeness (Riesz-Fischer), it makes L^p a Banach space. Option D conflates Minkowski with Hölder, which actually generalizes Cauchy-Schwarz."

- question: "A student tries to prove ‖f + g‖_p ≤ ‖f‖_p + ‖g‖_p for 1 < p < ∞ by using the pointwise inequality |f(x) + g(x)| ≤ |f(x)| + |g(x)|, raising both sides to the p-th power, and integrating. Why does this approach fail?"
  type: multiple-choice
  options:
    - "The pointwise triangle inequality |f + g| ≤ |f| + |g| is false for general L^p functions"
    - "Raising both sides to the p-th power and integrating does not give the right bound, because (a + b)^p ≠ a^p + b^p for p > 1"
    - "The approach fails because L^p does not contain pointwise-defined functions"
    - "The pointwise inequality gives a lower bound for |f + g|, not an upper bound"
  answer: 1
  explanation: "The pointwise triangle inequality is valid, but (a + b)^p ≥ a^p + b^p when a, b ≥ 0 and p > 1 — so integrating after taking the p-th power gives ∫|f + g|^p ≤ ∫(|f| + |g|)^p, which does NOT imply ‖f + g‖_p ≤ ‖f‖_p + ‖g‖_p. The correct proof must use Hölder's inequality: factor |f + g|^p = |f + g| · |f + g|^(p-1), apply the pointwise bound to the first factor, then apply Hölder to each integral term. The nonlinearity of the p-th power is precisely what makes this case nontrivial."

- question: "Minkowski's inequality for L^p relies on Hölder's inequality in its proof for 1 < p < ∞."
  type: true-false
  answer: true
  explanation: "The proof for 1 < p < ∞ works by factoring ‖f + g‖_p^p = ∫|f + g| · |f + g|^(p-1) dμ, bounding the first factor pointwise, and applying Hölder's inequality with conjugate exponents (p, q) where 1/p + 1/q = 1 to each resulting integral. The Hölder conjugate relationship makes the algebra close: ‖|f+g|^(p-1)‖_q = ‖f+g‖_p^(p-1), and dividing both sides by this factor yields the inequality. Hölder is the engine of the proof; Minkowski is a consequence."

- question: "Minkowski's inequality ‖f + g‖_p ≤ ‖f‖_p + ‖g‖_p holds for most p > 0."
  type: true-false
  answer: false
  explanation: "Minkowski's inequality requires p ≥ 1. For 0 < p < 1, the triangle inequality *fails* — the quantity (∫|f|^p dμ)^(1/p) does not define a norm because it is not subadditive. This is why L^p spaces as normed (and Banach) spaces require p ≥ 1. The boundary cases p = 1 and p = ∞ have direct proofs; the Hölder-based argument handles 1 < p < ∞. Knowing where the inequality breaks is as important as knowing where it holds."

- question: "Explain why the p = 1 case of Minkowski's inequality is immediate, and why the case 1 < p < ∞ requires a more indirect argument."
  type: short-answer
  answer: "For p = 1: ‖f + g‖₁ = ∫|f + g| dμ ≤ ∫(|f| + |g|) dμ = ‖f‖₁ + ‖g‖₁. This works directly because integration is linear and the pointwise triangle inequality integrates as-is. For 1 < p < ∞: the p-th power is nonlinear, so integrating (|f| + |g|)^p produces mixed cross-terms rather than a clean separation. The proof must factor |f + g|^p = |f + g| · |f + g|^(p-1), apply the pointwise bound to the first factor, and then use Hölder's inequality to control each integral. The Hölder conjugate relationship makes the algebra close."
  explanation: "The p = 1 case is elementary because addition and integration interact simply when the exponent is 1. The nonlinearity introduced by p-th powers for p > 1 requires the indirect approach via Hölder. This is a recurring pattern in analysis: linear estimates come directly, nonlinear ones require a conjugate tool. Hölder pairs two functions via conjugate exponents and provides the leverage needed to control the nonlinear interaction — which is why Minkowski's inequality is, in this sense, a corollary of Hölder's."
```

## Explainer

From your study of the Lᵖ norm, you know that ‖f‖_p = (∫|f|ᵖ dμ)^(1/p) measures the size of a function in a way that generalizes the Euclidean norm on Rⁿ. For a collection of functions to form a normed vector space, the most demanding axiom to verify — after checking linearity of the space and positivity of the norm — is the **triangle inequality**: the norm of a sum cannot exceed the sum of the norms. Minkowski's inequality asserts exactly this holds for Lᵖ: ‖f + g‖_p ≤ ‖f‖_p + ‖g‖_p for all 1 ≤ p ≤ ∞.

For p = 1 and p = ∞ the inequality follows directly. When p = 1: ‖f + g‖₁ = ∫|f + g| dμ ≤ ∫(|f| + |g|) dμ = ‖f‖₁ + ‖g‖₁, using the pointwise triangle inequality |f(x) + g(x)| ≤ |f(x)| + |g(x)| and linearity of integration. When p = ∞: ‖f + g‖_∞ = ess sup|f + g| ≤ ess sup(|f| + |g|) ≤ ess sup|f| + ess sup|g|. The nontrivial case is 1 < p < ∞, where the pth power is nonlinear and pointwise bounds must be integrated in a more indirect way.

The proof for 1 < p < ∞ uses **Hölder's inequality** as its engine. Factor |f + g|ᵖ = |f + g| · |f + g|^(p−1), then bound |f + g| ≤ |f| + |g| to get ‖f + g‖_pᵖ ≤ ∫|f||f+g|^(p-1) dμ + ∫|g||f+g|^(p-1) dμ. Apply Hölder to each integral with exponent pair (p, q) where 1/p + 1/q = 1: each term bounds to ‖f‖_p · ‖|f+g|^(p-1)‖_q and ‖g‖_p · ‖|f+g|^(p-1)‖_q. Since (p−1)q = p, the factor ‖|f+g|^(p-1)‖_q = ‖f+g‖_p^(p-1). Dividing both sides by that factor yields the inequality. The Hölder conjugate relationship makes the algebra close cleanly.

The consequence is conceptual as much as computational: Minkowski's inequality is what certifies Lᵖ as a normed vector space. Without it, Lᵖ would be a set with a notion of size but no guarantee that sums behave consistently. With it, Lᵖ has the full structure of a **normed vector space** — and since it is also complete (the Riesz-Fischer theorem), it is a **Banach space**. The entire functional-analytic theory of Lᵖ spaces — dual spaces, bounded operators, spectral theory — rests on Minkowski supplying the triangle inequality.
