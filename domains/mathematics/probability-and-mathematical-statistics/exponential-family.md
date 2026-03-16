---
id: exponential-family
title: Exponential Family of Distributions
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: distribution-functions-densities-rigorous
  type: hard
- id: maximum-likelihood-estimation-theory
  type: soft
builds-toward:
- sufficient-statistics
- conjugate-priors
tags:
- exponential-family
- distributions
- statistics
stage: formal-systems
status: draft
---

# Exponential Family of Distributions

## Core Idea
A family of distributions {f(x|θ)} belongs to the exponential family if it has the form f(x|θ) = h(x) exp{Σⱼ ηⱼ(θ)Tⱼ(x) - A(θ)}, where A(θ) is the log-partition function. Examples include normal, binomial, Poisson, and exponential. The exponential family is mathematically convenient: sufficient statistics are easy to identify, conjugate priors exist, and maximum likelihood estimators often have closed forms.
