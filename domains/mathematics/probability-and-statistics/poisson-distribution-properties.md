---
id: poisson-distribution-properties
title: 'Poisson Distribution: Rare Events and Applications'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: poisson-distribution
  type: soft
builds-toward:
- chi-square-distribution-theory
tags:
- poisson
- rare-events
stage: formal-systems
status: draft
---

# Poisson Distribution: Rare Events and Applications

## Core Idea
Poisson(λ): counts of rare events in fixed time/space. PMF: P(X=k)=e^{−λ}λ^k/k!. E[X]=λ, Var(X)=λ. Limit of binomial as n→∞, p→0 with np=λ constant. Models events like defects, arrivals, and accidents.

## Explainer

The Poisson distribution models the count of rare, independent events occurring in a fixed interval of time or space. Think of it as the natural distribution for "how many times did something happen in an hour?" when each event is unlikely but there are many opportunities for it to occur. Classic examples: the number of calls arriving at a call center per minute, the number of typos on a page, or the number of radioactive decays per second. What makes Poisson special is that a single parameter **λ** (lambda) — the average rate — determines everything about the distribution.

If you've studied the binomial distribution, you can derive the Poisson distribution from it. Suppose you have n independent trials, each with probability p of success. As n → ∞ and p → 0 while keeping np = λ constant (many chances, each very unlikely), the binomial PMF converges to P(X = k) = e^{−λ}λ^k / k!. This limiting argument explains why the Poisson naturally arises when counting rare events: you are in the regime where n is large and p is small, which is exactly the "rare event" scenario.

The most striking property of the Poisson distribution is that its mean and variance are both equal to λ. This equality — E[X] = Var(X) = λ — is a unique fingerprint of the Poisson. In practice, if you observe count data and find that the sample mean and variance are roughly equal, that is evidence the process might be Poisson. If the variance is much larger than the mean (**overdispersion**), a negative binomial model may be more appropriate. If the variance is much smaller (**underdispersion**), the Poisson is likely a poor fit.

The parameter λ also scales naturally: if events occur at a Poisson rate λ per hour, then over t hours they follow Poisson(λt). This **additivity** property — if X ~ Poisson(λ₁) and Y ~ Poisson(λ₂) are independent, then X + Y ~ Poisson(λ₁ + λ₂) — makes the Poisson particularly tractable for modeling processes that combine multiple independent sources of rare events, such as total defects from several independent production lines.
