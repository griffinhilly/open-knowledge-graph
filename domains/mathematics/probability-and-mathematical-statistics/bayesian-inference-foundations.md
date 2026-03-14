---
id: bayesian-inference-foundations
title: Bayesian Inference Foundations
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: bayes-theorem
  type: hard
- id: probability-spaces-measure-theoretic
  type: soft
builds-toward:
- conjugate-priors
- bayesian-point-estimation
tags:
- bayesian
- prior
- posterior
stage: abstract-reasoning
status: draft
---

# Bayesian Inference Foundations

## Core Idea
Bayesian inference treats unknown parameters as random variables with a prior π(θ). The posterior π(θ|x) ∝ L(θ|x)π(θ) is computed by Bayes' theorem. Inference is based on the posterior: credible intervals, point estimates, and predictions. Bayesian methods incorporate prior beliefs and naturally quantify uncertainty.
