---
id: monotone-convergence-theorem-analysis
title: Monotone Convergence Theorem
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lebesgue-integral-non-negative
  type: hard
builds-toward:
- fatou-lemma-measure-theory
- dominated-convergence-theorem
tags:
- convergence-theorems
stage: abstract-reasoning
status: draft
---

# Monotone Convergence Theorem

## Core Idea
If 0 ≤ fₙ ≤ f_{n+1} pointwise for all n and fₙ → f, then ∫fₙ dμ → ∫f dμ. This is the most fundamental convergence theorem for the Lebesgue integral, allowing us to interchange limit and integral under monotonicity.

## Explainer

One of the central challenges in integration theory — which you encountered when building the Lebesgue integral for non-negative functions — is determining when you can swap a limit and an integral: ∫(lim fₙ) = lim ∫fₙ. For Riemann integrals, the swap requires uniform convergence, a very stringent condition. The **Monotone Convergence Theorem** (MCT) shows that for the Lebesgue integral, pointwise monotone convergence is enough, making it a far more powerful tool.

The theorem says: if 0 ≤ f₁ ≤ f₂ ≤ f₃ ≤ ... pointwise and fₙ → f pointwise, then ∫fₙ dμ → ∫f dμ (with the limit possibly being +∞). The key insight is that the integrals ∫fₙ form a non-decreasing sequence of non-negative extended real numbers — they converge to a limit in [0, ∞], with no oscillation possible. The Lebesgue integral was built to handle exactly this situation: it measures "area under the curve" by approximating from below with simple functions (finite linear combinations of indicator functions), and monotone convergence means those approximations converge to the right answer without any mass being lost or gained.

A concrete example anchors the intuition. Let fₙ = χ_{[0,n]} on ℝ with Lebesgue measure — the indicator function of the interval [0, n]. The sequence is increasing (fₙ(x) ≤ f_{n+1}(x) everywhere), and fₙ → f = χ_{[0,∞)} pointwise. The integrals are ∫fₙ dλ = n → ∞ = ∫f dλ. The MCT applies, and the conclusion is that both sides are ∞ — the theorem handles infinite limits gracefully without requiring any finiteness assumption.

The MCT is not just a convergence result — it is the constructive engine for the entire Lebesgue integration theory. Any non-negative measurable function f can be approximated from below by an increasing sequence of **simple functions** sₙ ↑ f (this is a standard construction using dyadic approximations). Defining ∫f dμ = lim ∫sₙ dμ is consistent and well-defined precisely because the MCT guarantees the limit exists and is independent of the approximating sequence. Everything built afterward — Fatou's Lemma, the Dominated Convergence Theorem, L^p spaces — relies on this foundation. The non-negativity and monotonicity hypotheses are not just technical conveniences; they are exactly what prevents the mass-escaping behavior that makes unconstrained limits of integrals unreliable.
