---
id: confidence-intervals-rigorous
title: Confidence Intervals (Rigorous Theory)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: asymptotic-normality-of-mle
  type: hard
builds-toward:
- bayesian-inference-foundations
tags:
- confidence-intervals
- coverage
- inversion
stage: advanced
status: draft
---

# Confidence Intervals (Rigorous Theory)

## Core Idea
A confidence interval [L(X), U(X)] has level 1-α if P(θ ∈ [L,U]) = 1-α for all θ (exact) or approximately (asymptotic). Intervals are constructed by inverting hypothesis tests or using pivotal quantities. Asymptotic CIs rely on the CLT and estimator asymptotics. Confidence is frequentist; different from Bayesian credible intervals.

## Explainer

From the asymptotic normality of the MLE, you know that under regularity conditions √n(θ̂ - θ) →_d N(0, I(θ)^{-1}), where I(θ) is the Fisher information. This gives the building block for interval estimation: an approximate normal pivot. A **confidence interval** [L(X), U(X)] is not a fixed interval with a probability attached to it — it is a random interval, a function of the data X, defined so that the probability of covering the true θ meets a specified level.

The formal definition makes the frequentist interpretation precise. We say [L(X), U(X)] has **coverage probability** 1-α if P_θ(θ ∈ [L(X), U(X)]) = 1-α for all θ in the parameter space. The subscript θ means: we are computing probability over the distribution of X when θ is the true parameter. In repeated sampling — draw a new dataset, compute a new interval, repeat — exactly 100(1-α)% of those intervals contain the true θ. No single computed interval carries a probability: once data is observed, L and U are fixed numbers and θ is a fixed (unknown) number. Either θ is in [L, U] or it is not. The 1-α confidence level describes the procedure's long-run performance, not any individual interval's uncertainty.

There are two standard constructions. The **pivotal quantity** approach finds a function Q(X, θ) whose distribution does not depend on θ, then inverts its probability statement into an interval. For example, if Q = (X̄ - μ)/(s/√n) ~ t_{n-1}, then P(-t_{α/2} ≤ Q ≤ t_{α/2}) = 1-α rearranges to P(X̄ - t_{α/2}·s/√n ≤ μ ≤ X̄ + t_{α/2}·s/√n) = 1-α. The **test inversion** approach is equivalent in theory: the 1-α confidence set for θ is exactly the set of parameter values θ₀ that would not be rejected by a level-α test at the observed data. These two constructions produce the same intervals and illuminate their connection to hypothesis testing.

The Bayesian **credible interval** looks superficially similar but is philosophically distinct. It treats θ as a random variable with a prior distribution, and gives P(θ ∈ interval | data) = 1-α using the posterior distribution. A 95% credible interval means exactly what naive intuition expects — 95% posterior probability — while a 95% confidence interval means long-run coverage. In practice the intervals often have similar numerical endpoints, especially in large samples or with diffuse priors. But they answer different questions: the frequentist confidence interval makes a claim about the procedure; the Bayesian credible interval makes a claim about the current posterior state of belief.
