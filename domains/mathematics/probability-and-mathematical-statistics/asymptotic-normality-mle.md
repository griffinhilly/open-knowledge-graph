---
id: asymptotic-normality-mle
title: Asymptotic Normality of MLEs
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: consistency-of-estimators
  type: hard
- id: central-limit-theorem-rigorous
  type: hard
- id: fisher-information
  type: hard
builds-toward:
- umvue
- confidence-intervals-rigorous-theory
tags:
- asymptotic-normality
- mle
- asymptotics
stage: advanced
status: draft
---

# Asymptotic Normality of MLEs

## Core Idea
Under regularity conditions, √n(θ̂ₙ - θ) converges in distribution to N(0, 1/I(θ)), where I(θ) is Fisher information. This shows MLEs are asymptotically normal and efficient (achieving the Cramer-Rao bound asymptotically). Asymptotic normality enables hypothesis tests and confidence intervals for MLEs.

## Explainer

Your three prerequisites each contribute something essential here. From **consistency of estimators**, you know θ̂_n → θ in probability as n → ∞ — the MLE converges to the true parameter. From the **central limit theorem (rigorous)**, you know that properly normalized sums of i.i.d. random variables converge in distribution to a normal. From **Fisher information** I(θ), you know it quantifies how much information each observation carries about θ, and that the Cramér-Rao bound says no unbiased estimator can have variance less than 1/(n I(θ)). Asymptotic normality of MLEs ties all three together: not only does the MLE converge, but the normalized deviation √n(θ̂_n − θ) has a specific, computable limiting distribution — N(0, 1/I(θ)).

The proof sketch is a Taylor expansion of the **score function** S(θ) = ∂/∂θ log L(θ; X₁,…,X_n) = Σᵢ ℓ'(θ; Xᵢ). At the MLE θ̂_n, the score is zero by definition. Taylor-expanding around the true θ: Σ ℓ'(θ; Xᵢ) + (θ̂_n − θ) Σ ℓ''(θ; Xᵢ) ≈ 0. Solving for (θ̂_n − θ): it equals −(Σ ℓ'(θ; Xᵢ)) / (Σ ℓ''(θ; Xᵢ)). The numerator, normalized by 1/√n, converges to N(0, I(θ)) by the CLT (since E[ℓ'(θ;X)] = 0 and Var[ℓ'(θ;X)] = I(θ)). The denominator divided by n converges to −I(θ) by the WLLN and the identity E[ℓ''(θ;X)] = −I(θ). After normalization, the ratio converges in distribution to N(0, 1/I(θ)).

The result says the MLE is **asymptotically efficient**: among all consistent, asymptotically normal estimators, it achieves the smallest possible asymptotic variance — exactly the Cramér-Rao bound. This is not a finite-sample claim; small samples can behave poorly. But for large n, no estimator can systematically beat the MLE in variance. The practical payoff is immediate: since √n(θ̂_n − θ) ≈ N(0, 1/I(θ)), an approximate 95% confidence interval for θ is θ̂_n ± 1.96/√(n·Î(θ)), where Î(θ) is Fisher information evaluated at the MLE.

Understanding the regularity conditions that support this result is as important as the result itself. The conditions — differentiability of the log-likelihood, identifiability of θ, finite Fisher information, interchange of differentiation and integration — can fail. When they do, for example with the Uniform(0, θ) model where the MLE is the maximum order statistic, the MLE may converge at a rate different from √n and to a non-normal limit distribution. Asymptotic normality is the generic case, but its exceptions teach you what makes estimation problems genuinely hard.
