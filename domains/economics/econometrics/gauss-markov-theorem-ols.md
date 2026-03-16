---
id: gauss-markov-theorem-ols
title: Gauss-Markov Theorem and OLS Efficiency
domain: economics
course: econometrics
prerequisites:
- id: least-squares-regression-fundamentals
  type: hard
- id: ols-assumptions
  type: hard
- id: linear-algebra
  type: soft
builds-toward:
- estimator-consistency-unbiasedness
tags:
- efficiency
- ols
- theorem
stage: formal-systems
status: draft
---

# Gauss-Markov Theorem and OLS Efficiency

## Core Idea
Under the Gauss-Markov assumptions (linearity, zero-mean errors, homoskedasticity, no autocorrelation, no perfect multicollinearity), OLS is the Best Linear Unbiased Estimator (BLUE)—it has the smallest variance among all linear unbiased estimators. This fundamental result justifies OLS as the primary estimation method in applied econometrics.

## Explainer

When you learned least-squares regression, you learned how OLS works mechanically — it minimizes the sum of squared residuals to find coefficients. The Gauss-Markov theorem answers a different and deeper question: *why should you use OLS?* Given that infinitely many estimators could produce an estimate of a regression coefficient, the theorem says OLS is the best among a specific class — linear and unbiased — as long as five assumptions hold.

Let's unpack what **BLUE** actually means. "Linear" means the estimator is a linear function of the observed outcomes Y. "Unbiased" means the expected value of the estimate equals the true parameter: E[β̂] = β. Many estimators are unbiased — you could just pick one observation's Y/X ratio, and on average it might equal β. But unbiased isn't enough; you also want precision. "Best" means lowest variance among all linear unbiased estimators. The Gauss-Markov theorem says OLS achieves this minimum variance — no other estimator in this class is more efficient.

The five **Gauss-Markov assumptions** are conditions on the data-generating process, not on the sample. Linearity means the true model is linear in parameters (not necessarily in variables — you can include X² and still satisfy linearity). Zero-mean errors means Cov(X, u) = 0 — errors are uncorrelated with regressors, which is the exogeneity condition. **Homoskedasticity** means all errors have the same variance: Var(uᵢ) = σ² for all i. **No autocorrelation** means Cov(uᵢ, uⱼ) = 0 for i ≠ j. No perfect multicollinearity means the regressors aren't exact linear combinations of each other. Each assumption plays a specific role in the proof — violate one and a competing estimator can beat OLS.

What happens when assumptions fail is as instructive as when they hold. If errors are **heteroskedastic** (unequal variance), OLS is still unbiased but is no longer efficient — Generalized Least Squares (GLS), which weights observations by the inverse of their error variance, produces lower-variance estimates. If errors are **autocorrelated**, the same logic applies. If the zero-mean/exogeneity assumption fails — as in simultaneous equations or omitted variable bias — OLS is not even unbiased, let alone efficient, and instrumental variables become necessary. The Gauss-Markov theorem thus serves as a diagnostic framework: identify which assumption is violated, and the right alternative estimator follows directly from that diagnosis.

