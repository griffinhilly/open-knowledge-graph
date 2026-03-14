---
id: exponential-family
title: The Exponential Family
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: distribution-and-density-functions
  type: hard
- id: sufficient-statistics
  type: soft
builds-toward:
- fisher-information
- maximum-likelihood-estimation-theory
- conjugate-priors
tags:
- exponential-family
- natural-parameters
- sufficient-statistics
stage: abstract-reasoning
status: draft
---

# The Exponential Family

## Core Idea
Exponential family distributions have densities f(x|θ) = h(x) exp(η(θ)·T(x) - A(θ)). Here T(x) is sufficient, η(θ) are natural parameters, and A(θ) is the log-partition function. The family includes normal, exponential, binomial, Poisson, and gamma. Exponential families have special properties: sufficient statistics have known distributions and conjugate priors exist.
