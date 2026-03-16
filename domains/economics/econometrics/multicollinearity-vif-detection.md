---
id: multicollinearity-vif-detection
title: 'Multicollinearity: Detection Using VIF'
domain: economics
course: econometrics
prerequisites:
- id: multicollinearity
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
- id: condition-number-of-a-matrix
  type: soft
- id: linear-independence
  type: soft
tags:
- multicollinearity
- diagnostics
stage: formal-systems
status: draft
---

# Multicollinearity: Detection Using VIF

## Core Idea
The Variance Inflation Factor VIFⱼ = 1 / (1 - Rⱼ²) measures how much variance of β̂ⱼ is inflated by collinearity with other regressors. Rules of thumb: VIF > 10 indicates severe multicollinearity; values 5-10 suggest moderate concern. Correlation matrix and condition number also reveal collinearity patterns.

## Explainer

From your study of multicollinearity, you know the core problem: when predictors move together, OLS has trouble distinguishing their individual effects on the outcome. The coefficient estimates become unreliable — large standard errors, wild sign flips when a variable is added or removed, coefficients that are individually insignificant yet jointly significant. The **Variance Inflation Factor** gives you a precise, interpretable measure of how severe this inflation is for each predictor.

The intuition behind VIFⱼ = 1 / (1 - Rⱼ²) comes from an **auxiliary regression**: regress predictor j on all other predictors in your model. The R² from that auxiliary regression tells you how well the other predictors can "explain" predictor j — in other words, how redundant predictor j is. If Rⱼ² = 0, predictor j is orthogonal to all others, and VIF = 1 (no inflation). If Rⱼ² = 0.9, ninety percent of predictor j's variation is explained by the others, and VIF = 10 (ten times as much variance as you'd have with no collinearity). This connects directly to linear independence: a VIF approaching infinity signals that the columns of your design matrix X are nearly linearly dependent.

The **condition number** of the matrix X'X, which you've encountered, provides a complementary diagnostic. It equals the square root of the ratio of the largest to smallest eigenvalue. Large eigenvalues correspond to directions in predictor space with lots of variation; small eigenvalues correspond to near-collinear combinations. A condition number above 30 is often flagged as problematic. While VIF diagnoses collinearity for individual predictors, the condition number and **eigenvalue decomposition** reveal which combinations of predictors are nearly collinear — useful when the problem involves several predictors interacting.

The harder question is what to do about multicollinearity once detected. OLS remains unbiased — multicollinearity doesn't cause bias, only imprecision. If your goal is prediction rather than causal inference, high VIFs may be tolerable. For causal interpretation, solutions include dropping one of a pair of highly correlated variables, constructing a composite index, using principal components, or collecting more data to increase precision. The key diagnostic insight is this: if removing one variable substantially changes the coefficients on others, you're seeing collinearity in action — the model is not identifying individual effects cleanly.
