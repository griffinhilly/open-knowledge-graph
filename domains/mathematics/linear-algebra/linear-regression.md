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
status: draft
---

# Linear Regression and Least Squares Estimation

## Core Idea
Linear regression fits a model y = Xβ + ε to data by minimizing ||y − Xβ||². The optimal coefficients are β* = (XᵀX)⁻¹Xᵀy (normal equations), found via orthogonal projection of y onto the column space of X. Residuals r = y − Xβ* are orthogonal to the fitted subspace. QR decomposition is preferred numerically over normal equations for stability.
