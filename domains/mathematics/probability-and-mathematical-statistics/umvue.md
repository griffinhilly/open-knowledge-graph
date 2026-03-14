---
id: umvue
title: Uniformly Minimum Variance Unbiased Estimation (UMVUE)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: cramer-rao-lower-bound
  type: hard
- id: sufficient-statistics
  type: hard
builds-toward:
- rao-blackwell-theorem
tags:
- umvue
- unbiased-estimation
- statistics
stage: abstract-reasoning
status: draft
---

# Uniformly Minimum Variance Unbiased Estimation (UMVUE)

## Core Idea
A UMVUE is an unbiased estimator with minimum variance among all unbiased estimators. By the Cramer-Rao bound, no unbiased estimator can have variance less than 1/I(θ). A necessary condition for a UMVUE is that it's a function of a complete sufficient statistic. UMVUEs need not always exist, and when they do, they are often difficult to find.
