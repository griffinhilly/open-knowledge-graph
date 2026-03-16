---
id: lp-space-completeness-riesz-fischer
title: Completeness of L^p Spaces (Riesz-Fischer Theorem)
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: minkowski-inequality-lp
  type: hard
builds-toward:
- banach-spaces-definition
tags:
- lp-spaces
- banach-spaces
stage: abstract-reasoning
status: draft
---

# Completeness of L^p Spaces (Riesz-Fischer Theorem)

## Core Idea
The Riesz-Fischer theorem states that L^p is complete: every Cauchy sequence in L^p converges to an L^p function. This makes L^p a Banach space and is essential for spectral theory and harmonic analysis.

## Explainer

From the Minkowski inequality you know that ‖f + g‖_p ≤ ‖f‖_p + ‖g‖_p, which makes Lᵖ a normed vector space. But a normed space is not automatically complete. The **Riesz-Fischer theorem** closes this gap: it proves that every Cauchy sequence in Lᵖ (1 ≤ p < ∞) converges to a function that is itself in Lᵖ. In other words, the limit of "functions that are getting close together in the Lᵖ sense" is still an Lᵖ function. This is the completeness property, and it is what makes Lᵖ a **Banach space**.

The proof strategy is illuminating. Given a Cauchy sequence {fₙ}, you extract a rapidly converging subsequence where ‖fₙₖ₊₁ − fₙₖ‖_p ≤ 2⁻ᵏ. You then construct the candidate limit by summing these incremental differences: f = f₁ + Σ(fₙₖ₊₁ − fₙₖ). Minkowski's inequality controls the partial sums, letting you apply the monotone convergence theorem to show the series converges a.e. and that the limit is in Lᵖ. The key step uses the fact that absolutely convergent series in Lᵖ are convergent — a direct consequence of the norm structure plus Minkowski.

The theorem has a subtle but essential technicality: Lᵖ functions are equivalence classes of functions, where two functions are identified if they differ on a set of measure zero. This is not a pedantic point — it is *required* for completeness. Without quotienting out null sets, a constant sequence fₙ = 1_ℚ (the indicator of the rationals) would converge to something outside the space. The quotient construction ensures the space is actually complete.

Why does this matter? Completeness is the prerequisite for virtually all of functional analysis. Fixed-point theorems, spectral theory, and variational methods require convergent sequences to stay within the space you are working in. Harmonic analysis in particular relies on Lᵖ completeness: the Fourier series of an L² function converges in the L² norm to that function — a result that requires knowing L² is complete. The Riesz-Fischer theorem is thus not an isolated result but the foundation on which Lᵖ analysis is built.
