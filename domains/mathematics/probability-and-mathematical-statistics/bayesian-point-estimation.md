---
id: bayesian-point-estimation
title: Bayesian Point Estimation
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
- id: conjugate-priors
  type: soft
- id: bayesian-inference-foundations
  type: hard
builds-toward:
- martingales-introduction
tags:
- bayesian-estimation
- point-estimation
- statistics
stage: advanced
status: draft
---

# Bayesian Point Estimation

## Core Idea
Common Bayesian point estimators are the posterior mean (minimizes squared error loss), posterior median (minimizes absolute error loss), and posterior mode (maximizes posterior). The choice depends on the loss function. Bayesian estimators naturally incorporate prior information and adapt to the posterior distribution.

## Explainer

From Bayesian inference foundations, you know that after observing data, your beliefs about a parameter θ are encoded in the **posterior distribution** p(θ | data) — a full probability distribution, not a single number. But often you need to report one number: a single best guess for θ. Bayesian point estimation is the principled process of collapsing the posterior into that single summary, and the key insight is that the "best" collapse depends on what kind of errors you most want to avoid.

The framework starts with a **loss function** L(θ̂, θ), which measures the cost of reporting estimate θ̂ when the true value is θ. The optimal Bayesian estimate minimizes the expected loss under the posterior. For squared error loss L = (θ̂ − θ)², the minimizer is the **posterior mean** E[θ | data]. For absolute error loss L = |θ̂ − θ|, the minimizer is the **posterior median**. For 0-1 loss (you lose 1 for any wrong answer, 0 for the exact right answer), the minimizer is the **posterior mode**, also called the **MAP estimate** (Maximum A Posteriori). Each estimator is optimal for a different cost structure.

To build intuition, consider a posterior that is a skewed distribution — say, an income distribution with a long right tail. The posterior mean is pulled right by the tail; the posterior median is not; the MAP (mode) is the most common value, possibly even lower. If overestimating is very costly, you'd prefer the median or even a quantile below 0.5. If you just want the single most likely value quickly, MAP is natural. The choice of estimator encodes an assumption about what "close enough" means — and making that assumption explicit is a strength of the Bayesian approach.

With **conjugate priors**, these point estimates often have closed forms that reveal how prior and data combine. For a Beta(α, β) prior on a binomial proportion p with n trials and k successes, the posterior is Beta(α + k, β + n − k). The posterior mean is (α + k) / (α + β + n) — a weighted average of the prior mean α/(α+β) and the data proportion k/n. As n grows large, the data proportion dominates and the prior fades. The MAP estimate is (α + k − 1) / (α + β + n − 2), slightly different for small samples. This concretely shows how Bayesian point estimation adapts: with little data, the prior matters; with lots of data, the estimate converges to the frequentist MLE.
