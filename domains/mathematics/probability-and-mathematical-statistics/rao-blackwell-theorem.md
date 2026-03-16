---
id: rao-blackwell-theorem
title: Rao-Blackwell Theorem
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: umvue
  type: soft
- id: conditional-expectation
  type: hard
- id: sufficient-statistics
  type: hard
builds-toward:
- bayesian-point-estimation
tags:
- rao-blackwell
- unbiased-estimation
- statistics
stage: advanced
status: draft
---

# Rao-Blackwell Theorem

## Core Idea
If T is an unbiased estimator of θ and S is a sufficient statistic, then φ = E[T|S] is unbiased for θ and Var(φ) ≤ Var(T). This theorem shows how to improve unbiased estimators by conditioning on sufficient statistics. Combined with completeness, it yields UMVUEs.

## Explainer

You've studied **sufficient statistics** — statistics S(X) that capture all the information in the data about the parameter θ, in the sense that the conditional distribution of the data given S does not depend on θ. You've also studied **conditional expectation** — E[T|S], the expected value of T after averaging over everything not captured by S. The Rao-Blackwell theorem puts these together: if you start with any unbiased estimator T and condition it on a sufficient statistic S, you get a new estimator that is at least as good, and often better.

The construction is this: define φ(S) = E[T|S]. Three properties follow immediately. First, **unbiasedness is preserved**: E[φ(S)] = E[E[T|S]] = E[T] = θ by the law of total expectation. Second, **φ depends only on S**: since S is sufficient, conditioning on S yields a distribution free of θ, so the conditional expectation is a well-defined function of S alone. Third, **variance cannot increase**: by the variance decomposition formula, Var(T) = Var(E[T|S]) + E[Var(T|S)] = Var(φ) + E[Var(T|S)] ≥ Var(φ). The extra term E[Var(T|S)] is the "noise" in T that is unrelated to θ — conditioning removes it.

The intuition is that any unbiased estimator T contains two kinds of variability: fluctuations that carry information about θ (good variance) and fluctuations that are irrelevant noise (bad variance). The sufficient statistic S has already extracted all the information. Conditioning T on S averages away the irrelevant noise while preserving the signal, producing an estimator with the same mean but lower variance. A simple example: suppose you want to estimate the mean of a normal population, and T is just the first observation X₁ — unbiased but high-variance. The sufficient statistic for this model is the sample mean X̄. Then E[X₁ | X̄] = X̄, and the Rao-Blackwellized estimator is the sample mean itself, which has variance σ²/n instead of σ².

Combined with **completeness** of the sufficient statistic, the theorem yields the UMVUE (Uniformly Minimum Variance Unbiased Estimator) via the Lehmann-Scheffé theorem: if a complete sufficient statistic S exists and you condition any unbiased estimator on S, the result is the unique UMVUE — no unbiased estimator can have smaller variance for any value of θ. The Rao-Blackwell theorem is the engine: start with any unbiased estimator (easy to find), condition on the sufficient statistic (always improves or maintains variance), and completeness guarantees the result is optimal.
