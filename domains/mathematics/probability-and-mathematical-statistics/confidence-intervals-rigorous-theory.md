---
id: confidence-intervals-rigorous-theory
title: Confidence Intervals (Rigorous Theory)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: asymptotic-normality-mle
  type: hard
- id: uniformly-most-powerful-tests
  type: soft
builds-toward:
- bayesian-inference-foundations
tags:
- confidence-intervals
- interval-estimation
- statistics
stage: advanced
status: draft
---

# Confidence Intervals (Rigorous Theory)

## Core Idea
A (1-α) confidence interval [L(X), U(X)] for θ satisfies P(L(X) ≤ θ ≤ U(X)) = 1 - α. Confidence intervals can be inverted from hypothesis tests: the (1-α) CI is {θ: θ is not rejected at level α}. Shortest confidence intervals use the critical region from the UMP test. Asymptotic CIs rely on asymptotic normality of estimators.

## Explainer

From asymptotic normality of the MLE, you know that under regularity conditions √n(θ̂_MLE − θ) → N(0, I(θ)⁻¹) in distribution, where I(θ) is the Fisher information. This immediately suggests a confidence interval: rearrange the normal approximation to get θ̂ ± z_{α/2}/√(n·I(θ)). But to call this a *confidence interval* rigorously requires a precise definition — one with a subtlety that most introductory treatments skip.

A **confidence interval** [L(X), U(X)] is formally a pair of statistics (functions of data, not of the unknown θ) satisfying P_θ(L(X) ≤ θ ≤ U(X)) ≥ 1 − α for *all* θ in the parameter space. Notice the direction of randomness: θ is fixed (though unknown), and the interval is random because L and U depend on the data X. The statement "there is a 95% probability that θ lies in this interval" is literally false once data is observed — θ either is or is not in the realized interval. The correct interpretation is frequentist: if you repeated the experiment and CI construction many times, at least (1−α)·100% of the resulting intervals would contain the true θ.

The **test inversion principle** connects CIs to hypothesis testing. For each candidate value θ₀, consider the level-α test of H₀: θ = θ₀. Let A(θ₀) be the acceptance region of this test. Define the confidence set C(X) = {θ₀ : X ∈ A(θ₀)} — the set of all parameter values that the data would not reject. Then P_θ(θ ∈ C(X)) = P_θ(X ∈ A(θ)) = 1 − α, so C(X) is a valid (1−α) confidence set. This is an exact equality, not just an analogy. When the test is **UMP** (uniformly most powerful), the resulting CI is the shortest possible at that confidence level — test optimality translates directly into CI optimality.

Asymptotic CIs fill the practical gap. Exact CIs exist in closed form only for special families (exponential family, location-scale). For most problems, the MLE's asymptotic normality provides a universal construction: estimate I(θ) by I(θ̂), apply the asymptotic normal approximation, and invert. The resulting CI has correct coverage as n → ∞ but may deviate from 1−α in finite samples. More refined approaches — likelihood ratio inversion, bootstrap CIs — improve finite-sample coverage but share the same foundational structure: define coverage probability, connect to a test or pivotal quantity, exploit large-sample approximations.
