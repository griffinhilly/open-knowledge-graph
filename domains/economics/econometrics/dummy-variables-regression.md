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

## Questions

```yaml
- question: "You are estimating a wage regression with a 4-category variable: season of birth (spring, summer, fall, winter). How many dummy variables should you include, and why?"
  type: multiple-choice
  options:
    - "4 dummies — one for each season, to capture each season's full effect"
    - "3 dummies — include all but one, which becomes the reference category"
    - "2 dummies — one for each pair of seasons (spring/summer vs. fall/winter)"
    - "1 dummy — a single variable can encode all 4 categories using values 0, 1, 2, 3"
  answer: 1
  explanation: "For a k-category variable, include k−1 = 3 dummies. Including all 4 creates perfect multicollinearity: the four dummy columns always sum to 1, exactly matching the intercept column, making (X'X) singular and OLS unsolvable — the dummy variable trap. The omitted season becomes the reference category; each included dummy's coefficient measures the wage difference from that reference. A single numeric variable (0, 1, 2, 3) would incorrectly impose an ordering and equal spacing between seasons."

- question: "A wage regression includes a female dummy D (1=female, 0=male) and years of education. The interaction term D × Education has a coefficient of +$800. What does this mean?"
  type: multiple-choice
  options:
    - "Women earn $800 more than men on average, regardless of education"
    - "Each additional year of education is worth $800 for both men and women"
    - "Each additional year of education is worth $800 more for women than for men"
    - "The gender wage gap closes by $800 for each year of education women complete"
  answer: 2
  explanation: "An interaction term D × Education allows the slope on education to differ by gender. The coefficient on the interaction (+$800) means that for women (D=1), each additional year of education raises wages by $800 more than it does for men (D=0). The main dummy coefficient still captures the baseline intercept difference (gender gap at zero education), while the interaction captures slope heterogeneity. Without the interaction, the model would force the return to education to be identical for both groups."

- question: "Including most k dummy variables for a k-category variable alongside an intercept term is fine in OLS regression, as long as your software is modern enough to handle the multicollinearity."
  type: true-false
  answer: false
  explanation: "This is the dummy variable trap. The k dummies always sum to 1 for every observation — identically equal to the intercept column (which is a column of 1s). This is perfect, not merely high, multicollinearity: the matrix X'X is literally singular and cannot be inverted. OLS has no unique solution. This is not a computational problem that better software can overcome — it is a mathematical impossibility. The fix is always to drop one category. Software packages handle this automatically, but understanding the underlying reason is essential for correctly interpreting which category was omitted."

- question: "Changing the reference category in a dummy variable regression changes the fitted values and the predicted mean outcomes for each group."
  type: true-false
  answer: false
  explanation: "The choice of reference category is arbitrary and affects only the coefficient labels, not the model's predictions or implied group means. Switching from 'high school' to 'college' as the reference changes which group the other coefficients are measured against, but the predicted wage for every individual and the implied mean for every group remain identical. The differences between groups are exactly the same regardless of reference category — what changes is only the baseline from which differences are expressed. This is why the reference choice is a labeling convention, not a substantive modeling decision."

- question: "What is the 'dummy variable trap,' and why does it make OLS estimation mathematically impossible?"
  type: short-answer
  answer: "The dummy variable trap occurs when all k dummies for a k-category variable are included along with an intercept. Because every observation belongs to exactly one category, the dummy values always sum to 1 — identical to the intercept column. This creates perfect multicollinearity: one column of the design matrix X is an exact linear combination of others. The matrix X'X becomes singular (non-invertible), so the OLS formula β̂ = (X'X)⁻¹X'y has no solution. The fix is to always omit one category, making it the reference group against which all others are measured."
  explanation: "Understanding the dummy variable trap matters because it explains the k−1 rule at a deeper level than 'just drop one.' It also helps with more complex settings: any time a set of variables must sum to a constant (like shares that sum to 1, or time dummies plus a constant), the same issue arises. Recognizing perfect multicollinearity as a structural feature of the design — not a data quality problem — lets you diagnose and fix it correctly."
```

## Explainer

A **dummy variable** (also called an indicator variable) is a 0/1 switch that lets categorical information enter a regression. Suppose you want to know whether women earn less than men, controlling for education and experience. You can't use "gender" directly as a number — it has no natural scale. Instead, you create a variable that equals 1 if female and 0 if male. The OLS regression then estimates a separate intercept shift for the female group: the coefficient on the dummy tells you the average wage gap, holding education and experience constant. This is the core insight — the dummy converts a group membership question into a coefficient interpretation you already know from multiple regression.

The **reference category** is the group coded as 0, and every dummy coefficient is interpreted as a difference *relative to that baseline*. If you have three education categories — high school, college, and graduate — you'd include two dummies and leave one out. The omitted category becomes the reference. A coefficient of +$15,000 on the college dummy means college graduates earn $15,000 more on average than high school graduates (the reference), holding other variables constant. You could make any category the reference; the predicted values and group differences don't change, only the coefficient labels.

The **dummy variable trap** is what happens when you include all k dummies for a k-category variable. Each observation must belong to exactly one category, so the dummies always sum to 1 — exactly equal to the intercept column. This perfect multicollinearity means the matrix (X'X) cannot be inverted, and OLS has no unique solution. The fix is mechanical: always omit one category. This is not a data problem — it's a modeling rule. Software packages typically drop a category automatically, but you should know which one was dropped to interpret coefficients correctly.

**Interaction terms** extend dummy variables into testing whether the *slope* of a continuous variable differs across groups. If you interact the female dummy with years of education, the interaction coefficient estimates how much the return to education differs for women versus men. A positive interaction means education pays off more for women; a negative one means less. Without the interaction, your model assumes the slope on education is identical for both groups — the dummy only shifts the intercept. With the interaction, you allow the line itself to have a different angle. This is a powerful generalization: the dummy controls for level differences, while the interaction term captures heterogeneous relationships, enabling you to test whether any relationship you've estimated is the same across groups.
