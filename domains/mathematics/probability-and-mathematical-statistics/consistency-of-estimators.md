---
id: consistency-of-estimators
title: Consistency of Estimators
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: convergence-in-probability
  type: hard
- id: maximum-likelihood-estimation-theory
  type: soft
builds-toward:
- asymptotic-normality-mle
tags:
- consistency
- asymptotics
- estimation
stage: advanced
status: draft
---

# Consistency of Estimators

## Core Idea
An estimator θ̂ₙ is consistent if θ̂ₙ converges in probability to θ as n → ∞. Consistency is a minimum requirement for reasonable estimators—as sample size grows, the estimator should approach the truth. Under regularity conditions, MLEs and method of moments estimators are consistent.

## Questions

```yaml
- question: "An estimator θ̂ₙ is known to be consistent for θ. A researcher applies it to a dataset with n=12 observations and obtains an estimate substantially far from the true θ. What should she conclude?"
  type: multiple-choice
  options:
    - "The estimator is not actually consistent — a consistent estimator must produce close estimates even for small samples"
    - "The model assumptions must be violated, since consistency would otherwise guarantee a good estimate"
    - "Nothing contradictory — consistency only guarantees convergence in probability as n → ∞, and poor performance on a specific small sample is fully compatible with consistency"
    - "The estimator has high bias, which by definition precludes consistency"
  answer: 2
  explanation: "Consistency is a purely asymptotic property: P(|θ̂ₙ − θ| > ε) → 0 as n → ∞. It makes no promise about any finite sample. For small n, a consistent estimator can be badly off — the probability of error is positive, just not converging to 1. This is one reason consistency alone is insufficient for a complete evaluation of an estimator; finite-sample properties like bias and mean squared error are separately important. A consistent estimator guarantees you'll do well *eventually*, not *now*."

- question: "An estimator θ̂ₙ has bias equal to 1/n and variance equal to 1/n. Which statement is correct?"
  type: multiple-choice
  options:
    - "The estimator is inconsistent — any nonzero bias disqualifies an estimator from being consistent"
    - "The estimator is consistent only if it is also unbiased, which it is not at finite n"
    - "The estimator is consistent — both bias and variance vanish as n → ∞, so by Chebyshev it converges in probability to θ"
    - "Consistency cannot be determined from bias and variance alone"
  answer: 2
  explanation: "Consistency does not require unbiasedness at finite sample sizes. What matters is whether the estimator converges to the truth as n → ∞. Since bias = 1/n → 0 and variance = 1/n → 0, the MSE = bias² + variance = 1/n² + 1/n → 0. By Chebyshev's inequality (P(|θ̂ₙ − θ| > ε) ≤ MSE/ε²), this gives consistency. An estimator that is biased at every finite n but whose bias shrinks to zero is a common and valid class of consistent estimators."

- question: "A consistent estimator must be unbiased for all finite sample sizes."
  type: true-false
  answer: false
  explanation: "This is a common conflation. Unbiasedness (E[θ̂ₙ] = θ for all n) and consistency (convergence in probability as n → ∞) are different properties. A biased estimator can be consistent as long as the bias vanishes as n grows. Conversely, an unbiased estimator need not be consistent — if its variance doesn't go to zero, it will not converge in probability. The two properties are logically independent, though an unbiased estimator with vanishing variance is a sufficient condition for consistency."

- question: "If an estimator is unbiased (E[θ̂ₙ] = θ for all n) and its variance converges to zero as n → ∞, then by Chebyshev's inequality it is consistent."
  type: true-false
  answer: true
  explanation: "Chebyshev's inequality states P(|θ̂ₙ − θ| > ε) ≤ Var(θ̂ₙ)/ε². If the estimator is unbiased, then |θ̂ₙ − θ| has the same distribution as the centered version, and MSE = Var(θ̂ₙ). As Var(θ̂ₙ) → 0, the right-hand side goes to 0 for any fixed ε > 0, which is exactly the definition of convergence in probability. This gives a clean sufficient condition for consistency: zero bias plus vanishing variance suffices."

- question: "What does consistency guarantee about an estimator, and what equally important properties does it NOT guarantee?"
  type: short-answer
  answer: "Consistency guarantees that as sample size grows without bound, the probability of the estimator being far from the true parameter goes to zero — the estimator converges in probability to the truth. It does NOT guarantee good performance at any finite sample size, does not specify how quickly the estimator converges (the rate), does not require unbiasedness, and gives no information about the distribution of the estimator for constructing confidence intervals. Those properties — finite-sample behavior, convergence rate, and sampling distribution — are addressed by asymptotic normality and mean squared error analysis."
  explanation: "The conceptual point is that consistency is a floor, not a ceiling. It rules out estimators that stay wrong no matter how much data you have, but it doesn't distinguish among the many consistent estimators that differ dramatically in their efficiency (speed of convergence) and finite-sample properties. Asymptotic normality, which states √n(θ̂ₙ − θ) → N(0, σ²), is the next step: it quantifies how fast a consistent estimator converges and enables the construction of confidence intervals."
```

## Explainer

An estimator is a rule for turning data into a guess about an unknown parameter. For that rule to be useful, it should at minimum do better with more data — intuitively, collecting millions of observations should get you very close to the truth. **Consistency** formalizes this requirement using the language of convergence in probability that you already know.

Recall that θ̂ₙ converges in probability to θ means: for any ε > 0, the probability P(|θ̂ₙ − θ| > ε) → 0 as n → ∞. In words, the chance that your estimate is far from the truth becomes negligible as the sample grows. This is weaker than almost-sure convergence (which says the estimate *will* eventually be close with probability 1 along every path), but it is the standard benchmark for estimators. A consistent estimator might produce a bad estimate for any specific sample — you could get unlucky — but the probability of a bad estimate vanishes as n grows.

The most important consistency results are for the **sample mean** and for **MLEs**. The sample mean X̄ₙ is consistent for the population mean μ by the Weak Law of Large Numbers, which is itself a direct consequence of convergence in probability. For MLEs, consistency follows from general regularity conditions (differentiability of the log-likelihood, identifiability of the model, compactness arguments) and is one reason MLEs are the default estimator in most settings. A useful sufficient condition: if an estimator is unbiased (E[θ̂ₙ] = θ) and its variance vanishes (Var(θ̂ₙ) → 0), then by Chebyshev's inequality it is consistent. But note that consistency does not require unbiasedness — a biased estimator can still be consistent if the bias shrinks to zero with n.

What consistency does *not* guarantee is equally important. Consistency is an asymptotic property — it says nothing about performance at any finite sample size. An estimator could be badly biased for small n yet perfectly consistent. And consistency gives no rate: it does not tell you how quickly the estimate approaches the truth. That information lives in **asymptotic normality** (the next topic), which tells you √n(θ̂ₙ − θ) converges in distribution to a normal, quantifying the speed of convergence and enabling confidence intervals. Think of consistency as the entry requirement for an estimator — necessary but far from sufficient for a complete understanding of its behavior.
