---
id: bayesian-methods-social-science
title: Bayesian Methods in Social Science
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: probability-and-statistics
  type: hard
- id: research-design-advanced
  type: soft
- id: bayes-theorem
  type: hard
- id: conditional-probability-fundamentals
  type: hard
- id: probability-axioms
  type: hard
- id: conditional-probability
  type: soft
builds-toward:
- bayesian-network-models-causal
- hierarchical-bayesian-models
tags:
- bayesian
- inference
- statistical-modeling
stage: advanced
status: draft
---

# Bayesian Methods in Social Science

## Core Idea
Bayesian methods use prior knowledge and observed data to estimate posterior probability distributions. They provide a principled framework for incorporating uncertainty, updating beliefs as new evidence arrives, and comparing competing theoretical models. Unlike frequentist approaches, Bayesian inference allows direct probability statements about parameters and is particularly useful for small samples and complex hierarchical social phenomena.

## How It's Best Learned
Start with simple binomial models and conjugate priors, then progress to MCMC methods using Stan or JAGS. Apply to real social science datasets comparing prior specifications.

## Common Misconceptions
- Assuming all priors are equally subjective when domain expertise can justify informative priors.
- Confusing posterior probability intervals with frequentist confidence intervals (they have different interpretations).
- Overestimating computational burden—modern software makes Bayesian estimation accessible.

## Explainer

You already know Bayes' theorem as a formula for updating probabilities: the posterior probability of a hypothesis given evidence equals the prior probability multiplied by the likelihood of the evidence, normalized by the total probability of the evidence. Bayesian methods in social science take that same logic and scale it up from a single calculation into a full framework for statistical inference. Instead of asking "is this effect statistically significant at p < 0.05?", a Bayesian analyst asks "what is our probability distribution over possible parameter values, after observing the data?"

The key inputs are the **prior distribution** — your quantified uncertainty about a parameter before observing data — and the **likelihood function** — how probable the observed data would be under different parameter values. Multiplying them and normalizing produces the **posterior distribution**, which represents updated uncertainty. The shift from a point estimate (like a regression coefficient) to a full distribution is what makes Bayesian inference particularly valuable in social science: it lets you say "there is a 90% probability that this effect is between 0.2 and 0.8 standard deviations" rather than "I reject the null at α = 0.05," which is a more honest representation of what a social scientist actually wants to know.

Prior selection is the most consequential methodological choice. An **uninformative prior** treats all parameter values as equally plausible before seeing data — useful when you genuinely have no domain knowledge. An **informative prior** encodes existing theory or previous research results. This is not a bug; it is a feature. If three previous studies all found effect sizes near 0.4, incorporating that prior knowledge prevents you from being misled by a small, noisy sample. The common misconception is that priors make Bayesian analysis "subjective" in a way frequentist analysis is not — but frequentist choices (which model to fit, which controls to include) involve equivalent substantive assumptions, just less explicitly stated.

In practice, most Bayesian social science models require numerical methods. **Markov Chain Monte Carlo (MCMC)** algorithms like Hamiltonian Monte Carlo (used by Stan) draw samples from the posterior distribution rather than computing it analytically. Think of the posterior as a landscape; MCMC sends walkers around that landscape, spending more time in high-probability regions, until the collection of visited locations accurately represents the full distribution. Modern software — Stan, JAGS, brms in R — has made this accessible: you specify the model structure and priors, and the sampler handles the rest.

Bayesian methods are especially well-suited to social science's structural challenges. Small samples (common in comparative politics, ethnographic follow-ups, natural experiments) produce posteriors that are heavily shaped by the prior — which is exactly right, because small data should update beliefs less dramatically than large data. Hierarchical or multilevel phenomena, where individuals are nested in groups that are nested in contexts, map naturally onto **hierarchical Bayesian models**, where priors on lower-level parameters are themselves drawn from a higher-level distribution. This partial pooling — borrowing strength across groups — addresses the classic trade-off between ignoring group differences and treating each group entirely separately. The Bayesian framework also makes model comparison natural: you can compute the posterior probability of each competing theoretical model given the data, rather than simply testing whether any single model fits better than a null.
