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
status: draft
---

# Normal Distribution: Properties and Fundamentals

## Core Idea
Normal(μ,σ²): PDF f(x)=(1/(σ√(2π)))exp(−(x−μ)²/(2σ²)). Symmetric and bell-shaped. E[X]=μ, Var(X)=σ². Central limit theorem makes it ubiquitous. Linear combinations of independent normals are normal.

## Explainer

You already know that a **probability density function** (PDF) describes how probability is spread over continuous values — areas under the curve give probabilities. The normal distribution is one particular PDF shape, and it is the most important one in all of statistics. Its formula looks forbidding, but the geometry is simple: a symmetric, bell-shaped curve centered at **μ** (the mean), whose spread is controlled by **σ²** (the variance). Roughly 68% of probability falls within one σ of the mean, 95% within two, and 99.7% within three. These are not facts to memorize separately — they all follow directly from the formula and the symmetry of the bell.

Why does this particular shape appear so constantly in nature and data? The deeper reason — which you will prove formally when you study the Central Limit Theorem — is that whenever a measurement is the sum of many small, independent contributions, its distribution approaches normal regardless of the shape of each individual contribution. Human heights, measurement errors, test scores, and countless physical quantities all arise as sums of many small factors. The normal is not just common; it is the *inevitable limit* of that additive structure.

One algebraically important property is **closure under linear combinations**: if X ~ Normal(μ₁, σ₁²) and Y ~ Normal(μ₂, σ₂²) are independent, then X + Y ~ Normal(μ₁ + μ₂, σ₁² + σ₂²). This is a special feature — most distributions don't have it. It means that if you model individual components as normal, the aggregate is also normal, which makes complex calculations tractable. The mean adds, the variance adds (not the standard deviations — a common mistake), and the shape remains Gaussian.

The parameter μ shifts the bell left or right along the x-axis; σ stretches or compresses it. A **standard normal** has μ = 0 and σ = 1, written Z ~ Normal(0, 1). Any normal random variable can be converted to a standard normal by subtracting its mean and dividing by its standard deviation: Z = (X − μ)/σ. This standardization is why tables and software only need to tabulate one version of the distribution — every normal computation reduces to the standard form. When you work with z-scores in your next topic, you are using exactly this transformation to compare values from distributions with different scales.


