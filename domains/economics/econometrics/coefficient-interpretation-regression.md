---
id: coefficient-interpretation-regression
title: Interpreting Regression Coefficients
domain: economics
course: econometrics
prerequisites:
- id: multiple-regression-model
  type: hard
- id: logarithms-intro
  type: soft
builds-toward:
- hypothesis-testing-regression
- dummy-variables-regression
tags:
- interpretation
- log-linear
- elasticity
- ceteris-paribus
stage: formal-systems
status: validated
---

# Interpreting Regression Coefficients

## Core Idea
The interpretation of a regression coefficient depends on the functional form. In a level-level model (y on x), β₁ gives the change in y per unit change in x. In a log-level model (log y on x), 100·β₁ gives the approximate percentage change in y per unit change in x. In a log-log model, β₁ is the elasticity — the percentage change in y per 1% change in x. Dummy variable coefficients compare a group mean to the omitted reference group, holding other covariates constant. Correct interpretation always includes the ceteris paribus qualifier.

## How It's Best Learned
Practice translating coefficient estimates into plain-language economic statements across different functional forms. The wage-education regression in log form is a canonical exercise.

## Common Misconceptions
- A coefficient of 0.05 in a log-level regression means a 5 percentage point change, not a 5% change — the distinction matters for large effects.
- Standardized beta coefficients answer a different question than raw coefficients; mixing them up leads to incorrect comparisons.

## Questions

```yaml
- question: "A researcher runs a log-level regression of log(wages) on years of education and finds β₁ = 0.12. What is the correct interpretation?"
  type: multiple-choice
  options:
    - "Each additional year of education increases wages by $0.12"
    - "Each additional year of education is associated with approximately a 12% increase in wages, holding other factors constant"
    - "Each 1% increase in education is associated with a 12% increase in wages"
    - "Each additional year of education increases wages by 12 percentage points"
  answer: 1
  explanation: "In a log-level model (log Y on X), the coefficient gives the approximate percentage change in Y per unit increase in X — not a dollar change, not a percentage-point change, and not an elasticity. The '100 × β₁' rule applies: 100 × 0.12 = 12% per year of schooling. Option A describes a level-level coefficient. Option C describes a log-log (elasticity) interpretation. Option D confuses percentage change with percentage-point change — a critical distinction when effects are large."

- question: "Two models both show β₁ = 0.05. Model A has log(price) on log(quantity). Model B has log(price) on quantity in units. How do the interpretations differ?"
  type: multiple-choice
  options:
    - "Both say a 1-unit increase in X raises log(price) by 5%"
    - "Model A says a 1% increase in quantity is associated with a 5% change in price (elasticity); Model B says a 1-unit increase in quantity is associated with approximately a 5% change in price"
    - "Model A says a 5% change in quantity raises price by 5 percentage points; Model B says a 1-unit change raises price by 5%"
    - "There is no difference — the same coefficient value always has the same interpretation"
  answer: 1
  explanation: "Functional form determines interpretation. In a log-log model (both variables in logs), β₁ is an elasticity: a 1% change in X is associated with a β₁% change in Y. In a log-level model (log Y, X in levels), β₁ gives the approximate percentage change in Y per one-unit change in X. Even though both coefficients equal 0.05, they measure completely different things. Reading them interchangeably would produce incorrect economic conclusions."

- question: "A coefficient of 0.08 in a log-level regression means wages rise by 8 percentage points for a one-unit increase in the regressor."
  type: true-false
  answer: false
  explanation: "In a log-level model, the coefficient gives an approximate percentage change, not a percentage-point change. The two are different concepts: a percentage change is relative to the starting level (wages rise by 8% of their current value), while a percentage-point change is an absolute change in a rate. The distinction matters most for large effects — a 0.30 coefficient does not mean wages rise by 30 percentage points; it means wages rise by approximately 30% from their baseline level, which in dollar terms depends on starting wages."

- question: "In a multiple regression, every coefficient must be interpreted as a ceteris paribus effect — the change in Y associated with a one-unit change in that regressor while all other regressors are held constant."
  type: true-false
  answer: true
  explanation: "The ceteris paribus qualifier is not optional — it is what distinguishes a regression coefficient from a simple correlation. A raw correlation between education and wages conflates the effect of education with the effects of ability, family background, and other correlated variables. The regression coefficient isolates the education effect by holding the other included variables constant. Dropping the qualifier means you are misrepresenting what the coefficient actually estimates."

- question: "Why does the interpretation of a regression coefficient change fundamentally depending on whether the outcome variable Y is in levels or in logs? What does the log transformation change about what the coefficient measures?"
  type: short-answer
  answer: "In a level-level model, the coefficient measures an absolute change: β₁ units of Y per unit of X. When Y is log-transformed, the coefficient instead measures a proportional change: approximately 100β₁ percent change in Y per unit of X. This is because a one-unit change in log(Y) corresponds to a percentage change in Y itself — log differences are approximately proportional differences for small changes. The log transformation shifts the model from measuring 'how many more dollars' to 'how many more percent,' which is often more economically natural for variables that grow multiplicatively, like wages or prices."
  explanation: "The key insight is that the coefficient always measures the relationship between the transformed variables, and log(Y) is a different variable than Y. The choice of transformation is a substantive modeling decision about what kind of relationship you believe exists — additive (level) or multiplicative (log) — and it determines what your estimates mean."
```

## Explainer

You already know that a multiple regression coefficient captures the relationship between one regressor and the outcome after holding all other regressors constant — the **ceteris paribus** effect. Now the question is: what units is that effect expressed in? The answer depends entirely on how you have transformed your variables, and getting this wrong turns a correct regression into a meaningless number.

In a **level-level model** — both Y and X in their natural units — the coefficient β₁ is the simplest case: a one-unit increase in X is associated with a β₁-unit change in Y. If wages (in dollars per hour) are regressed on years of education, a coefficient of 1.50 means an additional year of education predicts $1.50 more per hour. Straightforward. The level-level model is the right baseline interpretation to understand before the log transformations.

Log transformations change the units from levels to percentages, which is often more natural for economic variables that grow proportionally. In a **log-level model** (log Y on X, X still in levels), the coefficient β₁ means that a one-unit increase in X is associated with approximately a 100·β₁ percent change in Y. If log wages are regressed on years of education and β₁ = 0.08, then each additional year of schooling raises wages by roughly 8%. This approximation is exact for small changes but overstates the true percentage for large β values. In a **log-log model** (both in logs), β₁ is the **elasticity**: a 1% increase in X is associated with a β₁ percent change in Y. Log-log models appear constantly in demand analysis precisely because elasticity is the natural unit there.

**Dummy variable** coefficients follow the level-level rule but have a specific meaning: the coefficient compares the group mean of the dummy-coded group to the **reference group** (the omitted category), holding everything else constant. If you include a Female indicator in a wage regression and the coefficient is −0.12 in a log-level model, this says women earn approximately 12% less than men after controlling for the other variables in the model. The choice of reference group is arbitrary but affects which comparisons are directly readable from the output. Every interpretation must end with "holding other covariates constant" — without that qualifier, you are not reading a ceteris paribus effect; you are reading something else entirely.
