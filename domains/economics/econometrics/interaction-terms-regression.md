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

## Questions

```yaml
- question: "In the model Wage = β₀ + β₁*Education + β₂*Female + β₃*(Education × Female) + ε, what does β₁ represent?"
  type: multiple-choice
  options:
    - "The average return to education across all workers in the sample"
    - "The return to education for male workers specifically (the reference group when Female = 0)"
    - "The return to education for female workers specifically"
    - "The difference in education returns between men and women"
  answer: 1
  explanation: "When an interaction is present, β₁ is the effect of Education on Wage *when all other interacted variables equal zero* — here, when Female = 0, meaning for male workers. It is not the average effect for all workers; that average would require integrating over the distribution of Female. β₃ is the *difference* in returns (how much the female education return differs from the male return), and the female return to education is β₁ + β₃. This is the critical interpretation trap: β₁ alone no longer summarizes the effect of Education for anyone other than the reference group."

- question: "A researcher centers Education by subtracting its mean before including it in an interaction model. Which of the following correctly describes the effect of centering?"
  type: multiple-choice
  options:
    - "Centering changes the interaction coefficient β₃ and improves model fit"
    - "Centering changes the interpretation of main effect coefficients but leaves β₃, model fit, and predicted values unchanged"
    - "Centering eliminates multicollinearity between the main effects and the interaction term"
    - "Centering changes predicted values for observations near the mean of Education"
  answer: 1
  explanation: "Centering is a reparameterization, not a change in model. β₃ (the interaction coefficient) is invariant to centering. Model fit (R², residuals) is unchanged. Predicted values for any observation are identical. What changes is that the main effect coefficients now refer to the effect at the mean of Education rather than at zero — a more interpretable and estimable quantity when zero is outside the data range. Option C is a common misconception: centering reduces the *sample* correlation between X and X*Z, but does not eliminate the structural collinearity between them."

- question: "In a regression with an interaction term X*Z, the marginal effect of X on Y is a function of Z rather than a single constant."
  type: true-false
  answer: true
  explanation: "The marginal effect ∂Y/∂X = β₁ + β₃Z. When Z = 0, the effect is β₁; when Z takes other values, the effect changes accordingly. This is precisely what the interaction term captures: the relationship between X and Y is not fixed but depends on the level of another variable. Failing to recognize this leads to the common error of reporting β₁ as 'the effect of X' and ignoring that this is only correct at Z = 0."

- question: "If you estimate a model with an interaction term and find that β₁ is small and statistically insignificant, this tells you that X has no effect on Y."
  type: true-false
  answer: false
  explanation: "With an interaction term, β₁ is the effect of X *only when Z = 0*. If Z = 0 is not a meaningful or common value in the data, β₁ is essentially extrapolation and an insignificant β₁ says nothing about X's effect at typical values of Z. The full marginal effect is β₁ + β₃Z, so X can have a large, significant effect at common values of Z even when β₁ alone is near zero. Evaluating 'the effect of X' requires computing the marginal effect at substantively relevant values of Z."

- question: "Why is a plot of predicted values of Y against X at multiple representative values of Z more informative than simply reporting the interaction coefficient β₃?"
  type: short-answer
  answer: "β₃ alone tells you whether the relationship between X and Y changes with Z and by how much per unit of Z, but it does not convey the practical magnitude of those differences at the values of Z that actually appear in the data. A plot shows the full conditional relationship: whether the lines diverge, cross, or remain nearly parallel across the data range. Crossing lines signal that X has opposite effects at different levels of Z — a substantively important finding that a single coefficient cannot communicate. The plot forces the analyst to think about the entire function β₁ + β₃Z rather than a single-number summary."
  explanation: "This visualization approach is the recommended diagnostic for interaction models because it translates the abstract coefficient into concrete predictions. If the plotted lines are parallel (same slope at all Z values), there is no meaningful interaction even if β₃ is technically nonzero. If lines diverge substantially, the interaction matters. If they cross within the data range, the sign of X's effect reverses — a finding that policy analysis must take seriously. The plot also reveals whether any of those representative Z values are in-sample, preventing misleading extrapolations."
```

## Explainer

Your regression toolkit so far has assumed that the effect of each predictor on the outcome is fixed — a one-unit increase in education raises wages by the same amount regardless of gender, industry, or any other factor. Interaction terms relax exactly this assumption. They let you ask: does the effect of X on Y depend on the level of some other variable Z?

The mechanics are straightforward: add the product X × Z alongside both main effects. The model becomes Y = β₀ + β₁X + β₂Z + β₃(X × Z) + ε. The **marginal effect** of X is now ∂Y/∂X = β₁ + β₃Z. This is no longer a single number — it is a function of Z. When Z = 0, the effect of X is just β₁. When Z equals some other value, the effect is β₁ + β₃ times that value. This is why your coefficient interpretation prerequisite matters so much here: β₁ alone no longer summarizes the effect of X on Y in any general sense once an interaction is present.

The clearest case to build intuition is a **binary × continuous interaction**. Suppose you regress wages on years of education, a female dummy, and their product. The female dummy might have a negative coefficient (wage gap at zero education), the education coefficient captures returns to schooling for men (the reference group), and the interaction coefficient captures how much the education return *differs* for women. A negative interaction coefficient means women get a smaller wage premium per additional year of education. Notice that the female main effect coefficient is now the gap specifically when education = 0 — a quantity that may be extrapolation. This is the core trap: when you include an interaction, the interpretation of each main effect becomes conditional on the interacting variable equaling zero.

**Centering** the continuous variable before creating the interaction addresses this. If you demean education (subtract its mean) before multiplying, then the main effect for female now represents the wage gap at the average education level — a far more interpretable and estimable quantity. Centering does not change β₃ (the interaction coefficient), does not change model fit, and does not change predicted values — it only rescales what the main effects mean. This is why the common misconception that centering "changes the interaction" is wrong: only the interpretation of the main effects shifts.

A practical diagnostic is to plot predicted values across the range of X for different values of Z (often two or three representative levels). If the lines are parallel, there is no interaction — a multiplicative term will be near zero. If the lines diverge or cross, an interaction is present and substantively meaningful. This visual check is more informative than staring at a single coefficient, because it forces you to think about the full conditional relationship rather than trying to extract a single-number summary from a model where no such number exists.
