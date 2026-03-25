---
id: adjusted-r-squared-model-comparison
title: Adjusted R-Squared for Model Comparison
domain: economics
course: econometrics
prerequisites:
- id: r-squared-goodness-of-fit
  type: hard
- id: information-criteria-model-selection
  type: soft
- id: hausman-test-fe-versus-re
  type: soft
builds-toward:
- information-criteria-model-selection
tags:
- model-comparison
- model-selection
stage: advanced
status: validated
---
# Adjusted R-Squared for Model Comparison

## Core Idea
Adjusted R² = 1 - ((RSS/(n-k-1)) / (TSS/(n-1))) penalizes adding regressors via a degrees-of-freedom adjustment. Unlike R², it can decrease when irrelevant variables are added, making it useful for comparing non-nested models with different regressor counts.

## Questions

```yaml
- question: "You add two variables to a regression model. R² rises from 0.72 to 0.73, but adjusted R² falls from 0.71 to 0.70. What should you conclude?"
  type: multiple-choice
  options:
    - "Keep both variables — R² increased, confirming they improve the model"
    - "Drop both variables — the degrees-of-freedom penalty outweighs the variance they explain, so adjusted R² correctly indicates the model is worse"
    - "The model is overfit and should be re-estimated on a holdout sample"
    - "Adjusted R² is unreliable when R² increases, so R² should take priority"
  answer: 1
  explanation: "When adjusted R² falls while R² rises, the variables are not explaining enough new variance to justify the cost of the additional degrees of freedom. The adjusted formula penalizes each added variable by inflating the ratio RSS/(n−k−1); if the reduction in RSS is small, the penalty dominates and adjusted R² falls. This is exactly what adjusted R² is designed to detect — variables that appear to help (raising R²) but actually reduce the model's explanatory power per parameter. R² always weakly increases when variables are added, which is why it cannot be used for this comparison."

- question: "Why can R² never decrease when you add another regressor to an OLS model?"
  type: multiple-choice
  options:
    - "Adding a regressor increases the sample size, which mechanically improves fit"
    - "OLS minimizes RSS, so the new coefficient is chosen to reduce RSS as much as possible — in the worst case it is set to zero, leaving RSS unchanged"
    - "R² is normalized so that it is bounded below by the value from the smaller model"
    - "Adding a variable always improves the model because OLS is unbiased"
  answer: 1
  explanation: "OLS finds the coefficient values that minimize RSS. When you add a new variable, OLS can always choose to set its coefficient to zero — reproducing the original model's RSS exactly. If any non-zero coefficient reduces RSS further, OLS will use it. So RSS can only stay the same or decrease, and R² = 1 − RSS/TSS can only stay the same or increase. This mechanical property means R² rewards model size regardless of whether the added variables are meaningful — the key flaw that adjusted R² corrects."

- question: "Adjusted R² is always between 0 and 1, just like ordinary R²."
  type: true-false
  answer: false
  explanation: "Adjusted R² can be negative. When the model explains almost nothing (RSS is close to TSS) and k is large, the degrees-of-freedom penalty can dominate, making the ratio RSS/(n−k−1) larger than TSS/(n−1), so adjusted R² = 1 − (that ratio) drops below zero. This is a signal that the model is essentially useless — it explains less variance per parameter than a model with just an intercept. Ordinary R² is bounded [0,1] because without the degrees-of-freedom correction, RSS ≤ TSS always."

- question: "If adjusted R² decreases when a new variable is added, it means the variable explains less additional variance than the cost of the degree of freedom it consumes."
  type: true-false
  answer: true
  explanation: "This is exactly the interpretation of the adjusted R² penalty. Each additional variable costs one degree of freedom, which inflates RSS/(n−k−1). If the variable reduces RSS substantially, this inflation is more than offset and adjusted R² rises. If the variable barely reduces RSS, the inflation dominates and adjusted R² falls. A falling adjusted R² is the signal that the variable is not earning its place in the model — a criterion that raw R² is incapable of detecting."

- question: "A colleague argues 'R² is the right metric for model comparison because adding a useful variable always increases it.' What is wrong with this reasoning, and how does adjusted R² address the problem?"
  type: short-answer
  answer: "The flaw is that R² increases for any added variable — useful or not — because OLS can always set the new coefficient to zero to avoid increasing RSS. A useless variable will still weakly increase R², making R² unable to distinguish between variables that genuinely improve the model and those that add noise. Adjusted R² addresses this by penalizing model complexity: it divides RSS by n−k−1 (shrinking as k increases), so adding a variable that barely reduces RSS will actually decrease adjusted R². Only variables that reduce RSS enough to offset the degrees-of-freedom cost will improve adjusted R²."
  explanation: "The batting average analogy is helpful: R² is like total hits (always non-decreasing with more at-bats), while adjusted R² is like batting average (each new at-bat can hurt your average if you don't get a hit). This is why adjusted R² is used for comparing models with different numbers of regressors on the same dataset — it asks whether each variable is 'earning its keep.'"
```

## Explainer

From your study of **R-squared (R²)**, you know it measures the fraction of total variation in the dependent variable explained by the regression model: R² = 1 − RSS/TSS, where RSS is the residual sum of squares and TSS is the total sum of squares. You also know its key weakness: R² can never decrease when you add another variable to the model, even if that variable is pure noise. This mechanical property means that R² always favors larger models, making it useless for deciding whether an additional regressor actually improves the model.

**Adjusted R²** fixes this by introducing a penalty for model complexity. The formula replaces the raw sums of squares with their degrees-of-freedom-corrected versions: Adjusted R² = 1 − ((RSS/(n−k−1)) / (TSS/(n−1))), where n is the sample size and k is the number of regressors. The denominator of the RSS term, n−k−1, shrinks as you add regressors, inflating the ratio RSS/(n−k−1) relative to the raw RSS. This means that adding a variable only improves adjusted R² if the reduction in RSS is large enough to offset the penalty from losing a degree of freedom. If you add a useless variable, RSS barely changes but n−k−1 decreases by one, and adjusted R² falls.

Think of it like a batting average analogy. Raw R² is like counting total hits without regard to how many at-bats you took — more at-bats (more variables) can only add hits (explained variation), never subtract them. Adjusted R² is like batting average itself: each additional at-bat (variable) must produce enough hits (variance explained) to maintain or improve the average. A variable that explains very little variation is like a weak at-bat that drags the average down.

In practice, you use adjusted R² to compare models with different numbers of regressors estimated on the same dataset. If Model A with three variables has an adjusted R² of 0.72 and Model B with five variables has an adjusted R² of 0.71, you prefer the simpler Model A — the two extra variables did not earn their keep. Note that adjusted R² can even be negative (when the model explains almost nothing and the penalty dominates), and it is only valid for comparing models with the same dependent variable. For more sophisticated model selection, especially with many candidate models, **information criteria** like AIC and BIC provide stronger theoretical foundations — but adjusted R² remains a practical, intuitive first tool for the common question of whether adding a variable helps or hurts your model.
