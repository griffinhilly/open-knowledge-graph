---
id: estimator-consistency-unbiasedness
title: 'Estimator Properties: Consistency, Unbiasedness, and Efficiency'
domain: economics
course: econometrics
prerequisites:
- id: ols-assumptions
  type: hard
- id: coefficient-interpretation-regression
  type: soft
builds-toward:
- asymptotic-normality-regression
tags:
- statistical-properties
- inference
stage: formal-systems
status: draft
---

# Estimator Properties: Consistency, Unbiasedness, and Efficiency

## Core Idea
Unbiasedness means the estimator's expected value equals the true parameter; consistency means it converges to the true value as sample size grows; efficiency compares variance among unbiased estimators. OLS is unbiased under assumptions MLR 1-4 and consistent under weaker conditions, making these properties central to assessing when OLS is reliable.

## Explainer

You already know that OLS produces estimates β̂ by minimizing the sum of squared residuals. But a single estimate from a single dataset isn't enough to evaluate an estimator — you need to ask what would happen if you drew many datasets from the same population and ran OLS on each. **Unbiasedness** is a statement about that thought experiment: if E[β̂] = β, the estimator is unbiased, meaning the estimates are centered on the true value across repeated samples. Any individual estimate may be wrong, but there's no systematic pull in one direction.

**Consistency** is a different, and in many ways more practically important, property. An estimator is consistent if it converges in probability to the true parameter as the sample size n grows without bound — written plim(β̂) = β. Think of consistency as saying: "if I had enough data, I'd eventually get the right answer." An unbiased estimator is not necessarily consistent (if its variance doesn't shrink with n), and a consistent estimator is not necessarily unbiased (it can have a small bias in finite samples that disappears asymptotically). The key OLS requirement for consistency is that regressors be contemporaneously exogenous: E[uᵢ | xᵢ] = 0. This is weaker than the full strict exogeneity assumption needed for unbiasedness (MLR 4), which is why OLS remains consistent in some settings where it's technically biased.

**Efficiency** enters when you compare estimators that are all unbiased — which one has the smallest variance? The Gauss-Markov theorem, which you've seen through the OLS assumptions, tells you that OLS is the **Best Linear Unbiased Estimator (BLUE)** under assumptions MLR 1-5. "Best" means minimum variance among all linear unbiased estimators. If errors are also normally distributed (MLR 6), OLS achieves the Cramér-Rao lower bound and is efficient even among nonlinear estimators.

The practical takeaway is a diagnostic hierarchy. When OLS assumptions hold fully, you get unbiasedness and efficiency. When strict exogeneity fails but contemporaneous exogeneity holds, you lose unbiasedness but keep consistency — estimates are wrong in small samples but correct in large ones. When even contemporaneous exogeneity fails (endogeneity), OLS is neither unbiased nor consistent, and no amount of additional data will fix the problem. This is why identifying and addressing endogeneity — through instruments, fixed effects, or natural experiments — is the central challenge of applied econometrics.
