---
id: factor-analysis-measurement
title: Factor Analysis and Measurement Models
domain: psychology
course: psychometrics
prerequisites:
- id: classical-test-theory
  type: hard
- id: eigenvalues-eigenvectors
  type: soft
- id: eigenvalues-and-eigenvectors
  type: soft
- id: linear-transformations-definition
  type: soft
- id: linear-algebra
  type: hard
- id: basis-and-dimension
  type: hard
builds-toward:
- confirmatory-factor-analysis
- structural-equation-modeling-measurement
tags:
- factor-analysis
- exploratory
- latent-variables
- dimensionality
stage: advanced
status: draft
---

# Factor Analysis and Measurement Models

## Core Idea
Factor analysis identifies underlying latent constructs from correlations among observed variables. In measurement contexts, exploratory factor analysis reveals whether items measure one or multiple dimensions, while factor loadings indicate item quality and dimensionality structure.

## Explainer

From classical test theory, you know that any observed score is a combination of true score and error. Factor analysis extends this logic to a more fundamental question: when you have many observed variables (test items, survey responses, behavioral ratings), how many underlying constructs do they actually measure? The method works by examining the pattern of correlations: items that correlate strongly with each other but weakly with other items are likely measuring the same underlying thing. Factor analysis identifies and names those clusters — the **latent factors** — which are not directly observed but inferred from the co-variation pattern in the data.

The mathematical engine behind factor analysis draws on linear algebra you've already studied. Each **factor** is a weighted linear combination of observed variables, and each **factor loading** is the correlation between an observed variable and the latent factor. A loading of .80 means the item shares 64% of its variance with the factor (the square of the loading, called **communality**). A loading of .20 means the item barely connects to the factor. From your work with eigenvalues, you know they represent the amount of variance a linear transformation captures — in factor analysis, factors with eigenvalues greater than 1.0 (Kaiser criterion) capture more variance than any single observed variable, making them meaningful candidates for interpretation. Factors are extracted in order from most to least variance explained.

**Exploratory factor analysis (EFA)** is the data-driven form: you let the correlations determine the factor structure without imposing a prior theory. This is useful when you're developing a new scale or exploring whether a construct is one-dimensional or multidimensional. Suppose you write 20 items about "wellbeing" and run an EFA. If the items load onto two factors — one clustering around hedonic pleasure items, the other around meaning and purpose items — the analysis is telling you that "wellbeing" as you've operationalized it may have two distinct components, and you should either refine your theory or your scale. If all 20 items load onto a single factor, you have evidence for unidimensionality.

The practical output that matters most is the **factor loading matrix**: a table of every item's loading on every factor. Strong, clean loadings (close to ±1 on one factor, near zero on others) indicate a well-defined, interpretable structure. High **cross-loadings** — an item loading significantly on two or more factors — signal that the item is ambiguous and may need to be revised or dropped. **Rotation** (orthogonal like varimax, or oblique like promax) is applied after extraction to make the factor structure more interpretable; rotation doesn't change the total variance explained, only how it's partitioned across factors.

Factor analysis sits at the foundation of most psychological measurement: intelligence tests, personality inventories, diagnostic criteria, and attitude scales all rest on factor-analytic evidence for their dimensionality. The distinction between EFA (exploratory) and confirmatory factor analysis (which tests a pre-specified model) is one of the most important methodological forks in quantitative psychology — EFA generates hypotheses about structure, while CFA tests them. What you learn here about how latent factors are identified from observed correlations becomes the foundation for structural equation modeling, where entire networks of constructs and their relationships are modeled simultaneously.
