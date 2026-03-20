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

## Explainer

**Ordinary least squares (OLS)** finds the line (or hyperplane) through data that minimizes the total squared distance between observed outcomes and predicted values. You already know from bivariate regression that this produces a fitted line ŷ = β₀ + β₁x; what this topic adds is the formal derivation in matrix notation and a deeper understanding of why squared residuals — rather than absolute values or fourth powers — are the natural loss function to minimize.

The matrix setup replaces a column of numbers with compact notation. Stack all your observations into an n×k matrix **X** (rows are observations, columns are variables including a constant), stack your outcomes into an n×1 vector **y**, and write the model as **y = Xβ + ε**. The OLS objective is to choose β to minimize the scalar (y − Xβ)'(y − Xβ) — the sum of squared residuals. Taking the derivative with respect to β and setting it to zero gives the **normal equations**: X'Xβ = X'y. Solving these yields the OLS estimator: **β̂ = (X'X)⁻¹X'y**. This closed-form solution is what makes OLS analytically tractable — many other estimators require iterative numerical methods.

The geometric interpretation, which your linear algebra prerequisite prepared you for, is illuminating. OLS projects the vector **y** onto the column space of **X**. The fitted values **ŷ = Xβ̂** are the orthogonal projection of y onto that subspace, and the residuals **ê = y − ŷ** are perpendicular to every column of X (X'ê = 0 by construction). This orthogonality condition is not just a mathematical curiosity — it is the foundation for understanding what the OLS assumptions actually require. When the OLS assumptions hold, this projection has desirable properties; when they fail, the projection is still well-defined geometrically, but the statistical interpretation breaks down.

A critical point that addresses a common misconception: minimizing squared residuals *mechanically* always produces a solution, but that solution has good statistical properties (unbiasedness, consistency) only when the assumptions from your OLS prerequisite are satisfied — especially that the regressors are uncorrelated with the error term (E[X'ε] = 0). OLS is a procedure; the **Gauss-Markov theorem** (which this topic builds toward) is the theorem that says, *given* those assumptions, OLS is the Best Linear Unbiased Estimator. You can run OLS on any data. Whether the coefficients mean what you think they mean depends entirely on whether the world cooperates with the assumptions.
