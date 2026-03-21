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

## Questions

```yaml
- question: "You compare two sample variances using an F-test and get F = 0.15 with (6, 10) degrees of freedom. To find the lower-tail critical value using a standard F-table that gives only upper-tail values, you should:"
  type: multiple-choice
  options:
    - "Use the F-table with F(6, 10) directly — standard tables cover both tails"
    - "Compute 1/F ≈ 6.67 and look up the upper-tail critical value for F(10, 6)"
    - "Double the upper-tail p-value, since the F-distribution is symmetric"
    - "Square the F-statistic and use a chi-square table with 16 degrees of freedom"
  answer: 1
  explanation: "The F-distribution is NOT symmetric. Standard tables give only upper-tail critical values. The reciprocal relationship F_{α, k₁, k₂} = 1/F_{1−α, k₂, k₁} handles lower-tail values: invert F and swap the degrees of freedom, then look up the upper tail of that new F-distribution. Here 1/0.15 ≈ 6.67, looked up in F(10, 6). Option C is wrong because the F-distribution is right-skewed and asymmetric. Option D conflates F with chi-square."

- question: "In a one-way ANOVA, an F-statistic much larger than 1 most likely indicates:"
  type: multiple-choice
  options:
    - "The within-group variance substantially exceeds the between-group variance"
    - "The between-group variance substantially exceeds the within-group variance"
    - "The sample sizes across groups are unequal"
    - "The assumption of equal population variances has been violated"
  answer: 1
  explanation: "The F-statistic in ANOVA is the ratio of between-group variance (MSB) to within-group variance (MSW). When all group means are equal, both estimate the same underlying variance and their ratio should be near 1. When group means truly differ, MSB inflates — it now captures genuine mean differences plus sampling noise — while MSW remains stable. A large F signals real differences between group means, pushing the statistic into the right tail of the F-distribution."

- question: "The F-distribution always takes positive values and is right-skewed, especially when the degrees of freedom are small."
  type: true-false
  answer: true
  explanation: "The F-distribution is defined as [χ²(k₁)/k₁] / [χ²(k₂)/k₂]. Both chi-square variables are sums of squared normals, so they are non-negative — making their ratio non-negative (positive almost surely). Chi-square distributions are right-skewed, especially at small degrees of freedom, which the F inherits. As both degrees of freedom grow large, the distribution concentrates near 1 and the skew decreases, but it remains non-symmetric."

- question: "The shape of the F-distribution is determined by a single degrees-of-freedom parameter, just like the t-distribution."
  type: true-false
  answer: false
  explanation: "Unlike the t-distribution (one df parameter), the F-distribution has two separate parameters: numerator degrees of freedom k₁ and denominator degrees of freedom k₂. Because F is a ratio of two chi-square variables each divided by their own df, the shape depends on both. This is why F-tables are two-dimensional. The t-distribution is a special case (t(k)² = F(1, k)), but the general F is fundamentally biparametric."

- question: "Explain why the F-statistic in ANOVA should be close to 1 when all population group means are equal, and why it tends to exceed 1 when means differ."
  type: short-answer
  answer: "When all group means are equal, both the between-group estimate (MSB) and the within-group estimate (MSW) are estimating the same population variance σ². Their ratio F = MSB/MSW should therefore be near 1. When group means truly differ, MSB inflates because it captures both sampling variability and the actual spread of group means, while MSW continues to estimate only within-group variability. The numerator grows relative to the denominator, pushing F above 1 and into the right tail."
  explanation: "This is why F-tests for ANOVA are one-tailed (right-tail only): we reject when F is too large, because large F means between-group variation is too great to plausibly arise from groups with the same mean. An F near 1 is consistent with the null hypothesis; an F much greater than 1 is evidence against it."
```

## Explainer

From the chi-square distribution, you know that if Z₁, Z₂, ..., Z_k are independent standard normal variables, then Z₁² + Z₂² + ··· + Z_k² follows a chi-square distribution with k degrees of freedom, written χ²(k). The chi-square distribution is right-skewed and defined only for positive values, because it is a sum of squares. It has expected value k and variance 2k. The **F-distribution** is built directly on top of the chi-square: take two independent chi-square random variables, divide each by its degrees of freedom (this "normalizes" both to have expected value approximately 1), and take their ratio. The result is F(k₁, k₂) = [χ²(k₁)/k₁] / [χ²(k₂)/k₂].

The F-distribution inherits its shape from its construction. Because it is a ratio of two non-negative quantities, it is defined only for positive values. Because the chi-square distributions are right-skewed, especially when degrees of freedom are small, the F-distribution is also right-skewed. As both k₁ and k₂ grow large, both chi-square variables approach their expected values (by the law of large numbers), so the ratio approaches 1 and the distribution becomes increasingly concentrated. The shape depends on both the **numerator degrees of freedom** k₁ and the **denominator degrees of freedom** k₂ — there is a whole family of F-distributions, one for each pair (k₁, k₂).

The natural application is comparing variances. If you draw two independent samples from normal populations and compute sample variances s₁² and s₂², then the ratio (s₁²/σ₁²) / (s₂²/σ₂²) follows an F-distribution. Under the null hypothesis that σ₁² = σ₂² (equal population variances), this ratio simplifies to s₁²/s₂², which then follows F(n₁-1, n₂-1). A ratio far from 1 — either very large or very small — provides evidence against equal variances. Because the F-distribution is right-skewed and not symmetric, tables typically give only upper-tail critical values; lower-tail critical values are obtained via the reciprocal relationship F_{α, k₁, k₂} = 1/F_{1-α, k₂, k₁}.

The same logic extends to comparing multiple group means in ANOVA. Rather than variance of raw data, the F-statistic in ANOVA compares two estimates of variance: one derived from variation *between* groups and one from variation *within* groups. If the groups have the same mean, both estimates should be comparable, and their ratio should be near 1. If the groups differ, between-group variance will be inflated relative to within-group variance, pushing the F-statistic into the right tail. In this way, the F-distribution connects the theory of variance ratios to the practical problem of deciding whether group differences are too large to attribute to chance.
