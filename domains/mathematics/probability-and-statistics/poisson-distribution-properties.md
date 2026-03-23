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
status: validated
---

# Poisson Distribution: Rare Events and Applications

## Core Idea
Poisson(λ): counts of rare events in fixed time/space. PMF: P(X=k)=e^{−λ}λ^k/k!. E[X]=λ, Var(X)=λ. Limit of binomial as n→∞, p→0 with np=λ constant. Models events like defects, arrivals, and accidents.

## Questions

```yaml
- question: "A quality inspector counts defects per item on an assembly line. The sample mean is 2.1 defects and the sample variance is 8.7 defects². Which statement is most appropriate?"
  type: multiple-choice
  options:
    - "The data fits a Poisson distribution since 2.1 is close to a whole number"
    - "The data shows overdispersion — variance far exceeds the mean, which violates the Poisson assumption that E[X] = Var(X) = λ"
    - "The data fits a Poisson with λ = 8.7 since variance determines λ"
    - "The data fits a Poisson with λ = 2.1; variance is irrelevant for fitting"
  answer: 1
  explanation: "The Poisson distribution's defining property is E[X] = Var(X) = λ. Here mean = 2.1 but variance = 8.7 (about 4× larger). This is overdispersion — the variance is much larger than the mean, inconsistent with a Poisson model. A negative binomial distribution is typically more appropriate for overdispersed count data. The sample mean and variance being approximately equal is what would justify a Poisson model."

- question: "A Poisson random variable X has parameter λ = 6. What is Var(X)?"
  type: multiple-choice
  options:
    - "36, because Var(X) = λ²"
    - "√6, because the standard deviation equals √λ"
    - "6, because Var(X) = λ for any Poisson random variable"
    - "Cannot be determined without the full probability mass function"
  answer: 2
  explanation: "The Poisson distribution has the unique property that its variance equals its mean: Var(X) = E[X] = λ. So Var(X) = 6, not λ² = 36 or √6. This equality — not a squared or square-root relationship — is the fingerprint of the Poisson. A common error is confusing this with the normal distribution where mean and variance are independent parameters."

- question: "If calls arrive at a Poisson rate of 8 per hour, then over a 4-hour period the expected number of calls is 32 and the variance is also 32."
  type: true-false
  answer: true
  explanation: "The Poisson parameter scales linearly with time: over t hours, the count follows Poisson(λt). So 8 calls/hour over 4 hours gives Poisson(32), with both mean and variance equal to 32. This additivity — Poisson(λ₁) + Poisson(λ₂) = Poisson(λ₁ + λ₂) for independent variables — is one of the distribution's key practical properties."

- question: "A count dataset where the sample variance is much larger than the sample mean suggests a Poisson distribution is an appropriate model."
  type: true-false
  answer: false
  explanation: "Poisson requires E[X] = Var(X) = λ. A variance much larger than the mean indicates overdispersion, which violates the Poisson assumption. This is a signal to consider a negative binomial model instead. The Poisson is appropriate when mean and variance are approximately equal — that equality is the diagnostic test for Poisson suitability."

- question: "Why is the equality E[X] = Var(X) = λ useful in practice, not just theoretically interesting?"
  type: short-answer
  answer: "It provides a practical diagnostic test for model fit. If you have count data, comparing the sample mean and sample variance tells you whether a Poisson model is plausible before fitting anything. If the variance is much larger than the mean (overdispersion), the Poisson assumption is violated and a different model is needed. If they're roughly equal, Poisson is a reasonable candidate. This single check can save the effort of fitting and diagnosing a misspecified model."
  explanation: "The equality is both a defining property and a practical screening tool. Because both parameters are determined by a single λ, the Poisson makes a strong prediction that can be falsified by simple descriptive statistics."
```

## Explainer

The Poisson distribution models the count of rare, independent events occurring in a fixed interval of time or space. Think of it as the natural distribution for "how many times did something happen in an hour?" when each event is unlikely but there are many opportunities for it to occur. Classic examples: the number of calls arriving at a call center per minute, the number of typos on a page, or the number of radioactive decays per second. What makes Poisson special is that a single parameter **λ** (lambda) — the average rate — determines everything about the distribution.

If you've studied the binomial distribution, you can derive the Poisson distribution from it. Suppose you have n independent trials, each with probability p of success. As n → ∞ and p → 0 while keeping np = λ constant (many chances, each very unlikely), the binomial PMF converges to P(X = k) = e^{−λ}λ^k / k!. This limiting argument explains why the Poisson naturally arises when counting rare events: you are in the regime where n is large and p is small, which is exactly the "rare event" scenario.

The most striking property of the Poisson distribution is that its mean and variance are both equal to λ. This equality — E[X] = Var(X) = λ — is a unique fingerprint of the Poisson. In practice, if you observe count data and find that the sample mean and variance are roughly equal, that is evidence the process might be Poisson. If the variance is much larger than the mean (**overdispersion**), a negative binomial model may be more appropriate. If the variance is much smaller (**underdispersion**), the Poisson is likely a poor fit.

The parameter λ also scales naturally: if events occur at a Poisson rate λ per hour, then over t hours they follow Poisson(λt). This **additivity** property — if X ~ Poisson(λ₁) and Y ~ Poisson(λ₂) are independent, then X + Y ~ Poisson(λ₁ + λ₂) — makes the Poisson particularly tractable for modeling processes that combine multiple independent sources of rare events, such as total defects from several independent production lines.
