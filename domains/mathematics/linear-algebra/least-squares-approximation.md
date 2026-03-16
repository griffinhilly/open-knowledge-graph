---
id: least-squares-approximation
title: Least Squares Approximation and Normal Equations
domain: mathematics
course: linear-algebra
prerequisites:
- id: gram-schmidt-process
  type: hard
- id: systems-of-linear-equations
  type: hard
tags:
- least squares
- approximation
- normal equations
stage: formal-systems
status: draft
---

# Least Squares Approximation and Normal Equations

## Core Idea
For an inconsistent system Ax = b, the least squares solution minimizes ||Ax − b||². The solution satisfies A^T Ax = A^T b (the normal equations), giving x̂ = (A^T A)^{-1} A^T b when A has full column rank. Least squares finds the best approximation when exact solutions don't exist, essential in statistics and data fitting.

## Explainer

Most real-world systems are overdetermined: you have more equations than unknowns, and no single solution satisfies all of them simultaneously. Think of fitting a line to 100 data points — the line can't pass exactly through every point, so you want the line that comes as close as possible to all of them. This is exactly what least squares does. When Ax = b has no solution, least squares asks: what vector x̂ makes Ax̂ as close to b as possible, measured by the Euclidean distance ||Ax − b||?

The answer has a beautiful geometric interpretation rooted in the Gram-Schmidt work you've already done. The matrix A's columns span a subspace (the column space of A). The vector b may not lie in that subspace — that's precisely why the system is inconsistent. The best approximation Ax̂ is the **orthogonal projection** of b onto the column space of A. The residual vector b − Ax̂ must be perpendicular to every column of A. Writing this orthogonality condition as A^T(b − Ax̂) = 0 immediately yields the **normal equations**: A^T Ax̂ = A^T b. This is a square, solvable system even when the original was not.

When A has full column rank (its columns are linearly independent), A^T A is invertible and the unique solution is x̂ = (A^T A)^{-1} A^T b. The matrix (A^T A)^{-1} A^T is called the **pseudoinverse** of A. In statistics, this formula underlies ordinary least squares regression: if you set up the matrix A with a column of ones and a column of predictor values, the least squares solution gives you the intercept and slope of the best-fit line. The geometry — projecting b onto the column space — makes clear why this works and what "best" means precisely.

When A does not have full column rank (columns are linearly dependent), the normal equations still have solutions but the solution is not unique. In practice this signals a redundant predictor in a regression model. The Gram-Schmidt process you studied provides one route to handling this: QR decomposition factors A = QR, after which the normal equations simplify to Rx̂ = Q^T b, which is easy to solve by back-substitution. This is numerically preferable to forming A^T A directly, since squaring the matrix doubles the condition number and amplifies floating-point errors.
