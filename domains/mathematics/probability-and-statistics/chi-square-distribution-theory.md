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

## Questions

```yaml
- question: "Z₁, Z₂, Z₃, Z₄ are independent standard normal random variables. Which expression follows a chi-square distribution with 4 degrees of freedom?"
  type: multiple-choice
  options:
    - "Z₁ + Z₂ + Z₃ + Z₄"
    - "(Z₁ + Z₂ + Z₃ + Z₄)²"
    - "|Z₁| + |Z₂| + |Z₃| + |Z₄|"
    - "Z₁² + Z₂² + Z₃² + Z₄²"
  answer: 3
  explanation: "χ²(k) is defined as the sum of k *squared* independent standard normals. Option A is a sum of standard normals, which is N(0, 4). Option B is the square of a single sum, not the sum of individual squares. Option C sums absolute values (giving a half-normal-based distribution), not squares. Only option D matches: each Zᵢ² contributes 1 degree of freedom, and four independent squared normals give χ²(4)."

- question: "A goodness-of-fit test assigns survey responses to 6 categories, with n = 300 total responses. What are the degrees of freedom for the chi-square test statistic?"
  type: multiple-choice
  options:
    - "300 (the sample size)"
    - "6 (the number of categories)"
    - "5 (categories minus one)"
    - "299 (sample size minus one)"
  answer: 2
  explanation: "Degrees of freedom in a goodness-of-fit test equal k − 1, where k is the number of categories. With 6 categories, df = 5. The −1 arises because observed counts must sum to n, imposing one constraint and removing one degree of freedom. The sample size n affects expected counts and power but does not determine the degrees of freedom. Option D (n − 1 = 299) would apply to a t-test on a single mean."

- question: "A chi-square test statistic can take negative values, so unusually negative values provide evidence against the null hypothesis."
  type: true-false
  answer: false
  explanation: "A chi-square statistic is a sum of squared terms — either squared standard normals (by definition) or terms of the form (O_i − E_i)²/E_i — which are always non-negative. The distribution is bounded below at 0 and is right-skewed. Negative values are impossible. Chi-square tests are always one-tailed, rejecting H₀ only when the statistic is *large*. A value near 0 indicates the observed counts closely match the null model."

- question: "The expected value of a chi-square distribution with k degrees of freedom equals k."
  type: true-false
  answer: true
  explanation: "Since χ²(k) = Z₁² + Z₂² + ⋯ + Z_k² and each Zᵢ is standard normal, E[Zᵢ²] = Var(Zᵢ) = 1. By linearity of expectation, E[χ²(k)] = k × 1 = k. Each independent squared standard normal contributes exactly 1 to the expected value, and k independent contributions sum to k. The variance is 2k, following from Var(Zᵢ²) = E[Zᵢ⁴] − (E[Zᵢ²])² = 3 − 1 = 2."

- question: "Explain what the goodness-of-fit test statistic Σ(O_i − E_i)²/E_i measures and why a large value provides evidence against the null hypothesis."
  type: short-answer
  answer: "The statistic measures the overall discrepancy between observed counts (O_i) and what the null hypothesis predicts (E_i), with each squared difference scaled by 1/E_i to make it unit-free. Scaling matters: a deviation of 5 in a category with expected count 10 is more alarming than the same deviation in a category with expected count 500. Under H₀, observed counts should scatter randomly close to expected counts. A large statistic means the data deviate far more than chance would typically produce. Comparing to the χ²(k−1) distribution quantifies exactly how unlikely this much deviation is under H₀."
  explanation: "The connection to the definition of χ²(k) is direct: when H₀ is true, each term (O_i − E_i)/√E_i is approximately a standard normal, so the sum of their squares is approximately chi-square distributed. This is why the test statistic has the form it does — it is constructed to follow a known distribution under H₀."
```

## Explainer

The chi-square distribution arises naturally from normal random variables in a way that connects directly to the statistical tests you will build from it. The fundamental construction: if Z₁, Z₂, …, Z_k are **independent standard normal** random variables, then X = Z₁² + Z₂² + ⋯ + Z_k² follows a **chi-square distribution with k degrees of freedom**, written χ²(k). This is not merely a definition — it is the distribution that appears whenever you sum squared standardized normal quantities, which is exactly what happens in many test statistics.

The moments reveal the distribution's shape. E[χ²(k)] = k because E[Zᵢ²] = Var(Zᵢ) = 1 and expectations add. Var[χ²(k)] = 2k because Var(Zᵢ²) = E[Zᵢ⁴] − (E[Zᵢ²])² = 3 − 1 = 2 and variances of independent variables add. The distribution is right-skewed — a square is always non-negative, so the distribution is bounded below at 0, and the right tail extends far. As k grows, the skewness decreases: by the CLT, χ²(k) is approximately N(k, 2k) for large k. The **right tail** is what matters for hypothesis tests: you compute a test statistic, then ask how probable it is to see a value at least this large if H₀ is true.

Two key test contexts build directly from this structure. In a **goodness-of-fit test**, you have observed counts O_i and expected counts E_i across k categories. The test statistic Σ (O_i − E_i)²/E_i follows approximately χ²(k−1) when H₀ is true — the −1 comes from the constraint that counts must sum to n, removing one degree of freedom. In a **test of independence** on a contingency table with r rows and c columns, the statistic follows approximately χ²((r−1)(c−1)). The degrees of freedom always count the independent pieces of information: cells minus constraints imposed by row and column totals.

The chi-square distribution also connects to the sample variance: if X₁, …, X_n are i.i.d. N(μ, σ²), then (n−1)S²/σ² ~ χ²(n−1). This result underpins the t-distribution (formed as a ratio involving a standard normal over a √chi-square) and the F-distribution (a ratio of two independent chi-square values divided by their degrees of freedom). Understanding χ²(k) as a sum of squared standard normals is the correct mental model, because it makes every downstream result feel derived from first principles rather than memorized as an isolated fact.
