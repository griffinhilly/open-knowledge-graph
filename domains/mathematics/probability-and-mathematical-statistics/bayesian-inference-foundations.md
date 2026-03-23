---
id: bayesian-inference-foundations
title: Bayesian Inference Foundations
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: bayes-theorem
  type: hard
- id: conditional-expectation
  type: hard
builds-toward:
- conjugate-priors
- bayesian-point-estimation
tags:
- bayesian-inference
- probability
- statistics
stage: advanced
status: validated
---

# Bayesian Inference Foundations

## Core Idea
Bayesian inference treats θ as a random variable with prior distribution π(θ). Given data X, the posterior is π(θ|X) ∝ L(θ|X)π(θ) by Bayes' theorem. The posterior combines prior beliefs with data. Inference is based on the posterior: point estimates, credible intervals, and predictions all follow from the posterior distribution.

## Questions

```yaml
- question: "A researcher flips a coin 10 times and observes 7 heads. Using a uniform prior on θ ∈ [0,1], what is the Bayesian posterior mean for θ?"
  type: multiple-choice
  options:
    - "0.70 — the maximum likelihood estimate"
    - "0.667 — the mean of the resulting Beta(8, 4) posterior"
    - "0.50 — the prior mean"
    - "0.75 — the upper bound of a 95% credible interval"
  answer: 1
  explanation: "With a uniform prior, the posterior is Beta(8, 4) (7 heads + 1, 3 tails + 1), whose mean is 8/12 ≈ 0.667. The MLE of 0.70 maximizes the likelihood but ignores the prior; the posterior mean incorporates it, pulling the estimate slightly toward 0.5. The prior always 'smooths' the estimate relative to the MLE."

- question: "Which statement correctly describes a 95% Bayesian credible interval [a, b]?"
  type: multiple-choice
  options:
    - "If the experiment were repeated many times, 95% of such intervals would contain the true θ"
    - "Given the observed data, P(a ≤ θ ≤ b | X) = 0.95"
    - "The interval covers 95% of the prior distribution regardless of the data"
    - "The interval is centered on the maximum likelihood estimate"
  answer: 1
  explanation: "A Bayesian credible interval is a direct probability statement about θ given the observed data — computed by integrating the posterior. Option A describes the frequentist confidence interval, which makes no direct probability claim about θ; it characterizes the long-run behavior of the estimation procedure, not the probability that any particular interval contains θ."

- question: "In Bayesian inference, the optimal point estimate under squared-error loss is the posterior mean E[θ|X]."
  type: true-false
  answer: true
  explanation: "Under squared-error loss, minimizing expected loss requires choosing the estimator equal to the conditional expectation of θ given the data — exactly the posterior mean. This is a direct application of the role of conditional expectation in Bayesian decision theory and is why the posterior mean is the canonical Bayesian point estimate."

- question: "In Bayesian inference, the posterior distribution is computed before observing data; the likelihood then updates it afterward."
  type: true-false
  answer: false
  explanation: "This reverses the logic. The prior π(θ) is specified before seeing any data — it encodes prior beliefs. The posterior π(θ|X) is computed AFTER observing X, by multiplying the prior by the likelihood L(θ|X) and normalizing. The likelihood is the bridge from data to posterior, not the other way around."

- question: "Why does the Bayesian posterior mean typically differ from the frequentist maximum likelihood estimate, and what determines how large that difference is?"
  type: short-answer
  answer: "The posterior mean incorporates the prior distribution, which pulls the estimate toward the prior's center of mass. The MLE maximizes the likelihood alone. The degree of difference depends on the relative informativeness of the prior versus the data: with few observations and an informative prior, the posterior mean is pulled substantially toward the prior; with abundant data, the likelihood dominates and the posterior mean converges toward the MLE."
  explanation: "The MLE treats θ as a fixed unknown and maximizes L(θ|X). The posterior mean treats θ as a random variable and computes E[θ|X] by integrating over the full posterior, which weights every value of θ by both how well it explains the data and how plausible it was a priori. Even a uniform prior shifts the posterior mean from the MLE in finite samples — for example, Beta(8,4) has mean 8/12 ≈ 0.667 while the MLE is 7/10 = 0.70."
```

## Explainer

You already know Bayes' theorem as a formula for flipping conditional probabilities: P(A|B) = P(B|A)P(A)/P(B). Bayesian inference scales this up to statistical parameters. Instead of reasoning about events A and B, you reason about an unknown parameter θ (say, the true probability of heads on a coin, or the mean weight of a population). The key move is to treat θ as a random variable with its own distribution, not just an unknown fixed constant.

The framework has three components. The **prior distribution** π(θ) encodes your beliefs about θ before seeing any data — it could be flat (uniform, expressing no prior preference) or informative (reflecting domain knowledge). The **likelihood** L(θ|X) = f(X|θ) is the probability of the observed data X given that the parameter is θ — this is the same quantity you would compute in frequentist statistics. The **posterior distribution** π(θ|X) is your updated belief about θ after observing X. Bayes' theorem connects them: π(θ|X) = L(θ|X)π(θ) / ∫L(θ|X)π(θ)dθ. Because the denominator is just a normalizing constant (it does not depend on θ), practitioners write π(θ|X) ∝ L(θ|X)π(θ) — the posterior is proportional to likelihood times prior.

A coin-flipping example makes this concrete. You flip a coin 10 times and observe 7 heads. The parameter θ is the probability of heads. Choose a uniform prior π(θ) = 1 on [0,1]. The likelihood is binomial: L(θ|data) ∝ θ^7(1−θ)^3. The posterior is therefore proportional to θ^7(1−θ)^3, which is a Beta(8, 4) distribution. The frequentist maximum likelihood estimate is simply 7/10. The Bayesian **posterior mean** — which is E[θ|X], computed using your conditional expectation tools — is 8/12 ≈ 0.667, slightly pulled toward 0.5 compared to the MLE. The prior "smoothed" the estimate.

This is where your conditional expectation prerequisite becomes directly useful. All Bayesian point estimates, credible intervals, and predictions derive from the posterior. The optimal estimate under squared-error loss is exactly the posterior mean E[θ|X]. A 95% **credible interval** is any interval [a,b] with ∫ₐᵇ π(θ|X)dθ = 0.95 — you are directly computing the probability that θ lies in [a,b] given the data, which is a more intuitive statement than the frequentist confidence interval.
