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

## Questions

```yaml
- question: "A regression estimates a coefficient β̂ = 4.2 with standard error se = 1.4. The null hypothesis is β = 0. What is the t-statistic, and what is the correct interpretation?"
  type: multiple-choice
  options:
    - "t = 4.2; the coefficient is large enough to be automatically significant"
    - "t = 3.0; the estimate is 3 standard errors from zero, which we compare to a critical value to assess significance"
    - "t = 4.2 / 1.4 = 0.33; the effect is small relative to its variance"
    - "t = 1.4 / 4.2 = 0.33; we need additional information about sample size to interpret this"
  answer: 1
  explanation: "The t-statistic is (β̂ − β₀) / se = (4.2 − 0) / 1.4 = 3.0. This means the estimate is 3 standard errors above zero, which we compare to the critical value from the t-distribution with n − k degrees of freedom (approximately 1.96 for large n at 5% significance). The raw coefficient (4.2) cannot be judged as 'significant' without knowing the standard error—a coefficient of 4.2 with se = 5 is insignificant, while one with se = 0.5 is highly significant."

- question: "All five individual t-statistics in a regression are statistically insignificant at the 5% level. What can you conclude?"
  type: multiple-choice
  options:
    - "None of the independent variables have any effect on the dependent variable"
    - "The model has no explanatory power and should be discarded"
    - "The variables are jointly insignificant, as confirmed by the individual t-tests"
    - "The individual coefficients may still be jointly significant—a separate F-test is needed to assess joint significance"
  answer: 3
  explanation: "Individual t-tests assess each coefficient in isolation. Multicollinearity or other factors can make individual coefficients appear insignificant even when the group jointly explains meaningful variation. The F-test for joint significance is the correct tool for asking whether a set of restrictions (like all slopes equal zero) holds simultaneously. Concluding from individual t-tests alone that variables have no joint effect is a common error in applied regression."

- question: "A p-value of 0.04 for a coefficient means there is a 96% probability that the true coefficient is nonzero."
  type: true-false
  answer: false
  explanation: "This is one of the most common misinterpretations in statistics. The p-value is a frequency probability under the null hypothesis: it is the probability of observing a t-statistic at least as extreme as the one computed *if the null hypothesis were true*. It does not measure the probability that the null is true or false. Interpreting p = 0.04 as '96% chance the coefficient is real' conflates a frequentist p-value with a Bayesian posterior—a fundamentally different quantity."

- question: "Dividing the OLS estimate by its standard error is essential because a large coefficient is not necessarily evidence against the null hypothesis."
  type: true-false
  answer: true
  explanation: "A coefficient of 100 is meaningless without context. If the standard error is 200, the estimate is only 0.5 standard errors from zero—easily explained by sampling variation. The standard error quantifies how much the estimate would vary across repeated samples; only when the estimate is large relative to this variability do we have evidence against the null. This is why the t-statistic (the signal-to-noise ratio) is the right measure, not the raw coefficient."

- question: "Explain why running separate t-tests on many coefficients inflates the risk of false positives, and what problem this creates in practice."
  type: short-answer
  answer: "Each t-test at the 5% level has a 5% chance of falsely rejecting the null when it is true. With k independent tests, the probability of at least one false positive is approximately 1 − 0.95^k, which grows rapidly with k—testing 14 coefficients gives roughly a 50% chance of at least one false positive by chance alone. In practice, researchers who scan many candidates and report only 'significant' results are likely cherry-picking noise. Corrections (Bonferroni, false discovery rate) or joint F-tests address this problem."
  explanation: "Multiple testing inflation is why data-mining—running many regressions and highlighting significant results—requires correction. The t-statistic is designed for testing a pre-specified hypothesis, not for searching over many possible effects."
```

## Explainer

You already know from the normal linear regression model that OLS estimates β̂ are random variables — different samples would give different estimates. The question inference asks is: given the estimate we got, what can we conclude about the true population parameter β? The **t-statistic** is the tool that answers this question for individual coefficients, one at a time.

The formula tⱼ = (β̂ⱼ − βⱼ₀) / se(β̂ⱼ) has a clear structure. The numerator is the distance between your estimate and the null hypothesis value (usually βⱼ₀ = 0, meaning "does this variable have any effect?"). The denominator — the **standard error** of the estimate — measures how much sampling variability we'd expect in β̂ⱼ. Dividing by the standard error rescales the distance into units of "how many standard errors away is the estimate from the null?" If the true parameter equals the null value, this ratio follows a t-distribution with n − k degrees of freedom (n observations minus k parameters estimated), which you can look up in tables or evaluate with software. Larger absolute t-values are less likely to arise by chance when the null is true, so they constitute stronger evidence against it.

The mechanics of hypothesis testing with the t-statistic follow directly from your work on hypothesis testing in regression. Choose a significance level α (typically 5%), find the critical value t* such that P(|t| > t*) = α under the null, and reject H₀ if |tⱼ| > t*. For large samples, the t-distribution approaches the standard normal, so t* ≈ 1.96 for a two-sided test at 5%. Many regression outputs report the p-value directly — the probability of observing a t-statistic at least as extreme as the one computed, if H₀ is true. A p-value below 0.05 means the result is "statistically significant at the 5% level," which is shorthand for "we'd see a t-statistic this large less than 5% of the time if the true coefficient were zero."

The t-statistic also underlies **confidence intervals**: β̂ⱼ ± t* · se(β̂ⱼ) gives an interval that, in repeated samples, would contain the true βⱼ 95% of the time (for t* chosen to give 95% coverage). This is more informative than a yes/no reject/fail-to-reject decision because it shows you both the plausible range of the effect and its precision. A key caution: the t-test on individual coefficients does not tell you whether a *group* of coefficients is jointly significant — for that, you need an F-test. Testing many individual t-statistics inflates the chance of false positives, a problem that builds toward the topic of multiple testing corrections.
