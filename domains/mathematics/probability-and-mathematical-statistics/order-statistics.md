---
id: order-statistics
title: Order Statistics
domain: mathematics
course: probability-and-mathematical-statistics
prerequisites:
  - id: cumulative-distribution-function
    type: hard
  - id: probability-density-functions
    type: hard
  - id: binomial-distribution
    type: soft
  - id: transformations-of-random-variables
    type: soft
builds-toward: []
tags: [probability, statistics, order-statistics, minimum, maximum, sample-median, beta-distribution]
stage: advanced
status: validated
---

# Order Statistics

## Core Idea
Sorting a random sample X₁, ..., Xₙ from smallest to largest gives the order statistics X₍₁₎ ≤ X₍₂₎ ≤ ... ≤ X₍ₙ₎. The minimum, maximum, median and range are all order statistics or functions of them. For an independent sample from a continuous distribution with CDF F and density f, the maximum has CDF F(x)ⁿ, the minimum has CDF 1 - (1 - F(x))ⁿ, and the k-th order statistic has density n!/((k - 1)!(n - k)!) · F(x)^(k-1) · (1 - F(x))^(n-k) · f(x). These formulas underlie estimators based on extremes and the distribution of the sample median.

## How It's Best Learned
Derive the maximum's CDF first from the observation that the maximum is at most x exactly when every observation is at most x. Then derive the minimum by the complementary event. For the general k-th order statistic, count how many observations fall below, at, and above x, which turns the density into a multinomial counting argument. Check the formulas with a uniform sample, where the k-th order statistic has a beta distribution.

## Common Misconceptions
- The order statistics of an independent sample are themselves independent. (They are dependent; for example X₍₁₎ ≤ X₍₂₎ always, so knowing one restricts the other.)
- The maximum of n observations has the same distribution as a single observation. (Its CDF F(x)ⁿ is pushed to the right; for n uniform(0, 1) observations its mean is n/(n + 1), not 1/2.)
- The CDF of the minimum is F(x)ⁿ. (That is the maximum; the minimum exceeds x only when every observation does, so its CDF is 1 - (1 - F(x))ⁿ.)

## Questions

```yaml
- question: "X₁, ..., X₅ are independent and uniform on (0, 1). What is P(max Xᵢ ≤ 0.8)?"
  type: multiple-choice
  options: ["0.8", "0.8⁵ ≈ 0.328", "1 - 0.2⁵ ≈ 0.9997", "5 × 0.8 = 4"]
  answer: 1
  explanation: "The maximum is at most 0.8 exactly when all five values are at most 0.8. By independence the probability is 0.8⁵ ≈ 0.328. The expression 1 - 0.2⁵ is the probability that the minimum is at most 0.8."

- question: "The minimum of n independent exponential random variables, each with rate λ, is exponential with rate nλ."
  type: true-false
  answer: true
  explanation: "P(min > x) = P(all Xᵢ > x) = (e^(-λx))ⁿ = e^(-nλx). That is the survival function of an exponential distribution with rate nλ. For example, the first of n independent components to fail does so at rate nλ."

- question: "For an independent uniform(0, 1) sample of size n, what is the expected value of the k-th order statistic?"
  type: short-answer
  answer: "k/(n + 1)"
  explanation: "X₍ₖ₎ has a Beta(k, n - k + 1) distribution, whose mean is k/(k + (n - k + 1)) = k/(n + 1). The n points split (0, 1) into n + 1 gaps that have equal expected length 1/(n + 1)."

- question: "Explain where the factor n!/((k - 1)!(n - k)!) in the density of X₍ₖ₎ comes from."
  type: short-answer
  answer: "It counts the ways to choose which k - 1 observations fall below x, which one falls at x, and which n - k fall above x."
  explanation: "For X₍ₖ₎ to be near x, exactly k - 1 values lie below x (probability F(x) each), one lies in a small interval at x (probability about f(x)dx), and n - k lie above (probability 1 - F(x) each). The number of ways to assign the n observations to these three groups is the multinomial coefficient n!/((k - 1)! 1! (n - k)!)."
```

## Explainer

Many questions about a sample concern its extremes or its middle rather than its average. How tall is the tallest of 30 students? How long until the first of 10 light bulbs burns out? What is the typical value of a sample median? The order statistics answer these. Sort the sample X₁, ..., Xₙ to get X₍₁₎ ≤ ... ≤ X₍ₙ₎. Then X₍₁₎ is the minimum, X₍ₙ₎ is the maximum, and the median is the middle value.

Throughout, assume the Xᵢ are independent with common CDF F and density f. Start with the maximum. The event {X₍ₙ₎ ≤ x} happens exactly when every Xᵢ ≤ x. By independence,

P(X₍ₙ₎ ≤ x) = F(x)ⁿ.

Differentiating gives the density nF(x)^(n-1) f(x). The minimum works through the complement: X₍₁₎ > x exactly when every Xᵢ > x, so P(X₍₁₎ ≤ x) = 1 - (1 - F(x))ⁿ.

A quick application: if n components have independent exponential lifetimes with rate λ, the first failure time satisfies P(X₍₁₎ > x) = e^(-nλx). So the minimum is exponential with rate nλ, and the expected time to first failure is 1/(nλ).

For the general k-th order statistic, count. For X₍ₖ₎ to lie in a tiny interval at x, exactly k - 1 observations must fall below x, one must fall in the interval, and n - k must fall above. Each has probability F(x), f(x)dx and 1 - F(x), and the number of ways to pick which observations play which role is n!/((k - 1)!(n - k)!). This gives

f₍ₖ₎(x) = n!/((k - 1)!(n - k)!) · F(x)^(k-1) · (1 - F(x))^(n-k) · f(x).

For a uniform(0, 1) sample, F(x) = x, and this is the Beta(k, n - k + 1) density. Its mean is k/(n + 1). So the expected maximum of n uniforms is n/(n + 1), and the expected minimum is 1/(n + 1). The n sorted points tend to split the interval into n + 1 pieces of equal expected length.

Order statistics appear throughout statistics. For a uniform(0, θ) sample, the maximum likelihood estimate of θ is X₍ₙ₎, and its distribution gives an exact confidence interval. Sample quantiles, the median, the range X₍ₙ₎ - X₍₁₎, and rank-based nonparametric tests are all built from order statistics. Remember that the order statistics are dependent, even though the original observations are independent.
