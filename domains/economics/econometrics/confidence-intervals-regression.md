---
id: confidence-intervals-regression
title: Confidence Intervals and Hypothesis Tests in Regression
domain: economics
course: econometrics
prerequisites:
- id: asymptotic-normality-regression
  type: hard
- id: hypothesis-testing-regression
  type: hard
builds-toward:
- prediction-intervals-regression
tags:
- inference
- hypothesis-testing
- intervals
stage: advanced
status: validated
---

# Confidence Intervals and Hypothesis Tests in Regression

## Core Idea
Confidence intervals quantify uncertainty around parameter estimates using estimated standard errors and critical values from the t-distribution; hypothesis tests evaluate whether parameters equal specific values. Both rely on asymptotic normality and require valid estimates of standard errors, accounting for any heteroskedasticity or serial correlation.

## Questions

```yaml
- question: "After running a regression, a researcher reports: 'There is a 95% probability that the true coefficient β lies between 0.3 and 0.8.' What is wrong with this statement?"
  type: multiple-choice
  options:
    - "Nothing — this is the standard frequentist interpretation of a 95% confidence interval"
    - "The interval should use z-critical values, not t-critical values, for a 95% interval"
    - "The true coefficient β is a fixed unknown constant, not a random variable. The interval is what varies across samples. The correct statement is that if this procedure were repeated many times, 95% of such intervals would contain the true β"
    - "The researcher should report a prediction interval, not a confidence interval, for inference about β"
  answer: 2
  explanation: "This is the most common misinterpretation of confidence intervals. In frequentist statistics, the true parameter β is a fixed (unknown) constant — it either is or isn't in any particular interval, with probability 1 or 0, not 0.95. What has a 95% probability is the *procedure*: if you repeatedly drew samples from the population and computed intervals this way, 95% of those intervals would contain the true β. Any given computed interval either covers β or it doesn't. The probabilistic statement applies to the random interval before data are collected, not to the fixed interval after you have computed it. Option A is the misconception; Option C is the correction."

- question: "A 95% confidence interval for a slope coefficient β̂_j is computed as [0.15, 0.85]. A colleague runs a t-test for H₀: β_j = 0 at the 5% significance level. What should they find?"
  type: multiple-choice
  options:
    - "The t-test cannot be determined from the confidence interval alone — they test different things"
    - "The t-test fails to reject H₀, because the interval is wide and therefore uncertain"
    - "The t-test rejects H₀ at 5%, because 0 falls outside the 95% confidence interval — the interval and test are perfectly dual"
    - "The t-test result depends on the sample size, which the confidence interval does not convey"
  answer: 2
  explanation: "The confidence interval and t-test are mathematically dual: the 95% CI contains exactly the values of c for which a two-sided t-test of H₀: β_j = c would fail to reject at the 5% level. Since 0 is outside [0.15, 0.85], the t-test of H₀: β_j = 0 rejects at the 5% level. Equivalently, if 0 were inside the interval, the test would fail to reject. This duality means you can read hypothesis test results from confidence intervals: the interval communicates both the significance decision and the magnitude of the effect, making it more informative than the t-statistic alone."

- question: "A 95% confidence interval constructed using OLS standard errors has a 95% probability of containing the true β in large samples, regardless of whether errors are heteroskedastic."
  type: true-false
  answer: false
  explanation: "When errors are heteroskedastic, the classical OLS standard errors are inconsistent — they typically underestimate the true sampling uncertainty. This means the computed confidence intervals are too narrow, and they cover the true β less than 95% of the time. In practice, heteroskedastic errors cause over-rejection: tests that should fail to reject at 5% do reject, and CIs that should contain β don't. Correct coverage requires using heteroskedasticity-robust (HC) standard errors. The OLS coefficient estimator β̂ is still unbiased under heteroskedasticity — it's the standard errors (and therefore the intervals) that break down."

- question: "Because the confidence interval and the hypothesis test are mathematically equivalent, reporting a p-value conveys strictly less information than reporting the confidence interval."
  type: true-false
  answer: true
  explanation: "A p-value gives a binary (reject/fail to reject) answer for one specific null hypothesis (usually H₀: β = 0). The confidence interval communicates the same decision (does 0 fall outside it?) but also shows the range of plausible values for β and the precision of the estimate. Knowing β̂ = 0.5 with CI [0.48, 0.52] versus CI [0.1, 0.9] conveys very different information about the reliability and practical importance of the effect, even though both might reject H₀: β = 0. This is why journals increasingly require reporting of confidence intervals alongside p-values — the p-value alone discards information about effect size and uncertainty."

- question: "Why does the presence of heteroskedasticity invalidate standard OLS confidence intervals, and what is the appropriate remedy?"
  type: short-answer
  answer: "OLS confidence intervals use the formula β̂ ± t* · se(β̂), where se(β̂) is the estimated standard error. The classical OLS standard error formula assumes homoskedastic errors (constant variance). When errors are heteroskedastic (variance differs across observations), the classical formula produces inconsistent estimates of the true sampling variance — typically underestimates — so the standard errors are too small, the intervals too narrow, and they fail to cover the true β at the claimed rate. The remedy is to use heteroskedasticity-robust (White or HC) standard errors, which estimate the true sampling variance consistently under heteroskedasticity. The OLS coefficient estimates β̂ are unchanged; only the standard errors used to construct intervals and test statistics change."
  explanation: "The key insight is that β̂ itself is not affected by heteroskedasticity (it remains unbiased and consistent), but inference — confidence intervals, t-statistics, p-values — all depend entirely on having correct standard errors. Getting standard errors right is not a refinement; it determines whether your statistical conclusions are reliable. Cluster-robust standard errors extend this logic to serial correlation within groups."
```

## Explainer

You already know from asymptotic normality that the OLS estimator β̂ is approximately normally distributed in large samples: (β̂ − β) / se(β̂) → N(0,1). A **confidence interval** uses this fact directly — it constructs a range around β̂ that, under repeated sampling, would contain the true β in 95% of cases (for a 95% interval). The formula is β̂ ± t* · se(β̂), where t* is the critical value from the t-distribution with n − k − 1 degrees of freedom. In large samples, t* ≈ 1.96 for 95% confidence. The interval does not mean "there is a 95% chance β is inside this range" — β is a fixed (unknown) constant, not a random variable. What varies across samples is β̂ itself.

The **t-statistic** for hypothesis testing is the same building block rearranged. To test H₀: βⱼ = c (typically c = 0, the hypothesis that variable j has no effect), compute t = (β̂ⱼ − c) / se(β̂ⱼ). Under H₀, this statistic follows an approximate t-distribution. A large absolute value of t means the estimate is many standard errors from the hypothesized value — unlikely if H₀ were true. The **p-value** converts this to a probability: it is the probability of observing a t-statistic at least as extreme as yours if H₀ were true. A p-value below your chosen significance level (commonly 0.05) leads to rejection of H₀.

The confidence interval and hypothesis test are two sides of the same coin: β̂ ± t* · se(β̂) contains exactly the values c for which a two-sided test would fail to reject H₀: βⱼ = c. If zero is inside the 95% confidence interval, the t-test at 5% significance fails to reject H₀: βⱼ = 0. If zero is outside, you reject. This duality gives you two ways to communicate the same inference — the interval conveys both significance and effect magnitude, while the test gives a clean binary decision.

The critical ingredient in all of this is se(β̂) — the estimated standard error. You know from your prerequisites that if errors are heteroskedastic or serially correlated, the classical OLS standard errors are inconsistent; they typically understate the true uncertainty, producing confidence intervals that are too narrow and t-statistics that are too large. This is why valid inference requires using **heteroskedasticity-robust** or **cluster-robust** standard errors whenever those problems are present. The formula for β̂ does not change — only the standard errors you attach to it do. Getting this right is not a technical nicety; it is the difference between inference you can trust and inference that will mislead you.
