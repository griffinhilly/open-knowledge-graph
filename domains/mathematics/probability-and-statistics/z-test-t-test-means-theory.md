---
id: z-test-t-test-means-theory
title: Z-Tests and T-Tests for Means
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: hypothesis-testing-framework-theory
  type: hard
builds-toward:
- type-i-and-type-ii-errors
tags:
- z-test
- t-test
stage: formal-systems
status: validated
---

# Z-Tests and T-Tests for Means

## Core Idea
Z-test: Z=(X̄−μ₀)/(σ/√n) when σ known. T-test: T=(X̄−μ₀)/(s/√n) with n−1 df when σ unknown. Use t-test (more conservative) in practice. Both test H₀:μ=μ₀. T-distribution accounts for estimating σ from data.

## Questions

```yaml
- question: "A researcher tests whether a sample mean differs from a known value. She knows the exact population standard deviation σ. Her colleague advises: 'Always use the t-test — it's more conservative and safer.' Should she follow this advice?"
  type: multiple-choice
  options:
    - "Yes — the t-test's heavier tails provide better protection against false positives in all situations"
    - "Yes — t-tests are always preferred at small sample sizes, regardless of what is known"
    - "No — when σ is known, the z-test is the exact and correct procedure; using the t-test introduces unnecessary conservatism without justification"
    - "No — when σ is known, a chi-squared test should be used instead"
  answer: 2
  explanation: "The t-test's heavier tails exist to account for uncertainty in estimating σ from data. When σ is known exactly, there is no such uncertainty, and the z-test is the correct exact procedure. Using the t-test in this case over-inflates uncertainty without scientific justification — it is more conservative than the data warrants. The choice between z-test and t-test is not a safety preference; it is determined by whether σ is known or estimated."

- question: "As sample size n increases without bound, what happens to the relationship between the t-test and the z-test?"
  type: multiple-choice
  options:
    - "The t-test becomes increasingly conservative relative to the z-test"
    - "The z-test becomes invalid because the Central Limit Theorem assumptions break down"
    - "The two tests converge because s converges to σ and the t-distribution approaches the standard normal"
    - "The t-test automatically switches to the standard normal distribution when n > 30"
  answer: 2
  explanation: "As n → ∞, the sample standard deviation s is estimated from more data and converges to the true σ. With this convergence, the extra variability that causes the t-distribution's heavier tails disappears. The t-distribution with n−1 degrees of freedom approaches the standard normal as n → ∞. The distinction between t-test and z-test matters primarily at small sample sizes where s is a poor estimator of σ."

- question: "The t-distribution has heavier tails than the standard normal because estimating σ from data introduces additional variability that must be accounted for."
  type: true-false
  answer: true
  explanation: "When you substitute s for σ in the test statistic, s itself varies from sample to sample — it is a random variable, not a fixed constant. This extra source of variability makes extreme values of the test statistic more likely than under the standard normal. The t-distribution captures this by assigning more probability to its tails. Fewer degrees of freedom (smaller n) means s is estimated from less data, so it varies more, and the tails get heavier."

- question: "When the population standard deviation σ is known, a t-test with n−1 degrees of freedom is the appropriate procedure."
  type: true-false
  answer: false
  explanation: "When σ is known, the z-test is the correct procedure. The t-test exists specifically to handle the case where σ is unknown and must be estimated by s. Using the t-test when σ is known over-inflates the uncertainty in the test, making it harder to reject a false null hypothesis than the data actually warrants."

- question: "Why does the t-test use n−1 degrees of freedom rather than n, and how does this make the test more conservative at small sample sizes?"
  type: short-answer
  answer: "After computing the sample mean X̄ from n data points, only n−1 of the deviations (xᵢ − X̄) are free to vary independently — the last deviation is determined by the constraint that all deviations sum to zero. So s is estimated from n−1 independent pieces of information. Fewer degrees of freedom give the t-distribution heavier tails, which means the critical threshold for rejecting H₀ is higher, demanding stronger evidence. At small n, s is highly variable and may be far from σ, so the extra conservatism is appropriate."
  explanation: "The degrees of freedom directly measure how much independent information is used to estimate σ. At n = 2, you have only 1 degree of freedom — the distribution is very wide and demands extreme evidence. As n grows, degrees of freedom increase, the t-distribution tightens toward the normal, and the conservatism shrinks to nothing. The test automatically scales its caution to the amount of information available."
```

## Explainer

From the hypothesis testing framework, you know the core procedure: assume H₀ is true, compute a test statistic measuring how far the data falls from what H₀ predicts, then calculate the probability of observing a result that extreme by chance. The z-test and t-test are the two standard implementations of this framework when the question is about a population mean. They share the same logic — they differ only in how much you know about the population.

The **z-test** applies when the population standard deviation σ is known. The test statistic is Z = (X̄ − μ₀) / (σ/√n). The denominator σ/√n is the **standard error** — the standard deviation of the sampling distribution of X̄, which you derived from the Central Limit Theorem. Dividing the observed deviation X̄ − μ₀ by the standard error converts the raw difference into a dimensionless z-score: how many standard errors away from μ₀ your sample mean landed. Under H₀, this statistic follows a standard normal distribution, and you look up the tail probability from that distribution.

The **t-test** applies when σ is unknown — which is nearly always in practice. You estimate σ using the sample standard deviation s, giving T = (X̄ − μ₀) / (s/√n). The problem is that s itself varies from sample to sample, introducing additional uncertainty. This extra variability means the test statistic no longer follows a standard normal distribution; instead, it follows a **t-distribution** with n − 1 **degrees of freedom**. The t-distribution looks like a normal distribution but has heavier tails — it assigns more probability to extreme values, making it more conservative. As n grows large, s converges to σ, the t-distribution converges to the normal, and the t-test and z-test give identical results.

The degrees of freedom n − 1 reflect a subtle cost: once you've estimated the mean X̄ from your n data points, only n − 1 of the deviations (xᵢ − X̄) are free to vary independently. The last one is determined by the constraint that deviations sum to zero. Fewer degrees of freedom → more uncertainty → heavier tails → a higher threshold to reject H₀. This is why the t-test is described as more conservative: at small sample sizes, it demands stronger evidence before concluding the effect is real, appropriately accounting for the uncertainty in estimating σ from limited data.
