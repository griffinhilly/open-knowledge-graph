---
id: umvue
title: Uniformly Minimum Variance Unbiased Estimation (UMVUE)
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: cramer-rao-lower-bound
  type: hard
- id: sufficient-statistics
  type: hard
builds-toward:
- rao-blackwell-theorem
tags:
- umvue
- unbiased-estimation
- statistics
stage: advanced
status: draft
---

# Uniformly Minimum Variance Unbiased Estimation (UMVUE)

## Core Idea
A UMVUE is an unbiased estimator with minimum variance among all unbiased estimators. By the Cramer-Rao bound, no unbiased estimator can have variance less than 1/I(θ). A necessary condition for a UMVUE is that it's a function of a complete sufficient statistic. UMVUEs need not always exist, and when they do, they are often difficult to find.

## Explainer

From the Cramér-Rao lower bound, you know there is a floor on how small the variance of an unbiased estimator can be: Var(T̂) ≥ 1/I(θ), where I(θ) is the Fisher information. An estimator that achieves this bound is called **efficient** — it extracts every bit of information the data contain about θ, with no waste. The UMVUE asks: even among unbiased estimators that *don't* achieve the Cramér-Rao bound (because the bound is not always tight), which one has the smallest variance? The UMVUE is the winner of that competition.

The concept of a **sufficient statistic** is your other prerequisite here. Recall that T is sufficient for θ if the conditional distribution of the data given T does not depend on θ — T captures all the information in the sample about θ. Now add a refinement: T is **complete** if the only function of T that has zero expectation for all θ is the zero function. Completeness rules out "redundancy" in T — there are no linear combinations of T that are informationally empty. Complete sufficient statistics are rare and special; for exponential family distributions (normal, Poisson, binomial, exponential, etc.), the natural sufficient statistic is always complete.

The key theorem connecting these ideas is the **Lehmann-Scheffé theorem**: if T is a complete sufficient statistic and h(T) is an unbiased estimator of θ, then h(T) is the UMVUE. The proof uses the **Rao-Blackwell theorem** as a component: starting from any unbiased estimator, conditioning on T can only reduce variance. So the best unbiased estimator must be a function of T. Completeness then guarantees uniqueness — there can be only one such function, making it the UMVUE.

In practice, finding a UMVUE involves two steps: identify a complete sufficient statistic (often given by the exponential family structure), then find or construct an unbiased function of it. For a Poisson sample, the complete sufficient statistic is the sum ΣXᵢ, and the sample mean X̄ = ΣXᵢ/n is unbiased for λ, making it the UMVUE of λ. UMVUEs are elegant in theory but have limits: they restrict attention to unbiased estimators, and sometimes a slightly biased estimator with much lower mean squared error (like a ridge or Bayes estimator) is preferable in practice. The UMVUE is the best you can do within the unbiasedness constraint — a theoretically optimal benchmark, though not always the most practically useful one.
