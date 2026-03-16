---
id: chi-square-distribution-theory
title: 'Chi-Square Distribution: Theory and Tests'
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: chi-square-distribution
  type: soft
builds-toward:
- chi-square-test
- hypothesis-testing-fundamentals
tags:
- chi-square
stage: formal-systems
status: draft
---

# Chi-Square Distribution: Theory and Tests

## Core Idea
χ²(k): distribution of sum of k squared independent standard normals. E[χ²(k)]=k, Var[χ²(k)]=2k. Right-skewed. Arises in testing independence and goodness-of-fit. Critical values depend on degrees of freedom.

## Explainer

The chi-square distribution arises naturally from normal random variables in a way that connects directly to the statistical tests you will build from it. The fundamental construction: if Z₁, Z₂, …, Z_k are **independent standard normal** random variables, then X = Z₁² + Z₂² + ⋯ + Z_k² follows a **chi-square distribution with k degrees of freedom**, written χ²(k). This is not merely a definition — it is the distribution that appears whenever you sum squared standardized normal quantities, which is exactly what happens in many test statistics.

The moments reveal the distribution's shape. E[χ²(k)] = k because E[Zᵢ²] = Var(Zᵢ) = 1 and expectations add. Var[χ²(k)] = 2k because Var(Zᵢ²) = E[Zᵢ⁴] − (E[Zᵢ²])² = 3 − 1 = 2 and variances of independent variables add. The distribution is right-skewed — a square is always non-negative, so the distribution is bounded below at 0, and the right tail extends far. As k grows, the skewness decreases: by the CLT, χ²(k) is approximately N(k, 2k) for large k. The **right tail** is what matters for hypothesis tests: you compute a test statistic, then ask how probable it is to see a value at least this large if H₀ is true.

Two key test contexts build directly from this structure. In a **goodness-of-fit test**, you have observed counts O_i and expected counts E_i across k categories. The test statistic Σ (O_i − E_i)²/E_i follows approximately χ²(k−1) when H₀ is true — the −1 comes from the constraint that counts must sum to n, removing one degree of freedom. In a **test of independence** on a contingency table with r rows and c columns, the statistic follows approximately χ²((r−1)(c−1)). The degrees of freedom always count the independent pieces of information: cells minus constraints imposed by row and column totals.

The chi-square distribution also connects to the sample variance: if X₁, …, X_n are i.i.d. N(μ, σ²), then (n−1)S²/σ² ~ χ²(n−1). This result underpins the t-distribution (formed as a ratio involving a standard normal over a √chi-square) and the F-distribution (a ratio of two independent chi-square values divided by their degrees of freedom). Understanding χ²(k) as a sum of squared standard normals is the correct mental model, because it makes every downstream result feel derived from first principles rather than memorized as an isolated fact.
