---
id: sufficient-statistics
title: Sufficient Statistics
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: conditional-expectation
  type: hard
- id: exponential-family
  type: soft
builds-toward:
- rao-blackwell-theorem
- cramer-rao-lower-bound
tags:
- sufficient-statistics
- statistics
- inference
stage: advanced
status: draft
---

# Sufficient Statistics

## Core Idea
A statistic T(X) is sufficient for θ if the conditional distribution of X given T(X) does not depend on θ. Intuitively, T captures all information about θ in the data. The factorization theorem: T is sufficient iff f(x|θ) = g(T(x)|θ)h(x) where h doesn't depend on θ. Sufficient statistics form the basis for efficient inference.
