---
id: ols-assumptions
title: Classical OLS Assumptions (Gauss-Markov)
domain: economics
course: econometrics
prerequisites:
- id: bivariate-regression
  type: hard
- id: expected-value
  type: hard
- id: random-variables-intro
  type: hard
- id: variance-of-random-variables
  type: soft
- id: normal-distribution
  type: soft
builds-toward:
- multiple-regression-model
- heteroskedasticity
- serial-correlation
- omitted-variable-bias
tags:
- Gauss-Markov
- BLUE
- assumptions
- unbiasedness
stage: formal-systems
status: validated
---

# Classical OLS Assumptions (Gauss-Markov)

## Core Idea
The Gauss-Markov theorem states that OLS is the Best Linear Unbiased Estimator (BLUE) when six classical assumptions hold: linearity in parameters, random sampling, no perfect multicollinearity, zero conditional mean of errors (E[u|x]=0), homoskedasticity, and no serial correlation. The most critical assumption is E[u|x]=0, which requires that all determinants of y omitted from the model are uncorrelated with x. When this assumption fails — due to omitted variables, measurement error, or simultaneity — OLS estimates are biased and inconsistent. The remaining assumptions govern efficiency rather than unbiasedness.

## How It's Best Learned
Work through examples of each assumption violation — simulate data with heteroskedastic errors, then see how OLS still estimates coefficients correctly (unbiased) but standard errors are wrong. This separates biasedness from inefficiency.

## Common Misconceptions
- Violating homoskedasticity biases standard errors, not coefficients — a common confusion.
- The 'linearity' assumption applies to parameters (β), not to the functional form of x; including x² is still 'linear in parameters'.

## Questions

```yaml
- question: "A researcher runs OLS and discovers that error variance increases with the level of x (heteroskedasticity). What is the primary consequence for the OLS estimates?"
  type: multiple-choice
  options:
    - "The coefficient estimates β̂ are biased and inconsistent"
    - "The coefficient estimates β̂ are still unbiased, but standard errors are biased, making inference unreliable"
    - "Both coefficients and standard errors are unbiased; only efficiency is lost"
    - "The model must be re-estimated using a different technique because OLS cannot be applied"
  answer: 1
  explanation: "Heteroskedasticity violates the efficiency assumption (homoskedasticity) but does not affect unbiasedness or consistency of the coefficient estimates. The coefficients β̂ are still correct on average. However, OLS standard errors assume constant variance; when variance is non-constant, the computed standard errors are wrong, which invalidates t-tests and confidence intervals. The fix is to use heteroskedasticity-robust standard errors — not to discard OLS."

- question: "If the OLS assumption E[u|x] = 0 is violated due to an omitted variable, the coefficient estimates are still unbiased as long as the sample is large enough."
  type: true-false
  answer: false
  explanation: "E[u|x] = 0 (exogeneity) is required for unbiasedness and consistency. When an omitted variable is correlated with x, it enters the error term u, making u correlated with x and violating this assumption. The resulting omitted variable bias does not shrink as the sample grows — it is a persistent, systematic error. A larger sample just estimates the wrong parameter more precisely. No amount of data can fix a violation of exogeneity."

- question: "The Gauss-Markov theorem says OLS is BLUE. What does each of those four letters mean, and why does the 'unbiased' part depend on a different assumption than the 'best' part?"
  type: short-answer
  answer: "BLUE stands for Best Linear Unbiased Estimator. 'Unbiased' (E[β̂] = β) requires E[u|x] = 0 — the exogeneity assumption. 'Best' (minimum variance among linear unbiased estimators) requires homoskedasticity and no serial correlation. These are governed by separate assumptions, so it is possible to have an unbiased but inefficient estimator (when homoskedasticity fails) or a biased but precise one."
  explanation: "The distinction between unbiasedness and efficiency maps directly onto which assumptions are load-bearing for each property. E[u|x] = 0 is the hardest assumption to satisfy — it rules out omitted variable bias, measurement error in x, and simultaneity — and its failure destroys the fundamental validity of OLS. Homoskedasticity and no serial correlation govern efficiency only: their failure means OLS is no longer the minimum-variance estimator, but coefficients remain interpretable. This is why heteroskedasticity-robust standard errors are a fix that preserves the coefficient estimates while correcting the inference."
```

## Explainer

When you learned bivariate regression, you found a formula that fits a line through data. The Gauss-Markov theorem tells you when that line can be trusted as more than a description of the sample — specifically, when OLS is the Best Linear Unbiased Estimator (BLUE) for the population parameters. Understanding the theorem means understanding which assumptions are doing what.

The six classical assumptions can be grouped by what they protect. The first three — linearity in parameters, random sampling, and no perfect multicollinearity — are structural requirements that make estimation possible at all. If the model is nonlinear in parameters, or if two regressors are perfectly collinear, OLS simply cannot produce a unique solution. These assumptions are often satisfied by construction.

The fourth assumption, E[u|x] = 0, is the most critical and the most likely to fail. It says that the expected value of the error term, conditional on x, is zero — in other words, knowing x tells you nothing about the average size of the unobserved factors in u. This is the exogeneity condition. It fails whenever an omitted variable is correlated with x (omitted variable bias), when x is measured with error (attenuation bias), or when x and y jointly determine each other (simultaneity). When E[u|x] ≠ 0, the coefficient estimates are biased and inconsistent — no amount of additional data will fix the problem.

The fifth and sixth assumptions — homoskedasticity (constant error variance) and no serial correlation — govern efficiency, not unbiasedness. When these fail, OLS remains unbiased and consistent, but it is no longer the minimum-variance estimator among linear unbiased estimators. In practice, heteroskedasticity is extremely common (error variance often grows with income, firm size, or other scale variables), and the fix is straightforward: use heteroskedasticity-robust standard errors. The coefficients themselves are kept; only the standard errors are corrected.

A common confusion arises from the word "linearity" in the first assumption. The linearity requirement applies to the parameters β — the model must be linear in β — not to the functional form of the regressors. A model with x, x², and log(x) on the right-hand side is perfectly linear in parameters and satisfies the assumption. This flexibility means OLS can handle a wide range of nonlinear relationships between y and x, as long as the model remains linear in the unknowns you are estimating.
