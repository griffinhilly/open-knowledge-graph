---
id: fisher-information
title: Fisher Information
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: expectation-measure-theoretic
  type: hard
- id: distribution-and-density-functions
  type: hard
- id: chain-rule
  type: soft
builds-toward:
- cramer-rao-lower-bound
- asymptotic-normality-of-mle
tags:
- fisher-information
- likelihood
- second-derivative
stage: abstract-reasoning
status: draft
---

# Fisher Information

## Core Idea
Fisher information is I(θ) = E[(∂ log L/∂θ)²] = -E[∂² log L/∂θ²], measuring information the data carries about θ. For exponential families, I(θ) = A''(θ). Larger information means the parameter is more precisely determined. It is fundamental to the Cramér-Rao lower bound and asymptotic efficiency theory.
