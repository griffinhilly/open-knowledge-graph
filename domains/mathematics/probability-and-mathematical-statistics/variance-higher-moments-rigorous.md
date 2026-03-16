---
id: variance-higher-moments-rigorous
title: Variance and Higher Moments (Rigorous)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: expectation-measure-theoretic
  type: hard
- id: variance-of-random-variables
  type: soft
builds-toward:
- moment-generating-functions
- characteristic-functions
- convergence-in-lp
tags:
- moments
- variance
- measure-theory
stage: advanced
status: draft
---

# Variance and Higher Moments (Rigorous)

## Core Idea
The k-th moment of X is μₖ = E[Xᵏ], which exists if E[|X|ᵏ] < ∞. Variance Var(X) = E[(X - E[X])²] measures spread; higher central moments μₖ = E[(X - E[X])ᵏ] capture skewness (k=3) and kurtosis (k=4). Hölder's inequality and Jensen's inequality are key tools relating moments.

## Explainer

From measure-theoretic expectation, you know that E[X] = ∫ X dP is a Lebesgue integral with respect to the probability measure P. The k-th **moment** E[Xᵏ] is simply the integral of the function Xᵏ — that is, ∫ Xᵏ dP. The central question is always existence: when is this integral finite? The answer is the condition E[|X|ᵏ] < ∞, which is exactly the statement that Xᵏ is integrable, or equivalently that X ∈ Lᵏ(Ω, ℱ, P). The Lᵏ spaces you may know from functional analysis appear here as the natural home for random variables with finite k-th moments. Existence of higher moments is genuinely restrictive: X ~ Cauchy has no finite first moment; X ~ t_ν has finite moments only up to order ν − 1.

**Variance** Var(X) = E[(X − μ)²] = E[X²] − (E[X])² is the second central moment, measuring the average squared deviation from the mean. The measure-theoretic proof that E[X²] − (E[X])² ≥ 0 is a direct application of **Jensen's inequality**: for any convex function φ, φ(E[X]) ≤ E[φ(X)]. Taking φ(t) = t², Jensen gives (E[X])² ≤ E[X²], so Var(X) = E[X²] − (E[X])² ≥ 0, with equality iff X is almost surely constant. Jensen's inequality is pervasive: it gives the AM-GM inequality, concavity of entropy, and the fact that the geometric mean never exceeds the arithmetic mean, all from the same principle.

**Hölder's inequality** |E[XY]| ≤ E[|X|^p]^(1/p) · E[|Y|^q]^(1/q) (for conjugate exponents 1/p + 1/q = 1) is the other fundamental tool. The special case p = q = 2 is the **Cauchy-Schwarz inequality**: |E[XY]| ≤ √(E[X²]) √(E[Y²]), or equivalently |Cov(X,Y)| ≤ σ_X σ_Y. Hölder also establishes that existence of higher moments implies existence of lower ones: if E[|X|ᵏ] < ∞, then E[|X|ʲ] < ∞ for all j < k. This follows by applying Hölder with an indicator function. The Lᵏ spaces are nested: L² ⊆ L¹ for probability measures (a fact that is false for general σ-finite measures).

The **third central moment** μ₃ = E[(X − μ)³] measures **skewness** — asymmetry in the distribution. Positive skewness means the right tail is heavier (the distribution is pulled toward large positive deviations); negative skewness means the left tail. The standardized skewness γ₁ = μ₃/σ³ is the dimensionless version. The **fourth central moment** μ₄ = E[(X − μ)⁴] underlies **kurtosis** γ₂ = μ₄/σ⁴ − 3 (subtracting 3 so that the normal distribution has kurtosis 0). High kurtosis (leptokurtic) indicates heavy tails and a sharp peak; low kurtosis (platykurtic) indicates light tails. These higher moments appear throughout statistics: the moment conditions in the central limit theorem, the method of moments estimator, and the characterization of the normal distribution as the distribution determined by its first two cumulants all depend on this framework.

The rigorous treatment matters because moments can fail to characterize a distribution. There exist distinct distributions with identical moments of all orders — the log-normal and certain modifications have this property. The moment problem (when does a moment sequence uniquely determine a distribution?) is resolved by Carleman's condition: if ∑ₖ μ₂ₖ^(−1/2k) = ∞, the distribution is uniquely determined by its moments. This subtlety — invisible in informal treatments — is exactly the kind of issue that measure-theoretic probability is designed to surface and resolve.
