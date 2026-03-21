---
id: distribution-of-sample-mean-theory
title: Distribution of the Sample Mean
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: sampling-distributions-theory
  type: hard
builds-toward:
- central-limit-theorem
- confidence-intervals-means
tags:
- sample-mean
stage: formal-systems
status: draft
---

# Distribution of the Sample Mean

## Core Idea
For random sample X₁,...,Xₙ with mean μ and variance σ²: E[X̄]=μ and Var(X̄)=σ²/n. Standard error SE(X̄)=σ/√n. If population is normal, X̄ is exactly normal; otherwise normal holds approximately for large n by CLT.

## Questions

```yaml
- question: "A population has mean μ = 50 and standard deviation σ = 10. A random sample of n = 25 is drawn. What is the standard error of the sample mean?"
  type: multiple-choice
  options:
    - "10 — the standard error equals the population standard deviation"
    - "2 — SE = σ/√n = 10/5"
    - "4 — SE = σ²/n = 100/25"
    - "0.4 — SE = σ/n = 10/25"
  answer: 1
  explanation: "The standard error is SE(X̄) = σ/√n = 10/√25 = 10/5 = 2. Option A confuses SE with σ itself (the point of SE is that averages are less variable than individual observations). Option C confuses Var(X̄) = σ²/n = 4 with the standard error — you must take the square root to get SE. Option D divides σ by n directly, skipping the square root."

- question: "A researcher wants to cut the standard error of their sample mean in half. They currently have n = 100 observations. How many total observations do they need?"
  type: multiple-choice
  options:
    - "150 — adding half again is enough"
    - "200 — doubling the sample size halves the standard error"
    - "400 — SE shrinks as 1/√n, so halving SE requires quadrupling n"
    - "10,000 — SE shrinks as 1/n, so halving SE requires squaring n"
  answer: 2
  explanation: "Because SE = σ/√n, halving SE means √n must double, which requires n to quadruple: from 100 to 400. This is the square root law of diminishing returns. Option B is the most common misconception — doubling n multiplies SE by 1/√2 ≈ 0.71, a reduction of only 29%, not 50%."

- question: "The sample mean X̄ is an unbiased estimator of the population mean μ, meaning E[X̄] = μ for any sample size n."
  type: true-false
  answer: true
  explanation: "Unbiasedness follows directly from linearity of expectation: E[X̄] = E[(X₁ + ··· + Xₙ)/n] = (E[X₁] + ··· + E[Xₙ])/n = nμ/n = μ. This holds regardless of population shape and for any n ≥ 1. Unbiasedness means the sample mean is 'on target' on average — not that any individual sample will equal μ."

- question: "If the population is not normally distributed, the sample mean X̄ cannot be used in statistical inference because its distribution is unknown."
  type: true-false
  answer: false
  explanation: "This is false — the Central Limit Theorem guarantees that for any population with finite mean and variance, the standardized sample mean converges to a standard normal distribution as n grows. In practice, the normal approximation is reliable for n ≥ 30 for moderately skewed populations. Inference doesn't require the population to be normal; it only requires n to be large enough for the CLT to apply."

- question: "Why does the variance of the sample mean decrease as sample size increases, and what does the square root in SE = σ/√n imply about the returns to collecting more data?"
  type: short-answer
  answer: "When you average n independent observations, extreme values in different observations partially cancel each other out. The more observations, the more cancellation, so the average is less variable — specifically, Var(X̄) = σ²/n, shrinking proportionally to 1/n. But standard deviation (the relevant scale measure) is the square root of variance, giving SE = σ/√n. This square root creates diminishing returns: doubling n reduces SE by only a factor of √2 ≈ 1.41, not 2. To halve SE you must quadruple n. Collecting data gets increasingly expensive per unit of precision gained."
  explanation: "The variance formula Var(X̄) = σ²/n follows from the independence of observations and the variance addition rule: Var(X₁ + ··· + Xₙ) = nσ², then dividing by n² gives σ²/n. The square root law is why large observational studies are expensive and why there are practical limits to how precisely we can estimate population parameters from samples."
```

## Explainer

From sampling distributions, you know that a statistic is itself a random variable — it varies across samples. The sample mean X̄ = (X₁ + ··· + Xₙ)/n is a particularly important statistic. What can we say about its distribution? Two properties follow from linearity of expectation and variance, without any assumption about the population shape. First, **E[X̄] = μ**: the expected value of the sample mean equals the population mean. Averaging is unbiased — in the long run, the sample mean is right on target. Second, **Var(X̄) = σ²/n**: the variance of the sample mean is n times smaller than the population variance.

The variance formula is the deeper and more important result. Think about why it makes sense: if you average n independent observations, extreme values in individual observations partially cancel each other out. With more observations, there is more cancellation, so the average is less variable. The formula says the variance shrinks proportionally to 1/n. Since standard deviation is the square root of variance, the **standard error SE(X̄) = σ/√n** shrinks proportionally to 1/√n. To halve the standard error, you need four times as many observations — this square root law explains why collecting data has diminishing returns in reducing estimation uncertainty.

The shape of X̄'s distribution depends on the population. If the population is exactly normal — X_i ~ N(μ, σ²) — then X̄ is exactly normal for any sample size n. This follows because the sum of independent normal random variables is normal, and dividing by n just rescales. In this case, X̄ ~ N(μ, σ²/n) exactly, which is the basis for exact z-tests and t-tests when σ is known. The t-distribution enters when σ must be estimated from the same sample — the extra uncertainty in estimating σ fattens the tails compared to the normal.

When the population is not normal, the exact distribution of X̄ is typically intractable. Here the **Central Limit Theorem** provides the rescue: for any population with finite mean μ and variance σ², the standardized sample mean (X̄ − μ)/(σ/√n) converges in distribution to the standard normal as n → ∞. In practice this approximation is reliable for n ≥ 30 for moderately skewed populations, though heavier-tailed distributions require larger n. The CLT is why the normal distribution appears throughout statistics: even if individual measurements are not normal, averages of many measurements tend to be, and statistics are almost always aggregates of many observations.
