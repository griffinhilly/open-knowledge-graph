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

## Explainer

Your regression toolkit so far has assumed that the effect of each predictor on the outcome is fixed — a one-unit increase in education raises wages by the same amount regardless of gender, industry, or any other factor. Interaction terms relax exactly this assumption. They let you ask: does the effect of X on Y depend on the level of some other variable Z?

The mechanics are straightforward: add the product X × Z alongside both main effects. The model becomes Y = β₀ + β₁X + β₂Z + β₃(X × Z) + ε. The **marginal effect** of X is now ∂Y/∂X = β₁ + β₃Z. This is no longer a single number — it is a function of Z. When Z = 0, the effect of X is just β₁. When Z equals some other value, the effect is β₁ + β₃ times that value. This is why your coefficient interpretation prerequisite matters so much here: β₁ alone no longer summarizes the effect of X on Y in any general sense once an interaction is present.

The clearest case to build intuition is a **binary × continuous interaction**. Suppose you regress wages on years of education, a female dummy, and their product. The female dummy might have a negative coefficient (wage gap at zero education), the education coefficient captures returns to schooling for men (the reference group), and the interaction coefficient captures how much the education return *differs* for women. A negative interaction coefficient means women get a smaller wage premium per additional year of education. Notice that the female main effect coefficient is now the gap specifically when education = 0 — a quantity that may be extrapolation. This is the core trap: when you include an interaction, the interpretation of each main effect becomes conditional on the interacting variable equaling zero.

**Centering** the continuous variable before creating the interaction addresses this. If you demean education (subtract its mean) before multiplying, then the main effect for female now represents the wage gap at the average education level — a far more interpretable and estimable quantity. Centering does not change β₃ (the interaction coefficient), does not change model fit, and does not change predicted values — it only rescales what the main effects mean. This is why the common misconception that centering "changes the interaction" is wrong: only the interpretation of the main effects shifts.

A practical diagnostic is to plot predicted values across the range of X for different values of Z (often two or three representative levels). If the lines are parallel, there is no interaction — a multiplicative term will be near zero. If the lines diverge or cross, an interaction is present and substantively meaningful. This visual check is more informative than staring at a single coefficient, because it forces you to think about the full conditional relationship rather than trying to extract a single-number summary from a model where no such number exists.
