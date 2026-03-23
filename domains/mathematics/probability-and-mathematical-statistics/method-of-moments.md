---
id: method-of-moments
title: Method of Moments
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: variance-higher-moments-rigorous
  type: hard
- id: weak-law-of-large-numbers
  type: soft
builds-toward:
- consistency-of-estimators
tags:
- method-of-moments
- estimation
- statistics
stage: advanced
status: validated
---

# Method of Moments

## Core Idea
The method of moments equates sample moments with population moments: set m̂ₖ = μₖ(θ) where m̂ₖ = (1/n)Σ Xᵢᵏ. Solve for θ. This approach is simple but less efficient than MLE. Method of moments estimators are consistent by the WLLN and asymptotically normal under suitable conditions.

## Questions

```yaml
- question: "You are estimating parameters of a Gamma(α, β) distribution, which has two unknown parameters. How should you set up a method of moments estimation?"
  type: multiple-choice
  options:
    - "Use one equation matching the sample mean to E[X], since the mean alone determines the distribution shape"
    - "Use two equations matching the first and second sample moments to E[X] and E[X²], then solve the 2×2 system for α and β"
    - "Use three or more equations for robustness, choosing the ones with the smallest variance"
    - "Use one equation matching the sample median, which is more robust to outliers than the mean"
  answer: 1
  explanation: "When you have p unknown parameters, you need p moment equations. For Gamma(α, β) with two unknowns, you set m̂₁ = μ'₁(α,β) and m̂₂ = μ'₂(α,β) and solve the system. Using fewer equations leaves the system underdetermined; using more creates overdetermination (the basis of GMM). The median is not a moment and is not used in the standard method of moments framework."

- question: "For an Exponential(λ) distribution, the method of moments gives λ̂ = 1/X̄, which happens to equal the MLE. A student concludes that MOM always equals MLE. What is the fundamental error in this reasoning?"
  type: multiple-choice
  options:
    - "MOM and MLE are mathematically identical for all exponential family distributions, so the conclusion is actually correct"
    - "The agreement is a coincidence specific to the exponential distribution; MOM and MLE generally differ, and MLE uses the full likelihood shape rather than only moment summaries"
    - "MOM is always more efficient than MLE because it uses fewer computational assumptions"
    - "MOM and MLE agree whenever the distribution has a single sufficient statistic"
  answer: 1
  explanation: "The exponential is a special case where MOM and MLE coincide. For distributions like the Beta, Gamma, or Weibull, MOM and MLE give different estimates, and MLE is typically more efficient because it uses the entire likelihood surface — the full shape of the distribution — rather than just the values of one or two moments. Using only moment summaries discards information, which is precisely why MOM has lower statistical efficiency."

- question: "Method of moments estimators are consistent because sample moments converge in probability to their population counterparts as sample size grows."
  type: true-false
  answer: true
  explanation: "True. This is a direct application of the weak law of large numbers: the k-th sample moment m̂_k = (1/n)Σ Xᵢᵏ converges in probability to E[X^k] = μ'_k(θ). If the mapping from population moments to parameters is continuous (invertible), then by the continuous mapping theorem, the MOM estimator θ̂ converges in probability to θ. Consistency is thus essentially built into the method."

- question: "Since method of moments uses multiple moment equations to capture more features of the distribution, it is generally more statistically efficient than maximum likelihood estimation."
  type: true-false
  answer: false
  explanation: "False. MLE is generally more efficient because it uses the full likelihood — the entire shape of the density or probability function — which encodes more information than any finite set of moments. The Cramér-Rao lower bound quantifies this: MLE achieves the bound under regularity conditions, while MOM typically does not. Using more moments does not recover the full distributional information; MLE extracts all available information simultaneously through the score function."

- question: "Why are method of moments estimators consistent, and why are they typically less statistically efficient than maximum likelihood estimators?"
  type: short-answer
  answer: "MOM estimators are consistent because they are continuous functions of sample moments, and the WLLN guarantees that sample moments converge in probability to their population counterparts. By the continuous mapping theorem, the MOM estimator converges to the true parameter. They are less efficient than MLE because MOM uses only a finite set of moment summaries (e.g., mean and variance), while MLE uses the full likelihood, which encodes the complete shape of the distribution. Any information in the distributional shape not captured by the chosen moments is lost, increasing estimator variance."
  explanation: "The key contrast is: MOM uses summary statistics (moments) to match features of the distribution; MLE maximizes the probability of the observed data under the model, squeezing out all available information. For distributions where moments determine the distribution well (like the normal), the gap is small. For complex distributions, the gap in efficiency can be substantial."
```

## Explainer

Your prerequisite on **variance and higher moments** gave you the concept of population moments: μ'_k = E[X^k], the k-th moment of a distribution — functions of the unknown parameter(s) θ. Your introduction to the **weak law of large numbers** told you that sample averages converge to their expectations. Method of moments puts these two facts together into a simple and general estimation strategy.

The idea is direct: the **k-th sample moment** m̂_k = (1/n)Σᵢ Xᵢᵏ is a natural estimate of the population moment μ'_k(θ) = E[X^k], because the WLLN guarantees m̂_k → μ'_k(θ) in probability. If your model has p unknown parameters, you set up a system of p equations — m̂_1 = μ'_1(θ), m̂_2 = μ'_2(θ), …, m̂_p = μ'_p(θ) — and solve for θ. As a concrete example: for a Normal(μ, σ²) distribution, the first two population moments are μ'_1 = μ and μ'_2 = μ² + σ². Setting m̂_1 = μ̂ and m̂_2 = μ̂² + σ̂² and solving gives μ̂ = X̄ and σ̂² = (1/n)Σ(Xᵢ − X̄)² — the sample mean and sample variance (with divisor n, not n−1).

Method of moments estimators are consistent because they are continuous functions of sample moments that converge in probability to the correct population moments. They are also typically asymptotically normal by the delta method applied to the CLT for sample moments. However, they are often **less efficient than MLEs** because they use only moment summaries and can ignore information embedded in the full shape of the likelihood. For example, for an Exponential(λ) distribution, the MOM estimator from the first moment gives λ̂ = 1/X̄, which coincidentally equals the MLE. But for distributions with complex shapes, like the Beta distribution, MOM and MLE can differ noticeably, with MLE being more efficient.

The real virtue of method of moments is **tractability**. When the log-likelihood is hard to differentiate or maximize analytically, method of moments provides a closed-form starting point — often used to initialize numerical MLE optimization. It is also the conceptual ancestor of **generalized method of moments (GMM)**, a cornerstone of modern econometrics, where you match more moment conditions than you have parameters and use the over-identification as a diagnostic for model misspecification. Before encountering MLE or Bayesian estimation, method of moments teaches the essential principle: use observed data to match theoretically predicted features of the distribution.
