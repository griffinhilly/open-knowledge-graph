---
id: dummy-variables-regression
title: Dummy Variables and Categorical Regressors
domain: economics
course: econometrics
prerequisites:
- id: coefficient-interpretation-regression
  type: hard
- id: multiple-regression-model
  type: hard
builds-toward:
- difference-in-differences
- fixed-effects-models
tags:
- dummy-variables
- categorical
- indicator
- interaction-terms
stage: formal-systems
status: draft
---

# Dummy Variables and Categorical Regressors

## Core Idea
A dummy (indicator) variable takes values 0 or 1 to represent group membership, allowing categorical variables to enter linear regression. The coefficient on a dummy captures the mean difference in y between that group and the omitted reference group, holding all other regressors constant. For a variable with k categories, include k−1 dummies to avoid perfect multicollinearity (the dummy variable trap). Interaction terms between a dummy and a continuous variable allow the slope on the continuous variable to differ across groups, enabling tests of whether relationships are heterogeneous.

## How It's Best Learned
Run a gender wage gap regression with and without control variables to see how the dummy coefficient changes — this illustrates both interpretation and the role of controls in reducing omitted variable bias.

## Common Misconceptions
- Including all k dummies creates perfect multicollinearity with the intercept (dummy variable trap) — always drop one.
- The reference category matters for the coefficient values but not for the implied predicted means or their differences.
