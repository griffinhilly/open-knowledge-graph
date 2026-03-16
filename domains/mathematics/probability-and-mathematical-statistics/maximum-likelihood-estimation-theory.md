---
id: maximum-likelihood-estimation-theory
title: Maximum Likelihood Estimation (Theory)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: optimization-problems
  type: soft
builds-toward:
- consistency-of-estimators
- asymptotic-normality-mle
- likelihood-ratio-tests
tags:
- mle
- estimation
- statistics
stage: formal-systems
status: draft
---

# Maximum Likelihood Estimation (Theory)

## Core Idea
The maximum likelihood estimator (MLE) θ̂ₙ maximizes the likelihood L(θ|X) = ∏ᵢ f(Xᵢ|θ). MLEs have desirable asymptotic properties: consistency, asymptotic normality, and efficiency (achieving the Cramer-Rao bound asymptotically). Under regularity conditions, θ̂ₙ solves ∂log L/∂θ = 0 and is unique.

## How It's Best Learned
Compute MLEs for standard families (normal, exponential, binomial). Verify regularity conditions. Apply the asymptotic normality result to construct confidence intervals.

## Common Misconceptions
- Thinking MLEs are always unbiased; MLEs can be biased for finite samples. - Assuming the MLE always has a closed form; many MLEs require numerical optimization. - Forgetting that asymptotic normality requires regularity conditions.

## Explainer

**Maximum likelihood estimation** formalizes a natural intuition: given observed data, choose the parameter value that makes the data most probable. Suppose you flip a coin 10 times and get 7 heads. You don't know the coin's bias p. The likelihood function L(p | data) = p⁷(1 − p)³ tells you how probable the observed outcome (7 heads in 10 flips) would be for each candidate value of p. L(0.5) ≈ 0.117, L(0.7) ≈ 0.267, L(0.9) ≈ 0.057. The value p = 0.7 makes the data most probable — and indeed, maximizing the likelihood analytically (by setting its derivative to zero) gives p̂ = 7/10 = 0.7. The MLE is the parameter value that best "explains" the data you actually observed.

In practice, you maximize the **log-likelihood** ℓ(θ) = log L(θ | X) = Σᵢ log f(Xᵢ | θ) rather than the likelihood itself. Logs convert products to sums, which are easier to differentiate, and since log is monotonically increasing, the maximizer doesn't change. Setting the **score equation** ∂ℓ/∂θ = 0 and solving gives the MLE. For the Gaussian N(μ, σ²) with known variance, differentiating Σᵢ(xᵢ − μ)²/σ² with respect to μ immediately yields μ̂ = x̄, the sample mean. For the exponential distribution with rate λ, the MLE is λ̂ = 1/x̄. These closed-form solutions are convenient, but many models (logistic regression, mixture models) require numerical optimization of the log-likelihood — your prerequisite optimization knowledge is directly applicable here.

The asymptotic theory is what makes MLEs so valuable beyond finite samples. Under regularity conditions (roughly: the model is identifiable, the true parameter lies in the interior of the parameter space, and derivatives exchange with integrals), the MLE θ̂ₙ based on n i.i.d. observations satisfies three properties. First, **consistency**: θ̂ₙ → θ₀ in probability as n → ∞. Second, **asymptotic normality**: √n(θ̂ₙ − θ₀) → N(0, I(θ₀)⁻¹) in distribution, where I(θ) = −E[∂²ℓ/∂θ²] is the **Fisher information**. Third, **efficiency**: no consistent estimator has a smaller asymptotic variance than I(θ₀)⁻¹, the Cramér-Rao lower bound.

The Fisher information deserves emphasis. It measures how much a single observation "tells you" about θ — how sharply peaked the log-likelihood is around the true value. Large Fisher information means the data is highly informative, the MLE concentrates tightly around the truth, and you need fewer observations to estimate precisely. The asymptotic normality result lets you construct approximate confidence intervals: θ̂ ± 1.96/√(n·I(θ̂)). This is the workhorse of likelihood-based inference — valid for any model satisfying regularity conditions, without requiring the data itself to be normally distributed. The price is that these guarantees are asymptotic: for small samples, the MLE can be biased and its variance may not match the Fisher information bound.
