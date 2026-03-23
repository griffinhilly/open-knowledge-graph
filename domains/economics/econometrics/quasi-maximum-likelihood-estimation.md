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
status: validated
---

# Quasi-Maximum Likelihood Estimation

## Core Idea
QML estimates models by maximizing a (possibly incorrect) log-likelihood function. Under mild regularity conditions, QML estimators are consistent and asymptotically normal even if the true distribution differs. The covariance matrix requires a sandwich adjustment accounting for likelihood misspecification.

## Questions

```yaml
- question: "A researcher uses Poisson regression to model bilateral trade flows, which are non-negative but clearly not counts drawn from a Poisson distribution. What can they validly claim about the resulting estimates?"
  type: multiple-choice
  options:
    - "Nothing — the estimates are inconsistent because the distributional assumption is violated"
    - "The coefficient estimates are consistent if the conditional mean is correctly specified, but standard errors require a sandwich adjustment"
    - "The estimates are fully efficient because the Poisson likelihood is always well-behaved"
    - "The coefficient estimates are consistent, and the standard MLE standard errors are valid"
  answer: 1
  explanation: "This is the central use case for QMLE. By the linear exponential family result, maximizing the Poisson likelihood yields consistent estimates of the conditional mean parameters even when the true distribution is not Poisson — as long as the conditional mean model E[y|x] is correctly specified. However, distributional misspecification breaks the equality of the Hessian and outer-product-of-scores formulas, so standard MLE standard errors are invalid. The sandwich estimator (H⁻¹BH⁻¹) is required."

- question: "What is the consequence of applying the standard MLE covariance formula (inverse Hessian) to a QMLE estimator when the likelihood is misspecified?"
  type: multiple-choice
  options:
    - "The standard errors are unaffected because the Hessian is invariant to distributional assumptions"
    - "The standard errors are typically too large, leading to overly conservative inference"
    - "The standard errors are typically too small, producing false precision and over-rejection of true nulls"
    - "The standard errors are correct if the sample size is large enough"
  answer: 2
  explanation: "Under correct specification, the Hessian (expected curvature) and the outer product of scores (expected squared gradient) are equal — the information matrix equality. Misspecification breaks this equality. In practice, using the standard formula when the likelihood is misspecified typically underestimates variance, making confidence intervals too narrow and hypothesis tests too aggressive. The sandwich estimator accounts for this discrepancy by separately estimating both pieces."

- question: "A Poisson regression applied to non-count data can produce consistent coefficient estimates as long as the conditional mean E[y|x] is correctly specified."
  type: true-false
  answer: true
  explanation: "This follows from the linear exponential family result: the Poisson likelihood's score condition is satisfied at the true parameter value whenever the conditional mean is correctly specified, regardless of the true distribution's shape. This is why Poisson regression has become a standard tool for non-negative outcomes like trade flows, patents, and citations — the distributional label 'Poisson' is a computational convenience, not a genuine probabilistic claim about the data."

- question: "A QMLE estimator is only consistent if it converges to the true parameter value, which requires the specified likelihood to match the true data-generating process."
  type: true-false
  answer: false
  explanation: "This is the key misconception QMLE overturns. Under the linear exponential family result, the QML estimator converges to the true parameter even when the likelihood is wrong, as long as the conditional mean is correctly specified. The misspecified likelihood still has its score equal to zero at the true parameter value — this is the regularity condition that ensures consistency. The distributional assumption beyond the mean can be entirely wrong without affecting the probability limit of the estimator."

- question: "Why does quasi-maximum likelihood estimation require a sandwich covariance estimator rather than the standard MLE inverse-Hessian formula?"
  type: short-answer
  answer: "Under correct specification, the information matrix equality holds: the expected Hessian (curvature of the log-likelihood) equals the expected outer product of scores (variance of the gradient). These are two ways of computing the same quantity, so the standard formula is valid. When the likelihood is misspecified, these two quantities differ — the Hessian reflects the shape of the wrong likelihood, while the outer product of scores captures actual sampling variation. The sandwich estimator (H⁻¹BH⁻¹) uses both pieces separately, correctly accounting for the discrepancy and producing valid asymptotic standard errors."
  explanation: "The sandwich structure arises because standard MLE relies on the information matrix equality as a computational shortcut. QMLE cannot use that shortcut. If you use only H⁻¹, you get standard errors that reflect the curvature of the wrong likelihood, which typically underestimates the true sampling variance. The outer-product matrix B corrects for this, and sandwiching it between H⁻¹ gives the correct asymptotic covariance for the QMLE estimator."
```

## Explainer

From your study of maximum likelihood estimation, you know the ideal story: specify the correct probability distribution for the data, write down the log-likelihood, maximize it, and obtain an estimator that is consistent, asymptotically efficient, and whose standard errors come from the inverse Fisher information matrix. **Quasi-maximum likelihood estimation (QMLE)** asks: what happens when you deliberately or inadvertently maximize the wrong likelihood? The answer, under certain conditions, is: less than you might fear.

The intuition starts with an analogy. Suppose you are trying to find the highest point in a mountain range and you use a slightly inaccurate map. If the map preserves the rough topology — if high points on the map correspond to high points in reality — you will still walk toward a peak, even if your route is not optimal. QMLE is similar: if the parametric model you maximize is related to the true data-generating process in the right way (specifically, if the moment conditions implied by the likelihood score are satisfied at the true parameter value), the QML estimator converges to the truth even though the full distributional assumption is wrong.

The most important case is the **linear exponential family** result: if your specified model correctly captures the conditional mean E[y|x], then maximizing any likelihood from the linear exponential family (Gaussian, Poisson, logistic, etc.) yields a consistent estimator of the mean parameters, regardless of the true distribution of y. This is why Poisson regression is routinely applied to non-count, non-negative outcomes like trade flows or innovation counts — the Poisson likelihood is used as a computational device, not as a genuine probabilistic claim. The coefficient estimates are consistent as long as the conditional mean model is right.

The cost of misspecification shows up in the **covariance matrix**. Under true MLE, Var(β̂) = −E[∂²ℓ/∂β∂β']⁻¹ (the inverse Hessian), and this equals the outer product formula E[score · score']. When the likelihood is misspecified, these two quantities no longer agree, so the standard MLE covariance formula is wrong. The correct covariance under QML is the **sandwich estimator**: (H⁻¹)(B)(H⁻¹), where H is the estimated Hessian and B is the estimated outer product of scores. This "bread-meat-bread" structure inflates the estimated variance to account for the fact that the likelihood's curvature no longer accurately reflects the sampling uncertainty. Using the wrong covariance — the standard MLE formula — would produce standard errors that are typically too small, leading to false precision.
