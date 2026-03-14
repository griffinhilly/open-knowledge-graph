---
id: method-of-moments
title: Method of Moments
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: variance-higher-moments-rigorous
  type: hard
- id: weak-law-of-large-numbers
  type: soft
builds-toward:
- consistency-of-estimators
tags:
- method-of-moments
- estimation
- statistics
stage: abstract-reasoning
status: draft
---

# Method of Moments

## Core Idea
The method of moments equates sample moments with population moments: set m̂ₖ = μₖ(θ) where m̂ₖ = (1/n)Σ Xᵢᵏ. Solve for θ. This approach is simple but less efficient than MLE. Method of moments estimators are consistent by the WLLN and asymptotically normal under suitable conditions.
