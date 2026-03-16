---
id: dominated-convergence-theorem
title: Dominated Convergence Theorem
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: lebesgue-integral-general-definition
  type: hard
builds-toward:
- lp-space-completeness-riesz-fischer
tags:
- convergence-theorems
stage: abstract-reasoning
status: draft
---

# Dominated Convergence Theorem

## Core Idea
If fₙ → f pointwise a.e. and |fₙ| ≤ g with ∫g < ∞, then ∫fₙ → ∫f. This is the most powerful convergence theorem, requiring only pointwise a.e. convergence and an integrable dominating function.

## How It's Best Learned
Apply to sequences shrinking to zero outside growing intervals, or bounded sequences on finite-measure sets.

## Common Misconceptions
The dominating function must be integrable; |fₙ| ≤ g pointwise is insufficient if ∫g = ∞. Without a dominating function, DCT does not apply.

## Explainer

From your study of the Lebesgue integral, you know that Lebesgue integration is more powerful than Riemann integration partly because it handles limits better. The central question in analysis is: when can you swap a limit with an integral? That is, when does ∫ lim fₙ = lim ∫ fₙ? Without restrictions, this swap can fail catastrophically. Consider the sequence fₙ = n · 1_{(0, 1/n)}: each function integrates to 1, yet fₙ → 0 pointwise almost everywhere. The limit of integrals is 1, but the integral of the limit is 0. The **Dominated Convergence Theorem (DCT)** gives precise conditions under which the swap is safe.

The theorem states: if a sequence fₙ converges **pointwise almost everywhere** to a function f, and if there exists an integrable function g — called a **dominating function** — such that |fₙ(x)| ≤ g(x) for almost every x and every n, then f is integrable and ∫fₙ → ∫f. The role of g is to act as a uniform leash on the entire sequence. No matter how wildly fₙ might oscillate or concentrate at individual points, as long as the whole sequence stays uniformly below g — and g itself has finite integral — the integral can't "escape to infinity" in the limit. The Lebesgue measure's ability to control mass on sets of small measure is what makes this work.

To understand why the integrability of g is non-negotiable: if g has infinite integral, the sequence could redistribute mass without limit even while converging pointwise. The example fₙ = 1_{[n, n+1]} converges pointwise to 0, so ∫f = 0, but ∫fₙ = 1 for all n. The natural dominating candidate g = 1 fails here only because ∫ℝ 1 = ∞; there is no integrable dominating function on ℝ for this sequence. The lesson is that both conditions — pointwise convergence and a genuine (finite-integral) dominator — are load-bearing.

In practice, the DCT is the workhorse of Lebesgue integration. When you need to differentiate under an integral sign, compute Fourier transforms, or pass a parameter through an integral, you typically exhibit a dominating function and invoke DCT to justify the exchange. For functions on a **finite-measure set** with a **bounded** sequence, the dominating function is just the bound times the characteristic function of the set — a convenient package that makes DCT almost automatic. The harder applications require finding a creative dominator, which is where the analytical depth of the theorem lives.
