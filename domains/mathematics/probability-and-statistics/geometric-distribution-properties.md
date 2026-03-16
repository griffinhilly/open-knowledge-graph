---
id: geometric-distribution-properties
title: 'Geometric Distribution: Waiting Times'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: geometric-distribution
  type: soft
builds-toward:
- exponential-distribution-theory
tags:
- geometric
- waiting-time
stage: formal-systems
status: draft
---

# Geometric Distribution: Waiting Times

## Core Idea
Geometric(p): number of trials until first success with probability p. PMF: P(X=k)=(1−p)^{k-1}p. E[X]=1/p, Var(X)=(1−p)/p². Only discrete distribution with memoryless property: P(X>n+m|X>n)=P(X>m).

## Explainer

The geometric distribution models the simplest waiting time scenario: you repeatedly perform independent Bernoulli trials (each succeeds with probability p), and X counts how many trials you need until the first success. From your study of the **geometric distribution** basics, you know the PMF is P(X = k) = (1 − p)^{k−1} · p. The factor (1 − p)^{k−1} is the probability of failing k − 1 times in a row; the final factor p is the probability of succeeding on trial k. The trials are independent, so these multiply.

The mean E[X] = 1/p has a clean intuition: if each trial succeeds with probability p, you need on average 1/p trials. With p = 0.1 (a 10% success rate), expect 10 trials. With p = 0.5, expect 2. This can be derived by summing the series Σ k(1−p)^{k−1}p from k = 1 to ∞, or more elegantly by a first-step argument: on the first trial, you either succeed (probability p) or fail and restart (probability 1−p), giving E[X] = p · 1 + (1−p)(1 + E[X]), which solves to E[X] = 1/p. The variance Var(X) = (1−p)/p² captures how spread out the waiting time is — when p is small, waits are long and highly variable.

The **memoryless property** is the geometric distribution's most important characteristic, and the only discrete distribution that has it. It states: P(X > n + m | X > n) = P(X > m). In plain language: if you have already waited n trials without success, the conditional distribution of additional waiting time is exactly the same as the original distribution — as if the n failed trials never happened. Each trial truly starts fresh. A concrete example: you're rolling a die waiting for a six (p = 1/6). After rolling 20 times without a six, your expected additional wait is still 6 more rolls — not 6 minus 20. Past failures give you no information about future trials when each trial is independent.

The memoryless property is what connects the geometric distribution to its continuous analog: the **exponential distribution** builds exactly on this concept, replacing discrete trial counts with continuous time. Just as Geometric(p) is the only memoryless discrete distribution, Exponential(λ) is the only memoryless continuous distribution. The exponential distribution is the continuous limit of the geometric as p → 0 and the number of trials per unit time grows, with λ = p · (trials per unit time) held constant. Understanding the geometric distribution's waiting-time interpretation and memoryless property is therefore the discrete foundation for all of continuous-time probability theory.
