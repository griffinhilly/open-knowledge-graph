---
id: bayesian-epidemiology
title: Bayesian Methods in Epidemiology
domain: health-and-human-development
course: epidemiology
prerequisites:
- id: missing-data-epidemiology
  type: soft
- id: multivariable-regression-epi
  type: hard
tags:
- bayesian-inference
- prior-specification
- posterior-inference
stage: advanced
status: draft
---

# Bayesian Methods in Epidemiology

## Core Idea
Bayesian epidemiology combines prior beliefs about parameters with observed data to produce posterior distributions. Bayesian methods naturally handle complex models, missing data, and indirect evidence, and yield probabilistic statements about parameters and hypotheses.

## Explainer

From your work in multivariable regression, you are accustomed to a particular mode of inference: fit a model to the data, estimate coefficients, compute confidence intervals, and evaluate statistical significance via p-values. This is the **frequentist** framework — parameters are treated as fixed (if unknown) quantities, and probability refers to long-run frequencies over hypothetical repeated samples. Bayesian inference offers a different and complementary framework. In Bayesian thinking, parameters are treated as **random variables** with probability distributions, and "probability" describes your degree of belief given the available information. The payoff is that you can make direct probabilistic statements about the parameters themselves — not just about hypothetical repeated samples.

The mechanics rest on Bayes' theorem. You begin with a **prior distribution** P(θ) that encodes your beliefs about a parameter θ before observing new data. After collecting data D, you update via the likelihood P(D|θ) — the probability of observing those data given each possible value of the parameter. The result is the **posterior distribution**: P(θ|D) ∝ P(θ) × P(D|θ). In words: your posterior belief is your prior belief, updated by the evidence from the data. The posterior combines what you knew before the study with what the data tell you, weighted by how informative the data are. When data are abundant and informative, the posterior will be dominated by the likelihood, and the choice of prior matters little. When data are sparse, the prior carries more weight — which is both a strength and a responsibility, since the choice of prior then substantially influences conclusions.

In epidemiology, Bayesian methods offer several concrete advantages over purely frequentist approaches. First, **prior information from previous studies or mechanistic knowledge** can be formally incorporated. If you are studying the effect of a well-characterized exposure in a new population, a prior derived from meta-analytic estimates of effect sizes in similar populations is a rational and efficient use of scientific knowledge. Second, Bayesian **posterior distributions** directly answer the questions practitioners actually want to ask: "Given these data, what is the probability that the true relative risk exceeds 1.5?" — something a p-value cannot tell you. Third, complex hierarchical models (multilevel, longitudinal, spatial), missing data problems, and models with many parameters are often more tractable in a Bayesian framework, where **Markov Chain Monte Carlo (MCMC)** sampling algorithms can approximate posterior distributions even when analytic solutions are unavailable.

The key practical challenge in Bayesian epidemiology is **prior specification** — choosing prior distributions that are substantively defensible and not inadvertently dominating the analysis. Analysts often report sensitivity analyses using different priors (informative priors versus weakly informative or non-informative priors) to show how conclusions change with prior assumptions. When results are robust across a range of plausible priors, the posterior is said to be **prior-robust**, and the evidence is convincing. When results depend heavily on the prior, the analysis honestly reveals that the data alone are insufficient to resolve the question, which is itself a scientifically important finding.
