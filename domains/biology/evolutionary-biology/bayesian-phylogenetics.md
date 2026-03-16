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

## Explainer

You already understand maximum likelihood phylogenetics, where you search for the tree and parameter values that maximize the probability of observing your sequence data. And from Bayes' theorem, you know that posterior probability is proportional to the likelihood times the prior: P(hypothesis|data) ∝ P(data|hypothesis) × P(hypothesis). **Bayesian phylogenetics** applies this framework to tree inference, and the shift in perspective is profound: instead of finding a single best tree, you estimate the **posterior probability distribution** over all possible trees, branch lengths, and model parameters.

The practical difference is in how uncertainty is handled. Maximum likelihood gives you a point estimate — the single best tree — and you assess confidence through bootstrapping, which resamples your data and re-estimates the tree many times. Bayesian inference instead directly calculates the probability that each possible tree is correct, given the data and your prior beliefs. A **posterior probability of 0.95** on a clade means there is a 95% probability that clade is real, given your data and model — a more intuitive interpretation than a bootstrap value, which measures how often a clade appears under resampling. The Bayesian framework also naturally handles nuisance parameters: rather than fixing the substitution model and estimating the tree, you can let the model parameters (substitution rates, base frequencies, rate variation across sites) vary and **integrate over their uncertainty**.

The computational challenge is that the number of possible tree topologies grows super-exponentially with the number of taxa — for just 50 species, there are more possible unrooted trees than atoms in the observable universe. You cannot evaluate every tree, so Bayesian phylogenetics relies on **Markov chain Monte Carlo (MCMC)** sampling. The MCMC algorithm starts with a random tree, proposes small modifications (rearranging branches, adjusting lengths), and accepts or rejects each proposal based on whether it increases the posterior probability. Over millions of iterations, the chain converges to a stationary distribution that samples trees in proportion to their posterior probability. The set of sampled trees is summarized as a **consensus tree** with posterior probabilities on each branch.

**Prior distributions** are both the strength and the controversy of Bayesian phylogenetics. You must specify priors on tree topology (usually uniform), branch lengths (often exponential), and model parameters. For molecular dating, priors on divergence times incorporate fossil calibration points — known minimum or maximum ages for specific nodes. When data are abundant, the prior has minimal influence and Bayesian and likelihood results converge. When data are sparse, the prior matters more, which is why sensitivity analysis (running the analysis with different priors and checking whether conclusions change) is essential practice. Programs like MrBayes and BEAST implement these methods and have become standard tools for phylogenetic inference and molecular dating.
