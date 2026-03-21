---
id: poisson-distribution
title: Poisson Distribution
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: discrete-random-variables
  type: hard
builds-toward:
- sampling-distributions
tags:
- poisson
- rate
- rare-events
stage: formal-systems
status: draft
---

# Poisson Distribution

## Core Idea
The Poisson distribution models the number of events occurring in a fixed interval when events occur at a constant average rate λ and independently. Its PMF is P(X = k) = e^(-λ) × λ^k / k!. Both mean and variance equal λ. The Poisson distribution approximates the binomial distribution when n is large and p is small (so np ≈ λ), and arises naturally as a limit of binomial processes.

## How It's Best Learned
Derive Poisson as a limit of binomial. Model real phenomena (phone calls, website traffic) using Poisson. Compare Poisson and binomial approximations for large n and small p.

## Common Misconceptions
Using Poisson for events in fixed counts rather than fixed intervals/regions. Forgetting that mean and variance are equal. Applying Poisson without the independence assumption.

## Questions

```yaml
- question: "A data scientist models customer support tickets per hour using Poisson(λ = 10). After collecting data, the sample mean is 10 but the sample variance is 35. What does this indicate?"
  type: multiple-choice
  options:
    - "The Poisson model may be inadequate — the data shows overdispersion"
    - "The model is fine; variance slightly exceeding the mean is normal sampling variation"
    - "A larger sample would resolve the discrepancy"
    - "The model is correct; variance should exceed the mean in real data"
  answer: 0
  explanation: "A key property of the Poisson distribution is mean = variance = λ. When observed variance substantially exceeds the mean (35 >> 10), this is overdispersion, which often signals that events are not independent (e.g., one ticket triggers others, or load is bursty). A negative binomial model handles overdispersion better. Option B is wrong — a variance 3.5× the mean is not sampling noise; it indicates systematic departure from Poisson assumptions."

- question: "Which of the following situations best fits a Poisson model?"
  type: multiple-choice
  options:
    - "Number of emails arriving at a server per minute at constant, steady traffic"
    - "Number of heads in 100 coin flips"
    - "Number of students who pass an exam out of 30 enrolled"
    - "Number of goals scored by a team, given they score more often after the first goal"
  answer: 0
  explanation: "Poisson models count events at a constant rate, independently, in a fixed interval. Option A fits: independent arrivals, constant rate, countable events per minute. Options B and C are binomial (fixed n trials, success/failure). Option D violates independence — clustering after the first goal means events are not independent, which would produce overdispersion."

- question: "For a Poisson random variable with parameter λ = 4, the variance equals 2 (the square root of the mean)."
  type: true-false
  answer: false
  explanation: "For any Poisson distribution, variance = λ, not √λ. With λ = 4, the variance is 4. The standard deviation is √λ = 2, but variance and standard deviation are different things. The equal-mean-and-variance property (both = λ) is a diagnostic signature of the Poisson distribution."

- question: "The Poisson distribution arises as a limit of the binomial when n is large and p is small, with λ = np held constant."
  type: true-false
  answer: true
  explanation: "Divide a fixed interval into n tiny sub-intervals, each with probability p = λ/n of an event. The total count follows Binomial(n, p). As n → ∞ with np = λ fixed, this converges to Poisson(λ). This derivation reveals the three Poisson conditions: many independent opportunities, each with small probability, at a fixed average rate."

- question: "What does it mean for count data to be 'overdispersed,' and why does overdispersion suggest the Poisson model is inappropriate?"
  type: short-answer
  answer: "Overdispersion means the sample variance substantially exceeds the sample mean. The Poisson distribution requires variance = mean = λ, which follows from the independence assumption — events don't cluster. When overdispersion occurs, it usually signals dependence: one event makes another more likely (aftershocks, contagious disease cases). Using Poisson anyway underestimates variability, making confidence intervals and predictions too narrow. A negative binomial model is typically used instead, as it adds a parameter allowing variance > mean."
  explanation: "The mean = variance property is not just a curiosity — it is a testable model assumption. Checking sample mean ≈ sample variance is a quick diagnostic for whether Poisson applies. Overdispersion (variance >> mean) is extremely common in real count data, which is why negative binomial models appear so frequently in practice."
```

## Explainer

The Poisson distribution's origin is a limit of the binomial. Suppose you split a fixed time interval into n very short sub-intervals, each so short that at most one event can occur in it, with probability p = λ/n. As n → ∞ with λ = np held fixed, the binomial PMF converges to P(X = k) = e^(-λ) λ^k / k!. This derivation reveals exactly when Poisson applies: "large number of opportunities, each with small individual probability, independent." Phone calls per hour, typos per page, radioactive decays per second — all fit this description. The parameter λ is both the rate and the expected count over the interval.

The equal-mean-and-variance property is a diagnostic signature, not just a curiosity. When you fit count data to a Poisson model, checking whether the sample mean ≈ sample variance is a quick model adequacy test. If the variance substantially exceeds the mean — a pattern called **overdispersion** — the Poisson model is inadequate, often because events cluster (a car accident makes another more likely, not less). Overdispersed count data frequently requires a **negative binomial model** instead. Conversely, underdispersion suggests that events regulate each other.

The PMF P(X = k) = e^(-λ) λ^k / k! has a memorable structure once you see why it sums to 1: the sum over all k of λ^k / k! is exactly e^λ, so the e^(-λ) factor is precisely the normalizing constant. As k increases from 0, probabilities first rise (λ^k grows faster than k! for small k) then fall (k! dominates for large k). The mode is at ⌊λ⌋. For small λ (rare events), the distribution is sharply right-skewed — the most likely outcome is zero. For large λ, by the central limit theorem, Poisson(λ) is well approximated by Normal(λ, λ), and tables or normal calculations can substitute.

Applying Poisson correctly requires checking three conditions: events occur at a **constant average rate** λ, they are **independent** (past events don't affect future ones), and **simultaneous events** are impossible (probability of two events in an infinitesimal interval is negligible). These are violated more often than beginners realize. Earthquakes trigger aftershocks (dependence). Website traffic spikes at lunch hour (non-constant rate). When these assumptions fail but you use Poisson anyway, your variance estimate will be wrong and any confidence intervals or predictions based on it will be misleading.
