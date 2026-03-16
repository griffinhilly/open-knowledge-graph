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

## Explainer

From your work on hypothesis testing and the z-test, you know the basic logic: assume the null hypothesis, compute how unusual your data would be under that assumption, and reject if the probability is small enough. The z-test uses the test statistic z = (x̄ − μ₀) / (σ/√n), which requires knowing the population standard deviation σ. In practice, σ is almost never known — you only have your sample. The natural fix is to plug in the sample standard deviation s, giving t = (x̄ − μ₀) / (s/√n). But this substitution introduces extra uncertainty: s itself is a random variable, varying from sample to sample. The **t-distribution** accounts for this extra randomness. It looks like a standard normal but has heavier tails — the extra probability in the tails reflects the possibility that s is an underestimate of σ, making your standardized statistic larger than a z-score would be.

The **degrees of freedom** parameter controls how heavy the tails are. For a one-sample t-test, df = n − 1. With df = 2 (n = 3), the distribution has very heavy tails — extreme values are common. With df = 30 (n = 31), the tails are barely distinguishable from the normal. This makes intuitive sense: a large sample gives a reliable estimate of σ, so there is little extra uncertainty to account for. As n → ∞, the t-distribution converges to the standard normal, which is why the z-test is a limiting special case.

The choice between the three t-test variants depends on study design, not preference. **One-sample**: you have one group and want to test its mean against a known reference value (e.g., does this batch of pills contain exactly 500mg?). **Two-sample independent**: you have two separate groups and want to compare their means (e.g., do treated patients improve more than control patients?). Use Welch's t-test by default — it does not assume equal population variances, and it performs nearly as well as the pooled version even when variances are equal. **Paired**: you have matched pairs — two measurements on the same subject, or two subjects deliberately matched on key characteristics. The critical move is to compute the difference for each pair first, then run a one-sample t-test on those differences. Treating paired data as independent discards the matching information and artificially inflates variance, dramatically reducing power.

The conditions for validity are worth understanding, not just memorizing. The t-test is exact when the population is normal. When the population is not normal, the Central Limit Theorem saves you for large n — the sampling distribution of x̄ is approximately normal regardless of the population shape. What counts as "large enough" depends on skewness and the presence of outliers: for roughly symmetric populations, n ≥ 15 often suffices; for heavily skewed distributions, n ≥ 30 or more is safer. For small samples from clearly non-normal populations, consider a nonparametric alternative like the Wilcoxon signed-rank test, which does not assume normality.
