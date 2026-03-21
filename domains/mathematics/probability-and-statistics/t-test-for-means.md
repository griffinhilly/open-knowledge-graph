---
id: t-test-for-means
title: One-Sample and Two-Sample T-Tests
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: hypothesis-testing-fundamentals
  type: hard
- id: z-test-for-means
  type: soft
- id: measures-of-spread
  type: hard
- id: p-values-and-significance
  type: soft
builds-toward:
- anova-one-way
tags:
- t-test
- t-distribution
- degrees-of-freedom
- two-sample
- paired
stage: formal-systems
status: validated
---
# One-Sample and Two-Sample T-Tests

## Core Idea
The t-test replaces the z-test when the population standard deviation σ is unknown, estimating it with the sample standard deviation s. The test statistic t = (x̄ − μ₀) / (s/√n) follows a t-distribution with n − 1 degrees of freedom — a bell-shaped distribution with heavier tails than the normal. Two-sample t-tests compare means of two independent groups; paired t-tests account for matched pairs by analyzing differences. As n increases, the t-distribution approaches the standard normal.

## How It's Best Learned
Use technology for p-value computation — the t-distribution CDF is not tabulated conveniently. Focus on conditions: nearly normal population or large n, independent observations. Practice deciding which t-test applies: one-sample, two-sample independent, or paired.

## Common Misconceptions
- Using pooled variance when population variances are not assumed equal (Welch's t-test is safer).
- Forgetting to compute differences first in a paired design — treating paired data as independent.
- Not checking normality conditions before applying the t-test to small samples.

## Questions

```yaml
- question: "A researcher wants to test whether the mean blood pressure of a patient sample differs from a known reference value of 120 mmHg. The population standard deviation is unknown. Which test is appropriate, and why?"
  type: multiple-choice
  options:
    - "A z-test, because the reference value μ₀ is known"
    - "A t-test, because the population standard deviation σ is unknown and must be estimated from the sample"
    - "A z-test, because blood pressure is normally distributed in the population"
    - "A t-test, because the sample size is likely small"
  answer: 1
  explanation: "The z-test requires knowing the population standard deviation σ. When σ is unknown — the common situation in practice — the sample standard deviation s is substituted, producing the t-statistic t = (x̄ − μ₀)/(s/√n). This substitution introduces extra uncertainty about how well s approximates σ, which is captured by the t-distribution's heavier tails. The normality of the population or the size of the sample are secondary considerations that affect validity, not the choice between z and t."

- question: "A study measures each participant's blood pressure before and after a training program. A researcher analyzes the data by running a standard two-sample independent t-test on the before and after groups. What error has the researcher made?"
  type: multiple-choice
  options:
    - "Using a t-test instead of a z-test, since the measurements are paired"
    - "Ignoring the pairing structure — matched pairs should be analyzed as differences, then subjected to a one-sample t-test"
    - "Nothing — a two-sample t-test is always valid when comparing two sets of measurements"
    - "Using a one-tailed instead of two-tailed test"
  answer: 1
  explanation: "When data consists of matched pairs (two measurements on the same subject), the correct approach is to compute the difference for each pair first, then run a one-sample t-test on those differences. Treating the 'before' and 'after' groups as independent discards the matching information — the correlation between a person's before and after measurements — and artificially inflates the variance estimate, dramatically reducing the test's power to detect a real effect."

- question: "As the sample size n increases in a one-sample t-test, the t-distribution used to compute p-values approaches the standard normal distribution."
  type: true-false
  answer: true
  explanation: "With more data, the sample standard deviation s becomes a more reliable estimate of the true σ, so the extra uncertainty that distinguishes the t-distribution from the normal diminishes. Formally, the t-distribution with df = n − 1 converges to N(0, 1) as n → ∞. This is why the z-test can be seen as a limiting special case of the t-test — when n is large enough, s ≈ σ and the two tests produce nearly identical results."

- question: "The t-test statistic is computed identically to the z-test statistic — both use the population standard deviation σ in the denominator."
  type: true-false
  answer: false
  explanation: "This is precisely the distinction between the two tests. The z-statistic uses z = (x̄ − μ₀)/(σ/√n), where σ is the known population standard deviation. The t-statistic uses t = (x̄ − μ₀)/(s/√n), where s is the sample standard deviation — an estimate of σ computed from the data itself. This substitution of a random quantity (s) for a fixed quantity (σ) is what gives the test statistic a t-distribution rather than a normal distribution, with heavier tails to account for the additional variability."

- question: "Why does the t-distribution have heavier tails than the standard normal distribution, and what does this mean for hypothesis testing in practice?"
  type: short-answer
  answer: "The t-distribution has heavier tails because the test statistic uses s (the sample standard deviation) instead of the known σ. Since s is itself a random variable that varies from sample to sample, the t-statistic carries extra uncertainty beyond what the normal accounts for. Heavier tails mean the critical values (e.g., t* for α = 0.05) are larger than the corresponding z* values — making it harder to reject the null with small samples."
  explanation: "The practical implication is that with small samples, you need a larger observed effect to reach statistical significance compared to a z-test. This is the cost of not knowing σ: you use a wider rejection region to account for the possibility that your s underestimates σ and your standardized statistic is therefore inflated. The degrees of freedom parameter (df = n − 1) tracks how much information you have about σ — more data, more information, thinner tails, critical values closer to the normal."
```

## Explainer

From your work on hypothesis testing and the z-test, you know the basic logic: assume the null hypothesis, compute how unusual your data would be under that assumption, and reject if the probability is small enough. The z-test uses the test statistic z = (x̄ − μ₀) / (σ/√n), which requires knowing the population standard deviation σ. In practice, σ is almost never known — you only have your sample. The natural fix is to plug in the sample standard deviation s, giving t = (x̄ − μ₀) / (s/√n). But this substitution introduces extra uncertainty: s itself is a random variable, varying from sample to sample. The **t-distribution** accounts for this extra randomness. It looks like a standard normal but has heavier tails — the extra probability in the tails reflects the possibility that s is an underestimate of σ, making your standardized statistic larger than a z-score would be.

The **degrees of freedom** parameter controls how heavy the tails are. For a one-sample t-test, df = n − 1. With df = 2 (n = 3), the distribution has very heavy tails — extreme values are common. With df = 30 (n = 31), the tails are barely distinguishable from the normal. This makes intuitive sense: a large sample gives a reliable estimate of σ, so there is little extra uncertainty to account for. As n → ∞, the t-distribution converges to the standard normal, which is why the z-test is a limiting special case.

The choice between the three t-test variants depends on study design, not preference. **One-sample**: you have one group and want to test its mean against a known reference value (e.g., does this batch of pills contain exactly 500mg?). **Two-sample independent**: you have two separate groups and want to compare their means (e.g., do treated patients improve more than control patients?). Use Welch's t-test by default — it does not assume equal population variances, and it performs nearly as well as the pooled version even when variances are equal. **Paired**: you have matched pairs — two measurements on the same subject, or two subjects deliberately matched on key characteristics. The critical move is to compute the difference for each pair first, then run a one-sample t-test on those differences. Treating paired data as independent discards the matching information and artificially inflates variance, dramatically reducing power.

The conditions for validity are worth understanding, not just memorizing. The t-test is exact when the population is normal. When the population is not normal, the Central Limit Theorem saves you for large n — the sampling distribution of x̄ is approximately normal regardless of the population shape. What counts as "large enough" depends on skewness and the presence of outliers: for roughly symmetric populations, n ≥ 15 often suffices; for heavily skewed distributions, n ≥ 30 or more is safer. For small samples from clearly non-normal populations, consider a nonparametric alternative like the Wilcoxon signed-rank test, which does not assume normality.
