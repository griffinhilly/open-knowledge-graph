---
id: umvue
title: Uniformly Minimum-Variance Unbiased Estimation (UMVUE)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: sufficient-statistics
  type: hard
- id: cramer-rao-lower-bound
  type: soft
builds-toward:
- rao-blackwell-theorem
tags:
- umvue
- unbiased
- minimum-variance
stage: abstract-reasoning
status: draft
---

# Uniformly Minimum-Variance Unbiased Estimation (UMVUE)

## Core Idea
A UMVUE is an unbiased estimator with minimum variance among all unbiased estimators for θ. By the Lehmann-Scheffé theorem, if T is a complete sufficient statistic and T̂ is unbiased for g(θ), then T̂ is the UMVUE. UMVUEs achieve the Cramér-Rao lower bound when achievable, but may be dominated by biased estimators.
