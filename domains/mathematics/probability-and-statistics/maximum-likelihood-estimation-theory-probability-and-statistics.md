---
id: maximum-likelihood-estimation-theory-probability-and-statistics
title: Maximum Likelihood Estimation
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: probability-mass-functions-theory
  type: hard
builds-toward:
- bayesian-inference-intro
tags:
- mle
- estimation
stage: formal-systems
status: draft
---

# Maximum Likelihood Estimation

## Core Idea
MLE θ̂ maximizes likelihood L(θ)=∏p(x_i|θ) or L(θ)=∏f(x_i|θ). Under regularity, MLEs are consistent, asymptotically normal, and efficient. Often found via log-likelihood ℓ(θ)=Σlog p(x_i|θ) by solving dℓ/dθ=0.

## Explainer

You already know that a probability mass function p(x|θ) gives the probability of observing outcome x when the true parameter is θ. Maximum likelihood estimation flips this question: given data that you have already observed, which value of θ makes that data most probable? The **likelihood function** L(θ) is exactly p(x|θ) re-read as a function of θ with the data held fixed. It is not a probability over θ — it is a measure of how "compatible" each candidate parameter value is with your observations.

For independent observations x₁, x₂, …, xₙ, the joint probability of the entire dataset is the product of individual probabilities: L(θ) = ∏ p(xᵢ|θ). The **maximum likelihood estimate** θ̂ is the value that makes this product as large as possible. Intuitively, you are asking: if I had to pick one θ and then "generate" the observed data from that distribution, which θ would make the data I actually saw the least surprising? The answer is θ̂.

In practice, products of many small numbers are numerically unstable and analytically awkward. Taking the logarithm converts the product into a sum: ℓ(θ) = Σ log p(xᵢ|θ). Because log is strictly increasing, maximizing ℓ(θ) gives the same θ̂ as maximizing L(θ). This **log-likelihood** is almost always what you differentiate in practice. Setting dℓ/dθ = 0 and solving yields the MLE, though for multiparameter models you set all partial derivatives to zero simultaneously.

A worked example cements the idea. Suppose you flip a coin n times and observe k heads. The PMF is p(k|θ) = C(n,k) θᵏ(1−θ)ⁿ⁻ᵏ. The log-likelihood is ℓ(θ) = k log θ + (n−k) log(1−θ) plus a constant. Differentiating and solving gives θ̂ = k/n — the sample proportion. This is unsurprising, but it is exactly what MLE says: the proportion you observed is the value of θ that would have made what you saw most probable.

Three asymptotic properties make MLE powerful beyond any single example. MLEs are **consistent** — as n → ∞, θ̂ converges to the true θ. They are **asymptotically normal** — the sampling distribution of θ̂ approaches a normal distribution, making inference tractable. And they are **efficient** — among all consistent estimators, MLEs achieve the smallest possible variance in the limit (the Cramér–Rao bound). These guarantees hold under "regularity conditions" — smoothness and identifiability constraints on the model — and they are the reason MLE is the workhorse of parametric estimation across statistics, machine learning, and econometrics.
