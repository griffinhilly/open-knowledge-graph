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
status: draft
---

# Cramer-Rao Lower Bound

## Core Idea
For any unbiased estimator T of θ, Var(T) ≥ 1/I(θ). The bound is tight: equality holds iff T is the uniformly minimum variance unbiased estimator (UMVUE). The CRLB shows that Fisher information lower-bounds estimator precision. MLEs are asymptotically efficient, achieving the CRLB in the limit.

## Explainer

From Fisher information, you know that I(θ) = E[(∂/∂θ log f(X; θ))²] measures how sharply the likelihood peaks around the true parameter: high Fisher information means the data is highly informative about θ, and the log-likelihood is tightly curved. From variance, you know Var(T) measures how spread out an estimator T is around its mean. The **Cramér-Rao Lower Bound** connects these two: it says that no unbiased estimator can have variance smaller than 1/I(θ). The more information the data carries, the lower this floor — and thus the more precisely θ can be estimated.

The proof uses the Cauchy-Schwarz inequality in a clever way. For any unbiased estimator T(X), the condition E[T(X)] = θ can be differentiated with respect to θ (under regularity conditions) to give Cov(T, S) = 1, where S = ∂/∂θ log f(X; θ) is the **score function**. Since Cov(T, S)² ≤ Var(T) · Var(S) = Var(T) · I(θ), substituting Cov(T, S) = 1 gives 1 ≤ Var(T) · I(θ), which is exactly Var(T) ≥ 1/I(θ). The constraint that E[T] = θ (unbiasedness) is what forces Cov(T, S) = 1 and makes the bound tight.

Equality Var(T) = 1/I(θ) holds if and only if T is a linear function of the score, i.e., T − θ = c(θ) · S for some function c(θ). This happens precisely in **exponential family** distributions, where the sufficient statistic achieves the bound. For example, the sample mean X̄ from a normal distribution N(μ, σ²) has Var(X̄) = σ²/n, and the Fisher information about μ from n observations is n/σ², so Var(X̄) = 1/I(μ) exactly — X̄ is a **efficient estimator**.

For more complex models, the CRLB defines a benchmark for **efficiency**: the efficiency of an estimator T is the ratio (1/I(θ)) / Var(T), which lies in (0, 1]. Maximum likelihood estimators are generally not exactly efficient for finite samples, but they are **asymptotically efficient**: as n → ∞, √n(T_MLE − θ) → N(0, 1/I(θ)), meaning the MLE variance approaches the CRLB in the limit. This asymptotic efficiency is a key justification for using MLEs in practice.
