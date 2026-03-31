---
id: mixed-effects-models-biostatistics
title: Mixed-Effects Models in Biostatistics
domain: health-and-human-development
course: biostatistics
prerequisites:
- id: linear-regression
  type: hard
- id: logistic-regression-biostatistics
  type: soft
- id: study-design-biostatistics
  type: soft
builds-toward:
- joint-longitudinal-survival-models
- generalized-estimating-equations
tags:
- mixed-effects
- random-effects
- hierarchical
- longitudinal
- repeated-measures
- multilevel
stage: expert
status: validated
---

# Mixed-Effects Models in Biostatistics

## Core Idea
Mixed-effects models (also called hierarchical or multilevel models) handle data with natural grouping structures — repeated measurements on the same patient, patients nested within hospitals, or students within schools. They include both fixed effects (population-average effects of predictors, the same for everyone) and random effects (subject-specific deviations that account for the correlation among observations within the same cluster). A random intercept allows each subject's baseline to differ; a random slope allows each subject's response to a predictor to differ. By explicitly modeling the within-cluster correlation, mixed-effects models produce correct standard errors (unlike ordinary regression, which treats all observations as independent), efficiently borrow strength across clusters, and provide subject-specific predictions that are shrunk toward the population mean.

## Questions

```yaml
- question: "A study measures blood pressure at 6 time points for each of 200 patients after initiating antihypertensive treatment. Why would a standard linear regression of blood pressure on time be inappropriate?"
  type: multiple-choice
  options:
    - "Linear regression cannot handle time as a predictor"
    - "The 6 observations from each patient are correlated (not independent), violating the independence assumption of standard regression, which produces incorrect standard errors"
    - "Linear regression requires at least 10 observations per patient"
    - "Blood pressure is not normally distributed"
  answer: 1
  explanation: "Standard linear regression assumes all observations are independent, but repeated measures on the same patient are correlated — Patient A's blood pressures cluster together because of shared genetics, lifestyle, and physiology. Ignoring this correlation produces standard errors that are too small (because the effective sample size is not 1,200 independent observations but something closer to 200 independent patients), leading to inflated Type I error rates. A mixed-effects model with random intercepts (and potentially random slopes) explicitly accounts for within-patient correlation."

- question: "In a mixed-effects model with a random intercept for patient, the random intercept captures between-patient variability in baseline levels. What additional structure does a random slope for time add?"
  type: short-answer
  answer: "A random slope for time allows each patient to have a different rate of change over time, not just a different starting point. Some patients' blood pressure may decline rapidly while others decline slowly or not at all. Without a random slope, the model assumes all patients change at the same rate (the fixed slope) and differ only in their starting level. The random slope captures heterogeneity in treatment response across patients."
  explanation: "The random slope introduces a correlation between intercept and slope — patients who start higher might decline more (or less), and this correlation is estimated from the data. The covariance matrix of the random effects (intercept variance, slope variance, and their correlation) characterizes the population-level heterogeneity in trajectories, which is often of primary scientific interest."

- question: "Mixed-effects model predictions for individual clusters are 'shrunk' toward the population mean. This shrinkage is a defect of the method that should be corrected."
  type: true-false
  answer: false
  explanation: "Shrinkage is a feature, not a defect. Subject-specific estimates from a mixed-effects model are empirical Bayes predictions that blend the individual's data with the population average. Subjects with more observations or less noisy data are shrunk less (their data are more informative), while subjects with few observations are shrunk more toward the population mean. This regularization reduces the mean squared error of individual predictions by trading a small bias for a large reduction in variance — the same principle that makes Bayesian and ridge regression estimators more accurate than unbiased estimates in many settings."

- question: "A researcher has data on 50 hospitals, each contributing 10-100 patients. She runs a standard regression with hospital as a fixed effect (49 dummy variables) instead of a random effect. What are the consequences?"
  type: multiple-choice
  options:
    - "No consequences — the two approaches give identical results"
    - "Fixed hospital effects use 49 degrees of freedom, cannot predict for new hospitals, cannot estimate between-hospital variance, and provide unreliable estimates for hospitals with few patients"
    - "Random effects are only valid when there are at least 100 groups"
    - "Fixed effects are always preferred because they make fewer assumptions"
  answer: 1
  explanation: "Fixed hospital effects consume many degrees of freedom, especially problematic with many hospitals. They provide no shrinkage, so hospitals with 10 patients get the same weight as hospitals with 100, producing noisy estimates. They cannot generalize to new hospitals (the estimates are specific to observed hospitals only) and do not estimate the between-hospital variance component, which is often of scientific interest. Random effects treat hospitals as a sample from a larger population, estimate the between-hospital variance, shrink small-sample hospitals toward the mean, and use far fewer parameters (variance components instead of dummy variables)."
```

## Explainer

Health data almost always has structure. Patients are measured repeatedly over time (longitudinal data), patients are treated in hospitals that vary in quality (nested data), and clinical trials recruit from multiple centers (clustered data). In all these settings, observations within the same group are more similar to each other than observations across groups. Standard regression assumes independence and will produce **incorrect standard errors** — typically too small — when this correlation exists, leading to false confidence in results.

**Mixed-effects models** handle this by introducing **random effects** — subject-specific (or cluster-specific) parameters drawn from a population distribution. A random intercept for patient assumes each patient has their own baseline level, drawn from a normal distribution centered on the population mean. A random slope for time assumes each patient has their own rate of change. Together, these define a family of patient-specific trajectories that share a common structure but vary around it. The fixed effects capture the population-average relationship (the mean trajectory), while the random effects capture how individual trajectories deviate from it.

Estimation of mixed-effects models uses **restricted maximum likelihood** (REML) or full maximum likelihood. REML produces less biased estimates of variance components and is the default in most software. The individual-level predictions (Best Linear Unbiased Predictions, or BLUPs) combine each subject's own data with the population-level estimates, weighted by the relative precision of each. A subject with many measurements gets a prediction close to their own data; a subject with few measurements gets a prediction pulled ("shrunk") toward the population mean. This **shrinkage** is not a limitation — it is a statistically optimal way to handle the varying information content across subjects.

The choice between random intercepts only, random intercepts and slopes, and more complex random effects structures is driven by the data and the research question. Likelihood ratio tests, AIC, and BIC can compare nested models. The key practical considerations are: does the model converge? (Complex random effects structures with many correlated parameters may fail to converge with limited data.) Do the random effects make scientific sense? (A random slope for treatment group requires that treatment effects truly vary across clusters, not just baseline levels.) And is the random effects distribution reasonable? (The standard assumption is multivariate normal; severe departures may require robust or non-parametric alternatives.)
