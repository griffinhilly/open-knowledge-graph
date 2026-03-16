---
id: minkowski-inequality-lp
title: Minkowski's Inequality for L^p Spaces
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lp-norm-metric
  type: hard
builds-toward:
- lp-space-completeness-riesz-fischer
tags:
- lp-spaces
- triangle-inequality
stage: abstract-reasoning
status: draft
---

# Minkowski's Inequality for L^p Spaces

## Core Idea
Minkowski's inequality asserts ‖f + g‖_p ≤ ‖f‖_p + ‖g‖_p for all f, g ∈ L^p. This is the triangle inequality, establishing that L^p is a normed space. It follows from Hölder's inequality.

## Explainer

From your study of the Lᵖ norm, you know that ‖f‖_p = (∫|f|ᵖ dμ)^(1/p) measures the size of a function in a way that generalizes the Euclidean norm on Rⁿ. For a collection of functions to form a normed vector space, the most demanding axiom to verify — after checking linearity of the space and positivity of the norm — is the **triangle inequality**: the norm of a sum cannot exceed the sum of the norms. Minkowski's inequality asserts exactly this holds for Lᵖ: ‖f + g‖_p ≤ ‖f‖_p + ‖g‖_p for all 1 ≤ p ≤ ∞.

For p = 1 and p = ∞ the inequality follows directly. When p = 1: ‖f + g‖₁ = ∫|f + g| dμ ≤ ∫(|f| + |g|) dμ = ‖f‖₁ + ‖g‖₁, using the pointwise triangle inequality |f(x) + g(x)| ≤ |f(x)| + |g(x)| and linearity of integration. When p = ∞: ‖f + g‖_∞ = ess sup|f + g| ≤ ess sup(|f| + |g|) ≤ ess sup|f| + ess sup|g|. The nontrivial case is 1 < p < ∞, where the pth power is nonlinear and pointwise bounds must be integrated in a more indirect way.

The proof for 1 < p < ∞ uses **Hölder's inequality** as its engine. Factor |f + g|ᵖ = |f + g| · |f + g|^(p−1), then bound |f + g| ≤ |f| + |g| to get ‖f + g‖_pᵖ ≤ ∫|f||f+g|^(p-1) dμ + ∫|g||f+g|^(p-1) dμ. Apply Hölder to each integral with exponent pair (p, q) where 1/p + 1/q = 1: each term bounds to ‖f‖_p · ‖|f+g|^(p-1)‖_q and ‖g‖_p · ‖|f+g|^(p-1)‖_q. Since (p−1)q = p, the factor ‖|f+g|^(p-1)‖_q = ‖f+g‖_p^(p-1). Dividing both sides by that factor yields the inequality. The Hölder conjugate relationship makes the algebra close cleanly.

The consequence is conceptual as much as computational: Minkowski's inequality is what certifies Lᵖ as a normed vector space. Without it, Lᵖ would be a set with a notion of size but no guarantee that sums behave consistently. With it, Lᵖ has the full structure of a **normed vector space** — and since it is also complete (the Riesz-Fischer theorem), it is a **Banach space**. The entire functional-analytic theory of Lᵖ spaces — dual spaces, bounded operators, spectral theory — rests on Minkowski supplying the triangle inequality.
