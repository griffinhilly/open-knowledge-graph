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
- id: column-space
  type: hard
- id: gram-schmidt-orthogonalization
  type: soft
- id: kernel-and-image
  type: soft
- id: orthogonal-projections
  type: hard
tags:
- least squares
- approximation
- normal equations
stage: formal-systems
status: validated
---

# Least Squares Approximation and Normal Equations

## Core Idea
For an inconsistent system Ax = b, the least squares solution minimizes ||Ax − b||². The solution satisfies A^T Ax = A^T b (the normal equations), giving x̂ = (A^T A)^{-1} A^T b when A has full column rank. Least squares finds the best approximation when exact solutions don't exist, essential in statistics and data fitting.

## Questions

```yaml
- question: "You have 100 data points and want to fit a line y = mx + c. Setting up the equation for each point gives a 100×2 system Ax = b. Why can't you solve this system exactly?"
  type: multiple-choice
  options:
    - "The system is underdetermined — with only 2 unknowns and 100 equations, there are infinitely many solutions"
    - "The system is overdetermined — with 100 equations and 2 unknowns, no single line can pass through all 100 points exactly (unless they are perfectly collinear)"
    - "The system cannot be solved because A is not a square matrix"
    - "The system can always be solved exactly; least squares is just an optimization technique for speed"
  answer: 1
  explanation: "With 100 equations and 2 unknowns, the system is overdetermined: there are far more constraints than degrees of freedom. Unless all 100 data points happen to lie exactly on a single line (an almost impossible coincidence with real data), no single pair (m, c) satisfies all 100 equations simultaneously — the system is inconsistent. Least squares finds the best approximate solution by minimizing the total squared error. Option A confuses 'more equations than unknowns' with underdetermination (more unknowns than equations). Option C is true but not the reason — non-square matrices can still have exact solutions if the system is consistent."

- question: "What is the geometric interpretation of the least squares solution x̂ to an inconsistent system Ax = b?"
  type: multiple-choice
  options:
    - "x̂ minimizes the number of equations that are violated"
    - "x̂ is the vector such that Ax̂ is the orthogonal projection of b onto the column space of A"
    - "x̂ is the midpoint between the closest two exact solutions"
    - "x̂ minimizes the maximum error across all equations"
  answer: 1
  explanation: "The column space of A is the set of all vectors Ax can produce. Since b is not in this subspace (the system is inconsistent), the best approximation Ax̂ is the point in the column space closest to b — its orthogonal projection. The residual b − Ax̂ is then perpendicular to the column space, which is why every column of A is orthogonal to the residual. This orthogonality condition, written as A^T(b − Ax̂) = 0, immediately gives the normal equations A^TAx̂ = A^Tb. Option D describes the minimax criterion (used in L∞ optimization), not least squares."

- question: "In the least squares solution to Ax = b, the residual vector b − Ax̂ is orthogonal to every column of A."
  type: true-false
  answer: true
  explanation: "This is the fundamental geometric fact that generates the normal equations. The least squares solution Ax̂ is the orthogonal projection of b onto the column space of A. By definition of orthogonal projection, the vector from the projected point back to b — the residual b − Ax̂ — must be perpendicular to everything in the column space, including each column of A. Writing this as A^T(b − Ax̂) = 0 gives A^TAx̂ = A^Tb: the normal equations. The entire derivation of least squares follows from this one orthogonality condition."

- question: "Computing the normal equations by forming A^TA directly is generally numerically preferable to using QR decomposition because it reduces the size of the matrix."
  type: true-false
  answer: false
  explanation: "Forming A^TA directly is numerically inferior to QR decomposition. The condition number of A^TA is the square of the condition number of A — meaning floating-point errors are amplified. If A is already ill-conditioned, A^TA can be catastrophically inaccurate. QR decomposition factors A = QR, reducing the normal equations to the well-conditioned triangular system Rx̂ = Q^Tb, solvable by back-substitution without squaring the condition number. The normal equation form A^TAx̂ = A^Tb is conceptually cleaner for understanding why least squares works, but in practice QR is the numerically stable method."

- question: "Why do the normal equations A^TAx̂ = A^Tb always have at least one solution, even when the original system Ax = b has none?"
  type: short-answer
  answer: "The normal equations are derived by multiplying both sides of Ax = b by A^T. The resulting system A^TAx̂ = A^Tb is always consistent because A^Tb always lies in the column space of A^TA. Geometrically: the right-hand side A^Tb is always reachable by the matrix A^TA. More directly, the normal equations express the orthogonality condition that the residual b − Ax̂ be perpendicular to the column space of A — and there is always at least one point in the column space closest to any given vector b. When A has full column rank, A^TA is invertible and the solution is unique; when A has linearly dependent columns, there are infinitely many solutions but at least one always exists."
  explanation: "The key insight is that going from Ax = b (inconsistent) to A^TAx̂ = A^Tb (always consistent) is not a coincidence — it is precisely the point of the construction. Multiplying by A^T projects the equation into a space where it can always be satisfied. The geometric language makes this clearest: 'find the projection of b onto the column space of A' always has an answer (the projection always exists), even when 'find x such that Ax = b exactly' does not."
```

## Explainer

Most real-world systems are overdetermined: you have more equations than unknowns, and no single solution satisfies all of them simultaneously. Think of fitting a line to 100 data points — the line can't pass exactly through every point, so you want the line that comes as close as possible to all of them. This is exactly what least squares does. When Ax = b has no solution, least squares asks: what vector x̂ makes Ax̂ as close to b as possible, measured by the Euclidean distance ||Ax − b||?

The answer has a beautiful geometric interpretation rooted in the Gram-Schmidt work you've already done. The matrix A's columns span a subspace (the column space of A). The vector b may not lie in that subspace — that's precisely why the system is inconsistent. The best approximation Ax̂ is the **orthogonal projection** of b onto the column space of A. The residual vector b − Ax̂ must be perpendicular to every column of A. Writing this orthogonality condition as A^T(b − Ax̂) = 0 immediately yields the **normal equations**: A^T Ax̂ = A^T b. This is a square, solvable system even when the original was not.

When A has full column rank (its columns are linearly independent), A^T A is invertible and the unique solution is x̂ = (A^T A)^{-1} A^T b. The matrix (A^T A)^{-1} A^T is called the **pseudoinverse** of A. In statistics, this formula underlies ordinary least squares regression: if you set up the matrix A with a column of ones and a column of predictor values, the least squares solution gives you the intercept and slope of the best-fit line. The geometry — projecting b onto the column space — makes clear why this works and what "best" means precisely.

When A does not have full column rank (columns are linearly dependent), the normal equations still have solutions but the solution is not unique. In practice this signals a redundant predictor in a regression model. The Gram-Schmidt process you studied provides one route to handling this: QR decomposition factors A = QR, after which the normal equations simplify to Rx̂ = Q^T b, which is easy to solve by back-substitution. This is numerically preferable to forming A^T A directly, since squaring the matrix doubles the condition number and amplifies floating-point errors.
