---
id: cramer-rao-lower-bound
title: Cramer-Rao Lower Bound
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: fisher-information
  type: hard
- id: variance-higher-moments-rigorous
  type: hard
builds-toward:
- umvue
- asymptotic-normality-mle
tags:
- cramer-rao
- lower-bounds
- estimation
stage: advanced
status: validated
---

# Cramer-Rao Lower Bound

## Core Idea
For any unbiased estimator T of θ, Var(T) ≥ 1/I(θ). The bound is tight: equality holds iff T is the uniformly minimum variance unbiased estimator (UMVUE). The CRLB shows that Fisher information lower-bounds estimator precision. MLEs are asymptotically efficient, achieving the CRLB in the limit.

## Questions

```yaml
- question: "A researcher claims that because a new experimental design doubles the Fisher information I(θ), the MLE variance is cut in half for all sample sizes. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Doubling Fisher information has no effect on estimator variance — they are unrelated quantities"
    - "The CRLB gives a lower bound 1/I(θ) — doubling I(θ) halves the bound, but the MLE is only asymptotically efficient. At finite sample sizes, the MLE variance may exceed 1/I(θ) and need not decrease by exactly half"
    - "Fisher information cannot be doubled by experimental design — it is a fixed property of the distribution"
    - "The CRLB applies only to Bayesian estimators, not to MLEs"
  answer: 1
  explanation: "The CRLB says Var(T) ≥ 1/I(θ) — the floor drops when I(θ) doubles, but the floor and the actual variance are not the same thing. MLEs are asymptotically efficient (variance approaches 1/I(θ) as n → ∞) but for finite samples, the MLE may not achieve the bound. The claim confuses 'the minimum possible variance' with 'what the MLE actually achieves.' In simple exponential family cases (normal mean, Poisson rate), the MLE does achieve the CRLB exactly — but this is a special property, not a general one."

- question: "The proof of the Cramér-Rao lower bound uses the Cauchy-Schwarz inequality. What is the key role of the unbiasedness condition E[T(X)] = θ in the proof?"
  type: multiple-choice
  options:
    - "Unbiasedness ensures that the score function S = ∂/∂θ log f(X; θ) has mean zero, which is needed to apply Cauchy-Schwarz"
    - "Unbiasedness ensures that differentiating E[T(X)] = θ with respect to θ yields Cov(T, S) = 1, so Cauchy-Schwarz gives 1 ≤ Var(T) · I(θ)"
    - "Unbiasedness guarantees that T and S are independent, simplifying the covariance calculation"
    - "Unbiasedness is not needed — the CRLB applies to all estimators, biased or not"
  answer: 1
  explanation: "The unbiasedness condition E[T] = θ, when differentiated with respect to θ (under regularity), gives Cov(T, S) = 1. This single equation is the constraint that drives the bound: Cauchy-Schwarz then gives Cov(T,S)² ≤ Var(T) · Var(S) = Var(T) · I(θ), so 1 ≤ Var(T) · I(θ), yielding Var(T) ≥ 1/I(θ). Without unbiasedness, Cov(T,S) need not equal 1, and the bound does not apply in this form."

- question: "The Cramér-Rao lower bound applies only to unbiased estimators — a biased estimator can in principle have variance smaller than 1/I(θ)."
  type: true-false
  answer: true
  explanation: "The CRLB as stated bounds the variance of UNBIASED estimators. Biased estimators are not constrained by it: by introducing bias, an estimator can reduce variance below 1/I(θ) — this is the bias-variance tradeoff. For example, a shrinkage estimator or a James-Stein estimator can achieve lower mean squared error than any unbiased estimator by accepting some bias. The CRLB tells us the best achievable variance among estimators that commit to unbiasedness."

- question: "An estimator that achieves variance exactly equal to 1/I(θ) for all finite sample sizes must be the MLE."
  type: true-false
  answer: false
  explanation: "Achieving the CRLB exactly means the estimator is the UMVUE (Uniformly Minimum Variance Unbiased Estimator), not necessarily the MLE. The MLE is asymptotically efficient — it achieves the bound in the limit as n → ∞ — but for finite samples, the MLE may exceed the bound. In exponential family distributions, the sufficient statistic achieves the CRLB exactly (e.g., sample mean for normal μ), and this statistic coincides with the MLE in these cases — but the key property is that it is a linear function of the score, not that it is the MLE per se."

- question: "Explain what Fisher information captures about a statistical model, and why a higher Fisher information leads to a lower Cramér-Rao lower bound."
  type: short-answer
  answer: "Fisher information I(θ) measures how sharply the likelihood function peaks around the true parameter — equivalently, it is the expected squared score (curvature of the log-likelihood). High Fisher information means the data is highly sensitive to the parameter: small changes in θ produce large changes in the likelihood, so the data can 'pin down' θ more precisely. The CRLB says no unbiased estimator can have variance below 1/I(θ). When I(θ) is large, the floor 1/I(θ) is small — meaning the data supports much more precise estimation. When I(θ) is small, the floor is high — even the best estimator cannot be very precise. Fisher information is thus the 'exchange rate' between the informativeness of the data and the achievable precision of estimation."
  explanation: "The intuition: if the likelihood is a sharp, narrow peak (high I(θ)), the data strongly discriminates between nearby parameter values, so estimators can be very precise. If the likelihood is flat (low I(θ)), nearby parameters look nearly identical given the data, and no estimator can reliably distinguish them — hence high variance is unavoidable. The CRLB formalizes this intuition into a hard lower bound, explaining why adding observations (which multiplicatively increases I(θ)) allows estimators to improve, and why some parameters are inherently harder to estimate than others."
```

## Explainer

From Fisher information, you know that I(θ) = E[(∂/∂θ log f(X; θ))²] measures how sharply the likelihood peaks around the true parameter: high Fisher information means the data is highly informative about θ, and the log-likelihood is tightly curved. From variance, you know Var(T) measures how spread out an estimator T is around its mean. The **Cramér-Rao Lower Bound** connects these two: it says that no unbiased estimator can have variance smaller than 1/I(θ). The more information the data carries, the lower this floor — and thus the more precisely θ can be estimated.

The proof uses the Cauchy-Schwarz inequality in a clever way. For any unbiased estimator T(X), the condition E[T(X)] = θ can be differentiated with respect to θ (under regularity conditions) to give Cov(T, S) = 1, where S = ∂/∂θ log f(X; θ) is the **score function**. Since Cov(T, S)² ≤ Var(T) · Var(S) = Var(T) · I(θ), substituting Cov(T, S) = 1 gives 1 ≤ Var(T) · I(θ), which is exactly Var(T) ≥ 1/I(θ). The constraint that E[T] = θ (unbiasedness) is what forces Cov(T, S) = 1 and makes the bound tight.

Equality Var(T) = 1/I(θ) holds if and only if T is a linear function of the score, i.e., T − θ = c(θ) · S for some function c(θ). This happens precisely in **exponential family** distributions, where the sufficient statistic achieves the bound. For example, the sample mean X̄ from a normal distribution N(μ, σ²) has Var(X̄) = σ²/n, and the Fisher information about μ from n observations is n/σ², so Var(X̄) = 1/I(μ) exactly — X̄ is a **efficient estimator**.

For more complex models, the CRLB defines a benchmark for **efficiency**: the efficiency of an estimator T is the ratio (1/I(θ)) / Var(T), which lies in (0, 1]. Maximum likelihood estimators are generally not exactly efficient for finite samples, but they are **asymptotically efficient**: as n → ∞, √n(T_MLE − θ) → N(0, 1/I(θ)), meaning the MLE variance approaches the CRLB in the limit. This asymptotic efficiency is a key justification for using MLEs in practice.
