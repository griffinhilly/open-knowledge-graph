---
id: bayesian-statistics-fundamentals
title: 'Bayesian Statistics: Prior, Posterior, Credible Intervals'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: bayes-theorem-and-inference
  type: hard
- id: probability-density-functions-theory
  type: hard
builds-toward:
- conjugate-priors
tags:
- bayesian
- inference
stage: formal-systems
status: draft
---

# Bayesian Statistics: Prior, Posterior, Credible Intervals

## Core Idea
Bayesian updating: posterior ∝ likelihood × prior. Posterior distribution of θ summarizes belief after seeing data. Credible intervals [a,b] satisfy P(θ∈[a,b]|data)=0.95, directly answering 'where is θ?' Unlike frequentist CIs, these are probability statements about θ.

## Explainer

From Bayes' theorem, you know that P(A|B) = P(B|A)·P(A)/P(B). Bayesian statistics is what happens when A is a hypothesis about a parameter θ and B is the data you observed. Before seeing data, you have a **prior distribution** π(θ) that encodes your beliefs (or lack thereof) about θ. It is a full probability distribution — not just a point estimate, but a spread of plausibility over all possible values of θ. After observing data x, you update this belief using the data's likelihood L(θ; x) = f(x|θ), the probability of seeing your data if θ were the true value.

The update formula is the fundamental equation: **posterior ∝ likelihood × prior**, written π(θ|x) ∝ f(x|θ) · π(θ). The proportionality hides the normalizing constant (the marginal likelihood ∫ f(x|θ) π(θ) dθ), which makes the posterior integrate to 1 but plays no role in inference about θ. Intuitively: the prior says "here is where I thought θ lived before"; the likelihood says "here are the values of θ that make my data probable"; the posterior says "here is where I believe θ lives now, combining both signals." Regions where the prior is high and the likelihood is high become regions where the posterior is especially concentrated.

The **posterior distribution** is the complete answer to a Bayesian inference problem — not a number, but a distribution. From it you can extract any summary you want. The **posterior mean** E[θ|x] and **posterior mode** (MAP estimate) are both point summaries. A **credible interval** [a, b] with coverage 1 − α is any interval satisfying P(θ ∈ [a, b] | x) = 1 − α — a direct probability statement about where θ lies. This is what people often *want* from a confidence interval but cannot get: a 95% credible interval literally means "given my prior and this data, I am 95% sure θ is in [a, b]." A frequentist confidence interval means something more convoluted (it describes a procedure that covers the true θ 95% of the time across hypothetical repetitions), not a probability about this particular θ.

The practical power of the Bayesian framework is most visible when you have genuine prior information — domain knowledge about plausible parameter ranges, previous experiments, or regularizing constraints — and when you need to propagate uncertainty rather than just report a point estimate. The prior is often criticized as subjective, but this objection weakens as data accumulates: with sufficient data, the likelihood dominates the prior, and posteriors from different reasonable priors converge. The Bayesian framework also naturally handles **hierarchical models** (priors on priors), sequential updating (the posterior from one study becomes the prior for the next), and prediction via the posterior predictive distribution p(x̃|x) = ∫ f(x̃|θ) π(θ|x) dθ — integrating over all uncertainty in θ rather than plugging in a point estimate.
