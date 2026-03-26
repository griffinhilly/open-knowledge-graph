---
id: confirmatory-factor-analysis
title: Confirmatory Factor Analysis and Measurement Validation
domain: psychology
course: psychometrics
prerequisites:
- id: factor-analysis-measurement
  type: hard
- id: linear-algebra
  type: hard
- id: eigenvalues-and-eigenvectors
  type: soft
- id: eigenvalues-and-eigenvectors
  type: hard
- id: matrix-operations
  type: hard
builds-toward:
- structural-equation-modeling-measurement
- validity-evidence-frameworks
tags:
- cfa
- confirmatory
- measurement-model
- fit-indices
stage: expert
status: validated
---

# Confirmatory Factor Analysis and Measurement Validation

## Core Idea
Confirmatory factor analysis tests whether data fit a pre-specified measurement model, directly evaluating whether items measure intended constructs. Fit indices (CFI, RMSEA, SRMR) and factor loadings assess model adequacy, making CFA essential for validating test structure and detecting unintended multidimensionality.

## How It's Best Learned
Specify competing measurement models based on theory and compare fit statistics. Examine modification indices to understand when respecification is theory-driven versus exploratory.

## Common Misconceptions
All fit indices should exceed arbitrary cutoffs. Each index has different sensitivity; using multiple indices addresses different aspects of fit. Good fit alone doesn't guarantee validity; it's necessary but insufficient.

## Questions

```yaml
- question: "A researcher specifies a CFA model in which all six items on a depression scale load onto a single latent factor. The model returns CFI = 0.96 and RMSEA = 0.05. What does this primarily indicate?"
  type: multiple-choice
  options: ["The depression items are uncorrelated with each other", "The hypothesized one-factor structure fits the data well", "The scale measures depression better than any alternative scale", "The factor loadings are all statistically significant"]
  answer: 1
  explanation: "CFI close to 1.0 and RMSEA below 0.06 are conventional thresholds indicating the pre-specified model fits the observed covariance structure well. Good fit means the proposed factor structure is plausible — it does not speak to item correlations, comparative validity, or individual loading significance."

- question: "A CFA model with CFI = 0.97 and RMSEA = 0.04 is sufficient evidence to conclude that a scale validly measures the intended construct."
  type: true-false
  answer: false
  explanation: "Good model fit is necessary but not sufficient for construct validity. Fit indices only evaluate whether the factor structure matches the data's covariance pattern — they say nothing about whether the latent factor actually corresponds to the intended real-world construct. External validity evidence (convergent, discriminant, criterion-related) is still required."

- question: "What is the fundamental difference between exploratory factor analysis (EFA) and confirmatory factor analysis (CFA)?"
  type: short-answer
  answer: "EFA discovers factor structure from data without prior specification; CFA tests whether data fit a theoretically pre-specified factor structure."
  explanation: "In EFA, the researcher lets the analysis determine how many factors exist and which items load on which factors. In CFA, the researcher specifies the number of factors, which items load on each factor, and (often) which cross-loadings are constrained to zero — then tests whether this theory-driven model fits the observed covariance matrix. CFA is hypothesis-testing; EFA is hypothesis-generating."
```

## Explainer

Confirmatory factor analysis is the tool you use when you already have a theory about how a set of items should cluster. Whereas exploratory factor analysis lets the data reveal structure, CFA works in reverse: you specify a measurement model first — based on theory or prior EFA results — and then ask whether that model is consistent with the observed pattern of correlations among items. If you believe six questionnaire items all measure a single construct called "depression," CFA lets you test that claim directly against data.

The core operation in CFA is comparing two covariance matrices: the one actually observed in your sample, and the one your model implies should exist if the factor structure is correct. The difference between these matrices is your residual. Fit indices summarize how large that residual is. The CFI (Comparative Fit Index) compares your model to a null model where variables are uncorrelated — values above 0.95 suggest good fit. The RMSEA (Root Mean Square Error of Approximation) estimates the error per degree of freedom — values below 0.06 are conventionally acceptable. The SRMR (Standardized Root Mean Square Residual) reflects average discrepancy between observed and model-implied correlations — below 0.08 is typical. No single index tells the whole story; you look at all three together, and you look at modification indices to understand which specific constraints the model is straining against.

The most important misconception to guard against is equating good fit with validity. A CFA model can fit beautifully and still measure the wrong thing. Fit only tells you that the factor structure is internally consistent — not that the factor corresponds to a real and meaningful construct. To make validity claims, you need convergent evidence (does the scale correlate with other measures it should correlate with?) and discriminant evidence (does it fail to correlate with measures it shouldn't?). CFA is the foundation of measurement validation, not the whole edifice.

CFA also enables powerful model comparison. You can test a one-factor model against a two-factor model and use likelihood ratio tests or AIC/BIC comparisons to evaluate which structure fits better. This is how researchers test whether, for example, anxiety and depression are best represented as one undifferentiated factor or two related but distinct constructs. The ability to pit competing theories against each other — rather than letting data suggest structure post hoc — is what makes CFA a cornerstone of modern psychometrics.
