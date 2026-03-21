---
id: bayesian-phylogenetics
title: Bayesian Phylogenetics
domain: biology
course: evolutionary-biology
prerequisites:
- id: maximum-likelihood-phylogenetics
  type: hard
- id: bayes-theorem
  type: hard
builds-toward:
- molecular-dating
tags:
- phylogenetics
- statistics
- bayesian
stage: advanced
status: draft
---

# Bayesian Phylogenetics

## Core Idea
Bayesian phylogenetics integrates over uncertainty in tree topology, branch lengths, and evolutionary model parameters using posterior probability. MCMC sampling allows efficient exploration of tree space and produces credible intervals for evolutionary parameters. Bayesian methods naturally incorporate prior information and are powerful for dating divergences.

## Questions

```yaml
- question: "A Bayesian phylogenetic analysis assigns a posterior probability of 0.95 to a particular clade. What does this value mean?"
  type: multiple-choice
  options:
    - "The clade appeared in 95% of bootstrap replicates when the sequence data were resampled"
    - "There is a 95% probability that this clade is correct, given the data and the prior model"
    - "The maximum likelihood tree supports this clade with a likelihood ratio of 0.95"
    - "If the analysis were repeated 100 times with different random seeds, the clade would appear in 95 of them"
  answer: 1
  explanation: "Posterior probability has a direct probabilistic interpretation: given the data and the prior distributions you specified, there is a 95% probability that the clade is correct. This is more intuitive than a bootstrap value (option A), which is a frequentist measure of how often a clade appears under data resampling — not a direct probability that the clade is real. Options C and D confuse Bayesian posterior probability with likelihood ratios and repeated-sampling logic respectively. The Bayesian posterior integrates over uncertainty in tree topology, branch lengths, and model parameters."

- question: "Why is Markov chain Monte Carlo (MCMC) sampling necessary in Bayesian phylogenetics rather than simply evaluating all possible trees?"
  type: multiple-choice
  options:
    - "MCMC speeds up the calculation of maximum likelihood scores for each candidate tree"
    - "MCMC corrects for substitution rate heterogeneity across sites in the alignment"
    - "The number of possible tree topologies grows super-exponentially with the number of taxa, making exhaustive evaluation impossible — MCMC samples trees in proportion to their posterior probability"
    - "MCMC allows the analysis to be run without specifying prior distributions on model parameters"
  answer: 2
  explanation: "For even modest numbers of taxa, the number of possible unrooted tree topologies is astronomically large — for 50 species, more than the number of atoms in the observable universe. No computer could evaluate all possible trees, let alone integrate over all parameter values at each topology. MCMC solves this by constructing a random walk through tree space that, at convergence, visits trees in proportion to their posterior probability. The resulting sample of trees approximates the full posterior distribution without requiring exhaustive enumeration."

- question: "In Bayesian phylogenetics, the prior distribution on model parameters can influence the posterior when sequence data are sparse."
  type: true-false
  answer: true
  explanation: "By Bayes' theorem, the posterior is proportional to the likelihood times the prior. When data are abundant and informative, the likelihood dominates and the prior has little effect — Bayesian and maximum likelihood analyses converge on similar results. But when data are sparse (few taxa, short sequences, rapidly evolving regions), the likelihood surface is flat and the prior exerts substantial influence on the posterior. This is why sensitivity analysis — running analyses under different prior specifications and checking whether conclusions change — is essential practice in Bayesian phylogenetics."

- question: "Bayesian phylogenetics and maximum likelihood phylogenetics answer the same fundamental question: which single tree topology is best supported by the sequence data."
  type: true-false
  answer: false
  explanation: "Maximum likelihood finds the single tree topology (and parameter values) that maximizes the probability of observing the data — it produces a point estimate. Bayesian phylogenetics estimates the full posterior probability distribution over all possible tree topologies, branch lengths, and model parameters. Instead of one best tree, you get a distribution of trees, each with a posterior probability. This distributional answer directly quantifies uncertainty about the tree, whereas ML treats uncertainty indirectly through bootstrapping — resampling the data to ask how often a clade appears, not what its probability is."

- question: "What is the fundamental difference between a maximum likelihood phylogenetic analysis and a Bayesian one, in terms of what each produces and how each handles uncertainty?"
  type: short-answer
  answer: "Maximum likelihood finds the single tree topology and parameter values that maximize P(data|tree, parameters) — it produces a point estimate, one best tree. Uncertainty is assessed indirectly through bootstrapping: the data are resampled, the tree is re-estimated each time, and the frequency with which a clade appears across replicates is used as a support measure. Bayesian phylogenetics instead estimates the posterior probability distribution P(tree, parameters|data) ∝ P(data|tree, parameters) × P(prior). MCMC samples from this distribution, producing a collection of trees visited in proportion to their posterior probability. Uncertainty is expressed directly as posterior probabilities on clades — the probability, given the data and prior, that each clade is real."
  explanation: "The practical consequence is that Bayesian posterior probabilities are more intuitively interpretable than bootstrap values, and Bayesian analyses naturally integrate over model parameter uncertainty rather than fixing parameters at their ML estimates. The tradeoff is that Bayesian analyses require specifying prior distributions, which introduces assumptions that can influence results when data are limited."
```

## Explainer

You already understand maximum likelihood phylogenetics, where you search for the tree and parameter values that maximize the probability of observing your sequence data. And from Bayes' theorem, you know that posterior probability is proportional to the likelihood times the prior: P(hypothesis|data) ∝ P(data|hypothesis) × P(hypothesis). **Bayesian phylogenetics** applies this framework to tree inference, and the shift in perspective is profound: instead of finding a single best tree, you estimate the **posterior probability distribution** over all possible trees, branch lengths, and model parameters.

The practical difference is in how uncertainty is handled. Maximum likelihood gives you a point estimate — the single best tree — and you assess confidence through bootstrapping, which resamples your data and re-estimates the tree many times. Bayesian inference instead directly calculates the probability that each possible tree is correct, given the data and your prior beliefs. A **posterior probability of 0.95** on a clade means there is a 95% probability that clade is real, given your data and model — a more intuitive interpretation than a bootstrap value, which measures how often a clade appears under resampling. The Bayesian framework also naturally handles nuisance parameters: rather than fixing the substitution model and estimating the tree, you can let the model parameters (substitution rates, base frequencies, rate variation across sites) vary and **integrate over their uncertainty**.

The computational challenge is that the number of possible tree topologies grows super-exponentially with the number of taxa — for just 50 species, there are more possible unrooted trees than atoms in the observable universe. You cannot evaluate every tree, so Bayesian phylogenetics relies on **Markov chain Monte Carlo (MCMC)** sampling. The MCMC algorithm starts with a random tree, proposes small modifications (rearranging branches, adjusting lengths), and accepts or rejects each proposal based on whether it increases the posterior probability. Over millions of iterations, the chain converges to a stationary distribution that samples trees in proportion to their posterior probability. The set of sampled trees is summarized as a **consensus tree** with posterior probabilities on each branch.

**Prior distributions** are both the strength and the controversy of Bayesian phylogenetics. You must specify priors on tree topology (usually uniform), branch lengths (often exponential), and model parameters. For molecular dating, priors on divergence times incorporate fossil calibration points — known minimum or maximum ages for specific nodes. When data are abundant, the prior has minimal influence and Bayesian and likelihood results converge. When data are sparse, the prior matters more, which is why sensitivity analysis (running the analysis with different priors and checking whether conclusions change) is essential practice. Programs like MrBayes and BEAST implement these methods and have become standard tools for phylogenetic inference and molecular dating.
