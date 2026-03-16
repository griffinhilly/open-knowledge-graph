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
status: draft
---

# Bayesian Inference Foundations

## Core Idea
Bayesian inference treats θ as a random variable with prior distribution π(θ). Given data X, the posterior is π(θ|X) ∝ L(θ|X)π(θ) by Bayes' theorem. The posterior combines prior beliefs with data. Inference is based on the posterior: point estimates, credible intervals, and predictions all follow from the posterior distribution.

## Explainer

You already know Bayes' theorem as a formula for flipping conditional probabilities: P(A|B) = P(B|A)P(A)/P(B). Bayesian inference scales this up to statistical parameters. Instead of reasoning about events A and B, you reason about an unknown parameter θ (say, the true probability of heads on a coin, or the mean weight of a population). The key move is to treat θ as a random variable with its own distribution, not just an unknown fixed constant.

The framework has three components. The **prior distribution** π(θ) encodes your beliefs about θ before seeing any data — it could be flat (uniform, expressing no prior preference) or informative (reflecting domain knowledge). The **likelihood** L(θ|X) = f(X|θ) is the probability of the observed data X given that the parameter is θ — this is the same quantity you would compute in frequentist statistics. The **posterior distribution** π(θ|X) is your updated belief about θ after observing X. Bayes' theorem connects them: π(θ|X) = L(θ|X)π(θ) / ∫L(θ|X)π(θ)dθ. Because the denominator is just a normalizing constant (it does not depend on θ), practitioners write π(θ|X) ∝ L(θ|X)π(θ) — the posterior is proportional to likelihood times prior.

A coin-flipping example makes this concrete. You flip a coin 10 times and observe 7 heads. The parameter θ is the probability of heads. Choose a uniform prior π(θ) = 1 on [0,1]. The likelihood is binomial: L(θ|data) ∝ θ^7(1−θ)^3. The posterior is therefore proportional to θ^7(1−θ)^3, which is a Beta(8, 4) distribution. The frequentist maximum likelihood estimate is simply 7/10. The Bayesian **posterior mean** — which is E[θ|X], computed using your conditional expectation tools — is 8/12 ≈ 0.667, slightly pulled toward 0.5 compared to the MLE. The prior "smoothed" the estimate.

This is where your conditional expectation prerequisite becomes directly useful. All Bayesian point estimates, credible intervals, and predictions derive from the posterior. The optimal estimate under squared-error loss is exactly the posterior mean E[θ|X]. A 95% **credible interval** is any interval [a,b] with ∫ₐᵇ π(θ|X)dθ = 0.95 — you are directly computing the probability that θ lies in [a,b] given the data, which is a more intuitive statement than the frequentist confidence interval.
