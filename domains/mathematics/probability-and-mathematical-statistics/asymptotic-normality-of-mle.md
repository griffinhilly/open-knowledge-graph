---
id: asymptotic-normality-of-mle
title: Asymptotic Normality of the MLE
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: maximum-likelihood-estimation-theory
  type: hard
- id: central-limit-theorem-rigorous
  type: hard
- id: fisher-information
  type: soft
builds-toward:
- confidence-intervals-rigorous
tags:
- mle
- asymptotics
- normal-approximation
stage: advanced
status: draft
---

# Asymptotic Normality of the MLE

## Core Idea
Under regularity conditions, √n(θ̂_n - θ) converges in distribution to N(0, I(θ)^{-1}), so θ̂_n ≈ N(θ, I(θ)^{-1}/n) for large n. The convergence rate is √n and the asymptotic variance achieves the Cramér-Rao lower bound (asymptotic efficiency). This enables construction of confidence intervals and hypothesis tests.

## Explainer

From the **Central Limit Theorem** (rigorous version), you know that the sample mean of i.i.d. random variables, properly scaled, converges to a normal distribution. The asymptotic normality of the MLE is the same phenomenon applied not to a simple average but to the maximizer of the log-likelihood. The result says: as the sample size n grows, the MLE θ̂_n behaves approximately like a normal random variable centered at the true parameter θ, with variance shrinking at rate 1/n. More precisely, the scaled deviation √n(θ̂_n − θ) converges in distribution to N(0, I(θ)⁻¹), where I(θ) is the **Fisher information** at the true parameter.

The proof sketch connects your prerequisites. The score function ∂log L/∂θ equals zero at the MLE (it is the first-order condition). Taylor-expanding the score around the true θ and rearranging gives: √n(θ̂_n − θ) ≈ [−(1/n)∂²log L/∂θ²]⁻¹ · [(1/√n)∂log L/∂θ]. The numerator — the scaled score — is a sum of i.i.d. terms with mean zero and variance I(θ), so by the CLT it converges to N(0, I(θ)). The denominator — the scaled observed Fisher information — converges to I(θ) by the law of large numbers. The ratio converges to N(0, I(θ)⁻¹). This argument is heuristic; the rigorous version requires regularity conditions (twice-differentiable log-likelihood, compact parameter space, identifiability) to justify the interchange of limit and differentiation.

The **Fisher information** I(θ) = E[(∂log f(X;θ)/∂θ)²] is the variance of the score — it measures how sensitively the log-likelihood changes as θ moves. High Fisher information means the data is very informative about θ, so the MLE can pin down θ precisely: the asymptotic variance I(θ)⁻¹ is small. Low Fisher information means the data carries little signal about θ, and the MLE's variance is large. This is not accidental — the **Cramér-Rao lower bound** says no unbiased estimator can have variance below I(θ)⁻¹/n. The MLE achieves this lower bound asymptotically, making it **asymptotically efficient**: in the large-sample limit, no competing estimator can have smaller variance.

This result is the workhorse of frequentist inference. Because θ̂_n ≈ N(θ, I(θ̂_n)⁻¹/n) for large n, you can construct approximate **confidence intervals**: θ̂_n ± z_{α/2} / √(n · I(θ̂_n)). You can test hypotheses using Wald statistics: n(θ̂_n − θ₀)² · I(θ̂_n) ≈ χ²(1) under H₀: θ = θ₀. The entire architecture of large-sample likelihood inference rests on this one asymptotic distribution result — it converts the MLE from a point estimate into a gateway to intervals and tests.
