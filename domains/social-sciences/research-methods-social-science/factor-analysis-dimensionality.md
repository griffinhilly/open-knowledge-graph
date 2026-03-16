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
- id: eigenvalues-eigenvectors
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
stage: advanced
status: draft
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

## Explainer

From your work on eigenvalues and eigenvectors, you know that a matrix can be decomposed into directions (eigenvectors) and their associated scaling magnitudes (eigenvalues). Factor analysis applies this intuition to a correlation matrix among observed variables. Imagine you give people a 20-item survey about political attitudes — each item is a variable. Factor analysis asks: can the correlations among these 20 items be explained by a smaller number of underlying **latent factors** that we never directly measured? If items about economic policy all correlate with each other but not with items about social policy, that pattern suggests two underlying dimensions (factors), not twenty independent ones.

The mechanics start with the correlation matrix. Factor extraction — whether via principal axis factoring, maximum likelihood, or other methods — finds the linear combinations of observed variables that capture the most shared variance. The first factor accounts for the most common variance, the second for the next most, and so on. Each factor has an eigenvalue representing how much variance it explains. You then face a **retention decision**: how many factors are real signal versus noise? Common criteria include Kaiser's rule (keep factors with eigenvalue > 1), the scree plot (look for the "elbow"), and parallel analysis (compare eigenvalues to those from random data). None of these is definitive — this is a judgment call informed by theory.

Once factors are extracted, **rotation** is used to make them interpretable. Unrotated solutions are mathematically clean but often theoretically murky — every item loads moderately on every factor. Rotation reallocates variance so that items load strongly on one factor and weakly on others. **Orthogonal rotation** (like Varimax) keeps factors uncorrelated; **oblique rotation** (like Oblimin) allows factors to correlate, which is more realistic when underlying constructs are related. The key output is the **loading matrix** — a table showing how strongly each item relates to each factor. Strong loadings (above .40 or .50 by convention) define what a factor "is," and naming the factor requires reading the common thread among high-loading items.

**Exploratory factor analysis (EFA)** is used when you don't know the factor structure in advance — you let the data suggest it. **Confirmatory factor analysis (CFA)** is used when you have a theoretical model specifying which items load on which factors, and you test whether the data fit that model. These are not interchangeable: running EFA to find a structure and then immediately running CFA on the same data to "confirm" it is circular — you need an independent sample to truly test. CFA requires specifying which loadings are free (estimated) and which are fixed to zero, and it produces model fit statistics (CFI, RMSEA, SRMR) that tell you how well the hypothesized structure matches the observed correlations. Good fit means your measurement model is plausible; it does not prove the latent constructs exist or are well-measured.
