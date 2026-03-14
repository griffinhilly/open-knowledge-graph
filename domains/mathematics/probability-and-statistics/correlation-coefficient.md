---
id: correlation-coefficient
title: Correlation Coefficient
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: scatterplots-and-correlation
  type: hard
- id: measures-of-spread
  type: soft
builds-toward:
- linear-regression-basics
tags:
- correlation
- pearson
- r
- association
stage: formal-systems
status: draft
---

# Correlation Coefficient

## Core Idea
The Pearson correlation coefficient r measures linear association between two variables, ranging from -1 (perfect negative linear relationship) to +1 (perfect positive linear relationship), with 0 indicating no linear association. Defined as r = Cov(X,Y)/(σ_X × σ_Y), correlation is unitless and symmetric in X and Y. A correlation near 0 doesn't mean no relationship—it indicates no linear relationship; nonlinear associations may be strong but have correlation near 0.

## How It's Best Learned
Compute r for various datasets and compare to scatterplot. Generate data with specified correlations. Show examples where r = 0 but strong relationships exist.

## Common Misconceptions
Thinking r = 0 implies independence or no association. Confusing correlation with causation. Believing |r| > 0.5 indicates strong relationship (depends on context).
