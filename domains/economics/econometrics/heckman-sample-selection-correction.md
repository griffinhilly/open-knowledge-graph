---
id: heckman-sample-selection-correction
title: Heckman Sample Selection Correction
domain: economics
course: econometrics
prerequisites:
- id: selection-bias-econometrics
  type: hard
- id: logit-probit-models
  type: hard
- id: maximum-likelihood-econometrics
  type: soft
- id: tobit-censored-regression
  type: soft
builds-toward:
- lifecycle-labor-supply
- occupational-choice
tags:
- sample selection
- Heckman
- inverse Mills ratio
- Heckit
- exclusion restriction
- limited dependent variable
stage: advanced
status: validated
---

# Heckman Sample Selection Correction

## Core Idea
Sample selection arises when the outcome is observed only for units that pass a selection rule related to the outcome's error, as when wages are seen only for people who work. OLS on the selected sample is then biased. James Heckman's 1979 approach models selection with a probit equation and shows that, under joint normality of the two errors, the expected outcome in the selected sample equals xβ plus a term proportional to the inverse Mills ratio, λ(zγ) = φ(zγ)/Φ(zγ). The two-step estimator fits the probit, computes λ̂ for each selected observation, and adds it as a regressor. A credible correction needs at least one variable that affects selection but not the outcome.

## How It's Best Learned
Begin with the married women's wage example: wages exist for everyone but are recorded only for women in the labor force. Ask which women with low potential wages choose not to work and how their absence shifts the observed wage-education relationship. Then derive the selection term from the bivariate normal model and run the two steps in order, checking the t-statistic on λ̂ as a test for selection.

## Common Misconceptions
- Any sample with missing outcomes needs a Heckman correction. (If selection depends only on the regressors x, or is unrelated to the outcome error, OLS on the selected sample remains consistent.)
- The two-step method works well without an exclusion restriction. (Without a variable in the selection equation excluded from the outcome equation, identification rests only on the nonlinear shape of λ, which is close to linear over much of its range, so estimates are often imprecise and fragile.)
- The usual OLS standard errors from the second step are correct. (λ̂ is an estimated regressor, so the standard errors must be adjusted, or the model estimated jointly by maximum likelihood.)

## Questions

```yaml
- question: "In a study of women's wages, the selection equation for labor force participation includes the number of children under age six, but the wage equation does not. What role does this variable play?"
  type: multiple-choice
  options: ["It is an omitted variable that biases the wage equation", "It is the exclusion restriction that helps identify the selection correction", "It replaces the inverse Mills ratio", "It must also be included in the wage equation for consistency"]
  answer: 1
  explanation: "Young children plausibly affect whether a woman works but not the wage she would be offered. Including it in the probit and excluding it from the wage equation gives variation in λ that is not a function of x alone, which is what identifies the correction."
- question: "In the second step of the Heckman procedure, a coefficient on the inverse Mills ratio that is statistically indistinguishable from zero is evidence that sample selection bias is not a serious problem."
  type: true-false
  answer: true
  explanation: "The coefficient on λ̂ equals ρσ, where ρ is the correlation between the selection and outcome errors. If it is zero, selection is not related to the outcome error, and OLS on the selected sample is consistent. A t-test on it is a standard test for selection bias."
- question: "What is the inverse Mills ratio evaluated at zγ?"
  type: multiple-choice
  options: ["Φ(zγ)/φ(zγ)", "φ(zγ)/Φ(zγ)", "1 − Φ(zγ)", "zγ/σ"]
  answer: 1
  explanation: "λ(c) = φ(c)/Φ(c), the standard normal density divided by the standard normal CDF. It is large when the probability of selection is low and falls toward zero as selection becomes nearly certain."
- question: "Explain why OLS on only working women can understate the return to education when selection is positive on the wage error."
  type: short-answer
  answer: "Women with little education work only if their wage error is high enough to make working worthwhile, while highly educated women work even with modest errors. So among workers, the average error is higher at low education than at high education. This raises observed wages at low education relative to high education and flattens the estimated education slope."
  explanation: "The selection term λ is larger for groups with lower participation probabilities, and including it removes this pattern from the error."
```

## Explainer
You have seen that selection bias occurs when the units we observe differ systematically from those we do not. A particular version arises in **sample selection**: the outcome exists for everyone, but we only see it for those who pass some rule. Wages are the standard example. Every adult has a potential wage offer, but we observe wages only for people who work. If the decision to work depends on that potential wage, the working sample is not representative.

James Heckman's 1979 paper treated this as a specification error and proposed a correction; he shared the 2000 Nobel Memorial Prize in Economic Sciences partly for this work. The model has two equations. The outcome equation is y = xβ + u. The selection equation says y is observed when zγ + v > 0, where z includes the variables in x and at least one more. Assume u and v are jointly normal, with v having variance one and correlation ρ with u.

Under these assumptions, the expected outcome among selected units is E(y | x, selected) = xβ + ρσλ(zγ), where σ is the standard deviation of u and λ(c) = φ(c)/Φ(c) is the **inverse Mills ratio**. The second term is the source of bias. When ρ > 0, people with high unobserved wage potential are more likely to work, so the selected sample has a positive average error. That average is larger for groups with low participation probabilities, where λ is large.

The **two-step estimator**, often called Heckit, follows directly. Step one: estimate a probit of participation on z using the full sample, and compute λ̂ = λ(zγ̂) for each selected unit. Step two: regress y on x and λ̂ using the selected sample. The coefficient on x estimates β consistently, and the coefficient on λ̂ estimates ρσ. A t-test of that coefficient tests for selection bias. Because λ̂ is estimated, the second-step standard errors need adjustment. Full maximum likelihood is an alternative.

The most important practical issue is the **exclusion restriction**. If z contains no variable outside x, λ̂ is a function of x alone and is nearly linear over much of its range, so it is highly collinear with x. Good exclusion restrictions affect selection but not the outcome, such as young children or other household income in a model of women's wages. Such variables are debatable, so applied work usually reports how results change with different choices.
