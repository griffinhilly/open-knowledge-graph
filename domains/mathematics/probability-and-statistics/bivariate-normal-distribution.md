---
id: bivariate-normal-distribution
title: Bivariate Normal Distribution
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: normal-distribution-intro
  type: hard
- id: covariance-between-random-variables
  type: hard
builds-toward:
- multivariate-normal-distribution
tags:
- normal-distribution
- multivariate
- continuous-distributions
stage: formal-systems
status: draft
---

# Bivariate Normal Distribution

## Core Idea
The bivariate normal distribution is a joint distribution where both marginals are normal and all conditional distributions are normal. It's determined by five parameters: μ₁, μ₂, σ₁, σ₂, and ρ. Contour plots show elliptical level sets.

## How It's Best Learned
Simulate data from bivariate normal distributions with different correlations. Create scatterplots and contour plots. Compute marginals and conditionals algebraically. Relate the correlation parameter to the shape of the elliptical contours.

## Explainer

You know from studying the **normal distribution** that a single normal random variable is described by its mean μ and variance σ². And from **covariance**, you know how to measure the linear relationship between two random variables. The bivariate normal distribution is the natural generalization: a joint distribution for two variables (X, Y) that extends the bell-curve shape into two dimensions and makes covariance a first-class part of the model.

A **bivariate normal** distribution is fully specified by five parameters: the marginal means μ₁ = E[X] and μ₂ = E[Y], the marginal standard deviations σ₁ and σ₂, and the **correlation coefficient** ρ = Cov(X,Y)/(σ₁σ₂) ∈ [−1, 1]. The joint density is an explicit formula (involving ρ in the exponent), but the key facts follow from the structure without memorizing the density. First, each **marginal distribution** is normal: X ~ N(μ₁, σ₁²) and Y ~ N(μ₂, σ₂²). Second, every **conditional distribution** is also normal: given X = x, the conditional distribution Y|X = x is normal with mean μ₂ + ρ(σ₂/σ₁)(x − μ₁) and variance σ₂²(1 − ρ²). The conditional mean is a linear function of x — this is the population version of a regression line.

The geometry is vivid: level curves of the joint density (where the density equals a constant) are **ellipses** centered at (μ₁, μ₂). When ρ = 0, the ellipses are axis-aligned — X and Y are independent (in the normal case, zero correlation implies independence, which is not true for distributions in general). As |ρ| increases toward 1, the ellipses tilt and elongate: ρ > 0 tilts them northeast, ρ < 0 tilts them southeast. At ρ = ±1 the ellipses collapse to a line, corresponding to a perfect linear relationship.

The bivariate normal is the building block for multivariate statistics. Linear combinations of jointly normal variables are normal: aX + bY ~ N(aμ₁ + bμ₂, a²σ₁² + 2abρσ₁σ₂ + b²σ₂²). This additivity, plus the normal marginals and normal conditionals, is what makes the bivariate normal so tractable analytically and so central to regression, factor analysis, and Gaussian process models. Understanding it deeply — especially the role of ρ in shaping the conditional distribution — prepares you directly for the general multivariate normal.
