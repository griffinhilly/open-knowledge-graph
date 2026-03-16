---
id: structural-equation-modeling-latent
title: Structural Equation Modeling with Latent Variables
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: linear-regression-social-science
  type: hard
- id: factor-analysis-dimensionality
  type: soft
- id: eigenvalues-eigenvectors
  type: hard
- id: matrix-operations
  type: hard
- id: basis-and-dimension
  type: soft
- id: eigenvalues-and-eigenvectors
  type: soft
- id: matrices-intro
  type: soft
tags:
- SEM
- latent-variables
- path-analysis
- confirmatory-factor-analysis
stage: advanced
status: draft
---

# Structural Equation Modeling with Latent Variables

## Core Idea
Introduces SEM as a comprehensive framework for testing theories with latent variables and indirect effects. Covers path analysis, measurement models, structural models, and model fit assessment. Enables testing complex theories against observed survey data with attention to measurement error.

## How It's Best Learned
Develop a path model from theory, estimate measurement and structural components, evaluate fit indices and modification indices, practice interpretation of direct and indirect effects.

## Common Misconceptions
- Latent variables are just factors
- Good fit means the theory is correct
- Modification indices tell you what to do theoretically

## Explainer

Structural equation modeling is best understood as the combination of two models you already know: a **measurement model** (confirmatory factor analysis, which you covered in factor analysis) and a **structural model** (a system of regression equations). The measurement model specifies how observable survey items relate to underlying latent constructs — "trust in institutions" might be measured by four items that each load on one latent factor. The structural model then specifies causal or predictive relationships among those latent constructs — "socioeconomic status predicts institutional trust, which predicts civic participation." SEM estimates both models simultaneously, which is its main advantage: it accounts for measurement error in the predictors, something ordinary regression cannot do.

A **path diagram** is the visual grammar of SEM. Rectangles represent observed variables (the actual survey items). Ovals represent latent variables (the unmeasured constructs). Single-headed arrows represent directional effects (regression paths). Double-headed curved arrows represent covariances or correlations without a hypothesized direction. The diagram encodes your theoretical model before you look at any data, and that prior commitment is what makes SEM a confirmatory rather than exploratory technique. You're not fishing for what predicts what — you're testing a specific set of claims against the observed covariance matrix.

Model **fit** is assessed by comparing the covariance matrix implied by your model to the observed covariance matrix in your data. If the model fits well, the discrepancy is small. Common indices include the CFI and TLI (values above .95 suggest good fit), RMSEA (values below .06 suggest good fit), and SRMR. The critical misconception is treating good fit as proof of your theory. Good fit means your model is *consistent* with the data — but many alternative models can also fit the same data. A model can fit perfectly and be theoretically wrong. Similarly, **modification indices** tell you which fixed parameters (paths you set to zero) would improve fit if freed, but they say nothing about whether freeing them makes theoretical sense. Chasing modification indices produces models optimized to a specific sample, not to theory.

**Indirect effects** are one of SEM's most powerful capabilities. In a mediation model — where X → M → Y — you can estimate the path from X to Y that runs *through* M (the indirect effect) separately from the direct path X → Y. Multiplying the X→M coefficient by the M→Y coefficient gives the indirect effect. SEM with bootstrapped confidence intervals is now the standard approach for testing mediation, replacing the older Baron-Kenny stepwise procedure. This is especially valuable in social science, where most causal processes are mediated through multiple constructs — education affects health partly through income, partly through health behaviors, and partly through psychological resources — and SEM lets you decompose these pathways systematically.
