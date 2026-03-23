---
id: linear-regression
title: Linear Regression and Least Squares Estimation
domain: mathematics
course: linear-algebra
prerequisites:
- id: orthogonal-projections-least-squares
  type: hard
tags:
- linear-regression
- least-squares
- statistics
- applications
stage: formal-systems
status: validated
---

# Linear Regression and Least Squares Estimation

## Core Idea
Linear regression fits a model y = Xβ + ε to data by minimizing ||y − Xβ||². The optimal coefficients are β* = (XᵀX)⁻¹Xᵀy (normal equations), found via orthogonal projection of y onto the column space of X. Residuals r = y − Xβ* are orthogonal to the fitted subspace. QR decomposition is preferred numerically over normal equations for stability.

## Questions

```yaml
- question: "In the linear algebra view of regression, the fitted values ŷ = Xβ* are best described as:"
  type: multiple-choice
  options: ["The average of the observed response values", "The orthogonal projection of y onto the column space of X", "The maximum-likelihood estimate under any error distribution", "The solution minimizing the sum of absolute residuals"]
  answer: 1
  explanation: "The fitted values ŷ = Xβ* = X(XᵀX)⁻¹Xᵀy = Py, where P = X(XᵀX)⁻¹Xᵀ is the orthogonal projection matrix onto col(X). This projection interpretation is the core geometric insight: we find the point in the column space of X closest to y, and the error is the perpendicular distance from y to that subspace."

- question: "Solving the normal equations (XᵀX)β = Xᵀy directly by inverting XᵀX is always the preferred numerical method for computing β* in practice."
  type: true-false
  answer: false
  explanation: "Inverting XᵀX squares the condition number of X, making the calculation numerically unstable when X is near-singular (e.g., when predictors are nearly collinear). QR decomposition of X directly is preferred because it works with the original condition number of X, not its square. Most regression software (R, NumPy's lstsq, etc.) uses QR or SVD internally."

- question: "What geometric property must the residual vector r = y − Xβ* satisfy, and why does this property uniquely define the least-squares solution?"
  type: short-answer
  answer: "The residuals must be orthogonal to every column of X — equivalently, Xᵀr = 0. This is the perpendicularity condition: the minimum-distance point from y to col(X) is the foot of the perpendicular from y to that subspace, so the error vector must point directly away from the subspace."
  explanation: "The condition Xᵀ(y − Xβ*) = 0 is exactly the normal equations rearranged. Any other coefficient vector β would produce a residual with a nonzero component inside col(X), meaning we could reduce ||y − Xβ||² by moving β in that direction — so β* would not be the minimizer. Orthogonality of residuals is both the geometric definition of the projection and the algebraic optimality condition."
```

## Explainer

Linear regression, viewed through linear algebra, is a problem about projection. You have a vector of observations y in ℝⁿ and a matrix X whose columns span a subspace — the column space of X. No vector β will generally make Xβ equal y exactly (the system is overdetermined: more equations than unknowns), so instead you find the β that makes Xβ as close to y as possible. "Closest" means minimizing the Euclidean distance ||y − Xβ||², which is the sum of squared residuals.

The key geometric insight is that the minimizer is the **orthogonal projection** of y onto col(X). From your work on orthogonal projections, you know that the closest point in a subspace to a given vector is the foot of the perpendicular from that vector to the subspace. The fitted values ŷ = Xβ* are exactly that foot, and the residual vector r = y − ŷ is perpendicular to col(X). Algebraically, this perpendicularity condition is Xᵀr = 0, which expands to Xᵀ(y − Xβ*) = 0 and rearranges to the **normal equations**: (XᵀX)β* = Xᵀy. If XᵀX is invertible, β* = (XᵀX)⁻¹Xᵀy.

The matrix P = X(XᵀX)⁻¹Xᵀ is called the **hat matrix** (because ŷ = Py "puts a hat on y"). It is an orthogonal projection matrix: P² = P and Pᵀ = P. The complementary matrix I − P projects onto the orthogonal complement of col(X), and (I − P)y = r is the residual. This decomposition y = ŷ + r = Py + (I − P)y partitions the response into explained variation and unexplained noise — exactly what R² measures.

In practice, computing β* by inverting XᵀX explicitly is avoided. Forming XᵀX squares the condition number of X, making the calculation fragile when predictors are nearly collinear. The preferred approach is **QR decomposition**: write X = QR where Q has orthonormal columns and R is upper triangular. Then β* = R⁻¹Qᵀy, which is numerically stable and requires only back-substitution rather than a matrix inverse. This is what virtually all statistical software computes under the hood when you call a regression function.

One thing to notice: the normal equations β* = (XᵀX)⁻¹Xᵀy look like ordinary division scaled up to matrices — you are "dividing y by X" in a matrix sense. The factor (XᵀX)⁻¹Xᵀ is the **Moore-Penrose pseudoinverse** of X when X has full column rank, and generalizes to all X via SVD. Linear regression is thus not a statistical trick but a straightforward application of projection geometry — the statistics (error distributions, inference, R²) are layered on top of this geometric foundation.
