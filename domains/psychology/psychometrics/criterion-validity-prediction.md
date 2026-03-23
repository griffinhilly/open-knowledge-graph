---
id: criterion-validity-prediction
title: Criterion-Related Validity and Predictive Accuracy
domain: psychology
course: psychometrics
prerequisites:
- id: reliability-validity-relationship
  type: hard
- id: linear-regression
  type: soft
builds-toward:
- validity-evidence-frameworks
- computerized-adaptive-testing
tags:
- criterion-validity
- prediction
- utility-analysis
stage: expert
status: validated
---

# Criterion-Related Validity and Predictive Accuracy

## Core Idea
Criterion-related validity examines whether test scores predict or relate to relevant external outcomes (criteria). Predictive validity refers to forecasting future performance; concurrent validity relates to current outcomes. Correlation coefficients, regression coefficients, and utility analysis quantify these relationships.

## Questions

```yaml
- question: "A cognitive ability test for job applicants has a validity coefficient of r = 0.40 with supervisor ratings of job performance. What percentage of variance in job performance does this test account for?"
  type: multiple-choice
  options:
    - "40%, because the validity coefficient directly represents the proportion of variance explained"
    - "16%, because the coefficient of determination is r² = 0.16"
    - "60%, because 1 – r represents the unexplained portion"
    - "80%, because r = 0.40 indicates a strong relationship in applied settings"
  answer: 1
  explanation: "The validity coefficient r tells you the direction and strength of the linear relationship, but the proportion of variance in the criterion explained by the test is r² — the coefficient of determination. For r = 0.40, r² = 0.16, meaning the test accounts for 16% of variance in job performance. This is why r² is the more interpretable effect size. Option A is the most common misconception: treating r itself as if it were a proportion of variance."

- question: "A researcher validates a new depression screening scale by administering it to 300 patients and simultaneously collecting clinician diagnostic ratings. She finds a strong correlation between scale scores and clinician judgments. This study establishes:"
  type: multiple-choice
  options:
    - "Predictive validity, because the scale forecasts future clinical outcomes"
    - "Concurrent validity, because the scale scores and criterion are collected at the same point in time"
    - "Construct validity, because it shows the scale measures what it claims to measure"
    - "Incremental validity, because the scale adds information beyond what clinicians already know"
  answer: 1
  explanation: "Concurrent validity is established when test scores and criterion measures are collected simultaneously. The defining feature is timing: no waiting period. Predictive validity requires administering the test first and then measuring the criterion outcome at a later date. While concurrent validity is faster and cheaper to establish, predictive validity is usually more important for selection and screening contexts because the practical value of a test is its ability to forecast, not just correlate with current status."

- question: "A test that shows strong concurrent validity — a high correlation between test scores and current criterion status — is equally suitable for personnel selection as a test with strong predictive validity."
  type: true-false
  answer: false
  explanation: "Concurrent validity and predictive validity differ in what they tell you. Concurrent validity tells you that the test correlates with a criterion measured at the same time, which may reflect that both are tapping the same present state. Predictive validity tells you that test scores administered now forecast performance measured later — which is the actual task in selection contexts. A test that correlates with current performance may not predict who will succeed in a role months or years later. The time lag matters enormously for applied purposes."

- question: "Even a modest validity coefficient (e.g., r = 0.30) can justify using a selection test in high-stakes hiring decisions, depending on base rates, selection ratios, and the costs of selection errors."
  type: true-false
  answer: true
  explanation: "Utility analysis shows that the practical value of a test depends on more than its validity coefficient. If the base rate of success is moderate (not too high or too low), the selection ratio is competitive (many applicants per position), and the cost of a hiring mistake is high, even r = 0.30 can produce substantial economic benefit. Conversely, a test with r = 0.50 may have little practical value if nearly all applicants succeed anyway (high base rate) or if positions always get filled (selection ratio = 1). Validity alone does not determine usefulness."

- question: "Why is r² a more useful way to interpret a validity coefficient than r alone, and what implication does this have for tests with 'moderate' validity (r ≈ 0.40–0.50)?"
  type: short-answer
  answer: "r² represents the proportion of criterion variance accounted for by the test, which is the direct measure of how much the test reduces prediction error. r is a correlation coefficient whose scale is not directly interpretable as a proportion. A validity of r = 0.40 seems substantial in isolation, but r² = 0.16 reveals that 84% of criterion variance is still unexplained — the test has real but limited predictive power. This matters for setting expectations: tests with 'good' validity coefficients still leave most of the criterion outcome to be explained by other factors. It also guards against overconfidence in prediction."
  explanation: "The common error is treating r as if it directly measures predictive accuracy or explained variance, when it measures only the linear association strength. Squaring r to obtain r² — the coefficient of determination — converts the correlation into a proportion-of-variance metric that is directly interpretable."
```

## Explainer

You've studied the reliability-validity relationship and know that validity comes in multiple forms, each answering a different question about what a test measures. You've also worked with linear regression, which lets you quantify the relationship between a predictor and an outcome. Criterion-related validity brings these concepts together in the most practically grounded form of validity evidence: does this test actually predict something that matters in the world?

The question criterion validity asks is concrete. If you have a cognitive ability test for job applicants, does it predict job performance? If you have an anxiety measure, does it predict who responds to treatment? **Criterion-related validity** is quantified as the correlation (or regression relationship) between test scores and a separate, meaningful outcome measure — the **criterion**. A test with high criterion validity is genuinely useful; one with low criterion validity, however theoretically motivated, gives you little practical traction.

Two forms are distinguished by timing. **Predictive validity** tests whether scores forecast future outcomes: administer the test now, wait, then measure the criterion outcome months or years later. The classic example is SAT scores predicting college GPA — a forward-in-time relationship. **Concurrent validity** measures the relationship between test scores and a criterion collected at the same time, such as a depression scale correlated with current clinician diagnosis. Concurrent validity is faster and cheaper to establish; predictive validity is usually more important, because the practical value of a test in selection or screening contexts is its ability to forecast, not just correlate with current standing.

Your regression background applies directly here. The **validity coefficient** — the correlation r between test and criterion — tells you the direction and strength of the relationship. But r² (the coefficient of determination) tells you the proportion of criterion variance accounted for, which is the more interpretable effect-size metric. A validity coefficient of 0.40 sounds substantial but accounts for only 16% of criterion variance. **Utility analysis** then asks a practical question: even a modest validity coefficient may justify using a test if the stakes are high, selection is competitive, or errors are costly. The economic value of a selection instrument depends jointly on the validity coefficient, the base rate of success in the population, and the selection ratio — how many positions there are relative to applicants.
