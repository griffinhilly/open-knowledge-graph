---
id: structural-equation-modeling-measurement
title: 'Structural Equation Modeling: Measurement and Structural Components'
domain: psychology
course: psychometrics
prerequisites:
- id: confirmatory-factor-analysis
  type: hard
- id: linear-algebra applications
  type: hard
- id: linear-transformation-matrix-representation
  type: soft
- id: linear-algebra
  type: hard
- id: matrix-operations
  type: hard
builds-toward:
- differential-item-functioning
tags:
- sem
- measurement-model
- structural-model
- latent-variables
stage: expert
status: validated
---

# Structural Equation Modeling: Measurement and Structural Components

## Core Idea
SEM integrates measurement models (latent variables' relationships to observed items) with structural models (latent variables' relationships to each other). It simultaneously estimates factor loadings, item residuals, and structural parameters, providing comprehensive evaluation of measurement quality and theoretical relationships.

## Questions

```yaml
- question: "A researcher regresses observed 'cognitive ability' test scores on observed 'academic motivation' scores to estimate their relationship. A reviewer recommends SEM instead. What specific problem does SEM address that regression cannot?"
  type: multiple-choice
  options:
    - "SEM automatically controls for all possible confounding variables"
    - "Regression on error-contaminated observed composites attenuates the coefficient toward zero; SEM estimates paths between true-score constructs by explicitly partitioning measurement error in the measurement model first"
    - "SEM always produces smaller standard errors, yielding more precise estimates"
    - "Regression cannot handle the non-normal distributions common in psychological data"
  answer: 1
  explanation: "When you regress one error-contaminated observed composite on another, measurement error in both variables attenuates (biases toward zero) the regression coefficient — you systematically underestimate the true relationship between the constructs. SEM avoids this by modeling measurement error explicitly in the CFA layer before estimating structural paths, so the paths reflect relationships between the underlying true-score latent variables. Options A and C describe properties SEM does not reliably provide; option D is unrelated to why regression fails here."

- question: "Two SEM models are fitted to the same data: Model A has a path X → Y; Model B has Y → X. Both produce identical χ², RMSEA, and CFI values. What can be concluded?"
  type: multiple-choice
  options:
    - "Model A is correct because the researcher's original theory specified that direction"
    - "Causal direction cannot be determined from covariance data alone; design-level evidence (experiments, longitudinal ordering) is required to distinguish the models"
    - "The models are mathematically equivalent, so both must be rejected as unidentified"
    - "The model with stronger theoretical justification should be reported as the confirmed causal structure"
  answer: 1
  explanation: "This is the equivalent models problem. Covariance data do not carry directional information — two models with arrows pointing in opposite directions can imply identical covariance structures and fit identically. Good fit means the data are consistent with a causal structure, not that the structure is proven. Establishing causal direction requires experimental manipulation, temporal ordering in longitudinal designs, or natural experiments. Option D is appealing but conflates theoretical plausibility with empirical proof — consistency is not confirmation."

- question: "In SEM, a model with more free parameters always fits the observed covariance data at least as well as a more constrained model."
  type: true-false
  answer: true
  explanation: "A saturated model — one with as many free parameters as unique covariance elements — achieves perfect fit by construction (χ² = 0) because it imposes no constraints on the data. Every constraint added (parameters fixed to zero or set equal) forces the implied covariance matrix to depart from the observed one, worsening fit. More constrained models fit worse but are more theoretically informative — they make falsifiable predictions. Fit is always evaluated relative to the constraints imposed by the researcher's theory."

- question: "A well-fitting SEM model estimated from cross-sectional observational data establishes that the hypothesized causal relationships between latent variables are correct."
  type: true-false
  answer: false
  explanation: "Good fit means the data are *consistent* with the hypothesized causal structure — not that the structure is proven. The equivalent models problem shows that models with different causal directions can fit identically. Causation requires design-level evidence: random assignment, temporal precedence in longitudinal data, or natural experiments. SEM is a confirmatory tool for evaluating consistency, not a method for discovering causation from observational data. Distinguishing 'consistent with' from 'proved by' is the most critical reading skill for SEM consumers."

- question: "What does it mean to say SEM separates the 'measurement model' from the 'structural model,' and why does this separation matter for estimating relationships between constructs?"
  type: short-answer
  answer: "The measurement model (the CFA layer) specifies how observed indicators load onto latent constructs, explicitly partitioning each indicator's variance into true-score and error components. The structural model then specifies directional paths between the latent constructs themselves — estimated after measurement error has been accounted for. This separation matters because it allows structural paths to be estimated between error-free constructs, correcting the attenuation bias that occurs when observable composites are used directly in regression."
  explanation: "Without the measurement model, regressing observed composites on each other underestimates relationships because error in both variables biases coefficients toward zero. By modeling error explicitly first, SEM recovers the relationships between the underlying theoretical constructs. The separation also allows simultaneous evaluation of measurement quality (are items loading as theorized?) and theoretical claims (do constructs relate as hypothesized?), something regression of observed variables cannot do."
```

## Explainer

From confirmatory factor analysis, you know how to specify a model where latent variables (factors) explain the covariances among observed indicators, estimate factor loadings, evaluate model fit, and test whether a hypothesized factor structure is consistent with data. CFA treats the latent variables as end points — it answers the measurement question ("do these indicators cohere as hypothesized?") but says nothing about how the latent variables relate to *each other*. **Structural equation modeling** extends CFA by adding a second layer: the **structural model**, which specifies directional relationships among the latent variables themselves, complete with path coefficients, mediated effects, and residual variances.

Think of SEM as two simultaneous models. The **measurement model** is essentially CFA: observed indicators load onto latent variables via factor loadings (λ), and each indicator retains a residual (δ) representing variance not explained by the latent construct. The **structural model** then treats the latent variables as nodes in a directed path diagram, with regression-like coefficients (β or γ) linking them. The critical advantage over running a regression on observed composite scores is that structural relationships are modeled between **true-score constructs**, not error-contaminated observed variables. When you regress one observed composite on another, measurement error attenuates the regression coefficient — you systematically underestimate the relationship. SEM corrects for this attenuation by explicitly partitioning measurement error in the measurement model before estimating structural paths.

The matrix algebra prerequisite comes into play because SEM estimation is fundamentally a covariance structure problem. The model implies a predicted covariance matrix **Σ(θ)** — a function of all free parameters (loadings, structural paths, residuals, factor variances). The estimation algorithm minimizes the discrepancy between **Σ(θ)** and the empirical sample covariance matrix **S**. Maximum likelihood estimation finds the parameter values that minimize a fit function based on the log-determinant of the discrepancy. Fit statistics — χ², RMSEA, CFI, SRMR — each measure a different aspect of how well the implied matrix matches the observed one. Perfect fit (χ² = 0) only occurs when the model is saturated (has as many free parameters as unique covariance elements), so fit is always evaluated relative to the constraints the researcher imposed. A simpler, more constrained model fits worse but is more informative theoretically.

A conceptual warning worth internalizing: SEM does not establish causation from observational data alone. The arrows in a structural model represent *a priori* hypothesized directional relationships — they encode the researcher's theory, not empirically demonstrated causal mechanisms. Two models with arrows pointing in opposite directions between the same two latent variables can fit observed covariance data equally well (they are **equivalent models**). Causation requires design-level evidence: experimental manipulation, longitudinal temporal ordering, or natural experiments. SEM tests whether data are *consistent* with a causal structure, which is valuable evidence — but consistency is not proof. Distinguishing "the data do not contradict my causal model" from "my causal model is correct" is the most important critical reading skill for SEM research consumers.
