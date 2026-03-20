---
id: adjusted-r-squared-model-comparison
title: Adjusted R-Squared for Model Comparison
domain: economics
course: econometrics
prerequisites:
- id: r-squared-goodness-of-fit
  type: hard
builds-toward:
- information-criteria-model-selection
tags:
- model-comparison
- model-selection
stage: advanced
status: draft
---

# Adjusted R-Squared for Model Comparison

## Core Idea
Adjusted R² = 1 - ((RSS/(n-k-1)) / (TSS/(n-1))) penalizes adding regressors via a degrees-of-freedom adjustment. Unlike R², it can decrease when irrelevant variables are added, making it useful for comparing non-nested models with different regressor counts.

## Explainer

From your study of **R-squared (R²)**, you know it measures the fraction of total variation in the dependent variable explained by the regression model: R² = 1 − RSS/TSS, where RSS is the residual sum of squares and TSS is the total sum of squares. You also know its key weakness: R² can never decrease when you add another variable to the model, even if that variable is pure noise. This mechanical property means that R² always favors larger models, making it useless for deciding whether an additional regressor actually improves the model.

**Adjusted R²** fixes this by introducing a penalty for model complexity. The formula replaces the raw sums of squares with their degrees-of-freedom-corrected versions: Adjusted R² = 1 − ((RSS/(n−k−1)) / (TSS/(n−1))), where n is the sample size and k is the number of regressors. The denominator of the RSS term, n−k−1, shrinks as you add regressors, inflating the ratio RSS/(n−k−1) relative to the raw RSS. This means that adding a variable only improves adjusted R² if the reduction in RSS is large enough to offset the penalty from losing a degree of freedom. If you add a useless variable, RSS barely changes but n−k−1 decreases by one, and adjusted R² falls.

Think of it like a batting average analogy. Raw R² is like counting total hits without regard to how many at-bats you took — more at-bats (more variables) can only add hits (explained variation), never subtract them. Adjusted R² is like batting average itself: each additional at-bat (variable) must produce enough hits (variance explained) to maintain or improve the average. A variable that explains very little variation is like a weak at-bat that drags the average down.

In practice, you use adjusted R² to compare models with different numbers of regressors estimated on the same dataset. If Model A with three variables has an adjusted R² of 0.72 and Model B with five variables has an adjusted R² of 0.71, you prefer the simpler Model A — the two extra variables did not earn their keep. Note that adjusted R² can even be negative (when the model explains almost nothing and the penalty dominates), and it is only valid for comparing models with the same dependent variable. For more sophisticated model selection, especially with many candidate models, **information criteria** like AIC and BIC provide stronger theoretical foundations — but adjusted R² remains a practical, intuitive first tool for the common question of whether adding a variable helps or hurts your model.
