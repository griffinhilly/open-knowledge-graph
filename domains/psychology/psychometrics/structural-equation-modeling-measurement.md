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
stage: advanced
status: draft
---

# Structural Equation Modeling: Measurement and Structural Components

## Core Idea
SEM integrates measurement models (latent variables' relationships to observed items) with structural models (latent variables' relationships to each other). It simultaneously estimates factor loadings, item residuals, and structural parameters, providing comprehensive evaluation of measurement quality and theoretical relationships.

## Explainer

From confirmatory factor analysis, you know how to specify a model where latent variables (factors) explain the covariances among observed indicators, estimate factor loadings, evaluate model fit, and test whether a hypothesized factor structure is consistent with data. CFA treats the latent variables as end points — it answers the measurement question ("do these indicators cohere as hypothesized?") but says nothing about how the latent variables relate to *each other*. **Structural equation modeling** extends CFA by adding a second layer: the **structural model**, which specifies directional relationships among the latent variables themselves, complete with path coefficients, mediated effects, and residual variances.

Think of SEM as two simultaneous models. The **measurement model** is essentially CFA: observed indicators load onto latent variables via factor loadings (λ), and each indicator retains a residual (δ) representing variance not explained by the latent construct. The **structural model** then treats the latent variables as nodes in a directed path diagram, with regression-like coefficients (β or γ) linking them. The critical advantage over running a regression on observed composite scores is that structural relationships are modeled between **true-score constructs**, not error-contaminated observed variables. When you regress one observed composite on another, measurement error attenuates the regression coefficient — you systematically underestimate the relationship. SEM corrects for this attenuation by explicitly partitioning measurement error in the measurement model before estimating structural paths.

The matrix algebra prerequisite comes into play because SEM estimation is fundamentally a covariance structure problem. The model implies a predicted covariance matrix **Σ(θ)** — a function of all free parameters (loadings, structural paths, residuals, factor variances). The estimation algorithm minimizes the discrepancy between **Σ(θ)** and the empirical sample covariance matrix **S**. Maximum likelihood estimation finds the parameter values that minimize a fit function based on the log-determinant of the discrepancy. Fit statistics — χ², RMSEA, CFI, SRMR — each measure a different aspect of how well the implied matrix matches the observed one. Perfect fit (χ² = 0) only occurs when the model is saturated (has as many free parameters as unique covariance elements), so fit is always evaluated relative to the constraints the researcher imposed. A simpler, more constrained model fits worse but is more informative theoretically.

A conceptual warning worth internalizing: SEM does not establish causation from observational data alone. The arrows in a structural model represent *a priori* hypothesized directional relationships — they encode the researcher's theory, not empirically demonstrated causal mechanisms. Two models with arrows pointing in opposite directions between the same two latent variables can fit observed covariance data equally well (they are **equivalent models**). Causation requires design-level evidence: experimental manipulation, longitudinal temporal ordering, or natural experiments. SEM tests whether data are *consistent* with a causal structure, which is valuable evidence — but consistency is not proof. Distinguishing "the data do not contradict my causal model" from "my causal model is correct" is the most important critical reading skill for SEM research consumers.
