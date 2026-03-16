---
id: conjugate-priors
title: Conjugate Priors
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: bayesian-inference-foundations
  type: hard
- id: exponential-family
  type: soft
builds-toward:
- bayesian-point-estimation
tags:
- conjugate-priors
- bayesian-inference
- statistics
stage: advanced
status: draft
---

# Conjugate Priors

## Core Idea
A prior π is conjugate for a likelihood if the posterior π(θ|X) is in the same family as the prior. For exponential family likelihoods, conjugate priors exist and have closed-form posteriors. Examples: Beta prior for Binomial likelihood, Normal prior for Normal likelihood with known variance. Conjugate priors simplify Bayesian computation.

## Explainer

From your study of Bayesian inference, you know that updating beliefs works through Bayes' theorem: posterior ∝ likelihood × prior. In principle, this always works. In practice, the posterior is an integral that must be normalized — and for most likelihood-prior combinations, that integral has no closed form. Conjugate priors are the elegant exception: they are the priors for which the posterior lands in the same distributional family, making the update analytic.

The **Beta-Binomial** pairing is the canonical example. Suppose you're estimating the probability p of success in a coin flip, and you observe X successes in n trials. The Binomial likelihood is L(p | X) ∝ p^X (1−p)^{n−X}. Now choose a Beta(α, β) prior for p, which has density π(p) ∝ p^{α−1}(1−p)^{β−1}. Multiplying them together: posterior ∝ p^{X+α−1}(1−p)^{n−X+β−1}. This is exactly the kernel of a Beta(α + X, β + n − X) distribution. The posterior is Beta — the same family as the prior. The hyperparameters α and β act like "pseudo-counts": α is like having seen α−1 prior successes, β like α−1 prior failures. Observing X real successes simply adds X to α, and (n−X) to β.

This **hyperparameter update rule** is the payoff of conjugacy. You don't need integration; you just need addition. And the interpretation is intuitive: if you start with a flat (uninformative) Beta(1, 1) prior — which is just Uniform(0,1) — and observe 7 heads in 10 flips, your posterior is Beta(8, 4). The posterior mean is 8/(8+4) = 2/3, which sits between the prior mean of 1/2 and the maximum likelihood estimate of 7/10. The prior pulls the estimate toward the center; more data makes the data dominate.

A second important pair is **Normal-Normal**: a Normal prior on a Normal mean (with known variance) produces a Normal posterior. The update blends the prior mean and the sample mean in proportion to their respective precisions (inverse variances). A high-precision prior dominates; a high-precision likelihood (many observations or small sampling variance) dominates. This is the formal machinery behind the intuition that "more data should overwhelm prior beliefs."

Conjugate priors are not always the right choice — they may not accurately represent your actual prior beliefs, and modern Markov Chain Monte Carlo methods can handle arbitrary posteriors. But conjugate priors remain important for three reasons: they give closed-form posteriors for fast computation, their hyperparameters have natural interpretations as prior pseudo-data, and they build intuition for how Bayesian updating works before you encounter more complex models. When a conjugate prior exists and is reasonable, using it is both computationally efficient and conceptually transparent.
