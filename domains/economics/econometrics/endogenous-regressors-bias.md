---
id: endogenous-regressors-bias
title: 'Endogenous Regressors: Bias and Consequences'
domain: economics
course: econometrics
prerequisites:
- id: endogeneity
  type: hard
- id: omitted-variable-bias
  type: hard
builds-toward:
- instrumental-variables-validity
tags:
- endogeneity
- causality
- bias
stage: formal-systems
status: draft
---

# Endogenous Regressors: Bias and Consequences

## Core Idea
Endogeneity—when E[Xⱼuᵢ] ≠ 0—causes OLS bias and inconsistency. Sources include omitted confounders, simultaneous causality, and measurement error in regressors. Even weak correlation between Xⱼ and u induces substantial bias; direction and magnitude depend on signs and magnitudes of correlations.
