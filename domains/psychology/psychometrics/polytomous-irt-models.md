---
id: polytomous-irt-models
title: Polytomous Item Response Theory Models
domain: psychology
course: psychometrics
prerequisites:
- id: item-response-functions
  type: hard
- id: two-parameter-logistic-model
  type: hard
builds-toward:
- dimensional-assessment-and-bifactor-models
tags:
- irt
- ordered-responses
- rating-scales
- partial-credit
- graded-response
stage: advanced
status: draft
---

# Polytomous Item Response Theory Models

## Core Idea
Polytomous IRT models extend the binary right/wrong framework to ordered categorical responses, such as Likert-scale ratings, partial-credit items on math tests, or confidence judgments. Models like the Graded Response Model (GRM) and Generalized Partial Credit Model (GPCM) extract more information from each item response than classical test theory and provide nuanced item-level diagnostics.

## How It's Best Learned
Work with real rating-scale data from personality or attitude measures. Fit GRM and GPCM models and interpret item threshold parameters (step difficulties) and discrimination parameters. Compare results to classical item statistics to understand what additional information polytomous IRT provides.

## Common Misconceptions
- Assuming that all ordered response categories contribute equally to measurement precision; middle categories often have lower information.
- Treating polytomous responses as interval-scaled when they are ordinal; IRT models respect the ordering without assuming equal intervals.
- Using classical item-total correlations for category-level analysis when polytomous IRT is more appropriate.
