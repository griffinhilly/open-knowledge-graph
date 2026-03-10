---
id: correlation-coefficient
title: The Pearson Correlation Coefficient
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: scatterplots-and-correlation
  type: hard
- id: measures-of-spread
  type: hard
builds-toward:
- linear-regression
tags:
- correlation
- pearson-r
- linear-association
- covariance
stage: formal-systems
status: draft
---

# The Pearson Correlation Coefficient

## Core Idea
The Pearson correlation coefficient r = [Σ(xᵢ − x̄)(yᵢ − ȳ)] / [(n−1)sₓsᵧ] measures the strength and direction of linear association between two quantitative variables. It ranges from −1 (perfect negative linear) to +1 (perfect positive linear), with 0 indicating no linear relationship. The correlation is dimensionless and unitless — it is unchanged by linear transformations of either variable. Because r only captures linear association, a strong curved relationship can have r near 0.

## How It's Best Learned
Have students estimate r from scatterplots before computing it — this builds visual intuition. Then compute r by hand for a small dataset. Emphasize that r is symmetric (correlation of X with Y equals correlation of Y with X) and that it measures only linear association.

## Common Misconceptions
- Thinking r = 0 means no relationship, when a nonlinear relationship could be strong.
- Treating r as a proportion of data points on the line rather than a standardized covariance.
- Applying r to non-linear or categorical data.
