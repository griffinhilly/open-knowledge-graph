---
id: factor-analysis-dimensionality
title: Factor Analysis and Dimensionality Reduction
domain: social-sciences
course: research-methods-social-science
prerequisites:
- id: linear-regression-social-science
  type: soft
- id: measurement-validity-social-science
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
- id: basis-and-dimension
  type: hard
- id: eigenvalues-and-eigenvectors
  type: soft
- id: matrices-intro
  type: soft
builds-toward:
- structural-equation-modeling-latent
tags:
- factor-analysis
- latent-variables
- dimensionality
- communalities
stage: formal-systems
status: validated
---

# Factor Analysis and Dimensionality Reduction

## Core Idea
Develops exploratory and confirmatory factor analysis for identifying latent constructs underlying observed variables. Covers factor extraction methods, rotation, interpretation of loadings, communalities, and deciding on dimensionality. Applications to instrument development and scale validation in social science.

## How It's Best Learned
Conduct exploratory factor analysis on survey items, compare extraction and rotation methods, create scree plots and interpret patterns, conduct confirmatory factor analysis on independent sample.

## Common Misconceptions
- EFA and CFA test different hypotheses
- High loadings prove construct validity
- Parallel analysis is definitive for factor retention

## Questions

```yaml
- question: "A researcher uses EFA on a 20-item survey to discover a 3-factor structure, then runs CFA on the same dataset and obtains excellent fit (CFI = .97, RMSEA = .04). Can the researcher claim the 3-factor structure is confirmed?"
  type: multiple-choice
  options:
    - "Yes — the excellent CFA fit indices independently confirm that the factor structure is correct"
    - "No — using the same data for both EFA and CFA is circular: the CFA model was built to fit these correlations, so good fit is expected by construction, not evidence of generalizability"
    - "Yes — CFI > .95 is a universal benchmark proving the factor structure reflects reality"
    - "No — but only because CFA requires a minimum of 500 participants to produce valid fit statistics"
  answer: 1
  explanation: "This is the EFA-CFA circularity trap. EFA derives the factor structure by finding the best-fitting solution in a specific dataset. CFA then 'tests' whether that structure fits — but it's the same data the structure came from. Of course it fits: the model was optimized on those correlations. Genuine confirmation requires an independent sample where the pre-specified model is tested on data it has never seen. EFA is hypothesis-generating; CFA is hypothesis-testing; they require separate samples."

- question: "A researcher applies Kaiser's rule (eigenvalue > 1) and retains 7 factors from a 25-item scale. A colleague suggests this may be too many. What should the researcher do?"
  type: multiple-choice
  options:
    - "Accept the 7-factor solution — Kaiser's rule is the definitive standard for factor retention"
    - "Cross-check with a scree plot and parallel analysis, since Kaiser's rule often retains too many factors and the retention decision is a theory-informed judgment, not a mechanical rule"
    - "Halve the number of factors to 3 or 4, since social constructs rarely have more than 4 dimensions"
    - "Use only the first factor, since the first eigenvalue is always the most meaningful"
  answer: 1
  explanation: "Kaiser's rule (eigenvalue > 1) is widely used but widely criticized because it tends to over-retain factors — especially with larger item sets, many eigenvalues will exceed 1 by chance. Parallel analysis, which compares observed eigenvalues to those from random data of the same size, provides a more defensible baseline. The scree plot can reveal a natural elbow. Most importantly, the retention decision should be guided by theory — how many dimensions make conceptual sense? Factor retention is a judgment call informed by multiple criteria, not a deterministic formula."

- question: "Oblique rotation is often preferable to orthogonal rotation in social science factor analysis because real psychological constructs are rarely completely uncorrelated with each other."
  type: true-false
  answer: true
  explanation: "Orthogonal rotation (e.g., Varimax) constrains factors to be uncorrelated, which produces clean, simple loading patterns but imposes an unrealistic assumption when the constructs are theoretically related. Extraversion and positive affect, anxiety and neuroticism — these are not zero-correlated in reality. Oblique rotation (e.g., Oblimin, Promax) allows factors to correlate naturally, producing a more realistic solution. The trade-off is a slightly more complex interpretation (you need a pattern matrix and a structure matrix), but the gain in realism usually outweighs the cost."

- question: "If an item loads .70 on a factor in exploratory factor analysis, this is strong evidence that the item is a valid measure of the psychological construct the factor represents."
  type: true-false
  answer: false
  explanation: "This conflates statistical coherence with construct validity. A high loading means the item shares substantial variance with other items on that factor — they co-vary together. But what the factor 'is' depends on theoretical interpretation of the common thread among high-loading items, not on the loading values alone. High loadings are reliability-adjacent evidence (internal structure), not validity evidence. Validity requires showing the factor relates to external criteria in theoretically expected ways, which loading size cannot establish."

- question: "Why must exploratory factor analysis and confirmatory factor analysis be conducted on separate samples to provide genuine evidence about a scale's factor structure?"
  type: short-answer
  answer: "EFA discovers a factor structure by finding the solution that best fits the correlation patterns in a given dataset — it is data-driven and capitalizes on that sample's specific covariances. CFA tests whether a pre-specified structure fits new data. If the CFA model is derived from EFA on the same sample, the model was built to fit those correlations, and good CFA fit is tautological. An independent sample allows CFA to test whether the EFA-derived structure generalizes beyond the discovery data — which is the actual scientific question."
  explanation: "This is the discovery-vs-confirmation distinction: EFA generates hypotheses, CFA tests them. Running both on the same data conflates these roles. The same issue arises in any model-building context: a model always fits the data it was built on better than new data. Only independent replication distinguishes a model that captures real structure from one that merely describes sampling noise."
```

## Explainer

From your work on eigenvalues and eigenvectors, you know that a matrix can be decomposed into directions (eigenvectors) and their associated scaling magnitudes (eigenvalues). Factor analysis applies this intuition to a correlation matrix among observed variables. Imagine you give people a 20-item survey about political attitudes — each item is a variable. Factor analysis asks: can the correlations among these 20 items be explained by a smaller number of underlying **latent factors** that we never directly measured? If items about economic policy all correlate with each other but not with items about social policy, that pattern suggests two underlying dimensions (factors), not twenty independent ones.

The mechanics start with the correlation matrix. Factor extraction — whether via principal axis factoring, maximum likelihood, or other methods — finds the linear combinations of observed variables that capture the most shared variance. The first factor accounts for the most common variance, the second for the next most, and so on. Each factor has an eigenvalue representing how much variance it explains. You then face a **retention decision**: how many factors are real signal versus noise? Common criteria include Kaiser's rule (keep factors with eigenvalue > 1), the scree plot (look for the "elbow"), and parallel analysis (compare eigenvalues to those from random data). None of these is definitive — this is a judgment call informed by theory.

Once factors are extracted, **rotation** is used to make them interpretable. Unrotated solutions are mathematically clean but often theoretically murky — every item loads moderately on every factor. Rotation reallocates variance so that items load strongly on one factor and weakly on others. **Orthogonal rotation** (like Varimax) keeps factors uncorrelated; **oblique rotation** (like Oblimin) allows factors to correlate, which is more realistic when underlying constructs are related. The key output is the **loading matrix** — a table showing how strongly each item relates to each factor. Strong loadings (above .40 or .50 by convention) define what a factor "is," and naming the factor requires reading the common thread among high-loading items.

**Exploratory factor analysis (EFA)** is used when you don't know the factor structure in advance — you let the data suggest it. **Confirmatory factor analysis (CFA)** is used when you have a theoretical model specifying which items load on which factors, and you test whether the data fit that model. These are not interchangeable: running EFA to find a structure and then immediately running CFA on the same data to "confirm" it is circular — you need an independent sample to truly test. CFA requires specifying which loadings are free (estimated) and which are fixed to zero, and it produces model fit statistics (CFI, RMSEA, SRMR) that tell you how well the hypothesized structure matches the observed correlations. Good fit means your measurement model is plausible; it does not prove the latent constructs exist or are well-measured.
