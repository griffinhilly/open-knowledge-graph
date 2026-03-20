---
id: bayesian-inference-intro
title: Introduction to Bayesian Inference
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: bayes-theorem
  type: hard
- id: probability-spaces-measure-theoretic
  type: soft
builds-toward:
- bayesian-point-estimation
tags:
- bayesian
- inference
- probability
stage: advanced
status: draft
---

# Introduction to Bayesian Inference

## Core Idea
Bayesian inference uses Bayes' rule to update prior beliefs about parameters given data: P(θ|data) ∝ P(data|θ)P(θ). The posterior distribution combines information from the prior and likelihood. Bayesian methods naturally incorporate prior knowledge and quantify uncertainty.

## How It's Best Learned
Apply Bayes' rule to simple problems with discrete parameters. Compare frequentist and Bayesian confidence/credible intervals. Choose sensible priors for familiar distributions. Recognize sensitivity of conclusions to prior specification.

## Explainer

You already know Bayes' theorem: P(A|B) = P(B|A)P(A)/P(B). Bayesian inference is the application of this rule to statistical learning — using it to update beliefs about unknown parameters as data arrives. The key conceptual shift is that in the Bayesian framework, unknown parameters are treated as **random variables** with probability distributions, not as fixed but unknown constants. This makes it possible to make direct probability statements about parameters, which frequentist inference cannot do.

The structure of Bayesian inference has three components. The **prior distribution** P(θ) encodes your beliefs about the parameter θ before seeing any data. It might be broad and uninformative if you know little, or informative if domain knowledge constrains the plausible values. The **likelihood** P(data|θ) tells you how probable the observed data would be if the parameter were θ — this is the same likelihood function you encounter in maximum likelihood estimation. Multiplying them and normalizing gives the **posterior distribution** P(θ|data) ∝ P(data|θ)P(θ), which encodes updated beliefs about θ after observing the data. The posterior is the complete answer to a Bayesian inference problem.

A concrete example makes this tangible. Suppose you want to estimate a coin's probability of heads, θ. Your prior might be a Beta(2, 2) distribution — slightly favoring θ near 0.5 but not strongly. You flip the coin 10 times and see 7 heads. The likelihood is Binomial: P(7 heads | θ) ∝ θ⁷(1−θ)³. The posterior is Beta(2+7, 2+3) = Beta(9, 5) — a distribution centered near 9/14 ≈ 0.64, updated from 0.5 toward the observed proportion but not entirely swamped by the data. You can read off a **credible interval**: the central 95% of the Beta(9,5) distribution gives an interval within which θ falls with 95% probability, given the data and prior.

The contrast with frequentist inference is philosophically significant. A frequentist 95% confidence interval means: if you repeated this procedure many times, 95% of the resulting intervals would contain the true θ. It says nothing about the probability that *this* interval contains θ. A Bayesian 95% **credible interval** directly says: given this data and prior, P(θ ∈ interval | data) = 0.95. This is typically what practitioners intuitively want to say. The cost is that Bayesian inference depends on the prior, and different priors lead to different posteriors. When data is plentiful, the likelihood dominates and the prior matters little. When data is sparse, prior specification is critical — which is why sensitivity analysis (checking whether conclusions change under different reasonable priors) is a standard part of applied Bayesian work.
