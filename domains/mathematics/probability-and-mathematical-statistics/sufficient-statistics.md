---
id: sufficient-statistics
title: Sufficient Statistics
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: conditional-expectation
  type: hard
- id: random-variables-as-measurable-functions
  type: soft
builds-toward:
- fisher-information
- umvue
- maximum-likelihood-estimation-theory
tags:
- sufficiency
- estimation
- data-reduction
stage: abstract-reasoning
status: draft
---

# Sufficient Statistics

## Core Idea
A statistic T(X) is sufficient for parameter θ if the conditional distribution of X given T(X) does not depend on θ. By the factorization criterion, T is sufficient iff L(θ;x) = g(T(x),θ)h(x) where h is θ-free. Sufficient statistics capture all information relevant to θ, enabling data reduction without information loss.
