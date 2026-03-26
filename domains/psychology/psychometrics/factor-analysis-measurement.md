---
id: factor-analysis-measurement
title: Factor Analysis and Measurement Models
domain: psychology
course: psychometrics
prerequisites:
- id: classical-test-theory
  type: hard
- id: eigenvalues-and-eigenvectors
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
stage: expert
status: validated
---

# Factor Analysis and Measurement Models

## Core Idea
Factor analysis identifies underlying latent constructs from correlations among observed variables. In measurement contexts, exploratory factor analysis reveals whether items measure one or multiple dimensions, while factor loadings indicate item quality and dimensionality structure.

## Questions

```yaml
- question: "An item on a wellbeing scale has a loading of .32 on Factor 1 (hedonic pleasure) and .38 on Factor 2 (meaning and purpose). What is the most appropriate action?"
  type: multiple-choice
  options:
    - "Keep the item — loadings above .30 on any factor indicate it is measuring something meaningful"
    - "Assign the item to whichever factor has the higher loading and proceed"
    - "Flag the item as having a high cross-loading and consider revising or dropping it, as it does not clearly measure either construct"
    - "Apply oblique rotation to force the item onto a single factor"
  answer: 2
  explanation: "High cross-loadings — significant loadings on two or more factors simultaneously — indicate an ambiguous item that does not clearly measure any single construct. Such an item clouds the factor structure and makes the constructs harder to interpret and name. The goal of factor analysis in scale development is simple structure: high loadings on one factor and near-zero loadings on others. Rotation (oblique or orthogonal) can improve interpretability but cannot rescue a genuinely ambiguous item."

- question: "In exploratory factor analysis, a factor with an eigenvalue greater than 1.0 (the Kaiser criterion) is typically retained. What does the eigenvalue represent in this context?"
  type: multiple-choice
  options:
    - "The average correlation among items loading on that factor"
    - "The number of items that load significantly on the factor"
    - "The amount of total variance in the observed variables that the factor accounts for, measured in units of a single variable's variance"
    - "The probability that the factor reflects a true latent construct rather than random noise"
  answer: 2
  explanation: "Eigenvalues in factor analysis represent the variance explained by a factor, measured in units of the variance of a single standardized variable (which equals 1). A factor with eigenvalue > 1 explains more variance than any single observed variable, justifying its retention as a meaningful summary. Eigenvalue ≤ 1 means the factor explains less than one variable's worth of variance — adding it explains nothing useful beyond what's already in the data."

- question: "Applying rotation (varimax or promax) to extracted factors changes the total variance explained by the factor solution."
  type: true-false
  answer: false
  explanation: "Rotation redistributes variance among factors but preserves total variance explained. Think of rotation as rotating the coordinate axes in factor space: the data points (item positions) don't change, only the axes used to describe them. Varimax (orthogonal) and promax (oblique) rotations reapportion the variance differently across factors to improve interpretability — making some loadings larger and others smaller — without changing the total communality. This is why rotation is about interpretability, not fit."

- question: "A factor loading of .70 means the factor accounts for 70% of that item's variance."
  type: true-false
  answer: false
  explanation: "A loading of .70 means the item correlates .70 with the factor. The proportion of variance explained (communality from that factor) is the squared loading: .70² = .49, or 49%. This is analogous to r² in regression. The loading itself is a correlation, not a proportion of variance. Students frequently confuse the loading with r² — always square the loading to get the variance explained."

- question: "Why does a well-designed psychological scale want items with high loadings on one factor and near-zero loadings on all others?"
  type: short-answer
  answer: "High loadings on one factor indicate the item strongly and specifically measures that underlying construct. Near-zero loadings on other factors indicate the item is not contaminated by other constructs. This 'simple structure' makes the factors interpretable (each factor has a clear identity), the scale unidimensional (all items measure the same thing), and scores on the scale a valid reflection of the target construct rather than a blend of multiple constructs."
  explanation: "This is the measurement validity argument. If an item loads on two factors, its observed responses reflect a mixture of two latent constructs, making it impossible to know which construct it is measuring. A scale built on such items produces scores that are ambiguous composites. Simple structure — each item loading on one factor — means each factor can be cleanly named and each item unambiguously contributes to exactly one construct's measurement."
```

## Explainer

From classical test theory, you know that any observed score is a combination of true score and error. Factor analysis extends this logic to a more fundamental question: when you have many observed variables (test items, survey responses, behavioral ratings), how many underlying constructs do they actually measure? The method works by examining the pattern of correlations: items that correlate strongly with each other but weakly with other items are likely measuring the same underlying thing. Factor analysis identifies and names those clusters — the **latent factors** — which are not directly observed but inferred from the co-variation pattern in the data.

The mathematical engine behind factor analysis draws on linear algebra you've already studied. Each **factor** is a weighted linear combination of observed variables, and each **factor loading** is the correlation between an observed variable and the latent factor. A loading of .80 means the item shares 64% of its variance with the factor (the square of the loading, called **communality**). A loading of .20 means the item barely connects to the factor. From your work with eigenvalues, you know they represent the amount of variance a linear transformation captures — in factor analysis, factors with eigenvalues greater than 1.0 (Kaiser criterion) capture more variance than any single observed variable, making them meaningful candidates for interpretation. Factors are extracted in order from most to least variance explained.

**Exploratory factor analysis (EFA)** is the data-driven form: you let the correlations determine the factor structure without imposing a prior theory. This is useful when you're developing a new scale or exploring whether a construct is one-dimensional or multidimensional. Suppose you write 20 items about "wellbeing" and run an EFA. If the items load onto two factors — one clustering around hedonic pleasure items, the other around meaning and purpose items — the analysis is telling you that "wellbeing" as you've operationalized it may have two distinct components, and you should either refine your theory or your scale. If all 20 items load onto a single factor, you have evidence for unidimensionality.

The practical output that matters most is the **factor loading matrix**: a table of every item's loading on every factor. Strong, clean loadings (close to ±1 on one factor, near zero on others) indicate a well-defined, interpretable structure. High **cross-loadings** — an item loading significantly on two or more factors — signal that the item is ambiguous and may need to be revised or dropped. **Rotation** (orthogonal like varimax, or oblique like promax) is applied after extraction to make the factor structure more interpretable; rotation doesn't change the total variance explained, only how it's partitioned across factors.

Factor analysis sits at the foundation of most psychological measurement: intelligence tests, personality inventories, diagnostic criteria, and attitude scales all rest on factor-analytic evidence for their dimensionality. The distinction between EFA (exploratory) and confirmatory factor analysis (which tests a pre-specified model) is one of the most important methodological forks in quantitative psychology — EFA generates hypotheses about structure, while CFA tests them. What you learn here about how latent factors are identified from observed correlations becomes the foundation for structural equation modeling, where entire networks of constructs and their relationships are modeled simultaneously.
