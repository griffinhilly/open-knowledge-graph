---
id: covariance-correlation-theory
title: Covariance and Correlation Coefficients
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: expected-value-theory
  type: hard
- id: joint-marginal-distributions
  type: hard
builds-toward:
- linear-regression
- bivariate-normal-distribution
tags:
- covariance
- correlation
stage: formal-systems
status: draft
---

# Covariance and Correlation Coefficients

## Core Idea
Covariance Cov(X,Y)=E[(X−μ_X)(Y−μ_Y)] measures linear association; equals 0 if independent but nonzero doesn't imply dependence. Correlation ρ=Cov(X,Y)/(σ_X σ_Y) ∈ [−1,1] is scale-invariant. Zero correlation means no linear association.
