---
id: t-statistic-individual-coefficient
title: T-Statistic for Individual Coefficients
domain: economics
course: econometrics
prerequisites:
- id: normal-linear-regression-model
  type: hard
- id: hypothesis-testing-regression
  type: hard
builds-toward:
- confidence-intervals-regression
tags:
- hypothesis-testing
- inference
- coefficients
stage: advanced
status: draft
---

# T-Statistic for Individual Coefficients

## Core Idea
The t-statistic tⱼ = (β̂ⱼ - βⱼ₀) / se(β̂ⱼ) tests individual coefficients under normality, following a t-distribution with n - k degrees of freedom under H₀: βⱼ = βⱼ₀. It is used to construct confidence intervals and conduct significance tests on individual parameters.

## Explainer

You already know from the normal linear regression model that OLS estimates β̂ are random variables — different samples would give different estimates. The question inference asks is: given the estimate we got, what can we conclude about the true population parameter β? The **t-statistic** is the tool that answers this question for individual coefficients, one at a time.

The formula tⱼ = (β̂ⱼ − βⱼ₀) / se(β̂ⱼ) has a clear structure. The numerator is the distance between your estimate and the null hypothesis value (usually βⱼ₀ = 0, meaning "does this variable have any effect?"). The denominator — the **standard error** of the estimate — measures how much sampling variability we'd expect in β̂ⱼ. Dividing by the standard error rescales the distance into units of "how many standard errors away is the estimate from the null?" If the true parameter equals the null value, this ratio follows a t-distribution with n − k degrees of freedom (n observations minus k parameters estimated), which you can look up in tables or evaluate with software. Larger absolute t-values are less likely to arise by chance when the null is true, so they constitute stronger evidence against it.

The mechanics of hypothesis testing with the t-statistic follow directly from your work on hypothesis testing in regression. Choose a significance level α (typically 5%), find the critical value t* such that P(|t| > t*) = α under the null, and reject H₀ if |tⱼ| > t*. For large samples, the t-distribution approaches the standard normal, so t* ≈ 1.96 for a two-sided test at 5%. Many regression outputs report the p-value directly — the probability of observing a t-statistic at least as extreme as the one computed, if H₀ is true. A p-value below 0.05 means the result is "statistically significant at the 5% level," which is shorthand for "we'd see a t-statistic this large less than 5% of the time if the true coefficient were zero."

The t-statistic also underlies **confidence intervals**: β̂ⱼ ± t* · se(β̂ⱼ) gives an interval that, in repeated samples, would contain the true βⱼ 95% of the time (for t* chosen to give 95% coverage). This is more informative than a yes/no reject/fail-to-reject decision because it shows you both the plausible range of the effect and its precision. A key caution: the t-test on individual coefficients does not tell you whether a *group* of coefficients is jointly significant — for that, you need an F-test. Testing many individual t-statistics inflates the chance of false positives, a problem that builds toward the topic of multiple testing corrections.
