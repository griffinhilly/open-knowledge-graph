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
stage: abstract-reasoning
status: draft
---

# Bayesian Inference Foundations

## Core Idea
Bayesian inference treats θ as a random variable with prior distribution π(θ). Given data X, the posterior is π(θ|X) ∝ L(θ|X)π(θ) by Bayes' theorem. The posterior combines prior beliefs with data. Inference is based on the posterior: point estimates, credible intervals, and predictions all follow from the posterior distribution.
