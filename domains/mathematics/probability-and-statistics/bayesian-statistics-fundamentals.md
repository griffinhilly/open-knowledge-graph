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

## Questions

```yaml
- question: "A statistician computes a 95% frequentist confidence interval [0.3, 0.7] for a coin's bias θ. A colleague says: 'There's a 95% chance the true bias is between 0.3 and 0.7.' Is this correct?"
  type: multiple-choice
  options:
    - "Yes — a 95% CI always means a 95% probability that the parameter is in the interval"
    - "No — the interval either contains the true θ or it doesn't; the 95% describes the procedure's long-run coverage across hypothetical repetitions, not a probability about this specific interval"
    - "Yes — as long as the sample size was large, the CI approximates a Bayesian credible interval and the interpretation holds"
    - "No — the colleague should have said '95% probability of observing data consistent with the interval'"
  answer: 1
  explanation: "Once you observe a specific interval [0.3, 0.7], the true θ is a fixed constant — it either is or isn't in that interval. The 95% is a property of the *procedure*: if you ran the experiment many times and computed a CI each time, 95% of those intervals would contain the true θ. A Bayesian credible interval *can* make the probability statement 'P(θ∈[0.3,0.7]|data) = 0.95' — but only because it incorporates a prior and treats θ as a random variable. The frequentist interval cannot make probability statements about a fixed (non-random) θ."

- question: "A researcher has a strong prior belief that a drug effect size θ is near 0.2, encoded as a tight prior. After seeing data that strongly suggests θ ≈ 0.8, what will the posterior look like?"
  type: multiple-choice
  options:
    - "The posterior will be centered at 0.2 — a strongly-held prior anchors the estimate regardless of data"
    - "The posterior will be centered near the likelihood's peak (≈0.8), since sufficient data overwhelms even an informative prior"
    - "The posterior will be bimodal, split between 0.2 and 0.8 to incorporate both signals equally"
    - "The posterior will equal the prior, because the likelihood cannot update a strongly informative prior"
  answer: 1
  explanation: "Posterior ∝ likelihood × prior. With sufficiently strong data (a sharply peaked likelihood), the likelihood overwhelms even an informative prior. The posterior shifts toward the data — not exactly to 0.8 (the prior still pulls), but substantially away from 0.2. This is Bayesian convergence: with enough data, posteriors from different priors converge toward the same answer. Option A is the common misconception about Bayesian updating — a strong prior provides more resistance, but it is not immovable. With strong enough data, the prior's influence shrinks."

- question: "A 95% Bayesian credible interval [a, b] means that, given the observed data and the prior, there is a 95% probability that the true parameter θ lies between a and b."
  type: true-false
  answer: true
  explanation: "This is exactly what a Bayesian credible interval means — and it's the interpretation most people intuitively want from an interval estimate. The interval is derived from the posterior distribution P(θ|data), and the coverage is a direct probability statement about θ's location given all available information. This contrasts with the frequentist confidence interval, which describes a long-run property of the estimation procedure, not a probability about any particular θ."

- question: "If two researchers start with different priors but observe the same data, they will always arrive at the same posterior distribution."
  type: true-false
  answer: false
  explanation: "Different priors lead to different posteriors for the same data — posterior ∝ likelihood × prior, so if the prior differs, the product differs. With large amounts of data, the likelihood dominates and posteriors from 'reasonable' priors converge. But convergence with large samples is not the same as equality: with finite data, especially sparse data, different priors can produce substantively different posteriors. The choice of prior genuinely matters, particularly in small-sample or low-signal settings."

- question: "Explain what it means for the posterior to be a probability distribution over θ, and why this is philosophically different from a frequentist point estimate."
  type: short-answer
  answer: "In Bayesian inference, θ is treated as a random variable with a probability distribution representing our uncertainty about its true value. The posterior π(θ|data) assigns probability to every possible value of θ — encoding not just a best guess but the full shape of our uncertainty. A frequentist treats θ as a fixed (non-random) unknown constant, so 'probability over θ' is a category error in that framework."
  explanation: "The practical consequence is that the posterior supports direct probability statements: 'θ is 80% likely to be above 0.5,' 'the most probable value is 0.3,' 'the 95% credible region is [a,b].' All of these are valid posterior summaries. A frequentist cannot make such statements about θ because θ isn't random. This difference becomes practically important when combining evidence (the posterior of one study becomes the prior for the next), propagating uncertainty through decisions, or communicating results to stakeholders who naturally think in terms of probability over parameters."
```

## Explainer

From Bayes' theorem, you know that P(A|B) = P(B|A)·P(A)/P(B). Bayesian statistics is what happens when A is a hypothesis about a parameter θ and B is the data you observed. Before seeing data, you have a **prior distribution** π(θ) that encodes your beliefs (or lack thereof) about θ. It is a full probability distribution — not just a point estimate, but a spread of plausibility over all possible values of θ. After observing data x, you update this belief using the data's likelihood L(θ; x) = f(x|θ), the probability of seeing your data if θ were the true value.

The update formula is the fundamental equation: **posterior ∝ likelihood × prior**, written π(θ|x) ∝ f(x|θ) · π(θ). The proportionality hides the normalizing constant (the marginal likelihood ∫ f(x|θ) π(θ) dθ), which makes the posterior integrate to 1 but plays no role in inference about θ. Intuitively: the prior says "here is where I thought θ lived before"; the likelihood says "here are the values of θ that make my data probable"; the posterior says "here is where I believe θ lives now, combining both signals." Regions where the prior is high and the likelihood is high become regions where the posterior is especially concentrated.

The **posterior distribution** is the complete answer to a Bayesian inference problem — not a number, but a distribution. From it you can extract any summary you want. The **posterior mean** E[θ|x] and **posterior mode** (MAP estimate) are both point summaries. A **credible interval** [a, b] with coverage 1 − α is any interval satisfying P(θ ∈ [a, b] | x) = 1 − α — a direct probability statement about where θ lies. This is what people often *want* from a confidence interval but cannot get: a 95% credible interval literally means "given my prior and this data, I am 95% sure θ is in [a, b]." A frequentist confidence interval means something more convoluted (it describes a procedure that covers the true θ 95% of the time across hypothetical repetitions), not a probability about this particular θ.

The practical power of the Bayesian framework is most visible when you have genuine prior information — domain knowledge about plausible parameter ranges, previous experiments, or regularizing constraints — and when you need to propagate uncertainty rather than just report a point estimate. The prior is often criticized as subjective, but this objection weakens as data accumulates: with sufficient data, the likelihood dominates the prior, and posteriors from different reasonable priors converge. The Bayesian framework also naturally handles **hierarchical models** (priors on priors), sequential updating (the posterior from one study becomes the prior for the next), and prediction via the posterior predictive distribution p(x̃|x) = ∫ f(x̃|θ) π(θ|x) dθ — integrating over all uncertainty in θ rather than plugging in a point estimate.
