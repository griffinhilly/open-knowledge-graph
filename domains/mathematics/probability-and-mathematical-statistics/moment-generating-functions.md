---
id: moment-generating-functions
title: Moment Generating Functions
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: variance-higher-moments-rigorous
  type: hard
- id: taylor-series
  type: soft
builds-toward:
- characteristic-functions
- central-limit-theorem-rigorous
- multivariate-normal-distribution
tags:
- mgf
- generating-functions
- moments
stage: formal-systems
status: draft
---

# Moment Generating Functions

## Core Idea
The moment generating function (MGF) is M(t) = E[e^{tX}], defined for t in some neighborhood of 0. If M(t) exists, all moments can be recovered: E[Xᵏ] = M^{(k)}(0). The MGF uniquely determines the distribution, and convergence of MGFs implies convergence of distributions.
