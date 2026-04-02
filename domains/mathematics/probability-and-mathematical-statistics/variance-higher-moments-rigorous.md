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
stage: expert
status: validated
---

# Variance and Higher Moments (Rigorous)

## Core Idea
The k-th moment of X is μₖ = E[Xᵏ], which exists if E[|X|ᵏ] < ∞. Variance Var(X) = E[(X - E[X])²] measures spread; higher central moments μₖ = E[(X - E[X])ᵏ] capture skewness (k=3) and kurtosis (k=4). Hölder's inequality and Jensen's inequality are key tools relating moments.

## Questions

```yaml
- question: "X follows a Cauchy distribution. A student claims 'the variance of X is infinite.' What is the more precise statement?"
  type: multiple-choice
  options:
    - "Var(X) = ∞, but E[X] = 0 exists as a finite number"
    - "The variance is undefined because E[X] itself does not exist — the Cauchy distribution has no finite moments of any order"
    - "Var(X) is undefined only because the fourth moment diverges, not the second"
    - "Var(X) = ∞ exists as an extended real number; higher moments are finite"
  answer: 1
  explanation: "The Cauchy distribution has no finite moments of any order — not even the first. E[|X|^k] = ∞ for all k ≥ 1. Saying 'variance is infinite' is imprecise because variance is defined as E[(X−E[X])²], which requires E[X] to exist first. Since E[X] doesn't exist for the Cauchy distribution, Var(X) is not just 'infinite' but genuinely undefined. This illustrates why the condition E[|X|^k] < ∞ is not a technicality — it's a genuine existence requirement."

- question: "Jensen's inequality states that for a convex function φ, φ(E[X]) ≤ E[φ(X)]. Which of the following is a direct application of this to prove Var(X) ≥ 0?"
  type: multiple-choice
  options:
    - "Apply φ(t) = |t| (convex): |E[X]| ≤ E[|X|], which implies variance is non-negative"
    - "Apply φ(t) = t² (convex): (E[X])² ≤ E[X²], so E[X²] − (E[X])² ≥ 0, which is Var(X)"
    - "Apply φ(t) = e^t (convex): E[e^X] ≥ e^{E[X]}, which bounds the variance from below"
    - "Apply φ(t) = −t (linear): E[−X] = −E[X], proving symmetry, hence variance ≥ 0"
  answer: 1
  explanation: "Taking φ(t) = t², which is convex, Jensen gives (E[X])² ≤ E[X²]. Since Var(X) = E[X²] − (E[X])², this immediately gives Var(X) ≥ 0, with equality iff X is almost surely constant. This is a clean measure-theoretic proof that requires no algebra beyond the inequality itself. The other options don't directly yield the result."

- question: "If E[|X|⁴] < ∞, then E[|X|²] < ∞ as well."
  type: true-false
  answer: true
  explanation: "On probability spaces, Lᵏ spaces are nested: Lᵏ ⊆ Lʲ for k > j. This follows from Hölder's inequality applied with an indicator function: if E[|X|⁴] < ∞, then X ∈ L⁴, and since the probability measure is finite (total measure 1), L⁴ ⊆ L². Informally: a higher moment being finite forces all lower moments to also be finite. This is a genuinely useful fact — if you can bound a high moment, you get the lower moments for free."

- question: "Two distinct probability distributions that have identical moments of most orders is expected to be the same distribution."
  type: true-false
  answer: false
  explanation: "This is false — the moment problem is not always determinate. There exist pairs of distinct distributions with identical moments of all orders; the log-normal distribution and certain modifications provide classic counterexamples. A distribution is uniquely determined by its moments only when Carleman's condition is satisfied: ∑ₖ μ₂ₖ^(−1/(2k)) = ∞. Distributions with heavy tails (like the log-normal) may violate this, making the moment sequence insufficient to characterize them uniquely."

- question: "Why does positive skewness (γ₁ > 0) indicate a heavy right tail, given that skewness is the third standardized central moment E[(X − μ)³]/σ³?"
  type: short-answer
  answer: "The cube function preserves sign: (x − μ)³ is large and positive when x is far above the mean, and large and negative when x is far below. If the distribution has a heavy right tail, large positive deviations occur more frequently or more extremely than large negative deviations, making E[(X − μ)³] > 0. The standardization by σ³ makes the measure dimensionless. Negative skewness (left-tail heavy) similarly makes E[(X − μ)³] < 0 because extreme negative deviations dominate."
  explanation: "The key is that cubing (unlike squaring) preserves the sign of the deviation, so E[(X−μ)³] reflects the net asymmetry in the distribution's tails. A symmetric distribution like the normal has E[(X−μ)³] = 0 because positive and negative deviations cancel. Skewness ≠ 0 tells you which tail is heavier, and its magnitude tells you how strongly asymmetric the distribution is — information that the mean and variance alone cannot convey."
```

## Explainer

From measure-theoretic expectation, you know that E[X] = ∫ X dP is a Lebesgue integral with respect to the probability measure P. The k-th **moment** E[Xᵏ] is simply the integral of the function Xᵏ — that is, ∫ Xᵏ dP. The central question is always existence: when is this integral finite? The answer is the condition E[|X|ᵏ] < ∞, which is exactly the statement that Xᵏ is integrable, or equivalently that X ∈ Lᵏ(Ω, ℱ, P). The Lᵏ spaces you may know from functional analysis appear here as the natural home for random variables with finite k-th moments. Existence of higher moments is genuinely restrictive: X ~ Cauchy has no finite first moment; X ~ t_ν has finite moments only up to order ν − 1.

**Variance** Var(X) = E[(X − μ)²] = E[X²] − (E[X])² is the second central moment, measuring the average squared deviation from the mean. The measure-theoretic proof that E[X²] − (E[X])² ≥ 0 is a direct application of **Jensen's inequality**: for any convex function φ, φ(E[X]) ≤ E[φ(X)]. Taking φ(t) = t², Jensen gives (E[X])² ≤ E[X²], so Var(X) = E[X²] − (E[X])² ≥ 0, with equality iff X is almost surely constant. Jensen's inequality is pervasive: it gives the AM-GM inequality, concavity of entropy, and the fact that the geometric mean never exceeds the arithmetic mean, all from the same principle.

**Hölder's inequality** |E[XY]| ≤ E[|X|^p]^(1/p) · E[|Y|^q]^(1/q) (for conjugate exponents 1/p + 1/q = 1) is the other fundamental tool. The special case p = q = 2 is the **Cauchy-Schwarz inequality**: |E[XY]| ≤ √(E[X²]) √(E[Y²]), or equivalently |Cov(X,Y)| ≤ σ_X σ_Y. Hölder also establishes that existence of higher moments implies existence of lower ones: if E[|X|ᵏ] < ∞, then E[|X|ʲ] < ∞ for all j < k. This follows by applying Hölder with an indicator function. The Lᵏ spaces are nested: L² ⊆ L¹ for probability measures (a fact that is false for general σ-finite measures).

The **third central moment** μ₃ = E[(X − μ)³] measures **skewness** — asymmetry in the distribution. Positive skewness means the right tail is heavier (the distribution is pulled toward large positive deviations); negative skewness means the left tail. The standardized skewness γ₁ = μ₃/σ³ is the dimensionless version. The **fourth central moment** μ₄ = E[(X − μ)⁴] underlies **kurtosis** γ₂ = μ₄/σ⁴ − 3 (subtracting 3 so that the normal distribution has kurtosis 0). High kurtosis (leptokurtic) indicates heavy tails and a sharp peak; low kurtosis (platykurtic) indicates light tails. These higher moments appear throughout statistics: the moment conditions in the central limit theorem, the method of moments estimator, and the characterization of the normal distribution as the distribution determined by its first two cumulants all depend on this framework.

The rigorous treatment matters because moments can fail to characterize a distribution. There exist distinct distributions with identical moments of all orders — the log-normal and certain modifications have this property. The moment problem (when does a moment sequence uniquely determine a distribution?) is resolved by Carleman's condition: if ∑ₖ μ₂ₖ^(−1/2k) = ∞, the distribution is uniquely determined by its moments. This subtlety — invisible in informal treatments — is exactly the kind of issue that measure-theoretic probability is designed to surface and resolve.
