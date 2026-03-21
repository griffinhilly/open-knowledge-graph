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

## Questions

```yaml
- question: "A researcher builds an SEM with CFI = .97 and RMSEA = .04 and concludes: 'These fit indices confirm that my theory of how socioeconomic status influences civic participation through institutional trust is correct.' What is wrong with this conclusion?"
  type: multiple-choice
  options:
    - "The CFI threshold for confirmation is .99, not .95"
    - "Good fit only shows the model is consistent with the data — many alternative models could fit equally well"
    - "RMSEA must be below .03 for any theoretical conclusion to be valid"
    - "SEM cannot test mediation models, so the conclusion is procedurally invalid"
  answer: 1
  explanation: "Good fit means your model's implied covariance matrix closely matches the observed covariance matrix — it means your model is *consistent* with the data, not that it is correct. Multiple theoretically different models can fit the same data equally well. A model can achieve excellent fit while encoding wrong theoretical assumptions; equivalently, a correct theory might fit poorly if it is mis-specified. This is the central epistemological limitation of SEM: fit is necessary but not sufficient evidence for a theory."

- question: "What is SEM's primary advantage over ordinary multiple regression when predictors are psychological constructs measured by survey items?"
  type: multiple-choice
  options:
    - "SEM produces larger R-squared values by including more variables simultaneously"
    - "SEM explicitly models measurement error in latent variables, yielding unbiased structural coefficients"
    - "SEM does not require multivariate normality, making it more robust"
    - "SEM generates larger sample sizes through data imputation"
  answer: 1
  explanation: "When you regress one observed variable on others, any measurement error in the predictors biases the regression coefficients toward zero (attenuation bias). SEM solves this by distinguishing the latent variable (the true construct) from its observed indicators, explicitly modeling the measurement error in each indicator. The structural paths then connect the latent variables — purged of measurement error — so the coefficients are unbiased estimates of the true relationships. This is the main advantage over ordinary regression for psychological and social science constructs."

- question: "When SEM modification indices indicate that freeing a fixed parameter (adding a path) would improve model fit, this tells the researcher which paths are theoretically meaningful and should be added."
  type: true-false
  answer: false
  explanation: "Modification indices are purely statistical: they report how much the chi-square fit statistic would decrease if a currently-fixed parameter were freed. They say nothing about whether that parameter makes theoretical sense. Chasing modification indices produces models that are over-fit to a specific sample rather than to a theory — they capitalize on chance variation in the data and will not replicate. Adding paths based on modification indices alone is a form of post-hoc data dredging that undermines SEM's confirmatory purpose."

- question: "In SEM, estimating the measurement model and structural model simultaneously allows the structural paths to account for measurement error in the latent constructs."
  type: true-false
  answer: true
  explanation: "This simultaneous estimation is what distinguishes SEM from a two-step approach (first factor analysis, then regression on factor scores). When both models are estimated together, the structural paths connect latent variables whose measurement error is explicitly modeled — giving unbiased estimates of the relationships among the true underlying constructs. Estimating separately would introduce bias because factor scores themselves carry residual measurement error."

- question: "Why is good model fit in SEM not sufficient evidence that a theoretical model is correct, even when fit indices like CFI and RMSEA meet recommended thresholds?"
  type: short-answer
  answer: "Good fit means the model's implied covariance matrix is consistent with the observed data — but there are always multiple models that can produce the same covariance structure. Two models with opposite causal directions, or with entirely different mediating variables, can be statistically equivalent — they fit identically and cannot be distinguished by fit indices alone. Additionally, a model can fit because it is flexible enough to accommodate the data even if its theoretical claims are wrong. Fit is a necessary but not sufficient condition for theoretical validity; substantive interpretation, experimental replication, and alternative model comparison are also required."
  explanation: "This connects to the broader principle that statistical consistency is not causal identification. SEM is a confirmatory technique, but 'confirmatory' means you've committed to a structure before looking at data — it doesn't mean the structure is uniquely supported. The remedy is triangulation: reporting alternative equivalent models, using longitudinal data to test temporal order, replicating in independent samples, and treating good fit as 'not yet falsified' rather than 'confirmed.'"
```

## Explainer

Structural equation modeling is best understood as the combination of two models you already know: a **measurement model** (confirmatory factor analysis, which you covered in factor analysis) and a **structural model** (a system of regression equations). The measurement model specifies how observable survey items relate to underlying latent constructs — "trust in institutions" might be measured by four items that each load on one latent factor. The structural model then specifies causal or predictive relationships among those latent constructs — "socioeconomic status predicts institutional trust, which predicts civic participation." SEM estimates both models simultaneously, which is its main advantage: it accounts for measurement error in the predictors, something ordinary regression cannot do.

A **path diagram** is the visual grammar of SEM. Rectangles represent observed variables (the actual survey items). Ovals represent latent variables (the unmeasured constructs). Single-headed arrows represent directional effects (regression paths). Double-headed curved arrows represent covariances or correlations without a hypothesized direction. The diagram encodes your theoretical model before you look at any data, and that prior commitment is what makes SEM a confirmatory rather than exploratory technique. You're not fishing for what predicts what — you're testing a specific set of claims against the observed covariance matrix.

Model **fit** is assessed by comparing the covariance matrix implied by your model to the observed covariance matrix in your data. If the model fits well, the discrepancy is small. Common indices include the CFI and TLI (values above .95 suggest good fit), RMSEA (values below .06 suggest good fit), and SRMR. The critical misconception is treating good fit as proof of your theory. Good fit means your model is *consistent* with the data — but many alternative models can also fit the same data. A model can fit perfectly and be theoretically wrong. Similarly, **modification indices** tell you which fixed parameters (paths you set to zero) would improve fit if freed, but they say nothing about whether freeing them makes theoretical sense. Chasing modification indices produces models optimized to a specific sample, not to theory.

**Indirect effects** are one of SEM's most powerful capabilities. In a mediation model — where X → M → Y — you can estimate the path from X to Y that runs *through* M (the indirect effect) separately from the direct path X → Y. Multiplying the X→M coefficient by the M→Y coefficient gives the indirect effect. SEM with bootstrapped confidence intervals is now the standard approach for testing mediation, replacing the older Baron-Kenny stepwise procedure. This is especially valuable in social science, where most causal processes are mediated through multiple constructs — education affects health partly through income, partly through health behaviors, and partly through psychological resources — and SEM lets you decompose these pathways systematically.
