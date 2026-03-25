---
id: statistical-conclusion-validity-assumptions
title: Statistical Conclusion Validity and Assumptions of Statistical Tests
domain: psychology
course: research-methods-psychology
prerequisites:
- id: inferential-statistics-psychology
  type: hard
- id: effect-size-and-power
  type: hard
- id: hypothesis-testing-framework
  type: soft
- id: type-i-type-ii-error-tradeoffs
  type: soft
- id: assumption-violations-robustness
  type: soft
builds-toward:
- multiple-comparisons-correction-type-i-error
- exploratory-vs-confirmatory-analysis-strategies
tags:
- validity
- statistics
- assumptions
- inference
stage: formal-systems
status: validated
---
# Statistical Conclusion Validity and Assumptions of Statistical Tests

## Core Idea
Statistical conclusion validity concerns the accuracy of conclusions about whether an observed covariation between variables is genuine. This depends on proper assumptions including independent observations, homogeneity of variance, appropriate distribution forms, and adequate statistical power. Violations of assumptions can lead to inflated or deflated Type I and Type II error rates, producing biased conclusions. Researchers must verify statistical assumptions through diagnostic tests and use appropriate statistical techniques (e.g., nonparametric alternatives, robust estimators) when assumptions are violated.

## How It's Best Learned
Conduct analyses assuming violated assumptions to observe how conclusions change. Practice diagnostic tests (Q-Q plots, Levene's test, independence checks) on real datasets.

## Common Misconceptions
If p < .05, the conclusion is definitely correct (violating assumptions can bias p-values). Statistical tests are robust to all assumption violations (actual robustness depends on specific assumptions, effect sizes, and sample sizes).

## Questions

```yaml
- question: "A researcher measures math anxiety in 200 students, with 20 students nested within each of 10 classrooms. They run a standard independent-samples t-test comparing anxious vs. non-anxious students. What is the primary threat to statistical conclusion validity?"
  type: multiple-choice
  options:
    - "Non-normality — student anxiety scores are unlikely to be normally distributed"
    - "Violation of independence — students within the same classroom share experiences, inflating Type I error"
    - "Insufficient power — 200 students is too small a sample for a t-test"
    - "Heterogeneity of variance — anxious and non-anxious students likely have different score variances"
  answer: 1
  explanation: "The independence assumption is violated because students within the same classroom share the same teacher, physical environment, and classroom climate — making their scores positively correlated within clusters. Standard errors computed assuming independence are too small, p-values are artificially low, and Type I error is inflated above the nominal α. The fix is multilevel modeling or cluster-robust standard errors. Independence violations are especially dangerous because they are invisible in the data — you must know the data collection procedure to detect them."

- question: "A study uses a standard ANOVA with α = .05 but the group variances are quite heterogeneous and group sizes are unequal (the larger group has larger variance). What is the likely consequence for the actual Type I error rate?"
  type: multiple-choice
  options:
    - "Type I error rate stays at .05 — ANOVA is robust to all assumption violations"
    - "Type I error rate is deflated below .05 — the test becomes more conservative"
    - "Type I error rate is inflated above .05 — false positives occur more than intended"
    - "Type II error rate is inflated — the test loses power but maintains α = .05"
  answer: 2
  explanation: "When the larger group has larger variance, standard ANOVA inflates the Type I error rate — you reject the null hypothesis more often than the nominal α implies. This specific pattern (larger group, larger variance) makes the test anti-conservative. The fix is Welch's ANOVA, which adjusts degrees of freedom to account for unequal variances and should be the default. The belief that ANOVA is 'robust to everything' is the misconception this question targets; robustness is conditional on the specific violation and design."

- question: "A p-value below .05 guarantees that statistical conclusion validity is intact — the conclusion about covariation between variables is trustworthy."
  type: true-false
  answer: false
  explanation: "Statistical conclusion validity is threatened whenever test assumptions are violated, because assumption violations silently change the actual Type I error rate from the nominal α. A test that appears to operate at α = .05 might actually produce false positives at α = .15 under severe violations. Getting p < .05 from a test with violated assumptions does not mean the result is real — it may mean the test's null distribution was wrong, making the critical value incorrect. Checking p against a threshold only works if the threshold was computed correctly, which requires valid assumptions."

- question: "The central limit theorem protects against non-normality in small samples, making parametric tests robust to distributional violations even when n < 20."
  type: true-false
  answer: false
  explanation: "The central limit theorem provides protection in large samples — as n increases, sampling distributions of means become approximately normal even if the raw data are not. In small samples (roughly n < 30–40 per group), the CLT has not had enough sample size to 'kick in,' and non-normality of the underlying distribution can substantially distort p-values. For small samples with non-normal data, nonparametric alternatives (Wilcoxon, Mann-Whitney) or bootstrap methods are more appropriate."

- question: "Why is violation of the independence assumption especially dangerous for statistical conclusion validity, compared to violations of normality or homogeneity of variance?"
  type: short-answer
  answer: "Independence violations are invisible in the raw data — you cannot detect them by examining the numbers. You can only identify them by knowing how the data were collected (e.g., students nested within classrooms, repeated measures from the same person). By contrast, non-normality and heterogeneity of variance can be detected through diagnostic plots (Q-Q plots, Levene's test). Additionally, independence violations typically inflate Type I error, often dramatically, because standard errors under clustering are too small — the test sees apparent precision that doesn't exist."
  explanation: "The severity also depends on the intraclass correlation (ICC): how similar are observations within the same cluster? High ICC (e.g., patients at the same clinic responding similarly to treatment) produces severe inflation; low ICC produces minor inflation. Without accounting for clustering, you may 'find' effects that are purely artifacts of shared environmental influence within clusters — a common source of non-replicable findings in psychology and education research."
```

## Explainer

From your study of hypothesis testing and statistical power, you know that a statistical test can produce two kinds of error: a **Type I error** (a false positive — you conclude there is an effect when there isn't) and a **Type II error** (a false negative — you miss a real effect). You also know that power is the probability of detecting a true effect. **Statistical conclusion validity** is the umbrella question: *can you trust the conclusion your statistical test produced?* It is threatened whenever the test's assumptions are violated, because those violations silently change the actual Type I and Type II error rates away from what you thought you had set.

Every parametric statistical test is built on assumptions. The t-test and ANOVA assume that observations are **independent** of each other (no clustering), that residuals are approximately **normally distributed**, and that group variances are roughly **equal** (homogeneity of variance). These are not arbitrary formalities — the math that produces the p-value you observe is derived under these conditions. When the conditions do not hold, the null distribution changes shape, and the critical value you used to decide whether to reject H₀ is no longer correct. A test that nominally operates at α = .05 might, under severe assumption violations, actually produce false positives at α = .15 — or, if the violation pushes in the other direction, at α = .01. You no longer know what you have.

The most consequential assumption in practice is **independence of observations**. Clustering — measuring multiple students in the same classroom, multiple patients from the same clinic, multiple observations from the same person over time — introduces positive dependence within clusters. Standard errors computed under the independence assumption are too small, p-values are too small, and Type I error rates are inflated. The fix is to use multilevel models or cluster-robust standard errors that account for the nested structure. Independence violations are especially insidious because they are invisible in raw data — you have to know the data collection procedure to spot them.

**Non-normality** of residuals matters most in small samples. With sample sizes above roughly 30–40 per group, the **central limit theorem** means that sampling distributions of means are approximately normal even if the raw data are not — this is what people mean when they say ANOVA is "robust to non-normality." But this robustness is conditional on adequate sample size and does not apply to all statistics (e.g., tests involving variances are less robust). **Heterogeneity of variance** is more troubling when combined with unequal group sizes: if the large group also has the larger variance, Type I error is inflated; if the large group has the smaller variance, it is deflated. Welch's t-test and Welch's ANOVA correct for unequal variances and should be used by default rather than the standard versions.

The practical discipline of statistical conclusion validity is running diagnostic checks before interpreting results. **Q-Q plots** assess normality of residuals; **Levene's test** or **Bartlett's test** assesses homogeneity of variance; intraclass correlations detect clustering. When assumptions are violated, the response is not to run the test anyway and hope — it is to choose a procedure whose assumptions match your data: nonparametric alternatives (Wilcoxon, Kruskal-Wallis) when normality is badly violated; robust estimators (bootstrap confidence intervals, heteroskedasticity-consistent standard errors) when variance is unequal; multilevel models when data are nested. The goal is not a specific p-value, but a p-value you can interpret as meaning what it is supposed to mean.
