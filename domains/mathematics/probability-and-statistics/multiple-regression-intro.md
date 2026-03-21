---
id: multiple-regression-intro
title: Introduction to Multiple Linear Regression
domain: mathematics
course: probability-and-statistics
prerequisites:
- id: linear-regression
  type: hard
tags:
- regression
- multiple-regression
- multivariate
stage: formal-systems
status: draft
---

# Introduction to Multiple Linear Regression

## Core Idea
Multiple linear regression extends simple regression to many predictors: E[Y|X₁,...,Xₚ] = β₀ + β₁X₁ + ... + βₚXₚ. Coefficients represent partial effects (adjusted for other predictors). Model selection and multicollinearity are key concerns.

## How It's Best Learned
Fit multiple regression models with software. Compare nested models using F-tests. Examine variance inflation factors (VIF) for multicollinearity. Interpret partial slopes as adjusted effects. Use visualization and residual diagnostics.

## Common Misconceptions
Interpreting regression coefficients causally without experimentation. Ignoring multicollinearity and its effects on interpretability. Believing all significant predictors should be included. Overfitting with too many predictors.

## Questions

```yaml
- question: "In a simple regression, number of books in the home positively predicts vocabulary scores (slope = 2.3). When family income is added to the model, the slope for books drops to 0.4. The most likely explanation is:"
  type: multiple-choice
  options:
    - "The data was entered incorrectly — adding income shouldn't change the books coefficient"
    - "Family income is a confounder: wealthier families both have more books and higher-vocabulary children, so the books slope was partly capturing income's effect"
    - "Multicollinearity has made the books coefficient biased toward zero"
    - "Income should not have been added since it isn't directly related to vocabulary"
  answer: 1
  explanation: "This is statistical control in action. In simple regression, books' slope absorbed the shared variance with income (books and income are correlated; both predict vocabulary). Adding income lets the model partial out income's contribution, isolating books' unique effect. The original slope wasn't wrong — it was the correct marginal slope for books without controlling for income. Option C is incorrect: multicollinearity would inflate standard errors and create instability, not systematically shrink a coefficient."

- question: "A multiple regression model achieves R² = 0.92 with 15 predictors on only 20 observations. A statistician flags this as problematic. Why?"
  type: multiple-choice
  options:
    - "R² above 0.9 always indicates multicollinearity"
    - "With 20 observations and 15 predictors, the model is almost certainly overfitting — fitting noise in the data rather than real signal"
    - "15 predictors is simply too many to interpret, regardless of sample size"
    - "High R² in multiple regression always signals a spurious causal relationship"
  answer: 1
  explanation: "With only 20 observations and 15 predictors, the model has almost no degrees of freedom remaining. Adding predictors always increases R² on training data, even if the predictors are pure noise — with 15 predictors and 20 observations, you're essentially memorizing the dataset. The rule of thumb is roughly 10–20 observations per predictor for stable estimates. High R² is not inherently problematic; high R² with very few observations per predictor is."

- question: "A predictor with a non-significant p-value in multiple regression has no real relationship with the outcome variable."
  type: true-false
  answer: false
  explanation: "Non-significance can reflect multicollinearity rather than a true lack of relationship. When two predictors are strongly correlated, the model cannot distinguish their contributions — both get large standard errors and high p-values even if each has a genuine association with Y. A predictor can be genuinely important while appearing non-significant because it shares variance with another predictor in the model. Non-significance means 'we can't isolate this predictor's effect,' not 'this predictor doesn't matter.'"

- question: "The partial slope β₁ in multiple regression tells you the expected change in Y for a one-unit increase in X₁, holding all other predictors in the model constant."
  type: true-false
  answer: true
  explanation: "This is the definition of a partial slope and the conceptual core of multiple regression. The 'holding everything else constant' interpretation is what makes multiple regression useful for observational data: by including potential confounders, you partial out their contributions and estimate each predictor's unique association with the outcome. This is statistical control — the model does algebraically what a controlled experiment does physically."

- question: "Why can a predictor's slope in multiple regression differ substantially from its slope in a simple regression with only that predictor?"
  type: short-answer
  answer: "In simple regression, the slope for X₁ captures its total association with Y, including shared variance with any omitted predictors. In multiple regression, each partial slope represents X₁'s unique association with Y after statistically partialing out all other predictors in the model. If X₁ is correlated with another predictor X₂, and X₂ also predicts Y, simple regression conflates both effects in X₁'s slope. Multiple regression separates them, revealing X₁'s independent contribution."
  explanation: "This difference between marginal and partial slopes is the key conceptual advance of multiple regression. The slope change when adding a predictor is not a flaw — it reveals how much of the original association was due to confounding. A large drop in a coefficient after adding predictors is evidence that the original association was partly spurious. This is why multiple regression is so important for disentangling correlated predictors in observational research."
```

## Explainer

Simple linear regression asks: how does Y change with X? Multiple regression asks a harder question: how does Y change with X₁ *holding X₂, X₃, ... constant*? This "holding everything else constant" idea is the heart of the model. The equation E[Y|X₁,...,Xₚ] = β₀ + β₁X₁ + ... + βₚXₚ looks like a straight line extended to higher dimensions — a flat hyperplane through p-dimensional predictor space. Each slope βⱼ is a **partial slope**: it tells you the expected change in Y for a one-unit increase in Xⱼ when all other predictors are held fixed.

The key insight is that partial slopes can differ dramatically from simple slopes. Suppose you regress exam scores on study hours and find a positive slope. Now add a second predictor, prior GPA. The coefficient on study hours shrinks — not because study hours matter less, but because some of its apparent effect was actually attributable to GPA (better students both study more *and* score higher). Multiple regression disentangles these associations. This is called **statistical control**: by including a variable in the model, you partial out its contribution, isolating the unique relationship of each predictor with the outcome.

**Multicollinearity** occurs when predictors are strongly correlated with each other. Intuitively: if X₁ and X₂ move almost in lockstep, the model cannot tell which one is doing the work. Mathematically, the coefficient estimates become unstable — large standard errors, wildly varying slopes across similar datasets. The **variance inflation factor (VIF)** quantifies this instability for each predictor. A VIF above 5 or 10 is a warning sign. Remedies include dropping one of the correlated predictors, combining them (e.g., via PCA), or collecting more data. Multicollinearity does not bias predictions from the model as a whole; it only undermines the interpretability of individual coefficients.

Model selection — choosing which predictors to include — is one of the central practical challenges. Adding more predictors always improves R² on the training data, but can hurt predictive accuracy on new data (**overfitting**). Adjusted R², AIC, or cross-validation penalize model complexity. The deeper issue is conceptual: a model with 20 predictors and 25 observations is fitting noise, not signal. The rule of thumb is roughly 10–20 observations per predictor for stable estimates. When in doubt, prefer the simpler model that captures the essential relationships without chasing every fluctuation in the data.
