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
status: validated
---

# Dummy Variables and Categorical Regressors

## Core Idea
A dummy (indicator) variable takes values 0 or 1 to represent group membership, allowing categorical variables to enter linear regression. The coefficient on a dummy captures the mean difference in y between that group and the omitted reference group, holding all other regressors constant. For a variable with k categories, include k−1 dummies to avoid perfect multicollinearity (the dummy variable trap). Interaction terms between a dummy and a continuous variable allow the slope on the continuous variable to differ across groups, enabling tests of whether relationships are heterogeneous.

## How It's Best Learned
Run a gender wage gap regression with and without control variables to see how the dummy coefficient changes — this illustrates both interpretation and the role of controls in reducing omitted variable bias.

## Common Misconceptions
- Including all k dummies creates perfect multicollinearity with the intercept (dummy variable trap) — always drop one.
- The reference category matters for the coefficient values but not for the implied predicted means or their differences.

## Explainer

A **dummy variable** (also called an indicator variable) is a 0/1 switch that lets categorical information enter a regression. Suppose you want to know whether women earn less than men, controlling for education and experience. You can't use "gender" directly as a number — it has no natural scale. Instead, you create a variable that equals 1 if female and 0 if male. The OLS regression then estimates a separate intercept shift for the female group: the coefficient on the dummy tells you the average wage gap, holding education and experience constant. This is the core insight — the dummy converts a group membership question into a coefficient interpretation you already know from multiple regression.

The **reference category** is the group coded as 0, and every dummy coefficient is interpreted as a difference *relative to that baseline*. If you have three education categories — high school, college, and graduate — you'd include two dummies and leave one out. The omitted category becomes the reference. A coefficient of +$15,000 on the college dummy means college graduates earn $15,000 more on average than high school graduates (the reference), holding other variables constant. You could make any category the reference; the predicted values and group differences don't change, only the coefficient labels.

The **dummy variable trap** is what happens when you include all k dummies for a k-category variable. Each observation must belong to exactly one category, so the dummies always sum to 1 — exactly equal to the intercept column. This perfect multicollinearity means the matrix (X'X) cannot be inverted, and OLS has no unique solution. The fix is mechanical: always omit one category. This is not a data problem — it's a modeling rule. Software packages typically drop a category automatically, but you should know which one was dropped to interpret coefficients correctly.

**Interaction terms** extend dummy variables into testing whether the *slope* of a continuous variable differs across groups. If you interact the female dummy with years of education, the interaction coefficient estimates how much the return to education differs for women versus men. A positive interaction means education pays off more for women; a negative one means less. Without the interaction, your model assumes the slope on education is identical for both groups — the dummy only shifts the intercept. With the interaction, you allow the line itself to have a different angle. This is a powerful generalization: the dummy controls for level differences, while the interaction term captures heterogeneous relationships, enabling you to test whether any relationship you've estimated is the same across groups.
