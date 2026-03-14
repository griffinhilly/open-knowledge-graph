---
id: interaction-terms-regression
title: Interaction Terms in Regression
domain: economics
course: econometrics
prerequisites:
- id: multiple-regression-model
  type: hard
- id: coefficient-interpretation-regression
  type: hard
builds-toward:
- nonlinear-models-interpretation
tags:
- regression
- specification
- interaction
stage: formal-systems
status: draft
---

# Interaction Terms in Regression

## Core Idea
Interaction terms allow the effect of one variable on the outcome to depend on the value of another variable. Including the product of two regressors captures whether their effects are additive or synergistic.

## How It's Best Learned
Start with binary indicator interactions to visualize group-specific slopes. Plot predicted values across one variable at different levels of the interacting variable to see how the relationship changes.

## Common Misconceptions
The coefficient on the main variable is not the overall effect when interactions are present—the marginal effect depends on the value of the interacting variable. Centering variables changes the interpretation of main effects but not the interaction effect itself.
