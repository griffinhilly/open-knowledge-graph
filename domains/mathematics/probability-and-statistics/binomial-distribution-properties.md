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
