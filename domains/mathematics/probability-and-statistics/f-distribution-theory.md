---
id: f-distribution-theory
title: 'F-Distribution: Comparing Variances'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: f-distribution
  type: soft
- id: chi-square-distribution-theory
  type: hard
builds-toward:
- anova-one-way
- hypothesis-testing-fundamentals
tags:
- f-distribution
stage: formal-systems
status: draft
---

# F-Distribution: Comparing Variances

## Core Idea
F(k₁,k₂): ratio of independent χ²(k₁)/k₁ to χ²(k₂)/k₂. Right-skewed, positive. Used to test equality of variances and in ANOVA. Critical values depend on both numerator and denominator degrees of freedom.

## Explainer

From the chi-square distribution, you know that if Z₁, Z₂, ..., Z_k are independent standard normal variables, then Z₁² + Z₂² + ··· + Z_k² follows a chi-square distribution with k degrees of freedom, written χ²(k). The chi-square distribution is right-skewed and defined only for positive values, because it is a sum of squares. It has expected value k and variance 2k. The **F-distribution** is built directly on top of the chi-square: take two independent chi-square random variables, divide each by its degrees of freedom (this "normalizes" both to have expected value approximately 1), and take their ratio. The result is F(k₁, k₂) = [χ²(k₁)/k₁] / [χ²(k₂)/k₂].

The F-distribution inherits its shape from its construction. Because it is a ratio of two non-negative quantities, it is defined only for positive values. Because the chi-square distributions are right-skewed, especially when degrees of freedom are small, the F-distribution is also right-skewed. As both k₁ and k₂ grow large, both chi-square variables approach their expected values (by the law of large numbers), so the ratio approaches 1 and the distribution becomes increasingly concentrated. The shape depends on both the **numerator degrees of freedom** k₁ and the **denominator degrees of freedom** k₂ — there is a whole family of F-distributions, one for each pair (k₁, k₂).

The natural application is comparing variances. If you draw two independent samples from normal populations and compute sample variances s₁² and s₂², then the ratio (s₁²/σ₁²) / (s₂²/σ₂²) follows an F-distribution. Under the null hypothesis that σ₁² = σ₂² (equal population variances), this ratio simplifies to s₁²/s₂², which then follows F(n₁-1, n₂-1). A ratio far from 1 — either very large or very small — provides evidence against equal variances. Because the F-distribution is right-skewed and not symmetric, tables typically give only upper-tail critical values; lower-tail critical values are obtained via the reciprocal relationship F_{α, k₁, k₂} = 1/F_{1-α, k₂, k₁}.

The same logic extends to comparing multiple group means in ANOVA. Rather than variance of raw data, the F-statistic in ANOVA compares two estimates of variance: one derived from variation *between* groups and one from variation *within* groups. If the groups have the same mean, both estimates should be comparable, and their ratio should be near 1. If the groups differ, between-group variance will be inflated relative to within-group variance, pushing the F-statistic into the right tail. In this way, the F-distribution connects the theory of variance ratios to the practical problem of deciding whether group differences are too large to attribute to chance.
