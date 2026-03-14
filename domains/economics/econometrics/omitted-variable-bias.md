---
id: omitted-variable-bias
title: Omitted Variable Bias
domain: economics
course: econometrics
prerequisites:
- id: multiple-regression-model
  type: hard
- id: ols-assumptions
  type: hard
- id: r-squared-and-model-fit
  type: soft
builds-toward:
- endogeneity
- instrumental-variables
- causal-inference-econometrics
tags:
- OVB
- bias
- confounding
- identification
stage: formal-systems
status: validated
---
# Omitted Variable Bias

## Core Idea
Omitted variable bias (OVB) occurs when a variable that affects y and is correlated with an included regressor is excluded from the model, causing the OLS estimator to be biased and inconsistent. The direction of bias is determined by the sign of the correlation between the omitted variable and the included regressor, multiplied by the sign of the omitted variable's effect on y. The canonical example is estimating the return to education: omitting ability biases the education coefficient upward because ability raises wages and is positively correlated with schooling. OVB is the fundamental obstacle to causal inference with observational data.

## How It's Best Learned
Derive the OVB formula algebraically, then apply the 'sign heuristic' to real examples — labor economics wage regressions are ideal for this exercise.

## Common Misconceptions
- OVB cannot be fixed by adding more data; it requires either measuring the omitted variable or using an instrumental variable strategy.
- If the omitted variable is uncorrelated with the regressor of interest, omitting it biases the standard errors but not the coefficient.
