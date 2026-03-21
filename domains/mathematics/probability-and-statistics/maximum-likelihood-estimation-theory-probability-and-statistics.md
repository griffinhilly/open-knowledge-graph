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

## Questions

```yaml
- question: "A statistician writes L(θ) = ∏ p(xᵢ|θ) after observing data x₁, ..., xₙ. Which statement correctly describes what L(θ) is?"
  type: multiple-choice
  options:
    - "A probability distribution over possible parameter values — the probability that θ takes each value given the data"
    - "A measure of how probable the observed data would be for each candidate value of θ, with the data held fixed"
    - "The marginal probability of the data summed over all possible parameter values"
    - "A probability distribution over possible datasets for a fixed value of θ"
  answer: 1
  explanation: "The likelihood function is not a distribution over θ — it doesn't represent the probability that θ has a particular value, and it doesn't integrate to 1 over θ. It is the joint probability of the observed data, re-read as a function of the parameter with the data held constant. Two things that are numerically identical can mean very different things: p(x|θ) is a probability over data for fixed θ; L(θ) = p(x|θ) is a function of θ for fixed data. Confusing these is the most common conceptual error in learning MLE."

- question: "You flip a coin 10 times and observe 7 heads. What does MLE give as the estimate of the probability of heads?"
  type: multiple-choice
  options:
    - "0.5 — a fair coin is the most principled default assumption"
    - "0.7 — this is the parameter value that makes observing exactly 7 heads in 10 flips most probable"
    - "It cannot be determined without specifying a prior distribution over the probability of heads"
    - "0.7 if the coin is known to be biased; 0.5 if the coin is assumed fair"
  answer: 1
  explanation: "MLE finds the θ̂ that maximizes L(θ) = C(10,7) θ⁷(1−θ)³. Taking the log-likelihood and differentiating gives θ̂ = 7/10 = 0.7. MLE makes no use of prior beliefs about whether the coin 'should' be fair — it answers only: which θ makes the data you observed most probable? A prior distribution is a Bayesian concept, not part of MLE."

- question: "The likelihood function L(θ) is a probability distribution over the parameter θ and therefore integrates (or sums) to 1 over all possible values of θ."
  type: true-false
  answer: false
  explanation: "The likelihood function is not a probability distribution over θ. It doesn't integrate to 1 over θ and has no probabilistic interpretation as a distribution over parameter values. It is a function measuring the compatibility of the observed data with each value of θ. Treating it as a distribution over θ is the confusion that motivates Bayesian statistics — to get a proper distribution over θ you need a prior, which MLE does not use."

- question: "Maximizing the log-likelihood ℓ(θ) = Σ log p(xᵢ|θ) gives the same θ̂ as maximizing the likelihood L(θ) = ∏ p(xᵢ|θ)."
  type: true-false
  answer: true
  explanation: "The logarithm is strictly increasing, so it preserves the location of the maximum: the θ that maximizes L(θ) is the same θ that maximizes log L(θ). The log-likelihood is preferred in practice because it converts products into sums (easier to differentiate) and avoids numerical underflow from multiplying many small probabilities. The mathematical result is identical."

- question: "What is the central question MLE asks, and how does it differ from the question that a probability mass or density function answers?"
  type: short-answer
  answer: "A PMF/PDF answers: given this parameter value θ, how probable is this outcome? MLE inverts the question: given the observed data, which parameter value θ makes that data most probable? The PMF treats θ as fixed and data as variable; the likelihood function treats the observed data as fixed and θ as the variable to optimize over. MLE finds the θ that would have made the data you actually saw the least surprising."
  explanation: "This inversion is conceptually subtle. p(x|θ) and L(θ) = p(x|θ) are numerically the same expression but ask different questions. Failing to see the difference leads to treating the likelihood as a probability over θ. MLE is a frequentist procedure: it finds the best-fit parameter but makes no probability claims about where the true θ lies — that is the province of Bayesian inference."
```

## Explainer

You already know that a probability mass function p(x|θ) gives the probability of observing outcome x when the true parameter is θ. Maximum likelihood estimation flips this question: given data that you have already observed, which value of θ makes that data most probable? The **likelihood function** L(θ) is exactly p(x|θ) re-read as a function of θ with the data held fixed. It is not a probability over θ — it is a measure of how "compatible" each candidate parameter value is with your observations.

For independent observations x₁, x₂, …, xₙ, the joint probability of the entire dataset is the product of individual probabilities: L(θ) = ∏ p(xᵢ|θ). The **maximum likelihood estimate** θ̂ is the value that makes this product as large as possible. Intuitively, you are asking: if I had to pick one θ and then "generate" the observed data from that distribution, which θ would make the data I actually saw the least surprising? The answer is θ̂.

In practice, products of many small numbers are numerically unstable and analytically awkward. Taking the logarithm converts the product into a sum: ℓ(θ) = Σ log p(xᵢ|θ). Because log is strictly increasing, maximizing ℓ(θ) gives the same θ̂ as maximizing L(θ). This **log-likelihood** is almost always what you differentiate in practice. Setting dℓ/dθ = 0 and solving yields the MLE, though for multiparameter models you set all partial derivatives to zero simultaneously.

A worked example cements the idea. Suppose you flip a coin n times and observe k heads. The PMF is p(k|θ) = C(n,k) θᵏ(1−θ)ⁿ⁻ᵏ. The log-likelihood is ℓ(θ) = k log θ + (n−k) log(1−θ) plus a constant. Differentiating and solving gives θ̂ = k/n — the sample proportion. This is unsurprising, but it is exactly what MLE says: the proportion you observed is the value of θ that would have made what you saw most probable.

Three asymptotic properties make MLE powerful beyond any single example. MLEs are **consistent** — as n → ∞, θ̂ converges to the true θ. They are **asymptotically normal** — the sampling distribution of θ̂ approaches a normal distribution, making inference tractable. And they are **efficient** — among all consistent estimators, MLEs achieve the smallest possible variance in the limit (the Cramér–Rao bound). These guarantees hold under "regularity conditions" — smoothness and identifiability constraints on the model — and they are the reason MLE is the workhorse of parametric estimation across statistics, machine learning, and econometrics.
