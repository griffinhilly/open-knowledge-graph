---
id: maximum-likelihood-estimation-theory
title: Maximum Likelihood Estimation (Theory)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: optimization-problems
  type: soft
- id: central-limit-theorem-rigorous
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
status: validated
---

# Maximum Likelihood Estimation (Theory)

## Core Idea
The maximum likelihood estimator (MLE) θ̂ₙ maximizes the likelihood L(θ|X) = ∏ᵢ f(Xᵢ|θ). MLEs have desirable asymptotic properties: consistency, asymptotic normality, and efficiency (achieving the Cramer-Rao bound asymptotically). Under regularity conditions, θ̂ₙ solves ∂log L/∂θ = 0 and is unique.

## How It's Best Learned
Compute MLEs for standard families (normal, exponential, binomial). Verify regularity conditions. Apply the asymptotic normality result to construct confidence intervals.

## Common Misconceptions
- Thinking MLEs are always unbiased; MLEs can be biased for finite samples. - Assuming the MLE always has a closed form; many MLEs require numerical optimization. - Forgetting that asymptotic normality requires regularity conditions.

## Questions

```yaml
- question: "You observe 3 successes in 10 Bernoulli trials. What is the MLE for the success probability p, and why?"
  type: multiple-choice
  options:
    - "p̂ = 0.5, because we have no prior reason to prefer any other value"
    - "p̂ = 0.3, because it maximizes the likelihood of observing exactly 3 successes in 10 trials"
    - "p̂ = 0.5, because the MLE for Bernoulli trials always equals 0.5 by symmetry"
    - "p̂ = 0.3, because it is always the unbiased estimator of p"
  answer: 1
  explanation: "The MLE picks the parameter value that makes the observed data most probable. The likelihood is L(p) = p³(1−p)⁷. Setting d/dp[log L] = 3/p − 7/(1−p) = 0 gives p̂ = 3/10 = 0.3. This is the p for which observing exactly 3 successes in 10 trials is most likely. Option A is wrong (0.5 would be the MLE only if you observed 5 heads). Option D confuses MLE with unbiasedness — they often agree here, but the reason the MLE is 0.3 is that it maximizes the likelihood, not that it is unbiased."

- question: "A researcher computes the MLE for the variance σ² of a normal distribution with unknown mean and obtains σ̂² = (1/n)Σ(xᵢ − x̄)². Which statement is correct?"
  type: multiple-choice
  options:
    - "This estimator is unbiased, because MLEs are always unbiased"
    - "This estimator is biased — dividing by n rather than n−1 underestimates the true variance for finite samples"
    - "This estimator is efficient, so it must also be unbiased"
    - "The bias is irrelevant because MLE only guarantees asymptotic properties"
  answer: 1
  explanation: "The MLE for normal variance (1/n)Σ(xᵢ − x̄)² has expectation (n−1)σ²/n — it systematically underestimates the true variance for any finite n. This is a concrete counterexample to the misconception that MLEs are always unbiased. MLEs are asymptotically unbiased (bias vanishes as n → ∞) but can be biased in finite samples. The unbiased estimator S² = (1/(n−1))Σ(xᵢ − x̄)² corrects for this. Option C confuses efficiency (minimum asymptotic variance) with unbiasedness — these are separate properties."

- question: "The MLE usually produces a closed-form solution that can be computed analytically from a formula."
  type: true-false
  answer: false
  explanation: "Many MLEs require numerical optimization. Logistic regression, mixture models, and neural networks all require iterative algorithms (gradient descent, Newton-Raphson, EM algorithm) to maximize the log-likelihood. Closed-form solutions exist for standard families like the normal, exponential, and binomial, but this is the exception rather than the rule in applied statistics."

- question: "A large Fisher information value I(θ) implies the MLE will have high variance and be a poor estimator of θ."
  type: true-false
  answer: false
  explanation: "This is backwards. Large Fisher information means the data is highly informative about θ — the log-likelihood is sharply peaked around the true value, and the MLE concentrates tightly around the truth. The asymptotic variance of the MLE is I(θ)⁻¹, so large I(θ) means small variance and a precise estimator. Low Fisher information means the likelihood is flat and the data is uninformative, leading to a high-variance MLE."

- question: "What does it mean to say the MLE is 'the parameter value that makes the observed data most probable,' and why do we maximize the log-likelihood rather than the likelihood itself?"
  type: short-answer
  answer: "The likelihood function L(θ|X) gives the probability (or density) of the observed data X for each candidate value of θ. The MLE θ̂ is the value of θ that maximizes this function — making the observed outcome as probable as possible under the assumed model. We maximize the log-likelihood because the log converts the product ∏f(xᵢ|θ) into a sum Σlog f(xᵢ|θ), which is easier to differentiate and numerically more stable. Since log is monotonically increasing, the maximizer of log L is identical to the maximizer of L."
  explanation: "The log transformation is one of the most powerful computational tricks in statistics. It converts products to sums, which are much easier to differentiate and prevent floating-point underflow when n is large. The score equation ∂ℓ/∂θ = 0 is often analytically tractable when the corresponding likelihood derivative would be algebraically complex. The invariance of the maximizer under monotone transformations is the mathematical justification — and it's why asymptotic theory is developed in terms of the log-likelihood and its curvature (Fisher information)."
```

## Explainer

**Maximum likelihood estimation** formalizes a natural intuition: given observed data, choose the parameter value that makes the data most probable. Suppose you flip a coin 10 times and get 7 heads. You don't know the coin's bias p. The likelihood function L(p | data) = p⁷(1 − p)³ tells you how probable the observed outcome (7 heads in 10 flips) would be for each candidate value of p. L(0.5) ≈ 0.117, L(0.7) ≈ 0.267, L(0.9) ≈ 0.057. The value p = 0.7 makes the data most probable — and indeed, maximizing the likelihood analytically (by setting its derivative to zero) gives p̂ = 7/10 = 0.7. The MLE is the parameter value that best "explains" the data you actually observed.

In practice, you maximize the **log-likelihood** ℓ(θ) = log L(θ | X) = Σᵢ log f(Xᵢ | θ) rather than the likelihood itself. Logs convert products to sums, which are easier to differentiate, and since log is monotonically increasing, the maximizer doesn't change. Setting the **score equation** ∂ℓ/∂θ = 0 and solving gives the MLE. For the Gaussian N(μ, σ²) with known variance, differentiating Σᵢ(xᵢ − μ)²/σ² with respect to μ immediately yields μ̂ = x̄, the sample mean. For the exponential distribution with rate λ, the MLE is λ̂ = 1/x̄. These closed-form solutions are convenient, but many models (logistic regression, mixture models) require numerical optimization of the log-likelihood — your prerequisite optimization knowledge is directly applicable here.

The asymptotic theory is what makes MLEs so valuable beyond finite samples. Under regularity conditions (roughly: the model is identifiable, the true parameter lies in the interior of the parameter space, and derivatives exchange with integrals), the MLE θ̂ₙ based on n i.i.d. observations satisfies three properties. First, **consistency**: θ̂ₙ → θ₀ in probability as n → ∞. Second, **asymptotic normality**: √n(θ̂ₙ − θ₀) → N(0, I(θ₀)⁻¹) in distribution, where I(θ) = −E[∂²ℓ/∂θ²] is the **Fisher information**. Third, **efficiency**: no consistent estimator has a smaller asymptotic variance than I(θ₀)⁻¹, the Cramér-Rao lower bound.

The Fisher information deserves emphasis. It measures how much a single observation "tells you" about θ — how sharply peaked the log-likelihood is around the true value. Large Fisher information means the data is highly informative, the MLE concentrates tightly around the truth, and you need fewer observations to estimate precisely. The asymptotic normality result lets you construct approximate confidence intervals: θ̂ ± 1.96/√(n·I(θ̂)). This is the workhorse of likelihood-based inference — valid for any model satisfying regularity conditions, without requiring the data itself to be normally distributed. The price is that these guarantees are asymptotic: for small samples, the MLE can be biased and its variance may not match the Fisher information bound.
