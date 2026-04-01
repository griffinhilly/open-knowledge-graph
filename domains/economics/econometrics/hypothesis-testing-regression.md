---
id: hypothesis-testing-regression
title: Hypothesis Testing in Regression
domain: economics
course: econometrics
prerequisites:
- id: coefficient-interpretation-regression
  type: hard
- id: hypothesis-testing-fundamentals
  type: hard
- id: t-test-for-means
  type: hard
- id: p-values-and-significance
  type: hard
- id: confidence-intervals-means
  type: hard
- id: hypothesis-test-framework
  type: soft
builds-toward:
- f-test-joint-significance
- r-squared-and-model-fit
tags:
- t-test
- significance
- standard-errors
- hypothesis-testing
stage: formal-systems
status: validated
---

# Hypothesis Testing in Regression

## Core Idea
In regression, each coefficient β̂ⱼ has an associated standard error se(β̂ⱼ), and the t-statistic t = (β̂ⱼ − β₀)/se(β̂ⱼ) tests whether βⱼ equals some hypothesized value (usually zero) in the population. Under the null, this t-statistic follows a t-distribution with n−k−1 degrees of freedom; for large samples it approaches the standard normal. Statistical significance at the 5% level means the p-value is below 0.05, but economic significance — whether the effect size matters practically — is a separate judgment. Confidence intervals for coefficients convey both magnitude and precision.

## How It's Best Learned
Interpret regression tables from published papers, explaining each coefficient's sign, magnitude, standard error, and significance level. Practice constructing confidence intervals manually from reported standard errors.

## Common Misconceptions
- A statistically significant coefficient may be economically trivial, especially in large samples.
- Failing to reject the null does not prove the null is true — it may reflect low power from a small sample or high variance.

## Questions

```yaml
- question: "A regression on n = 1,000,000 observations finds β̂₁ = 0.0004 with a p-value of 0.001. Which conclusion is most defensible?"
  type: multiple-choice
  options:
    - "The result is both statistically and economically significant"
    - "The result is statistically significant but the effect size is almost certainly economically trivial"
    - "The result is not significant because the coefficient is very small"
    - "The p-value is meaningless with such a large sample"
  answer: 1
  explanation: "With a million observations, standard errors are tiny — even minuscule effects produce significant p-values. A coefficient of 0.0004 means a one-unit change in x predicts a 0.04% change in y. Whether that matters economically depends on the context, but it is almost never substantively important. Statistical significance tells you the effect is probably real; economic significance tells you whether it matters."

- question: "A p-value of 0.04 means there is a 4% chance that the null hypothesis is true."
  type: true-false
  answer: false
  explanation: "The p-value is the probability of observing a test statistic as extreme as the one computed, *assuming the null hypothesis is true*. It is not the probability that H₀ is true. A p-value of 0.04 means: if H₀ were true, you would see a result this extreme 4% of the time. Inverting this — saying H₀ has a 4% chance of being true — is a common and serious misinterpretation."

- question: "A researcher tests H₀: β₁ = 0 and gets a p-value of 0.42. Does this prove the true coefficient is zero? Explain."
  type: short-answer
  answer: "No. Failing to reject H₀ does not prove it is true. The result may simply reflect low statistical power — a sample too small or variance too high to detect a real but modest effect."
  explanation: "Hypothesis testing can only reject or fail to reject the null — it cannot confirm it. A p-value of 0.42 means the data are consistent with β₁ = 0, but they are also consistent with many nonzero values. This is especially true when sample size is small, since confidence intervals will be wide and include zero even for economically meaningful effect sizes."
```

## Explainer

When you learned t-tests for comparing means, you computed a test statistic by dividing an estimate by its standard error: t = (x̄ − μ₀)/se(x̄). Hypothesis testing in regression is exactly the same idea applied to a regression coefficient. The OLS estimator β̂ⱼ is a random variable with a sampling distribution — it varies across hypothetical repeated samples. The standard error se(β̂ⱼ) measures how much β̂ⱼ varies across those samples. The t-statistic t = (β̂ⱼ − β₀)/se(β̂ⱼ) measures how many standard errors the estimate lies from the hypothesized value β₀ (usually zero). Under the null, this follows a t-distribution with n − k − 1 degrees of freedom; in large samples it is approximately standard normal.

Reading a regression table fluently means interpreting four things for each coefficient: its sign (direction of effect), its magnitude (how large is the effect), its standard error (how precisely estimated), and its p-value or significance stars (whether you would see this estimate by chance under H₀). The stars tell you whether the effect is statistically distinguishable from zero; they do not tell you whether the effect is large enough to matter. Every published table reports these together, and conflating them is one of the most common errors in applied work.

The statistical vs. economic significance distinction is the central lesson of this topic, and it is non-obvious. With a large enough sample, even a microscopic true effect will produce a tiny standard error, generating a significant p-value. An economist studying wages with n = 2,000,000 records might find that having a window seat at work raises wages by $0.12 per year with p < 0.001. That effect is real — it is not due to noise — but it is economically meaningless. Conversely, with n = 50 observations, a genuinely large effect may fail to reach significance simply because the sample is too small to detect it. Always report effect sizes alongside significance, and ask whether the magnitude of β̂ is large enough to matter for any real decision.

What does it actually mean when a result is significant at the 5% level? It means that if the null hypothesis were true, you would observe a t-statistic at least this large only 5% of the time by chance. It does not mean there is a 95% chance the null is false, and it does not mean the coefficient is 'probably' the right sign. The p-value is a statement about what you would observe in hypothetical repeated sampling under H₀ — not a probability assigned to the null hypothesis being true or false.

Confidence intervals are often more informative than p-values. A 95% confidence interval for β̂ⱼ is approximately β̂ⱼ ± 1.96 × se(β̂ⱼ). This interval gives you the range of effect sizes consistent with the data, rather than forcing a binary significant/not-significant verdict. A very wide confidence interval that just excludes zero is technically significant but tells you almost nothing about the true effect size. A narrow interval centered on a small value tells you the effect is real and small. Reporting and interpreting confidence intervals is the best habit to develop for honest empirical work.

