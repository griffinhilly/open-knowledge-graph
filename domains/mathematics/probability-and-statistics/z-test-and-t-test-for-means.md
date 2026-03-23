---
id: z-test-and-t-test-for-means
title: Z-Tests and T-Tests for Means
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: hypothesis-testing-fundamentals
  type: hard
- id: standard-normal-and-z-scores
  type: hard
- id: confidence-intervals-means
  type: soft
tags:
- z-test
- t-test
- test-statistic
- p-value
stage: formal-systems
status: validated
---

# Z-Tests and T-Tests for Means

## Core Idea
A z-test tests hypotheses about a population mean when the population standard deviation σ is known (rare in practice). The test statistic is z = (x̄ - μ₀) / (σ/√n). A t-test is used when σ is unknown and replaced by sample standard deviation s; the test statistic is t = (x̄ - μ₀) / (s/√n), which follows a t-distribution with n-1 degrees of freedom. The t-distribution has heavier tails than normal, so t-tests account for additional uncertainty from estimating σ. Both tests compare observed sample means to hypothesized population means.

## How It's Best Learned
Compute z and t statistics from data. Use tables or software to find p-values. Compare z-test and t-test on the same data for large and small samples. Understand why t-distribution is appropriate for small samples.

## Common Misconceptions
Using z-test when σ is unknown. Confusing degrees of freedom in t-distribution. Thinking larger t values have larger p-values (opposite is true). Misapplying tests without checking normality assumptions for small samples.

## Questions

```yaml
- question: "A researcher tests whether a new drug reduces blood pressure using 12 patients. She doesn't know the population standard deviation, so she estimates it as s = 8.3 from her sample. Which test should she use, and why?"
  type: multiple-choice
  options:
    - "Z-test, because her sample size is large enough to assume approximate normality."
    - "Z-test, because estimating σ from a sample is standard practice and does not change the test."
    - "T-test, because σ is unknown and using s in its place introduces additional uncertainty that the heavier-tailed t-distribution accounts for."
    - "Either test is equally valid for this problem; the choice makes no difference in practice."
  answer: 2
  explanation: "The key distinction: the z-test requires knowing the true population standard deviation σ. When you substitute the sample standard deviation s, you introduce a second layer of randomness — s itself varies from sample to sample. This extra uncertainty is captured by the t-distribution's heavier tails. Option A conflates normality (a sampling distribution assumption) with knowledge of σ; those are separate requirements. Option D is wrong because for small n, the two tests give meaningfully different critical values."

- question: "A researcher computes t = 3.5 on one hypothesis test and t = 1.2 on another (both two-sided, same degrees of freedom). Compared to t = 1.2, the p-value for t = 3.5 is:"
  type: multiple-choice
  options:
    - "Larger — a higher t-value indicates more spread in the sampling distribution."
    - "Smaller — a t-statistic farther from zero is less likely under the null hypothesis, so the tail probability is smaller."
    - "The same — degrees of freedom determine the p-value, not the magnitude of t."
    - "Cannot be determined without knowing the hypothesized population mean."
  answer: 1
  explanation: "A larger absolute t-value means the sample result sits farther from the null hypothesis value in units of standard error. The probability of observing a result that extreme (or more extreme) under H₀ is therefore smaller — a smaller p-value, not a larger one. This is one of the most common beginner errors: students assume a bigger test statistic means a bigger p-value. The direction is opposite."

- question: "As sample size n increases, the t-distribution approaches the standard normal distribution, which is why z-tests and t-tests produce nearly identical results for large samples."
  type: true-false
  answer: true
  explanation: "The t-distribution has heavier tails because s is an imprecise estimate of σ for small samples. As n grows, s stabilizes and converges toward σ — the extra uncertainty shrinks. The t-distribution with n−1 degrees of freedom approaches the standard normal as n → ∞. By n ≈ 30, the two distributions are nearly indistinguishable, which is why large-sample z-tests are defensible even when σ is technically unknown."

- question: "The z-test is the appropriate default for testing a population mean whenever the sample size exceeds 30, because the Central Limit Theorem guarantees normality of the sample mean."
  type: true-false
  answer: false
  explanation: "The Central Limit Theorem justifies approximate normality of x̄ — but the z-test also requires knowing σ, which is almost never the case in real data. The t-test is the correct default: it handles unknown σ properly, and for large n it gives essentially the same answer as the z-test anyway (since the t-distribution converges to normal). Choosing z over t when σ is unknown is a common but avoidable error."

- question: "Why does the t-distribution have heavier tails than the standard normal, and what does this imply about the critical values needed for a t-test versus a z-test at the same significance level?"
  type: short-answer
  answer: "The t-distribution has heavier tails because using s instead of σ introduces a second source of randomness — s is itself a random variable that varies from sample to sample. This extra variability in the denominator of the test statistic makes extreme values more probable than they would be under the standard normal. As a consequence, the critical values for a t-test are larger in magnitude than for a z-test at the same α: the t-test demands a more extreme sample result before rejecting H₀, appropriately accounting for the additional uncertainty."
  explanation: "For example, at α = 0.05 two-sided with 10 degrees of freedom, the t critical value is ±2.228, compared to ±1.96 for the z-test. With more degrees of freedom (larger n), the t critical value approaches 1.96 as the two distributions converge. The heavier tails are a feature, not a bug — they prevent false rejections caused by using an imprecise estimate of spread."
```

## Explainer

You already know the core logic of hypothesis testing: assume the null hypothesis is true, compute how far your sample result is from what the null predicts, and ask how likely such a deviation is by chance. You also know how to convert raw values to **z-scores** using the standard normal distribution. The z-test and t-test both apply that exact logic to sample means — the only real difference is what you know about the population's variability.

A **z-test** applies when you know the true population standard deviation σ. The test statistic z = (x̄ − μ₀) / (σ/√n) measures how many standard errors your sample mean sits from the hypothesized population mean μ₀. The denominator σ/√n is the **standard error of the mean** — the theoretical spread of sample means when repeatedly drawing samples of size n. Because σ is known, this denominator is exact, and the test statistic follows a standard normal distribution precisely. In practice, knowing σ is rare (it would require surveying the entire population), so the z-test is mostly theoretical or used for large samples where the Central Limit Theorem ensures approximate normality.

In real data analysis, you almost always estimate σ from the sample itself using the sample standard deviation s. Plugging s in where σ was gives the **t-test statistic**: t = (x̄ − μ₀) / (s/√n). But here's the subtle problem: s is itself a random variable — it varies from sample to sample — introducing additional uncertainty into the denominator. This extra randomness makes the test statistic follow a **t-distribution** rather than a standard normal. The t-distribution looks like a normal distribution but with heavier tails, reflecting that extreme outcomes are somewhat more likely when your estimate of spread is itself imprecise. The exact shape depends on **degrees of freedom** (df = n − 1): with only a few observations, uncertainty is large and tails are heavy; as n grows, s stabilizes and the t-distribution converges to the standard normal. By n ≈ 30, the two distributions are nearly identical, which is why large-sample z-tests are defensible even when σ is unknown.

The decision rule is the same for both tests: compute the test statistic, find the p-value (the probability of observing a result this extreme under H₀), and compare to your significance level α. A larger absolute value of z or t pushes the p-value *down*, making the result more significant — the opposite of what beginners sometimes assume. When running a two-sided test, you're asking whether your sample mean is far from μ₀ in *either* direction, so you use the total tail probability on both ends. When choosing between z and t, the rule is simple: use t-tests by default. They handle the unknown-σ case correctly, and when n is large enough that z would have been fine, the t-test gives essentially the same answer anyway.

