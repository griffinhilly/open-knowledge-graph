---
id: quasi-maximum-likelihood-estimation
title: Quasi-Maximum Likelihood Estimation
domain: economics
course: econometrics
prerequisites:
- id: maximum-likelihood-econometrics
  type: hard
tags:
- estimation
- maximum-likelihood
- misspecification
stage: advanced
status: draft
---

# Quasi-Maximum Likelihood Estimation

## Core Idea
QML estimates models by maximizing a (possibly incorrect) log-likelihood function. Under mild regularity conditions, QML estimators are consistent and asymptotically normal even if the true distribution differs. The covariance matrix requires a sandwich adjustment accounting for likelihood misspecification.

## Explainer

From your study of maximum likelihood estimation, you know the ideal story: specify the correct probability distribution for the data, write down the log-likelihood, maximize it, and obtain an estimator that is consistent, asymptotically efficient, and whose standard errors come from the inverse Fisher information matrix. **Quasi-maximum likelihood estimation (QMLE)** asks: what happens when you deliberately or inadvertently maximize the wrong likelihood? The answer, under certain conditions, is: less than you might fear.

The intuition starts with an analogy. Suppose you are trying to find the highest point in a mountain range and you use a slightly inaccurate map. If the map preserves the rough topology — if high points on the map correspond to high points in reality — you will still walk toward a peak, even if your route is not optimal. QMLE is similar: if the parametric model you maximize is related to the true data-generating process in the right way (specifically, if the moment conditions implied by the likelihood score are satisfied at the true parameter value), the QML estimator converges to the truth even though the full distributional assumption is wrong.

The most important case is the **linear exponential family** result: if your specified model correctly captures the conditional mean E[y|x], then maximizing any likelihood from the linear exponential family (Gaussian, Poisson, logistic, etc.) yields a consistent estimator of the mean parameters, regardless of the true distribution of y. This is why Poisson regression is routinely applied to non-count, non-negative outcomes like trade flows or innovation counts — the Poisson likelihood is used as a computational device, not as a genuine probabilistic claim. The coefficient estimates are consistent as long as the conditional mean model is right.

The cost of misspecification shows up in the **covariance matrix**. Under true MLE, Var(β̂) = −E[∂²ℓ/∂β∂β']⁻¹ (the inverse Hessian), and this equals the outer product formula E[score · score']. When the likelihood is misspecified, these two quantities no longer agree, so the standard MLE covariance formula is wrong. The correct covariance under QML is the **sandwich estimator**: (H⁻¹)(B)(H⁻¹), where H is the estimated Hessian and B is the estimated outer product of scores. This "bread-meat-bread" structure inflates the estimated variance to account for the fact that the likelihood's curvature no longer accurately reflects the sampling uncertainty. Using the wrong covariance — the standard MLE formula — would produce standard errors that are typically too small, leading to false precision.
