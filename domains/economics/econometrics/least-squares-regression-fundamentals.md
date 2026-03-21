---
id: least-squares-regression-fundamentals
title: 'Least Squares Regression: Fundamentals and Derivation'
domain: economics
course: econometrics
prerequisites:
- id: bivariate-regression
  type: hard
- id: ols-assumptions
  type: hard
- id: linear-algebra
  type: hard
- id: matrix-operations
  type: hard
- id: least-squares-approximation
  type: hard
- id: optimization-multivariable-basics
  type: soft
- id: linear-transformation-matrix-representation
  type: soft
- id: linear-regression
  type: soft
builds-toward:
- gauss-markov-theorem-ols
- estimator-consistency-unbiasedness
tags:
- ols
- estimation
- regression
stage: advanced
status: draft
---

# Least Squares Regression: Fundamentals and Derivation

## Core Idea
Ordinary least squares (OLS) minimizes the sum of squared residuals to estimate regression coefficients. The OLS estimator has a closed-form solution and is the foundation of econometric analysis, with well-understood statistical properties that depend on assumptions about the data-generating process.

## How It's Best Learned
Work through matrix-form derivations minimizing the sum of squared residuals. Compare OLS to other loss functions and see why quadratic loss leads to the least squares solution.

## Common Misconceptions
OLS does not require normally distributed errors (normality is only needed for exact inference), and minimizing squared residuals alone does not ensure unbiasedness—additional assumptions about regressors are required.

## Questions

```yaml
- question: "A researcher runs OLS regression and obtains coefficient estimates. What determines whether these estimates are unbiased?"
  type: multiple-choice
  options:
    - "Whether the residuals are normally distributed — OLS requires normality for unbiasedness"
    - "Whether the sample size is large enough — large samples correct for any violations of assumptions"
    - "Whether the regressors are uncorrelated with the error term — E[X'ε] = 0 in the population"
    - "Whether the sum of squared residuals is at its global minimum — achieving the OLS objective guarantees unbiasedness"
  answer: 2
  explanation: "OLS mechanically always minimizes squared residuals — that is what it does by definition. But this mechanical minimization yields unbiased estimates only when the key exogeneity assumption holds: E[X'ε] = 0, meaning regressors are uncorrelated with the error term. If regressors are correlated with the error (omitted variable bias, simultaneity, measurement error), OLS estimates are biased regardless of sample size or residual distribution. Normality is only needed for exact small-sample inference, not for unbiasedness itself."

- question: "A student regresses exam scores on study hours and writes: 'Since I minimized the sum of squared residuals, my OLS estimates must be unbiased.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — minimizing squared residuals always guarantees unbiased coefficient estimates"
    - "OLS should minimize absolute residuals, not squared residuals, to achieve unbiasedness"
    - "Minimizing squared residuals ensures the estimator is a valid projection, but whether it is unbiased depends on whether the OLS assumptions hold in the data-generating process"
    - "The student should use the normal equations directly rather than the closed-form OLS formula"
  answer: 2
  explanation: "This is the core misconception the topic targets. OLS always finds the projection minimizing squared residuals — this is a mathematical fact about the procedure, independent of the data. But achieving the minimum says nothing about whether the underlying assumptions hold. If student ability (an omitted variable correlated with study hours) is not in the model, the coefficient on study hours will be biased — the OLS formula still runs and produces numbers, but those numbers don't estimate what the student thinks they do. The Gauss-Markov theorem, not the minimization itself, is what establishes unbiasedness under the right conditions."

- question: "OLS can always be computed and will always minimize the sum of squared residuals, regardless of whether the OLS assumptions hold."
  type: true-false
  answer: true
  explanation: "OLS is a mechanical procedure. Given any X and y (assuming X'X is invertible), β̂ = (X'X)⁻¹X'y always produces numbers, and those numbers always minimize the sum of squared residuals — this is a property of the formula, not of the data-generating process. What the OLS assumptions determine is not whether you can run OLS, but whether the resulting estimates have desirable statistical properties (unbiasedness, consistency) as estimates of the true population parameters. You can always run OLS; what you cannot always do is trust what it produces."

- question: "OLS requires normally distributed errors in order to produce unbiased coefficient estimates."
  type: true-false
  answer: false
  explanation: "Normality of errors is NOT required for OLS unbiasedness. The estimator is unbiased whenever E[X'ε] = 0 and other basic conditions hold — none of which involve normality. Normality is only invoked for exact small-sample inference: to construct exact t-statistics and F-statistics from OLS estimates, we assume normal errors. With large samples, the Central Limit Theorem provides asymptotic normality of the coefficient estimates even if errors are non-normal. Many textbooks introduce normality early, leading students to incorrectly conclude it is required for the estimator itself."

- question: "Why does the geometric interpretation of OLS — projecting y onto the column space of X — clarify what the OLS assumptions are actually doing?"
  type: short-answer
  answer: "OLS geometrically projects y onto the column space of X, producing fitted values ŷ and residuals ê that are always orthogonal to every column of X (X'ê = 0) — a mathematical fact that holds by construction. But the OLS assumption E[X'ε] = 0 in the population says that the true error is uncorrelated with the regressors, which is what makes this sample orthogonality a reliable guide to the population relationship. If the true error is correlated with X, the projection is still geometrically valid and orthogonal in the sample, but ê is a biased estimate of the true ε — the projection points in the wrong direction in parameter space."
  explanation: "The geometric picture shows that OLS always finds the closest point in the column space, but 'closest' is only 'correct' when the column space is the right subspace — which requires the exogeneity assumption. This makes the assumptions interpretable: they are not arbitrary technical conditions but the requirements for the projection to be meaningful as an estimate of the true parameters."
```

## Explainer

**Ordinary least squares (OLS)** finds the line (or hyperplane) through data that minimizes the total squared distance between observed outcomes and predicted values. You already know from bivariate regression that this produces a fitted line ŷ = β₀ + β₁x; what this topic adds is the formal derivation in matrix notation and a deeper understanding of why squared residuals — rather than absolute values or fourth powers — are the natural loss function to minimize.

The matrix setup replaces a column of numbers with compact notation. Stack all your observations into an n×k matrix **X** (rows are observations, columns are variables including a constant), stack your outcomes into an n×1 vector **y**, and write the model as **y = Xβ + ε**. The OLS objective is to choose β to minimize the scalar (y − Xβ)'(y − Xβ) — the sum of squared residuals. Taking the derivative with respect to β and setting it to zero gives the **normal equations**: X'Xβ = X'y. Solving these yields the OLS estimator: **β̂ = (X'X)⁻¹X'y**. This closed-form solution is what makes OLS analytically tractable — many other estimators require iterative numerical methods.

The geometric interpretation, which your linear algebra prerequisite prepared you for, is illuminating. OLS projects the vector **y** onto the column space of **X**. The fitted values **ŷ = Xβ̂** are the orthogonal projection of y onto that subspace, and the residuals **ê = y − ŷ** are perpendicular to every column of X (X'ê = 0 by construction). This orthogonality condition is not just a mathematical curiosity — it is the foundation for understanding what the OLS assumptions actually require. When the OLS assumptions hold, this projection has desirable properties; when they fail, the projection is still well-defined geometrically, but the statistical interpretation breaks down.

A critical point that addresses a common misconception: minimizing squared residuals *mechanically* always produces a solution, but that solution has good statistical properties (unbiasedness, consistency) only when the assumptions from your OLS prerequisite are satisfied — especially that the regressors are uncorrelated with the error term (E[X'ε] = 0). OLS is a procedure; the **Gauss-Markov theorem** (which this topic builds toward) is the theorem that says, *given* those assumptions, OLS is the Best Linear Unbiased Estimator. You can run OLS on any data. Whether the coefficients mean what you think they mean depends entirely on whether the world cooperates with the assumptions.
