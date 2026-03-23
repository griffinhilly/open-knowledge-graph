---
id: normal-distribution-theory
title: 'Normal Distribution: Properties and Fundamentals'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: probability-density-functions-theory
  type: hard
builds-toward:
- standard-normal-and-z-scores
- central-limit-theorem
tags:
- normal
- gaussian
stage: formal-systems
status: validated
---

# Normal Distribution: Properties and Fundamentals

## Core Idea
Normal(μ,σ²): PDF f(x)=(1/(σ√(2π)))exp(−(x−μ)²/(2σ²)). Symmetric and bell-shaped. E[X]=μ, Var(X)=σ². Central limit theorem makes it ubiquitous. Linear combinations of independent normals are normal.

## Questions

```yaml
- question: "X ~ Normal(0, 9) and Y ~ Normal(0, 16) are independent. What is the distribution of X + Y?"
  type: multiple-choice
  options:
    - "Normal(0, 25) — variances add: 9 + 16 = 25"
    - "Normal(0, 49) — standard deviations add: σ_X = 3, σ_Y = 4, so σ = 7 and σ² = 49"
    - "Normal(0, 5) — the sum has standard deviation equal to the larger minus the smaller"
    - "The sum is not normally distributed — only the original variables are normal"
  answer: 0
  explanation: "For independent normal random variables, variances add: Var(X + Y) = 9 + 16 = 25. So X + Y ~ Normal(0, 25), with σ = 5. The tempting error is adding standard deviations: σ_X = 3, σ_Y = 4, giving σ = 7 — but standard deviations do NOT add. Variances do. This is a critical practical distinction: if you model two independent error sources as Normal(0, σ₁²) and Normal(0, σ₂²), the combined error has variance σ₁² + σ₂², not standard deviation σ₁ + σ₂."

- question: "Why does the normal distribution appear so frequently in natural measurements like human heights, measurement errors, and test scores?"
  type: multiple-choice
  options:
    - "Because nature produces symmetric distributions, and symmetry implies normality"
    - "Because statisticians prefer the normal distribution and routinely fit it to data regardless of its actual shape"
    - "Because measurements that arise as the sum of many small independent contributions inevitably approach the normal distribution"
    - "Because the normal distribution is the simplest possible continuous distribution and serves as the default assumption"
  answer: 2
  explanation: "This is the content of the Central Limit Theorem, which you'll prove formally in a subsequent topic. Human height is determined by hundreds of genetic and environmental factors; measurement error is the sum of many small instrument and observer variations; test scores aggregate many individual question performances. In each case, the measured quantity is a sum of many independent contributions. The CLT guarantees convergence to normality regardless of the shape of each individual contribution — which is why the normal appears everywhere additive processes operate."

- question: "Any normal random variable X ~ Normal(μ, σ²) can be converted to a standard normal Z ~ Normal(0, 1) by the transformation Z = (X − μ)/σ."
  type: true-false
  answer: true
  explanation: "Subtracting μ shifts the distribution so its mean is 0; dividing by σ scales it so its standard deviation is 1. This standardization works for any normal, which is why probability tables and software only need to tabulate one distribution — the standard normal. Every probability calculation about any normal distribution reduces to a computation about Z ~ Normal(0, 1)."

- question: "If X ~ Normal(μ₁, σ₁²) and Y ~ Normal(μ₂, σ₂²) are independent, then the standard deviation of X + Y equals σ₁ + σ₂."
  type: true-false
  answer: false
  explanation: "The variance of X + Y equals σ₁² + σ₂² — variances add, not standard deviations. The standard deviation of X + Y is therefore √(σ₁² + σ₂²), not σ₁ + σ₂. These are equal only if one standard deviation is 0. This distinction matters whenever you're aggregating independent sources of uncertainty: adding σ overestimates the combined spread."

- question: "Explain why the closure property of the normal distribution under linear combinations requires variances — not standard deviations — to add. Why does this distinction matter in practice?"
  type: short-answer
  answer: "Variance is the quantity that adds for independent random variables because of how expectation operates on squared deviations: Var(X + Y) = Var(X) + Var(Y) when X and Y are independent. Standard deviation is the square root of variance, and √(a² + b²) ≠ a + b in general (by the triangle inequality). In practice, this means modeling combined uncertainty correctly requires working with variances, then taking the square root at the end — not adding the individual standard deviations first."
  explanation: "The additivity of variance for independent variables is a consequence of the linearity of expectation applied to squared deviations. It does not generalize to standard deviations. The practical error this prevents: if two independent measurement instruments each have standard deviation 2, the combined measurement error has standard deviation √(4 + 4) = √8 ≈ 2.83, not 2 + 2 = 4. Adding standard deviations overestimates combined uncertainty by assuming perfect positive correlation."
```

## Explainer

You already know that a **probability density function** (PDF) describes how probability is spread over continuous values — areas under the curve give probabilities. The normal distribution is one particular PDF shape, and it is the most important one in all of statistics. Its formula looks forbidding, but the geometry is simple: a symmetric, bell-shaped curve centered at **μ** (the mean), whose spread is controlled by **σ²** (the variance). Roughly 68% of probability falls within one σ of the mean, 95% within two, and 99.7% within three. These are not facts to memorize separately — they all follow directly from the formula and the symmetry of the bell.

Why does this particular shape appear so constantly in nature and data? The deeper reason — which you will prove formally when you study the Central Limit Theorem — is that whenever a measurement is the sum of many small, independent contributions, its distribution approaches normal regardless of the shape of each individual contribution. Human heights, measurement errors, test scores, and countless physical quantities all arise as sums of many small factors. The normal is not just common; it is the *inevitable limit* of that additive structure.

One algebraically important property is **closure under linear combinations**: if X ~ Normal(μ₁, σ₁²) and Y ~ Normal(μ₂, σ₂²) are independent, then X + Y ~ Normal(μ₁ + μ₂, σ₁² + σ₂²). This is a special feature — most distributions don't have it. It means that if you model individual components as normal, the aggregate is also normal, which makes complex calculations tractable. The mean adds, the variance adds (not the standard deviations — a common mistake), and the shape remains Gaussian.

The parameter μ shifts the bell left or right along the x-axis; σ stretches or compresses it. A **standard normal** has μ = 0 and σ = 1, written Z ~ Normal(0, 1). Any normal random variable can be converted to a standard normal by subtracting its mean and dividing by its standard deviation: Z = (X − μ)/σ. This standardization is why tables and software only need to tabulate one version of the distribution — every normal computation reduces to the standard form. When you work with z-scores in your next topic, you are using exactly this transformation to compare values from distributions with different scales.


