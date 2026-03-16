---
id: binomial-distribution-properties
title: 'Binomial Distribution: Properties and Applications'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: binomial-distribution
  type: soft
- id: independence-of-events
  type: hard
builds-toward:
- normal-distribution-approximation
- hypothesis-testing-fundamentals
tags:
- binomial
stage: formal-systems
status: draft
---

# Binomial Distribution: Properties and Applications

## Core Idea
Binomial B(n,p): the number of successes in n independent trials with success probability p. PMF: P(X=k)=C(n,k)p^k(1−p)^{n-k}. E[X]=np, Var(X)=np(1−p). Used for count data and proportions; approximated by normal for large np and n(1−p).

## Explainer

You already know the binomial distribution describes counting successes in independent trials. Now the goal is to build genuine intuition for *why* the mean and variance take their specific forms, and when the binomial distribution can be approximated by other distributions — intuition that will serve you in hypothesis testing and beyond.

The **mean** E[X] = np has a beautifully simple justification through your knowledge of independence of events. Each trial is a Bernoulli random variable Bᵢ with mean p. Since X = B₁ + B₂ + ... + Bₙ and the expected value of a sum is the sum of expected values (linearity of expectation holds regardless of dependence), E[X] = E[B₁] + ... + E[Bₙ] = np. No special tricks needed. The **variance** Var(X) = np(1−p) follows from the same decomposition: because the trials are independent, the variance of their sum equals the sum of their variances, and each Bernoulli trial has variance p(1−p). So Var(X) = np(1−p).

The shape of the binomial distribution changes dramatically with p. When p = 0.5, the distribution is perfectly symmetric. When p is close to 0, the distribution is strongly right-skewed — most of the probability sits near 0, with a long right tail. When p is close to 1, it's left-skewed. The **spread** np(1−p) is maximized at p = 0.5 and shrinks toward zero as p approaches 0 or 1 — which makes intuitive sense, since near-certain or near-impossible events leave little room for variability. The product np(1−p) is the binomial's signature: it appears in confidence interval formulas, standard error formulas for proportions, and power calculations, so recognizing it is a frequently useful skill.

The normal approximation works well when both np and n(1−p) are large (a common rule of thumb is both ≥ 10). The reasoning is the **Central Limit Theorem**: X is a sum of n independent, identically distributed Bernoulli trials, and the CLT says that such sums become approximately normal as n grows. The approximation breaks down when p is very small and n is moderate — in that regime, the **Poisson distribution** (with λ = np) is a better approximation. These two limiting cases — normal for balanced, large-n situations; Poisson for rare events — divide most binomial applications in practice, and knowing which approximation applies is as important as knowing the exact formula.
