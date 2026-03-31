---
id: poisson-regression-biostatistics
title: Poisson Regression in Biostatistics
domain: health-and-human-development
course: biostatistics
prerequisites:
- id: logistic-regression-biostatistics
  type: soft
- id: linear-regression
  type: hard
- id: study-design-biostatistics
  type: soft
builds-toward:
- cox-proportional-hazards-detailed
tags:
- Poisson
- count-data
- incidence-rate
- rate-ratio
- offset
- overdispersion
stage: advanced
status: validated
---

# Poisson Regression in Biostatistics

## Core Idea
Poisson regression models count outcomes (number of infections, hospital admissions, deaths) by relating the log of the expected count to a linear combination of predictors: log(mu) = beta_0 + beta_1*x_1 + ... + beta_k*x_k. The log link ensures predicted counts are always positive. When subjects contribute different amounts of observation time, an offset term log(person-time) is included, effectively modeling incidence rates rather than raw counts. Exponentiated coefficients represent incidence rate ratios. The key assumption is equidispersion — that the variance equals the mean — which is frequently violated in practice (overdispersion), requiring extensions like negative binomial regression or robust standard errors.

## Questions

```yaml
- question: "A Poisson regression of hospital readmissions includes age and comorbidity count as predictors. The coefficient for comorbidity count is 0.15. What is the correct interpretation?"
  type: multiple-choice
  options:
    - "Each additional comorbidity increases readmissions by 0.15 events"
    - "Each additional comorbidity increases the expected readmission count by a factor of exp(0.15) ≈ 1.16, or about 16%"
    - "Each additional comorbidity increases the probability of readmission by 15%"
    - "Comorbidity count explains 15% of the variance in readmissions"
  answer: 1
  explanation: "Poisson regression coefficients are on the log-count (or log-rate) scale. The coefficient of 0.15 means each additional comorbidity increases the log of the expected count by 0.15. Exponentiating gives the rate ratio: exp(0.15) ≈ 1.16, meaning the expected readmission rate increases by about 16% per additional comorbidity. This is a multiplicative effect — the same proportional increase regardless of the baseline count."

- question: "In a Poisson regression of cancer deaths across counties, different counties contribute different population sizes. Why is an offset term for log(population) necessary?"
  type: multiple-choice
  options:
    - "It adjusts for the fact that larger counties have more deaths simply because they have more people — the offset converts raw counts to rates"
    - "It ensures the model produces probabilities between 0 and 1"
    - "It corrects for overdispersion caused by population heterogeneity"
    - "It is only needed when population sizes are unknown"
  answer: 0
  explanation: "A county with 1 million people will have more cancer deaths than a county with 10,000 people regardless of any risk factor — raw counts are not comparable across different exposure times or population sizes. The offset log(population) moves from the right side of the equation, converting the model from log(expected count) = Xβ to log(expected count / population) = Xβ, which is log(rate) = Xβ. The coefficients then represent log rate ratios rather than log count ratios, making comparisons valid."

- question: "If the variance of a count outcome substantially exceeds the mean, the Poisson model's standard errors will be too small, but the coefficient estimates themselves remain unbiased."
  type: true-false
  answer: true
  explanation: "Overdispersion (variance > mean) does not bias the Poisson regression point estimates — the coefficients remain consistent. However, the Poisson model assumes variance equals the mean, so it underestimates the true variability when overdispersion is present. This produces standard errors that are too small, confidence intervals that are too narrow, and p-values that are too small — leading to false positives. Solutions include using robust (sandwich) standard errors, quasi-Poisson models, or switching to negative binomial regression which has an additional parameter for overdispersion."

- question: "Explain why Poisson regression uses a log link rather than modeling counts directly as a linear function of predictors."
  type: short-answer
  answer: "Counts are non-negative integers, but a linear function of predictors can produce negative values, which are meaningless as counts. The log link maps the positive real line to all reals, ensuring that the expected count exp(Xβ) is always positive regardless of predictor values. The log link also provides a natural multiplicative interpretation: effects are proportional changes in the rate rather than additive changes, which matches how most biological exposures affect disease rates."
  explanation: "The log link is the canonical link for the Poisson distribution in the generalized linear model framework. It also connects directly to epidemiological thinking — rate ratios (multiplicative comparisons) are the standard measure of association for incidence data, and the log link produces exactly these quantities as exponentiated coefficients."
```

## Explainer

Many outcomes in biostatistics are counts: the number of asthma attacks per year, the number of infections in a hospital ward per month, the number of cancer cases in a population. These outcomes are non-negative integers with a right-skewed distribution that cannot be modeled well with ordinary linear regression. Poisson regression is the generalized linear model designed for count data, using a log link function and assuming the outcome follows a Poisson distribution.

The model specifies that the log of the expected count is a linear function of predictors: log(E[Y|X]) = beta_0 + beta_1*x_1 + ... This means that exp(beta_j) gives the **rate ratio** — the multiplicative change in the expected count for a one-unit increase in x_j. If exp(beta_1) = 1.3, the expected count is 30% higher for each additional unit of x_1. The log link ensures predicted counts are always positive (you cannot have negative asthma attacks), and the multiplicative interpretation is natural for biological processes where risk factors scale rates proportionally.

When observations contribute different amounts of **person-time** (patients followed for different durations, populations of different sizes), raw counts are not comparable. A hospital that follows 1,000 patients for a year will have more infections than one following 100 patients for a month, even if the rate is identical. The **offset** term handles this by including log(person-time) as a predictor with a fixed coefficient of 1. Algebraically, this converts the model from log(expected count) = Xβ to log(expected count / person-time) = Xβ, which models rates rather than counts. The offset is essential whenever the denominator (time at risk or population size) varies across observations.

The critical assumption of Poisson regression is **equidispersion**: the variance of the outcome equals its mean. In practice, this assumption is frequently violated — real count data often exhibit **overdispersion** (variance > mean) due to unobserved heterogeneity, clustering, or excess zeros. When overdispersion is present, the model's standard errors are too small, producing artificially narrow confidence intervals and inflated significance. Diagnostics include comparing the residual deviance to the degrees of freedom (a ratio much greater than 1 suggests overdispersion). Solutions include quasi-Poisson estimation (which scales standard errors by a dispersion parameter), negative binomial regression (which adds a parameter for overdispersion), or zero-inflated models when the excess variance comes specifically from too many zeros.
